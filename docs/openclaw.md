# AGIF Governor for OpenClaw (v0.1 Adapter MVP)

**Product name:** AGIF Governor for OpenClaw
**Adapter name:** AGIF-Claw Adapter
**Status:** v0.1 adapter MVP — validated against OpenClaw 2026.4.22 for chat governance only. Tool / action governance is out of scope in this release.

## What it does

`agif-xcore serve --openclaw-profile` is the existing OpenAI-compatible proxy locked down for safe use behind OpenClaw:

- Exactly one served model id is advertised on `/v1/models`.
- Any `/v1/chat/completions` request whose body `model` differs from the served id gets a `404 model_not_found`.
- Any request carrying tool/function-call intent fails closed with a fixed assistant refusal message.
- Cross-turn memory is force-disabled (no `memory_enabled=True` accepted).
- `Access-Control-Allow-Origin: *` is not emitted.
- An optional bearer token (read from an env var) is required on `/v1/*`.
- All fail-closed events are appended to the trace JSONL as `openclaw_profile_event_v1` audit records.

## MVP promise

OpenClaw can route chat replies through AGIF-XCore governance and receive governed answers plus trace records.

**Not in v0.1:** tool execution, function calling, model switching, NemoClaw/OpenShell, true token streaming, network-exposed deployment, opt-in memory.

**v0.2 adds:** named tool-call governance via the substrate's action_gate stage. See [openclaw_v0_2.md](openclaw_v0_2.md).

**v0.3 adds:** the substrate's `soften` decision now lets `tool_calls` pass through with a flagged audit trail; per-tool argument inspection via stdlib regex deny patterns; and a JSON `--tool-policy-file` for declarative per-tool decisions. See [openclaw_v0_3.md](openclaw_v0_3.md). Tool *execution* remains a non-goal — the proxy never executes a tool itself.

Validation records:

- [openclaw_mvp_smoke_results.md](openclaw_mvp_smoke_results.md) (v0.1 curl smoke)
- [openclaw_10_prompt_results.md](openclaw_10_prompt_results.md) (v0.1 + auth addendum)
- [openclaw_v0_1_release_note.md](openclaw_v0_1_release_note.md) (v0.1 release note)
- [openclaw_v0_2.md](openclaw_v0_2.md) (v0.2 contract + validation)
- [openclaw_v0_3.md](openclaw_v0_3.md) (v0.3 contract + validation)

## Threat model

- Default bind: `127.0.0.1` loopback only. `--unsafe-bind` required to bind elsewhere.
- No wildcard CORS. Add an explicit allowlist later if you need browser origins.
- Bearer auth is optional; when enabled it guards `/v1/*`. `/health` stays open so probes and dashboards can read the profile state without a token.
- The bearer token value is never logged, never printed in the startup banner, and never echoed in audit events.

## Start the proxy

```bash
agif-xcore serve \
  --backend ollama \
  --model gemma3:270m \
  --served-model-id agif-governor/gemma3-270m \
  --openclaw-profile \
  --trace-visibility both \
  --trace-file traces/openclaw_agif.jsonl
```

With bearer auth:

```bash
export AGIF_GOVERNOR_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(32))")
agif-xcore serve \
  --backend ollama \
  --model gemma3:270m \
  --served-model-id agif-governor/gemma3-270m \
  --openclaw-profile \
  --trace-visibility both \
  --trace-file traces/openclaw_agif.jsonl \
  --proxy-api-key-env AGIF_GOVERNOR_KEY
```

### Required flags under `--openclaw-profile`

| Flag | Purpose |
|---|---|
| `--served-model-id` | The id advertised to OpenClaw; requests with a different `model` get 404. |
| `--trace-file` | JSONL sink for governance traces AND OpenClaw audit events. |
| `--governance` (default on) | Cannot be combined with `--no-governance`. |

### Optional flags

| Flag | Purpose |
|---|---|
| `--trace-visibility {metadata,footer,both}` | Where the trace pointer shows up. Default: `metadata` (only `x_agif_trace`). |
| `--proxy-api-key-env ENV_VAR` | Name of an env var holding the bearer token. The value itself is never logged. |
| `--unsafe-bind` | Required to bind to a non-loopback host. |

## OpenClaw provider config

Configure one (and only one) provider in OpenClaw pointing at the proxy.

| Setting | Value |
|---|---|
| Provider key | `agif` |
| Base URL | `http://127.0.0.1:8088/v1` |
| API type | OpenAI-compatible chat completions |
| Model | `agif-governor/gemma3-270m` |
| Streaming | **disabled** |
| Fallback models | **none** |
| Model switching | **disabled** |
| Tool execution/schema injection | **disabled with `tools.deny: ["*"]`** |

Validated minimal OpenClaw config:

```json
{
  "$schema": "https://docs.openclaw.ai/schema/openclaw.json",
  "gateway": {
    "mode": "local"
  },
  "models": {
    "mode": "replace",
    "providers": {
      "agif": {
        "baseUrl": "http://127.0.0.1:8088/v1",
        "api": "openai-completions",
        "models": [
          {
            "id": "agif-governor/gemma3-270m",
            "name": "AGIF Governor (Gemma3-270m)",
            "input": ["text"]
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "workspace": "~/.openclaw/workspace",
      "model": "agif/agif-governor/gemma3-270m",
      "models": {
        "agif/agif-governor/gemma3-270m": {}
      },
      "skills": [],
      "mediaGenerationAutoProviderFallback": false
    }
  },
  "tools": {
    "deny": ["*"]
  }
}
```

Do not use `tools.allow: []` as the tool-disable control. In OpenClaw 2026.4.22, an empty allowlist does not prevent tool schemas from reaching the model call; `tools.deny: ["*"]` is the validated workaround.

If bearer auth is enabled on the proxy, set the OpenClaw provider API key to the same env var via an env-backed secret reference. OpenClaw sends it as `Authorization: Bearer <value>`.

```json
"apiKey": {
  "source": "env",
  "provider": "default",
  "id": "AGIF_GOVERNOR_KEY"
}
```

## Verification

```bash
# /health reports profile state without secrets
curl -s http://127.0.0.1:8088/health | python -m json.tool

# Only the served model id is listed
curl -s http://127.0.0.1:8088/v1/models | python -m json.tool

# Matching served id → governed reply
curl -s http://127.0.0.1:8088/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"agif-governor/gemma3-270m","messages":[{"role":"user","content":"ping"}]}' \
  | python -m json.tool

# Wrong model id → 404 model_not_found
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8088/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"wrong-id","messages":[{"role":"user","content":"x"}]}'

# Tool payload → fail-closed 200 with refusal content
curl -s http://127.0.0.1:8088/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"agif-governor/gemma3-270m","messages":[{"role":"user","content":"x"}],"tools":[{"type":"function","function":{"name":"f"}}]}' \
  | python -m json.tool

# Trace file contains governed traces and fail-closed audit events
wc -l traces/openclaw_agif.jsonl
```

## Response shape

### Success

```json
{
  "id": "chatcmpl-turn_...",
  "object": "chat.completion",
  "created": 1714000000,
  "model": "agif-governor/gemma3-270m",
  "choices": [{
    "index": 0,
    "message": {"role": "assistant", "content": "<answer>"},
    "finish_reason": "stop"
  }],
  "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
  "x_agif_trace": {
    "trace_id": "turn_...",
    "answer_mode": "grounded_fact",
    "governance_enabled": true,
    "served_model_id": "agif-governor/gemma3-270m",
    "upstream_model_id": "gemma3:270m",
    "memory_enabled": false,
    "total_ms": 123,
    "refs": []
  }
}
```

With `--trace-visibility footer` or `both`, the assistant message ends with:

```
AGIF: mode=<answer_mode>; trace=<trace_id>
```

### Tool refusal (fail closed)

HTTP 200, OpenAI-shaped completion, `answer_mode="abstain"`, trace id prefixed `refusal-`. Content:

> AGIF Governor MVP does not execute tool or function calls. Disable tool use in your OpenClaw provider settings and retry.

### Model mismatch (fail closed)

HTTP 404, OpenAI-shaped error:

```json
{
  "error": {
    "message": "The model 'wrong-id' is not served by this proxy. Only 'agif-governor/gemma3-270m' is available.",
    "type": "invalid_request_error",
    "code": "model_not_found"
  }
}
```

### Auth failure

HTTP 401:

```json
{"error": {"message": "Missing or invalid API key.", "type": "invalid_request_error", "code": "invalid_api_key"}}
```

## Audit events

Fail-closed paths append one line to the trace file using schema `openclaw_profile_event_v1`:

```json
{
  "schema_version": "openclaw_profile_event_v1",
  "event_type": "tool_refusal",
  "trace_id": "refusal-abc123def456",
  "created": 1714000000,
  "served_model_id": "agif-governor/gemma3-270m",
  "upstream_model_id": "gemma3:270m",
  "answer_mode": "abstain",
  "reason_code": "tools_present",
  "governance_enabled": true,
  "memory_enabled": false
}
```

`event_type` ∈ `tool_refusal` | `model_mismatch` | `auth_failure`.
`reason_code` values:
- `tool_refusal`: `tools_present`, `functions_present`, `tool_choice_not_none`, `function_call_not_none`, `role_tool_in_messages`, `tool_calls_in_messages`
- `model_mismatch`: `requested_id_not_served`
- `auth_failure`: `missing_authorization_header`, `wrong_scheme`, `wrong_token`

The `trace_id` in the audit event equals the `x_agif_trace.trace_id` returned to the client for the same request.

**What is never logged:** bearer token values, API keys, full `Authorization` header contents, raw tool payloads, raw tool argument strings.

## Non-goals

- Tool / function-call **execution** or governance. Tool governance requires a native OpenClaw plugin or tool-interception support and is tracked for a later phase.
- True token streaming. The existing single-event SSE fallback remains in place; OpenClaw providers should set streaming to disabled.
- NemoClaw, OpenShell, or any front-end other than OpenClaw.
- Network-exposed deployment. Use loopback plus explicit auth and network controls.
