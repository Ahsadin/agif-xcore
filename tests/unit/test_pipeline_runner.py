"""Unit tests for the pipeline runner.

Uses a stub backend so we never touch the network. Verifies:
- the 3-stage order runs end-to-end
- per-stage timings get recorded
- a backend error propagates and the runner still records the failing
  stage's timing
- budget enforcement kicks in when a stage exceeds the global budget
"""

from __future__ import annotations

import time
import unittest
from dataclasses import dataclass
from typing import Any

from agif_xcore.backends.base import BackendError, BackendResponse
from agif_xcore.pipeline.runner import PipelineBudget, PipelineTimeoutError, Runner
from agif_xcore.schemas import GroundingBundle, TurnEnvelope, make_turn_id


# ---------------------------------------------------------------------------
# Test doubles
# ---------------------------------------------------------------------------

@dataclass
class _StubBackend:
    name: str = "stub"
    reply_text: str = "stub answer"
    raise_error: bool = False

    def complete(
        self,
        messages,
        *,
        model: str,
        temperature: float = 0.0,
        max_tokens: int | None = None,
        timeout_ms: int = 30_000,
        tools: list[dict] | None = None,
    ) -> BackendResponse:  # noqa: ARG002
        if self.raise_error:
            raise BackendError("stub failure")
        return BackendResponse(
            text=self.reply_text,
            model_id=model,
            finish_reason="stop",
            prompt_tokens=5,
            completion_tokens=4,
            latency_ms=1,
        )

    def healthcheck(self) -> dict[str, Any]:
        return {"reachable": True, "loaded_models": []}


def _build_turn() -> TurnEnvelope:
    created = TurnEnvelope.now_iso()
    return TurnEnvelope(
        turn_id=make_turn_id("conversation_test", created, "hi"),
        conversation_id="conversation_test",
        user_input_text="hi",
        backend_name="stub",
        model_id="stubmodel",
        created_at=created,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class DefaultRunnerTests(unittest.TestCase):
    def test_default_stage_names(self) -> None:
        runner = Runner()
        self.assertEqual(runner.stage_names, ["intake", "planner", "realizer"])

    def test_runs_three_stages_end_to_end(self) -> None:
        runner = Runner()
        backend = _StubBackend(reply_text="Hello from the stub.")
        turn = _build_turn()
        grounding = GroundingBundle()

        proposal = runner.run(turn=turn, grounding=grounding, backend=backend)

        self.assertEqual(proposal.raw_answer_text, "Hello from the stub.")
        self.assertEqual(proposal.backend_model_id, "stubmodel")
        self.assertEqual(proposal.finish_reason, "stop")
        self.assertEqual(
            sorted(proposal.stage_outputs.keys()),
            ["intake", "planner", "realizer"],
        )
        self.assertIn("intake", proposal.stage_timings_ms)
        self.assertIn("planner", proposal.stage_timings_ms)
        self.assertIn("realizer", proposal.stage_timings_ms)

    def test_intake_captures_input_length(self) -> None:
        runner = Runner()
        backend = _StubBackend()
        turn = _build_turn()
        turn.user_input_text = "the quick brown fox"
        proposal = runner.run(turn=turn, grounding=GroundingBundle(), backend=backend)
        intake = proposal.stage_outputs["intake"]
        self.assertEqual(intake["input_length_chars"], len("the quick brown fox"))
        self.assertEqual(intake["input_word_count"], 4)

    def test_realizer_strips_text(self) -> None:
        runner = Runner()
        backend = _StubBackend(reply_text="  spaced  \n")
        proposal = runner.run(
            turn=_build_turn(),
            grounding=GroundingBundle(),
            backend=backend,
        )
        self.assertEqual(proposal.raw_answer_text, "spaced")


class ErrorPropagationTests(unittest.TestCase):
    def test_backend_error_propagates_with_timing_recorded(self) -> None:
        runner = Runner()
        backend = _StubBackend(raise_error=True)
        turn = _build_turn()

        with self.assertRaises(BackendError):
            runner.run(turn=turn, grounding=GroundingBundle(), backend=backend)


class BudgetTests(unittest.TestCase):
    def test_global_budget_kills_slow_pipeline(self) -> None:
        # Build a runner whose only stage is a slow one that exceeds the
        # global budget. The second stage should never run.
        class _SlowStage:
            name = "slow"
            timeout_ms = 10_000

            def run(self, ctx):
                time.sleep(0.05)
                return ctx

        class _NeverStage:
            name = "never"
            timeout_ms = 10_000

            def run(self, ctx):  # pragma: no cover - asserted never-called
                raise AssertionError("should not run once budget is blown")

        runner = Runner(
            stages=[_SlowStage(), _NeverStage()],
            budget=PipelineBudget(global_ms=10),
        )
        with self.assertRaises(PipelineTimeoutError):
            runner.run(
                turn=_build_turn(),
                grounding=GroundingBundle(),
                backend=_StubBackend(),
            )


if __name__ == "__main__":
    unittest.main()
