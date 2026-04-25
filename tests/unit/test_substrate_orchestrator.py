"""Tests for the substrate orchestrator (run_substrate).

Verifies the 9-stage chain executes in order and produces correct
decisions for representative scenarios.
"""

from __future__ import annotations

import unittest

from agif_xcore.substrate import run_substrate


def _turn(text: str = "hello", **overrides) -> dict:
    defaults = {
        "turn_id": "turn_test",
        "conversation_id": "conversation_test",
        "user_input_text": text,
        "admitted_corpus_refs": ["doc1"],
        "policy_context_refs_or_none": None,
        "prior_state_refs_or_none": None,
        "requested_action_class_or_none": None,
        "task_family": None,
    }
    defaults.update(overrides)
    return defaults


def _proposal(**overrides) -> dict:
    defaults = {
        "proposal_id": "proposal:turn_test",
        "turn_id": "turn_test",
        "proposed_content_summary_or_none": "test answer",
        "proposed_action_or_none": None,
        "proposed_answer_mode_candidates": ["grounded_fact"],
        "proposed_evidence_refs_or_none": ["doc1"],
        "memory_suggestion_or_none": None,
    }
    defaults.update(overrides)
    return defaults


class SupportedTurnTests(unittest.TestCase):
    def test_supported_turn_with_retrieval_grounds(self) -> None:
        result = run_substrate(
            turn_envelope=_turn(),
            proposal_envelope=_proposal(),
            retrieval_count=3,
        )
        self.assertEqual(result["final_answer_mode"], "grounded_fact")
        self.assertEqual(result["authorization_status"], "authorized")
        self.assertEqual(
            result["support_state_record"]["support_label"],
            "supported",
        )
        self.assertFalse(result["contradiction_record"]["blocking_flag"])
        self.assertEqual(result["policy_gate_decision"]["decision_class"], "allow")

    def test_supported_turn_without_retrieval_derives(self) -> None:
        result = run_substrate(
            turn_envelope=_turn(),
            proposal_envelope=_proposal(),
            retrieval_count=0,
        )
        self.assertEqual(result["final_answer_mode"], "derived_explanation")


class MissingEvidenceTests(unittest.TestCase):
    def test_missing_evidence_with_no_grounding_needs_search(self) -> None:
        result = run_substrate(
            turn_envelope=_turn(),
            proposal_envelope=_proposal(
                proposed_evidence_refs_or_none=["missing_doc"],
            ),
            retrieval_count=0,
        )
        self.assertEqual(result["final_answer_mode"], "search_needed")
        self.assertEqual(
            result["support_state_record"]["support_label"],
            "unsupported_missing_evidence",
        )


class PolicyBlockTests(unittest.TestCase):
    def test_policy_block_forces_abstain(self) -> None:
        result = run_substrate(
            turn_envelope=_turn(
                policy_context_refs_or_none=["policy:block:test"],
            ),
            proposal_envelope=_proposal(),
            retrieval_count=3,
        )
        self.assertEqual(result["final_answer_mode"], "abstain")
        self.assertEqual(
            result["policy_gate_decision"]["decision_class"],
            "block",
        )


class ContradictionTests(unittest.TestCase):
    def test_blocking_conflict_forces_abstain(self) -> None:
        result = run_substrate(
            turn_envelope=_turn(
                prior_state_refs_or_none=["conflict:entry_a"],
            ),
            proposal_envelope=_proposal(),
            retrieval_count=3,
        )
        self.assertEqual(result["final_answer_mode"], "abstain")
        self.assertTrue(result["contradiction_record"]["blocking_flag"])


class CorruptStateTests(unittest.TestCase):
    def test_corrupt_state_quarantines(self) -> None:
        result = run_substrate(
            turn_envelope=_turn(
                prior_state_refs_or_none=["state:corrupt:db_entry"],
            ),
            proposal_envelope=_proposal(),
            retrieval_count=3,
        )
        self.assertEqual(result["final_answer_mode"], "abstain")
        self.assertEqual(result["authorization_status"], "quarantined")
        self.assertEqual(
            result["rollback_or_quarantine_record"]["decision_class"],
            "quarantine",
        )


class AllNineStagesPresent(unittest.TestCase):
    def test_result_contains_all_nine_records(self) -> None:
        result = run_substrate(
            turn_envelope=_turn(),
            proposal_envelope=_proposal(),
        )
        expected_keys = {
            "provenance_record",
            "support_state_record",
            "contradiction_record",
            "policy_gate_decision",
            "action_gate_decision",
            "memory_admission_decision",
            "rollback_or_quarantine_record",
            "final_answer_mode_decision",
            "final_answer_mode",
            "authorization_status",
        }
        self.assertTrue(expected_keys.issubset(result.keys()), result.keys())


if __name__ == "__main__":
    unittest.main()
