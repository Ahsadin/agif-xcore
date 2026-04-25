"""DOCX loader using python-docx (optional dependency).

If python-docx is not installed this module raises ``ImportError`` at
import time, which is caught by ``loaders/__init__.py``.
"""

from __future__ import annotations

from pathlib import Path

import docx  # type: ignore[import-untyped]  # optional dep


class DocxLoader:
    extensions = (".docx",)

    def load(self, path: Path) -> str:
        document = docx.Document(str(path))
        paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)
