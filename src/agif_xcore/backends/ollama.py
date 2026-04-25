"""Ollama specialization.

Ollama exposes **two** compatible APIs at the same port:

- OpenAI-compatible: ``/v1/chat/completions``
- Native: ``/api/chat``

For M1 we just subclass ``OpenAICompatBackend`` with the right default
base URL. A future release can switch to the native path if we want
Ollama-specific features like structured outputs or tool-calling
differences; both endpoints coexist.
"""

from __future__ import annotations

from .openai_compat import OpenAICompatBackend, OpenAICompatConfig


DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434/v1"


class OllamaBackend(OpenAICompatBackend):
    """OpenAI-compat backend with Ollama defaults.

    Accepts either a full URL like ``http://localhost:11434/v1`` or a
    host shorthand like ``localhost`` / ``localhost:11434``. The caller
    can override ``model_enforcement`` if running a tag with a server-
    generated suffix.
    """

    name = "ollama"

    def __init__(
        self,
        base_url: str = DEFAULT_OLLAMA_BASE_URL,
        *,
        api_key: str | None = None,
        model_enforcement: str = "strict",
    ) -> None:
        normalized = _normalize_ollama_base_url(base_url)
        super().__init__(
            OpenAICompatConfig(
                base_url=normalized,
                api_key_or_none=api_key,
                model_enforcement=model_enforcement,
                user_agent="agif-xcore/0.1.0 (ollama)",
            )
        )


def _normalize_ollama_base_url(base_url: str) -> str:
    """Accept loose inputs and return a canonical ``http://host:port/v1``."""
    raw = (base_url or "").strip()
    if not raw:
        return DEFAULT_OLLAMA_BASE_URL
    if "://" not in raw:
        raw = f"http://{raw}"
    raw = raw.rstrip("/")
    if not raw.endswith("/v1"):
        raw = f"{raw}/v1"
    return raw
