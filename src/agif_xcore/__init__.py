"""AGIF-XCore — a model-agnostic governance sidecar for LLMs.

Public surface:

    from agif_xcore import GovernedClient
    client = GovernedClient(backend="ollama", model="gemma3:270m")
    answer = client.ask("What is BM25?")
    print(answer.text)
    print(answer.trace_id)
"""

from __future__ import annotations

from .backends.base import (
    BackendBlocked,
    BackendContractError,
    BackendError,
    BackendModelMismatch,
    BackendResponse,
    BackendTimeout,
    ModelBackend,
)
from .backends.registry import available_backends, resolve_backend
from .client import GovernedClient
from .schemas import (
    ALLOWED_ANSWER_MODES,
    AnswerEnvelope,
    GroundingBundle,
    GroundingChunk,
    ProposalEnvelope,
    SubstrateDecisions,
    TraceEnvelope,
    TurnEnvelope,
    canonical_json,
    compute_inputs_hash,
    make_conversation_id,
    make_turn_id,
    pretty_json,
)
from .memory import ConversationMemory, InMemoryStore, MemoryEntry
from .meta import (
    EscalationResult,
    WeakAnswerDiagnosis,
    diagnose_weak_answer,
    should_escalate,
)
from .trace import (
    FileJsonlSink,
    MultiSink,
    NullSink,
    StdoutJsonlSink,
    TraceSink,
    build_trace,
    trace_content_hash,
)

__version__ = "1.0.0"

__all__ = [
    "ALLOWED_ANSWER_MODES",
    "AnswerEnvelope",
    "BackendBlocked",
    "BackendContractError",
    "BackendError",
    "BackendModelMismatch",
    "BackendResponse",
    "BackendTimeout",
    "ConversationMemory",
    "EscalationResult",
    "FileJsonlSink",
    "GovernedClient",
    "GroundingBundle",
    "GroundingChunk",
    "InMemoryStore",
    "MemoryEntry",
    "ModelBackend",
    "MultiSink",
    "NullSink",
    "ProposalEnvelope",
    "StdoutJsonlSink",
    "SubstrateDecisions",
    "TraceEnvelope",
    "TraceSink",
    "TurnEnvelope",
    "WeakAnswerDiagnosis",
    "__version__",
    "available_backends",
    "build_trace",
    "canonical_json",
    "compute_inputs_hash",
    "diagnose_weak_answer",
    "make_conversation_id",
    "make_turn_id",
    "pretty_json",
    "resolve_backend",
    "should_escalate",
    "trace_content_hash",
]
