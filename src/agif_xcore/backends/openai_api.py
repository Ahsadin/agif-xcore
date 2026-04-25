"""Named backend for the real OpenAI API.

This is just ``OpenAICompatBackend`` with the right defaults:
- ``base_url = https://api.openai.com/v1``
- ``api_key`` required (from arg or ``OPENAI_API_KEY`` env)
- ``model_enforcement = prefix`` (OpenAI appends snapshot dates to model ids)

Since OpenAI's API speaks the same ``/v1/chat/completions`` protocol,
no new HTTP code is needed. This file exists so the registry can
resolve ``--backend openai`` to a pre-configured instance.
"""

from __future__ import annotations

import os

from .base import BackendError
from .openai_compat import OpenAICompatBackend, OpenAICompatConfig

OPENAI_BASE_URL = "https://api.openai.com/v1"


class OpenAIBackend(OpenAICompatBackend):
    """Pre-configured backend for the OpenAI API."""

    name = "openai"

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = OPENAI_BASE_URL,
        model_enforcement: str = "prefix",
    ) -> None:
        resolved_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not resolved_key:
            raise BackendError(
                "OpenAI backend requires an API key. "
                "Pass api_key= or set OPENAI_API_KEY env."
            )
        super().__init__(
            OpenAICompatConfig(
                base_url=base_url,
                api_key_or_none=resolved_key,
                model_enforcement=model_enforcement,
                user_agent="agif-xcore/0.1.0 (openai)",
            )
        )
