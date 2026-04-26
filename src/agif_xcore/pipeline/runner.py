"""Pipeline runner.

Composes ordered stages, enforces per-stage + global budgets, and
produces a ``ProposalEnvelope`` ready to be fed to the substrate.

In M1 the stage list is fixed at ``(intake, planner, realizer)``. The
``Runner`` class is still written to be extensible so M2 can add
retrieval / semantic / critic stages without touching consumers.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

from ..backends.base import BackendError, ModelBackend
from ..schemas import GroundingBundle, ProposalEnvelope, TurnEnvelope
from .intake import IntakeStage
from .planner import PlannerStage
from .realizer import RealizerStage
from .stage import PipelineContext, PipelineStage


@dataclass
class PipelineBudget:
    """Per-stage and global time budgets in milliseconds."""

    global_ms: int = 60_000
    per_stage_ms: dict[str, int] = field(default_factory=dict)


class PipelineTimeoutError(BackendError):
    """Raised when the global budget runs out mid-pipeline."""


class Runner:
    """The M1 three-stage runner."""

    def __init__(
        self,
        stages: list[PipelineStage] | None = None,
        budget: PipelineBudget | None = None,
    ) -> None:
        self._stages: list[PipelineStage] = stages or _default_m1_stages()
        self._budget = budget or PipelineBudget()

    @property
    def stage_names(self) -> list[str]:
        return [stage.name for stage in self._stages]

    def run(
        self,
        *,
        turn: TurnEnvelope,
        grounding: GroundingBundle,
        backend: ModelBackend,
        memory_context: list[dict[str, str]] | None = None,
        tools: list[dict] | None = None,
    ) -> ProposalEnvelope:
        ctx = PipelineContext(
            turn=turn, grounding=grounding, backend=backend,
            memory_context=memory_context or [],
            tools=tools,
        )
        pipeline_started = time.perf_counter()

        for stage in self._stages:
            self._check_global_budget(pipeline_started)

            started = time.perf_counter()
            try:
                ctx = stage.run(ctx)
            except BackendError:
                # Record the failing stage timing so the trace still has a
                # row for every attempted stage, then re-raise unchanged.
                ctx.stage_timings_ms[stage.name] = int(
                    (time.perf_counter() - started) * 1000
                )
                raise
            ctx.stage_timings_ms[stage.name] = int(
                (time.perf_counter() - started) * 1000
            )

        return _context_to_proposal(ctx)

    def _check_global_budget(self, pipeline_started_perf: float) -> None:
        elapsed_ms = int((time.perf_counter() - pipeline_started_perf) * 1000)
        if elapsed_ms >= self._budget.global_ms:
            raise PipelineTimeoutError(
                f"pipeline global budget exceeded: {elapsed_ms}ms >= {self._budget.global_ms}ms"
            )


def _default_m1_stages() -> list[PipelineStage]:
    return [IntakeStage(), PlannerStage(), RealizerStage()]


def _context_to_proposal(ctx: PipelineContext) -> ProposalEnvelope:
    return ProposalEnvelope(
        turn_id=ctx.turn.turn_id,
        raw_answer_text=ctx.raw_answer_text,
        backend_model_id=ctx.backend_model_id or ctx.turn.model_id,
        cited_refs=list(ctx.cited_refs),
        stage_outputs=dict(ctx.stage_outputs),
        stage_timings_ms=dict(ctx.stage_timings_ms),
        finish_reason=ctx.finish_reason,
        prompt_tokens=ctx.prompt_tokens,
        completion_tokens=ctx.completion_tokens,
        tool_calls=list(ctx.tool_calls) if ctx.tool_calls else None,
    )
