"""Document loaders — extract plain text from files.

M2 ships text and basic PDF/DOCX extraction using stdlib only. When
the optional ``grounding`` extras are installed (pypdf, python-docx),
the richer implementations activate automatically.
"""

from __future__ import annotations

from pathlib import Path

from .text import TextLoader

_LOADERS_BY_EXT: dict[str, type] = {}


def _register_defaults() -> None:
    """Register known loaders. PDF/DOCX use best-effort: stdlib fallback
    if the rich library is missing."""
    for ext in TextLoader.extensions:
        _LOADERS_BY_EXT[ext] = TextLoader

    # PDF: try pypdf, fall back to stub
    try:
        from .pdf import PdfLoader
        for ext in PdfLoader.extensions:
            _LOADERS_BY_EXT[ext] = PdfLoader
    except ImportError:
        pass

    # DOCX: try python-docx, fall back to stub
    try:
        from .docx import DocxLoader
        for ext in DocxLoader.extensions:
            _LOADERS_BY_EXT[ext] = DocxLoader
    except ImportError:
        pass


_register_defaults()


def load_file(path: Path) -> tuple[str, str]:
    """Load a file and return ``(text, loader_name)``.

    Falls back to plain-text loading for unrecognised extensions.
    """
    ext = path.suffix.lower()
    loader_cls = _LOADERS_BY_EXT.get(ext, TextLoader)
    loader = loader_cls()
    text = loader.load(path)
    return text, type(loader).__name__


def supported_extensions() -> list[str]:
    return sorted(_LOADERS_BY_EXT.keys())
