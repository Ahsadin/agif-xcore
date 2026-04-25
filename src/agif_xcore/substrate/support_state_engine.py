"""Support-state classification.

Ported from X1 ``agif_substrate/support_state_engine.py`` (62 LOC).
Emits exactly one frozen support label before answer-mode selection.
"""

from __future__ import annotations

from ._util import unique_list

ALLOWED_SUPPORT_LABELS = {
    "supported",
    "ambiguous_needs_clarification",
    "unsupported_missing_evidence",
    "unsupported_off_scope",
    "unsupported_conflicting_evidence",
    "blocked_by_policy",
}


def determine_support_state(turn_envelope: dict, provenance_record: dict) -> dict:
    turn_id = turn_envelope["turn_id"]
    user_text = str(turn_envelope["user_input_text"]).lower()
    policy_refs = unique_list(turn_envelope.get("policy_context_refs_or_none"))
    prior_refs = unique_list(turn_envelope.get("prior_state_refs_or_none"))
    missing_evidence = provenance_record.get("missing_evidence_refs_or_none") or []

    if any(ref.startswith("policy:block:") for ref in policy_refs):
        label = "blocked_by_policy"
        basis = policy_refs
    elif "missing_user_detail" in user_text:
        label = "ambiguous_needs_clarification"
        basis = provenance_record.get("admitted_evidence_refs") or []
    elif missing_evidence:
        label = "unsupported_missing_evidence"
        basis = missing_evidence
    elif any(ref.startswith("conflict:") for ref in prior_refs):
        label = "unsupported_conflicting_evidence"
        basis = [r for r in prior_refs if r.startswith("conflict:")]
    elif any(tok in user_text for tok in ("investment advice", "tax advice", "legal advice")):
        label = "unsupported_off_scope"
        basis = []
    else:
        label = "supported"
        basis = provenance_record.get("admitted_evidence_refs") or []

    if label not in ALLOWED_SUPPORT_LABELS:
        raise ValueError(f"invalid support label: {label}")

    return {
        "support_state_ref": f"support:{turn_id}",
        "turn_id": turn_id,
        "support_label": label,
        "basis_refs": basis,
        "missing_evidence_flag": bool(missing_evidence),
    }
