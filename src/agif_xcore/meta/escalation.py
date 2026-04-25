"""Weak-answer diagnosis and optional single retry.

Ported from AGIFCore Phase 10 meta-cognition, specifically:

  * ``weak_answer_diagnosis.py`` — 5 diagnosis categories
  * ``meta_cognition_layer.py`` — coordinator with CritiqueOutcome
  * ``skeptic_counterexample.py`` — adversarial branch reasoning

XCore adapts the pattern into a simpler model focused on extractable
features (no LLM call needed for diagnosis):

  1. **Hedge-word density** — high density of hedging language
  2. **Answer length** — too short for the question type
  3. **Reference count** — grounding was provided but not cited
  4. **Grounding overlap** — answer text overlaps poorly with evidence
  5. **Repetitive uncertainty** — "I don't know" style repetition

If the diagnosis says weak AND governance is enabled, the escalation
module can optionally retry ONCE with a tighter prompt. The hard cap
of 1 retry per turn is enforced unconditionally.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Sequence


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Hedge words/phrases that indicate uncertainty.
# Not exhaustive — just enough to catch the common patterns.
HEDGE_WORDS: tuple[str, ...] = (
    "maybe",
    "perhaps",
    "might",
    "possibly",
    "probably",
    "i think",
    "it seems",
    "i believe",
    "not sure",
    "i'm not sure",
    "i am not sure",
    "unclear",
    "hard to say",
    "difficult to determine",
    "i don't know",
    "i do not know",
    "cannot determine",
    "not certain",
    "it depends",
    "arguably",
)

# Thresholds
HEDGE_DENSITY_THRESHOLD = 0.08  # 8% of words are hedge words → weak
MIN_ANSWER_LENGTH_WORDS = 8     # fewer than 8 words → suspiciously short
GROUNDING_OVERLAP_THRESHOLD = 0.05  # <5% word overlap with evidence → weak
MAX_RETRIES = 1                 # Hard cap, enforced unconditionally

# Tighter system prompt used for the retry attempt
RETRY_SYSTEM_PROMPT = (
    "You are a precise and helpful assistant. "
    "Your previous answer was too vague or hedged. "
    "This time, answer the question directly and specifically. "
    "If you have reference material, cite it explicitly. "
    "If you truly cannot answer, say exactly what information is missing. "
    "Do not hedge with 'maybe' or 'perhaps' — be direct."
)


# ---------------------------------------------------------------------------
# Diagnosis
# ---------------------------------------------------------------------------

@dataclass
class WeakAnswerDiagnosis:
    """Extractable-feature diagnosis of answer quality.

    No LLM call. Pure text analysis.
    """

    hedge_word_density: float
    answer_length_words: int
    ref_count: int
    expected_ref_count: int
    grounding_overlap: float
    is_weak: bool
    reasons: list[str] = field(default_factory=list)


def diagnose_weak_answer(
    answer_text: str,
    *,
    grounding_texts: Sequence[str] = (),
    expected_ref_count: int = 0,
) -> WeakAnswerDiagnosis:
    """Diagnose whether an answer is weak based on extractable features.

    Returns a ``WeakAnswerDiagnosis`` with ``is_weak=True`` if any
    weakness threshold is breached. The ``reasons`` list explains why.
    """
    answer_lower = answer_text.lower()
    words = answer_lower.split()
    word_count = len(words)

    reasons: list[str] = []

    # 1. Hedge-word density
    hedge_count = 0
    for hedge in HEDGE_WORDS:
        if " " in hedge:
            # Multi-word hedge: count phrase occurrences
            hedge_count += len(re.findall(re.escape(hedge), answer_lower))
        else:
            hedge_count += words.count(hedge)
    density = hedge_count / max(word_count, 1)
    if density >= HEDGE_DENSITY_THRESHOLD:
        reasons.append(f"hedge_word_density={density:.2f} (>={HEDGE_DENSITY_THRESHOLD})")

    # 2. Answer length
    if word_count < MIN_ANSWER_LENGTH_WORDS:
        reasons.append(f"answer_too_short={word_count} words (<{MIN_ANSWER_LENGTH_WORDS})")

    # 3. Reference count
    actual_ref_count = 0
    # Count [Source: ...] or [ref: ...] patterns
    actual_ref_count = len(re.findall(r"\[(?:source|ref)[:\s]", answer_lower))
    if expected_ref_count > 0 and actual_ref_count == 0:
        reasons.append(f"no_refs_cited (expected>={expected_ref_count})")

    # 4. Grounding overlap
    overlap = 0.0
    if grounding_texts:
        grounding_words: set[str] = set()
        for gt in grounding_texts:
            grounding_words.update(gt.lower().split())
        # Remove common stop words from overlap calculation
        stop_words = {"the", "a", "an", "is", "are", "was", "were", "be",
                      "been", "being", "have", "has", "had", "do", "does",
                      "did", "will", "would", "could", "should", "may",
                      "might", "shall", "can", "to", "of", "in", "for",
                      "on", "with", "at", "by", "from", "as", "into",
                      "and", "or", "but", "not", "no", "if", "this",
                      "that", "it", "its", "my", "your", "his", "her",
                      "our", "their", "what", "which", "who", "how"}
        answer_content_words = {w for w in words if w not in stop_words and len(w) > 2}
        grounding_content_words = {w for w in grounding_words if w not in stop_words and len(w) > 2}

        if answer_content_words and grounding_content_words:
            overlap = len(answer_content_words & grounding_content_words) / len(answer_content_words)

        if grounding_texts and overlap < GROUNDING_OVERLAP_THRESHOLD:
            reasons.append(f"low_grounding_overlap={overlap:.2f} (<{GROUNDING_OVERLAP_THRESHOLD})")

    # 5. Repetitive uncertainty
    uncertainty_phrases = ["i don't know", "i do not know", "i'm not sure", "i am not sure"]
    uncertainty_count = sum(answer_lower.count(phrase) for phrase in uncertainty_phrases)
    if uncertainty_count >= 2:
        reasons.append(f"repetitive_uncertainty={uncertainty_count}")

    return WeakAnswerDiagnosis(
        hedge_word_density=round(density, 4),
        answer_length_words=word_count,
        ref_count=actual_ref_count,
        expected_ref_count=expected_ref_count,
        grounding_overlap=round(overlap, 4),
        is_weak=bool(reasons),
        reasons=reasons,
    )


# ---------------------------------------------------------------------------
# Escalation
# ---------------------------------------------------------------------------

@dataclass
class EscalationResult:
    """Result of the escalation check.

    ``retried`` is True if a retry was attempted. ``retry_count``
    never exceeds ``MAX_RETRIES`` (1).
    """

    original_diagnosis: WeakAnswerDiagnosis
    retried: bool
    retry_diagnosis: WeakAnswerDiagnosis | None = None
    retry_text: str | None = None
    final_text: str = ""
    retry_count: int = 0


def should_escalate(diagnosis: WeakAnswerDiagnosis) -> bool:
    """Return True if the diagnosis warrants a retry attempt.

    Escalation is warranted when the answer is weak AND at least one
    of: hedge density is high, answer is very short, or no refs were
    cited when expected.
    """
    return diagnosis.is_weak


def build_retry_messages(
    user_input_text: str,
    original_answer: str,
    grounding_texts: Sequence[str] = (),
) -> list[dict[str, str]]:
    """Build the message list for a retry attempt.

    Includes the original answer as context so the model can improve
    on it rather than starting from scratch.
    """
    parts: list[str] = []

    if grounding_texts:
        grounding_block = "\n\n".join(
            f"[Source {i + 1}]\n{text}"
            for i, text in enumerate(grounding_texts)
        )
        parts.append(
            f"Reference material:\n\n{grounding_block}"
        )

    parts.append(
        f"Your previous answer was: {original_answer[:500]}\n\n"
        f"That answer was too vague or hedged. "
        f"Please answer the following question more directly and specifically.\n\n"
        f"Question: {user_input_text}"
    )

    return [
        {"role": "system", "content": RETRY_SYSTEM_PROMPT},
        {"role": "user", "content": "\n\n".join(parts)},
    ]


__all__ = [
    "HEDGE_WORDS",
    "MAX_RETRIES",
    "WeakAnswerDiagnosis",
    "EscalationResult",
    "diagnose_weak_answer",
    "should_escalate",
    "build_retry_messages",
]
