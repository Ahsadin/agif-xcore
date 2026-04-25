# AGIF-XCore Repo Rules

## Purpose

`AGIF-XCore` is a reusable Python library and proxy for governed LLM calls.
It is not a phase-driven planning repo and it is not a benchmark theater repo.

## Read Before Work

Read these files before making changes:

1. `README.md`
2. `docs/architecture.md`
3. `docs/policies.md`
4. `docs/schemas.md`
5. `docs/openclaw.md` (when touching proxy `--openclaw-profile` behavior)
6. `pyproject.toml`

Then read the specific code and tests for the area you are changing.

## Core Rules

- Keep changes small and easy to review.
- Do not restructure folders unless explicitly asked.
- Keep the core package usable with zero required runtime dependencies.
- Optional integrations must stay behind optional extras.
- Do not claim a backend, CLI command, policy bundle, or feature unless it is actually implemented.
- Do not add benchmark-specific shortcuts or hardcoded answer paths.
- Do not edit benchmark result files unless you are intentionally rerunning the benchmark and documenting that change.
- Keep traces, schemas, and replay behavior honest and deterministic.

## Code And Test Rules

- Update tests with code changes when behavior changes.
- Prefer simple, standard-library-first solutions.
- Avoid new dependencies unless there is a clear need.
- Keep public API changes backward-compatible when possible, or document them clearly when not.
- Do not commit `__pycache__` or other generated artifacts as source changes.

## Documentation Rules

- Keep README and docs aligned with the real implementation.
- If a feature is partial, say so plainly.
- Use predictable file names and simple language.

