"""Plain-text file loader."""

from __future__ import annotations

from pathlib import Path


class TextLoader:
    extensions = (".txt", ".md", ".csv", ".json", ".yaml", ".yml", ".log", ".xml", ".html")

    def load(self, path: Path) -> str:
        return path.read_text(encoding="utf-8", errors="replace")
