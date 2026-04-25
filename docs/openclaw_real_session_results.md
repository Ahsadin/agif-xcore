# OpenClaw Real-Session Validation — Blocked

**Date:** 2026-04-23
**Status:** **Blocked.** OpenClaw is not installed on this machine. Per task constraints ("do not install without confirmation"; "stop and report if OpenClaw install/config requires account login, private token, or destructive changes"), no install was attempted and no real session was run.

## OpenClaw installed / configured status

**Not installed. Not configured.**

Verified absent by:

| Check | Result |
|---|---|
| `which openclaw / open-claw / nemoclaw / nemo-claw / openshell` | all unresolved |
| `/Applications`, `~/Applications` | no matching bundle |
| Homebrew casks and formulas | no match |
| `npm list -g`, `pipx list` | no match |
| `docker ps -a`, `docker images` | docker not running; no matching image |
| Listening TCP ports near common chat UIs (3000, 3001, 5173, 8080, 8081, 8082, 3080, 5000, 7860, 8000) | only macOS Control Center on 5000 and ollama on 11434 |
| `find ~ -maxdepth 4 -iname '*openclaw*'` | no match |
| `grep -ri openclaw /Users/ahsadin/Documents` | matches only inside AGIF-XCore itself (files authored in this workstream) and an unrelated huggingface_hub agent-detector |

No provider config file exists because there is no OpenClaw installation.

## AGIF Governor command (prepared, NOT run)

The command specified for this validation step:

```
.venv/bin/python -m agif_xcore serve \
  --backend ollama \
  --model gemma3:270m-it-fp16 \
  --served-model-id agif-governor/gemma3-270m \
  --openclaw-profile \
  --trace-visibility both \
  --trace-file /tmp/openclaw_agif_real_session.jsonl
```

It was **not started**. Starting it without a real client would just repeat the curl smoke run already documented in `docs/openclaw_mvp_smoke_results.md`. The trace file `/tmp/openclaw_agif_real_session.jsonl` does not exist.

## Provider settings (prepared, NOT applied)

If and when OpenClaw is installed, the provider settings per `docs/openclaw.md` are:

- Provider id: `agif-governor`
- Base URL: `http://127.0.0.1:8088/v1`
- Model: `agif-governor/gemma3-270m`
- Streaming: disabled
- Fallback models: none
- Tool execution: disabled
- Model switching: disabled (if configurable)

No config file on disk was changed.

## 10-prompt pass/fail table

| # | Prompt class | Status |
|---|---|---|
| 1 | simple factual question | NOT RUN — OpenClaw absent |
| 2 | unsupported / current-data question | NOT RUN — OpenClaw absent |
| 3 | contradiction question | NOT RUN — OpenClaw absent |
| 4 | tool-like request ("delete a file") | NOT RUN — OpenClaw absent |
| 5 | multi-turn follow-up | NOT RUN — OpenClaw absent |
| 6 | factual + short | NOT RUN — OpenClaw absent |
| 7 | factual + ambiguous | NOT RUN — OpenClaw absent |
| 8 | tool-like request ("send an email") | NOT RUN — OpenClaw absent |
| 9 | unsupported / numeric claim | NOT RUN — OpenClaw absent |
| 10 | multi-turn continuation | NOT RUN — OpenClaw absent |

0 of 10 real prompts executed.

## Trace file

- Planned path: `/tmp/openclaw_agif_real_session.jsonl`
- Actual state: file does not exist (proxy was not started)
- Trace ids observed: none

## Failures and limitations

- **Primary blocker:** OpenClaw is not installed. Every local discovery check returned no match.
- **Canonical install source unverified.** A web search surfaced candidate URLs (`openclaw.ai`, `github.com/openclaw/openclaw`, plus several third-party "2026 setup guide" pages on low-reputation domains). I did not fetch, trust, or execute any install instructions from them. Several red flags: multiple SEO-oriented tutorial pages with identical structure, and the feature descriptions returned by the search ("local-first gateway for sessions, channels, tools, and events" across dozens of messaging platforms) do not match the minimal "OpenAI-compatible chat UI" definition you used in the plan. I am not willing to install code on your machine from a source I cannot authenticate against your own intent.
- **Task constraints honored.** Per this task's rules I did not install anything, did not create accounts, did not fetch tokens, and did not make any destructive or network-exposing changes.
- **No source code changes.** `src/agif_xcore/**` and `tests/**` are untouched this turn. Previous proxy and OpenClaw-profile tests still pass at the state reported earlier (`301 passed, 6 skipped`).
- **External repos untouched.** AGIF-X1, AGIF-XCore-R1, AGIFCore, and AGIF-CellPOS status unchanged.

## Recommendation

**NOT READY for a token-authenticated OpenClaw run** until the client exists and is pointed at the proxy. The MVP on the server side remains validated by unit tests and the earlier loopback curl smoke — what's missing is the actual OpenClaw client. Two reasonable next options, your pick:

1. **Confirm the canonical OpenClaw source.** Point me at the exact install URL or repo you intend to use (e.g., confirm whether `github.com/openclaw/openclaw` is the correct project or send me the binary/installer). Once you confirm, I can (a) show you the specific install and config commands for review, and (b) run them only after you approve.
2. **Substitute a verified OSS chat UI for MVP validation.** If the goal is to exercise the proxy end-to-end through a real OpenAI-compatible client, a known-good OSS chat UI (Open WebUI, LibreChat, Chatbox, Jan, etc.) would give the same signal. This would validate the proxy against real client behavior without depending on an unverified product. Note in the record that the adapter's OpenClaw-specific wording is unchanged, but the real client used was a substitute.

Either path will let us produce a genuine 10-prompt trace. Right now the honest answer is: the server MVP is good; a real-client validation has not yet happened.

## Files created this turn

- `docs/openclaw_real_session_results.md` (this file)

No source, test, or configuration files were modified.
