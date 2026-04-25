"""Cross-turn conversation memory (M4).

Ported from AGIFCore Phase 4 memory planes. Three planes:

  * **working** — current-turn scratch, cleared per turn.
  * **episodic** — one entry per turn recording the Q+A.
  * **continuity** — key facts persisted for cross-turn reference.

All writes go through the substrate's ``memory_admission`` gate.
"""

from __future__ import annotations

from .base import (
    MAX_CONTINUITY_ENTRIES,
    MAX_EPISODIC_ENTRIES,
    MAX_WORKING_ENTRIES,
    MEMORY_PLANES,
    InMemoryStore,
    MemoryEntry,
    MemoryStore,
)
from .store import ConversationMemory

__all__ = [
    "ConversationMemory",
    "InMemoryStore",
    "MAX_CONTINUITY_ENTRIES",
    "MAX_EPISODIC_ENTRIES",
    "MAX_WORKING_ENTRIES",
    "MEMORY_PLANES",
    "MemoryEntry",
    "MemoryStore",
]
