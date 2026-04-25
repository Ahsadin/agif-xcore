"""`agif-xcore` CLI entry point.

Dispatches to subcommands. M1 ships ``ask`` only; ``replay`` and
``serve`` land in later milestones.
"""

from __future__ import annotations

import argparse
import sys

from .. import __version__
from .ask import add_ask_parser
from .serve import add_serve_parser


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agif-xcore",
        description=(
            "A model-agnostic governance sidecar for LLMs. "
            "Wraps any OpenAI-compatible backend and emits a replayable "
            "trace per turn."
        ),
    )
    parser.add_argument("--version", action="version", version=f"agif-xcore {__version__}")
    subparsers = parser.add_subparsers(dest="command", metavar="command")
    subparsers.required = True
    add_ask_parser(subparsers)
    add_serve_parser(subparsers)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    func = getattr(args, "func", None)
    if func is None:
        parser.print_help()
        return 1
    try:
        return int(func(args))
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
