"""Unit tests for the CLI parser.

We don't exercise the real backend here — that belongs in the
integration test. These tests only verify that the parser shape, exit
codes, and error paths behave sensibly.
"""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from agif_xcore.cli.main import build_parser, main


class ParserShapeTests(unittest.TestCase):
    def test_version_flag_exits_cleanly(self) -> None:
        parser = build_parser()
        with self.assertRaises(SystemExit) as ctx:
            parser.parse_args(["--version"])
        self.assertEqual(ctx.exception.code, 0)

    def test_ask_without_prompt_is_rejected(self) -> None:
        parser = build_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["ask", "--model", "gemma3:270m"])

    def test_ask_without_model_is_rejected(self) -> None:
        parser = build_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["ask", "what is bm25?"])

    def test_ask_accepts_minimal_args(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["ask", "hi", "--model", "gemma3:270m"])
        self.assertEqual(args.prompt, "hi")
        self.assertEqual(args.model, "gemma3:270m")
        self.assertEqual(args.backend, "ollama")
        self.assertEqual(args.temperature, 0.0)


class MainEntrypointTests(unittest.TestCase):
    def test_main_prints_help_with_no_args(self) -> None:
        # argparse subparsers.required=True means no-args triggers an
        # error exit; use explicit -h to verify help output.
        buffer = io.StringIO()
        with self.assertRaises(SystemExit) as ctx:
            with redirect_stdout(buffer):
                main(["-h"])
        self.assertEqual(ctx.exception.code, 0)
        self.assertIn("agif-xcore", buffer.getvalue())

    def test_unknown_backend_prints_error(self) -> None:
        err = io.StringIO()
        with redirect_stderr(err):
            code = main(
                [
                    "ask",
                    "hello",
                    "--backend",
                    "doesnotexist",
                    "--model",
                    "whatever",
                ]
            )
        self.assertEqual(code, 2)
        self.assertIn("error", err.getvalue())


if __name__ == "__main__":
    unittest.main()
