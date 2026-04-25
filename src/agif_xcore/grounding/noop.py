"""No-op retriever — returns an empty bundle. Used when no grounding is configured."""

from __future__ import annotations

from ..schemas import GroundingBundle


class NoOpRetriever:
    name = "noop"

    def retrieve(self, query: str, k: int = 5) -> GroundingBundle:
        return GroundingBundle(chunks=[], retriever_name=self.name, retrieval_ms=0)
