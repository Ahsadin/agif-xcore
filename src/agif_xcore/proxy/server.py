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
from ..policies.tool_policy import ToolPolicy, tool_policy_from_allowlist


_LOOPBACK_HOSTS = frozenset({"127.0.0.1", "::1", "localhost"})
_TOOL_REFUSAL_MESSAGE = (
    "AGIF Governor MVP does not execute tool or function calls. "
    "Disable tool use in your OpenClaw provider settings and retry."
)
# v0.2: classify the request body's tool-related fields. Modern OpenAI
# ``tools`` arrays go through the substrate's action_gate; everything else
# (legacy ``functions``, multi-turn ``role: tool`` history, populated
# ``tool_calls`` in history) keeps the v0.1 fast fail-closed path.
_TOOL_INTENT_NONE = "none"
_TOOL_INTENT_SUBSTRATE = "substrate"
_TOOL_INTENT_FAIL_CLOSED = "fail_closed"


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

    Returns ``(True, reason_code)`` when the OpenClaw profile sees tool
    intent. v0.1 used this to fail-closed unconditionally; v0.2 still uses
    it as the trigger but classifies the intent further with
    ``_classify_tool_intent``.

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


def _classify_tool_intent(body: dict) -> tuple[str, str]:
    """Classify a request's tool intent for v0.2 routing.

    Returns ``(mode, reason_code)`` where ``mode`` is one of:

    - ``"none"``: no tool intent; route to the regular chat path.
    - ``"substrate"``: modern ``tools`` array present. Pass through to the
      governed client; the substrate's action_gate decides allow/block based
      on the operator's tool allowlist.
    - ``"fail_closed"``: legacy ``functions`` array, ``tool_choice`` /
      ``function_call`` directives, ``role: tool`` history messages, or
      populated ``tool_calls`` in history. v0.2 keeps these on the v0.1 fail
      closed path because they imply multi-turn tool flows out of MVP scope.
    """
    tools = body.get("tools")
    if isinstance(tools, list) and len(tools) > 0:
        return _TOOL_INTENT_SUBSTRATE, "tools_present"
    functions = body.get("functions")
    if isinstance(functions, list) and len(functions) > 0:
        return _TOOL_INTENT_FAIL_CLOSED, "functions_present"
    if "tool_choice" in body and body.get("tool_choice") != "none":
        return _TOOL_INTENT_FAIL_CLOSED, "tool_choice_not_none"
    if "function_call" in body and body.get("function_call") != "none":
        return _TOOL_INTENT_FAIL_CLOSED, "function_call_not_none"
    messages = body.get("messages")
    if isinstance(messages, list):
        for msg in messages:
            if not isinstance(msg, dict):
                continue
            if msg.get("role") == "tool":
                return _TOOL_INTENT_FAIL_CLOSED, "role_tool_in_messages"
            tc = msg.get("tool_calls")
            if isinstance(tc, list) and len(tc) > 0:
                return _TOOL_INTENT_FAIL_CLOSED, "tool_calls_in_messages"
    return _TOOL_INTENT_NONE, ""


def _tool_call_function_name(tool_call: dict) -> str:
    """Extract function name from one OpenAI-shaped ``tool_call`` dict."""
    if not isinstance(tool_call, dict):
        return ""
    fn = tool_call.get("function")
    if isinstance(fn, dict):
        name = fn.get("name")
        if isinstance(name, str):
            return name
    name = tool_call.get("name")
    return name if isinstance(name, str) else ""


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
        tool_allowlist: Sequence[str] | None = None,
        tool_policy: ToolPolicy | None = None,
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
        # v0.3: ToolPolicy is the authoritative shape. v0.2's tool_allowlist
        # is preserved as backward-compat sugar (auto-converted via
        # tool_policy_from_allowlist). Both flags can't be set at once.
        if tool_allowlist is not None and tool_policy is not None:
            raise ValueError(
                "tool_allowlist and tool_policy are mutually exclusive; "
                "pass one or the other (tool_policy is the v0.3 form)"
            )
        if tool_policy is not None:
            self.tool_policy: ToolPolicy | None = tool_policy
        elif tool_allowlist is not None and len(tool_allowlist) > 0:
            self.tool_policy = tool_policy_from_allowlist(tool_allowlist)
        else:
            self.tool_policy = None

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

    @property
    def tool_allowlist(self) -> tuple[str, ...]:
        """v0.2 compat: list of tool names whose decision is ``allow``.

        Empty tuple when no policy is configured.
        """
        if self.tool_policy is None:
            return ()
        return tuple(
            sorted(
                name
                for name, td in self.tool_policy.tools.items()
                if td.decision == "allow"
            )
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
        tool_policy=config.tool_policy,
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

            substrate_routed_tools: list[dict] | None = None
            if self._config.openclaw_profile:
                intent_mode, intent_reason = _classify_tool_intent(body)
                if intent_mode == _TOOL_INTENT_FAIL_CLOSED:
                    # v0.1 fast fail for legacy/multi-turn tool patterns.
                    self._respond_openclaw_tool_refusal(intent_reason)
                    return
                if intent_mode == _TOOL_INTENT_SUBSTRATE:
                    if self._config.tool_policy is None:
                        # No policy configured by the operator: keep v0.1
                        # default-block behaviour without burning a backend
                        # call. Audit event is the existing tool_refusal.
                        self._respond_openclaw_tool_refusal(intent_reason)
                        return
                    raw_tools = body.get("tools")
                    if isinstance(raw_tools, list):
                        substrate_routed_tools = [
                            t for t in raw_tools if isinstance(t, dict)
                        ]
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
                    answer = self._client.ask(
                        user_text, tools=substrate_routed_tools,
                    )
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

            tool_calls_allowed = bool(answer.tool_calls)
            argument_denials_payload: list[dict] = list(answer.argument_denials)
            soften_warnings_payload: list[str] = list(answer.soften_warnings)

            # v0.3: emit one of three audit-event types when applicable. The
            # branches are mutually exclusive in priority order:
            #
            #   1. argument_denials present  → tool_blocked_by_argument
            #      (one event per denial; tool_calls were dropped by the
            #      client-side argument inspector regardless of substrate.)
            #   2. soften_warnings present and tool_calls allowed
            #      → tool_softened (substrate emitted soften but the
            #      argument inspection passed; tool_calls are in the
            #      response.)
            #   3. substrate-routed and not tool_calls_allowed and no
            #      argument denials → tool_blocked (v0.2 behaviour for
            #      substrate name-level block.)
            if self._config.openclaw_profile and substrate_routed_tools is not None:
                ag: dict[str, Any] = {}
                if answer.decisions is not None and answer.decisions.action_gate_decision:
                    ag = answer.decisions.action_gate_decision
                now = int(time.time())

                if argument_denials_payload:
                    for denial in argument_denials_payload:
                        _write_openclaw_audit_event(
                            self._config.trace_file,
                            {
                                "schema_version": "openclaw_profile_event_v1",
                                "event_type": "tool_blocked_by_argument",
                                "trace_id": answer.trace_id,
                                "created": now,
                                "served_model_id": self._config.served_model_id,
                                "upstream_model_id": self._config.model,
                                "answer_mode": answer.answer_mode,
                                "reason_code": denial.get(
                                    "reason_code", "argument_pattern_match"
                                ),
                                "tool_name": denial.get("tool_name", ""),
                                "argument_path": denial.get("argument_path", ""),
                                "pattern_id": denial.get("pattern_id", ""),
                                "governance_enabled": self._config.governance_enabled,
                                "memory_enabled": bool(self._config.memory_enabled),
                            },
                        )
                elif soften_warnings_payload and tool_calls_allowed:
                    softened_names = sorted(
                        {
                            _tool_call_function_name(tc)
                            for tc in (answer.tool_calls or [])
                        }
                        - {""}
                    )
                    _write_openclaw_audit_event(
                        self._config.trace_file,
                        {
                            "schema_version": "openclaw_profile_event_v1",
                            "event_type": "tool_softened",
                            "trace_id": answer.trace_id,
                            "created": now,
                            "served_model_id": self._config.served_model_id,
                            "upstream_model_id": self._config.model,
                            "answer_mode": answer.answer_mode,
                            "reason_code": ag.get(
                                "reason_code", "action_gate_soften"
                            ),
                            "softened_tool_names": softened_names,
                            "soften_reasons": list(soften_warnings_payload),
                            "governance_enabled": self._config.governance_enabled,
                            "memory_enabled": bool(self._config.memory_enabled),
                        },
                    )
                elif not tool_calls_allowed:
                    # v0.2 tool_blocked path: substrate name-level block.
                    allowed_set = set(self._config.tool_allowlist)
                    requested_names: list[str] = []
                    for entry in substrate_routed_tools:
                        fn = entry.get("function") if isinstance(entry, dict) else None
                        if isinstance(fn, dict):
                            nm = fn.get("name")
                            if isinstance(nm, str) and nm:
                                requested_names.append(nm)
                    blocked_names = sorted(
                        {n for n in requested_names if n not in allowed_set}
                    )
                    _write_openclaw_audit_event(
                        self._config.trace_file,
                        {
                            "schema_version": "openclaw_profile_event_v1",
                            "event_type": "tool_blocked",
                            "trace_id": answer.trace_id,
                            "created": now,
                            "served_model_id": self._config.served_model_id,
                            "upstream_model_id": self._config.model,
                            "answer_mode": answer.answer_mode,
                            "reason_code": ag.get(
                                "reason_code", "action_gate_block"
                            ),
                            "blocked_tool_names": blocked_names,
                            "governance_enabled": self._config.governance_enabled,
                            "memory_enabled": bool(self._config.memory_enabled),
                        },
                    )

            content = answer.text
            assistant_message: dict[str, Any] = {
                "role": "assistant",
                "content": content,
            }
            finish_reason = "stop"
            if tool_calls_allowed:
                # OpenAI shape: when tool_calls is present, content is null and
                # finish_reason is "tool_calls". v0.3 specifically does NOT
                # inject an AGIF footer into a null content field — soften
                # information surfaces only via x_agif_trace and the
                # tool_softened audit event.
                assistant_message["content"] = None
                assistant_message["tool_calls"] = list(answer.tool_calls)
                finish_reason = "tool_calls"
            else:
                # Plain-text response: keep the v0.1/v0.2 footer behaviour.
                if self._config.trace_visibility in ("footer", "both"):
                    assistant_message["content"] = (
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
                        "message": assistant_message,
                        "finish_reason": finish_reason,
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
                    "tool_calls_allowed": tool_calls_allowed,
                    "soften_warnings": list(soften_warnings_payload),
                    "argument_denials": list(argument_denials_payload),
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
