"""Shared helpers for substrate modules.

X1 duplicated ``_unique_list`` in 4 files. We extract it once here.
"""

from __future__ import annotations


def unique_list(values: list[str] | None) -> list[str]:
    """De-duplicate while preserving insertion order."""
    if not values:
        return []
    seen: dict[str, None] = {}
    for v in values:
        seen[str(v)] = None
    return list(seen.keys())
