"""Unit tests for ``agif_xcore.policies.tool_policy`` (v0.3)."""

from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from agif_xcore.policies.tool_policy import (
    ALLOWED_DECISIONS,
    MAX_ARGUMENT_VALUE_CHARS,
    SCHEMA_VERSION,
    ArgumentDenial,
    ToolPolicy,
    load_tool_policy,
    tool_policy_from_allowlist,
)


class _Tmpfile:
    """Tiny context manager for a JSON tempfile so each test gets a fresh path."""

    def __init__(self, payload: dict) -> None:
        self._payload = payload
        self._tmp: tempfile.NamedTemporaryFile | None = None

    def __enter__(self) -> Path:
        self._tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8",
        )
        json.dump(self._payload, self._tmp)
        self._tmp.flush()
        self._tmp.close()
        return Path(self._tmp.name)

    def __exit__(self, *_exc: object) -> None:
        if self._tmp is not None:
            try:
                Path(self._tmp.name).unlink()
            except FileNotFoundError:
                pass


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------


class LoadToolPolicyTests(unittest.TestCase):
    def test_load_tool_policy_minimal_valid_bundle(self) -> None:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "default": "block",
            "tools": {
                "search": {"decision": "allow"},
                "delete_file": {"decision": "block", "reason": "destructive"},
            },
        }
        with _Tmpfile(payload) as p:
            policy = load_tool_policy(p)
        self.assertEqual(policy.schema_version, SCHEMA_VERSION)
        self.assertEqual(policy.default, "block")
        self.assertEqual(set(policy.tools.keys()), {"search", "delete_file"})
        self.assertEqual(policy.tools["search"].decision, "allow")
        self.assertEqual(policy.tools["delete_file"].decision, "block")
        self.assertEqual(policy.tools["delete_file"].reason, "destructive")

    def test_load_tool_policy_rejects_unknown_schema_version(self) -> None:
        payload = {"schema_version": "openclaw_tool_policy_v99", "tools": {}}
        with _Tmpfile(payload) as p:
            with self.assertRaises(ValueError) as ctx:
                load_tool_policy(p)
        self.assertIn("schema_version", str(ctx.exception))

    def test_load_tool_policy_rejects_bad_decision_value(self) -> None:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "tools": {"search": {"decision": "maybe"}},
        }
        with _Tmpfile(payload) as p:
            with self.assertRaises(ValueError) as ctx:
                load_tool_policy(p)
        self.assertIn("decision", str(ctx.exception))
        self.assertIn("maybe", str(ctx.exception))

    def test_load_tool_policy_compiles_argument_deny_patterns(self) -> None:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "default": "allow",
            "tools": {
                "exec": {
                    "decision": "allow",
                    "argument_deny_patterns": {
                        "command": r"rm\s+-rf|sudo",
                    },
                },
            },
        }
        with _Tmpfile(payload) as p:
            policy = load_tool_policy(p)
        td = policy.tools["exec"]
        self.assertEqual(len(td.argument_deny_patterns), 1)
        pat = td.argument_deny_patterns[0]
        self.assertEqual(pat.argument_path, "command")
        self.assertIsInstance(pat.deny_regex, re.Pattern)
        self.assertEqual(len(pat.pattern_id), 8)

    def test_load_tool_policy_rejects_invalid_regex(self) -> None:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "tools": {
                "exec": {
                    "decision": "allow",
                    "argument_deny_patterns": {"command": "[unterminated"},
                },
            },
        }
        with _Tmpfile(payload) as p:
            with self.assertRaises(ValueError) as ctx:
                load_tool_policy(p)
        self.assertIn("regex", str(ctx.exception).lower())

    def test_load_tool_policy_rejects_array_index_path(self) -> None:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "tools": {
                "exec": {
                    "decision": "allow",
                    "argument_deny_patterns": {"args[0]": "rm"},
                },
            },
        }
        with _Tmpfile(payload) as p:
            with self.assertRaises(ValueError) as ctx:
                load_tool_policy(p)
        msg = str(ctx.exception)
        self.assertIn("array index", msg)
        self.assertIn("args[0]", msg)


# ---------------------------------------------------------------------------
# Decisions and argument evaluation
# ---------------------------------------------------------------------------


def _policy(payload: dict) -> ToolPolicy:
    """Inline-build a ToolPolicy from a JSON-shaped dict via load_tool_policy."""
    with _Tmpfile(payload) as p:
        return load_tool_policy(p)


class ToolPolicyDecisionTests(unittest.TestCase):
    def test_decide_returns_default_for_unknown_tool(self) -> None:
        policy = _policy({
            "schema_version": SCHEMA_VERSION,
            "default": "soften",
            "tools": {"search": {"decision": "allow"}},
        })
        td = policy.decide("unknown_tool")
        self.assertEqual(td.decision, "soften")
        self.assertEqual(td.name, "unknown_tool")

    def test_evaluate_arguments_top_level_match(self) -> None:
        policy = _policy({
            "schema_version": SCHEMA_VERSION,
            "default": "block",
            "tools": {
                "exec": {
                    "decision": "allow",
                    "argument_deny_patterns": {
                        "command": r"rm\s+-rf",
                    },
                },
            },
        })
        denials = policy.evaluate_arguments(
            "exec", json.dumps({"command": "rm -rf /tmp/foo"}),
        )
        self.assertEqual(len(denials), 1)
        d = denials[0]
        self.assertIsInstance(d, ArgumentDenial)
        self.assertEqual(d.tool_name, "exec")
        self.assertEqual(d.argument_path, "command")
        self.assertEqual(d.reason_code, "argument_pattern_match")

    def test_evaluate_arguments_dot_path_into_nested_dict(self) -> None:
        policy = _policy({
            "schema_version": SCHEMA_VERSION,
            "tools": {
                "request": {
                    "decision": "allow",
                    "argument_deny_patterns": {
                        "options.url": r"file://",
                    },
                },
            },
        })
        denials = policy.evaluate_arguments(
            "request",
            json.dumps({"options": {"url": "file:///etc/passwd"}}),
        )
        self.assertEqual(len(denials), 1)

    def test_evaluate_arguments_skips_non_string_values(self) -> None:
        policy = _policy({
            "schema_version": SCHEMA_VERSION,
            "tools": {
                "exec": {
                    "decision": "allow",
                    "argument_deny_patterns": {"command": "rm"},
                },
            },
        })
        # Argument is an integer, not a string. v0.3 must skip silently.
        denials = policy.evaluate_arguments(
            "exec", json.dumps({"command": 42}),
        )
        self.assertEqual(denials, [])

    def test_evaluate_arguments_blocks_value_over_max_chars_without_running_regex(self) -> None:
        # A pathological regex that would catastrophically backtrack on a long
        # input; if the safety limit didn't fire, the test would hang. The
        # limit must fire BEFORE the regex is evaluated.
        policy = _policy({
            "schema_version": SCHEMA_VERSION,
            "tools": {
                "exec": {
                    "decision": "allow",
                    "argument_deny_patterns": {
                        "command": r"(a+)+b",  # catastrophic-backtracking regex
                    },
                },
            },
        })
        long_value = "a" * (MAX_ARGUMENT_VALUE_CHARS + 1)
        denials = policy.evaluate_arguments(
            "exec", json.dumps({"command": long_value}),
        )
        self.assertEqual(len(denials), 1)
        self.assertEqual(denials[0].reason_code, "argument_value_too_long")

    def test_evaluate_arguments_no_denials_when_pattern_does_not_match(self) -> None:
        policy = _policy({
            "schema_version": SCHEMA_VERSION,
            "tools": {
                "exec": {
                    "decision": "allow",
                    "argument_deny_patterns": {"command": r"rm\s+-rf"},
                },
            },
        })
        denials = policy.evaluate_arguments(
            "exec", json.dumps({"command": "ls -la"}),
        )
        self.assertEqual(denials, [])


# ---------------------------------------------------------------------------
# v0.2 sugar: tool_policy_from_allowlist
# ---------------------------------------------------------------------------


class FromAllowlistTests(unittest.TestCase):
    def test_tool_policy_from_allowlist_matches_v0_2_behaviour(self) -> None:
        policy = tool_policy_from_allowlist(["search", "fetch", "search"])
        self.assertEqual(policy.default, "block")
        self.assertEqual(set(policy.tools.keys()), {"search", "fetch"})
        for td in policy.tools.values():
            self.assertEqual(td.decision, "allow")
        self.assertEqual(policy.decide("not_listed").decision, "block")

    def test_tool_policy_from_allowlist_handles_empty(self) -> None:
        policy = tool_policy_from_allowlist([])
        self.assertEqual(policy.default, "block")
        self.assertEqual(policy.tools, {})


# ---------------------------------------------------------------------------
# Sanity
# ---------------------------------------------------------------------------


class ConstantsTests(unittest.TestCase):
    def test_allowed_decisions_set(self) -> None:
        self.assertEqual(
            ALLOWED_DECISIONS, frozenset({"allow", "soften", "block"}),
        )


if __name__ == "__main__":
    unittest.main()
