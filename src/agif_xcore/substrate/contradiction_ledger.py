"""Contradiction preservation.

Ported from X1 ``agif_substrate/contradiction_ledger.py`` (43 LOC).
Flags blocking contradictions as explicit control records.
"""

from __future__ import annotations

from ._util import unique_list


def build_contradiction_record(
    turn_envelope: dict,
    provenance_record: dict,
    support_state_record: dict,
) -> dict:
    turn_id = turn_envelope["turn_id"]
    prior_refs = unique_list(turn_envelope.get("prior_state_refs_or_none"))
    conflict_refs = [r for r in prior_refs if r.startswith("conflict:")]

    if support_state_record["support_label"] == "unsupported_conflicting_evidence" or conflict_refs:
        return {
            "contradiction_ref_or_explicit_none": f"contradiction:{turn_id}",
            "turn_id": turn_id,
            "contradiction_status": "blocking_conflict",
            "blocking_flag": True,
            "contradiction_refs_or_none": conflict_refs or provenance_record.get("prior_state_refs_or_none"),
            "required_resolution_or_none": "manual_resolution_required",
        }

    return {
        "contradiction_ref_or_explicit_none": f"none:contradiction:{turn_id}",
        "turn_id": turn_id,
        "contradiction_status": "explicit_none",
        "blocking_flag": False,
        "contradiction_refs_or_none": None,
        "required_resolution_or_none": None,
    }
