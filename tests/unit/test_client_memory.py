"""Tests for GovernedClient with memory and escalation enabled.

Verifies:
  * Memory entries are stored after governed turns.
  * Memory context from prior turns is injected into the planner prompt.
  * Cross-turn continuity: turn N can reference facts from turn 1.
  * Escalation retries weak answers exactly once.
  * Episodic memory is always stored (not gated by admission).
  * Memory is conversation-scoped.
"""

from __future__ import annotations

import unittest
from dataclasses import dataclass, field
from typing import Any

from agif_xcore import GovernedClient
from agif_xcore.backends.base import BackendResponse


# ---------------------------------------------------------------------------
# Stub backend that records prompts for inspection
# ---------------------------------------------------------------------------

@dataclass
class _RecordingBackend:
    """Backend that records every message list it receives."""

    name: str = "recording"
    reply_text: str = "The backup cadence is daily incremental."
    call_count: int = 0
    recorded_messages: list[list[dict]] = field(default_factory=list)

    def complete(
        self,
        messages,
        *,
        model: str,
        temperature: float = 0.0,
        max_tokens: int | None = None,
        timeout_ms: int = 30_000,
    ) -> BackendResponse:
        self.call_count += 1
        self.recorded_messages.append(list(messages))
        return BackendResponse(
            text=self.reply_text,
            model_id=model,
            finish_reason="stop",
            prompt_tokens=10,
            completion_tokens=8,
            latency_ms=2,
        )

    def healthcheck(self) -> dict[str, Any]:
        return {"reachable": True, "loaded_models": ["stubmodel"]}


@dataclass
class _WeakThenStrongBackend:
    """First call returns a weak answer; second call returns a strong one."""

    name: str = "weak_then_strong"
    _call_count: int = 0
    recorded_messages: list[list[dict]] = field(default_factory=list)

    def complete(
        self,
        messages,
        *,
        model: str,
        temperature: float = 0.0,
        max_tokens: int | None = None,
        timeout_ms: int = 30_000,
    ) -> BackendResponse:
        self._call_count += 1
        self.recorded_messages.append(list(messages))
        if self._call_count == 1:
            text = "Maybe perhaps I think it might be something."
        else:
            text = (
                "The backup cadence is daily incremental with weekly full backups. "
                "Retention is 90 days per the enterprise policy."
            )
        return BackendResponse(
            text=text, model_id=model, finish_reason="stop",
            prompt_tokens=10, completion_tokens=8, latency_ms=2,
        )

    def healthcheck(self) -> dict[str, Any]:
        return {"reachable": True, "loaded_models": ["stubmodel"]}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class MemoryEnabledTests(unittest.TestCase):
    """Memory storage and retrieval across turns."""

    def test_memory_stored_after_governed_turn(self) -> None:
        """With governance ON + memory ON, entries should be stored."""
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True, memory_enabled=True,
        ) as client:
            client.ask("What is BM25?")
            # Should have at least episodic + continuity entry
            count = client.memory.count(client.conversation_id)
            self.assertGreaterEqual(count, 1)

    def test_episodic_always_stored_without_governance(self) -> None:
        """Even without governance, episodic memory is recorded."""
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=False, memory_enabled=True,
        ) as client:
            client.ask("Hello")
            count = client.memory.count(client.conversation_id, plane="episodic")
            self.assertEqual(count, 1)

    def test_memory_context_injected_into_second_turn(self) -> None:
        """The planner prompt for turn 2 should contain context from turn 1."""
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True, memory_enabled=True,
        ) as client:
            client.ask("Our backup cadence is daily incremental.")
            client.ask("What was the backup cadence I mentioned?")

            # The second call to the backend should have memory context
            self.assertEqual(backend.call_count, 2)
            second_messages = backend.recorded_messages[1]
            user_content = second_messages[1]["content"]
            self.assertIn("backup cadence", user_content.lower())
            # Should have a memory section
            self.assertIn("Earlier in our conversation", user_content)

    def test_memory_scoped_to_conversation(self) -> None:
        """Memory from conversation A should not leak into conversation B."""
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True, memory_enabled=True,
        ) as client:
            client.ask("The secret password is sesame.")
            # Start a new conversation
            client.new_conversation()
            client.ask("What was the password?")

            # Second call should NOT contain "sesame" in memory context
            second_messages = backend.recorded_messages[1]
            user_content = second_messages[1]["content"]
            self.assertNotIn("sesame", user_content)

    def test_memory_disabled_no_injection(self) -> None:
        """With memory_enabled=False, no context should be injected."""
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True, memory_enabled=False,
        ) as client:
            client.ask("First turn")
            client.ask("Second turn")

            second_messages = backend.recorded_messages[1]
            user_content = second_messages[1]["content"]
            self.assertNotIn("Conversation Memory", user_content)

    def test_five_turn_dialog_cross_reference(self) -> None:
        """M4 gate: turn 4 references a fact from turn 1 via memory.

        This is a unit test with a stub backend. The integration test
        hits a real model.
        """
        backend = _RecordingBackend(
            reply_text="The backup cadence is daily incremental per our SOP."
        )
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True, memory_enabled=True,
        ) as client:
            # Turn 1: establish a fact
            client.ask("Our SOP says backup cadence is daily incremental.")
            # Turn 2: unrelated
            client.ask("What is the weather today?")
            # Turn 3: unrelated
            client.ask("Tell me about Python typing.")
            # Turn 4: reference turn 1's fact
            client.ask("What backup cadence did I mention earlier?")
            # Turn 5: final turn
            client.ask("Thanks, that's all.")

            # Verify turn 4's prompt contains turn 1's content
            turn_4_messages = backend.recorded_messages[3]
            user_content = turn_4_messages[1]["content"]
            self.assertIn("backup cadence", user_content.lower())
            self.assertIn("Earlier in our conversation", user_content)

            # Verify memory has entries from all 5 turns
            total = client.memory.count(client.conversation_id)
            self.assertGreaterEqual(total, 5)  # at least 5 episodic


class EscalationTests(unittest.TestCase):
    """Weak-answer escalation integration with the client."""

    def test_escalation_retries_weak_answer(self) -> None:
        """When escalation is enabled and the first answer is weak, retry once."""
        backend = _WeakThenStrongBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True,
            escalation_enabled=True,
        ) as client:
            answer = client.ask("What is the backup cadence?")
            # Should have called backend twice (original + retry)
            self.assertEqual(backend._call_count, 2)
            # Final answer should be the stronger one
            self.assertIn("backup cadence", answer.text.lower())

    def test_escalation_disabled_no_retry(self) -> None:
        """When escalation is disabled, no retry even for weak answers."""
        backend = _WeakThenStrongBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True,
            escalation_enabled=False,
        ) as client:
            client.ask("What is the backup cadence?")
            self.assertEqual(backend._call_count, 1)

    def test_escalation_only_with_governance(self) -> None:
        """Escalation requires governance to be enabled."""
        backend = _WeakThenStrongBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=False,
            escalation_enabled=True,
        ) as client:
            client.ask("What is the backup cadence?")
            # No retry because governance is off
            self.assertEqual(backend._call_count, 1)

    def test_escalation_retry_prompt_includes_original(self) -> None:
        """The retry prompt should reference the original weak answer."""
        backend = _WeakThenStrongBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
            governance_enabled=True,
            escalation_enabled=True,
        ) as client:
            client.ask("What is the backup cadence?")
            # Check the retry message (second call)
            self.assertEqual(len(backend.recorded_messages), 2)
            retry_messages = backend.recorded_messages[1]
            retry_user = retry_messages[1]["content"]
            self.assertIn("previous answer", retry_user.lower())


class MemoryPropertyTests(unittest.TestCase):
    """Verify the new client properties."""

    def test_memory_enabled_property(self) -> None:
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel", memory_enabled=True,
        ) as client:
            self.assertTrue(client.memory_enabled)

    def test_memory_disabled_property(self) -> None:
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel", memory_enabled=False,
        ) as client:
            self.assertFalse(client.memory_enabled)

    def test_memory_object_accessible(self) -> None:
        backend = _RecordingBackend()
        with GovernedClient(
            backend=backend, model="stubmodel",
        ) as client:
            self.assertIsNotNone(client.memory)


if __name__ == "__main__":
    unittest.main()
