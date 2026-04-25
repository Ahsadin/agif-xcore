"""Rollback and quarantine control.

Ported from X1 ``agif_substrate/rollback_quarantine.py`` (71 LOC).
Chooses rollback, quarantine, or explicit none.
"""

from __future__ import annotations

from ._util import unique_list

HIGH_RISK_ACTIONS = {"payment_release", "override", "refund", "state_change"}


def decide_rollback_or_quarantine(
    turn_envelope: dict,
    contradiction_record: dict,
    policy_gate_decision: dict,
    action_gate_decision: dict,
    memory_admission_decision: dict,
) -> dict:
    turn_id = turn_envelope["turn_id"]
    prior_refs = unique_list(turn_envelope.get("prior_state_refs_or_none"))
    corrupt_refs = [r for r in prior_refs if r.startswith("state:corrupt:")]
    requested_action = turn_envelope.get("requested_action_class_or_none")

    if corrupt_refs:
        return {
            "rollback_or_quarantine_ref_or_explicit_none": f"quarantine:{turn_id}",
            "turn_id": turn_id,
            "decision_class": "quarantine",
            "trigger_refs_or_none": corrupt_refs,
            "state_snapshot_ref_or_none": corrupt_refs[0].replace("state:", "snapshot:", 1),
            "reason_code": "corrupt_prior_state",
        }

    if contradiction_record["blocking_flag"] and (
        requested_action in HIGH_RISK_ACTIONS or action_gate_decision["decision_class"] == "block"
    ):
        return {
            "rollback_or_quarantine_ref_or_explicit_none": f"rollback:{turn_id}",
            "turn_id": turn_id,
            "decision_class": "rollback",
            "trigger_refs_or_none": contradiction_record["contradiction_refs_or_none"],
            "state_snapshot_ref_or_none": f"snapshot:rollback:{turn_id}",
            "reason_code": "blocking_conflict_on_high_risk_path",
        }

    if (
        memory_admission_decision["decision_class"] == "reject_write"
        and policy_gate_decision["decision_class"] == "block"
    ):
        return {
            "rollback_or_quarantine_ref_or_explicit_none": f"rollback:{turn_id}",
            "turn_id": turn_id,
            "decision_class": "rollback",
            "trigger_refs_or_none": [
                memory_admission_decision["reason_code"],
                policy_gate_decision["reason_code"],
            ],
            "state_snapshot_ref_or_none": f"snapshot:rollback:{turn_id}",
            "reason_code": "blocked_mutation_attempt",
        }

    return {
        "rollback_or_quarantine_ref_or_explicit_none": f"none:rollback_or_quarantine:{turn_id}",
        "turn_id": turn_id,
        "decision_class": "explicit_none",
        "trigger_refs_or_none": None,
        "state_snapshot_ref_or_none": None,
        "reason_code": "no_control_recovery_required",
    }
