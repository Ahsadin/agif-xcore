"""Canonical data envelopes used across AGIF-XCore.

M1 uses stdlib dataclasses. These types are the schema contract between
the backends, the pipeline, the substrate (M2+), the trace layer, and
the client-facing API.

Every envelope carries a ``schema_version`` so determinism tests can
detect an unannounced schema change. Version bumps are manual.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

# ---------------------------------------------------------------------------
# Version constants
# ---------------------------------------------------------------------------

SCHEMA_VERSION_TURN = "1.0.0"
SCHEMA_VERSION_GROUNDING = "1.0.0"
SCHEMA_VERSION_PROPOSAL = "1.0.0"
SCHEMA_VERSION_SUBSTRATE = "1.0.0"
SCHEMA_VERSION_TRACE = "1.0.0"
SCHEMA_VERSION_ANSWER = "1.0.0"


# ---------------------------------------------------------------------------
# Allowed answer modes (frozen enum as a plain tuple, no external enum dep)
# ---------------------------------------------------------------------------

# The 8 modes inherited from X1's substrate. M1 only emits "grounded_fact"
# (no substrate) but the schema reserves every mode so M2+ can add them
# without a schema bump.
ALLOWED_ANSWER_MODES: tuple[str, ...] = (
    "grounded_fact",
    "grounded_summary",
    "grounded_with_gap",
    "derived_explanation",
    "clarify",
    "search_needed",
    "abstain",
    "bounded_estimate",
)


# ---------------------------------------------------------------------------
# Core envelopes
# ---------------------------------------------------------------------------

@dataclass
class TurnEnvelope:
    """Inputs to a single turn. Immutable once constructed."""

    turn_id: str
    conversation_id: str
    user_input_text: str
    backend_name: str
    model_id: str
    created_at: str
    schema_version: str = SCHEMA_VERSION_TURN
    task_family_hint: str | None = None
    policy_refs: list[str] | None = None
    grounding_refs: list[str] | None = None
    temperature: float = 0.0
    max_tokens: int | None = None

    @staticmethod
    def now_iso() -> str:
        """UTC ISO-8601 string without fractional seconds."""
        return (
            datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )


@dataclass
class GroundingChunk:
    """One retrieved chunk of evidence."""

    ref: str
    source_path: str
    text: str
    score: float
    loader: str


@dataclass
class GroundingBundle:
    """All evidence retrieved for a single turn. Empty in M1."""

    chunks: list[GroundingChunk] = field(default_factory=list)
    retriever_name: str = "noop"
    retrieval_ms: int = 0
    schema_version: str = SCHEMA_VERSION_GROUNDING

    @property
    def is_empty(self) -> bool:
        return not self.chunks


@dataclass
class ProposalEnvelope:
    """The raw + cited answer material produced by the pipeline.

    In M1 ``raw_answer_text`` is the backend's own response and
    ``cited_refs`` is empty; M2 populates citations and multi-stage
    outputs.
    """

    turn_id: str
    raw_answer_text: str
    backend_model_id: str
    schema_version: str = SCHEMA_VERSION_PROPOSAL
    cited_refs: list[str] = field(default_factory=list)
    stage_outputs: dict[str, dict[str, Any]] = field(default_factory=dict)
    stage_timings_ms: dict[str, int] = field(default_factory=dict)
    finish_reason: str | None = None
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    # v0.2: parsed tool_calls returned by the upstream model. Substrate
    # action_gate decides whether they are relayed to the client.
    tool_calls: list[dict[str, Any]] | None = None


@dataclass
class SubstrateDecisions:
    """All 9 substrate decision records. M2+ populates these; M1 leaves them None."""

    provenance_record: dict[str, Any] | None = None
    support_state_record: dict[str, Any] | None = None
    contradiction_record: dict[str, Any] | None = None
    policy_gate_decision: dict[str, Any] | None = None
    action_gate_decision: dict[str, Any] | None = None
    memory_admission_decision: dict[str, Any] | None = None
    rollback_or_quarantine_record: dict[str, Any] | None = None
    final_answer_mode_decision: dict[str, Any] | None = None
    schema_version: str = SCHEMA_VERSION_SUBSTRATE

    @property
    def governance_enabled(self) -> bool:
        """True if at least one substrate stage actually ran."""
        return any(
            getattr(self, name) is not None
            for name in (
                "provenance_record",
                "support_state_record",
                "contradiction_record",
                "policy_gate_decision",
                "action_gate_decision",
                "memory_admission_decision",
                "rollback_or_quarantine_record",
                "final_answer_mode_decision",
            )
        )


@dataclass
class TraceEnvelope:
    """The replayable trace of one turn end-to-end."""

    turn_id: str
    inputs_hash: str
    turn_envelope: TurnEnvelope
    grounding_bundle: GroundingBundle
    proposal_envelope: ProposalEnvelope
    substrate_decisions: SubstrateDecisions
    final_text: str
    total_ms: int
    schema_version: str = SCHEMA_VERSION_TRACE
    final_refs: list[str] = field(default_factory=list)


@dataclass
class AnswerEnvelope:
    """What ``GovernedClient.ask()`` returns to the caller.

    The ``tool_calls`` field is populated when the substrate's action_gate
    decided ``allow`` or ``soften`` for a tool-bearing turn (v0.3) — soften
    still passes tool_calls through but flags them via ``soften_warnings``.
    v0.1 callers that did not pass ``tools`` to ``ask()`` will always see
    ``tool_calls=None`` and can ignore it.

    v0.3 fields:

    - ``soften_warnings``: substrate reason codes when action_gate emitted
      ``soften``. Empty list when not softened.
    - ``argument_denials``: per-argument deny-pattern matches recorded after
      the substrate ran. When non-empty, v0.3 drops the tool_calls entirely
      (all-or-nothing) and the response surfaces ``text`` instead.
    """

    text: str
    trace_id: str
    schema_version: str = SCHEMA_VERSION_ANSWER
    refs: list[str] = field(default_factory=list)
    decisions: SubstrateDecisions | None = None
    total_ms: int = 0
    answer_mode: str = "grounded_fact"
    tool_calls: list[dict[str, Any]] | None = None
    soften_warnings: list[str] = field(default_factory=list)
    argument_denials: list[dict[str, Any]] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Canonical serialization + hashing
# ---------------------------------------------------------------------------

def canonical_json(obj: Any) -> str:
    """Produce a canonical JSON form (sorted keys, no whitespace, ensure_ascii).

    The canonical form is what determinism tests hash. It is not intended
    for human reading — use ``pretty_json`` for that.
    """
    return json.dumps(
        _to_jsonable(obj),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    )


def pretty_json(obj: Any) -> str:
    """Human-readable JSON serialization (2-space indent, sorted keys)."""
    return json.dumps(
        _to_jsonable(obj),
        sort_keys=True,
        indent=2,
        ensure_ascii=False,
        default=str,
    )


def _to_jsonable(obj: Any) -> Any:
    """Best-effort conversion of dataclasses/nested types to JSON primitives."""
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return obj
    if isinstance(obj, (list, tuple)):
        return [_to_jsonable(item) for item in obj]
    if isinstance(obj, dict):
        return {str(k): _to_jsonable(v) for k, v in obj.items()}
    # dataclass instance
    try:
        return _to_jsonable(asdict(obj))
    except TypeError:
        return str(obj)


def compute_inputs_hash(turn: TurnEnvelope, grounding: GroundingBundle) -> str:
    """SHA-256 over the canonical form of the turn + grounding bundle.

    This is the key used for replay: two runs whose inputs hash matches
    must produce identical trace envelopes when ``temperature=0.0``.
    """
    payload = {
        "turn_envelope": _to_jsonable(turn),
        "grounding_bundle": _to_jsonable(grounding),
    }
    blob = canonical_json(payload).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


# ---------------------------------------------------------------------------
# Turn-id generation
# ---------------------------------------------------------------------------

def make_turn_id(conversation_id: str, created_at: str, user_input_text: str) -> str:
    """Deterministic turn id from (conversation, time, input).

    Two identical calls with the same (conversation, time, input) produce
    the same id. This is what makes the replay test stable.
    """
    seed = f"{conversation_id}|{created_at}|{user_input_text}"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return f"turn_{digest[:16]}"


def make_conversation_id() -> str:
    """Fresh conversation id derived from the current UTC timestamp."""
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    return f"conversation_{stamp}"
