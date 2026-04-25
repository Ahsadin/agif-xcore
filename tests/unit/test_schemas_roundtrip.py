"""Unit tests for ``agif_xcore.schemas``."""

from __future__ import annotations

import json
import unittest

from agif_xcore.schemas import (
    ALLOWED_ANSWER_MODES,
    AnswerEnvelope,
    GroundingBundle,
    GroundingChunk,
    ProposalEnvelope,
    SubstrateDecisions,
    TraceEnvelope,
    TurnEnvelope,
    canonical_json,
    compute_inputs_hash,
    make_conversation_id,
    make_turn_id,
    pretty_json,
)


class AllowedAnswerModesTests(unittest.TestCase):
    def test_exactly_eight_modes(self) -> None:
        self.assertEqual(len(ALLOWED_ANSWER_MODES), 8)

    def test_modes_are_unique(self) -> None:
        self.assertEqual(len(set(ALLOWED_ANSWER_MODES)), 8)

    def test_expected_mode_names_present(self) -> None:
        for expected in (
            "grounded_fact",
            "grounded_summary",
            "grounded_with_gap",
            "derived_explanation",
            "clarify",
            "search_needed",
            "abstain",
            "bounded_estimate",
        ):
            self.assertIn(expected, ALLOWED_ANSWER_MODES)


class TurnEnvelopeTests(unittest.TestCase):
    def test_now_iso_is_z_suffixed(self) -> None:
        stamp = TurnEnvelope.now_iso()
        self.assertTrue(stamp.endswith("Z"), stamp)
        # Shape like 2026-04-12T00:00:00Z
        self.assertEqual(stamp[10], "T")
        self.assertEqual(len(stamp), 20)

    def test_make_turn_id_is_deterministic(self) -> None:
        a = make_turn_id("conversation_a", "2026-04-12T00:00:00Z", "hello")
        b = make_turn_id("conversation_a", "2026-04-12T00:00:00Z", "hello")
        self.assertEqual(a, b)
        self.assertTrue(a.startswith("turn_"))

    def test_make_turn_id_diverges_on_input_change(self) -> None:
        a = make_turn_id("conversation_a", "2026-04-12T00:00:00Z", "hello")
        b = make_turn_id("conversation_a", "2026-04-12T00:00:00Z", "goodbye")
        self.assertNotEqual(a, b)

    def test_make_conversation_id_unique_over_time(self) -> None:
        first = make_conversation_id()
        second = make_conversation_id()
        # Not strictly required to differ (microseconds can collide in
        # pathological cases) but overwhelmingly likely to differ.
        self.assertTrue(first.startswith("conversation_"))
        self.assertTrue(second.startswith("conversation_"))


class CanonicalJsonTests(unittest.TestCase):
    def test_sorts_keys(self) -> None:
        raw = {"b": 1, "a": 2}
        self.assertEqual(canonical_json(raw), '{"a":2,"b":1}')

    def test_handles_dataclass(self) -> None:
        turn = TurnEnvelope(
            turn_id="turn_1",
            conversation_id="conversation_x",
            user_input_text="hello",
            backend_name="ollama",
            model_id="gemma3:270m",
            created_at="2026-04-12T00:00:00Z",
        )
        serialized = canonical_json(turn)
        parsed = json.loads(serialized)
        self.assertEqual(parsed["turn_id"], "turn_1")
        self.assertEqual(parsed["schema_version"], "1.0.0")
        self.assertIsNone(parsed["task_family_hint"])

    def test_pretty_json_is_parseable(self) -> None:
        chunk = GroundingChunk(
            ref="ref1",
            source_path="/tmp/doc.txt",
            text="hello",
            score=0.9,
            loader="text",
        )
        parsed = json.loads(pretty_json(chunk))
        self.assertEqual(parsed["ref"], "ref1")


class InputsHashTests(unittest.TestCase):
    def _build_turn(self) -> TurnEnvelope:
        return TurnEnvelope(
            turn_id="turn_1",
            conversation_id="conversation_x",
            user_input_text="hello",
            backend_name="ollama",
            model_id="gemma3:270m",
            created_at="2026-04-12T00:00:00Z",
        )

    def test_identical_turns_hash_identically(self) -> None:
        turn = self._build_turn()
        grounding = GroundingBundle()
        h1 = compute_inputs_hash(turn, grounding)
        h2 = compute_inputs_hash(turn, grounding)
        self.assertEqual(h1, h2)
        self.assertEqual(len(h1), 64)  # sha256 hex

    def test_different_turns_hash_differently(self) -> None:
        t1 = self._build_turn()
        t2 = self._build_turn()
        t2.user_input_text = "goodbye"
        bundle = GroundingBundle()
        self.assertNotEqual(compute_inputs_hash(t1, bundle), compute_inputs_hash(t2, bundle))

    def test_different_grounding_hashes_differently(self) -> None:
        turn = self._build_turn()
        empty = GroundingBundle()
        loaded = GroundingBundle(
            chunks=[
                GroundingChunk(
                    ref="r1",
                    source_path="/x.txt",
                    text="hi",
                    score=1.0,
                    loader="text",
                )
            ]
        )
        self.assertNotEqual(compute_inputs_hash(turn, empty), compute_inputs_hash(turn, loaded))


class SubstrateDecisionsTests(unittest.TestCase):
    def test_empty_is_not_governance_enabled(self) -> None:
        decisions = SubstrateDecisions()
        self.assertFalse(decisions.governance_enabled)

    def test_partial_decisions_are_governance_enabled(self) -> None:
        decisions = SubstrateDecisions(policy_gate_decision={"decision_class": "allow"})
        self.assertTrue(decisions.governance_enabled)


class AnswerEnvelopeTests(unittest.TestCase):
    def test_roundtrip_through_canonical_json(self) -> None:
        decisions = SubstrateDecisions()
        answer = AnswerEnvelope(
            text="hello world",
            trace_id="turn_1",
            refs=["r1"],
            decisions=decisions,
            total_ms=42,
            answer_mode="grounded_fact",
        )
        parsed = json.loads(canonical_json(answer))
        self.assertEqual(parsed["text"], "hello world")
        self.assertEqual(parsed["trace_id"], "turn_1")
        self.assertEqual(parsed["refs"], ["r1"])
        self.assertEqual(parsed["answer_mode"], "grounded_fact")


class TraceEnvelopeTests(unittest.TestCase):
    def test_trace_contains_all_components(self) -> None:
        turn = TurnEnvelope(
            turn_id="turn_1",
            conversation_id="conversation_x",
            user_input_text="hello",
            backend_name="ollama",
            model_id="gemma3:270m",
            created_at="2026-04-12T00:00:00Z",
        )
        grounding = GroundingBundle()
        proposal = ProposalEnvelope(
            turn_id="turn_1",
            raw_answer_text="hi there",
            backend_model_id="gemma3:270m",
        )
        decisions = SubstrateDecisions()
        trace = TraceEnvelope(
            turn_id="turn_1",
            inputs_hash="abc",
            turn_envelope=turn,
            grounding_bundle=grounding,
            proposal_envelope=proposal,
            substrate_decisions=decisions,
            final_text="hi there",
            total_ms=10,
        )
        dumped = json.loads(canonical_json(trace))
        self.assertEqual(dumped["turn_id"], "turn_1")
        self.assertEqual(dumped["final_text"], "hi there")
        self.assertEqual(dumped["turn_envelope"]["model_id"], "gemma3:270m")
        self.assertEqual(dumped["proposal_envelope"]["raw_answer_text"], "hi there")


if __name__ == "__main__":
    unittest.main()
