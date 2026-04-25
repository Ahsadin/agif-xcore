"""Memory plane types and store protocol.

Ported from AGIFCore Phase 4 memory planes. The original has 5 planes
(working, episodic, semantic, procedural, continuity) with review-gated
promotion, compression, and forgetting. XCore adapts this into a
simpler model focused on:

  * **Working** — current-turn scratch space, cleared each turn.
  * **Episodic** — turn summaries (question + answer), persisted.
  * **Continuity** — key facts established in the conversation,
    persisted across turns for cross-turn reference.

All planes are bounded. All writes go through the substrate's
``memory_admission`` gate before reaching the store.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Protocol


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MEMORY_PLANES: tuple[str, ...] = ("working", "episodic", "continuity")

# Capacity bounds (from AGIFCore: working=64, episodic=512, continuity=256)
MAX_WORKING_ENTRIES = 64
MAX_EPISODIC_ENTRIES = 512
MAX_CONTINUITY_ENTRIES = 256


# ---------------------------------------------------------------------------
# MemoryEntry
# ---------------------------------------------------------------------------

@dataclass
class MemoryEntry:
    """One item stored in a memory plane.

    Immutable once the substrate admits it. Supersession creates a new
    entry; the old one gets ``superseded_by`` set.
    """

    entry_id: str
    plane: str
    key: str
    content: str
    source_turn_id: str
    conversation_id: str
    created_at: str
    superseded_by: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @staticmethod
    def make_entry_id(plane: str, turn_id: str, key: str) -> str:
        """Deterministic entry id from (plane, turn_id, key)."""
        seed = f"{plane}|{turn_id}|{key}"
        digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16]
        return f"mem:{plane}:{digest}"

    @staticmethod
    def now_iso() -> str:
        return (
            datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )


# ---------------------------------------------------------------------------
# MemoryStore protocol
# ---------------------------------------------------------------------------

class MemoryStore(Protocol):
    """Backend-agnostic memory storage.

    Default is in-memory (dict-backed). ``sqlite`` and ``redis``
    backends land later. The protocol is intentionally minimal.
    """

    def write(self, entry: MemoryEntry) -> None:
        """Persist an entry. Overwrites if entry_id already exists."""
        ...

    def read(self, entry_id: str) -> MemoryEntry | None:
        """Return an entry by id, or None."""
        ...

    def query(
        self,
        conversation_id: str,
        *,
        plane: str | None = None,
        limit: int = 100,
    ) -> list[MemoryEntry]:
        """Return entries matching the filters, newest first.

        Only returns non-superseded entries by default.
        """
        ...

    def supersede(self, old_entry_id: str, new_entry_id: str) -> None:
        """Mark ``old_entry_id`` as superseded by ``new_entry_id``."""
        ...

    def clear(self, conversation_id: str | None = None) -> None:
        """Clear entries. If conversation_id is None, clear all."""
        ...

    def count(self, conversation_id: str | None = None, plane: str | None = None) -> int:
        """Count entries matching the filters."""
        ...


# ---------------------------------------------------------------------------
# InMemoryStore
# ---------------------------------------------------------------------------

class InMemoryStore:
    """Dict-backed, single-process memory store. Default for M4."""

    def __init__(self) -> None:
        self._entries: dict[str, MemoryEntry] = {}

    def write(self, entry: MemoryEntry) -> None:
        if entry.plane not in MEMORY_PLANES:
            raise ValueError(f"unknown plane '{entry.plane}', must be one of {MEMORY_PLANES}")
        self._entries[entry.entry_id] = entry

    def read(self, entry_id: str) -> MemoryEntry | None:
        return self._entries.get(entry_id)

    def query(
        self,
        conversation_id: str,
        *,
        plane: str | None = None,
        limit: int = 100,
    ) -> list[MemoryEntry]:
        results = []
        for entry in self._entries.values():
            if entry.conversation_id != conversation_id:
                continue
            if entry.superseded_by is not None:
                continue
            if plane is not None and entry.plane != plane:
                continue
            results.append(entry)
        # newest first
        results.sort(key=lambda e: e.created_at, reverse=True)
        return results[:limit]

    def supersede(self, old_entry_id: str, new_entry_id: str) -> None:
        old = self._entries.get(old_entry_id)
        if old is not None:
            old.superseded_by = new_entry_id

    def clear(self, conversation_id: str | None = None) -> None:
        if conversation_id is None:
            self._entries.clear()
        else:
            to_remove = [
                eid for eid, entry in self._entries.items()
                if entry.conversation_id == conversation_id
            ]
            for eid in to_remove:
                del self._entries[eid]

    def count(self, conversation_id: str | None = None, plane: str | None = None) -> int:
        total = 0
        for entry in self._entries.values():
            if conversation_id is not None and entry.conversation_id != conversation_id:
                continue
            if plane is not None and entry.plane != plane:
                continue
            if entry.superseded_by is not None:
                continue
            total += 1
        return total


__all__ = [
    "MEMORY_PLANES",
    "MAX_WORKING_ENTRIES",
    "MAX_EPISODIC_ENTRIES",
    "MAX_CONTINUITY_ENTRIES",
    "MemoryEntry",
    "MemoryStore",
    "InMemoryStore",
]
