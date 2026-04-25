# AGIF-XCore Architecture

## System thesis

XCore is a **governance sidecar** for any LLM. A turn flows:

1. User text + grounding refs enter the system
2. The 6-stage **pipeline** produces a raw proposal from the backend
3. The 9-stage **substrate** evaluates the proposal against evidence,
   policies, and memory
4. The resolved **answer mode** reshapes the raw text into its final
   natural-language form
5. A **trace envelope** records every decision for deterministic replay

The user sees a fluent answer; the trace carries the audit trail.

## Turn flow

```
User input
    |
    v
+-----------+
| Pipeline  |   6 stages: intake -> retrieval -> semantic ->
| (6-stage) |              planner -> critic -> realizer
+-----------+
    |
    v
+------------+
| Substrate  |   9 stages: provenance -> support -> contradiction ->
| (9-stage)  |             policy -> action -> memory admission ->
+------------+             rollback/quarantine -> answer_mode -> trace
    |
    v
+-------------+
| Answer Mode |   8 modes: grounded_fact, grounded_summary,
| Reshaping   |            grounded_with_gap, derived_explanation,
+-------------+            clarify, search_needed, abstain,
    |                      bounded_estimate
    v
Trace envelope + natural-language answer
```

## Pipeline stages

| Stage | Purpose | Backend call? |
|---|---|---|
| Intake | Validates input, captures metadata | No |
| Retrieval | Fetches grounding chunks via BM25/vector | No |
| Semantic | Semantic abstraction of evidence | Optional |
| Planner | Asks the LLM to answer, injecting grounding + memory | Yes |
| Critic | NLI-style verification of answer vs evidence | Optional |
| Realizer | Final text cleanup | No |

Each stage has a per-stage budget. The runner enforces a global budget
across all stages.

## Substrate stages

The substrate is a chain of pure-logic modules. No LLM calls. Each
stage reads the proposal and prior stage outputs, then writes a decision
record to the trace.

| Stage | Module | Decision |
|---|---|---|
| 1. Provenance | `provenance_graph.py` | Records evidence refs |
| 2. Support state | `support_state_engine.py` | Labels support level |
| 3. Contradiction | `contradiction_ledger.py` | Detects conflicts |
| 4. Policy gate | `policy_gate.py` | Applies policy rules |
| 5. Action gate | `action_gate.py` | Blocks risky actions |
| 6. Memory admission | `memory_admission.py` | Gates memory writes |
| 7. Rollback/quarantine | `rollback_quarantine.py` | Handles corrupt state |
| 8. Answer mode | `decision_table.py` | Resolves final mode |
| 9. Trace | `trace/envelope.py` | Builds replayable envelope |

## Answer modes

The decision table resolves to one of 8 modes based on:

- `support_label` (supported / partial / unsupported / missing_evidence)
- `blocking_flag` (any stage blocked the proposal)
- `policy.decision_class` (allow / block / soften)
- `action.decision_class` (allow / block / soften)
- `task_family_hint` (optional)
- `retrieval_count` (how many grounding chunks were found)

| Mode | Trigger |
|---|---|
| `grounded_fact` | Supported + evidence refs present |
| `grounded_summary` | Supported + multiple refs |
| `grounded_with_gap` | Partial support, gaps noted |
| `derived_explanation` | No grounding, model explains from parametric knowledge |
| `clarify` | Question is ambiguous |
| `search_needed` | Evidence required but not available |
| `abstain` | Policy block, contradiction, or corrupt state |
| `bounded_estimate` | Estimated answer with stated bounds |

## Memory

Three memory planes with capacity caps:

| Plane | Cap | Purpose |
|---|---|---|
| Working | 64 | Current conversation state |
| Episodic | 512 | Every turn's Q/A record |
| Continuity | 256 | Substrate-admitted facts |

Memory is injected into the planner prompt on subsequent turns.
Filler detection prevents small models from echoing acknowledgements.

## Backends

All backends implement `ModelBackend` (ABC):

```python
class ModelBackend(ABC):
    @abstractmethod
    def complete(self, messages, *, model, temperature, max_tokens) -> BackendResponse: ...
    @abstractmethod
    def healthcheck(self) -> dict: ...
```

| Backend | Protocol |
|---|---|
| `OpenAICompatBackend` | HTTP `/v1/chat/completions` |
| `OllamaBackend` | HTTP `/api/chat` (native) |
| `AnthropicBackend` | Anthropic Messages API |
| `OnnxBackend` | Local onnxruntime inference |

## Trace determinism

- `inputs_hash` = SHA-256 of canonical JSON of (turn + grounding)
- `trace_content_hash` = SHA-256 of canonical JSON of the full envelope
- Two runs with the same inputs and `temperature=0.0` produce identical
  traces
- Regression test: 20 fixture turns, hashes checked across runs

## One code path

Raw vs governed runs go through the same `GovernedClient.ask()` method
with a `governance_enabled` boolean. There are no separate "arm"
functions.

```python
# Governed
client = GovernedClient(governance_enabled=True, ...)
result = client.ask("question")

# Raw (same code path, same method)
client = GovernedClient(governance_enabled=False, ...)
result = client.ask("question")
```
