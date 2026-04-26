"""Abstract backend contract.

Every backend (Ollama, LM Studio, OpenAI, Anthropic, vLLM, llama.cpp,
Groq, ONNX, ...) implements this small surface. The pipeline never
touches HTTP or inference libraries directly; it only sees this
interface.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


# ---------------------------------------------------------------------------
# Message + response types (intentionally plain dicts for M1 portability)
# ---------------------------------------------------------------------------

ChatMessage = dict[str, str]
"""A chat message. Keys: ``role`` in {"system", "user", "assistant"} and ``content``."""


@dataclass
class BackendResponse:
    """Flat structure representing one non-streaming completion.

    The ``tool_calls`` field is populated only when the upstream model returned
    OpenAI-shaped tool_calls in ``choices[0].message.tool_calls``. v0.1 callers
    can ignore it; it defaults to ``None`` so existing call sites are
    backward-compatible. Whether tool_calls are *governed* (passed to the
    client or stripped) is decided by the substrate, not by the backend.
    """

    text: str
    model_id: str
    finish_reason: str | None = None
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    raw: dict[str, Any] = field(default_factory=dict)
    latency_ms: int = 0
    tool_calls: list[dict[str, Any]] | None = None


# ---------------------------------------------------------------------------
# Error hierarchy
# ---------------------------------------------------------------------------

class BackendError(RuntimeError):
    """Base class for all backend failures. Fail closed, never fall back silently."""


class BackendBlocked(BackendError):
    """The backend is unreachable or refused the request for a known reason."""


class BackendContractError(BackendError):
    """The backend returned a response that does not match the expected shape."""


class BackendModelMismatch(BackendError):
    """The backend returned a different model id than requested.

    The anti-theater rule: approved-model enforcement is *behavioral*, not
    nominal. If we asked for ``gemma3:270m`` and the server returns
    ``llama3.2:latest``, we fail closed. We never pretend we ran against
    the configured model when we didn't.
    """


class BackendTimeout(BackendError):
    """The backend did not respond within the configured timeout."""


# ---------------------------------------------------------------------------
# Protocol
# ---------------------------------------------------------------------------

class ModelBackend(Protocol):
    """The contract every backend must satisfy."""

    name: str  # short identifier used by the registry ("ollama", "openai_compat", ...)

    def complete(
        self,
        messages: list[ChatMessage],
        *,
        model: str,
        temperature: float = 0.0,
        max_tokens: int | None = None,
        timeout_ms: int = 30_000,
        tools: list[dict[str, Any]] | None = None,
    ) -> BackendResponse:
        """Run a non-streaming chat completion and return the response.

        Raises ``BackendError`` (or a subclass) on any failure. Must not
        return partial results; must not silently degrade.

        If ``tools`` is provided (non-empty), the backend forwards the
        OpenAI-shaped tool spec to the upstream and parses ``tool_calls`` from
        the response into ``BackendResponse.tool_calls``. Backends that do not
        support tools must raise ``BackendError`` rather than silently drop
        them. ``tools=None`` and ``tools=[]`` behave identically (no tool
        passthrough).
        """
        ...

    def healthcheck(self) -> dict[str, Any]:
        """Return a small dict describing whether the backend is reachable."""
        ...
