"""Base types for pipeline stages.

A stage takes a ``PipelineContext``, does work (possibly calling the
backend), mutates the context, and returns it. Stages are small,
testable, and independent — the runner composes them.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from ..backends.base import ModelBackend
from ..schemas import GroundingBundle, TurnEnvelope


@dataclass
class PipelineContext:
    """Mutable working state passed through the pipeline.

    Every stage reads what it needs and writes its output into
    ``stage_outputs[stage_name]``. The runner tracks per-stage timing.
    """

    turn: TurnEnvelope
    grounding: GroundingBundle
    backend: ModelBackend
    stage_outputs: dict[str, dict[str, Any]] = field(default_factory=dict)
    stage_timings_ms: dict[str, int] = field(default_factory=dict)
    raw_answer_text: str = ""
    backend_model_id: str = ""
    finish_reason: str | None = None
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    cited_refs: list[str] = field(default_factory=list)
    # M4: memory entries from prior turns, injected into the planner prompt
    memory_context: list[dict[str, str]] = field(default_factory=list)
    # v0.2: optional OpenAI-shaped tool spec passed to the backend, and the
    # tool_calls parsed back out of its response. Tool governance happens in
    # the substrate, not in the pipeline.
    tools: list[dict[str, Any]] | None = None
    tool_calls: list[dict[str, Any]] | None = None


class PipelineStage(Protocol):
    """Each stage implements this protocol."""

    name: str
    timeout_ms: int

    def run(self, ctx: PipelineContext) -> PipelineContext:
        """Do the stage's work and return the (possibly mutated) context."""
        ...
