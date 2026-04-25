"""Build and hash ``TraceEnvelope`` objects."""

from __future__ import annotations

import hashlib

from ..schemas import (
    GroundingBundle,
    ProposalEnvelope,
    SubstrateDecisions,
    TraceEnvelope,
    TurnEnvelope,
    canonical_json,
    compute_inputs_hash,
)


def build_trace(
    *,
    turn: TurnEnvelope,
    grounding: GroundingBundle,
    proposal: ProposalEnvelope,
    decisions: SubstrateDecisions,
    final_text: str,
    total_ms: int,
    final_refs: list[str] | None = None,
) -> TraceEnvelope:
    """Assemble a ``TraceEnvelope`` from the per-stage outputs.

    ``inputs_hash`` is a SHA-256 over canonical JSON of ``(turn,
    grounding)``. Two runs whose inputs hash matches must produce
    identical traces when the model is deterministic.
    """
    return TraceEnvelope(
        turn_id=turn.turn_id,
        inputs_hash=compute_inputs_hash(turn, grounding),
        turn_envelope=turn,
        grounding_bundle=grounding,
        proposal_envelope=proposal,
        substrate_decisions=decisions,
        final_text=final_text,
        total_ms=total_ms,
        final_refs=list(final_refs or []),
    )


def trace_content_hash(trace: TraceEnvelope) -> str:
    """SHA-256 over the canonical JSON form of the whole envelope.

    Used by the determinism regression test in M1's test suite: two
    runs with the same inputs_hash AND the same stage outputs AND the
    same final text must produce the same content hash.
    """
    blob = canonical_json(trace).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()
