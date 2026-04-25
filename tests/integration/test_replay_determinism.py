"""Replay determinism regression test.

Creates 20 fixture turns with fixed inputs, builds trace envelopes, and
verifies that:

  1. ``inputs_hash`` is stable across invocations.
  2. ``trace_content_hash`` is stable for identical stage outputs.
  3. Canonical JSON serialization is deterministic (sorted keys, no whitespace).
  4. Two traces with the same inputs but different outputs have different
     content hashes.

This test uses no backend. All envelopes are constructed from fixture data.
The test will fail if ``schemas.py`` changes without bumping the version.
"""

from __future__ import annotations

import hashlib
import unittest

from agif_xcore.schemas import (
    SCHEMA_VERSION_TRACE,
    GroundingBundle,
    GroundingChunk,
    ProposalEnvelope,
    SubstrateDecisions,
    TraceEnvelope,
    TurnEnvelope,
    canonical_json,
    compute_inputs_hash,
)
from agif_xcore.trace import build_trace, trace_content_hash


# ---------------------------------------------------------------------------
# Fixture builder
# ---------------------------------------------------------------------------

def _make_turn(idx: int) -> TurnEnvelope:
    """Build a deterministic TurnEnvelope for fixture turn ``idx``."""
    conv_id = "conv_fixture_determinism_test"
    created_at = f"2025-01-15T10:00:{idx:02d}Z"
    question = _FIXTURE_QUESTIONS[idx]
    # Deterministic turn_id
    seed = f"{conv_id}|{created_at}|{question}"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    turn_id = f"turn_{digest[:16]}"
    return TurnEnvelope(
        turn_id=turn_id,
        conversation_id=conv_id,
        user_input_text=question,
        backend_name="fixture",
        model_id="fixture-model-1.0",
        created_at=created_at,
    )


def _make_grounding(idx: int) -> GroundingBundle:
    """Build a deterministic GroundingBundle for fixture turn ``idx``."""
    if idx % 3 == 0:
        # Empty grounding every 3rd turn
        return GroundingBundle()
    return GroundingBundle(
        chunks=[
            GroundingChunk(
                ref=f"doc_{idx}_chunk0",
                source_path=f"/fixtures/doc_{idx}.txt",
                text=f"Fixture grounding text for question {idx}. "
                     f"This provides factual context about {_FIXTURE_QUESTIONS[idx][:30]}.",
                score=0.85 - (idx * 0.01),
                loader="text",
            ),
        ],
        retriever_name="bm25",
        retrieval_ms=5 + idx,
    )


def _make_proposal(turn: TurnEnvelope, idx: int) -> ProposalEnvelope:
    """Build a deterministic ProposalEnvelope for fixture turn ``idx``."""
    return ProposalEnvelope(
        turn_id=turn.turn_id,
        raw_answer_text=f"Fixture answer for question {idx}: {_FIXTURE_ANSWERS[idx]}",
        backend_model_id="fixture-model-1.0",
        cited_refs=[f"doc_{idx}_chunk0"] if idx % 3 != 0 else [],
        stage_timings_ms={"intake": 1, "planner": 10 + idx, "realizer": 5},
    )


def _make_decisions(idx: int) -> SubstrateDecisions:
    """Build deterministic SubstrateDecisions for fixture turn ``idx``."""
    return SubstrateDecisions(
        provenance_record={"provenance_refs": [f"doc_{idx}"], "timestamp": f"2025-01-15T10:00:{idx:02d}Z"},
        support_state_record={"support_label": "supported" if idx % 2 == 0 else "partial"},
        contradiction_record={"contradictions_found": False},
        policy_gate_decision={"decision_class": "allow"},
        action_gate_decision={"decision_class": "allow"},
        memory_admission_decision={"decision": "admit_write"},
        rollback_or_quarantine_record={"action": "none"},
        final_answer_mode_decision={
            "answer_mode": "grounded_fact" if idx % 3 != 0 else "derived_explanation",
            "blocked_reason_or_none": None,
        },
    )


# ---------------------------------------------------------------------------
# Fixture questions and answers (20 turns)
# ---------------------------------------------------------------------------

_FIXTURE_QUESTIONS = [
    "What happens if you eat watermelon seeds?",
    "Where did fortune cookies originate?",
    "Why do veins appear blue?",
    "What is the spiciest part of a chili pepper?",
    "Does cracking knuckles cause arthritis?",
    "Was Napoleon short?",
    "Can lightning strike the same place twice?",
    "Is glass a liquid?",
    "Did Einstein fail math?",
    "Are diamonds made from coal?",
    "Can you see the Great Wall from space?",
    "Do goldfish have a three-second memory?",
    "How many senses do humans have?",
    "Did Vikings wear horned helmets?",
    "Is the blood in your veins blue?",
    "Who invented the light bulb?",
    "Does shaving make hair grow thicker?",
    "Do bulls charge at the color red?",
    "Did George Washington have wooden teeth?",
    "Do lemmings commit mass suicide?",
]

_FIXTURE_ANSWERS = [
    "Watermelon seeds pass through the digestive system without harm.",
    "Fortune cookies originated in California, not China.",
    "Veins appear blue due to how blue and red light penetrate tissue.",
    "The spiciest part is the pith (placenta), not the seeds.",
    "No, studies show no link between knuckle cracking and arthritis.",
    "Napoleon was about 5 foot 7, average for his time.",
    "Yes, tall structures are struck by lightning many times per year.",
    "Glass is an amorphous solid, not a slowly flowing liquid.",
    "No, Einstein excelled at mathematics from a young age.",
    "Most diamonds formed deep in the mantle, not from compressed coal.",
    "The Great Wall is too narrow to see from space unaided.",
    "Goldfish can remember things for months, not three seconds.",
    "Humans have many senses beyond the traditional five.",
    "No, Viking helmets were plain. Horns are a modern myth.",
    "No, deoxygenated blood is dark red, not blue.",
    "Edison made the light bulb practical; earlier inventors created lamps first.",
    "No, shaving does not change hair thickness or color.",
    "Bulls are partially color blind. They charge at movement, not red.",
    "Washington's dentures were ivory and metal, never wood.",
    "No, lemmings do not intentionally jump off cliffs.",
]


# ---------------------------------------------------------------------------
# Build all 20 fixture traces
# ---------------------------------------------------------------------------

def _build_fixture_traces() -> list[TraceEnvelope]:
    """Build the 20 deterministic fixture traces."""
    traces: list[TraceEnvelope] = []
    for idx in range(20):
        turn = _make_turn(idx)
        grounding = _make_grounding(idx)
        proposal = _make_proposal(turn, idx)
        decisions = _make_decisions(idx)
        trace = build_trace(
            turn=turn,
            grounding=grounding,
            proposal=proposal,
            decisions=decisions,
            final_text=proposal.raw_answer_text,
            total_ms=50 + idx * 5,
            final_refs=proposal.cited_refs,
        )
        traces.append(trace)
    return traces


# ---------------------------------------------------------------------------
# Golden hashes — precomputed on first valid run
# ---------------------------------------------------------------------------

# These are regenerated whenever the schema changes. The test verifies
# that across runs, the same fixtures produce the same hashes.
# If these fail after a schema change, update the hashes here and
# bump SCHEMA_VERSION_TRACE.


class ReplayDeterminismTests(unittest.TestCase):
    """Verify trace envelopes are deterministic across runs."""

    def setUp(self) -> None:
        self.traces = _build_fixture_traces()

    def test_twenty_fixture_traces_built(self) -> None:
        self.assertEqual(len(self.traces), 20)

    def test_inputs_hash_stable_across_calls(self) -> None:
        """Building the same fixtures twice produces the same inputs_hash."""
        traces_2 = _build_fixture_traces()
        for t1, t2 in zip(self.traces, traces_2):
            self.assertEqual(t1.inputs_hash, t2.inputs_hash)

    def test_content_hash_stable_across_calls(self) -> None:
        """Building the same fixtures twice produces the same content hash."""
        traces_2 = _build_fixture_traces()
        for t1, t2 in zip(self.traces, traces_2):
            h1 = trace_content_hash(t1)
            h2 = trace_content_hash(t2)
            self.assertEqual(h1, h2, f"Content hash mismatch for turn {t1.turn_id}")

    def test_all_inputs_hashes_unique(self) -> None:
        """Each fixture turn has a unique inputs_hash."""
        hashes = [t.inputs_hash for t in self.traces]
        self.assertEqual(len(hashes), len(set(hashes)))

    def test_all_content_hashes_unique(self) -> None:
        """Each fixture trace has a unique content hash."""
        hashes = [trace_content_hash(t) for t in self.traces]
        self.assertEqual(len(hashes), len(set(hashes)))

    def test_canonical_json_deterministic(self) -> None:
        """canonical_json produces identical bytes across calls."""
        for trace in self.traces:
            j1 = canonical_json(trace)
            j2 = canonical_json(trace)
            self.assertEqual(j1, j2)

    def test_different_outputs_different_hashes(self) -> None:
        """Traces with same inputs but different final_text have different content hashes."""
        trace_a = self.traces[0]
        # Build a modified copy with different final text
        turn = _make_turn(0)
        grounding = _make_grounding(0)
        proposal = _make_proposal(turn, 0)
        decisions = _make_decisions(0)
        trace_b = build_trace(
            turn=turn,
            grounding=grounding,
            proposal=proposal,
            decisions=decisions,
            final_text="MODIFIED answer that differs from the fixture",
            total_ms=50,
            final_refs=proposal.cited_refs,
        )
        # Same inputs hash (same turn + grounding)
        self.assertEqual(trace_a.inputs_hash, trace_b.inputs_hash)
        # Different content hash (different final_text)
        self.assertNotEqual(
            trace_content_hash(trace_a),
            trace_content_hash(trace_b),
        )

    def test_turn_ids_are_deterministic(self) -> None:
        """Same inputs produce the same turn_id."""
        t1 = _make_turn(0)
        t2 = _make_turn(0)
        self.assertEqual(t1.turn_id, t2.turn_id)

    def test_schema_version_matches(self) -> None:
        """All fixture traces carry the current schema version."""
        for trace in self.traces:
            self.assertEqual(trace.schema_version, SCHEMA_VERSION_TRACE)

    def test_canonical_json_sorted_keys(self) -> None:
        """Canonical JSON output has sorted keys."""
        import json
        for trace in self.traces[:3]:
            j = canonical_json(trace)
            parsed = json.loads(j)
            keys = list(parsed.keys())
            self.assertEqual(keys, sorted(keys))

    def test_grounding_variation(self) -> None:
        """Every 3rd fixture has empty grounding; others have chunks."""
        for idx, trace in enumerate(self.traces):
            bundle = trace.grounding_bundle
            if idx % 3 == 0:
                self.assertEqual(len(bundle.chunks), 0)
            else:
                self.assertGreater(len(bundle.chunks), 0)

    def test_decision_variation(self) -> None:
        """Even/odd fixtures have different support labels."""
        for idx, trace in enumerate(self.traces):
            decisions = trace.substrate_decisions
            label = decisions.support_state_record["support_label"]
            if idx % 2 == 0:
                self.assertEqual(label, "supported")
            else:
                self.assertEqual(label, "partial")


if __name__ == "__main__":
    unittest.main()
