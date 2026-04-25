"""Grounding package — retrieval + document loading.

M2: BM25 (lexical) retriever over chunked documents.
M5: VectorRetriever (dense embedding) + HybridRetriever (RRF fusion).
"""

from .base import GroundingSource, Loader, Retriever
from .bm25 import BM25Retriever
from .noop import NoOpRetriever

# Vector retriever is behind optional imports
try:
    from .vector import HybridRetriever, VectorRetriever
except ImportError:
    HybridRetriever = None  # type: ignore[assignment, misc]
    VectorRetriever = None  # type: ignore[assignment, misc]

__all__ = [
    "BM25Retriever",
    "GroundingSource",
    "HybridRetriever",
    "Loader",
    "NoOpRetriever",
    "Retriever",
    "VectorRetriever",
]
