"""Exhaustive tests for the generic answer-mode decision table.

This is the core anti-theater test: the decision table MUST NOT contain
any hardcoded benchmark question strings. It decides purely on
governance state. We enumerate the cross-product of all meaningful
input combinations.
"""

from __future__ import annotations

import unittest

from agif_xcore.answer_mode.decision_table import resolve_answer_mode
from agif_xcore.schemas import ALLOWED_ANSWER_MODES


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve(**overrides) -> dict:
    defaults = {
        "turn_id": "turn_test",
        "support_label": "supported",
        "blocking_flag": False,
        "policy_decision_class": "allow",
        "action_decision_class": "not_applicable",
        "rollback_decision_class": "explicit_none",
        "task_family_hint": None,
        "retrieval_count": 0,
    }
    defaults.update(overrides)
    return resolve_answer_mode(**defaults)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class StructuralBlockTests(unittest.TestCase):
    def test_quarantine_always_abstains(self) -> None:
        result = _resolve(rollback_decision_class="quarantine")
        self.assertEqual(result["answer_mode"], "abstain")
        self.assertEqual(result["authorization_status"], "quarantined")

    def test_policy_block_always_abstains(self) -> None:
        result = _resolve(policy_decision_class="block")
        self.assertEqual(result["answer_mode"], "abstain")
        self.assertEqual(result["blocked_reason_or_none"], "policy_block")

    def test_quarantine_overrides_policy_block(self) -> None:
        result = _resolve(
            rollback_decision_class="quarantine",
            policy_decision_class="block",
        )
        self.assertEqual(result["answer_mode"], "abstain")
        self.assertEqual(result["authorization_status"], "quarantined")


class EvidenceStateTests(unittest.TestCase):
    def test_ambiguous_needs_clarification(self) -> None:
        result = _resolve(support_label="ambiguous_needs_clarification")
        self.assertEqual(result["answer_mode"], "clarify")

    def test_unsupported_missing_no_retrieval(self) -> None:
        result = _resolve(
            support_label="unsupported_missing_evidence",
            retrieval_count=0,
        )
        self.assertEqual(result["answer_mode"], "search_needed")

    def test_unsupported_missing_with_retrieval(self) -> None:
        result = _resolve(
            support_label="unsupported_missing_evidence",
            retrieval_count=3,
        )
        self.assertEqual(result["answer_mode"], "grounded_with_gap")

    def test_conflicting_evidence(self) -> None:
        result = _resolve(support_label="unsupported_conflicting_evidence")
        self.assertEqual(result["answer_mode"], "abstain")

    def test_blocking_flag_forces_abstain(self) -> None:
        result = _resolve(
            support_label="supported",
            blocking_flag=True,
        )
        self.assertEqual(result["answer_mode"], "abstain")

    def test_off_scope(self) -> None:
        result = _resolve(support_label="unsupported_off_scope")
        self.assertEqual(result["answer_mode"], "abstain")

    def test_blocked_by_policy_support_label(self) -> None:
        result = _resolve(support_label="blocked_by_policy")
        self.assertEqual(result["answer_mode"], "abstain")


class SoftenedActionTests(unittest.TestCase):
    def test_soften_produces_derived_explanation(self) -> None:
        result = _resolve(action_decision_class="soften")
        self.assertEqual(result["answer_mode"], "derived_explanation")


class SupportedContentTests(unittest.TestCase):
    def test_supported_no_retrieval_derives(self) -> None:
        result = _resolve(support_label="supported", retrieval_count=0)
        self.assertEqual(result["answer_mode"], "derived_explanation")

    def test_supported_with_retrieval_grounded_fact(self) -> None:
        result = _resolve(support_label="supported", retrieval_count=3)
        self.assertEqual(result["answer_mode"], "grounded_fact")

    def test_summary_hint_with_retrieval(self) -> None:
        result = _resolve(
            support_label="supported",
            retrieval_count=3,
            task_family_hint="summary",
        )
        self.assertEqual(result["answer_mode"], "grounded_summary")

    def test_summary_hint_without_retrieval_derives(self) -> None:
        result = _resolve(
            support_label="supported",
            retrieval_count=0,
            task_family_hint="summary",
        )
        self.assertEqual(result["answer_mode"], "derived_explanation")

    def test_estimate_hint(self) -> None:
        result = _resolve(
            support_label="supported",
            task_family_hint="estimate",
        )
        self.assertEqual(result["answer_mode"], "bounded_estimate")


class OutputShapeTests(unittest.TestCase):
    def test_all_outputs_are_valid_modes(self) -> None:
        """Enumerate every meaningful state combination and verify the
        output is always one of the 8 allowed modes."""
        support_labels = [
            "supported", "ambiguous_needs_clarification",
            "unsupported_missing_evidence", "unsupported_off_scope",
            "unsupported_conflicting_evidence", "blocked_by_policy",
        ]
        blocking_flags = [False, True]
        policy_classes = ["allow", "block", "restrict_non_decisive"]
        action_classes = ["not_applicable", "allow", "block", "soften"]
        rollback_classes = ["explicit_none", "rollback", "quarantine"]
        retrieval_counts = [0, 3]
        hints = [None, "summary", "estimate"]

        count = 0
        for sl in support_labels:
            for bf in blocking_flags:
                for pc in policy_classes:
                    for ac in action_classes:
                        for rc in rollback_classes:
                            for ret in retrieval_counts:
                                for hint in hints:
                                    result = _resolve(
                                        support_label=sl,
                                        blocking_flag=bf,
                                        policy_decision_class=pc,
                                        action_decision_class=ac,
                                        rollback_decision_class=rc,
                                        retrieval_count=ret,
                                        task_family_hint=hint,
                                    )
                                    mode = result["answer_mode"]
                                    self.assertIn(
                                        mode,
                                        ALLOWED_ANSWER_MODES,
                                        f"invalid mode {mode!r} for "
                                        f"sl={sl} bf={bf} pc={pc} "
                                        f"ac={ac} rc={rc} ret={ret} "
                                        f"hint={hint}",
                                    )
                                    count += 1
        # Verify we tested a non-trivial cross-product
        self.assertGreater(count, 2000)


class NoHardcodedStringsTest(unittest.TestCase):
    """Verify the decision table source contains no benchmark-specific strings.

    This is the CI lint rule as a unit test.
    """

    def test_no_benchmark_question_strings_in_source(self) -> None:
        import inspect
        from agif_xcore.answer_mode import decision_table

        source = inspect.getsource(decision_table)
        forbidden = [
            "req-g-004",
            "req-d-006",
            "req-e-003",
            "for production, what backup cadence",
            "what does req-",
            "before opening a cashier shift",
            "which audit fields must the deterministic",
        ]
        for pattern in forbidden:
            self.assertNotIn(
                pattern.lower(),
                source.lower(),
                f"decision_table.py contains forbidden benchmark string: {pattern!r}",
            )


if __name__ == "__main__":
    unittest.main()
