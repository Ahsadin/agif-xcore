"""Base types for grounding (retrieval + loading)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from ..schemas import GroundingBundle, GroundingChunk


class Loader(Protocol):
    """Extracts plain text from a file. Implementations live in ``loaders/``."""
    extensions: tuple[str, ...]
    def load(self, path: Path) -> str: ...


class Retriever(Protocol):
    """Scores query against a pre-indexed corpus and returns top-K chunks."""
    name: str
    def retrieve(self, query: str, k: int = 5) -> GroundingBundle: ...


@dataclass
class GroundingSource:
    """One loaded document ready for retrieval."""
    ref: str
    source_path: str
    text: str
    loader_name: str
