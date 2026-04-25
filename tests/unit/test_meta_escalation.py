"""Tests for weak-answer diagnosis and escalation.

Covers: hedge-word detection, answer length check, ref count check,
grounding overlap, repetitive uncertainty, escalation decision,
retry message construction, and the hard MAX_RETRIES cap.
"""

from __future__ import annotations

import unittest

from agif_xcore.meta.escalation import (
    HEDGE_DENSITY_THRESHOLD,
    HEDGE_WORDS,
    MAX_RETRIES,
    MIN_ANSWER_LENGTH_WORDS,
    EscalationResult,
    WeakAnswerDiagnosis,
    build_retry_messages,
    diagnose_weak_answer,
    should_escalate,
)


class DiagnoseWeakAnswerTests(unittest.TestCase):
    """Test the extractable-feature diagnosis."""

    def test_strong_answer_is_not_weak(self) -> None:
        """A direct, well-referenced answer should not be flagged."""
        answer = (
            "BM25 is a probabilistic ranking function used in information "
            "retrieval. It scores documents by term frequency weighted by "
            "inverse document frequency, with saturation and length "
            "normalization controlled by parameters k1 and b. [Source: ir_textbook]"
        )
        diagnosis = diagnose_weak_answer(answer)
        self.assertFalse(diagnosis.is_weak)
        self.assertEqual(len(diagnosis.reasons), 0)

    def test_hedge_heavy_answer_is_weak(self) -> None:
        """An answer loaded with hedge words should be flagged."""
        answer = (
            "Maybe it depends. I think it might possibly be related to "
            "perhaps some form of ranking, but I'm not sure. It seems "
            "like it could arguably work that way."
        )
        diagnosis = diagnose_weak_answer(answer)
        self.assertTrue(diagnosis.is_weak)
        self.assertTrue(
            any("hedge_word_density" in r for r in diagnosis.reasons),
            f"expected hedge density reason, got {diagnosis.reasons}",
        )
        self.assertGreaterEqual(diagnosis.hedge_word_density, HEDGE_DENSITY_THRESHOLD)

    def test_very_short_answer_is_weak(self) -> None:
        """An extremely short answer should be flagged."""
        diagnosis = diagnose_weak_answer("Yes.")
        self.assertTrue(diagnosis.is_weak)
        self.assertTrue(
            any("answer_too_short" in r for r in diagnosis.reasons),
            f"expected short answer reason, got {diagnosis.reasons}",
        )
        self.assertLess(diagnosis.answer_length_words, MIN_ANSWER_LENGTH_WORDS)

    def test_missing_refs_when_expected(self) -> None:
        """When grounding was provided but the answer cites nothing, flag it."""
        answer = "The backup cadence is daily with weekly full backups."
        diagnosis = diagnose_weak_answer(answer, expected_ref_count=3)
        self.assertTrue(diagnosis.is_weak)
        self.assertTrue(
            any("no_refs_cited" in r for r in diagnosis.reasons),
            f"expected missing refs reason, got {diagnosis.reasons}",
        )

    def test_answer_with_refs_not_flagged(self) -> None:
        """When the answer cites sources, no ref-count flag."""
        answer = (
            "The backup cadence is daily incremental with weekly full backups. "
            "[Source: backup_policy.txt] The retention period is 90 days. "
            "[Source: retention_sop.txt]"
        )
        diagnosis = diagnose_weak_answer(answer, expected_ref_count=2)
        self.assertFalse(
            any("no_refs_cited" in r for r in diagnosis.reasons),
            f"unexpected missing refs reason in {diagnosis.reasons}",
        )

    def test_low_grounding_overlap_is_weak(self) -> None:
        """When the answer has very little overlap with grounding, flag it."""
        grounding = ["backup cadence daily incremental full weekly retention"]
        answer = "I enjoy playing basketball on sunny afternoons in the park."
        diagnosis = diagnose_weak_answer(
            answer, grounding_texts=grounding, expected_ref_count=0,
        )
        self.assertTrue(diagnosis.is_weak)
        self.assertTrue(
            any("grounding_overlap" in r for r in diagnosis.reasons),
            f"expected low overlap reason, got {diagnosis.reasons}",
        )

    def test_good_grounding_overlap_not_flagged(self) -> None:
        """When the answer overlaps well with grounding, no flag."""
        grounding = ["backup cadence daily incremental full weekly retention 90 days"]
        answer = (
            "The backup cadence is daily incremental with weekly full backups. "
            "Retention is 90 days."
        )
        diagnosis = diagnose_weak_answer(answer, grounding_texts=grounding)
        self.assertFalse(
            any("grounding_overlap" in r for r in diagnosis.reasons),
            f"unexpected overlap reason in {diagnosis.reasons}",
        )

    def test_repetitive_uncertainty_is_weak(self) -> None:
        """Repeating 'I don't know' multiple times should be flagged."""
        answer = (
            "I don't know what the backup policy says. "
            "I really don't know. I'm not sure about the details. "
            "I don't know if there is a specific cadence defined."
        )
        diagnosis = diagnose_weak_answer(answer)
        self.assertTrue(diagnosis.is_weak)
        self.assertTrue(
            any("repetitive_uncertainty" in r for r in diagnosis.reasons),
            f"expected repetitive uncertainty reason, got {diagnosis.reasons}",
        )

    def test_single_uncertainty_not_flagged_as_repetitive(self) -> None:
        """A single 'I don't know' is fine — the model is being honest."""
        answer = (
            "I don't know the specific backup cadence for your environment. "
            "You should check with your system administrator for details."
        )
        diagnosis = diagnose_weak_answer(answer)
        self.assertFalse(
            any("repetitive_uncertainty" in r for r in diagnosis.reasons),
            f"unexpected repetitive uncertainty in {diagnosis.reasons}",
        )

    def test_empty_grounding_doesnt_trigger_overlap(self) -> None:
        """No grounding provided → no overlap check."""
        answer = "Some random answer text here for testing purposes."
        diagnosis = diagnose_weak_answer(answer, grounding_texts=[])
        self.assertFalse(
            any("grounding_overlap" in r for r in diagnosis.reasons),
        )


class ShouldEscalateTests(unittest.TestCase):
    def test_escalate_when_weak(self) -> None:
        diagnosis = WeakAnswerDiagnosis(
            hedge_word_density=0.15,
            answer_length_words=3,
            ref_count=0,
            expected_ref_count=2,
            grounding_overlap=0.0,
            is_weak=True,
            reasons=["hedge_word_density=0.15", "answer_too_short"],
        )
        self.assertTrue(should_escalate(diagnosis))

    def test_no_escalate_when_strong(self) -> None:
        diagnosis = WeakAnswerDiagnosis(
            hedge_word_density=0.01,
            answer_length_words=50,
            ref_count=2,
            expected_ref_count=2,
            grounding_overlap=0.5,
            is_weak=False,
            reasons=[],
        )
        self.assertFalse(should_escalate(diagnosis))


class BuildRetryMessagesTests(unittest.TestCase):
    def test_retry_messages_include_original_answer(self) -> None:
        messages = build_retry_messages(
            "What is BM25?",
            "Maybe it is something.",
        )
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[1]["role"], "user")
        self.assertIn("previous answer", messages[1]["content"])
        self.assertIn("Maybe it is something", messages[1]["content"])

    def test_retry_messages_include_grounding(self) -> None:
        messages = build_retry_messages(
            "What is BM25?",
            "I don't know.",
            grounding_texts=["BM25 is a ranking function."],
        )
        self.assertIn("Reference material", messages[1]["content"])
        self.assertIn("ranking function", messages[1]["content"])


class MaxRetriesTests(unittest.TestCase):
    def test_max_retries_is_one(self) -> None:
        """Hard cap: never more than 1 retry per turn."""
        self.assertEqual(MAX_RETRIES, 1)

    def test_hedge_words_tuple_is_populated(self) -> None:
        """Sanity check: hedge words list isn't empty."""
        self.assertGreater(len(HEDGE_WORDS), 10)


if __name__ == "__main__":
    unittest.main()
