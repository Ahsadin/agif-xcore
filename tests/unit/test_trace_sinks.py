"""Unit tests for trace builders and sinks."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from pathlib import Path

from agif_xcore.schemas import (
    GroundingBundle,
    ProposalEnvelope,
    SubstrateDecisions,
    TurnEnvelope,
    make_turn_id,
)
from agif_xcore.trace import (
    FileJsonlSink,
    MultiSink,
    NullSink,
    StdoutJsonlSink,
    build_trace,
    trace_content_hash,
)


def _build_trace():
    created = TurnEnvelope.now_iso()
    turn = TurnEnvelope(
        turn_id=make_turn_id("conversation_x", created, "hello"),
        conversation_id="conversation_x",
        user_input_text="hello",
        backend_name="stub",
        model_id="stubmodel",
        created_at=created,
    )
    grounding = GroundingBundle()
    proposal = ProposalEnvelope(
        turn_id=turn.turn_id,
        raw_answer_text="hi",
        backend_model_id="stubmodel",
    )
    decisions = SubstrateDecisions()
    return build_trace(
        turn=turn,
        grounding=grounding,
        proposal=proposal,
        decisions=decisions,
        final_text="hi",
        total_ms=1,
    )


class BuildTraceTests(unittest.TestCase):
    def test_inputs_hash_matches_components(self) -> None:
        trace = _build_trace()
        self.assertEqual(len(trace.inputs_hash), 64)
        self.assertEqual(trace.final_text, "hi")
        self.assertEqual(trace.total_ms, 1)

    def test_content_hash_is_stable_across_calls(self) -> None:
        trace = _build_trace()
        a = trace_content_hash(trace)
        b = trace_content_hash(trace)
        self.assertEqual(a, b)
        self.assertEqual(len(a), 64)


class NullSinkTests(unittest.TestCase):
    def test_write_and_close_do_nothing(self) -> None:
        sink = NullSink()
        sink.write(_build_trace())
        sink.close()


class StdoutJsonlSinkTests(unittest.TestCase):
    def test_writes_one_canonical_line_per_trace(self) -> None:
        buffer = io.StringIO()
        sink = StdoutJsonlSink(stream=buffer)
        trace = _build_trace()
        sink.write(trace)
        sink.write(trace)
        lines = buffer.getvalue().strip().splitlines()
        self.assertEqual(len(lines), 2)
        for line in lines:
            parsed = json.loads(line)
            self.assertEqual(parsed["turn_id"], trace.turn_id)


class FileJsonlSinkTests(unittest.TestCase):
    def test_appends_and_creates_parents(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sub" / "trace.jsonl"
            sink = FileJsonlSink(path)
            trace = _build_trace()
            sink.write(trace)
            sink.write(trace)
            sink.close()
            lines = path.read_text().strip().splitlines()
            self.assertEqual(len(lines), 2)
            parsed = json.loads(lines[0])
            self.assertEqual(parsed["turn_id"], trace.turn_id)


class MultiSinkTests(unittest.TestCase):
    def test_fans_out_to_every_sink(self) -> None:
        buf1 = io.StringIO()
        buf2 = io.StringIO()
        multi = MultiSink([StdoutJsonlSink(buf1), StdoutJsonlSink(buf2)])
        trace = _build_trace()
        multi.write(trace)
        self.assertEqual(len(buf1.getvalue().splitlines()), 1)
        self.assertEqual(len(buf2.getvalue().splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
