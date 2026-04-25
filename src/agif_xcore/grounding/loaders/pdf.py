"""PDF loader using pypdf (optional dependency).

If pypdf is not installed this module raises ``ImportError`` at import
time, which is caught by ``loaders/__init__.py`` — PDF loading simply
becomes unavailable until the user installs the grounding extras.
"""

from __future__ import annotations

from pathlib import Path

import pypdf  # type: ignore[import-untyped]  # optional dep


class PdfLoader:
    extensions = (".pdf",)

    def load(self, path: Path) -> str:
        reader = pypdf.PdfReader(str(path))
        pages: list[str] = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
        return "\n\n".join(pages)
