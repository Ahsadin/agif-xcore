"""Tool-call policy bundle for the OpenClaw profile (v0.3).

Owns the JSON policy-bundle schema, parsing, and per-tool / per-argument
decision logic in one small module so the proxy, the client, and the CLI
can all import the same helpers.

Lives in ``policies/`` (not ``proxy/``) on purpose: ``client.py`` consumes
this module and the client layer must not depend on the proxy layer.

JSON bundle shape (``schema_version: "openclaw_tool_policy_v1"``)::

    {
      "schema_version": "openclaw_tool_policy_v1",
      "default": "block",                 # allow | soften | block; default block
      "tools": {
        "search":      {"decision": "allow"},
        "fetch":       {"decision": "allow"},
        "write_file":  {"decision": "soften", "reason": "writes user files"},
        "delete_file": {"decision": "block",  "reason": "destructive"},
        "exec": {
          "decision": "allow",
          "argument_deny_patterns": {
            "command": "rm\\\\s+-rf|sudo"
          }
        }
      }
    }

Safety contract (stdlib ``re`` has no timeout):

- Only string-typed argument values are inspected. Non-strings (lists,
  dicts, ints, floats, bools, None) are skipped — they cannot match a
  deny pattern in v0.3.
- String values longer than :data:`MAX_ARGUMENT_VALUE_CHARS` (default
  ``4096``) are blocked **without running the regex**, with
  ``reason_code="argument_value_too_long"``. Conservative fail-closed
  behaviour beats hanging the proxy on a pathological pattern.
- Argument paths are dot-separated keys only. Paths containing ``[`` or
  ``]`` are rejected at policy load time.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Sequence


SCHEMA_VERSION = "openclaw_tool_policy_v1"

ALLOWED_DECISIONS = frozenset({"allow", "soften", "block"})

# Maximum string length that the regex inspector will run against. Any
# longer value is blocked without invoking the regex. Conservative fail
# closed: stdlib ``re`` has no timeout.
MAX_ARGUMENT_VALUE_CHARS = 4096


# ---------------------------------------------------------------------------
# Frozen dataclasses describing the policy
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ArgumentDenyPattern:
    """One compiled deny pattern for a single argument path."""

    argument_path: str
    deny_regex: re.Pattern[str]
    pattern_id: str  # short stable hash of the regex source


@dataclass(frozen=True)
class ToolDecision:
    """Operator decision for one tool."""

    name: str
    decision: str  # "allow" | "soften" | "block"
    reason: str | None = None
    argument_deny_patterns: tuple[ArgumentDenyPattern, ...] = ()


@dataclass(frozen=True)
class ArgumentDenial:
    """One argument-pattern denial recorded after the substrate runs."""

    tool_name: str
    argument_path: str
    pattern_id: str
    reason_code: str  # "argument_pattern_match" | "argument_value_too_long"

    def to_dict(self) -> dict[str, str]:
        return {
            "tool_name": self.tool_name,
            "argument_path": self.argument_path,
            "pattern_id": self.pattern_id,
            "reason_code": self.reason_code,
        }


@dataclass(frozen=True)
class ToolPolicy:
    """Loaded, validated, and pattern-compiled tool policy."""

    schema_version: str
    default: str  # "allow" | "soften" | "block"
    tools: Mapping[str, ToolDecision] = field(default_factory=dict)

    # ---- decisions ----

    def decide(self, tool_name: str) -> ToolDecision:
        """Return the per-tool decision, or a synthetic one with the default."""
        td = self.tools.get(tool_name)
        if td is not None:
            return td
        return ToolDecision(name=tool_name, decision=self.default, reason=None)

    def evaluate_arguments(
        self, tool_name: str, arguments: dict | str | None
    ) -> list[ArgumentDenial]:
        """Run argument-deny patterns for one proposed tool_call.

        ``arguments`` can be a dict (already parsed) or a JSON string (the
        OpenAI ``tool_calls[].function.arguments`` shape). Anything else
        (None, malformed JSON, non-dict after parse) yields ``[]`` — no
        inspection. The regex never runs against malformed input.
        """
        td = self.tools.get(tool_name)
        if td is None or not td.argument_deny_patterns:
            return []

        parsed: Any = arguments
        if isinstance(arguments, str):
            try:
                parsed = json.loads(arguments)
            except json.JSONDecodeError:
                return []
        if not isinstance(parsed, dict):
            return []

        denials: list[ArgumentDenial] = []
        for pat in td.argument_deny_patterns:
            value = _resolve_argument_path(parsed, pat.argument_path)
            if not isinstance(value, str):
                continue
            if len(value) > MAX_ARGUMENT_VALUE_CHARS:
                denials.append(
                    ArgumentDenial(
                        tool_name=tool_name,
                        argument_path=pat.argument_path,
                        pattern_id=pat.pattern_id,
                        reason_code="argument_value_too_long",
                    )
                )
                continue
            if pat.deny_regex.search(value):
                denials.append(
                    ArgumentDenial(
                        tool_name=tool_name,
                        argument_path=pat.argument_path,
                        pattern_id=pat.pattern_id,
                        reason_code="argument_pattern_match",
                    )
                )
        return denials


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def load_tool_policy(path: str | Path) -> ToolPolicy:
    """Read a JSON bundle from disk and return a validated :class:`ToolPolicy`.

    Raises ``ValueError`` on any schema or pattern problem; raises
    ``FileNotFoundError`` if ``path`` does not exist.
    """
    p = Path(path)
    raw = p.read_text(encoding="utf-8")
    try:
        bundle = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"tool policy file {p} is not valid JSON: {exc}") from exc
    return _build_tool_policy(bundle, source=str(p))


def tool_policy_from_allowlist(names: Sequence[str]) -> ToolPolicy:
    """Backward-compat sugar for v0.2's ``--tool-allowlist``.

    Returns a policy with ``default="block"`` and one entry per name with
    ``decision="allow"``. No argument deny patterns.
    """
    cleaned: list[str] = []
    for n in names:
        if isinstance(n, str) and n and n not in cleaned:
            cleaned.append(n)
    tools = {
        name: ToolDecision(name=name, decision="allow", reason=None)
        for name in cleaned
    }
    return ToolPolicy(
        schema_version=SCHEMA_VERSION,
        default="block",
        tools=tools,
    )


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------


def _build_tool_policy(bundle: Any, *, source: str) -> ToolPolicy:
    if not isinstance(bundle, dict):
        raise ValueError(f"tool policy {source}: top level must be a JSON object")

    sv = bundle.get("schema_version")
    if sv != SCHEMA_VERSION:
        raise ValueError(
            f"tool policy {source}: unknown schema_version {sv!r}; "
            f"expected {SCHEMA_VERSION!r}"
        )

    default = bundle.get("default", "block")
    if default not in ALLOWED_DECISIONS:
        raise ValueError(
            f"tool policy {source}: 'default' must be one of "
            f"{sorted(ALLOWED_DECISIONS)}; got {default!r}"
        )

    tools_raw = bundle.get("tools", {})
    if not isinstance(tools_raw, dict):
        raise ValueError(f"tool policy {source}: 'tools' must be an object")

    tools: dict[str, ToolDecision] = {}
    for name, entry in tools_raw.items():
        if not isinstance(name, str) or not name:
            raise ValueError(
                f"tool policy {source}: tool name must be a non-empty string"
            )
        if not isinstance(entry, dict):
            raise ValueError(
                f"tool policy {source}: tool {name!r} must map to an object"
            )
        decision = entry.get("decision")
        if decision not in ALLOWED_DECISIONS:
            raise ValueError(
                f"tool policy {source}: tool {name!r} decision must be one of "
                f"{sorted(ALLOWED_DECISIONS)}; got {decision!r}"
            )
        reason = entry.get("reason")
        if reason is not None and not isinstance(reason, str):
            raise ValueError(
                f"tool policy {source}: tool {name!r} reason must be a string"
            )
        deny_raw = entry.get("argument_deny_patterns") or {}
        if not isinstance(deny_raw, dict):
            raise ValueError(
                f"tool policy {source}: tool {name!r} argument_deny_patterns "
                f"must be an object"
            )
        deny_patterns = tuple(
            _compile_argument_deny_pattern(name, arg_path, pattern_src, source=source)
            for arg_path, pattern_src in deny_raw.items()
        )
        tools[name] = ToolDecision(
            name=name,
            decision=decision,
            reason=reason,
            argument_deny_patterns=deny_patterns,
        )

    return ToolPolicy(schema_version=sv, default=default, tools=tools)


def _compile_argument_deny_pattern(
    tool_name: str, argument_path: Any, pattern_src: Any, *, source: str
) -> ArgumentDenyPattern:
    if not isinstance(argument_path, str) or not argument_path:
        raise ValueError(
            f"tool policy {source}: tool {tool_name!r}: argument path must be "
            f"a non-empty string"
        )
    _validate_argument_path(argument_path, tool_name=tool_name, source=source)
    if not isinstance(pattern_src, str) or not pattern_src:
        raise ValueError(
            f"tool policy {source}: tool {tool_name!r} argument {argument_path!r} "
            f"deny pattern must be a non-empty string"
        )
    try:
        deny_regex = re.compile(pattern_src)
    except re.error as exc:
        raise ValueError(
            f"tool policy {source}: tool {tool_name!r} argument {argument_path!r} "
            f"deny pattern is not a valid regex: {exc}"
        ) from exc
    pattern_id = hashlib.sha256(pattern_src.encode("utf-8")).hexdigest()[:8]
    return ArgumentDenyPattern(
        argument_path=argument_path,
        deny_regex=deny_regex,
        pattern_id=pattern_id,
    )


def _validate_argument_path(
    path: str, *, tool_name: str, source: str
) -> None:
    if "[" in path or "]" in path:
        raise ValueError(
            f"tool policy {source}: tool {tool_name!r}: argument path contains "
            f"array index syntax which is not supported in v0.3: {path!r}"
        )
    parts = path.split(".")
    if any(not seg for seg in parts):
        raise ValueError(
            f"tool policy {source}: tool {tool_name!r}: argument path is malformed "
            f"(empty segment): {path!r}"
        )


def _resolve_argument_path(args: dict, path: str) -> Any:
    """Walk a dot-path into a dict by keys only. Returns None if missing."""
    cur: Any = args
    for part in path.split("."):
        if not isinstance(cur, dict):
            return None
        if part not in cur:
            return None
        cur = cur[part]
    return cur


__all__ = [
    "ALLOWED_DECISIONS",
    "ArgumentDenial",
    "ArgumentDenyPattern",
    "MAX_ARGUMENT_VALUE_CHARS",
    "SCHEMA_VERSION",
    "ToolDecision",
    "ToolPolicy",
    "load_tool_policy",
    "tool_policy_from_allowlist",
]
