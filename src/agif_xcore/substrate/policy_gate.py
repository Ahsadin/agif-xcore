"""Policy gating.

Ported from X1 ``agif_substrate/policy_gate.py`` (63 LOC).
Decides whether decisive response classes are allowed.
"""

from __future__ import annotations

from ._util import unique_list


def evaluate_policy_gate(
    turn_envelope: dict,
    support_state_record: dict,
    contradiction_record: dict,
) -> dict:
    turn_id = turn_envelope["turn_id"]
    support_label = support_state_record["support_label"]
    policy_refs = unique_list(turn_envelope.get("policy_context_refs_or_none"))

    if any(ref.startswith("policy:block:") for ref in policy_refs) or support_label == "blocked_by_policy":
        dc, rc, ar, br = "block", "policy_block", "abstain_only", "decisive_content"
    elif contradiction_record["blocking_flag"]:
        dc, rc, ar, br = "restrict_non_decisive", "blocking_contradiction", "non_decisive_only", "decisive_content"
    elif support_label == "ambiguous_needs_clarification":
        dc, rc, ar, br = "restrict_non_decisive", "clarification_required", "clarify_only", "decisive_content"
    elif support_label in {"unsupported_missing_evidence", "unsupported_conflicting_evidence", "unsupported_off_scope"}:
        dc, rc, ar, br = "restrict_non_decisive", "insufficient_governed_support", "non_decisive_only", "decisive_content"
    else:
        dc, rc, ar, br = "allow", "policy_allow", "decisive_content", None

    return {
        "policy_gate_ref": f"policy:{turn_id}",
        "turn_id": turn_id,
        "decision_class": dc,
        "reason_code": rc,
        "allowed_response_class": ar,
        "blocked_response_class_or_none": br,
    }
