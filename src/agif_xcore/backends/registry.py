"""Backend name -> instance resolver.

One small function the CLI and client use to translate ``--backend
ollama`` into a live ``OllamaBackend``. Keeping this in its own module
means we can register new backends in M3 (OpenAI, Anthropic) and M5
(ONNX) without touching the client.
"""

from __future__ import annotations

import os
from typing import Any

from .base import BackendError, ModelBackend
from .ollama import DEFAULT_OLLAMA_BASE_URL, OllamaBackend
from .openai_api import OpenAIBackend
from .openai_compat import OpenAICompatBackend, OpenAICompatConfig


# Names recognised by ``resolve_backend``. Keep alphabetised.
_REGISTERED = {"ollama", "onnx", "openai", "openai_compat"}


def available_backends() -> list[str]:
    """Return the list of backend names the registry knows about."""
    return sorted(_REGISTERED)


def resolve_backend(
    name: str,
    *,
    base_url: str | None = None,
    api_key: str | None = None,
    model_enforcement: str = "strict",
) -> ModelBackend:
    """Build a backend instance from a short name + optional overrides.

    The M1 defaults are intentionally narrow. Environment variables are
    read only as a last resort — the explicit argument always wins.
    """
    key = (name or "").strip().lower()

    if key == "ollama":
        return OllamaBackend(
            base_url=base_url or os.environ.get("OLLAMA_HOST") or DEFAULT_OLLAMA_BASE_URL,
            api_key=api_key or os.environ.get("OLLAMA_API_KEY") or None,
            model_enforcement=model_enforcement,
        )

    if key == "onnx":
        from .onnx import OnnxBackend
        model_path = base_url or os.environ.get("ONNX_MODEL_PATH")
        if not model_path:
            raise BackendError(
                "backend 'onnx' requires base_url (as model_path) or ONNX_MODEL_PATH env"
            )
        return OnnxBackend(model_path=model_path)

    if key == "openai":
        return OpenAIBackend(
            api_key=api_key,
            base_url=base_url or "https://api.openai.com/v1",
            model_enforcement=model_enforcement or "prefix",
        )

    if key == "openai_compat":
        resolved_base_url = base_url or os.environ.get("OPENAI_COMPAT_BASE_URL")
        if not resolved_base_url:
            raise BackendError(
                "backend 'openai_compat' requires base_url or OPENAI_COMPAT_BASE_URL env"
            )
        return OpenAICompatBackend(
            OpenAICompatConfig(
                base_url=resolved_base_url,
                api_key_or_none=api_key or os.environ.get("OPENAI_COMPAT_API_KEY"),
                model_enforcement=model_enforcement,
            )
        )

    raise BackendError(
        f"unknown backend '{name}'. Available: {', '.join(available_backends())}"
    )


__all__ = ["available_backends", "resolve_backend"]

# Keep a stable reference so static analysers don't drop the import.
_ = Any
