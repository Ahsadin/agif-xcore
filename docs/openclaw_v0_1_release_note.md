# AGIF Governor for OpenClaw — v0.1 Adapter MVP Release Note

**Date:** 2026-04-25
**Component:** `agif-xcore serve --openclaw-profile`
**Adapter name:** AGIF-Claw Adapter
**Status:** v0.1 adapter MVP — validated against real OpenClaw client.

## What v0.1 is

A locked-down OpenClaw profile inside the existing AGIF-XCore OpenAI-compatible proxy. When `--openclaw-profile` is set, the proxy serves a single model id, disables memory, fails closed on tool/function payloads, drops wildcard CORS, and supports an optional bearer token read from an env var. All fail-closed events are appended to the trace JSONL as `openclaw_profile_event_v1` audit records.

## What v0.1 is NOT

- **Not a tool/action governance layer.** Tool execution / function-calling governance is explicitly out of scope. The proxy refuses any request that carries `tools`, `tool_choice` (other than `"none"`), `functions`, `function_call` (other than `"none"`), `role: "tool"` messages, or non-empty `tool_calls`.
- **Not a truth-quality benchmark release.** The validation is for the integration contract — protocol compatibility, fail-closed correctness, trace fidelity, no-secret invariants — not for whether the upstream model produces truthful answers. With the 270M test model and no grounding corpus, several validation prompts produced wrong answers; that is a model-quality artifact, faithfully relayed by the proxy.
- **Not a release of OpenClaw itself.** OpenClaw is a third-party product. v0.1 only validates the AGIF Governor adapter against OpenClaw 2026.4.22.
- **Not a streaming-tested release.** The single-event SSE fallback exists but was not exercised through OpenClaw's `infer model run` path.

## What passed

### 1. Curl smoke (local, loopback)

Recorded in [openclaw_mvp_smoke_results.md](openclaw_mvp_smoke_results.md). Six raw curl probes — `/health`, `/v1/models`, valid chat, wrong model id, tool payload, `stream=true` — all returned the expected shapes. Trace file received governed turns and fail-closed audit events with matching trace ids; zero secret strings in artifacts.

### 2. Real-client 10-prompt OpenClaw validation

Recorded in [openclaw_10_prompt_results.md](openclaw_10_prompt_results.md). Ten prompts across simple math, factual, short explanation, contradiction, should-abstain, instruction-following, date / current-info, reasoning, safety boundary, and repeatability classes. All ten OpenClaw calls returned `ok: true`; all ten user-visible outputs carried the AGIF footer; all ten trace ids started with `turn_` (zero `refusal-*`); the trace file held ten full `TraceEnvelope` records. Zero `tool_refusal`, `model_mismatch`, or `auth_failure` events. Max prompt-token count was 46, proving no 23k-character agent-bootstrap blob entered the request — i.e. the `tools.deny: ["*"]` workaround held.

### 3. Token-authenticated smoke

Recorded as the addendum in [openclaw_10_prompt_results.md](openclaw_10_prompt_results.md). Three real OpenClaw prompts under `--proxy-api-key-env AGIF_GOVERNOR_KEY` with the OpenClaw provider's `apiKey` set to an env-backed reference (`{source: env, provider: default, id: AGIF_GOVERNOR_KEY}`). All three returned `ok: true`; `/health` reported `auth_enabled: true`; trace file lines confirm the three turn ids; zero `auth_failure` audit events. No literal token value appeared in the OpenClaw config, the proxy banner, the trace file, or any captured output.

## Exact scope

- **Adapter type:** chat inference adapter only — `POST /v1/chat/completions` and `GET /v1/models` (plus `GET /health`).
- **Validated client:** OpenClaw 2026.4.22 (npm package, GitHub `openclaw/openclaw`).
- **OpenClaw call surface used:** `openclaw infer model run --local --json --model agif/agif-governor/gemma3-270m --prompt "<text>"`. (`openclaw agent --local` injects tool schemas and is incompatible with this MVP without `tools.deny: ["*"]`.)
- **Tools:** disabled at the OpenClaw config layer with `tools.deny: ["*"]`. Empty `tools.allow` does NOT prevent injection in OpenClaw 2026.4.22; this is documented in [openclaw.md](openclaw.md).
- **Tool / action governance:** **not in v0.1.** Verified via a live tool-payload curl (returned the fail-closed refusal and `reason_code: tools_present`).
- **Truth-quality benchmark:** **no claim.** Several validation prompts produced wrong model answers; the substrate did not reclassify them because no grounding corpus was attached. v0.1 makes no statement about hallucination reduction or factual accuracy.

## Test coverage

- **302 unit tests** pass (6 skipped). The +1 over the pre-v0.1 baseline of 301 is `OpenClawAuthTests.test_v0_1_no_secret_regression_trace_body_and_stderr`, which locks the no-secret invariant across three surfaces (trace JSONL, HTTP error body, captured stderr) using a distinctive fake token plus the configured server secret. Any future regression that leaks a token to any of those surfaces will fail this test.

## Known limits

- Tool execution / function-call governance is **not** part of v0.1.
- Streaming end-to-end through OpenClaw was not exercised; the proxy's single-event SSE fallback remains unchanged.
- Validation upstream model is `gemma3:270m-it-fp16`. Larger upstream models or attached grounding would change substrate decisions; that is future evaluation work, not adapter work.
- OpenClaw was not network-exposed. `--unsafe-bind` was not exercised live; coverage is via `OpenClawCliValidatorTests`.
- AGIF-XCore is not currently a git repo on the validation host. Tagging is deferred per operator decision.

## Files of record

- `src/agif_xcore/proxy/server.py` — OpenClaw profile handler, audit logging, fail-closed paths
- `src/agif_xcore/cli/serve.py` — CLI flags + validator
- `tests/unit/test_proxy_server.py` — 30+ OpenClaw-profile tests, including the v0.1 no-secret regression test
- `docs/openclaw.md` — operator-facing adapter documentation
- `docs/openclaw_mvp_smoke_results.md` — curl-smoke validation evidence
- `docs/openclaw_10_prompt_results.md` — real-client + authenticated-smoke validation evidence
- `docs/openclaw_v0_1_release_note.md` — this note

No external repos (`AGIF-X1`, `AGIF-XCore-R1`, `AGIFCore`, `Codex/AGIF-CellPOS`) were touched in any phase of v0.1.

## Tag intent

When AGIF-XCore is initialized as a git repo, the matching tag for this work is `v0.1-openclaw-adapter` on the commit that includes the files above and the v0.1 regression test. Until that initialization happens, this note is the canonical milestone marker.
