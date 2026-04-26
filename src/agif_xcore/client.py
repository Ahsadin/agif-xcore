"""User-facing synchronous client.

    from agif_xcore import GovernedClient
    client = GovernedClient(
        backend="ollama", model="gemma3:270m",
        governance_enabled=True,
        grounding_paths=["./docs/"],
    )
    answer = client.ask("What does our SOP say about backups?")
    print(answer.text)

M2 adds the full substrate + BM25 grounding. ``governance_enabled=True``
runs the 9-stage governance substrate **through the same code path** as
``governance_enabled=False`` — no two hand-coded arms.

M4 adds cross-turn conversation memory and weak-answer escalation.
Memory entries are stored after each governed turn and injected into
the planner prompt on subsequent turns. Weak-answer diagnosis runs on
extractable features (no LLM call) and optionally retries once.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Sequence

from .answer_mode.realizer_templates import reshape_answer
from .backends.base import BackendError, ModelBackend
from .backends.registry import resolve_backend
from .grounding.bm25 import build_bm25_from_paths
from .grounding.noop import NoOpRetriever
from .memory.store import ConversationMemory
from .meta.escalation import (
    MAX_RETRIES,
    EscalationResult,
    build_retry_messages,
    diagnose_weak_answer,
    should_escalate,
)
from .pipeline.runner import Runner
from .policies.tool_policy import (
    ArgumentDenial,
    ToolPolicy,
    tool_policy_from_allowlist,
)
from .schemas import (
    AnswerEnvelope,
    GroundingBundle,
    SubstrateDecisions,
    TraceEnvelope,
    TurnEnvelope,
    make_conversation_id,
    make_turn_id,
)
from .substrate import run_substrate
from .trace import (
    FileJsonlSink,
    MultiSink,
    NullSink,
    StdoutJsonlSink,
    TraceSink,
    build_trace,
)


class GovernedClient:
    """Synchronous wrapper over a backend + pipeline + substrate + trace.

    ``governance_enabled=True`` activates the 9-stage substrate and the
    answer-mode reshaping. ``governance_enabled=False`` bypasses the
    substrate and returns the raw LLM answer. Both paths share one
    ``ask()`` method — no separate "arms" function.

    M4 additions:
      * ``memory_enabled=True`` stores each governed turn in conversation
        memory and injects prior turns into the planner prompt.
      * ``escalation_enabled=True`` runs weak-answer diagnosis on the
        raw answer and optionally retries once with a tighter prompt.
    """

    def __init__(
        self,
        *,
        backend: str | ModelBackend = "ollama",
        model: str,
        base_url: str | None = None,
        api_key: str | None = None,
        model_enforcement: str = "strict",
        temperature: float = 0.0,
        max_tokens: int | None = None,
        trace_file: str | Path | None = None,
        trace_to_stderr: bool = False,
        governance_enabled: bool = False,
        grounding_paths: Sequence[str | Path] | None = None,
        memory_enabled: bool = True,
        escalation_enabled: bool = False,
        tool_allowlist: Sequence[str] | None = None,
        tool_policy: ToolPolicy | None = None,
    ) -> None:
        if isinstance(backend, str):
            self._backend: ModelBackend = resolve_backend(
                backend,
                base_url=base_url,
                api_key=api_key,
                model_enforcement=model_enforcement,
            )
        else:
            self._backend = backend

        if not model:
            raise ValueError("model is required")
        self._model = model
        self._temperature = float(temperature)
        self._max_tokens = max_tokens
        self._governance_enabled = bool(governance_enabled)
        self._memory_enabled = bool(memory_enabled)
        self._escalation_enabled = bool(escalation_enabled)
        # v0.3: ToolPolicy is the authoritative shape. v0.2's tool_allowlist
        # is preserved as backward-compat sugar.
        if tool_allowlist is not None and tool_policy is not None:
            raise ValueError(
                "tool_allowlist and tool_policy are mutually exclusive; "
                "pass one or the other (tool_policy is the v0.3 form)"
            )
        if tool_policy is not None:
            self._tool_policy: ToolPolicy | None = tool_policy
        elif tool_allowlist is not None and len(tool_allowlist) > 0:
            self._tool_policy = tool_policy_from_allowlist(tool_allowlist)
        else:
            self._tool_policy = None
        self._runner = Runner()
        self._sink: TraceSink = self._build_sink(trace_file, trace_to_stderr)
        self._conversation_id = make_conversation_id()
        self._memory = ConversationMemory()

        # Build the retriever from grounding paths (M2+)
        if grounding_paths:
            resolved = []
            for gp in grounding_paths:
                p = Path(gp)
                if p.is_dir():
                    resolved.extend(sorted(f for f in p.rglob("*") if f.is_file()))
                elif p.is_file():
                    resolved.append(p)
            if resolved:
                self._retriever = build_bm25_from_paths(resolved)
            else:
                self._retriever = NoOpRetriever()
        else:
            self._retriever = NoOpRetriever()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def backend(self) -> ModelBackend:
        return self._backend

    @property
    def model(self) -> str:
        return self._model

    @property
    def conversation_id(self) -> str:
        return self._conversation_id

    @property
    def governance_enabled(self) -> bool:
        return self._governance_enabled

    @property
    def memory_enabled(self) -> bool:
        return self._memory_enabled

    @property
    def memory(self) -> ConversationMemory:
        return self._memory

    @property
    def tool_policy(self) -> ToolPolicy | None:
        return self._tool_policy

    @property
    def tool_allowlist(self) -> tuple[str, ...]:
        """v0.2 compatibility: list of tool names whose decision is ``allow``.

        Returns an empty tuple when no policy is configured.
        """
        if self._tool_policy is None:
            return ()
        return tuple(
            sorted(
                name
                for name, td in self._tool_policy.tools.items()
                if td.decision == "allow"
            )
        )

    def new_conversation(self) -> str:
        self._conversation_id = make_conversation_id()
        # Working memory is cleared per conversation; episodic/continuity
        # stay if the store is shared. For the default InMemoryStore,
        # each GovernedClient instance has its own store.
        return self._conversation_id

    def healthcheck(self) -> dict:
        return self._backend.healthcheck()

    def ask(
        self,
        user_input_text: str,
        *,
        conversation_id: str | None = None,
        task_family_hint: str | None = None,
        policy_refs: list[str] | None = None,
        grounding_refs: list[str] | None = None,
        tools: list[dict] | None = None,
    ) -> AnswerEnvelope:
        """Run one turn end-to-end.

        Same code path whether governance is on or off. When off, the
        substrate is skipped and the raw LLM answer is returned. When
        on, the substrate decides the answer mode and reshapes the text.

        v0.2: when ``tools`` is non-empty, the OpenAI-shaped tool spec is
        forwarded to the upstream model. The substrate's action_gate decides
        whether the model's tool_calls reply is allowed through. The
        client's ``tool_allowlist`` controls which tool names are permitted.
        """
        if not user_input_text or not user_input_text.strip():
            raise ValueError("user_input_text is required and cannot be empty")

        conv_id = conversation_id or self._conversation_id
        turn = self._build_turn_envelope(
            user_input_text=user_input_text.strip(),
            conversation_id=conv_id,
            task_family_hint=task_family_hint,
            policy_refs=policy_refs,
            grounding_refs=grounding_refs,
        )

        # Retrieve grounding chunks
        grounding = self._retriever.retrieve(turn.user_input_text, k=5)

        # M4: retrieve memory context from prior turns
        memory_context: list[dict[str, str]] = []
        if self._memory_enabled:
            prior_entries = self._memory.retrieve_context(
                conv_id, exclude_turn_id=turn.turn_id,
            )
            for entry in prior_entries:
                label = "Established fact from earlier" if entry.plane == "continuity" else "Prior exchange"
                memory_context.append({"label": label, "content": entry.content})

        # v0.2: figure out which tool names were requested. We need this both
        # to pass tools through to the backend and to synthesize substrate
        # policy refs ahead of time.
        requested_tool_names: list[str] = _extract_tool_names(tools)
        tool_intent_present = bool(requested_tool_names)

        total_started = time.perf_counter()
        proposal = self._runner.run(
            turn=turn,
            grounding=grounding,
            backend=self._backend,
            memory_context=memory_context,
            tools=tools if tool_intent_present else None,
        )
        pipeline_ms = int((time.perf_counter() - total_started) * 1000)

        # --- governance switch (one code path, one boolean) ---
        if self._governance_enabled:
            # Build memory suggestion for the substrate to gate
            memory_suggestion = {
                "target_memory_ref_or_none": f"mem:continuity:{turn.turn_id}",
                "superseded_memory_ref_or_none": None,
            } if self._memory_enabled else None

            # Build the turn envelope dict for the substrate
            corpus_refs = [c.ref for c in grounding.chunks]

            # v0.2: synthesize tool-policy refs so policy_gate / action_gate
            # can decide allow/block on tool intent. Off-allowlist tools yield
            # ``policy:block:tool:<n>`` refs that policy_gate matches.
            base_policy_refs = list(turn.policy_refs or [])
            tool_policy_refs = self._build_tool_policy_refs(requested_tool_names)
            combined_policy_refs = base_policy_refs + tool_policy_refs

            turn_dict = {
                "turn_id": turn.turn_id,
                "conversation_id": turn.conversation_id,
                "user_input_text": turn.user_input_text,
                "admitted_corpus_refs": corpus_refs,
                "policy_context_refs_or_none": (
                    combined_policy_refs if combined_policy_refs else None
                ),
                "prior_state_refs_or_none": None,
                "requested_action_class_or_none": (
                    "tool_call" if tool_intent_present else None
                ),
                "task_family": task_family_hint,
            }
            # v0.2: when the upstream model returned tool_calls, surface them
            # to the substrate so action_gate sees the actual proposed action.
            proposed_action: dict | None = None
            if proposal.tool_calls:
                proposed_action = {
                    "kind": "tool_calls",
                    "tool_calls": list(proposal.tool_calls),
                    "tool_names": [
                        _tool_call_name(tc) for tc in proposal.tool_calls
                    ],
                }
            proposal_dict = {
                "proposal_id": f"proposal:{turn.turn_id}",
                "turn_id": turn.turn_id,
                "proposed_content_summary_or_none": proposal.raw_answer_text[:200],
                "proposed_action_or_none": proposed_action,
                "proposed_answer_mode_candidates": ["grounded_fact", "derived_explanation"],
                "proposed_evidence_refs_or_none": corpus_refs or None,
                "memory_suggestion_or_none": memory_suggestion,
            }

            substrate_result = run_substrate(
                turn_envelope=turn_dict,
                proposal_envelope=proposal_dict,
                retrieval_count=len(grounding.chunks),
                task_family_hint=task_family_hint,
            )

            answer_mode = substrate_result["final_answer_mode"]
            decisions = SubstrateDecisions(
                provenance_record=substrate_result["provenance_record"],
                support_state_record=substrate_result["support_state_record"],
                contradiction_record=substrate_result["contradiction_record"],
                policy_gate_decision=substrate_result["policy_gate_decision"],
                action_gate_decision=substrate_result["action_gate_decision"],
                memory_admission_decision=substrate_result["memory_admission_decision"],
                rollback_or_quarantine_record=substrate_result["rollback_or_quarantine_record"],
                final_answer_mode_decision=substrate_result["final_answer_mode_decision"],
            )

            blocked_reason = substrate_result["final_answer_mode_decision"].get("blocked_reason_or_none")
            raw_text = proposal.raw_answer_text

            # M4: weak-answer escalation (optional, max 1 retry)
            escalation_result = None
            if self._escalation_enabled:
                grounding_texts = [c.text for c in grounding.chunks]
                diagnosis = diagnose_weak_answer(
                    raw_text,
                    grounding_texts=grounding_texts,
                    expected_ref_count=len(grounding.chunks),
                )
                if should_escalate(diagnosis):
                    retry_messages = build_retry_messages(
                        turn.user_input_text,
                        raw_text,
                        grounding_texts=grounding_texts,
                    )
                    try:
                        retry_response = self._backend.complete(
                            retry_messages,
                            model=self._model,
                            temperature=self._temperature,
                            max_tokens=self._max_tokens,
                        )
                        retry_diagnosis = diagnose_weak_answer(
                            retry_response.text,
                            grounding_texts=grounding_texts,
                            expected_ref_count=len(grounding.chunks),
                        )
                        # Use the retry only if it's less weak
                        if not retry_diagnosis.is_weak or len(retry_diagnosis.reasons) < len(diagnosis.reasons):
                            raw_text = retry_response.text
                        escalation_result = EscalationResult(
                            original_diagnosis=diagnosis,
                            retried=True,
                            retry_diagnosis=retry_diagnosis,
                            retry_text=retry_response.text,
                            final_text=raw_text,
                            retry_count=1,
                        )
                    except BackendError:
                        # Retry failed — use the original answer
                        escalation_result = EscalationResult(
                            original_diagnosis=diagnosis,
                            retried=False,
                            final_text=raw_text,
                        )

            final_text = reshape_answer(
                raw_text=raw_text,
                answer_mode=answer_mode,
                support_label=substrate_result["support_state_record"]["support_label"],
                blocked_reason=blocked_reason,
                refs=corpus_refs,
            )
            final_refs = corpus_refs

            # v0.3: decide whether the upstream's tool_calls reach the caller.
            # The substrate's action_gate emits one of allow / soften / block /
            # not_applicable. v0.3 maps:
            #
            # - allow  -> tool_calls pass through (same as v0.2 allow)
            # - soften -> tool_calls pass through AND soften_warnings populated
            # - block  -> tool_calls dropped, text refusal
            # - other  -> tool_calls dropped, text refusal
            #
            # After that decision, run argument-deny inspection on whatever
            # tool_calls survived. Any deny match is **all-or-nothing**:
            # drop the whole array and switch to the text-refusal path
            # (v0.3 simplification; per-call filtering is v0.4).
            governed_tool_calls: list[dict] | None = None
            soften_warnings: list[str] = []
            argument_denials_envelope: list[dict] = []
            if tool_intent_present and proposal.tool_calls:
                ag = substrate_result.get("action_gate_decision") or {}
                ag_decision_class = ag.get("decision_class")
                ag_reason_code = ag.get("reason_code")

                if ag_decision_class == "allow":
                    governed_tool_calls = list(proposal.tool_calls)
                elif ag_decision_class == "soften":
                    governed_tool_calls = list(proposal.tool_calls)
                    if isinstance(ag_reason_code, str) and ag_reason_code:
                        soften_warnings.append(ag_reason_code)
                    # Add per-tool soften reasons (the substrate emits one
                    # action_gate decision for the turn; we add tool-specific
                    # context so the trace names which tools were softened).
                    if self._tool_policy is not None:
                        for tc in proposal.tool_calls:
                            tcn = _tool_call_name(tc)
                            if not tcn:
                                continue
                            td = self._tool_policy.decide(tcn)
                            if td.decision == "soften" and td.reason:
                                soften_warnings.append(
                                    f"{tcn}:{td.reason}"
                                )
                else:
                    blocked_tool_names = [
                        _tool_call_name(tc) for tc in proposal.tool_calls
                    ]
                    final_text = _format_tool_block_message(
                        blocked_tool_names=blocked_tool_names,
                        allowlist=self.tool_allowlist,
                    )

                # v0.3 argument inspection runs on whatever survived the
                # substrate decision. If anything was going to pass through
                # (allow or soften), check the model's actual arguments.
                if governed_tool_calls is not None and self._tool_policy is not None:
                    denials: list[ArgumentDenial] = []
                    for tc in governed_tool_calls:
                        tcn = _tool_call_name(tc)
                        if not tcn:
                            continue
                        fn_args = (tc.get("function") or {}).get("arguments")
                        denials.extend(
                            self._tool_policy.evaluate_arguments(tcn, fn_args)
                        )
                    if denials:
                        # All-or-nothing: drop tool_calls, render refusal text.
                        argument_denials_envelope = [d.to_dict() for d in denials]
                        governed_tool_calls = None
                        soften_warnings = []  # don't leak soften when blocked
                        final_text = _format_argument_block_message(denials)

            # M4: store memory if admitted by the substrate
            if self._memory_enabled:
                self._memory.admit_and_store(
                    memory_admission_decision=substrate_result["memory_admission_decision"],
                    turn_id=turn.turn_id,
                    conversation_id=conv_id,
                    question=turn.user_input_text,
                    answer_text=raw_text,
                )
                # Always store an episodic record (not gated)
                self._memory.store_episodic(
                    turn_id=turn.turn_id,
                    conversation_id=conv_id,
                    question=turn.user_input_text,
                    answer_text=raw_text,
                    answer_mode=answer_mode,
                    governance_enabled=True,
                )
        else:
            # Governance OFF — raw answer, no substrate, no reshaping
            answer_mode = "grounded_fact"
            decisions = SubstrateDecisions()
            final_text = proposal.raw_answer_text
            final_refs = []
            escalation_result = None
            governed_tool_calls = list(proposal.tool_calls) if proposal.tool_calls else None
            soften_warnings = []
            argument_denials_envelope = []

            # M4: still store episodic memory even without governance
            if self._memory_enabled:
                self._memory.store_episodic(
                    turn_id=turn.turn_id,
                    conversation_id=conv_id,
                    question=turn.user_input_text,
                    answer_text=proposal.raw_answer_text,
                    answer_mode=answer_mode,
                    governance_enabled=False,
                )

        total_ms = int((time.perf_counter() - total_started) * 1000)

        trace: TraceEnvelope = build_trace(
            turn=turn,
            grounding=grounding,
            proposal=proposal,
            decisions=decisions,
            final_text=final_text,
            total_ms=total_ms,
            final_refs=final_refs,
        )
        self._sink.write(trace)

        return AnswerEnvelope(
            text=final_text,
            trace_id=turn.turn_id,
            refs=final_refs,
            decisions=decisions,
            total_ms=total_ms,
            answer_mode=answer_mode,
            tool_calls=governed_tool_calls,
            soften_warnings=list(soften_warnings),
            argument_denials=list(argument_denials_envelope),
        )

    def close(self) -> None:
        self._sink.close()

    def __enter__(self) -> "GovernedClient":
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _build_turn_envelope(
        self,
        *,
        user_input_text: str,
        conversation_id: str,
        task_family_hint: str | None,
        policy_refs: list[str] | None,
        grounding_refs: list[str] | None,
    ) -> TurnEnvelope:
        created_at = TurnEnvelope.now_iso()
        turn_id = make_turn_id(conversation_id, created_at, user_input_text)
        return TurnEnvelope(
            turn_id=turn_id,
            conversation_id=conversation_id,
            user_input_text=user_input_text,
            backend_name=getattr(self._backend, "name", "unknown"),
            model_id=self._model,
            created_at=created_at,
            task_family_hint=task_family_hint,
            policy_refs=list(policy_refs) if policy_refs else None,
            grounding_refs=list(grounding_refs) if grounding_refs else None,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
        )

    @staticmethod
    def _build_sink(
        trace_file: str | Path | None, trace_to_stderr: bool
    ) -> TraceSink:
        sinks: list[TraceSink] = []
        if trace_file is not None:
            sinks.append(FileJsonlSink(trace_file))
        if trace_to_stderr:
            sinks.append(StdoutJsonlSink())
        if not sinks:
            return NullSink()
        if len(sinks) == 1:
            return sinks[0]
        return MultiSink(sinks)

    def _build_tool_policy_refs(self, requested_tool_names: list[str]) -> list[str]:
        """Synthesize ``policy:<decision>:tool:<n>`` refs from the tool policy.

        v0.3 semantics: each requested tool name is looked up in the configured
        :class:`ToolPolicy`. The decision (``allow`` / ``soften`` / ``block``)
        determines the ref:

        - ``allow``  -> ``policy:allow:tool:<n>``
        - ``soften`` -> ``policy:soften:tool:<n>`` (action_gate soften trigger)
        - ``block``  -> ``policy:block:tool:<n>`` (policy_gate block trigger)

        When no policy is configured, every tool yields a block ref, preserving
        v0.1/v0.2 default-block behaviour. Tool names not enumerated in the
        policy fall back to ``policy.default``.
        """
        if not requested_tool_names:
            return []
        if self._tool_policy is None:
            return [
                f"policy:block:tool:{name}" for name in requested_tool_names
            ]
        refs: list[str] = []
        for name in requested_tool_names:
            decision = self._tool_policy.decide(name).decision
            refs.append(f"policy:{decision}:tool:{name}")
        return refs


# ---------------------------------------------------------------------------
# v0.2 module-level helpers (small, pure)
# ---------------------------------------------------------------------------


def _extract_tool_names(tools: list[dict] | None) -> list[str]:
    """Return the list of tool function names from an OpenAI-shaped tool spec."""
    if not tools:
        return []
    names: list[str] = []
    for entry in tools:
        if not isinstance(entry, dict):
            continue
        # OpenAI shape: {"type": "function", "function": {"name": ..., ...}}
        fn = entry.get("function")
        if isinstance(fn, dict):
            name = fn.get("name")
            if isinstance(name, str) and name:
                names.append(name)
                continue
        # Looser shape: {"name": ...}
        name = entry.get("name")
        if isinstance(name, str) and name:
            names.append(name)
    return names


def _tool_call_name(tool_call: dict) -> str:
    """Extract the function name from one OpenAI-shaped tool_call dict."""
    if not isinstance(tool_call, dict):
        return ""
    fn = tool_call.get("function")
    if isinstance(fn, dict):
        name = fn.get("name")
        if isinstance(name, str):
            return name
    name = tool_call.get("name")
    return name if isinstance(name, str) else ""


def _format_tool_block_message(
    *, blocked_tool_names: list[str], allowlist: tuple[str, ...]
) -> str:
    """Render the user-facing assistant text when tool_calls are blocked."""
    blocked_unique = ", ".join(sorted(set(n for n in blocked_tool_names if n))) or "<unnamed tool>"
    if allowlist:
        allowed = ", ".join(sorted(allowlist))
        return (
            f"AGIF Governor blocked tool calls: {blocked_unique}. "
            f"Allowed tools: {allowed}."
        )
    return (
        f"AGIF Governor blocked tool calls: {blocked_unique}. "
        "No tools are currently allowlisted by the operator."
    )


def _format_argument_block_message(
    denials: list["ArgumentDenial"],
) -> str:
    """Render the user-facing assistant text when argument deny-patterns matched.

    Names only field paths and pattern ids — never the argument value. v0.3
    is all-or-nothing: any denial drops the whole tool_calls array, so this
    summarises every denial as a single refusal sentence.
    """
    if not denials:
        return "AGIF Governor blocked tool calls: argument deny pattern matched."
    pieces = sorted(
        {
            f"{d.tool_name}.{d.argument_path}={d.reason_code}#{d.pattern_id}"
            for d in denials
        }
    )
    return (
        "AGIF Governor blocked tool calls: argument deny pattern matched. "
        + "; ".join(pieces)
        + "."
    )
