"""Stage 1 — intake.

Normalises the incoming turn: strips whitespace, measures length,
records basic features for later stages. No backend call here; this is
the "cheap pre-processing" stage. In M2 the 6-stage pipeline adds a
real intake neural assist; M1 is deliberately lightweight.
"""

from __future__ import annotations

from .stage import PipelineContext


class IntakeStage:
    name = "intake"
    timeout_ms = 100  # this stage never hits the network

    def run(self, ctx: PipelineContext) -> PipelineContext:
        text = (ctx.turn.user_input_text or "").strip()
        ctx.stage_outputs[self.name] = {
            "normalized_input": text,
            "input_length_chars": len(text),
            "input_word_count": len(text.split()),
            "grounding_chunk_count": len(ctx.grounding.chunks),
        }
        return ctx
