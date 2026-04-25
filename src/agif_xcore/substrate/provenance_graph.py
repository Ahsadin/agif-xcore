"""Provenance binding — admits proposed refs against the turn's admitted corpus.

Ported from X1 ``agif_substrate/provenance_graph.py`` (74 LOC). The logic
is unchanged: proposed evidence refs that appear in the admitted corpus
are "admitted"; the rest are "missing". Pure set arithmetic, no model.
"""

from __future__ import annotations

from ._util import unique_list

TURN_REQUIRED_FIELDS = [
    "turn_id",
    "conversation_id",
    "user_input_text",
    "admitted_corpus_refs",
]

PROPOSAL_REQUIRED_FIELDS = [
    "proposal_id",
    "turn_id",
    "proposed_evidence_refs_or_none",
]


def _require_fields(payload: dict, required: list[str], name: str) -> None:
    missing = [f for f in required if f not in payload]
    if missing:
        raise ValueError(f"{name} missing: {', '.join(missing)}")


def build_provenance_record(turn_envelope: dict, proposal_envelope: dict) -> dict:
    """Bind admitted vs missing evidence into one governed record."""
    _require_fields(turn_envelope, TURN_REQUIRED_FIELDS, "turn_envelope")
    _require_fields(proposal_envelope, PROPOSAL_REQUIRED_FIELDS, "proposal_envelope")

    turn_id = turn_envelope["turn_id"]
    admitted_refs = unique_list(turn_envelope.get("admitted_corpus_refs"))
    proposed_refs = unique_list(proposal_envelope.get("proposed_evidence_refs_or_none"))
    policy_basis = unique_list(turn_envelope.get("policy_context_refs_or_none")) or None
    prior_state = unique_list(turn_envelope.get("prior_state_refs_or_none")) or None

    admitted_evidence = [r for r in proposed_refs if r in admitted_refs]
    missing_evidence = [r for r in proposed_refs if r not in admitted_refs]

    if missing_evidence:
        status = "missing_evidence"
    elif admitted_evidence or policy_basis or prior_state:
        status = "grounded"
    else:
        status = "explicit_none"

    return {
        "provenance_ref": f"prov:{turn_id}",
        "turn_id": turn_id,
        "admitted_evidence_refs": admitted_evidence,
        "missing_evidence_refs_or_none": missing_evidence or None,
        "policy_basis_refs_or_none": policy_basis,
        "prior_state_refs_or_none": prior_state,
        "provenance_status": status,
    }
