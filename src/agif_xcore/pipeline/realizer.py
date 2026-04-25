"""Stage 3 — realizer.

In M1 the realizer is a thin pass-through: whatever the planner stage
produced becomes the final natural-language answer. M2 will add a
mode-aware re-shaping layer here (grounded_fact vs clarify vs abstain
vs bounded_estimate templates), but for M1 we deliberately do not
re-shape — the planner's text is what the user sees.

We keep the stage so the pipeline shape is already correct; swapping in
the real realizer in M2 is then just replacing this file.
"""

from __future__ import annotations

from .stage import PipelineContext


class RealizerStage:
    name = "realizer"
    timeout_ms = 100  # pass-through; never touches the network in M1

    def run(self, ctx: PipelineContext) -> PipelineContext:
        final_text = (ctx.raw_answer_text or "").strip()
        ctx.stage_outputs[self.name] = {
            "final_length_chars": len(final_text),
            "reshaped": False,  # M1 does not re-shape
            "mode_applied": "grounded_fact",  # nominal until substrate lands in M2
        }
        # Overwrite raw_answer_text with the normalised string. In M2 this
        # will diverge when abstain/clarify templates re-shape the text.
        ctx.raw_answer_text = final_text
        return ctx
