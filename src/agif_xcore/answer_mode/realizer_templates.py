"""Mode-aware answer reshaping.

Maps the resolved ``answer_mode`` to a natural-language reframing
of the raw LLM answer. The user sees fluent text — never a classifier
label.

In M2 this is a lightweight template layer. The LLM already produced
a raw answer in the planner stage; here we wrap it in an appropriate
frame based on the governance decision. A future milestone could
replace this with a second LLM call (the "language realization" stage)
for richer reshaping.
"""

from __future__ import annotations

from ..schemas import ALLOWED_ANSWER_MODES


def reshape_answer(
    *,
    raw_text: str,
    answer_mode: str,
    support_label: str,
    blocked_reason: str | None = None,
    refs: list[str] | None = None,
) -> str:
    """Return a natural-language answer text shaped by the governance mode.

    ``raw_text`` is the LLM's unfiltered answer from the planner stage.
    The output is what the user actually sees.
    """
    if answer_mode not in ALLOWED_ANSWER_MODES:
        raise ValueError(f"unknown answer_mode: {answer_mode}")

    if answer_mode == "abstain":
        return _abstain(blocked_reason)

    if answer_mode == "clarify":
        return _clarify(raw_text)

    if answer_mode == "search_needed":
        return _search_needed()

    if answer_mode == "grounded_with_gap":
        return _grounded_with_gap(raw_text, refs)

    if answer_mode == "grounded_fact":
        return _grounded_fact(raw_text, refs)

    if answer_mode == "grounded_summary":
        return _grounded_summary(raw_text, refs)

    if answer_mode == "bounded_estimate":
        return _bounded_estimate(raw_text, refs)

    # derived_explanation — the default supported mode
    return raw_text.strip()


# ---------------------------------------------------------------------------
# Per-mode templates
# ---------------------------------------------------------------------------

def _abstain(reason: str | None) -> str:
    if reason == "corrupt_prior_state":
        return (
            "I cannot produce an answer because prior state appears "
            "corrupted. This turn has been quarantined pending review."
        )
    if reason == "policy_block":
        return (
            "I cannot answer this question because it falls outside "
            "permitted policy boundaries."
        )
    if reason == "conflicting_evidence":
        return (
            "I found conflicting evidence on this topic and cannot "
            "produce a reliable answer. Manual review is needed."
        )
    if reason == "out_of_scope":
        return (
            "This question is outside the scope of topics I can "
            "answer with grounded evidence."
        )
    return (
        "I don't have sufficient grounded support to answer this "
        "question reliably."
    )


def _clarify(raw_text: str) -> str:
    # If the LLM's raw answer is already a clarification, use it.
    text = raw_text.strip()
    if text and any(text.lower().startswith(p) for p in (
        "could you", "can you", "do you mean", "i'd like to",
        "to answer", "before i",
    )):
        return text
    return (
        "I'd like to clarify one thing before answering: "
        "could you provide more detail about what specifically "
        "you're looking for?"
    )


def _search_needed() -> str:
    return (
        "I don't have grounded evidence to answer this yet. "
        "Could you point me at the relevant source documents "
        "so I can give you a supported answer?"
    )


def _grounded_with_gap(raw_text: str, refs: list[str] | None) -> str:
    text = raw_text.strip()
    ref_note = _format_refs(refs)
    gap_notice = (
        "\n\nNote: some of the evidence needed for a complete "
        "answer was not found in the provided sources."
    )
    return f"{text}{ref_note}{gap_notice}"


def _grounded_fact(raw_text: str, refs: list[str] | None) -> str:
    text = raw_text.strip()
    return f"{text}{_format_refs(refs)}"


def _grounded_summary(raw_text: str, refs: list[str] | None) -> str:
    text = raw_text.strip()
    return f"{text}{_format_refs(refs)}"


def _bounded_estimate(raw_text: str, refs: list[str] | None) -> str:
    text = raw_text.strip()
    caveat = (
        "\n\nCaveat: this is a bounded estimate based on the "
        "available evidence, not a definitive answer."
    )
    return f"{text}{_format_refs(refs)}{caveat}"


def _format_refs(refs: list[str] | None) -> str:
    if not refs:
        return ""
    formatted = ", ".join(refs[:5])
    more = f" (+{len(refs) - 5} more)" if len(refs) > 5 else ""
    return f"\n\nSources: {formatted}{more}"
