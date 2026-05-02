# AGIF Governor for OpenClaw — v0.3 Tool Policy, Soften, Argument Inspection

**Status:** v0.3 adapter — extends v0.2 with three additions, all stdlib-only, fully backward-compatible. With no `--tool-policy-file` and no `--tool-allowlist`, behaviour is byte-for-byte identical to v0.2 (which already preserves v0.1).

## What v0.3 changes

v0.2 governed tool calls by **name only** (`--tool-allowlist search,fetch`) and treated the substrate's `soften` decision as `block`. v0.3 adds three things:

1. **The soften path is real.** When the substrate emits `decision_class="soften"`, the proxy passes `tool_calls` through to the client *and* writes a `tool_softened` audit event with the substrate reason codes. The OpenAI response shape is unchanged: `content: null` and `finish_reason: "tool_calls"`. **No footer text is injected into a `tool_calls` response.** Soften visibility is via `x_agif_trace.soften_warnings` and the audit event.
2. **Argument inspection by stdlib regex.** Per-tool deny patterns can be declared per argument path. The model's `tool_calls.arguments` are parsed, walked dot-path, and matched. v0.3 is **all-or-nothing**: any deny match drops the entire `tool_calls` array for that turn and the response becomes a text refusal naming only field paths and short pattern ids — **never the argument values**.
3. **JSON policy bundle.** `--tool-policy-file <path>` accepts a small JSON file declaring per-tool `decision` (`allow` / `soften` / `block`), optional reason text, and optional argument deny patterns. The v0.2 `--tool-allowlist` form is preserved as backward-compat sugar; both flags are mutually exclusive.

**Tool execution still happens at the client (OpenClaw).** The proxy never executes a tool — it only decides whether the model is allowed to propose one and, when it is, whether the proposed arguments pass the operator's regex screen.

## Routing summary (v0.3, additions in **bold**)

```
request body
  ├── no tools → v0.1 chat path                               (unchanged)
  ├── tools[]  → v0.2/v0.3 substrate-routed                   (extended)
  │     ├── tool_policy is None → v0.1 fast fail-closed       (unchanged)
  │     └── tool_policy non-empty → governed
  │           ├── substrate=allow + args clean → tool_calls passthrough
  │           ├── substrate=soften + args clean → tool_calls passthrough
  │           │                                  + tool_softened audit       (NEW)
  │           ├── substrate=block → text refusal + tool_blocked audit
  │           └── any args matched deny pattern OR > MAX_ARGUMENT_VALUE_CHARS
  │                                  → tool_calls dropped (all-or-nothing)
  │                                  + tool_blocked_by_argument audit         (NEW)
  ├── functions[] / tool_choice ≠ "none" / role: "tool"
  │   / tool_calls in history → v0.1 fast fail-closed         (unchanged)
  └── tool_choice == "none" → v0.1 chat path                  (unchanged)
```

## JSON bundle schema

`schema_version: "openclaw_tool_policy_v1"`. Stdlib `json`, no extras.

```json
{
  "schema_version": "openclaw_tool_policy_v1",
  "default": "block",
  "tools": {
    "search":      { "decision": "allow" },
    "fetch":       { "decision": "allow" },
    "write_file":  { "decision": "soften", "reason": "writes user files" },
    "delete_file": { "decision": "block",  "reason": "destructive" },
    "exec": {
      "decision": "allow",
      "argument_deny_patterns": {
        "command": "rm\\s+-rf|sudo|curl\\s+.*\\|\\s*bash"
      }
    }
  }
}
```

**Validation rules** (all enforced at load time; bad bundle exits CLI with code 2):

- `schema_version` must be exactly `"openclaw_tool_policy_v1"`.
- `default` ∈ {`"allow"`, `"soften"`, `"block"`}; missing defaults to `"block"`.
- Each tool entry: `decision` ∈ same set; `reason` optional string; `argument_deny_patterns` optional dict mapping `argument_path → regex_string`.
- Argument paths are dot-separated keys only. Paths containing `[` or `]` are **rejected at load time** (no array indexing in v0.3).
- Each regex compiles eagerly. Bad regex → `ValueError` naming the offending tool and path.

**Regex safety** (stdlib `re` has no timeout):

- Only **string-typed** argument values are inspected. Non-strings (lists, dicts, ints, floats, bools, None) are skipped silently.
- Strings longer than `MAX_ARGUMENT_VALUE_CHARS = 4096` are blocked **without running the regex**, with `reason_code="argument_value_too_long"`. Conservative fail-closed beats hanging the proxy on a pathological pattern.

## CLI

```bash
agif-xcore serve \
  --backend ollama \
  --model gemma3:270m-it-fp16 \
  --served-model-id agif-governor/gemma3-270m \
  --openclaw-profile \
  --trace-visibility both \
  --trace-file traces/openclaw_agif.jsonl \
  --tool-policy-file ./policies/openclaw.json
```

The startup banner reflects the loaded policy:

```
  tool policy     : 5 tools (default=block) allow=3 soften=1 block=1
```

`--tool-allowlist` and `--tool-policy-file` are **mutually exclusive**. Setting both exits 2 with a clear error. v0.2 callers who only use `--tool-allowlist` see no change.

## Library

```python
from agif_xcore import GovernedClient
from agif_xcore.policies.tool_policy import load_tool_policy

policy = load_tool_policy("/etc/agif-governor/policy.json")

client = GovernedClient(
    backend="ollama",
    model="gemma3:270m-it-fp16",
    governance_enabled=True,
    tool_policy=policy,
)

result = client.ask(
    "Find and summarise the BM25 paper",
    tools=[{"type": "function", "function": {"name": "search"}}],
)
print(result.tool_calls)        # populated when allow OR soften and args clean
print(result.soften_warnings)   # substrate reason codes when softened
print(result.argument_denials)  # populated when args matched a deny pattern
```

## Response shapes

### Allow path (unchanged from v0.2)

`content: null`, `finish_reason: "tool_calls"`, `tool_calls: [...]`.

### Soften path (new)

```json
{
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": null,
      "tool_calls": [
        {"id": "call_0", "type": "function",
         "function": {"name": "write_file", "arguments": "..."}}
      ]
    },
    "finish_reason": "tool_calls"
  }],
  "x_agif_trace": {
    "trace_id": "turn_…",
    "answer_mode": "grounded_fact",
    "tool_calls_allowed": true,
    "soften_warnings": [
      "high_risk_action_requires_softening",
      "write_file:writes user files"
    ],
    "argument_denials": []
  }
}
```

`content` is `null` per OpenAI spec. **No AGIF footer is injected** when tool_calls are returned. Soften reasons surface only in `x_agif_trace` and the `tool_softened` audit event.

### Block path — tool name (unchanged from v0.2)

Text refusal naming the off-list tools. `tool_blocked` audit event.

### Block path — argument deny (new, all-or-nothing)

```json
{
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "AGIF Governor blocked tool calls: argument deny pattern matched. exec.command=argument_pattern_match#a1b2c3d4."
    },
    "finish_reason": "stop"
  }],
  "x_agif_trace": {
    "tool_calls_allowed": false,
    "argument_denials": [
      {
        "tool_name": "exec",
        "argument_path": "command",
        "pattern_id": "a1b2c3d4",
        "reason_code": "argument_pattern_match"
      }
    ]
  }
}
```

The user-visible text names only the field path and the 8-char `pattern_id` (a SHA-256 prefix of the regex source) — never the argument value. Even on `--trace-visibility=both`, the regular footer applies because this is a plain-text response.

## Audit events

v0.3 extends `openclaw_profile_event_v1` with two new `event_type` values:

### `tool_softened`

```json
{
  "schema_version": "openclaw_profile_event_v1",
  "event_type": "tool_softened",
  "trace_id": "turn_…",
  "created": 1714000000,
  "served_model_id": "agif-governor/gemma3-270m",
  "upstream_model_id": "gemma3:270m-it-fp16",
  "answer_mode": "grounded_fact",
  "reason_code": "high_risk_action_requires_softening",
  "softened_tool_names": ["write_file"],
  "soften_reasons": [
    "high_risk_action_requires_softening",
    "write_file:writes user files"
  ],
  "governance_enabled": true,
  "memory_enabled": false
}
```

### `tool_blocked_by_argument`

One event **per denial** (not per turn). `pattern_id` is a short hash of the regex; the regex source itself never leaks into the audit event.

```json
{
  "schema_version": "openclaw_profile_event_v1",
  "event_type": "tool_blocked_by_argument",
  "trace_id": "turn_…",
  "created": 1714000000,
  "served_model_id": "agif-governor/gemma3-270m",
  "upstream_model_id": "gemma3:270m-it-fp16",
  "answer_mode": "abstain",
  "reason_code": "argument_pattern_match",
  "tool_name": "exec",
  "argument_path": "command",
  "pattern_id": "a1b2c3d4",
  "governance_enabled": true,
  "memory_enabled": false
}
```

**Never logged in any audit event:**
- Argument values (only field paths and short pattern hashes).
- Tool argument JSON.
- The bearer token value (preserved from v0.1).
- The configured policy contents (only counts in the banner).
- The regex source (only the 8-char `pattern_id`).

## Backward compatibility

- v0.1 fast fail-closed when no policy is configured → unchanged.
- v0.2 `--tool-allowlist` continues to work via `tool_policy_from_allowlist`.
- v0.2 unit tests pass without modification.
- v0.1 no-secret regression test (`test_v0_1_no_secret_regression_trace_body_and_stderr`) still passes.
- The `tools.deny: ["*"]` workaround in OpenClaw provider config remains valid.

## Out of scope for v0.3

- **`argument_allow_patterns`.** Only deny patterns. Allow-style patterns are deferred to v0.4 because they conflate denylist and allowlist semantics.
- **Per-tool-call argument filtering.** v0.3 is all-or-nothing: one deny match drops the whole `tool_calls` array. Per-call filtering is v0.4.
- **JSON Schema validation of arguments.** Regex only.
- **LLM-as-judge.** Not in v0.3.
- **Streaming tool_calls.** Existing single-event SSE fallback only.
- **ONNX / Anthropic backend tool support.** Still raises `BackendError`.
- **Generic (non-OpenClaw) proxy path.** Untouched.
- **Multi-turn tool flows.** `role: "tool"` and history `tool_calls` remain on the v0.1 fast fail-closed path.
- **Per-agent policy bundles.** One global policy per proxy.
- **Live validation as a tag gate.** Stub-tests gate; live validation follows.

## Validation

Run from `/Users/ahsadin/Documents/AGIF-XCore`:

```bash
.venv/bin/python -m pytest tests -q
.venv/bin/python -m pytest tests/unit/test_tool_policy.py -q
.venv/bin/python -m pytest tests/unit/test_proxy_server.py::OpenClawToolGovernanceTests -q
.venv/bin/python -m pytest tests/unit/test_proxy_server.py::OpenClawCliValidatorTests -q
.venv/bin/python -m agif_xcore serve --help    # confirm --tool-policy-file appears
```

Expected: **341 passed, 6 skipped**. The +25 over v0.2's 316 are 15 new tests in `test_tool_policy.py`, 7 new tests in `OpenClawToolGovernanceTests`, and 3 new tests in `OpenClawCliValidatorTests`.

## Live validation status

**Status: hardware-deferred.** Live validation against a tool-capable upstream model has **not** been run on the validation host. The host (16 GB MacBook Air, Apple M4) had only `gemma3:270m-it-fp16` installed, which is chat-only and does not emit `tool_calls`. Running the four-probe procedure against `gemma3:270m` would have produced four indistinguishable plain-text responses and would not have validated the v0.3 decision paths in any way the stub tests don't already cover. The disciplined choice was to ship the runbook honestly and defer the live run.

### What IS verified (not deferred)

- **341 stub tests pass** on `commit b412b92`, including:
  - `test_v0_1_no_secret_regression_trace_body_and_stderr` — bearer token never reaches trace, error body, or stderr.
  - `test_argument_deny_audit_event_does_not_log_argument_value` — argument values never reach `tool_blocked_by_argument` audit events.
  - `test_argument_value_too_long_blocks_without_running_regex` — uses a catastrophic-backtracking regex `(a+)+b` against a 4097-char input; the safety limit fires before the regex runs (test completes in <5 s).
  - All four decision paths (allow / soften / name-block / argument-deny) exercised against a stub backend that returns canned `tool_calls`.
  - JSON policy-bundle parsing, regex compilation, schema-version mismatch, array-index-path rejection, default-decision fallback.
  - CLI mutual exclusion of `--tool-allowlist` and `--tool-policy-file`.

### What is NOT verified live

- That a real tool-capable model (e.g. `qwen2.5:7b-instruct`, `llama3.2:3b-instruct`) emits `tool_calls` in OpenAI shape against this proxy under each of the four decision paths.
- That a real model's `function.arguments` JSON shape parses cleanly through `evaluate_arguments` end-to-end.
- That OpenClaw's UX surface displays a soften response (`content: null` + `tool_calls`) without confusion.

The contract is gated on stubs. Under-the-wire reliability of `tool_calls` JSON shape from any specific upstream model is the operator's responsibility to confirm before relying on a given model.

### Runbook (any operator with a tool-capable model can run this)

Recommended models, choose by hardware:

| Hardware | Model | Disk | Notes |
|---|---|---:|---|
| 16 GB+ unified memory | `qwen2.5:7b-instruct-q4_K_M` | ~4.7 GB | Strongest tool-call reliability. |
| 8–16 GB | `qwen2.5:3b-instruct` | ~2.3 GB | Slightly less reliable; some probes may need a forced `tool_choice`. |
| 8–16 GB | `llama3.2:3b-instruct-q4_K_M` | ~2.0 GB | Smaller; tool-call emission is decent. |
| Any | OpenAI-compatible hosted (OpenRouter, Together, Groq) | 0 | Use proxy's `openai_compat` backend; needs an API key. |

**Policy file** (`/tmp/v0_3_policy.json`) — one tool per decision class:

```json
{
  "schema_version": "openclaw_tool_policy_v1",
  "default": "block",
  "tools": {
    "search":      { "decision": "allow" },
    "write_file":  { "decision": "soften", "reason": "writes user files" },
    "delete_file": { "decision": "block",  "reason": "destructive" },
    "exec": {
      "decision": "allow",
      "argument_deny_patterns": {
        "command": "rm\\s+-rf|sudo"
      }
    }
  }
}
```

**Start AGIF Governor with the policy:**

```bash
ollama pull qwen2.5:7b-instruct-q4_K_M    # or your chosen model

cd /Users/ahsadin/Documents/AGIF-XCore
.venv/bin/python -m agif_xcore serve \
  --backend ollama \
  --model qwen2.5:7b-instruct-q4_K_M \
  --served-model-id agif-governor/qwen2.5-7b \
  --openclaw-profile \
  --trace-visibility both \
  --trace-file /tmp/openclaw_v0_3_live.jsonl \
  --tool-policy-file /tmp/v0_3_policy.json &
sleep 6
curl -s http://127.0.0.1:8088/health | python3 -m json.tool
```

The startup banner should report:
```
  tool policy     : 4 tools (default=block) allow=2 soften=1 block=1
```

**Four probes** (one per decision class). Save each response to its own file:

```bash
# (1) ALLOW
curl -s http://127.0.0.1:8088/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"agif-governor/qwen2.5-7b",
       "messages":[{"role":"user","content":"Search the web for BM25"}],
       "tools":[{"type":"function","function":{"name":"search",
         "parameters":{"type":"object","properties":{"q":{"type":"string"}},"required":["q"]}}}],
       "tool_choice":"auto"}' > /tmp/v0_3_allow.json

# (2) SOFTEN
curl -s http://127.0.0.1:8088/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"agif-governor/qwen2.5-7b",
       "messages":[{"role":"user","content":"Write hello world to /tmp/hi.sh"}],
       "tools":[{"type":"function","function":{"name":"write_file",
         "parameters":{"type":"object","properties":{"path":{"type":"string"},"contents":{"type":"string"}},"required":["path","contents"]}}}],
       "tool_choice":"auto"}' > /tmp/v0_3_soften.json

# (3) NAME-BLOCK
curl -s http://127.0.0.1:8088/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"agif-governor/qwen2.5-7b",
       "messages":[{"role":"user","content":"Delete /tmp/junk.log"}],
       "tools":[{"type":"function","function":{"name":"delete_file",
         "parameters":{"type":"object","properties":{"path":{"type":"string"}},"required":["path"]}}}],
       "tool_choice":"auto"}' > /tmp/v0_3_name_block.json

# (4) ARGUMENT-DENY (model proposes `rm -rf`)
curl -s http://127.0.0.1:8088/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"agif-governor/qwen2.5-7b",
       "messages":[{"role":"user","content":"Run: rm -rf /tmp/scratch"}],
       "tools":[{"type":"function","function":{"name":"exec",
         "parameters":{"type":"object","properties":{"command":{"type":"string"}},"required":["command"]}}}],
       "tool_choice":"auto"}' > /tmp/v0_3_arg_deny.json

kill %1 2>/dev/null
```

**Expected results table** (the operator fills in the `trace_id` column from the responses):

| Case | finish_reason | content | tool_calls | tool_calls_allowed | audit event | trace_id |
|---|---|---|---|---|---|---|
| allow | `tool_calls` | null | populated | true | (none) | `turn_…` |
| soften | `tool_calls` | null | populated | true | `tool_softened` | `turn_…` |
| name_block | `stop` | text refusal naming `delete_file` | absent | false | `tool_blocked` | `turn_…` |
| arg_deny | `stop` | text naming `exec.command=argument_pattern_match#…` | absent | false | `tool_blocked_by_argument` | `turn_…` |

**No-leak grep** (the most important v0.3 invariant — argument values never reach audit events):

```bash
python3 - <<'PY'
import json
leaked = False
for line in open('/tmp/openclaw_v0_3_live.jsonl'):
    o = json.loads(line)
    if o.get('schema_version') == 'openclaw_profile_event_v1':
        if '/tmp/scratch' in json.dumps(o):
            print('LEAK:', o); leaked = True
print('PASS — no argument value leaked into audit events.' if not leaked else 'REGRESSION')
PY
```

**Capture the run** in `docs/openclaw_v0_3_live_validation.md` with: date, model + version, the four-row table filled in, the audit-event lines, the no-leak grep result, and any model-specific caveats (e.g. "case 4 needed two retries because the model returned plain text the first time").

### Caveats every operator should expect

1. **Models sometimes return text when you asked for tool_calls.** Even strong 7B models do this occasionally. Force `tool_choice` or retry; if persistent, the model isn't a fit.
2. **Models sometimes emit malformed `arguments` JSON.** v0.3's safety contract treats malformed input as a free pass (no inspection). Force `tool_choice` to a specific function and provide a tight parameter schema to reduce the failure mode.
3. **The model's choice is not the policy's choice.** A model may *also* return text-only when the substrate would have allowed a tool call. That doesn't break governance; it just means the model declined to use the tool. The validation table tracks what the *proxy* did, not what the *model* preferred.

This runbook will continue to live in this document until either the validation host gets a tool-capable model or an operator runs it elsewhere and adds `docs/openclaw_v0_3_live_validation.md` alongside.
