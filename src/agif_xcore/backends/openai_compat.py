"""OpenAI-compatible chat completions backend.

Covers **any** server that speaks ``POST /v1/chat/completions``:
Ollama (via ``http://localhost:11434/v1``), LM Studio, vLLM, llama.cpp's
``llama-server``, Groq, and OpenAI itself.

This module is a deliberate **rewrite** of the X1 file
``projects/agif_x1_terminal_chat_demo/04_execution/lm_studio_runner_client.py``.
The X1 version is 472 lines, hardcodes ``APPROVED_MODEL_MATCH_TOKENS =
("gemma", "270m")``, and blocks any model that does not contain those
tokens. Here we keep the discovery + request + contract-validation
pattern but strip the hardcodes. The caller specifies the model by name,
and *behavioral* model enforcement lives in ``BackendModelMismatch``
(see base.py).

M1 uses ``urllib.request`` (stdlib only) so the library has zero runtime
dependencies. M3 will add an async variant using ``httpx``.
"""

from __future__ import annotations

import json
import socket
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from .base import (
    BackendBlocked,
    BackendContractError,
    BackendError,
    BackendModelMismatch,
    BackendResponse,
    BackendTimeout,
    ChatMessage,
)


DEFAULT_TIMEOUT_MS = 30_000


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class OpenAICompatConfig:
    """Immutable configuration for one backend instance.

    Unlike the X1 client, nothing here is model-specific. The model name
    is passed per-call through ``complete(model=...)`` so one backend
    instance can serve any model the server has loaded.
    """

    base_url: str
    api_key_or_none: str | None = None
    model_enforcement: str = "strict"  # "strict" | "prefix" | "off"
    user_agent: str = "agif-xcore/0.1.0"


# ---------------------------------------------------------------------------
# Backend
# ---------------------------------------------------------------------------

class OpenAICompatBackend:
    """Non-streaming chat completion client over ``/v1/chat/completions``."""

    name = "openai_compat"

    def __init__(self, config: OpenAICompatConfig) -> None:
        if not config.base_url:
            raise BackendError("OpenAICompatBackend requires a non-empty base_url")
        self._config = OpenAICompatConfig(
            base_url=config.base_url.rstrip("/"),
            api_key_or_none=config.api_key_or_none,
            model_enforcement=config.model_enforcement,
            user_agent=config.user_agent,
        )

    # ------------------------------------------------------------------
    # Public API (ModelBackend protocol)
    # ------------------------------------------------------------------

    def complete(
        self,
        messages: list[ChatMessage],
        *,
        model: str,
        temperature: float = 0.0,
        max_tokens: int | None = None,
        timeout_ms: int = DEFAULT_TIMEOUT_MS,
    ) -> BackendResponse:
        if not model:
            raise BackendContractError("model is required")
        if not messages:
            raise BackendContractError("messages must be non-empty")

        body: dict[str, Any] = {
            "model": model,
            "messages": list(messages),
            "temperature": float(temperature),
            "stream": False,
        }
        if max_tokens is not None:
            body["max_tokens"] = int(max_tokens)

        url = f"{self._config.base_url}/chat/completions"
        started = time.perf_counter()
        payload = self._request_json(
            "POST",
            url,
            body=body,
            timeout_s=timeout_ms / 1000.0,
        )
        latency_ms = int((time.perf_counter() - started) * 1000)

        return self._payload_to_response(payload, requested_model=model, latency_ms=latency_ms)

    def healthcheck(self) -> dict[str, Any]:
        """Fetch ``/v1/models`` and return a small status dict. Never raises."""
        url = f"{self._config.base_url}/models"
        try:
            payload = self._request_json("GET", url, body=None, timeout_s=5.0)
        except BackendError as exc:
            return {
                "reachable": False,
                "base_url": self._config.base_url,
                "error": str(exc),
                "loaded_models": [],
            }

        loaded: list[str] = []
        if isinstance(payload, dict):
            for record in payload.get("data") or []:
                if isinstance(record, dict):
                    model_id = record.get("id")
                    if isinstance(model_id, str):
                        loaded.append(model_id)
        return {
            "reachable": True,
            "base_url": self._config.base_url,
            "loaded_models": loaded,
            "error": None,
        }

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _payload_to_response(
        self,
        payload: dict[str, Any],
        *,
        requested_model: str,
        latency_ms: int,
    ) -> BackendResponse:
        if not isinstance(payload, dict):
            raise BackendContractError(f"response is not a JSON object: {type(payload).__name__}")

        choices = payload.get("choices")
        if not isinstance(choices, list) or not choices:
            raise BackendContractError("response missing 'choices'")

        first = choices[0]
        if not isinstance(first, dict):
            raise BackendContractError("choices[0] is not an object")

        message = first.get("message")
        if not isinstance(message, dict):
            raise BackendContractError("choices[0].message is not an object")

        content = message.get("content")
        if not isinstance(content, str) or not content.strip():
            # Small models (< 1B) occasionally return empty content for
            # certain prompts. Return an empty string instead of crashing
            # so the pipeline can classify this as uninformative.
            content = ""

        finish_reason = first.get("finish_reason")
        if finish_reason is not None and not isinstance(finish_reason, str):
            finish_reason = str(finish_reason)

        server_model = payload.get("model")
        if not isinstance(server_model, str) or not server_model:
            server_model = requested_model

        self._enforce_model(requested=requested_model, returned=server_model)

        usage = payload.get("usage") or {}
        prompt_tokens = usage.get("prompt_tokens") if isinstance(usage, dict) else None
        completion_tokens = usage.get("completion_tokens") if isinstance(usage, dict) else None

        return BackendResponse(
            text=content,
            model_id=server_model,
            finish_reason=finish_reason,
            prompt_tokens=prompt_tokens if isinstance(prompt_tokens, int) else None,
            completion_tokens=completion_tokens if isinstance(completion_tokens, int) else None,
            raw=payload,
            latency_ms=latency_ms,
        )

    def _enforce_model(self, *, requested: str, returned: str) -> None:
        """Behavioral model enforcement. The anti-theater core rule.

        ``strict``  — the returned model id must equal the requested one.
        ``prefix``  — the returned id must start with the requested one
                      (useful for versioned servers like OpenAI that
                      append suffixes).
        ``off``     — no enforcement; caller accepts whatever the server
                      returns.
        """
        if self._config.model_enforcement == "off":
            return
        if self._config.model_enforcement == "prefix":
            if returned.startswith(requested):
                return
        elif self._config.model_enforcement == "strict":
            if returned == requested:
                return
        else:
            raise BackendError(
                f"unknown model_enforcement mode: {self._config.model_enforcement}"
            )
        raise BackendModelMismatch(
            f"backend returned model '{returned}' but '{requested}' was requested "
            f"(enforcement={self._config.model_enforcement})"
        )

    def _request_json(
        self,
        method: str,
        url: str,
        *,
        body: dict[str, Any] | None,
        timeout_s: float,
    ) -> Any:
        headers = {
            "Accept": "application/json",
            "User-Agent": self._config.user_agent,
        }
        if self._config.api_key_or_none:
            headers["Authorization"] = f"Bearer {self._config.api_key_or_none}"

        data: bytes | None = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")

        request = urllib.request.Request(url, data=data, headers=headers, method=method)

        try:
            with urllib.request.urlopen(request, timeout=timeout_s) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = _safe_read_error(exc)
            raise BackendBlocked(
                f"HTTP {exc.code} from {url}: {detail or exc.reason}"
            ) from exc
        except urllib.error.URLError as exc:
            reason = getattr(exc, "reason", exc)
            if isinstance(reason, socket.timeout):
                raise BackendTimeout(f"backend timed out after {timeout_s}s: {url}") from exc
            raise BackendBlocked(f"could not reach {url}: {reason}") from exc
        except socket.timeout as exc:
            raise BackendTimeout(f"backend timed out after {timeout_s}s: {url}") from exc
        except Exception as exc:  # pragma: no cover - defensive
            raise BackendError(f"unexpected network error: {exc!r}") from exc

        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise BackendContractError(
                f"backend returned non-JSON ({len(raw)} bytes): {raw[:200]!r}"
            ) from exc


def _safe_read_error(exc: urllib.error.HTTPError) -> str:
    try:
        return exc.read().decode("utf-8", errors="replace")
    except Exception:
        return ""
