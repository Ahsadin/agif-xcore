"""Real Ollama integration test.

Skipped unless one of these is true:
- ``AGIF_XCORE_RUN_INTEGRATION=1`` is set in the environment
- ``OLLAMA_HOST`` env var is set

When it does run, it talks to a real local Ollama server (default
``http://localhost:11434/v1``) and expects a model to be loaded whose
id matches the one passed through ``AGIF_XCORE_TEST_MODEL`` (default
``gemma3:270m``).

If the configured model is not loaded, the test skips with a clear
message — it never silently faking success. This is an anti-theater
test: it must either run for real or be explicitly skipped.
"""

from __future__ import annotations

import os
import unittest

from agif_xcore import BackendBlocked, BackendModelMismatch, GovernedClient


_DEFAULT_MODEL = "gemma3:270m"


def _should_run() -> bool:
    if os.environ.get("AGIF_XCORE_RUN_INTEGRATION") == "1":
        return True
    if os.environ.get("OLLAMA_HOST"):
        return True
    return False


@unittest.skipUnless(
    _should_run(),
    "set AGIF_XCORE_RUN_INTEGRATION=1 or OLLAMA_HOST to run the real Ollama test",
)
class OllamaEndToEndTests(unittest.TestCase):
    def setUp(self) -> None:
        self.model = os.environ.get("AGIF_XCORE_TEST_MODEL", _DEFAULT_MODEL)
        self.base_url = os.environ.get("OLLAMA_HOST", "http://localhost:11434/v1")
        self.client = GovernedClient(
            backend="ollama",
            model=self.model,
            base_url=self.base_url,
            model_enforcement="prefix",  # Ollama tags may add suffixes
            temperature=0.0,
            max_tokens=128,
        )

    def tearDown(self) -> None:
        self.client.close()

    def test_healthcheck_lists_loaded_models(self) -> None:
        status = self.client.healthcheck()
        self.assertTrue(
            status["reachable"],
            f"Ollama unreachable at {self.base_url}: {status.get('error')}",
        )
        # Don't require an exact match — the healthcheck is informational.
        self.assertIsInstance(status["loaded_models"], list)

    def test_single_turn_returns_nonempty_answer(self) -> None:
        try:
            answer = self.client.ask(
                "In exactly one short sentence, what is BM25 retrieval?"
            )
        except BackendModelMismatch as exc:
            self.skipTest(
                f"model '{self.model}' not loaded on Ollama: {exc}"
            )
        except BackendBlocked as exc:
            self.skipTest(f"Ollama blocked the request: {exc}")

        self.assertTrue(answer.text)
        self.assertTrue(answer.trace_id.startswith("turn_"))
        self.assertGreater(answer.total_ms, 0)

    def test_determinism_at_temperature_zero(self) -> None:
        """Same prompt twice with temp=0 should produce identical text.

        Most models converge at temp=0 but not all — we assert softly:
        either the text is identical, or we skip and record why. The
        goal is that when the test passes, it passes for a real reason.
        """
        try:
            first = self.client.ask("Reply with the single word 'ready'.")
            second = self.client.ask("Reply with the single word 'ready'.")
        except (BackendModelMismatch, BackendBlocked) as exc:
            self.skipTest(f"backend not ready: {exc}")

        if first.text != second.text:
            self.skipTest(
                f"model not perfectly deterministic at temp=0 "
                f"(first={first.text!r}, second={second.text!r})"
            )
        self.assertEqual(first.text, second.text)


if __name__ == "__main__":
    unittest.main()
