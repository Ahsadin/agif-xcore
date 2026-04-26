"""Stage 2 — planner.

In M1 this is the **only** stage that calls the backend. It assembles
a minimal system + user message pair and runs one completion. The raw
answer text is stored on the context for the realizer stage.

The system prompt is intentionally plain English, not a role-play card.
M2 will add a richer prompt chain (retrieval → semantic → planner →
critic), but the M1 planner is honest about what it is: a single
wrapped call to the backend.
"""

from __future__ import annotations

from ..backends.base import BackendError, ChatMessage
from .stage import PipelineContext


DEFAULT_SYSTEM_PROMPT = "Answer concisely."

# Longer prompt for larger models (7B+). Small models (< 1B) choke on
# verbose system prompts and respond "Okay, I understand" instead of
# answering. The default is kept minimal so it works everywhere.
DETAILED_SYSTEM_PROMPT = (
    "You are a precise and helpful assistant. "
    "Answer the user's question clearly and concisely. "
    "If the question is ambiguous, ask for the one clarification that would "
    "let you answer well. "
    "If you do not know the answer, say so directly rather than guessing."
)


class PlannerStage:
    name = "planner"
    timeout_ms = 30_000

    def __init__(self, system_prompt: str = DEFAULT_SYSTEM_PROMPT) -> None:
        self._system_prompt = system_prompt

    def run(self, ctx: PipelineContext) -> PipelineContext:
        # Build the user prompt with optional memory + grounding context
        prompt_parts: list[str] = []

        # M4: inject memory context from prior turns
        if ctx.memory_context:
            memory_text = "\n".join(
                f"- {entry['content']}"
                for entry in ctx.memory_context
            )
            prompt_parts.append(
                f"Earlier in our conversation, the following was discussed:\n"
                f"{memory_text}\n"
                f"Use this context if relevant to the question below."
            )

        # Augment the user prompt with grounding context when available
        if ctx.grounding.chunks:
            grounding_text = "\n\n".join(
                f"[Source: {chunk.ref}]\n{chunk.text}"
                for chunk in ctx.grounding.chunks
            )
            prompt_parts.append(
                f"Use the following reference material to answer the question. "
                f"Base your answer on this material and cite the source names.\n\n"
                f"--- Reference Material ---\n{grounding_text}\n"
                f"--- End Reference Material ---"
            )
            ctx.cited_refs = [chunk.ref for chunk in ctx.grounding.chunks]

        prompt_parts.append(f"Question: {ctx.turn.user_input_text}")

        # If we have context, join parts; otherwise use raw question
        if len(prompt_parts) > 1:
            user_content = "\n\n".join(prompt_parts)
        else:
            user_content = ctx.turn.user_input_text

        messages: list[ChatMessage] = [
            {"role": "system", "content": self._system_prompt},
            {"role": "user", "content": user_content},
        ]

        response = ctx.backend.complete(
            messages,
            model=ctx.turn.model_id,
            temperature=ctx.turn.temperature,
            max_tokens=ctx.turn.max_tokens,
            timeout_ms=self.timeout_ms,
            tools=ctx.tools,
        )

        ctx.raw_answer_text = response.text
        ctx.backend_model_id = response.model_id
        ctx.finish_reason = response.finish_reason
        ctx.prompt_tokens = response.prompt_tokens
        ctx.completion_tokens = response.completion_tokens
        ctx.tool_calls = response.tool_calls

        ctx.stage_outputs[self.name] = {
            "system_prompt_hash": _hash_prompt(self._system_prompt),
            "backend_name": getattr(ctx.backend, "name", "unknown"),
            "returned_model_id": response.model_id,
            "backend_latency_ms": response.latency_ms,
            "finish_reason": response.finish_reason,
            "raw_length_chars": len(response.text),
        }
        return ctx


def _hash_prompt(prompt: str) -> str:
    """Short, stable prompt identifier for the trace. Not a secret.

    Avoids dragging the full prompt into every trace row while keeping
    the trace auditable: identical prompts produce identical hashes.
    """
    import hashlib

    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:16]


# Re-export the error so consumers of this module don't have to know
# where it lives. Keeps the import graph small.
__all__ = ["PlannerStage", "DEFAULT_SYSTEM_PROMPT", "BackendError"]
