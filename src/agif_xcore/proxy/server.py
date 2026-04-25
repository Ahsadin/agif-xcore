"""OpenAI-compatible HTTP proxy server.

Wraps any upstream backend with AGIF-XCore governance. Any client that
speaks ``POST /v1/chat/completions`` (the OpenAI SDK, LangChain,
llama-index, curl) can point at this proxy transparently.

Uses stdlib ``http.server.ThreadingHTTPServer`` — zero external deps.
For production use consider installing the ``proxy`` extras and using
the ASGI variant (future milestone).

Routes:
  POST /v1/chat/completions  — governed chat completion
  GET  /v1/models            — list upstream models
  GET  /health               — proxy healthcheck

OpenClaw profile (``--openclaw-profile``) locks the proxy to a single
served model id, disables memory, fails closed on tool/function calls
and model mismatches, omits the wildcard CORS header, and optionally
enforces a bearer token. See ``docs/openclaw.md``.
"""

from __future__ import annotations

import json
import sys
import time
import traceback
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Sequence

from ..backends.base import BackendError
from ..client import GovernedClient


_LOOPBACK_HOSTS = frozenset({"127.0.0.1", "::1", "localhost"})
_TOOL_REFUSAL_MESSAGE = (
    "AGIF Governor MVP does not execute tool or function calls. "
    "Disable tool use in your OpenClaw provider settings and retry."
)


def _is_loopback_host(host: str) -> bool:
    """Return True if the host is a loopback address."""
    return host in _LOOPBACK_HOSTS


def _refusal_trace_id() -> str:
    """Generate a stable-unique id for OpenClaw fail-closed events."""
    return f"refusal-{uuid.uuid4().hex[:12]}"


def _write_openclaw_audit_event(
    trace_file: str | Path | None, event: dict[str, Any]
) -> None:
    """Append one JSONL audit event to the OpenClaw trace file.

    Used only in fail-closed paths that skip the backend call. No-op when
    ``trace_file`` is None. Audit-log failures log to stderr and do not
    raise — they must not crash the proxy.
    """
    if not trace_file:
        return
    try:
        with open(trace_file, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(event, ensure_ascii=False))
            fh.write("\n")
    except OSError:
        traceback.print_exc(file=sys.stderr)


def _has_tool_payload(body: dict) -> tuple[bool, str]:
    """Detect any tool/function-call intent in the request body.

    Returns ``(True, reason_code)`` when OpenClaw profile must fail closed.
    ``"auto"`` values for ``tool_choice`` / ``function_call`` still permit
    tool invocation when schemas are present, so we treat anything other
    than the literal string ``"none"`` as a trigger.
    """
    tools = body.get("tools")
    if isinstance(tools, list) and len(tools) > 0:
        return True, "tools_present"
    functions = body.get("functions")
    if isinstance(functions, list) and len(functions) > 0:
        return True, "functions_present"
    if "tool_choice" in body and body.get("tool_choice") != "none":
        return True, "tool_choice_not_none"
    if "function_call" in body and body.get("function_call") != "none":
        return True, "function_call_not_none"
    messages = body.get("messages")
    if isinstance(messages, list):
        for msg in messages:
            if not isinstance(msg, dict):
                continue
            if msg.get("role") == "tool":
                return True, "role_tool_in_messages"
            tc = msg.get("tool_calls")
            if isinstance(tc, list) and len(tc) > 0:
                return True, "tool_calls_in_messages"
    return False, ""


class ProxyConfig:
    """Immutable configuration for the proxy server."""

    def __init__(
        self,
        *,
        backend: str = "ollama",
        model: str,
        base_url: str | None = None,
        api_key: str | None = None,
        model_enforcement: str = "prefix",
        temperature: float = 0.0,
        max_tokens: int | None = None,
        governance_enabled: bool = True,
        grounding_paths: Sequence[str | Path] | None = None,
        trace_file: str | Path | None = None,
        openclaw_profile: bool = False,
        served_model_id: str | None = None,
        trace_visibility: str = "metadata",
        proxy_api_key: str | None = None,
        memory_enabled: bool | None = None,
        unsafe_bind: bool = False,
    ) -> None:
        self.backend = backend
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.model_enforcement = model_enforcement
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.governance_enabled = governance_enabled
        self.grounding_paths = grounding_paths
        self.trace_file = trace_file
        self.openclaw_profile = bool(openclaw_profile)
        self.served_model_id = served_model_id
        if trace_visibility not in ("metadata", "footer", "both"):
            raise ValueError(
                "trace_visibility must be one of metadata|footer|both, "
                f"got {trace_visibility!r}"
            )
        self.trace_visibility = trace_visibility
        self.proxy_api_key = proxy_api_key
        self.memory_enabled = memory_enabled
        self.unsafe_bind = bool(unsafe_bind)

        if self.openclaw_profile:
            if not self.served_model_id:
                raise ValueError("OpenClaw profile requires served_model_id")
            if not self.governance_enabled:
                raise ValueError(
                    "OpenClaw profile requires governance_enabled=True"
                )
            if self.trace_file is None:
                raise ValueError("OpenClaw profile requires trace_file")
            if self.memory_enabled is None:
                self.memory_enabled = False
            elif self.memory_enabled is not False:
                raise ValueError(
                    "OpenClaw profile requires memory_enabled=False (hard-off in MVP)"
                )


def build_proxy_server(
    config: ProxyConfig,
    host: str = "127.0.0.1",
    port: int = 8088,
) -> ThreadingHTTPServer:
    """Create the proxy server. Call ``.serve_forever()`` to start."""

    client_kwargs: dict[str, Any] = dict(
        backend=config.backend,
        model=config.model,
        base_url=config.base_url,
        api_key=config.api_key,
        model_enforcement=config.model_enforcement,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        governance_enabled=config.governance_enabled,
        grounding_paths=config.grounding_paths,
        trace_file=Path(config.trace_file) if config.trace_file else None,
    )
    if config.memory_enabled is not None:
        client_kwargs["memory_enabled"] = config.memory_enabled
    client = GovernedClient(**client_kwargs)

    class Handler(BaseHTTPRequestHandler):
        """Handles each HTTP request. ``_client`` is shared across threads."""

        _client = client
        _config = config
        _started_at = time.time()
        _host = host

        def log_message(self, fmt: str, *args: Any) -> None:
            pass

        # ----- auth -----

        def _auth_required_for_path(self, path: str) -> bool:
            return (
                self._config.proxy_api_key is not None
                and path.startswith("/v1/")
            )

        def _auth_ok(self) -> tuple[bool, str]:
            header = self.headers.get("Authorization")
            if not header:
                return False, "missing_authorization_header"
            if not header.startswith("Bearer "):
                return False, "wrong_scheme"
            token = header[len("Bearer "):].strip()
            if not token:
                return False, "wrong_scheme"
            if token != self._config.proxy_api_key:
                return False, "wrong_token"
            return True, ""

        def _reject_auth(self, reason_code: str) -> None:
            if self._config.openclaw_profile:
                trace_id = _refusal_trace_id()
                _write_openclaw_audit_event(self._config.trace_file, {
                    "schema_version": "openclaw_profile_event_v1",
                    "event_type": "auth_failure",
                    "trace_id": trace_id,
                    "created": int(time.time()),
                    "served_model_id": self._config.served_model_id,
                    "upstream_model_id": self._config.model,
                    "answer_mode": "abstain",
                    "reason_code": reason_code,
                    "governance_enabled": self._config.governance_enabled,
                    "memory_enabled": bool(self._config.memory_enabled),
                })
            body = json.dumps({
                "error": {
                    "message": "Missing or invalid API key.",
                    "type": "invalid_request_error",
                    "code": "invalid_api_key",
                }
            }, ensure_ascii=False).encode("utf-8")
            self.send_response(401)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("WWW-Authenticate", "Bearer")
            self.end_headers()
            self.wfile.write(body)

        # ----- routing -----

        def do_GET(self) -> None:  # noqa: N802
            path = self.path.split("?")[0].rstrip("/")
            if self._auth_required_for_path(path):
                ok, reason = self._auth_ok()
                if not ok:
                    self._reject_auth(reason)
                    return

            if path == "/health":
                self._respond_health()
                return

            if path == "/v1/models":
                self._respond_models()
                return

            self._respond_json(404, {"error": {"message": f"not found: {self.path}"}})

        def do_POST(self) -> None:  # noqa: N802
            path = self.path.split("?")[0].rstrip("/")
            if self._auth_required_for_path(path):
                ok, reason = self._auth_ok()
                if not ok:
                    self._reject_auth(reason)
                    return

            if path == "/v1/chat/completions":
                self._handle_chat_completions()
                return

            self._respond_json(404, {"error": {"message": f"not found: {self.path}"}})

        def do_OPTIONS(self) -> None:  # noqa: N802
            if self._config.openclaw_profile:
                self.send_response(204)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
            self.end_headers()

        # ----- endpoints -----

        def _respond_health(self) -> None:
            if self._config.openclaw_profile:
                payload = {
                    "status": "ok",
                    "uptime_s": int(time.time() - self._started_at),
                    "openclaw_profile": True,
                    "served_model_id": self._config.served_model_id,
                    "upstream_model_id": self._config.model,
                    "governance_enabled": self._config.governance_enabled,
                    "memory_enabled": bool(self._config.memory_enabled),
                    "trace_file_enabled": self._config.trace_file is not None,
                    "auth_enabled": self._config.proxy_api_key is not None,
                    "host_safe": _is_loopback_host(self._host) or self._config.unsafe_bind,
                }
            else:
                payload = {
                    "status": "ok",
                    "uptime_s": int(time.time() - self._started_at),
                    "governance_enabled": self._config.governance_enabled,
                    "backend": self._config.backend,
                    "model": self._config.model,
                }
            self._respond_json(200, payload)

        def _respond_models(self) -> None:
            if self._config.openclaw_profile:
                models = [{
                    "id": self._config.served_model_id,
                    "object": "model",
                    "owned_by": "agif-xcore",
                }]
            else:
                status = self._client.healthcheck()
                models = [
                    {"id": mid, "object": "model", "owned_by": "upstream"}
                    for mid in status.get("loaded_models", [])
                ]
            self._respond_json(200, {"object": "list", "data": models})

        # ----- chat completions -----

        def _handle_chat_completions(self) -> None:
            try:
                body = self._read_json_body()
            except Exception as exc:
                self._respond_json(400, {"error": {"message": f"invalid JSON: {exc}"}})
                return

            if self._config.openclaw_profile:
                has_tool, reason = _has_tool_payload(body)
                if has_tool:
                    self._respond_openclaw_tool_refusal(reason)
                    return
                req_model = body.get("model")
                if req_model != self._config.served_model_id:
                    self._respond_openclaw_model_mismatch(req_model)
                    return

            messages = body.get("messages", [])
            user_text = ""
            for msg in reversed(messages):
                if isinstance(msg, dict) and msg.get("role") == "user":
                    user_text = str(msg.get("content", ""))
                    break

            if not user_text.strip():
                self._respond_json(400, {
                    "error": {"message": "no user message found in messages array"}
                })
                return

            req_model = body.get("model", self._config.model)
            req_temp = body.get("temperature", self._config.temperature)
            req_max = body.get("max_tokens", self._config.max_tokens)
            stream_requested = body.get("stream", False)

            started = time.perf_counter()
            try:
                if self._config.openclaw_profile:
                    answer = self._client.ask(user_text)
                elif req_model != self._config.model:
                    answer = GovernedClient(
                        backend=self._client.backend,
                        model=req_model,
                        temperature=float(req_temp),
                        max_tokens=int(req_max) if req_max else None,
                        governance_enabled=self._config.governance_enabled,
                        grounding_paths=self._config.grounding_paths,
                    ).ask(user_text)
                else:
                    answer = self._client.ask(user_text)
            except BackendError as exc:
                self._respond_json(502, {
                    "error": {
                        "message": f"upstream backend error: {exc}",
                        "type": "backend_error",
                    }
                })
                return
            except Exception as exc:
                traceback.print_exc(file=sys.stderr)
                self._respond_json(500, {
                    "error": {
                        "message": f"internal proxy error: {exc}",
                        "type": "internal_error",
                    }
                })
                return

            response_model = (
                self._config.served_model_id
                if self._config.openclaw_profile
                else req_model
            )

            content = answer.text
            if self._config.trace_visibility in ("footer", "both"):
                content = (
                    f"{content}\n\nAGIF: mode={answer.answer_mode}; "
                    f"trace={answer.trace_id}"
                )

            response_payload = {
                "id": f"chatcmpl-{answer.trace_id}",
                "object": "chat.completion",
                "created": int(time.time()),
                "model": response_model,
                "choices": [
                    {
                        "index": 0,
                        "message": {"role": "assistant", "content": content},
                        "finish_reason": "stop",
                    }
                ],
                "usage": {
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "total_tokens": 0,
                },
                "x_agif_trace": {
                    "trace_id": answer.trace_id,
                    "answer_mode": answer.answer_mode,
                    "governance_enabled": self._config.governance_enabled,
                    "served_model_id": self._config.served_model_id,
                    "upstream_model_id": self._config.model,
                    "memory_enabled": self._client.memory_enabled,
                    "total_ms": answer.total_ms,
                    "refs": answer.refs,
                },
            }

            if stream_requested:
                self._respond_sse(response_payload)
            else:
                self._respond_json(200, response_payload)

        # ----- OpenClaw fail-closed responses -----

        def _respond_openclaw_tool_refusal(self, reason_code: str) -> None:
            trace_id = _refusal_trace_id()
            now = int(time.time())
            _write_openclaw_audit_event(self._config.trace_file, {
                "schema_version": "openclaw_profile_event_v1",
                "event_type": "tool_refusal",
                "trace_id": trace_id,
                "created": now,
                "served_model_id": self._config.served_model_id,
                "upstream_model_id": self._config.model,
                "answer_mode": "abstain",
                "reason_code": reason_code,
                "governance_enabled": self._config.governance_enabled,
                "memory_enabled": bool(self._config.memory_enabled),
            })
            content = _TOOL_REFUSAL_MESSAGE
            if self._config.trace_visibility in ("footer", "both"):
                content = f"{content}\n\nAGIF: mode=abstain; trace={trace_id}"
            self._respond_json(200, {
                "id": f"chatcmpl-{trace_id}",
                "object": "chat.completion",
                "created": now,
                "model": self._config.served_model_id,
                "choices": [
                    {
                        "index": 0,
                        "message": {"role": "assistant", "content": content},
                        "finish_reason": "stop",
                    }
                ],
                "usage": {
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "total_tokens": 0,
                },
                "x_agif_trace": {
                    "trace_id": trace_id,
                    "answer_mode": "abstain",
                    "governance_enabled": self._config.governance_enabled,
                    "served_model_id": self._config.served_model_id,
                    "upstream_model_id": self._config.model,
                    "memory_enabled": bool(self._config.memory_enabled),
                    "total_ms": 0,
                    "refs": [],
                    "reason_code": reason_code,
                },
            })

        def _respond_openclaw_model_mismatch(self, requested: Any) -> None:
            trace_id = _refusal_trace_id()
            _write_openclaw_audit_event(self._config.trace_file, {
                "schema_version": "openclaw_profile_event_v1",
                "event_type": "model_mismatch",
                "trace_id": trace_id,
                "created": int(time.time()),
                "served_model_id": self._config.served_model_id,
                "upstream_model_id": self._config.model,
                "answer_mode": "abstain",
                "reason_code": "requested_id_not_served",
                "governance_enabled": self._config.governance_enabled,
                "memory_enabled": bool(self._config.memory_enabled),
            })
            served = self._config.served_model_id
            self._respond_json(404, {
                "error": {
                    "message": (
                        f"The model '{requested}' is not served by this proxy. "
                        f"Only '{served}' is available."
                    ),
                    "type": "invalid_request_error",
                    "code": "model_not_found",
                },
                "x_agif_trace": {
                    "trace_id": trace_id,
                    "answer_mode": "abstain",
                    "reason_code": "requested_id_not_served",
                    "served_model_id": served,
                    "upstream_model_id": self._config.model,
                },
            })

        # ----- helpers -----

        def _read_json_body(self) -> dict:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length).decode("utf-8") if length else "{}"
            return json.loads(raw)

        def _respond_json(self, status_code: int, payload: dict) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status_code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            if not self._config.openclaw_profile:
                self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)

        def _respond_sse(self, payload: dict) -> None:
            """Emit a single SSE data event + [DONE] sentinel.

            Not true token streaming — the full answer as one event. True
            streaming needs an async server (future milestone). OpenAI SDK
            streaming parsers consume a single-event stream correctly.
            """
            chunk = {
                "id": payload["id"],
                "object": "chat.completion.chunk",
                "created": payload["created"],
                "model": payload["model"],
                "choices": [
                    {
                        "index": 0,
                        "delta": {
                            "role": "assistant",
                            "content": payload["choices"][0]["message"]["content"],
                        },
                        "finish_reason": None,
                    }
                ],
            }
            done_chunk = {
                "id": payload["id"],
                "object": "chat.completion.chunk",
                "created": payload["created"],
                "model": payload["model"],
                "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
                "x_agif_trace": payload.get("x_agif_trace"),
            }

            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            if not self._config.openclaw_profile:
                self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(f"data: {json.dumps(chunk)}\n\n".encode("utf-8"))
            self.wfile.write(f"data: {json.dumps(done_chunk)}\n\n".encode("utf-8"))
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()

    return ThreadingHTTPServer((host, port), Handler)
