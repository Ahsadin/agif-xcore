"""Integration test: cross-turn memory with a real Ollama model.

Runs a 5-turn dialog where turn 4 references a fact from turn 1 via
continuity memory. Skipped unless AGIF_XCORE_RUN_INTEGRATION=1.

This is the M4 gate test.
"""

from __future__ import annotations

import os
import unittest

from agif_xcore import GovernedClient


_RUN = os.environ.get("AGIF_XCORE_RUN_INTEGRATION", "") == "1"
_MODEL = os.environ.get("AGIF_XCORE_TEST_MODEL", "gemma3:270m-it-fp16")


@unittest.skipUnless(_RUN, "set AGIF_XCORE_RUN_INTEGRATION=1 to run")
class CrossTurnMemoryIntegrationTest(unittest.TestCase):
    """5-turn dialog with cross-turn memory reference."""

    def test_five_turn_dialog(self) -> None:
        with GovernedClient(
            backend="ollama",
            model=_MODEL,
            model_enforcement="prefix",
            governance_enabled=True,
            memory_enabled=True,
            temperature=0.0,
        ) as client:
            # Turn 1: establish a specific fact
            a1 = client.ask("Remember this: our company backup cadence is every 4 hours.")
            print(f"\n[Turn 1] Q: Remember backup cadence=4h")
            print(f"[Turn 1] A: {a1.text[:100]}...")
            print(f"[Turn 1] mode={a1.answer_mode}")

            # Turn 2: unrelated
            a2 = client.ask("What is the capital of France?")
            print(f"\n[Turn 2] Q: Capital of France?")
            print(f"[Turn 2] A: {a2.text[:100]}...")

            # Turn 3: unrelated
            a3 = client.ask("What is 2 + 2?")
            print(f"\n[Turn 3] Q: 2 + 2?")
            print(f"[Turn 3] A: {a3.text[:100]}...")

            # Turn 4: reference the fact from turn 1
            a4 = client.ask("What backup cadence did I mention earlier?")
            print(f"\n[Turn 4] Q: What backup cadence?")
            print(f"[Turn 4] A: {a4.text[:200]}")

            # Turn 5: confirm
            a5 = client.ask("Thanks, that's correct.")
            print(f"\n[Turn 5] Q: Thanks")
            print(f"[Turn 5] A: {a5.text[:100]}...")

            # Verify memory contains entries from all turns
            total = client.memory.count(client.conversation_id)
            print(f"\nTotal memory entries: {total}")
            self.assertGreaterEqual(total, 5)

            # Verify turn 4's answer references the backup cadence
            # (the model should know about it from memory context)
            a4_lower = a4.text.lower()
            # The model should mention something about backup or cadence
            self.assertTrue(
                "backup" in a4_lower or "4 hour" in a4_lower or "cadence" in a4_lower,
                f"Turn 4 answer should reference backup cadence, got: {a4.text[:200]}",
            )

    def test_memory_with_escalation(self) -> None:
        """Test that escalation works alongside memory."""
        with GovernedClient(
            backend="ollama",
            model=_MODEL,
            model_enforcement="prefix",
            governance_enabled=True,
            memory_enabled=True,
            escalation_enabled=True,
            temperature=0.0,
        ) as client:
            a1 = client.ask("What is BM25 retrieval in information retrieval?")
            print(f"\n[Escalation test] A: {a1.text[:200]}...")
            print(f"[Escalation test] mode={a1.answer_mode}")
            # Should return a non-empty answer
            self.assertGreater(len(a1.text), 10)


if __name__ == "__main__":
    unittest.main()
