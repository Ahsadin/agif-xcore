"""Unit tests for ``GovernedClient``.

Wires a stub backend directly into the client so these tests are
network-free and fast.
"""

from __future__ import annotations

import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agif_xcore import GovernedClient, ModelBackend
from agif_xcore.backends.base import BackendResponse


@dataclass
class _StubBackend:
    name: str = "stub"
    reply_text: str = "A short, honest answer."

    def complete(
        self,
        messages,
        *,
        model: str,
        temperature: float = 0.0,
        max_tokens: int | None = None,
        timeout_ms: int = 30_000,
        tools: list[dict] | None = None,
    ) -> BackendResponse:  # noqa: ARG002
        return BackendResponse(
            text=self.reply_text,
            model_id=model,
            finish_reason="stop",
            prompt_tokens=7,
            completion_tokens=5,
            latency_ms=2,
        )

    def healthcheck(self) -> dict[str, Any]:
        return {"reachable": True, "loaded_models": ["stubmodel"]}


class GovernedClientTests(unittest.TestCase):
    def _client(self, **kwargs) -> GovernedClient:
        return GovernedClient(backend=_StubBackend(), model="stubmodel", **kwargs)

    def test_ask_returns_answer_envelope(self) -> None:
        with self._client() as client:
            answer = client.ask("Tell me about BM25 in one sentence.")
        self.assertIn("answer", answer.text)  # stub reply contains the word "answer"
        self.assertTrue(answer.trace_id.startswith("turn_"))
        self.assertEqual(answer.answer_mode, "grounded_fact")
        self.assertGreaterEqual(answer.total_ms, 0)
        self.assertIsNotNone(answer.decisions)
        self.assertFalse(answer.decisions.governance_enabled)

    def test_ask_rejects_empty_input(self) -> None:
        with self._client() as client:
            with self.assertRaises(ValueError):
                client.ask("")
            with self.assertRaises(ValueError):
                client.ask("   ")

    def test_trace_file_is_written(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            trace_path = Path(tmp) / "traces.jsonl"
            with self._client(trace_file=trace_path) as client:
                client.ask("hello")
                client.ask("world")
            content = trace_path.read_text().strip().splitlines()
            self.assertEqual(len(content), 2)

    def test_new_conversation_changes_id(self) -> None:
        with self._client() as client:
            first = client.conversation_id
            new = client.new_conversation()
            self.assertNotEqual(first, new)
            self.assertEqual(client.conversation_id, new)

    def test_healthcheck_delegates_to_backend(self) -> None:
        with self._client() as client:
            result = client.healthcheck()
        self.assertTrue(result["reachable"])
        self.assertIn("stubmodel", result["loaded_models"])

    def test_model_required(self) -> None:
        with self.assertRaises(ValueError):
            GovernedClient(backend=_StubBackend(), model="")


class DeterministicTurnIdTests(unittest.TestCase):
    """Two asks with the same inputs + same clock produce the same turn id.

    We can't freeze the clock from outside, so we compare the underlying
    generation function directly instead. This test exists to document
    the determinism contract; the real replay test sits in
    ``tests/integration/test_replay_determinism.py``.
    """

    def test_make_turn_id_roundtrip(self) -> None:
        from agif_xcore.schemas import make_turn_id

        a = make_turn_id("conversation_A", "2026-04-12T00:00:00Z", "what is BM25?")
        b = make_turn_id("conversation_A", "2026-04-12T00:00:00Z", "what is BM25?")
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
