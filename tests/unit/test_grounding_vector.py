"""Tests for the vector retriever and hybrid retriever.

Tests cover two modes:

  1. **With sentence-transformers** — full vector retrieval tests run
     if the library is installed. Tests verify embedding, cosine
     similarity ranking, chunk count, and grounding bundle shape.

  2. **Without sentence-transformers** — tests verify graceful
     degradation (RuntimeError with a helpful message).

The hybrid retriever (BM25 + vector RRF fusion) is tested with
a mock vector retriever to avoid the sentence-transformers dep.
"""

from __future__ import annotations

import unittest
from collections import Counter

from agif_xcore.grounding.base import GroundingSource
from agif_xcore.grounding.bm25 import BM25Retriever
from agif_xcore.schemas import GroundingBundle, GroundingChunk


# Check if vector deps are available
try:
    from agif_xcore.grounding.vector import (
        HybridRetriever,
        VectorRetriever,
        vector_deps_available,
        _cosine_similarity,
    )
    _VECTOR_AVAILABLE = vector_deps_available()["sentence_transformers"]
except ImportError:
    _VECTOR_AVAILABLE = False


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

_TEST_SOURCES = [
    GroundingSource(
        ref="backup_policy.txt",
        source_path="/docs/backup_policy.txt",
        text=(
            "Our backup cadence is daily incremental with weekly full backups. "
            "Retention period is 90 days for all backup types. "
            "All backups must be encrypted using AES-256 before storage. "
            "Recovery tests are performed quarterly."
        ),
        loader_name="text",
    ),
    GroundingSource(
        ref="access_control.txt",
        source_path="/docs/access_control.txt",
        text=(
            "Multi-factor authentication is required for all privileged accounts. "
            "Password minimum length is 14 characters. "
            "Privilege reviews are conducted semi-annually. "
            "Service accounts must use certificate-based authentication."
        ),
        loader_name="text",
    ),
    GroundingSource(
        ref="incident_response.txt",
        source_path="/docs/incident_response.txt",
        text=(
            "Security incidents must be reported within 1 hour of detection. "
            "The incident response team is activated for severity 1 and 2 events. "
            "Post-incident review must be completed within 5 business days. "
            "All incident evidence must be preserved for 12 months."
        ),
        loader_name="text",
    ),
]


# ---------------------------------------------------------------------------
# Vector retriever tests (require sentence-transformers)
# ---------------------------------------------------------------------------

@unittest.skipUnless(_VECTOR_AVAILABLE, "sentence-transformers not installed")
class VectorRetrieverTests(unittest.TestCase):
    """Full vector retriever tests with real embeddings."""

    @classmethod
    def setUpClass(cls) -> None:
        """Build the retriever once (model loading is expensive)."""
        cls.retriever = VectorRetriever(_TEST_SOURCES, chunk_size=500, chunk_overlap=50)

    def test_chunk_count(self) -> None:
        self.assertGreater(self.retriever.chunk_count, 0)

    def test_embedding_dim(self) -> None:
        self.assertGreater(self.retriever.embedding_dim, 0)

    def test_retrieve_returns_grounding_bundle(self) -> None:
        bundle = self.retriever.retrieve("backup cadence", k=3)
        self.assertIsInstance(bundle, GroundingBundle)
        self.assertEqual(bundle.retriever_name, "vector")
        self.assertGreater(len(bundle.chunks), 0)

    def test_backup_query_ranks_backup_first(self) -> None:
        bundle = self.retriever.retrieve("What is the backup cadence?", k=3)
        top_chunk = bundle.chunks[0]
        self.assertIn("backup", top_chunk.text.lower())

    def test_auth_query_ranks_access_control_first(self) -> None:
        bundle = self.retriever.retrieve("multi-factor authentication requirements", k=3)
        top_chunk = bundle.chunks[0]
        self.assertIn("authentication", top_chunk.text.lower())

    def test_scores_are_descending(self) -> None:
        bundle = self.retriever.retrieve("incident response procedure", k=3)
        scores = [chunk.score for chunk in bundle.chunks]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_empty_query_returns_empty(self) -> None:
        bundle = self.retriever.retrieve("", k=3)
        self.assertEqual(len(bundle.chunks), 0)

    def test_chunks_have_refs(self) -> None:
        bundle = self.retriever.retrieve("password policy", k=2)
        for chunk in bundle.chunks:
            self.assertTrue(chunk.ref)
            self.assertIn("#chunk", chunk.ref)


@unittest.skipUnless(_VECTOR_AVAILABLE, "sentence-transformers not installed")
class CosineSimTests(unittest.TestCase):
    """Test the cosine similarity function directly."""

    def test_identical_vectors(self) -> None:
        import numpy as np
        v = np.array([1.0, 0.0, 0.0])
        corpus = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
        scores = _cosine_similarity(v, corpus)
        self.assertAlmostEqual(float(scores[0]), 1.0, places=5)
        self.assertAlmostEqual(float(scores[1]), 0.0, places=5)

    def test_orthogonal_vectors(self) -> None:
        import numpy as np
        v = np.array([1.0, 0.0])
        corpus = np.array([[0.0, 1.0]])
        scores = _cosine_similarity(v, corpus)
        self.assertAlmostEqual(float(scores[0]), 0.0, places=5)


# ---------------------------------------------------------------------------
# Graceful degradation tests (run even without sentence-transformers)
# ---------------------------------------------------------------------------

class VectorDepsTests(unittest.TestCase):
    """Test dependency detection."""

    def test_vector_deps_reports_correctly(self) -> None:
        from agif_xcore.grounding.vector import vector_deps_available
        result = vector_deps_available()
        self.assertIn("sentence_transformers", result)
        self.assertIn("numpy", result)
        self.assertIsInstance(result["sentence_transformers"], bool)
        self.assertIsInstance(result["numpy"], bool)


class VectorRetrieverNoDepsTests(unittest.TestCase):
    """Test that VectorRetriever fails clearly without deps."""

    @unittest.skipIf(_VECTOR_AVAILABLE, "deps are installed")
    def test_raises_without_deps(self) -> None:
        from agif_xcore.grounding.vector import VectorRetriever
        with self.assertRaises(RuntimeError) as ctx:
            VectorRetriever(_TEST_SOURCES)
        self.assertIn("sentence-transformers", str(ctx.exception))


# ---------------------------------------------------------------------------
# Hybrid retriever tests (mock vector, real BM25)
# ---------------------------------------------------------------------------

class _MockVectorRetriever:
    """Stub that returns pre-defined chunks for hybrid tests."""

    name = "mock_vector"

    def __init__(self, chunks: list[GroundingChunk]) -> None:
        self._chunks = chunks

    def retrieve(self, query: str, k: int = 5) -> GroundingBundle:
        return GroundingBundle(
            chunks=self._chunks[:k],
            retriever_name=self.name,
            retrieval_ms=1,
        )


class HybridRetrieverTests(unittest.TestCase):
    """Test RRF fusion of BM25 + vector results."""

    def setUp(self) -> None:
        self.bm25 = BM25Retriever(_TEST_SOURCES, chunk_size=500, chunk_overlap=50)

        # Create mock vector results with a different ranking
        self.mock_vector = _MockVectorRetriever([
            GroundingChunk(
                ref="incident_response.txt#chunk0",
                source_path="/docs/incident_response.txt",
                text="Security incidents must be reported within 1 hour.",
                score=0.95,
                loader="text",
            ),
            GroundingChunk(
                ref="backup_policy.txt#chunk0",
                source_path="/docs/backup_policy.txt",
                text="Our backup cadence is daily incremental.",
                score=0.82,
                loader="text",
            ),
        ])

    def test_hybrid_returns_grounding_bundle(self) -> None:
        from agif_xcore.grounding.vector import HybridRetriever
        hybrid = HybridRetriever(self.bm25, self.mock_vector)
        bundle = hybrid.retrieve("backup incident", k=3)
        self.assertIsInstance(bundle, GroundingBundle)
        self.assertEqual(bundle.retriever_name, "hybrid")
        self.assertGreater(len(bundle.chunks), 0)

    def test_hybrid_fuses_results(self) -> None:
        """Chunks appearing in both retrievers should score higher."""
        from agif_xcore.grounding.vector import HybridRetriever
        hybrid = HybridRetriever(self.bm25, self.mock_vector)
        bundle = hybrid.retrieve("backup", k=5)
        # backup_policy should appear since both retrievers have it
        refs = [c.ref for c in bundle.chunks]
        backup_refs = [r for r in refs if "backup" in r]
        self.assertGreater(len(backup_refs), 0)

    def test_hybrid_scores_are_descending(self) -> None:
        from agif_xcore.grounding.vector import HybridRetriever
        hybrid = HybridRetriever(self.bm25, self.mock_vector)
        bundle = hybrid.retrieve("incident response", k=5)
        scores = [chunk.score for chunk in bundle.chunks]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_hybrid_empty_query(self) -> None:
        from agif_xcore.grounding.vector import HybridRetriever
        hybrid = HybridRetriever(self.bm25, self.mock_vector)
        bundle = hybrid.retrieve("", k=3)
        # BM25 returns nothing for empty query; mock has pre-set results
        # So hybrid should still have some results from the mock
        self.assertIsInstance(bundle, GroundingBundle)


if __name__ == "__main__":
    unittest.main()
