"""Tests for BM25 retriever and text chunking."""

from __future__ import annotations

import unittest

from agif_xcore.grounding.base import GroundingSource
from agif_xcore.grounding.bm25 import BM25Retriever, chunk_text


class ChunkTextTests(unittest.TestCase):
    def test_empty_string_returns_empty(self) -> None:
        self.assertEqual(chunk_text(""), [])

    def test_short_string_returns_one_chunk(self) -> None:
        result = chunk_text("Hello world", chunk_size=100, overlap=20)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Hello world")

    def test_overlap_produces_more_chunks(self) -> None:
        text = "a" * 200
        no_overlap = chunk_text(text, chunk_size=100, overlap=0)
        with_overlap = chunk_text(text, chunk_size=100, overlap=50)
        self.assertGreater(len(with_overlap), len(no_overlap))


class BM25RetrieverTests(unittest.TestCase):
    def _sources(self) -> list[GroundingSource]:
        return [
            GroundingSource(
                ref="sop.txt",
                source_path="/tmp/sop.txt",
                text=(
                    "The backup cadence for production systems is daily "
                    "incremental with weekly full backup. Retention is "
                    "90 days for incremental and 365 days for full."
                ),
                loader_name="TextLoader",
            ),
            GroundingSource(
                ref="policy.txt",
                source_path="/tmp/policy.txt",
                text=(
                    "Employees must not share credentials. Access to "
                    "production systems requires MFA. Password rotation "
                    "is required every 90 days."
                ),
                loader_name="TextLoader",
            ),
            GroundingSource(
                ref="faq.txt",
                source_path="/tmp/faq.txt",
                text=(
                    "Q: What is BM25? A: BM25 is a ranking function "
                    "used by search engines to estimate the relevance "
                    "of documents to a given search query."
                ),
                loader_name="TextLoader",
            ),
        ]

    def test_retrieves_relevant_chunk(self) -> None:
        retriever = BM25Retriever(self._sources(), chunk_size=500, chunk_overlap=0)
        bundle = retriever.retrieve("what is the backup cadence", k=2)
        self.assertGreater(len(bundle.chunks), 0)
        # The backup SOP should rank highest
        self.assertIn("sop.txt", bundle.chunks[0].ref)

    def test_bm25_query_returns_bm25_ref(self) -> None:
        retriever = BM25Retriever(self._sources(), chunk_size=500, chunk_overlap=0)
        bundle = retriever.retrieve("what is BM25 retrieval ranking", k=2)
        self.assertGreater(len(bundle.chunks), 0)
        self.assertIn("faq.txt", bundle.chunks[0].ref)

    def test_empty_query_returns_empty_bundle(self) -> None:
        retriever = BM25Retriever(self._sources())
        bundle = retriever.retrieve("", k=5)
        self.assertEqual(len(bundle.chunks), 0)

    def test_no_sources_returns_empty(self) -> None:
        retriever = BM25Retriever([], chunk_size=500, chunk_overlap=0)
        bundle = retriever.retrieve("anything", k=5)
        self.assertEqual(len(bundle.chunks), 0)

    def test_chunk_count_matches_expected(self) -> None:
        retriever = BM25Retriever(self._sources(), chunk_size=500, chunk_overlap=0)
        self.assertEqual(retriever.chunk_count, 3)  # each source fits in one chunk

    def test_retrieval_ms_is_non_negative(self) -> None:
        retriever = BM25Retriever(self._sources())
        bundle = retriever.retrieve("backup", k=2)
        self.assertGreaterEqual(bundle.retrieval_ms, 0)


if __name__ == "__main__":
    unittest.main()
