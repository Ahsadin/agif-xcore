"""Vector-embedding retriever using sentence-transformers.

Uses dense embeddings for semantic retrieval. Complements the BM25
retriever (which is lexical). Both implement the ``Retriever``
protocol and share the same chunking + ``GroundingSource`` types.

Optional dependencies (behind import-time checks):

  * ``sentence-transformers>=2.7`` — embedding model
  * ``numpy`` (transitive dep of sentence-transformers)

Ranking: cosine similarity via numpy. No faiss required for
corpora under ~10K chunks; optional ``faiss-cpu`` for larger
corpora is a future extension.

Default model: ``all-MiniLM-L6-v2`` (22MB, fast, good quality).
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Sequence

from ..schemas import GroundingBundle, GroundingChunk
from .base import GroundingSource
from .bm25 import chunk_text  # reuse the same chunking logic


# ---------------------------------------------------------------------------
# Import checks
# ---------------------------------------------------------------------------

_SENTENCE_TRANSFORMERS_AVAILABLE = False
_NUMPY_AVAILABLE = False

try:
    import numpy as np  # type: ignore[import-untyped]
    _NUMPY_AVAILABLE = True
except ImportError:
    np = None  # type: ignore[assignment]

try:
    from sentence_transformers import SentenceTransformer  # type: ignore[import-untyped]
    _SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SentenceTransformer = None  # type: ignore[assignment, misc]


def vector_deps_available() -> dict[str, bool]:
    """Check which optional vector dependencies are installed."""
    return {
        "sentence_transformers": _SENTENCE_TRANSFORMERS_AVAILABLE,
        "numpy": _NUMPY_AVAILABLE,
    }


# ---------------------------------------------------------------------------
# Cosine similarity (numpy, no faiss needed for small corpora)
# ---------------------------------------------------------------------------

def _cosine_similarity(query_vec: Any, corpus_vecs: Any) -> Any:
    """Cosine similarity between a query vector and corpus matrix.

    Both arguments are numpy arrays. Returns a 1-D array of scores.
    """
    # Normalize
    query_norm = query_vec / (np.linalg.norm(query_vec) + 1e-10)
    corpus_norms = corpus_vecs / (
        np.linalg.norm(corpus_vecs, axis=1, keepdims=True) + 1e-10
    )
    return corpus_norms @ query_norm


# ---------------------------------------------------------------------------
# VectorRetriever
# ---------------------------------------------------------------------------

DEFAULT_EMBEDDING_MODEL = "all-MiniLM-L6-v2"


class VectorRetriever:
    """Dense-embedding retriever over a pre-loaded corpus.

    Build once from a list of ``GroundingSource`` objects; call
    ``retrieve(query, k)`` many times. Same pattern as ``BM25Retriever``.

    Raises ``RuntimeError`` at construction time if
    ``sentence-transformers`` is not installed.
    """

    name = "vector"

    def __init__(
        self,
        sources: Sequence[GroundingSource],
        *,
        model_name: str = DEFAULT_EMBEDDING_MODEL,
        chunk_size: int = 900,
        chunk_overlap: int = 180,
        batch_size: int = 64,
    ) -> None:
        if not _SENTENCE_TRANSFORMERS_AVAILABLE:
            raise RuntimeError(
                "sentence-transformers is required for VectorRetriever. "
                "Install with: pip install agif-xcore[vector]"
            )
        if not _NUMPY_AVAILABLE:
            raise RuntimeError(
                "numpy is required for VectorRetriever. "
                "Install with: pip install numpy"
            )

        self._model_name = model_name
        self._model = SentenceTransformer(model_name)  # type: ignore[misc]

        # Chunk and index
        self._chunks: list[_VectorChunk] = []
        for source in sources:
            raw_chunks = chunk_text(source.text, chunk_size, chunk_overlap)
            for i, text in enumerate(raw_chunks):
                self._chunks.append(_VectorChunk(
                    ref=f"{source.ref}#chunk{i}",
                    source_path=source.source_path,
                    text=text,
                    loader=source.loader_name,
                ))

        # Embed all chunks
        if self._chunks:
            chunk_texts = [c.text for c in self._chunks]
            self._embeddings = self._model.encode(
                chunk_texts,
                batch_size=batch_size,
                show_progress_bar=False,
                normalize_embeddings=True,
            )
        else:
            self._embeddings = np.array([])  # type: ignore[union-attr]

    @property
    def chunk_count(self) -> int:
        return len(self._chunks)

    @property
    def embedding_dim(self) -> int:
        if self._embeddings is not None and len(self._embeddings) > 0:
            return int(self._embeddings.shape[1])
        return 0

    def retrieve(self, query: str, k: int = 5) -> GroundingBundle:
        """Embed the query and return the top-K most similar chunks."""
        started = time.perf_counter()

        if not query.strip() or not self._chunks:
            return GroundingBundle(
                chunks=[], retriever_name=self.name, retrieval_ms=0,
            )

        # Embed query
        query_vec = self._model.encode(
            [query],
            show_progress_bar=False,
            normalize_embeddings=True,
        )[0]

        # Score all chunks via cosine similarity
        scores = _cosine_similarity(query_vec, self._embeddings)

        # Top-K
        top_k_idx = scores.argsort()[-k:][::-1]
        elapsed_ms = int((time.perf_counter() - started) * 1000)

        result_chunks: list[GroundingChunk] = []
        for idx in top_k_idx:
            score = float(scores[idx])
            if score <= 0:
                continue
            chunk = self._chunks[idx]
            result_chunks.append(GroundingChunk(
                ref=chunk.ref,
                source_path=chunk.source_path,
                text=chunk.text,
                score=round(score, 4),
                loader=chunk.loader,
            ))

        return GroundingBundle(
            chunks=result_chunks,
            retriever_name=self.name,
            retrieval_ms=elapsed_ms,
        )


class _VectorChunk:
    """One chunk with metadata (no embedding stored — indices align)."""

    __slots__ = ("ref", "source_path", "text", "loader")

    def __init__(
        self, ref: str, source_path: str, text: str, loader: str,
    ) -> None:
        self.ref = ref
        self.source_path = source_path
        self.text = text
        self.loader = loader


# ---------------------------------------------------------------------------
# Hybrid retriever (BM25 + vector, reciprocal rank fusion)
# ---------------------------------------------------------------------------

class HybridRetriever:
    """Combines BM25 (lexical) and vector (semantic) retrieval.

    Uses reciprocal rank fusion (RRF) with a configurable ``k``
    constant (default 60, per the original RRF paper). Both
    retrievers share the same ``Retriever`` protocol.
    """

    name = "hybrid"

    def __init__(
        self,
        bm25_retriever: Any,
        vector_retriever: VectorRetriever,
        *,
        rrf_k: int = 60,
        fetch_k: int = 20,
    ) -> None:
        self._bm25 = bm25_retriever
        self._vector = vector_retriever
        self._rrf_k = rrf_k
        self._fetch_k = fetch_k

    def retrieve(self, query: str, k: int = 5) -> GroundingBundle:
        """Fuse BM25 and vector results via reciprocal rank fusion."""
        started = time.perf_counter()

        bm25_bundle = self._bm25.retrieve(query, k=self._fetch_k)
        vector_bundle = self._vector.retrieve(query, k=self._fetch_k)

        # RRF scoring: score(d) = sum(1 / (k + rank))
        scores: dict[str, float] = {}
        chunk_map: dict[str, GroundingChunk] = {}

        for rank, chunk in enumerate(bm25_bundle.chunks):
            rrf = 1.0 / (self._rrf_k + rank + 1)
            scores[chunk.ref] = scores.get(chunk.ref, 0.0) + rrf
            chunk_map[chunk.ref] = chunk

        for rank, chunk in enumerate(vector_bundle.chunks):
            rrf = 1.0 / (self._rrf_k + rank + 1)
            scores[chunk.ref] = scores.get(chunk.ref, 0.0) + rrf
            if chunk.ref not in chunk_map:
                chunk_map[chunk.ref] = chunk

        # Sort by fused score, take top-K
        ranked = sorted(scores.items(), key=lambda x: -x[1])[:k]
        elapsed_ms = int((time.perf_counter() - started) * 1000)

        result_chunks: list[GroundingChunk] = []
        for ref, fused_score in ranked:
            original = chunk_map[ref]
            result_chunks.append(GroundingChunk(
                ref=original.ref,
                source_path=original.source_path,
                text=original.text,
                score=round(fused_score, 4),
                loader=original.loader,
            ))

        return GroundingBundle(
            chunks=result_chunks,
            retriever_name=self.name,
            retrieval_ms=elapsed_ms,
        )


# ---------------------------------------------------------------------------
# Convenience builder
# ---------------------------------------------------------------------------

def build_vector_from_paths(
    paths: Sequence[str | Path],
    *,
    model_name: str = DEFAULT_EMBEDDING_MODEL,
    chunk_size: int = 900,
    chunk_overlap: int = 180,
) -> VectorRetriever:
    """Load files and build a ``VectorRetriever`` in one call."""
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
    return VectorRetriever(
        sources,
        model_name=model_name,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )


__all__ = [
    "DEFAULT_EMBEDDING_MODEL",
    "HybridRetriever",
    "VectorRetriever",
    "build_vector_from_paths",
    "vector_deps_available",
]
