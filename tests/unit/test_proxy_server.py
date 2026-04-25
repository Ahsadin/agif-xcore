"""Tests for the OpenAI-compatible proxy server.

Starts the server in a background thread with a stub backend, then
hits it with ``urllib.request``. No external deps, no real model.
"""

from __future__ import annotations

import json
import os
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agif_xcore.backends.base import BackendError, BackendResponse
from agif_xcore.proxy.server import (
    ProxyConfig,
    _has_tool_payload,
    _is_loopback_host,
    build_proxy_server,
)


# ---------------------------------------------------------------------------
# Stub backend (same pattern as test_client.py)
# ---------------------------------------------------------------------------

@dataclass
class _StubBackend:
    name: str = "stub"
    reply_text: str = "The backup cadence is daily incremental."

    def complete(self, messages, *, model, temperature=0.0, max_tokens=None, timeout_ms=30000):
        return BackendResponse(
            text=self.reply_text, model_id=model,
            finish_reason="stop", prompt_tokens=10, completion_tokens=8, latency_ms=1,
        )

    def healthcheck(self):
        return {"reachable": True, "loaded_models": ["stubmodel"]}


# ---------------------------------------------------------------------------
# Test harness
# ---------------------------------------------------------------------------

def _free_port() -> int:
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class ProxyServerTests(unittest.TestCase):
    _server = None
    _thread = None
    _port = 0

    @classmethod
    def setUpClass(cls) -> None:
        cls._port = _free_port()
        # Monkey-patch the client inside the proxy to use our stub
        config = ProxyConfig(backend="ollama", model="stubmodel")
        cls._server = build_proxy_server(config, host="127.0.0.1", port=cls._port)

        # Replace the handler's _client with our stub-backed client
        from agif_xcore.client import GovernedClient
        stub_client = GovernedClient(backend=_StubBackend(), model="stubmodel")
        # Access the handler class from the server
        cls._server.RequestHandlerClass._client = stub_client

        cls._thread = threading.Thread(target=cls._server.serve_forever, daemon=True)
        cls._thread.start()
        time.sleep(0.1)  # let server bind

    @classmethod
    def tearDownClass(cls) -> None:
        if cls._server:
            cls._server.shutdown()

    @property
    def base(self) -> str:
        return f"http://127.0.0.1:{self._port}"

    def _get(self, path: str) -> dict:
        url = f"{self.base}{path}"
        with urllib.request.urlopen(url, timeout=5) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def _post(self, path: str, body: dict) -> dict:
        url = f"{self.base}{path}"
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            url, data=data, headers={"Content-Type": "application/json"}, method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))

    # ----- tests -----

    def test_health_endpoint(self) -> None:
        result = self._get("/health")
        self.assertEqual(result["status"], "ok")
        self.assertIn("uptime_s", result)
        self.assertIn("governance_enabled", result)

    def test_models_endpoint(self) -> None:
        result = self._get("/v1/models")
        self.assertEqual(result["object"], "list")
        self.assertIsInstance(result["data"], list)

    def test_chat_completions_returns_openai_shape(self) -> None:
        result = self._post("/v1/chat/completions", {
            "model": "stubmodel",
            "messages": [{"role": "user", "content": "What is the backup cadence?"}],
        })
        self.assertEqual(result["object"], "chat.completion")
        self.assertEqual(len(result["choices"]), 1)
        self.assertEqual(result["choices"][0]["message"]["role"], "assistant")
        self.assertIn("backup cadence", result["choices"][0]["message"]["content"].lower())
        self.assertEqual(result["choices"][0]["finish_reason"], "stop")
        # XCore trace metadata
        self.assertIn("x_agif_trace", result)
        self.assertIn("trace_id", result["x_agif_trace"])

    def test_empty_messages_returns_400(self) -> None:
        try:
            self._post("/v1/chat/completions", {
                "model": "stubmodel",
                "messages": [],
            })
            self.fail("expected HTTP error")
        except urllib.error.HTTPError as exc:
            self.assertEqual(exc.code, 400)

    def test_missing_user_message_returns_400(self) -> None:
        try:
            self._post("/v1/chat/completions", {
                "model": "stubmodel",
                "messages": [{"role": "system", "content": "you are helpful"}],
            })
            self.fail("expected HTTP error")
        except urllib.error.HTTPError as exc:
            self.assertEqual(exc.code, 400)

    def test_not_found_returns_404(self) -> None:
        try:
            self._get("/v1/nonexistent")
            self.fail("expected HTTP error")
        except urllib.error.HTTPError as exc:
            self.assertEqual(exc.code, 404)

    def test_chat_id_contains_trace_id(self) -> None:
        result = self._post("/v1/chat/completions", {
            "model": "stubmodel",
            "messages": [{"role": "user", "content": "hello"}],
        })
        self.assertTrue(result["id"].startswith("chatcmpl-turn_"))

    def test_stream_true_returns_sse(self) -> None:
        """When stream=true, the server returns SSE events."""
        url = f"{self.base}/v1/chat/completions"
        body = json.dumps({
            "model": "stubmodel",
            "messages": [{"role": "user", "content": "hello"}],
            "stream": True,
        }).encode("utf-8")
        req = urllib.request.Request(
            url, data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            content_type = resp.headers.get("Content-Type", "")
            self.assertIn("text/event-stream", content_type)
            raw = resp.read().decode("utf-8")
            self.assertIn("data: ", raw)
            self.assertIn("[DONE]", raw)


class ServeCliParserTests(unittest.TestCase):
    def test_serve_parser_accepts_minimal_args(self) -> None:
        from agif_xcore.cli.main import build_parser
        parser = build_parser()
        args = parser.parse_args([
            "serve", "--model", "gemma3:270m",
        ])
        self.assertEqual(args.model, "gemma3:270m")
        self.assertEqual(args.port, 8088)
        self.assertTrue(args.governance)
        self.assertFalse(args.openclaw_profile)
        self.assertIsNone(args.served_model_id)
        self.assertEqual(args.trace_visibility, "metadata")
        self.assertIsNone(args.proxy_api_key_env)
        self.assertFalse(args.unsafe_bind)

    def test_no_governance_flag(self) -> None:
        from agif_xcore.cli.main import build_parser
        parser = build_parser()
        args = parser.parse_args([
            "serve", "--model", "x", "--no-governance",
        ])
        self.assertFalse(args.governance)

    def test_parser_accepts_openclaw_flags(self) -> None:
        from agif_xcore.cli.main import build_parser
        parser = build_parser()
        args = parser.parse_args([
            "serve",
            "--model", "gemma3:270m",
            "--served-model-id", "agif-governor/gemma3-270m",
            "--openclaw-profile",
            "--trace-visibility", "both",
            "--trace-file", "/tmp/t.jsonl",
            "--proxy-api-key-env", "FAKE_ENV",
            "--unsafe-bind",
        ])
        self.assertTrue(args.openclaw_profile)
        self.assertEqual(args.served_model_id, "agif-governor/gemma3-270m")
        self.assertEqual(args.trace_visibility, "both")
        self.assertEqual(args.proxy_api_key_env, "FAKE_ENV")
        self.assertTrue(args.unsafe_bind)


# ---------------------------------------------------------------------------
# OpenClaw profile tests
# ---------------------------------------------------------------------------

SERVED_ID = "agif-governor/stub"
UPSTREAM_ID = "stubmodel"


def _make_stub_client(trace_file: Path):
    from agif_xcore.client import GovernedClient
    return GovernedClient(
        backend=_StubBackend(),
        model=UPSTREAM_ID,
        memory_enabled=False,
        trace_file=trace_file,
    )


def _start_openclaw_server(
    *,
    trace_file: Path,
    trace_visibility: str = "metadata",
    proxy_api_key: str | None = None,
) -> tuple[Any, int]:
    port = _free_port()
    config = ProxyConfig(
        backend="ollama",
        model=UPSTREAM_ID,
        openclaw_profile=True,
        served_model_id=SERVED_ID,
        trace_visibility=trace_visibility,
        trace_file=str(trace_file),
        proxy_api_key=proxy_api_key,
    )
    server = build_proxy_server(config, host="127.0.0.1", port=port)
    server.RequestHandlerClass._client = _make_stub_client(trace_file)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    time.sleep(0.1)
    return server, port


def _read_audit_events(trace_file: Path) -> list[dict]:
    if not trace_file.exists():
        return []
    out: list[dict] = []
    for line in trace_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and obj.get("schema_version") == "openclaw_profile_event_v1":
            out.append(obj)
    return out


class OpenClawProfileTests(unittest.TestCase):
    """End-to-end behavioral tests for the OpenClaw profile."""

    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.trace_file = Path(self._tmpdir.name) / "openclaw.jsonl"
        self.server, self.port = _start_openclaw_server(trace_file=self.trace_file)

    def tearDown(self) -> None:
        self.server.shutdown()
        self._tmpdir.cleanup()

    @property
    def base(self) -> str:
        return f"http://127.0.0.1:{self.port}"

    def _get(self, path: str, headers: dict[str, str] | None = None):
        req = urllib.request.Request(f"{self.base}{path}", headers=headers or {})
        with urllib.request.urlopen(req, timeout=5) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return resp.status, body, resp.headers

    def _post(self, path: str, body: dict, headers: dict[str, str] | None = None):
        data = json.dumps(body).encode("utf-8")
        full_headers = {"Content-Type": "application/json"}
        if headers:
            full_headers.update(headers)
        req = urllib.request.Request(
            f"{self.base}{path}", data=data, headers=full_headers, method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            return resp.status, payload, resp.headers

    # ---- /health ----

    def test_health_reports_openclaw_state_without_secrets(self) -> None:
        status, payload, _ = self._get("/health")
        self.assertEqual(status, 200)
        self.assertTrue(payload["openclaw_profile"])
        self.assertEqual(payload["served_model_id"], SERVED_ID)
        self.assertEqual(payload["upstream_model_id"], UPSTREAM_ID)
        self.assertTrue(payload["governance_enabled"])
        self.assertFalse(payload["memory_enabled"])
        self.assertTrue(payload["trace_file_enabled"])
        self.assertFalse(payload["auth_enabled"])
        self.assertTrue(payload["host_safe"])
        # No secrets
        serialized = json.dumps(payload)
        self.assertNotIn("Authorization", serialized)
        self.assertNotIn("Bearer", serialized)

    # ---- /v1/models ----

    def test_models_endpoint_returns_only_served_id(self) -> None:
        status, payload, _ = self._get("/v1/models")
        self.assertEqual(status, 200)
        self.assertEqual(payload["object"], "list")
        self.assertEqual(len(payload["data"]), 1)
        self.assertEqual(payload["data"][0]["id"], SERVED_ID)
        self.assertEqual(payload["data"][0]["owned_by"], "agif-xcore")

    # ---- /v1/chat/completions — success path ----

    def test_chat_completions_matching_served_id_succeeds(self) -> None:
        status, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "what is it?"}],
        })
        self.assertEqual(status, 200)
        self.assertEqual(payload["object"], "chat.completion")
        self.assertEqual(payload["model"], SERVED_ID)
        self.assertEqual(
            payload["x_agif_trace"]["served_model_id"], SERVED_ID,
        )
        self.assertEqual(
            payload["x_agif_trace"]["upstream_model_id"], UPSTREAM_ID,
        )
        self.assertFalse(payload["x_agif_trace"]["memory_enabled"])

    def test_x_agif_trace_includes_served_and_upstream_ids(self) -> None:
        status, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "ping"}],
        })
        self.assertEqual(status, 200)
        trace = payload["x_agif_trace"]
        self.assertEqual(trace["served_model_id"], SERVED_ID)
        self.assertEqual(trace["upstream_model_id"], UPSTREAM_ID)

    def test_x_agif_trace_includes_memory_enabled_false(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "ping"}],
        })
        self.assertFalse(payload["x_agif_trace"]["memory_enabled"])

    # ---- /v1/chat/completions — model mismatch ----

    def test_chat_completions_mismatched_model_returns_404_model_not_found(self) -> None:
        try:
            self._post("/v1/chat/completions", {
                "model": "wrong-id",
                "messages": [{"role": "user", "content": "x"}],
            })
            self.fail("expected HTTPError")
        except urllib.error.HTTPError as exc:
            self.assertEqual(exc.code, 404)
            body = json.loads(exc.read().decode("utf-8"))
            self.assertEqual(body["error"]["code"], "model_not_found")
            self.assertEqual(body["error"]["type"], "invalid_request_error")
            self.assertIn(SERVED_ID, body["error"]["message"])

    def test_model_mismatch_writes_audit_event(self) -> None:
        try:
            self._post("/v1/chat/completions", {
                "model": "wrong-id",
                "messages": [{"role": "user", "content": "x"}],
            })
        except urllib.error.HTTPError:
            pass
        events = _read_audit_events(self.trace_file)
        mismatches = [e for e in events if e["event_type"] == "model_mismatch"]
        self.assertEqual(len(mismatches), 1)
        ev = mismatches[0]
        self.assertEqual(ev["schema_version"], "openclaw_profile_event_v1")
        self.assertEqual(ev["served_model_id"], SERVED_ID)
        self.assertEqual(ev["upstream_model_id"], UPSTREAM_ID)
        self.assertEqual(ev["answer_mode"], "abstain")
        self.assertEqual(ev["reason_code"], "requested_id_not_served")
        self.assertTrue(ev["trace_id"].startswith("refusal-"))

    # ---- /v1/chat/completions — tool refusal ----

    def test_chat_completions_with_tools_fails_closed(self) -> None:
        status, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
            "tools": [{"type": "function", "function": {"name": "f"}}],
        })
        self.assertEqual(status, 200)
        self.assertIn(
            "does not execute tool or function calls",
            payload["choices"][0]["message"]["content"],
        )
        self.assertEqual(payload["x_agif_trace"]["answer_mode"], "abstain")
        self.assertEqual(payload["x_agif_trace"]["reason_code"], "tools_present")

    def test_chat_completions_with_tool_choice_forced_fails_closed(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
            "tool_choice": {"type": "function", "function": {"name": "f"}},
        })
        self.assertEqual(payload["x_agif_trace"]["answer_mode"], "abstain")
        self.assertEqual(payload["x_agif_trace"]["reason_code"], "tool_choice_not_none")

    def test_tool_choice_auto_fails_closed(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
            "tool_choice": "auto",
        })
        self.assertEqual(payload["x_agif_trace"]["answer_mode"], "abstain")
        self.assertEqual(payload["x_agif_trace"]["reason_code"], "tool_choice_not_none")

    def test_function_call_auto_fails_closed(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
            "function_call": "auto",
        })
        self.assertEqual(payload["x_agif_trace"]["answer_mode"], "abstain")
        self.assertEqual(
            payload["x_agif_trace"]["reason_code"], "function_call_not_none",
        )

    def test_tool_choice_none_is_allowed(self) -> None:
        """tool_choice='none' is allowed because it disables tool use."""
        status, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "hello"}],
            "tool_choice": "none",
        })
        self.assertEqual(status, 200)
        # Normal governed reply — not the refusal message
        self.assertNotIn(
            "does not execute tool or function calls",
            payload["choices"][0]["message"]["content"],
        )

    def test_chat_completions_with_role_tool_message_fails_closed(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [
                {"role": "user", "content": "x"},
                {"role": "tool", "content": "result", "tool_call_id": "c_1"},
            ],
        })
        self.assertEqual(payload["x_agif_trace"]["reason_code"], "role_tool_in_messages")

    def test_chat_completions_with_functions_fails_closed(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
            "functions": [{"name": "f", "parameters": {}}],
        })
        self.assertEqual(payload["x_agif_trace"]["reason_code"], "functions_present")

    def test_tool_refusal_writes_audit_event(self) -> None:
        self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
            "tools": [{"type": "function", "function": {"name": "f"}}],
        })
        events = _read_audit_events(self.trace_file)
        refusals = [e for e in events if e["event_type"] == "tool_refusal"]
        self.assertEqual(len(refusals), 1)
        ev = refusals[0]
        self.assertEqual(ev["reason_code"], "tools_present")
        self.assertEqual(ev["served_model_id"], SERVED_ID)
        self.assertEqual(ev["answer_mode"], "abstain")
        self.assertFalse(ev["memory_enabled"])

    def test_response_trace_id_matches_audit_trace_id(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
            "tools": [{"type": "function", "function": {"name": "f"}}],
        })
        resp_trace_id = payload["x_agif_trace"]["trace_id"]
        events = _read_audit_events(self.trace_file)
        matching = [e for e in events if e["trace_id"] == resp_trace_id]
        self.assertEqual(len(matching), 1)
        self.assertEqual(matching[0]["event_type"], "tool_refusal")

    # ---- trace file write-through ----

    def test_trace_file_contains_trace_id(self) -> None:
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "hello"}],
        })
        trace_id = payload["x_agif_trace"]["trace_id"]
        # The GovernedClient writes the full trace envelope with turn_id.
        # ``trace_id`` returned to the client is the same as ``turn_id``.
        raw = self.trace_file.read_text(encoding="utf-8")
        self.assertIn(trace_id, raw)

    # ---- CORS ----

    def test_no_cors_wildcard_in_openclaw_profile(self) -> None:
        _, _, headers = self._get("/health")
        self.assertNotEqual(headers.get("Access-Control-Allow-Origin"), "*")
        # Chat endpoint too
        _, _, headers = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "x"}],
        })
        self.assertNotEqual(headers.get("Access-Control-Allow-Origin"), "*")

    # ---- memory ----

    def test_openclaw_memory_is_disabled_on_client(self) -> None:
        client = self.server.RequestHandlerClass._client
        self.assertFalse(client.memory_enabled)

    # ---- footer ----

    def test_trace_visibility_metadata_no_footer(self) -> None:
        # Default profile uses metadata
        _, payload, _ = self._post("/v1/chat/completions", {
            "model": SERVED_ID,
            "messages": [{"role": "user", "content": "hello"}],
        })
        content = payload["choices"][0]["message"]["content"]
        self.assertNotIn("AGIF: mode=", content)


class OpenClawFooterTests(unittest.TestCase):
    """Footer appearance tests use a separately-configured server."""

    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.trace_file = Path(self._tmpdir.name) / "openclaw.jsonl"

    def tearDown(self) -> None:
        self._tmpdir.cleanup()

    def _roundtrip(self, visibility: str) -> dict:
        server, port = _start_openclaw_server(
            trace_file=self.trace_file, trace_visibility=visibility,
        )
        try:
            url = f"http://127.0.0.1:{port}/v1/chat/completions"
            data = json.dumps({
                "model": SERVED_ID,
                "messages": [{"role": "user", "content": "hi"}],
            }).encode("utf-8")
            req = urllib.request.Request(
                url, data=data,
                headers={"Content-Type": "application/json"}, method="POST",
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8"))
        finally:
            server.shutdown()

    def test_trace_visibility_footer_appends_footer(self) -> None:
        payload = self._roundtrip("footer")
        content = payload["choices"][0]["message"]["content"]
        self.assertIn("AGIF: mode=", content)
        self.assertIn(payload["x_agif_trace"]["trace_id"], content)

    def test_trace_visibility_both_appends_footer(self) -> None:
        payload = self._roundtrip("both")
        content = payload["choices"][0]["message"]["content"]
        self.assertIn("AGIF: mode=", content)
        # Metadata is also present
        self.assertIn("trace_id", payload["x_agif_trace"])


class OpenClawAuthTests(unittest.TestCase):
    """Bearer auth scoped to /v1/*, /health remains open."""

    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.trace_file = Path(self._tmpdir.name) / "openclaw.jsonl"
        self.server, self.port = _start_openclaw_server(
            trace_file=self.trace_file, proxy_api_key="s3cret",
        )
        self.base = f"http://127.0.0.1:{self.port}"

    def tearDown(self) -> None:
        self.server.shutdown()
        self._tmpdir.cleanup()

    def _post(self, body: dict, token: str | None) -> tuple[int, dict]:
        data = json.dumps(body).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"
        req = urllib.request.Request(
            f"{self.base}/v1/chat/completions", data=data, headers=headers, method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read().decode("utf-8"))

    def test_bearer_auth_missing_header_returns_401(self) -> None:
        body = {"model": SERVED_ID, "messages": [{"role": "user", "content": "x"}]}
        code, payload = self._post(body, token=None)
        self.assertEqual(code, 401)
        self.assertEqual(payload["error"]["code"], "invalid_api_key")

    def test_bearer_auth_wrong_token_returns_401(self) -> None:
        body = {"model": SERVED_ID, "messages": [{"role": "user", "content": "x"}]}
        code, _ = self._post(body, token="wrong")
        self.assertEqual(code, 401)

    def test_bearer_auth_correct_token_accepts(self) -> None:
        body = {"model": SERVED_ID, "messages": [{"role": "user", "content": "hi"}]}
        code, payload = self._post(body, token="s3cret")
        self.assertEqual(code, 200)
        self.assertEqual(payload["object"], "chat.completion")

    def test_bearer_auth_not_required_on_health(self) -> None:
        with urllib.request.urlopen(f"{self.base}/health", timeout=5) as resp:
            self.assertEqual(resp.status, 200)
            payload = json.loads(resp.read().decode("utf-8"))
            self.assertTrue(payload["auth_enabled"])

    def test_auth_failure_writes_audit_event_without_token(self) -> None:
        self._post(
            {"model": SERVED_ID, "messages": [{"role": "user", "content": "x"}]},
            token="wrong-token-value",
        )
        events = _read_audit_events(self.trace_file)
        fails = [e for e in events if e["event_type"] == "auth_failure"]
        self.assertEqual(len(fails), 1)
        ev = fails[0]
        self.assertEqual(ev["reason_code"], "wrong_token")
        # The token value must not appear anywhere in the audit file.
        raw = self.trace_file.read_text(encoding="utf-8")
        self.assertNotIn("wrong-token-value", raw)
        self.assertNotIn("s3cret", raw)

    def test_v0_1_no_secret_regression_trace_body_and_stderr(self) -> None:
        """v0.1 release invariant: bearer token never appears in any artifact.

        Locks the no-secret promise behaviorally across three surfaces:
          1. trace JSONL file (audit event emitted under fail-closed path)
          2. HTTP error response body returned to the client
          3. process stderr captured during the request

        If this test ever fails, that is a v0.1 regression to fix before any
        new release tag is cut. The configured server token is ``s3cret``;
        the request below uses a deliberately distinctive fake token so that
        any leak is unambiguous in the assertion failure message.
        """
        import contextlib
        import io

        fake_token = "fake-token-VERY-DISTINCTIVE-XYZ-9001"
        configured_secret = "s3cret"  # set in setUp via _start_openclaw_server

        body = {"model": SERVED_ID, "messages": [{"role": "user", "content": "x"}]}
        data = json.dumps(body).encode("utf-8")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {fake_token}",
        }
        req = urllib.request.Request(
            f"{self.base}/v1/chat/completions",
            data=data,
            headers=headers,
            method="POST",
        )

        # Capture stderr around the request. The proxy server runs in a
        # background thread but writes via module-level ``sys.stderr``, so
        # ``contextlib.redirect_stderr`` captures any print/traceback that
        # happens during the redirect window.
        captured_stderr = io.StringIO()
        error_body_bytes = b""
        with contextlib.redirect_stderr(captured_stderr):
            try:
                urllib.request.urlopen(req, timeout=10)
                self.fail("expected HTTPError on bearer-auth failure")
            except urllib.error.HTTPError as exc:
                self.assertEqual(exc.code, 401)
                error_body_bytes = exc.read()

        error_body = error_body_bytes.decode("utf-8", errors="replace")
        trace_raw = self.trace_file.read_text(encoding="utf-8")
        stderr_text = captured_stderr.getvalue()

        for label, blob in (
            ("error_response_body", error_body),
            ("trace_file", trace_raw),
            ("captured_stderr", stderr_text),
        ):
            self.assertNotIn(
                fake_token, blob,
                msg=f"fake bearer token leaked into {label}",
            )
            self.assertNotIn(
                configured_secret, blob,
                msg=f"configured server token leaked into {label}",
            )


# ---------------------------------------------------------------------------
# CLI-level validator tests (run _run_serve without binding a server)
# ---------------------------------------------------------------------------

class OpenClawCliValidatorTests(unittest.TestCase):
    def _run(self, argv: list[str], env: dict[str, str] | None = None) -> int:
        from agif_xcore.cli.main import build_parser
        from agif_xcore.cli.serve import _run_serve
        parser = build_parser()
        args = parser.parse_args(argv)
        original_env = {}
        if env:
            for k, v in env.items():
                original_env[k] = os.environ.get(k)
                os.environ[k] = v
        try:
            return _run_serve(args)
        finally:
            for k, original in original_env.items():
                if original is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = original

    def test_openclaw_requires_served_model_id_at_cli(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            rc = self._run([
                "serve",
                "--model", UPSTREAM_ID,
                "--openclaw-profile",
                "--trace-file", f"{d}/t.jsonl",
            ])
        self.assertEqual(rc, 2)

    def test_openclaw_requires_trace_file_at_cli(self) -> None:
        rc = self._run([
            "serve",
            "--model", UPSTREAM_ID,
            "--openclaw-profile",
            "--served-model-id", SERVED_ID,
        ])
        self.assertEqual(rc, 2)

    def test_openclaw_rejects_no_governance_at_cli(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            rc = self._run([
                "serve",
                "--model", UPSTREAM_ID,
                "--openclaw-profile",
                "--served-model-id", SERVED_ID,
                "--trace-file", f"{d}/t.jsonl",
                "--no-governance",
            ])
        self.assertEqual(rc, 2)

    def test_openclaw_rejects_non_loopback_bind_without_unsafe(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            rc = self._run([
                "serve",
                "--model", UPSTREAM_ID,
                "--openclaw-profile",
                "--served-model-id", SERVED_ID,
                "--trace-file", f"{d}/t.jsonl",
                "--host", "0.0.0.0",
            ])
        self.assertEqual(rc, 2)

    def test_openclaw_proxy_api_key_env_unset_returns_error(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            os.environ.pop("OPENCLAW_TEST_KEY_UNSET", None)
            rc = self._run([
                "serve",
                "--model", UPSTREAM_ID,
                "--openclaw-profile",
                "--served-model-id", SERVED_ID,
                "--trace-file", f"{d}/t.jsonl",
                "--proxy-api-key-env", "OPENCLAW_TEST_KEY_UNSET",
            ])
        self.assertEqual(rc, 2)


# ---------------------------------------------------------------------------
# Unit tests for pure helpers
# ---------------------------------------------------------------------------

class PureHelperTests(unittest.TestCase):
    def test_is_loopback_host_accepts_127_and_ipv6_and_localhost(self) -> None:
        self.assertTrue(_is_loopback_host("127.0.0.1"))
        self.assertTrue(_is_loopback_host("::1"))
        self.assertTrue(_is_loopback_host("localhost"))
        self.assertFalse(_is_loopback_host("0.0.0.0"))
        self.assertFalse(_is_loopback_host("10.0.0.1"))
        self.assertFalse(_is_loopback_host(""))

    def test_non_loopback_requires_unsafe_bind(self) -> None:
        # ProxyConfig itself does not enforce bind safety (the CLI does).
        # This test guards the CLI helper semantics end-to-end via the
        # standalone helper, and a separate CLI test confirms the
        # validator calls this helper.
        self.assertFalse(_is_loopback_host("0.0.0.0"))

    def test_has_tool_payload_empty_body_is_false(self) -> None:
        self.assertEqual(_has_tool_payload({}), (False, ""))

    def test_has_tool_payload_empty_tools_is_false(self) -> None:
        self.assertEqual(_has_tool_payload({"tools": []}), (False, ""))

    def test_has_tool_payload_tools_present(self) -> None:
        is_tool, code = _has_tool_payload({"tools": [{"type": "function"}]})
        self.assertTrue(is_tool)
        self.assertEqual(code, "tools_present")

    def test_has_tool_payload_tool_choice_none_is_false(self) -> None:
        self.assertEqual(
            _has_tool_payload({"tool_choice": "none"}), (False, ""),
        )

    def test_has_tool_payload_tool_choice_auto_is_true(self) -> None:
        is_tool, code = _has_tool_payload({"tool_choice": "auto"})
        self.assertTrue(is_tool)
        self.assertEqual(code, "tool_choice_not_none")


if __name__ == "__main__":
    unittest.main()
