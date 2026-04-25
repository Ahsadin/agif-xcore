"""Memory-admission control.

Ported from X1 ``agif_substrate/memory_admission.py`` (59 LOC).
Guards memory writes behind governance checks.
"""

from __future__ import annotations


def decide_memory_admission(
    turn_envelope: dict,
    support_state_record: dict,
    contradiction_record: dict,
    policy_gate_decision: dict,
    action_gate_decision: dict,
    proposal_envelope: dict,
) -> dict:
    turn_id = turn_envelope["turn_id"]
    suggestion = proposal_envelope.get("memory_suggestion_or_none")

    if not suggestion:
        return {
            "memory_admission_ref_or_explicit_none": f"none:memory:{turn_id}",
            "turn_id": turn_id,
            "decision_class": "explicit_none",
            "target_memory_ref_or_none": None,
            "superseded_memory_ref_or_none": None,
            "reason_code": "no_memory_suggestion",
        }

    if isinstance(suggestion, dict):
        target = suggestion.get("target_memory_ref_or_none")
        superseded = suggestion.get("superseded_memory_ref_or_none")
    else:
        target, superseded = str(suggestion), None

    blocked = any((
        contradiction_record["blocking_flag"],
        policy_gate_decision["decision_class"] == "block",
        action_gate_decision["decision_class"] == "block",
        support_state_record["support_label"] != "supported",
    ))

    return {
        "memory_admission_ref_or_explicit_none": f"memory:{turn_id}",
        "turn_id": turn_id,
        "decision_class": "reject_write" if blocked else "admit_write",
        "target_memory_ref_or_none": target,
        "superseded_memory_ref_or_none": superseded,
        "reason_code": "governance_blocked_memory_write" if blocked else "memory_write_admitted",
    }
