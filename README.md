# AGIF-XCore

**A model-agnostic governance sidecar for LLMs.**
Wraps any chat-completion backend and produces a natural-language answer
plus a deterministic, replayable trace envelope.

Status: **v1.0.0.** All six milestones complete. 52 source modules,
24 test modules, 261 tests passing. Benchmarked against TruthfulQA with
honest results.

---

## Why

Most LLM wrappers are a prompt template plus a retrieval step. XCore is
different: every turn passes through a 6-stage proposal pipeline and a
9-stage governance substrate before the final answer is rendered. The
user sees a fluent answer — never a classifier label — and the trace
records every decision the substrate made, keyed to a deterministic
replay hash so the same inputs always produce the same trace.

XCore is **not**:

- A new model or training framework
- A "bounded proof program" with frozen claims and review packets
- A RAG framework (it's a trust layer that can sit above any RAG pipeline)
- An agent framework

XCore **is**:

- A library you import: `from agif_xcore import GovernedClient`
- A CLI you invoke: `agif-xcore ask "..."`
- A drop-in HTTP proxy that speaks `/v1/chat/completions`
- A replay tool: `agif-xcore replay trace.jsonl`

---

## Install

```bash
pip install -e .
```

Core has **zero runtime dependencies**. Everything runs on Python 3.10+
stdlib. Optional extras pull in grounding, proxy, vector retrieval, and
ONNX support:

```bash
pip install -e ".[grounding]"      # BM25, PDF, DOCX, YAML
pip install -e ".[proxy]"          # Starlette + uvicorn
pip install -e ".[anthropic]"      # Anthropic Messages API
pip install -e ".[onnx]"           # onnxruntime local inference
pip install -e ".[vector]"         # sentence-transformers embeddings
pip install -e ".[dev]"            # pytest, respx
```

---

## Quick start

Assumes you have a local OpenAI-compatible server running. Ollama is the
reference backend:

```bash
ollama serve &
ollama pull gemma3:270m
```

### CLI

```bash
# Raw answer (no governance)
agif-xcore ask "What is BM25 retrieval?" --backend ollama --model gemma3:270m

# Governed answer with grounding
agif-xcore ask "What does our SOP say about backups?" \
  --backend ollama --model gemma3:270m \
  --governance --grounding ./docs/

# HTTP proxy (any OpenAI SDK points here)
agif-xcore serve --backend ollama --model gemma3:270m --port 8088
```

### OpenClaw integration

`--openclaw-profile` locks the proxy down for safe use behind OpenClaw: single served
model id, memory off, tool/function calls refused by default, wildcard CORS off,
optional bearer auth, and fail-closed audit events in the trace file. See
[docs/openclaw.md](docs/openclaw.md).

- **v0.1** — validated against OpenClaw 2026.4.22 for chat governance only.
  See the [v0.1 release note](docs/openclaw_v0_1_release_note.md).
- **v0.2** — adds substrate-routed *named* tool-call governance via
  `--tool-allowlist`. Tool execution still happens at the client; the proxy
  governs intent only. See [docs/openclaw_v0_2.md](docs/openclaw_v0_2.md).

### Library

```python
from agif_xcore import GovernedClient

# Governance ON — 9-stage substrate shapes the answer
client = GovernedClient(
    backend="ollama",
    model="gemma3:270m",
    governance_enabled=True,
    grounding_paths=["./docs/"],
)
result = client.ask("What does our SOP say about backups?")
print(result.text)          # fluent natural-language answer
print(result.answer_mode)   # e.g. "grounded_fact", "clarify", "abstain"
print(result.trace_id)      # deterministic replay anchor
print(result.refs)          # cited grounding refs

# Governance OFF — raw LLM output (same code path, one switch)
raw_client = GovernedClient(
    backend="ollama",
    model="gemma3:270m",
    governance_enabled=False,
)
raw = raw_client.ask("What does our SOP say about backups?")
```

---

## Architecture

```
User text + grounding refs
    |
    v
[6-stage pipeline]
    intake -> retrieval -> semantic -> planner -> critic -> realizer
    |
    v
[9-stage substrate]
    provenance -> support -> contradiction -> policy ->
    action -> memory admission -> rollback/quarantine ->
    answer_mode -> trace
    |
    v
Natural-language answer + trace envelope
```

### 8 answer modes

The substrate resolves to one of 8 modes. The realizer reshapes the raw
LLM text into a fluent answer appropriate for that mode:

| Mode | When |
|---|---|
| `grounded_fact` | Evidence supports the answer directly |
| `grounded_summary` | Multiple sources, summarized |
| `grounded_with_gap` | Partial evidence, gaps noted |
| `derived_explanation` | No grounding, but model can explain |
| `clarify` | Question is ambiguous |
| `search_needed` | Evidence required but not available |
| `abstain` | Policy block or contradiction detected |
| `bounded_estimate` | Estimated answer with stated bounds |

### Supported backends

| Backend | Module | Notes |
|---|---|---|
| Ollama | `backends.ollama` | Native `/api/chat` path |
| OpenAI-compatible | `backends.openai_compat` | LM Studio, vLLM, llama.cpp, Groq, OpenAI |
| Anthropic | `backends.anthropic` | Claude via Messages API |
| ONNX | `backends.onnx` | Local offline inference via onnxruntime |

### Grounding / retrieval

| Retriever | Module | Notes |
|---|---|---|
| BM25 | `grounding.bm25` | Keyword-based, zero deps |
| Vector | `grounding.vector` | sentence-transformers embeddings |
| Hybrid | `grounding.vector.HybridRetriever` | RRF fusion of BM25 + vector |

### Memory (M4)

Cross-turn conversation memory with three planes:

- **Working** (64 entries) — current conversation state
- **Episodic** (512 entries) — every turn's Q/A record
- **Continuity** (256 entries) — substrate-admitted facts

Filler detection prevents small models from echoing "Okay, I understand."
back as context.

### Weak-answer escalation (M4)

Extractable-feature diagnosis (hedge-word density, answer length, ref count,
grounding overlap, repetitive uncertainty). Optional single retry with a
tighter prompt. Hard cap: 1 retry per turn, no unbounded loops.

---

## Benchmark results

### TruthfulQA (790 questions, gemma3:270m-it-fp16 via Ollama)

Three arms, **one code path** (`GovernedClient` with `governance_enabled`
toggle). No hand-coded "arms", no rigged comparisons. Every row is a
real backend call recorded in its trace.

| Arm | Truthful | Hallucin. | Uninform. | Abstained | Truthful % | Hallucin. % |
|---|---|---|---|---|---|---|
| (a) Raw | 74 | 145 | 518 | 53 | 9.4% | 18.4% |
| (b) Governed | 74 | 145 | 518 | 53 | 9.4% | 18.4% |
| (c) Governed+grounding | 153 | 273 | 328 | 36 | 19.4% | 34.6% |

**Win condition: NOT MET.** We are shipping the real numbers.

**Honest analysis of why:**

1. **Raw vs Governed are identical.** The governance substrate classifies
   answer modes and reshapes text, but on a 270M model without grounding,
   the substrate has no evidence to work with. The 270M model produces
   the same answers either way. This is expected — the substrate is a
   trust layer over evidence, not a prompt improvement trick.

2. **Grounding doubled truthful rate (9.4% → 19.4%)** when the grounding
   corpus covered the topic. The model successfully extracted and
   presented factual information from the corpus.

3. **Grounding also increased hallucination rate (18.4% → 34.6%).**
   The grounding corpus covers ~30 of the 790 TruthfulQA topics. For
   the other 760 questions, irrelevant grounding text was injected,
   and the 270M model incorporated those words into answers. The
   keyword-overlap scorer then matched these words against incorrect
   reference answers. This is a real limitation of both the model size
   and the keyword-based scoring method.

4. **The keyword scorer is conservative.** 65% of raw answers are
   "uninformative" — the 270M model gives very short/vague responses
   that match neither correct nor incorrect keywords. An LLM judge
   would classify some of these differently.

**What would improve the results:**
- A larger model (7B+) that produces substantive answers for the raw arm,
  giving the governance layer more hallucinations to catch
- Topic-matched grounding (not one broad corpus for all 790 questions)
- An LLM-based scorer (at the cost of reproducibility and money)

### RAG retrieval (BM25, 20 eval questions)

| Metric | Value |
|---|---|
| Mean Precision@5 | 0.95 |
| Mean Recall@5 | 0.95 |
| Mean MRR | 0.95 |

---

## Running the benchmarks yourself

```bash
# TruthfulQA (requires running Ollama)
PYTHONPATH=. python -m benchmarks.truthfulqa_runner \
  --backend ollama --model gemma3:270m-it-fp16 \
  --output benchmarks/results --limit 50

# RAG eval (no backend needed — retrieval only)
PYTHONPATH=. python -m benchmarks.rag_eval_runner \
  --corpus benchmarks/data/grounding_facts.txt \
  --eval-set benchmarks/data/rag_eval_set.json \
  --output benchmarks/results/rag_eval.json
```

---

## Tests

```bash
pip install -e ".[dev]"
python -m pytest tests/ -q
```

261 tests, 6 skipped (vector tests skip when sentence-transformers not
installed; integration tests skip when Ollama not reachable).

---

## Roadmap

| Milestone | Scope | Status |
|---|---|---|
| **M1** | Library + CLI + OpenAI-compat backend + Ollama + trace | done |
| **M2** | 9-stage substrate + BM25 grounding + 6-stage pipeline | done |
| **M3** | HTTP proxy + OpenAI/Anthropic backends + streaming | done |
| **M4** | Memory planes + meta-cognition + weak-answer escalation | done |
| **M5** | ONNX backend + vector retrieval | done |
| **M6** | TruthfulQA benchmark + RAG eval + 1.0 release | done |

---

## Anti-theater rules (enforced in CI)

1. No hardcoded benchmark strings anywhere in `src/agif_xcore/`
2. No "contract dataclasses that return a config dict" pretending to
   be runtime
3. Raw vs governed comparisons share one code path with a boolean
   switch — never two hand-coded "arms"
4. Approved-model enforcement is behavioral (backend actually returns
   the expected model id), never nominal
5. No review packets, no handoff packets, no phase directories — just
   git tags
6. Every public module has a test with the same basename
7. Determinism regression test locks trace hashes across commits
8. No unbounded retry loops; meta retry capped at 1
9. No `# TODO: real implementation later` — merge gate
10. Benchmarks never hand-write answers; every row comes from a real
    backend call recorded in its trace

---

## License

Apache-2.0. See `LICENSE`.
