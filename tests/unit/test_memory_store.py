"""Tests for the memory module.

Covers: InMemoryStore CRUD, ConversationMemory admission/storage/retrieval,
plane capacity enforcement, supersession, and prompt formatting.
"""

from __future__ import annotations

import unittest

from agif_xcore.memory.base import (
    MEMORY_PLANES,
    InMemoryStore,
    MemoryEntry,
)
from agif_xcore.memory.store import ConversationMemory


class InMemoryStoreTests(unittest.TestCase):
    """Low-level store operations."""

    def setUp(self) -> None:
        self.store = InMemoryStore()

    def _make_entry(self, **overrides) -> MemoryEntry:
        defaults = {
            "entry_id": "mem:continuity:abc123",
            "plane": "continuity",
            "key": "test question",
            "content": "Q: test question\nA: test answer",
            "source_turn_id": "turn_0001",
            "conversation_id": "conv_001",
            "created_at": "2026-04-12T00:00:00Z",
        }
        defaults.update(overrides)
        return MemoryEntry(**defaults)

    def test_write_and_read(self) -> None:
        entry = self._make_entry()
        self.store.write(entry)
        result = self.store.read("mem:continuity:abc123")
        self.assertIsNotNone(result)
        self.assertEqual(result.content, "Q: test question\nA: test answer")

    def test_read_nonexistent_returns_none(self) -> None:
        self.assertIsNone(self.store.read("nonexistent"))

    def test_query_by_conversation(self) -> None:
        self.store.write(self._make_entry(entry_id="e1", conversation_id="conv_A"))
        self.store.write(self._make_entry(entry_id="e2", conversation_id="conv_B"))
        self.store.write(self._make_entry(entry_id="e3", conversation_id="conv_A"))
        results = self.store.query("conv_A")
        self.assertEqual(len(results), 2)
        ids = {r.entry_id for r in results}
        self.assertEqual(ids, {"e1", "e3"})

    def test_query_by_plane(self) -> None:
        self.store.write(self._make_entry(entry_id="e1", plane="continuity"))
        self.store.write(self._make_entry(entry_id="e2", plane="episodic"))
        results = self.store.query("conv_001", plane="continuity")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].entry_id, "e1")

    def test_query_excludes_superseded(self) -> None:
        self.store.write(self._make_entry(entry_id="e1"))
        self.store.write(self._make_entry(entry_id="e2"))
        self.store.supersede("e1", "e2")
        results = self.store.query("conv_001")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].entry_id, "e2")

    def test_query_returns_newest_first(self) -> None:
        self.store.write(self._make_entry(entry_id="e1", created_at="2026-01-01T00:00:00Z"))
        self.store.write(self._make_entry(entry_id="e2", created_at="2026-01-02T00:00:00Z"))
        self.store.write(self._make_entry(entry_id="e3", created_at="2026-01-03T00:00:00Z"))
        results = self.store.query("conv_001")
        self.assertEqual([r.entry_id for r in results], ["e3", "e2", "e1"])

    def test_clear_by_conversation(self) -> None:
        self.store.write(self._make_entry(entry_id="e1", conversation_id="conv_A"))
        self.store.write(self._make_entry(entry_id="e2", conversation_id="conv_B"))
        self.store.clear("conv_A")
        self.assertEqual(len(self.store.query("conv_A")), 0)
        self.assertEqual(len(self.store.query("conv_B")), 1)

    def test_clear_all(self) -> None:
        self.store.write(self._make_entry(entry_id="e1", conversation_id="conv_A"))
        self.store.write(self._make_entry(entry_id="e2", conversation_id="conv_B"))
        self.store.clear()
        self.assertEqual(self.store.count(), 0)

    def test_count(self) -> None:
        self.store.write(self._make_entry(entry_id="e1", plane="continuity"))
        self.store.write(self._make_entry(entry_id="e2", plane="episodic"))
        self.store.write(self._make_entry(entry_id="e3", plane="continuity"))
        self.assertEqual(self.store.count(), 3)
        self.assertEqual(self.store.count(plane="continuity"), 2)

    def test_invalid_plane_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.store.write(self._make_entry(plane="invalid"))

    def test_supersede_marks_old_entry(self) -> None:
        self.store.write(self._make_entry(entry_id="old"))
        self.store.supersede("old", "new")
        old = self.store.read("old")
        self.assertEqual(old.superseded_by, "new")


class MemoryEntryTests(unittest.TestCase):
    def test_make_entry_id_deterministic(self) -> None:
        a = MemoryEntry.make_entry_id("continuity", "turn_1", "what is BM25?")
        b = MemoryEntry.make_entry_id("continuity", "turn_1", "what is BM25?")
        self.assertEqual(a, b)
        self.assertTrue(a.startswith("mem:continuity:"))

    def test_make_entry_id_varies_by_plane(self) -> None:
        a = MemoryEntry.make_entry_id("continuity", "turn_1", "q")
        b = MemoryEntry.make_entry_id("episodic", "turn_1", "q")
        self.assertNotEqual(a, b)

    def test_all_planes_known(self) -> None:
        self.assertIn("working", MEMORY_PLANES)
        self.assertIn("episodic", MEMORY_PLANES)
        self.assertIn("continuity", MEMORY_PLANES)


class ConversationMemoryTests(unittest.TestCase):
    """Higher-level memory operations with admission gating."""

    def setUp(self) -> None:
        self.mem = ConversationMemory()

    def test_admit_and_store_accepted(self) -> None:
        decision = {
            "decision_class": "admit_write",
            "target_memory_ref_or_none": "mem:continuity:turn_1",
            "superseded_memory_ref_or_none": None,
        }
        entry = self.mem.admit_and_store(
            memory_admission_decision=decision,
            turn_id="turn_1",
            conversation_id="conv_1",
            question="What is BM25?",
            answer_text="BM25 is a ranking function used in information retrieval.",
        )
        self.assertIsNotNone(entry)
        self.assertEqual(entry.plane, "continuity")
        self.assertIn("BM25", entry.content)

    def test_admit_and_store_rejected(self) -> None:
        decision = {
            "decision_class": "reject_write",
            "target_memory_ref_or_none": None,
            "superseded_memory_ref_or_none": None,
        }
        entry = self.mem.admit_and_store(
            memory_admission_decision=decision,
            turn_id="turn_1",
            conversation_id="conv_1",
            question="q",
            answer_text="a",
        )
        self.assertIsNone(entry)

    def test_admit_and_store_explicit_none(self) -> None:
        decision = {"decision_class": "explicit_none"}
        entry = self.mem.admit_and_store(
            memory_admission_decision=decision,
            turn_id="turn_1",
            conversation_id="conv_1",
            question="q",
            answer_text="a",
        )
        self.assertIsNone(entry)

    def test_store_episodic_always_stores(self) -> None:
        entry = self.mem.store_episodic(
            turn_id="turn_1",
            conversation_id="conv_1",
            question="hello",
            answer_text="hi there",
            answer_mode="grounded_fact",
            governance_enabled=True,
        )
        self.assertEqual(entry.plane, "episodic")
        self.assertIn("hello", entry.content)

    def test_retrieve_context_returns_prior_turns(self) -> None:
        # Store two turns
        self.mem.store_episodic(
            turn_id="turn_1", conversation_id="conv_1",
            question="What is BM25?",
            answer_text="BM25 is a ranking function.",
            answer_mode="grounded_fact", governance_enabled=True,
        )
        self.mem.store_episodic(
            turn_id="turn_2", conversation_id="conv_1",
            question="How does it work?",
            answer_text="It uses term frequency and inverse document frequency.",
            answer_mode="derived_explanation", governance_enabled=True,
        )
        # Retrieve context excluding current turn
        entries = self.mem.retrieve_context("conv_1", exclude_turn_id="turn_3")
        self.assertEqual(len(entries), 2)

    def test_retrieve_context_excludes_current_turn(self) -> None:
        self.mem.store_episodic(
            turn_id="turn_1", conversation_id="conv_1",
            question="q", answer_text="a",
            answer_mode="grounded_fact", governance_enabled=True,
        )
        entries = self.mem.retrieve_context("conv_1", exclude_turn_id="turn_1")
        self.assertEqual(len(entries), 0)

    def test_retrieve_context_separates_conversations(self) -> None:
        self.mem.store_episodic(
            turn_id="turn_1", conversation_id="conv_A",
            question="q1", answer_text="a1",
            answer_mode="grounded_fact", governance_enabled=True,
        )
        self.mem.store_episodic(
            turn_id="turn_2", conversation_id="conv_B",
            question="q2", answer_text="a2",
            answer_mode="grounded_fact", governance_enabled=True,
        )
        entries_a = self.mem.retrieve_context("conv_A")
        entries_b = self.mem.retrieve_context("conv_B")
        self.assertEqual(len(entries_a), 1)
        self.assertEqual(len(entries_b), 1)

    def test_format_for_prompt_empty(self) -> None:
        result = self.mem.format_for_prompt([])
        self.assertEqual(result, "")

    def test_format_for_prompt_with_entries(self) -> None:
        entry = MemoryEntry(
            entry_id="e1", plane="continuity", key="q",
            content="User said: What is BM25?. Response: A ranking function.",
            source_turn_id="turn_1", conversation_id="conv_1",
            created_at="2026-04-12T00:00:00Z",
        )
        result = self.mem.format_for_prompt([entry])
        self.assertIn("Established fact from earlier", result)
        self.assertIn("BM25", result)

    def test_format_deduplicates_episodic_covered_by_continuity(self) -> None:
        """Episodic entries already covered by continuity are not repeated."""
        continuity = MemoryEntry(
            entry_id="c1", plane="continuity", key="q",
            content="Q: q\nA: a", source_turn_id="turn_1",
            conversation_id="conv_1", created_at="2026-04-12T00:00:00Z",
        )
        episodic = MemoryEntry(
            entry_id="e1", plane="episodic", key="q",
            content="Q: q\nA: a", source_turn_id="turn_1",
            conversation_id="conv_1", created_at="2026-04-12T00:00:00Z",
        )
        result = self.mem.format_for_prompt([continuity, episodic])
        # Should contain "Established fact" but NOT "Prior exchange"
        # because the episodic entry covers the same turn as continuity
        self.assertIn("Established fact", result)
        self.assertNotIn("Prior exchange", result)

    def test_clear_conversation(self) -> None:
        self.mem.store_episodic(
            turn_id="t1", conversation_id="conv_1",
            question="q", answer_text="a",
            answer_mode="grounded_fact", governance_enabled=True,
        )
        self.mem.clear("conv_1")
        self.assertEqual(self.mem.count("conv_1"), 0)

    def test_supersession_via_admission(self) -> None:
        """When a memory suggestion supersedes an old entry, the old entry is marked."""
        # First, store an entry directly
        old_entry = MemoryEntry(
            entry_id="old_ref", plane="continuity", key="q",
            content="old content", source_turn_id="turn_1",
            conversation_id="conv_1", created_at="2026-04-12T00:00:00Z",
        )
        self.mem.store.write(old_entry)

        # Now admit a new entry that supersedes it
        decision = {
            "decision_class": "admit_write",
            "target_memory_ref_or_none": "mem:continuity:turn_2",
            "superseded_memory_ref_or_none": "old_ref",
        }
        new_entry = self.mem.admit_and_store(
            memory_admission_decision=decision,
            turn_id="turn_2",
            conversation_id="conv_1",
            question="updated q",
            answer_text="updated answer",
        )
        self.assertIsNotNone(new_entry)
        # Old entry should be superseded
        old = self.mem.store.read("old_ref")
        self.assertEqual(old.superseded_by, new_entry.entry_id)

    def test_count_by_plane(self) -> None:
        self.mem.store_episodic(
            turn_id="t1", conversation_id="conv_1",
            question="q1", answer_text="a1",
            answer_mode="grounded_fact", governance_enabled=True,
        )
        decision = {"decision_class": "admit_write",
                     "target_memory_ref_or_none": "ref", "superseded_memory_ref_or_none": None}
        self.mem.admit_and_store(
            memory_admission_decision=decision,
            turn_id="t2", conversation_id="conv_1",
            question="q2", answer_text="a2",
        )
        self.assertEqual(self.mem.count("conv_1", plane="episodic"), 1)
        self.assertEqual(self.mem.count("conv_1", plane="continuity"), 1)


if __name__ == "__main__":
    unittest.main()
