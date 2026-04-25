"""Conversation memory — the bridge between substrate and storage.

``ConversationMemory`` is what the ``GovernedClient`` holds. It:

  1. Receives ``memory_admission_decision`` from the substrate.
  2. If the decision is ``admit_write``, stores the entry.
  3. On the next turn, retrieves relevant entries from prior turns
     and formats them for injection into the planner prompt.

Memory planes (ported from AGIFCore Phase 4):

  * **working** — current-turn scratch. Cleared at the start of each
    turn. Not injected into prompts (it *is* the current turn).
  * **episodic** — one entry per governed turn, recording the question
    and answer. Forms the conversation history.
  * **continuity** — key facts the model established. These persist
    and get injected into future turns so the model can reference
    them without re-asking.

Bounded: each plane enforces a max-entry cap. When the cap is hit,
the oldest entry is evicted (FIFO).
"""

from __future__ import annotations

from typing import Any

from .base import (
    MAX_CONTINUITY_ENTRIES,
    MAX_EPISODIC_ENTRIES,
    MAX_WORKING_ENTRIES,
    InMemoryStore,
    MemoryEntry,
    MemoryStore,
)


# ---------------------------------------------------------------------------
# Filler response detection
# ---------------------------------------------------------------------------

_FILLER_PHRASES: tuple[str, ...] = (
    "okay",
    "ok",
    "i understand",
    "got it",
    "sure",
    "understood",
    "noted",
    "alright",
    "acknowledged",
)


def _is_filler_response(text: str) -> bool:
    """Return True if the text is a short filler/acknowledgement.

    Small models often respond with "Okay, I understand." to factual
    statements. Storing those responses in memory context poisons
    subsequent turns — the model copies the filler instead of answering.
    """
    clean = text.lower().strip().rstrip(".!,;: ")
    # Short responses under 6 words that contain a filler phrase
    words = clean.split()
    if len(words) > 6:
        return False
    return any(phrase in clean for phrase in _FILLER_PHRASES)


# ---------------------------------------------------------------------------
# Capacity limits per plane
# ---------------------------------------------------------------------------

_PLANE_CAPS: dict[str, int] = {
    "working": MAX_WORKING_ENTRIES,
    "episodic": MAX_EPISODIC_ENTRIES,
    "continuity": MAX_CONTINUITY_ENTRIES,
}


class ConversationMemory:
    """Ties memory planes to the governed client lifecycle.

    One instance per ``GovernedClient``. Survives across turns within
    the same conversation; call ``new_conversation()`` or ``clear()``
    to reset.
    """

    def __init__(self, store: MemoryStore | None = None) -> None:
        self._store: MemoryStore = store or InMemoryStore()

    @property
    def store(self) -> MemoryStore:
        return self._store

    # ------------------------------------------------------------------
    # Write path (called after substrate)
    # ------------------------------------------------------------------

    def admit_and_store(
        self,
        *,
        memory_admission_decision: dict[str, Any],
        turn_id: str,
        conversation_id: str,
        question: str,
        answer_text: str,
    ) -> MemoryEntry | None:
        """Store a memory entry if the substrate admitted it.

        Returns the stored ``MemoryEntry``, or ``None`` if the write
        was rejected or there was no suggestion.
        """
        decision_class = memory_admission_decision.get("decision_class", "explicit_none")

        if decision_class != "admit_write":
            return None

        # Build the continuity entry
        now = MemoryEntry.now_iso()
        entry_id = MemoryEntry.make_entry_id("continuity", turn_id, question[:100])

        # Store only the user's input and the factual answer content.
        # Exclude filler responses (e.g. "Okay, I understand") that
        # can poison small models into echoing them.
        trimmed_answer = answer_text[:500].strip()
        answer_is_filler = _is_filler_response(trimmed_answer)

        if answer_is_filler:
            # The user's statement IS the fact; store it directly
            content = question[:500]
        else:
            content = f"{question[:200]} — {trimmed_answer}"

        entry = MemoryEntry(
            entry_id=entry_id,
            plane="continuity",
            key=question[:200],
            content=content,
            source_turn_id=turn_id,
            conversation_id=conversation_id,
            created_at=now,
        )

        # Handle supersession
        superseded_ref = memory_admission_decision.get("superseded_memory_ref_or_none")
        if superseded_ref:
            self._store.supersede(superseded_ref, entry_id)
            entry.metadata["supersedes"] = superseded_ref

        # Enforce capacity
        self._enforce_cap(conversation_id, "continuity")

        self._store.write(entry)
        return entry

    def store_episodic(
        self,
        *,
        turn_id: str,
        conversation_id: str,
        question: str,
        answer_text: str,
        answer_mode: str,
        governance_enabled: bool,
    ) -> MemoryEntry:
        """Always store an episodic record of the turn (no admission gate).

        Episodic entries are the raw turn log. They let the model
        know *what happened* in prior turns even if the continuity
        entry was rejected.
        """
        now = MemoryEntry.now_iso()
        entry_id = MemoryEntry.make_entry_id("episodic", turn_id, question[:100])

        # Same filler-detection as continuity
        trimmed_answer = answer_text[:300].strip()
        answer_is_filler = _is_filler_response(trimmed_answer)

        if answer_is_filler:
            content = f"Discussed: {question[:300]}"
        else:
            content = f"Asked: {question[:200]} — Answered: {trimmed_answer}"

        entry = MemoryEntry(
            entry_id=entry_id,
            plane="episodic",
            key=question[:200],
            content=content,
            source_turn_id=turn_id,
            conversation_id=conversation_id,
            created_at=now,
            metadata={
                "answer_mode": answer_mode,
                "governance_enabled": governance_enabled,
            },
        )

        self._enforce_cap(conversation_id, "episodic")
        self._store.write(entry)
        return entry

    # ------------------------------------------------------------------
    # Read path (called before pipeline)
    # ------------------------------------------------------------------

    def retrieve_context(
        self,
        conversation_id: str,
        *,
        exclude_turn_id: str | None = None,
        max_entries: int = 20,
    ) -> list[MemoryEntry]:
        """Retrieve continuity + episodic entries for this conversation.

        Returns entries sorted newest-first, excluding any from the
        current turn (to avoid self-reference). When both a continuity
        and episodic entry exist for the same source turn, only the
        continuity entry is returned (it's the more authoritative one).
        """
        continuity = self._store.query(
            conversation_id, plane="continuity", limit=max_entries,
        )
        episodic = self._store.query(
            conversation_id, plane="episodic", limit=max_entries,
        )

        # Merge: prefer continuity over episodic for the same source turn
        covered_turns: set[str] = set()
        merged: list[MemoryEntry] = []

        # First, add all continuity entries
        for entry in continuity:
            if exclude_turn_id and entry.source_turn_id == exclude_turn_id:
                continue
            covered_turns.add(entry.source_turn_id)
            merged.append(entry)

        # Then add episodic entries only for turns NOT already covered
        for entry in episodic:
            if exclude_turn_id and entry.source_turn_id == exclude_turn_id:
                continue
            if entry.source_turn_id in covered_turns:
                continue
            merged.append(entry)

        # Sort newest first, cap
        merged.sort(key=lambda e: e.created_at, reverse=True)
        return merged[:max_entries]

    def format_for_prompt(self, entries: list[MemoryEntry]) -> str:
        """Format memory entries for injection into the planner prompt.

        Groups by plane for clarity. Returns empty string if no entries.
        """
        if not entries:
            return ""

        continuity = [e for e in entries if e.plane == "continuity"]
        episodic = [e for e in entries if e.plane == "episodic"]

        parts: list[str] = []

        if continuity:
            items = "\n\n".join(
                f"[Established fact from earlier]\n{entry.content}"
                for entry in continuity
            )
            parts.append(items)

        if episodic:
            # Only include episodic entries NOT already covered by continuity
            continuity_turns = {e.source_turn_id for e in continuity}
            uncovered = [e for e in episodic if e.source_turn_id not in continuity_turns]
            if uncovered:
                items = "\n\n".join(
                    f"[Prior exchange]\n{entry.content}"
                    for entry in uncovered
                )
                parts.append(items)

        return "\n\n".join(parts)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def clear(self, conversation_id: str | None = None) -> None:
        """Clear memory. If conversation_id is given, clear only that conversation."""
        self._store.clear(conversation_id)

    def count(
        self,
        conversation_id: str | None = None,
        plane: str | None = None,
    ) -> int:
        return self._store.count(conversation_id, plane)

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _enforce_cap(self, conversation_id: str, plane: str) -> None:
        """Evict the oldest entry if the plane is at capacity (FIFO)."""
        cap = _PLANE_CAPS.get(plane, 256)
        entries = self._store.query(conversation_id, plane=plane, limit=cap + 1)
        if len(entries) >= cap:
            # entries is newest-first; evict the oldest
            oldest = entries[-1]
            self._store.supersede(oldest.entry_id, "evicted:capacity")


__all__ = ["ConversationMemory"]
