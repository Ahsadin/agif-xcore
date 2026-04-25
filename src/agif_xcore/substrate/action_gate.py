"""Action gating.

Ported from X1 ``agif_substrate/action_gate.py`` (66 LOC).
Decides whether proposed action advice may be emitted.
"""

from __future__ import annotations

from ._util import unique_list

HIGH_RISK_ACTIONS = {"payment_release", "override", "refund", "state_change"}


def evaluate_action_gate(
    turn_envelope: dict,
    support_state_record: dict,
    policy_gate_decision: dict,
    proposal_envelope: dict,
) -> dict:
    turn_id = turn_envelope["turn_id"]
    requested_action = (
        turn_envelope.get("requested_action_class_or_none")
        or proposal_envelope.get("proposed_action_or_none")
    )
    policy_refs = unique_list(turn_envelope.get("policy_context_refs_or_none"))
    support_label = support_state_record["support_label"]

    if not requested_action:
        dc, rc, allowed, softened = "not_applicable", "no_action_requested", None, None
    elif policy_gate_decision["decision_class"] == "block":
        dc, rc, allowed, softened = "block", "policy_gate_block", None, None
    elif support_label != "supported":
        dc, rc, allowed, softened = "block", "insufficient_support_for_action", None, None
    elif any(ref.startswith("policy:soften:") for ref in policy_refs) or requested_action in HIGH_RISK_ACTIONS:
        dc, rc = "soften", "high_risk_action_requires_softening"
        allowed, softened = None, "escalate_or_request_secondary_review"
    else:
        dc, rc, allowed, softened = "allow", "action_allow", requested_action, None

    return {
        "action_gate_ref": f"action:{turn_id}",
        "turn_id": turn_id,
        "decision_class": dc,
        "reason_code": rc,
        "allowed_action_surface_or_none": allowed,
        "softened_action_surface_or_none": softened,
    }
