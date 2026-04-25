# OpenClaw MVP — Smoke Validation Results

**Date:** 2026-04-23
**Scope:** AGIF Governor for OpenClaw MVP — governed chat only. Tool/action governance out of scope.
**Trace file used:** `/tmp/openclaw_agif.jsonl`
**Live Ollama used:** yes.

## Machine and context

- Working dir: `/Users/ahsadin/Documents/AGIF-XCore`
- Interpreter: `.venv/bin/python` (Python 3.14 via Homebrew)
- Platform: darwin 25.4.0 (arm64)
- Ollama: `/opt/homebrew/bin/ollama`, version `0.20.5`, daemon reachable at `127.0.0.1:11434`
- Local model: `gemma3:270m-it-fp16` (the exact tag used for M1 integration tests). The plan referenced `gemma3:270m`; that bare tag was not installed, so the `-it-fp16` variant was used as the upstream. Served id kept as `agif-governor/gemma3-270m`.
- Repos outside AGIF-XCore (`AGIF-X1`, `AGIFCore`, `AGIF-XCore-R1`, `Codex/AGIF-CellPOS`) not modified.

## Commands run

Verification:
```
.venv/bin/python -m pytest tests -q
.venv/bin/python -m agif_xcore serve --help
```

Proxy start (backgrounded):
```
.venv/bin/python -m agif_xcore serve \
  --backend ollama \
  --model gemma3:270m-it-fp16 \
  --served-model-id agif-governor/gemma3-270m \
  --openclaw-profile \
  --trace-visibility both \
  --trace-file /tmp/openclaw_agif.jsonl
```

Curl probes:
```
curl http://127.0.0.1:8088/health
curl http://127.0.0.1:8088/v1/models
curl -d '{"model":"agif-governor/gemma3-270m","messages":[{"role":"user","content":"..."}]}' \
  http://127.0.0.1:8088/v1/chat/completions
curl -d '{"model":"wrong-id","messages":[{"role":"user","content":"x"}]}' \
  http://127.0.0.1:8088/v1/chat/completions
curl -d '{"model":"agif-governor/gemma3-270m","messages":[{"role":"user","content":"x"}],"tools":[{"type":"function","function":{"name":"f"}}]}' \
  http://127.0.0.1:8088/v1/chat/completions
curl -N -d '{"model":"agif-governor/gemma3-270m","messages":[{"role":"user","content":"..."}],"stream":true}' \
  http://127.0.0.1:8088/v1/chat/completions
```

## Results

| # | Check | Expected | Observed | Pass |
|---|---|---|---|---|
| 1 | `pytest tests -q` | existing baseline plus 40 OpenClaw tests | 301 passed, 6 skipped | ✅ |
| 2 | `serve --help` | lists `--openclaw-profile`, `--served-model-id`, `--trace-visibility`, `--proxy-api-key-env`, `--unsafe-bind`; no secret values | all flags present, help text clean | ✅ |
| 3 | Ollama reachable at `127.0.0.1:11434` | daemon responds, approved model present | daemon responded, `gemma3:270m-it-fp16` listed | ✅ |
| 4 | Proxy startup banner | profile state, served/upstream ids, auth state bool only, no token | banner rendered with `auth OFF`, `host safe True`, no secrets | ✅ |
| a | `GET /health` | OpenClaw payload, no secrets | `openclaw_profile=true`, `memory_enabled=false`, `auth_enabled=false`, `host_safe=true` | ✅ |
| b | `GET /v1/models` | exactly one entry = served id | `agif-governor/gemma3-270m`, `owned_by=agif-xcore` | ✅ |
| c | `POST /v1/chat/completions` with served id | HTTP 200, OpenAI shape, footer appended, `x_agif_trace` has served+upstream+memory | HTTP 200, footer `AGIF: mode=derived_explanation; trace=turn_…`, `served_model_id`/`upstream_model_id`/`memory_enabled=false` all present | ✅ |
| d | wrong `model` | HTTP 404, `model_not_found`, names only served id | HTTP 404, `code=model_not_found`, message names only served id, `x_agif_trace.trace_id` prefixed `refusal-` | ✅ |
| e | request with `tools` | HTTP 200 refusal message, `answer_mode=abstain`, `reason_code=tools_present` | HTTP 200, expected refusal content with footer, `reason_code=tools_present` | ✅ |
| f | `stream=true` | SSE with `data:` events ending in `[DONE]`, `x_agif_trace` in final chunk | `Content-Type: text/event-stream`, two `data:` chunks, `x_agif_trace` in DONE chunk, `[DONE]` sentinel | ✅ |
| 5 | trace file present and growing | file exists, governed + audit events appended | 6 lines, 15.8 KB; every response `trace_id` found in file | ✅ |
| 6 | matching trace ids | response `x_agif_trace.trace_id` = audit event `trace_id` on fail-closed | `refusal-b2d0a54f7732` (model_mismatch) and `refusal-ec631ade3feb` (tool_refusal) found in both the response and the audit event, with `schema_version=openclaw_profile_event_v1` | ✅ |
| 7 | no secrets in artifacts | no `Bearer …` or `Authorization: …` in trace file | grep returned no matches | ✅ |
| 8 | external repos untouched | `AGIF-X1`, `AGIFCore` status unchanged vs session start | status lists are identical to pre-session (same 112-entry AGIF-X1 set of pre-existing `M` files) | ✅ |

All 14 checks: **pass**.

## Known limits (MVP)

- Auth was observed with `auth=OFF` in the smoke run. Bearer-auth correctness is covered by `OpenClawAuthTests` (4 tests) in `tests/unit/test_proxy_server.py`, not by a live curl run, to avoid writing a token anywhere on disk.
- The `gemma3:270m-it-fp16` model is small (270M params). It produced a semantically off answer ("retrieve the most frequent BM25 values…") for the BM25 prompt. That is a model-capability artifact, not a governance regression. The governance substrate correctly classified the answer as `answer_mode=derived_explanation` because no grounding corpus was attached.
- Streaming remains the existing single-event SSE fallback (one content chunk + one DONE chunk), not true token streaming.
- `host_safe` is a declarative flag for probes; non-loopback binding still requires `--unsafe-bind` at startup but the OS-level network exposure is the operator's responsibility.
- Content-length usage reporting is zeroed (`prompt_tokens/completion_tokens/total_tokens = 0`) because the 6-stage pipeline does not yet thread real token counts through to the proxy response. OpenClaw does not depend on these values; budgeting consumers would need to read trace JSONL instead.

## Files changed

- `docs/openclaw_mvp_smoke_results.md` (this file — new).

No source or test files were modified by this validation step.

## Next recommendation

The MVP is ready for a real OpenClaw configuration on the same loopback host, using the provider settings documented in `docs/openclaw.md`:

- Provider id: `agif-governor`
- Base URL: `http://127.0.0.1:8088/v1`
- Model: `agif-governor/gemma3-270m`
- Streaming: disabled
- Tool execution: disabled
- Fallback models: none
- Model switching: disabled

Suggested next step: run one real OpenClaw session against this proxy with a freshly rotated bearer token (`--proxy-api-key-env AGIF_GOVERNOR_KEY`), capture a short trace file, and confirm in post that (1) every OpenClaw chat turn has a matching `turn_*` line in the JSONL, (2) no audit event appears unexpectedly, and (3) the trace file never contains the bearer token value. After that, the MVP can be promoted to a tagged release in AGIF-XCore and documented as the first consumer of the OpenClaw profile.
