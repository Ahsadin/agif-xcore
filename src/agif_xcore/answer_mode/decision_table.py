"""Generic answer-mode decision table.

**REWRITE** of X1's ``answer_mode_resolver.py``. That file contained
hardcoded benchmark question strings (see the X1 audit). This file
uses **no question strings at all**. The decision is a pure function
of governance state:

  (support_label, blocking_flag, policy.decision_class,
   action.decision_class, rollback.decision_class,
   task_family_hint, retrieval_count)

       -> one of 8 modes

The 8 output modes are carried over verbatim from X1 because they are
a clean enumeration:

  grounded_fact, grounded_summary, grounded_with_gap,
  derived_explanation, clarify, search_needed,
  abstain, bounded_estimate
"""

from __future__ import annotations

from ..schemas import ALLOWED_ANSWER_MODES


def resolve_answer_mode(
    *,
    turn_id: str,
    support_label: str,
    blocking_flag: bool,
    policy_decision_class: str,
    action_decision_class: str,
    rollback_decision_class: str,
    task_family_hint: str | None = None,
    retrieval_count: int = 0,
) -> dict:
    """Choose the single allowed answer mode from governance state.

    Returns a dict with the same shape as X1's
    ``resolve_final_answer_mode`` so the substrate orchestrator and
    trace layer can consume it without schema changes.
    """

    # ------------------------------------------------------------------
    # Priority 1: structural blocks (quarantine, policy block)
    # ------------------------------------------------------------------
    if rollback_decision_class == "quarantine":
        mode = "abstain"
        auth = "quarantined"
        content_class = "no_output"
        blocked = "corrupt_prior_state"

    elif policy_decision_class == "block":
        mode = "abstain"
        auth = "authorized"
        content_class = "policy_block_notice"
        blocked = "policy_block"

    # ------------------------------------------------------------------
    # Priority 2: evidence-state routing
    # ------------------------------------------------------------------
    elif support_label == "ambiguous_needs_clarification":
        mode = "clarify"
        auth = "authorized"
        content_class = "clarification_request"
        blocked = None

    elif support_label == "unsupported_missing_evidence":
        if retrieval_count > 0:
            mode = "grounded_with_gap"
            content_class = "grounded_gap_notice"
        else:
            mode = "search_needed"
            content_class = "evidence_request"
        auth = "authorized"
        blocked = None

    elif support_label == "unsupported_conflicting_evidence" or blocking_flag:
        mode = "abstain"
        auth = "authorized"
        content_class = "conflict_notice"
        blocked = "conflicting_evidence"

    elif support_label == "unsupported_off_scope":
        mode = "abstain"
        auth = "authorized"
        content_class = "scope_boundary_notice"
        blocked = "out_of_scope"

    elif support_label == "blocked_by_policy":
        mode = "abstain"
        auth = "authorized"
        content_class = "policy_block_notice"
        blocked = "policy_block"

    # ------------------------------------------------------------------
    # Priority 3: softened actions
    # ------------------------------------------------------------------
    elif action_decision_class == "soften":
        mode = "derived_explanation"
        auth = "authorized"
        content_class = "softened_action_notice"
        blocked = None

    # ------------------------------------------------------------------
    # Priority 4: supported content — mode depends on grounding + hint
    # ------------------------------------------------------------------
    elif support_label == "supported":
        mode = _choose_supported_mode(task_family_hint, retrieval_count)
        auth = "authorized"
        content_class = "supported_content"
        blocked = None

    # ------------------------------------------------------------------
    # Fallback: conservative derived_explanation
    # ------------------------------------------------------------------
    else:
        mode = "derived_explanation"
        auth = "authorized"
        content_class = "supported_content"
        blocked = None

    if mode not in ALLOWED_ANSWER_MODES:
        raise ValueError(f"decision_table produced invalid mode: {mode}")

    return {
        "final_answer_mode_ref": f"answer_mode:{turn_id}",
        "turn_id": turn_id,
        "answer_mode": mode,
        "authorization_status": auth,
        "allowed_content_class": content_class,
        "blocked_reason_or_none": blocked,
    }


def _choose_supported_mode(
    task_family_hint: str | None,
    retrieval_count: int,
) -> str:
    """Pick among grounded_fact / grounded_summary / derived_explanation.

    The hint is optional and advisory. If absent or unrecognised, we
    fall back to ``derived_explanation`` when there's no grounding, or
    ``grounded_fact`` when there is.
    """
    hint = (task_family_hint or "").lower().strip()

    if hint in ("summary", "document_summary", "overview"):
        return "grounded_summary" if retrieval_count > 0 else "derived_explanation"

    if hint in ("estimate", "forecast", "projection"):
        return "bounded_estimate"

    # Default: if we have retrieved grounding, emit a grounded fact;
    # otherwise derive from the model's own knowledge.
    if retrieval_count > 0:
        return "grounded_fact"
    return "derived_explanation"
