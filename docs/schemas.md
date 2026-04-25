# AGIF-XCore Data Schemas

All data types are stdlib `dataclasses`. Every envelope carries a
`schema_version` string. Determinism tests hash the canonical JSON form.

## TurnEnvelope

Immutable inputs to one turn.

| Field | Type | Notes |
|---|---|---|
| `turn_id` | `str` | Deterministic SHA-256 from (conv_id, time, input) |
| `conversation_id` | `str` | Groups turns in a conversation |
| `user_input_text` | `str` | The user's raw question |
| `backend_name` | `str` | e.g. "ollama", "openai_compat" |
| `model_id` | `str` | e.g. "gemma3:270m" |
| `created_at` | `str` | ISO-8601 UTC |
| `schema_version` | `str` | Currently "1.0.0" |
| `task_family_hint` | `str | None` | Optional hint for the decision table |
| `policy_refs` | `list[str] | None` | Policy bundle refs |
| `grounding_refs` | `list[str] | None` | Grounding source refs |
| `temperature` | `float` | Default 0.0 |
| `max_tokens` | `int | None` | Optional max tokens |

## GroundingChunk

One retrieved chunk of evidence.

| Field | Type | Notes |
|---|---|---|
| `ref` | `str` | Source reference, e.g. "doc.txt#chunk0" |
| `source_path` | `str` | File path |
| `text` | `str` | Chunk text content |
| `score` | `float` | Retrieval score (0.0–1.0) |
| `loader` | `str` | Loader name (text, pdf, docx) |

## GroundingBundle

All evidence for one turn.

| Field | Type | Notes |
|---|---|---|
| `chunks` | `list[GroundingChunk]` | Retrieved chunks |
| `retriever_name` | `str` | e.g. "bm25", "vector", "hybrid" |
| `retrieval_ms` | `int` | Retrieval time in milliseconds |
| `schema_version` | `str` | Currently "1.0.0" |

## ProposalEnvelope

Raw answer material from the pipeline.

| Field | Type | Notes |
|---|---|---|
| `turn_id` | `str` | Links back to TurnEnvelope |
| `raw_answer_text` | `str` | The LLM's raw response |
| `backend_model_id` | `str` | Actual model used |
| `schema_version` | `str` | Currently "1.0.0" |
| `cited_refs` | `list[str]` | Cited grounding refs |
| `stage_outputs` | `dict[str, dict]` | Per-stage output data |
| `stage_timings_ms` | `dict[str, int]` | Per-stage timing |
| `finish_reason` | `str | None` | stop, length, etc. |
| `prompt_tokens` | `int | None` | If reported by backend |
| `completion_tokens` | `int | None` | If reported by backend |

## SubstrateDecisions

All 9 substrate decision records. Each is a dict or None.

| Field | Type |
|---|---|
| `provenance_record` | `dict | None` |
| `support_state_record` | `dict | None` |
| `contradiction_record` | `dict | None` |
| `policy_gate_decision` | `dict | None` |
| `action_gate_decision` | `dict | None` |
| `memory_admission_decision` | `dict | None` |
| `rollback_or_quarantine_record` | `dict | None` |
| `final_answer_mode_decision` | `dict | None` |
| `schema_version` | `str` |

Property: `governance_enabled` → `True` if any stage ran.

## TraceEnvelope

The replayable trace of one turn end-to-end.

| Field | Type | Notes |
|---|---|---|
| `turn_id` | `str` | Links to TurnEnvelope |
| `inputs_hash` | `str` | SHA-256 of canonical (turn + grounding) |
| `turn_envelope` | `TurnEnvelope` | Full input |
| `grounding_bundle` | `GroundingBundle` | Retrieved evidence |
| `proposal_envelope` | `ProposalEnvelope` | Raw pipeline output |
| `substrate_decisions` | `SubstrateDecisions` | All 9 decisions |
| `final_text` | `str` | User-facing answer |
| `total_ms` | `int` | Total processing time |
| `schema_version` | `str` | Currently "1.0.0" |
| `final_refs` | `list[str]` | Cited refs in the final answer |

## AnswerEnvelope

What `GovernedClient.ask()` returns.

| Field | Type | Notes |
|---|---|---|
| `text` | `str` | User-facing natural language |
| `trace_id` | `str` | For replay/audit |
| `refs` | `list[str]` | Cited grounding refs |
| `decisions` | `SubstrateDecisions | None` | Substrate decisions |
| `total_ms` | `int` | Total processing time |
| `answer_mode` | `str` | One of 8 modes |

## Serialization

```python
from agif_xcore import canonical_json, pretty_json, compute_inputs_hash

# Deterministic JSON (no whitespace, sorted keys)
canonical_json(trace)  # for hashing

# Human-readable JSON (2-space indent)
pretty_json(trace)     # for display

# Replay hash
compute_inputs_hash(turn, grounding)  # SHA-256
```

## Answer modes

```python
from agif_xcore import ALLOWED_ANSWER_MODES
# ('grounded_fact', 'grounded_summary', 'grounded_with_gap',
#  'derived_explanation', 'clarify', 'search_needed',
#  'abstain', 'bounded_estimate')
```
