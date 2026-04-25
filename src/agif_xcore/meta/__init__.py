"""Meta-cognition: weak-answer diagnosis and escalation (M4).

Ported from AGIFCore Phase 10. The original has 9 sub-engines
(self_model, observer, redirect, skeptic, journal, thinker,
surprise, fragments, diagnosis) coordinated by a meta-cognition
layer. XCore adapts the core insight — *detect weak answers from
extractable features and optionally retry once* — into a single
module with no LLM call needed for the diagnosis step.
"""

from __future__ import annotations

from .escalation import (
    MAX_RETRIES,
    EscalationResult,
    WeakAnswerDiagnosis,
    build_retry_messages,
    diagnose_weak_answer,
    should_escalate,
)

__all__ = [
    "EscalationResult",
    "MAX_RETRIES",
    "WeakAnswerDiagnosis",
    "build_retry_messages",
    "diagnose_weak_answer",
    "should_escalate",
]
