"""Unit tests for the OpenAI-compatible backend.

We monkey-patch ``urllib.request.urlopen`` so the tests never touch the
network. This is the M1 zero-dep equivalent of ``respx`` (which is a
planned dev-extra for M3+).
"""

from __future__ import annotations

import io
import json
import unittest
import urllib.error
import urllib.request
from contextlib import contextmanager
from typing import Any

from agif_xcore.backends.base import (
    BackendBlocked,
    BackendContractError,
    BackendModelMismatch,
)
from agif_xcore.backends.openai_compat import OpenAICompatBackend, OpenAICompatConfig


# ---------------------------------------------------------------------------
# Test double for urllib.request.urlopen
# ---------------------------------------------------------------------------

class _FakeResponse:
    def __init__(self, body: bytes, status: int = 200) -> None:
        self._body = body
        self.status = status

    def read(self) -> bytes:
        return self._body

    def __enter__(self) -> "_FakeResponse":
        return self

    def __exit__(self, *_exc: object) -> None:
        return None


def _fake_http_error(code: int, message: str = "boom") -> urllib.error.HTTPError:
    return urllib.error.HTTPError(
        url="http://x/",
        code=code,
        msg=message,
        hdrs=None,  # type: ignore[arg-type]
        fp=io.BytesIO(message.encode("utf-8")),
    )


@contextmanager
def patched_urlopen(handler):
    """Temporarily replace urllib.request.urlopen with ``handler``."""
    original = urllib.request.urlopen
    urllib.request.urlopen = handler  # type: ignore[assignment]
    try:
        yield
    finally:
        urllib.request.urlopen = original  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class CompleteHappyPathTests(unittest.TestCase):
    def _backend(self, enforcement: str = "strict") -> OpenAICompatBackend:
        return OpenAICompatBackend(
            OpenAICompatConfig(
                base_url="http://localhost:9999/v1",
                model_enforcement=enforcement,
            )
        )

    def _handler_for(self, payload: dict[str, Any]):
        def handler(request, timeout=None):  # noqa: ARG001
            body = json.dumps(payload).encode("utf-8")
            return _FakeResponse(body)

        return handler

    def test_returns_text_from_choices(self) -> None:
        backend = self._backend()
        payload = {
            "model": "gemma3:270m",
            "choices": [
                {
                    "message": {"role": "assistant", "content": "Hello world."},
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 10, "completion_tokens": 3},
        }
        with patched_urlopen(self._handler_for(payload)):
            result = backend.complete(
                [{"role": "user", "content": "hi"}],
                model="gemma3:270m",
            )
        self.assertEqual(result.text, "Hello world.")
        self.assertEqual(result.model_id, "gemma3:270m")
        self.assertEqual(result.finish_reason, "stop")
        self.assertEqual(result.prompt_tokens, 10)
        self.assertEqual(result.completion_tokens, 3)
        self.assertGreaterEqual(result.latency_ms, 0)

    def test_strict_enforcement_rejects_model_mismatch(self) -> None:
        backend = self._backend("strict")
        payload = {
            "model": "llama3.2:latest",  # <- server returned something else
            "choices": [
                {"message": {"role": "assistant", "content": "x"}, "finish_reason": "stop"}
            ],
        }
        with patched_urlopen(self._handler_for(payload)):
            with self.assertRaises(BackendModelMismatch):
                backend.complete(
                    [{"role": "user", "content": "hi"}],
                    model="gemma3:270m",
                )

    def test_prefix_enforcement_accepts_versioned_model_id(self) -> None:
        backend = self._backend("prefix")
        payload = {
            "model": "gemma3:270m-instruct-fp16",
            "choices": [
                {"message": {"role": "assistant", "content": "x"}, "finish_reason": "stop"}
            ],
        }
        with patched_urlopen(self._handler_for(payload)):
            result = backend.complete(
                [{"role": "user", "content": "hi"}],
                model="gemma3:270m",
            )
        self.assertEqual(result.text, "x")

    def test_off_enforcement_accepts_anything(self) -> None:
        backend = self._backend("off")
        payload = {
            "model": "anything-else",
            "choices": [
                {"message": {"role": "assistant", "content": "x"}, "finish_reason": "stop"}
            ],
        }
        with patched_urlopen(self._handler_for(payload)):
            result = backend.complete(
                [{"role": "user", "content": "hi"}],
                model="gemma3:270m",
            )
        self.assertEqual(result.text, "x")


class CompleteErrorPathTests(unittest.TestCase):
    def _backend(self) -> OpenAICompatBackend:
        return OpenAICompatBackend(OpenAICompatConfig(base_url="http://localhost:9999/v1"))

    def test_empty_messages_rejected(self) -> None:
        backend = self._backend()
        with self.assertRaises(BackendContractError):
            backend.complete([], model="gemma3:270m")

    def test_empty_model_rejected(self) -> None:
        backend = self._backend()
        with self.assertRaises(BackendContractError):
            backend.complete([{"role": "user", "content": "hi"}], model="")

    def test_missing_choices_rejected(self) -> None:
        backend = self._backend()

        def handler(request, timeout=None):  # noqa: ARG001
            return _FakeResponse(b"{}")

        with patched_urlopen(handler):
            with self.assertRaises(BackendContractError):
                backend.complete(
                    [{"role": "user", "content": "hi"}],
                    model="gemma3:270m",
                )

    def test_non_json_response_rejected(self) -> None:
        backend = self._backend()

        def handler(request, timeout=None):  # noqa: ARG001
            return _FakeResponse(b"<html>not json</html>")

        with patched_urlopen(handler):
            with self.assertRaises(BackendContractError):
                backend.complete(
                    [{"role": "user", "content": "hi"}],
                    model="gemma3:270m",
                )

    def test_http_error_raises_blocked(self) -> None:
        backend = self._backend()

        def handler(request, timeout=None):  # noqa: ARG001
            raise _fake_http_error(503, "upstream down")

        with patched_urlopen(handler):
            with self.assertRaises(BackendBlocked):
                backend.complete(
                    [{"role": "user", "content": "hi"}],
                    model="gemma3:270m",
                )

    def test_url_error_raises_blocked(self) -> None:
        backend = self._backend()

        def handler(request, timeout=None):  # noqa: ARG001
            raise urllib.error.URLError("connection refused")

        with patched_urlopen(handler):
            with self.assertRaises(BackendBlocked):
                backend.complete(
                    [{"role": "user", "content": "hi"}],
                    model="gemma3:270m",
                )


class HealthcheckTests(unittest.TestCase):
    def test_healthcheck_returns_models(self) -> None:
        backend = OpenAICompatBackend(
            OpenAICompatConfig(base_url="http://localhost:9999/v1")
        )

        def handler(request, timeout=None):  # noqa: ARG001
            body = json.dumps(
                {
                    "object": "list",
                    "data": [
                        {"id": "gemma3:270m"},
                        {"id": "llama3.2:latest"},
                    ],
                }
            ).encode("utf-8")
            return _FakeResponse(body)

        with patched_urlopen(handler):
            result = backend.healthcheck()
        self.assertTrue(result["reachable"])
        self.assertIn("gemma3:270m", result["loaded_models"])
        self.assertIn("llama3.2:latest", result["loaded_models"])
        self.assertIsNone(result["error"])

    def test_healthcheck_never_raises_on_failure(self) -> None:
        backend = OpenAICompatBackend(
            OpenAICompatConfig(base_url="http://localhost:9999/v1")
        )

        def handler(request, timeout=None):  # noqa: ARG001
            raise urllib.error.URLError("connection refused")

        with patched_urlopen(handler):
            result = backend.healthcheck()
        self.assertFalse(result["reachable"])
        self.assertEqual(result["loaded_models"], [])
        self.assertIsNotNone(result["error"])


class ConfigValidationTests(unittest.TestCase):
    def test_empty_base_url_rejected(self) -> None:
        with self.assertRaises(Exception):
            OpenAICompatBackend(OpenAICompatConfig(base_url=""))


if __name__ == "__main__":
    unittest.main()
