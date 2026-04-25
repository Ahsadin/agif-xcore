"""Substrate orchestrator.

Chains the 9 governance modules in the same order as X1's
``governed_demo_turn.py`` (L409-L449):

  provenance → support → contradiction → policy → action →
  memory admission → rollback/quarantine → answer_mode → trace

Every module is a pure dict-in/dict-out function. No LLM call, no
model awareness, no benchmark strings. The orchestrator is the only
place that knows the order.
"""

from __future__ import annotations

from typing import Any

from ..answer_mode.decision_table import resolve_answer_mode
from .action_gate import evaluate_action_gate
from .contradiction_ledger import build_contradiction_record
from .memory_admission import decide_memory_admission
from .policy_gate import evaluate_policy_gate
from .provenance_graph import build_provenance_record
from .rollback_quarantine import decide_rollback_or_quarantine
from .support_state_engine import determine_support_state


def run_substrate(
    *,
    turn_envelope: dict[str, Any],
    proposal_envelope: dict[str, Any],
    retrieval_count: int = 0,
    task_family_hint: str | None = None,
) -> dict[str, Any]:
    """Run the full 9-stage governance substrate.

    Returns a flat dict with one key per stage record plus a
    ``final_answer_mode`` shortcut.
    """

    # 1. Provenance: admit / reject proposed evidence refs
    provenance = build_provenance_record(turn_envelope, proposal_envelope)

    # 2. Support state: classify into one of 6 labels
    support = determine_support_state(turn_envelope, provenance)

    # 3. Contradiction: flag blocking conflicts
    contradiction = build_contradiction_record(turn_envelope, provenance, support)

    # 4. Policy gate: block / restrict / allow
    policy = evaluate_policy_gate(turn_envelope, support, contradiction)

    # 5. Action gate: block / soften / allow / N/A
    action = evaluate_action_gate(turn_envelope, support, policy, proposal_envelope)

    # 6. Memory admission: admit or reject proposed memory writes
    memory = decide_memory_admission(
        turn_envelope, support, contradiction, policy, action, proposal_envelope
    )

    # 7. Rollback / quarantine: corrupt state → quarantine; high-risk conflict → rollback
    rollback = decide_rollback_or_quarantine(
        turn_envelope, contradiction, policy, action, memory
    )

    # 8. Answer-mode resolution: generic decision table (no benchmark strings)
    answer_mode_decision = resolve_answer_mode(
        turn_id=turn_envelope["turn_id"],
        support_label=support["support_label"],
        blocking_flag=contradiction["blocking_flag"],
        policy_decision_class=policy["decision_class"],
        action_decision_class=action["decision_class"],
        rollback_decision_class=rollback["decision_class"],
        task_family_hint=task_family_hint,
        retrieval_count=retrieval_count,
    )

    return {
        "provenance_record": provenance,
        "support_state_record": support,
        "contradiction_record": contradiction,
        "policy_gate_decision": policy,
        "action_gate_decision": action,
        "memory_admission_decision": memory,
        "rollback_or_quarantine_record": rollback,
        "final_answer_mode_decision": answer_mode_decision,
        "final_answer_mode": answer_mode_decision["answer_mode"],
        "authorization_status": answer_mode_decision["authorization_status"],
    }
