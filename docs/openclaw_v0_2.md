# AGIF Governor for OpenClaw — v0.2 Tool-Call Governance

**Status:** v0.2 adapter — substrate-routed tool-call governance for the OpenClaw profile. Ships on top of [v0.1](openclaw_v0_2.md) and is fully backward-compatible: with no `--tool-allowlist`, behaviour is identical to v0.1 (every tool call fail-closed).

## What v0.2 changes

v0.1 fail-closed on **any** tool/function-call payload. Every request with `tools[]`, `tool_choice ≠ "none"`, `functions[]`, `function_call ≠ "none"`, `role: "tool"`, or `tool_calls` in history hit the same refusal path with a `tool_refusal` audit event.

v0.2 keeps the v0.1 path for legacy and multi-turn patterns but routes the modern `tools[]` array through the substrate's `action_gate` stage. Tools the operator has explicitly allowlisted reach the upstream model; the model's `tool_calls` reply is then governed by the substrate. Off-list tools are blocked at the policy gate before the model can act on them, and a `tool_blocked` audit event is appended to the trace JSONL.

**Tool execution still happens at the client (OpenClaw).** The proxy never executes a tool — it only decides whether the model is allowed to propose one.

## Routing

```
request body
  ├── no tools → v0.1 chat path                         (unchanged)
  ├── tools[]  → v0.2 substrate-routed                  (new)
  │     ├── tool_allowlist empty → v0.1 fast fail-closed (unchanged)
  │     └── tool_allowlist non-empty → governed
  ├── functions[] / tool_choice ≠ "none" / role: "tool"
  │   / tool_calls in history → v0.1 fast fail-closed   (unchanged)
  └── tool_choice == "none" → v0.1 chat path            (unchanged)
```

The classification helper is `agif_xcore.proxy.server._classify_tool_intent(body)` returning one of `"none" | "substrate" | "fail_closed"`.

## How the substrate decides

When the proxy classifies a request as **substrate-routed**:

1. Proxy passes `tools` to `GovernedClient.ask(..., tools=...)`.
2. The client passes `tools` to the backend's `complete(..., tools=...)`.
3. Backend forwards `tools` to the upstream and parses any returned `tool_calls`.
4. The client synthesizes substrate policy refs from the **request's** tool names:
   - `policy:allow:tool:<name>` for names in `tool_allowlist`
   - `policy:block:tool:<name>` for names not in `tool_allowlist`
5. The substrate runs the standard 9 stages. Two stages do the work:
   - `support_state_engine` sees a `policy:block:*` ref and labels the turn `blocked_by_policy`.
   - `policy_gate` matches the same ref pattern and emits `decision_class="block"`.
   - `action_gate` cascades: if `policy_gate=block`, then `action_gate=block` with `reason_code="policy_gate_block"`. If everything is clean, `action_gate=allow` with `allowed_action_surface_or_none="tool_call"`.
6. The client reads the action_gate decision:
   - **allow** → `AnswerEnvelope.tool_calls` is populated with the model's tool_calls.
   - **block / soften / not_applicable** → `tool_calls` is None and the assistant text becomes a structured refusal naming the off-list tools.

## Configuration

### Proxy CLI

```
--tool-allowlist NAME[,NAME...]     repeatable; comma-separated allowed
```

Example:

```bash
agif-xcore serve \
  --backend ollama \
  --model gemma3:270m-it-fp16 \
  --served-model-id agif-governor/gemma3-270m \
  --openclaw-profile \
  --trace-visibility both \
  --trace-file traces/openclaw_agif.jsonl \
  --tool-allowlist search,fetch \
  --tool-allowlist read_file
```

The startup banner reflects the state:

```
  tool allowlist  : ALLOW search, fetch, read_file
```

When omitted or empty, the banner reads `OFF (every tool call fail-closed; v0.1 behaviour)` and `tool_refusal` audit events keep firing exactly as in v0.1.

### Library

```python
from agif_xcore import GovernedClient

client = GovernedClient(
    backend="ollama",
    model="gemma3:270m-it-fp16",
    governance_enabled=True,
    tool_allowlist=("search", "fetch"),
)
result = client.ask(
    "Find the BM25 paper",
    tools=[{"type": "function", "function": {"name": "search"}}],
)
print(result.tool_calls)   # populated only when action_gate allowed
print(result.text)         # a refusal message when action_gate blocked
```

## Response shapes

### Allow path

```json
{
  "id": "chatcmpl-turn_…",
  "object": "chat.completion",
  "created": 1714000000,
  "model": "agif-governor/gemma3-270m",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": null,
      "tool_calls": [
        {"id": "call_0", "type": "function",
         "function": {"name": "search", "arguments": "{...}"}}
      ]
    },
    "finish_reason": "tool_calls"
  }],
  "x_agif_trace": {
    "trace_id": "turn_…",
    "answer_mode": "grounded_fact",
    "tool_calls_allowed": true,
    "served_model_id": "agif-governor/gemma3-270m",
    "upstream_model_id": "gemma3:270m-it-fp16",
    "memory_enabled": false,
    "...": "..."
  }
}
```

`finish_reason` is `"tool_calls"`. `content` is `null` per OpenAI spec. The client is expected to execute the tool and respond — but that's outside the proxy's scope.

### Block path (substrate decided block)

HTTP 200, plain text refusal:

```json
{
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "AGIF Governor blocked tool calls: delete. Allowed tools: search."
    },
    "finish_reason": "stop"
  }],
  "x_agif_trace": {
    "trace_id": "turn_…",
    "answer_mode": "abstain",
    "tool_calls_allowed": false
  }
}
```

`trace_id` starts with `turn_` because the model was called and the substrate decided after.

### Fast fail (legacy / empty allowlist)

Unchanged from v0.1: HTTP 200 with the fixed v0.1 refusal message and a `refusal-…` trace id.

## Audit events

v0.2 extends `openclaw_profile_event_v1` with one new `event_type`:

```
"tool_blocked"
```

Emitted exactly when:

- The request was substrate-routed (had a `tools[]` array, allowlist non-empty), AND
- The substrate did not allow tool_calls through (action_gate ≠ `allow`).

Event shape:

```json
{
  "schema_version": "openclaw_profile_event_v1",
  "event_type": "tool_blocked",
  "trace_id": "turn_…",
  "created": 1714000000,
  "served_model_id": "agif-governor/gemma3-270m",
  "upstream_model_id": "gemma3:270m-it-fp16",
  "answer_mode": "abstain",
  "reason_code": "policy_gate_block",
  "blocked_tool_names": ["delete"],
  "governance_enabled": true,
  "memory_enabled": false
}
```

The `trace_id` of the audit event matches `x_agif_trace.trace_id` returned to the client.

**Never logged in any audit event:**
- Tool argument JSON (only names appear).
- The bearer token value (preserved from v0.1).
- The configured tool allowlist (only the blocked-name list per request).

## Backward compatibility

- Empty `--tool-allowlist` → v0.1 behaviour byte-for-byte (`tool_refusal` audit events).
- Generic (non-OpenClaw) proxy path → unchanged.
- v0.1 unit tests continue to pass without modification.
- The v0.1 no-secret regression test (`test_v0_1_no_secret_regression_trace_body_and_stderr`) continues to pass.

## Out of scope for v0.2

- **Tool execution.** Always at the client.
- **`soften` decisions.** The substrate already emits `soften`; v0.2 treats it as `block` for response purposes (no soften wrapper). Plumbed through trace for forward-compatibility with v0.3.
- **Argument-content analysis.** v0.2 governs by tool name only.
- **ONNX and Anthropic backends.** They raise `BackendError("tools not supported by this backend in v0.2")` if `tools` is non-empty. Use `ollama` or `openai_compat`.
- **Streaming tool_calls.** Single-event SSE fallback only.
- **Generic-proxy tool governance.** The substrate-routed path is OpenClaw-profile only.
- **Live tool-capable upstream model** is not required for the v0.2 tag; tag gating uses stub-tests. A live validation report is post-tag follow-up.

## Validation

Run from `/Users/ahsadin/Documents/AGIF-XCore`:

```bash
.venv/bin/python -m pytest tests -q
.venv/bin/python -m pytest tests/unit/test_proxy_server.py::OpenClawToolGovernanceTests -q
.venv/bin/python -m pytest tests/unit/test_backends_openai_compat.py::CompleteToolsPassthroughTests -q
.venv/bin/python -m agif_xcore serve --help        # confirm --tool-allowlist is listed
```

Expected: 316 passed, 6 skipped. The +14 over v0.1's 302 are 10 new governance tests in `OpenClawToolGovernanceTests` plus 4 backend tests covering tool passthrough.

## Live validation (post-tag follow-up)

When a tool-capable upstream model is available (e.g. `qwen2.5-coder:7b`, `llama3.1:8b`):

1. Pull the model: `ollama pull qwen2.5-coder:7b`
2. Start AGIF Governor with `--tool-allowlist search,fetch` against the new upstream.
3. Send a tool-bearing request with `tools[]` containing one allowed tool and one denied tool.
4. Confirm:
   - The allowed tool's `tool_calls` reach the client.
   - A `tool_blocked` audit event lands in the trace file when the denied tool is requested.
   - Trace ids match between response and audit event.

Capture the result in `docs/openclaw_v0_2_live_validation.md`.
