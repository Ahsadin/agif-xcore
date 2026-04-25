"""Tests for the RAG evaluation scoring functions.

Covers precision@K, recall@K, MRR, eval set loading, and
aggregate metric computation.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from benchmarks.rag_eval_runner import (
    EvalQuestion,
    EvalResult,
    RAGMetrics,
    _compute_rag_metrics,
    load_eval_set,
    precision_at_k,
    recall_at_k,
    reciprocal_rank,
)


class PrecisionAtKTests(unittest.TestCase):
    """Test precision@K scoring."""

    def test_all_relevant(self) -> None:
        self.assertAlmostEqual(precision_at_k(["a", "b"], {"a", "b"}), 1.0)

    def test_none_relevant(self) -> None:
        self.assertAlmostEqual(precision_at_k(["a", "b"], {"c", "d"}), 0.0)

    def test_half_relevant(self) -> None:
        self.assertAlmostEqual(precision_at_k(["a", "b", "c", "d"], {"a", "c"}), 0.5)

    def test_empty_retrieved(self) -> None:
        self.assertAlmostEqual(precision_at_k([], {"a", "b"}), 0.0)


class RecallAtKTests(unittest.TestCase):
    """Test recall@K scoring."""

    def test_all_recalled(self) -> None:
        self.assertAlmostEqual(recall_at_k(["a", "b"], {"a", "b"}), 1.0)

    def test_none_recalled(self) -> None:
        self.assertAlmostEqual(recall_at_k(["c", "d"], {"a", "b"}), 0.0)

    def test_half_recalled(self) -> None:
        self.assertAlmostEqual(recall_at_k(["a", "c"], {"a", "b"}), 0.5)

    def test_empty_relevant(self) -> None:
        # Nothing to recall = perfect by convention
        self.assertAlmostEqual(recall_at_k(["a"], set()), 1.0)


class ReciprocalRankTests(unittest.TestCase):
    """Test MRR scoring."""

    def test_first_position(self) -> None:
        self.assertAlmostEqual(reciprocal_rank(["a", "b", "c"], {"a"}), 1.0)

    def test_second_position(self) -> None:
        self.assertAlmostEqual(reciprocal_rank(["x", "a", "c"], {"a"}), 0.5)

    def test_third_position(self) -> None:
        self.assertAlmostEqual(reciprocal_rank(["x", "y", "a"], {"a"}), 1.0 / 3.0)

    def test_not_found(self) -> None:
        self.assertAlmostEqual(reciprocal_rank(["x", "y", "z"], {"a"}), 0.0)

    def test_empty_retrieved(self) -> None:
        self.assertAlmostEqual(reciprocal_rank([], {"a"}), 0.0)


class LoadEvalSetTests(unittest.TestCase):
    """Test eval set JSON loading."""

    def test_load_valid(self) -> None:
        data = [
            {
                "question": "What is BM25?",
                "relevant_refs": ["doc1.txt"],
                "category": "ir",
            },
            {
                "question": "What is TF-IDF?",
                "relevant_refs": ["doc2.txt", "doc3.txt"],
            },
        ]
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(data, f)
            path = f.name

        questions = load_eval_set(Path(path))
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0].question, "What is BM25?")
        self.assertEqual(questions[0].relevant_refs, ["doc1.txt"])
        self.assertEqual(questions[0].category, "ir")
        # Default category
        self.assertEqual(questions[1].category, "")

        Path(path).unlink()


class ComputeRAGMetricsTests(unittest.TestCase):
    """Test aggregate RAG metric computation."""

    def test_basic_aggregation(self) -> None:
        results = [
            EvalResult(
                question="Q1", category="C",
                relevant_refs=["a"], retrieved_refs=["a", "b"],
                precision_at_k=0.5, recall_at_k=1.0,
                reciprocal_rank=1.0, retrieval_ms=10,
            ),
            EvalResult(
                question="Q2", category="C",
                relevant_refs=["x"], retrieved_refs=["y", "z"],
                precision_at_k=0.0, recall_at_k=0.0,
                reciprocal_rank=0.0, retrieval_ms=20,
            ),
        ]
        m = _compute_rag_metrics("bm25", results, k=5)
        self.assertEqual(m.total_questions, 2)
        self.assertAlmostEqual(m.mean_precision_at_k, 0.25)
        self.assertAlmostEqual(m.mean_recall_at_k, 0.5)
        self.assertAlmostEqual(m.mean_reciprocal_rank, 0.5)
        self.assertAlmostEqual(m.avg_retrieval_ms, 15.0)

    def test_empty_results(self) -> None:
        m = _compute_rag_metrics("bm25", [], k=5)
        self.assertEqual(m.total_questions, 0)
        self.assertAlmostEqual(m.mean_precision_at_k, 0.0)

    def test_summary_dict(self) -> None:
        m = RAGMetrics(
            retriever_name="bm25",
            total_questions=5,
            k=3,
            mean_precision_at_k=0.8,
            mean_recall_at_k=0.9,
            mean_reciprocal_rank=0.75,
            total_retrieval_ms=100,
        )
        d = m.summary_dict()
        self.assertEqual(d["retriever"], "bm25")
        self.assertEqual(d["k"], 3)
        self.assertAlmostEqual(d["mean_precision_at_k"], 0.8)
        self.assertAlmostEqual(d["avg_retrieval_ms"], 20.0)


if __name__ == "__main__":
    unittest.main()
