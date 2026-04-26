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

## Live validation (post-tag follow-up)

When a tool-capable upstream model is available (e.g. `qwen2.5-coder:7b`):

1. Pull the model: `ollama pull qwen2.5-coder:7b`.
2. Write a small policy file with one allowed tool, one softened, one blocked, and one allowed-with-argument-deny.
3. Run AGIF Governor with `--tool-policy-file`.
4. Send four prompts that exercise: allow (clean args), soften (clean args), block by name, block by argument deny.
5. Confirm:
   - The allow tool's `tool_calls` reach the client.
   - The soften tool's `tool_calls` reach the client AND a `tool_softened` audit event lands.
   - The named-block path returns the v0.2 text refusal AND a `tool_blocked` event.
   - The argument-block path returns a text refusal AND a `tool_blocked_by_argument` event with no argument value leakage.

Capture the result in `docs/openclaw_v0_3_live_validation.md`.
