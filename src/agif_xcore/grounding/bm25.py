"""BM25-style word-overlap retriever.

Ported from X1 ``upload_grounding_store.py`` (626 LOC). Keeps the core
idea: chunk loaded documents with overlap, score each chunk against the
query by token presence weighted by inverse document frequency, return
top-K.

Changes from X1:
- Removed macOS-only ``/usr/bin/textutil`` shellout; uses ``Loader``
  plugin interface instead.
- Removed X1 session/upload management; this is a pure retriever.
- Simplified to stdlib (``collections.Counter``) — no ``rank-bm25``
  dep needed for the basic approach.
"""

from __future__ import annotations

import math
import time
from collections import Counter
from pathlib import Path
from typing import Sequence

from ..schemas import GroundingBundle, GroundingChunk
from .base import GroundingSource


# ---------------------------------------------------------------------------
# Stopwords (light set; enough to avoid scoring noise)
# ---------------------------------------------------------------------------

_STOPWORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "been", "but", "by",
    "can", "do", "for", "from", "had", "has", "have", "he", "her",
    "him", "his", "how", "i", "if", "in", "into", "is", "it", "its",
    "may", "me", "my", "no", "not", "of", "on", "or", "our", "out",
    "own", "she", "so", "some", "than", "that", "the", "them", "then",
    "there", "these", "they", "this", "to", "up", "us", "was", "we",
    "were", "what", "when", "which", "who", "why", "will", "with",
    "you", "your",
})


def _tokenize(text: str) -> list[str]:
    """Lowercase, split on non-alnum, drop stopwords and short tokens."""
    tokens: list[str] = []
    for word in text.lower().split():
        cleaned = "".join(c for c in word if c.isalnum())
        if len(cleaned) >= 2 and cleaned not in _STOPWORDS:
            tokens.append(cleaned)
    return tokens


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

def chunk_text(
    text: str,
    chunk_size: int = 900,
    overlap: int = 180,
) -> list[str]:
    """Split text into overlapping chunks."""
    if not text:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end].strip())
        start += chunk_size - overlap
    return [c for c in chunks if c]


# ---------------------------------------------------------------------------
# BM25 retriever
# ---------------------------------------------------------------------------

class BM25Retriever:
    """Stateful retriever over a pre-loaded set of grounding sources.

    Build once from a list of ``GroundingSource`` objects (loaded via
    the ``Loader`` interface); call ``retrieve(query, k)`` many times.
    """

    name = "bm25"

    def __init__(
        self,
        sources: Sequence[GroundingSource],
        chunk_size: int = 900,
        chunk_overlap: int = 180,
    ) -> None:
        self._chunks: list[_IndexedChunk] = []
        self._doc_count = 0
        self._avg_dl = 0.0
        self._df: Counter[str] = Counter()

        all_chunks: list[_IndexedChunk] = []
        for source in sources:
            raw_chunks = chunk_text(source.text, chunk_size, chunk_overlap)
            for i, text in enumerate(raw_chunks):
                tokens = _tokenize(text)
                ic = _IndexedChunk(
                    ref=f"{source.ref}#chunk{i}",
                    source_path=source.source_path,
                    text=text,
                    loader=source.loader_name,
                    tokens=tokens,
                    token_counts=Counter(tokens),
                )
                all_chunks.append(ic)
                self._df.update(set(tokens))

        self._chunks = all_chunks
        self._doc_count = len(all_chunks)
        total_tokens = sum(len(c.tokens) for c in all_chunks)
        self._avg_dl = total_tokens / max(self._doc_count, 1)

    @property
    def chunk_count(self) -> int:
        return len(self._chunks)

    def retrieve(self, query: str, k: int = 5) -> GroundingBundle:
        started = time.perf_counter()
        query_tokens = _tokenize(query)
        if not query_tokens or not self._chunks:
            return GroundingBundle(
                chunks=[],
                retriever_name=self.name,
                retrieval_ms=0,
            )

        scored: list[tuple[float, _IndexedChunk]] = []
        for chunk in self._chunks:
            score = self._bm25_score(query_tokens, chunk)
            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda x: -x[0])
        top = scored[:k]
        elapsed_ms = int((time.perf_counter() - started) * 1000)

        result_chunks = [
            GroundingChunk(
                ref=chunk.ref,
                source_path=chunk.source_path,
                text=chunk.text,
                score=round(score, 4),
                loader=chunk.loader,
            )
            for score, chunk in top
        ]
        return GroundingBundle(
            chunks=result_chunks,
            retriever_name=self.name,
            retrieval_ms=elapsed_ms,
        )

    def _bm25_score(
        self,
        query_tokens: list[str],
        chunk: "_IndexedChunk",
        k1: float = 1.5,
        b: float = 0.75,
    ) -> float:
        dl = len(chunk.tokens)
        score = 0.0
        for qt in query_tokens:
            tf = chunk.token_counts.get(qt, 0)
            if tf == 0:
                continue
            df = self._df.get(qt, 0)
            idf = math.log((self._doc_count - df + 0.5) / (df + 0.5) + 1)
            numerator = tf * (k1 + 1)
            denominator = tf + k1 * (1 - b + b * (dl / max(self._avg_dl, 1)))
            score += idf * (numerator / denominator)
        return score


class _IndexedChunk:
    __slots__ = ("ref", "source_path", "text", "loader", "tokens", "token_counts")

    def __init__(
        self,
        ref: str,
        source_path: str,
        text: str,
        loader: str,
        tokens: list[str],
        token_counts: Counter,
    ) -> None:
        self.ref = ref
        self.source_path = source_path
        self.text = text
        self.loader = loader
        self.tokens = tokens
        self.token_counts = token_counts


# ---------------------------------------------------------------------------
# Convenience: load files and build a retriever in one call
# ---------------------------------------------------------------------------

def build_bm25_from_paths(
    paths: Sequence[str | Path],
    chunk_size: int = 900,
    chunk_overlap: int = 180,
) -> BM25Retriever:
    """Load files using the appropriate ``Loader`` and return a ``BM25Retriever``."""
    from .loaders import load_file

    sources: list[GroundingSource] = []
    for raw_path in paths:
        p = Path(raw_path)
        text, loader_name = load_file(p)
        sources.append(GroundingSource(
            ref=p.name,
            source_path=str(p),
            text=text,
            loader_name=loader_name,
        ))
    return BM25Retriever(sources, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
