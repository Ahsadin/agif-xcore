"""`agif-xcore ask` — one-shot turn against a backend."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ..backends.base import BackendBlocked, BackendError, BackendModelMismatch, BackendTimeout
from ..backends.registry import available_backends
from ..client import GovernedClient
from ..schemas import pretty_json


def add_ask_parser(subparsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
    parser = subparsers.add_parser(
        "ask",
        help="Ask a backend one question and print the governed answer.",
        description=(
            "Send one prompt to a backend through the XCore pipeline and "
            "print the natural-language answer. Writes a trace JSONL to "
            "the configured sink (default: none; use --trace-file or "
            "--trace-stderr)."
        ),
    )
    parser.add_argument("prompt", help="The user prompt.")
    parser.add_argument(
        "--backend",
        default="ollama",
        help=f"Backend name. One of: {', '.join(available_backends())}. Default: ollama.",
    )
    parser.add_argument(
        "--model",
        required=True,
        help="Model id as the backend expects it (e.g. 'gemma3:270m').",
    )
    parser.add_argument("--base-url", default=None, help="Override the backend base URL.")
    parser.add_argument("--api-key", default=None, help="Optional API key for the backend.")
    parser.add_argument(
        "--model-enforcement",
        choices=("strict", "prefix", "off"),
        default="strict",
        help=(
            "How strictly to compare the returned model id to the requested one. "
            "Default: strict (returned id must equal requested)."
        ),
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature. Default: 0.0 for deterministic replay.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help="Optional max tokens for the completion.",
    )
    parser.add_argument(
        "--trace-file",
        default=None,
        help="Append a trace JSONL line to this file path.",
    )
    parser.add_argument(
        "--trace-stderr",
        action="store_true",
        help="Emit the trace JSONL to stderr as well.",
    )
    parser.add_argument(
        "--governance",
        action="store_true",
        default=False,
        help=(
            "Enable the 9-stage governance substrate. Without this flag, "
            "the raw LLM answer is returned. With it, the substrate "
            "decides the answer mode and reshapes the text. "
            "Same code path — one switch, not two arms."
        ),
    )
    parser.add_argument(
        "--grounding",
        nargs="+",
        default=None,
        metavar="PATH",
        help=(
            "One or more file or directory paths to use as grounding "
            "evidence. XCore loads them, chunks them, and retrieves the "
            "most relevant chunks for each turn via BM25."
        ),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help=(
            "Print the full answer envelope (text + trace id + timings) as "
            "JSON on stdout instead of just the answer text."
        ),
    )
    parser.set_defaults(func=_run_ask)
    return parser


def _run_ask(args: argparse.Namespace) -> int:
    try:
        client = GovernedClient(
            backend=args.backend,
            model=args.model,
            base_url=args.base_url,
            api_key=args.api_key,
            model_enforcement=args.model_enforcement,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            trace_file=Path(args.trace_file) if args.trace_file else None,
            trace_to_stderr=args.trace_stderr,
            governance_enabled=args.governance,
            grounding_paths=args.grounding,
        )
    except BackendError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    try:
        with client:
            answer = client.ask(args.prompt)
    except BackendModelMismatch as exc:
        print(f"error: model mismatch: {exc}", file=sys.stderr)
        return 4
    except BackendTimeout as exc:
        print(f"error: backend timed out: {exc}", file=sys.stderr)
        return 5
    except BackendBlocked as exc:
        print(f"error: backend blocked: {exc}", file=sys.stderr)
        return 6
    except BackendError as exc:
        print(f"error: backend failure: {exc}", file=sys.stderr)
        return 3

    if args.json:
        payload = {
            "text": answer.text,
            "trace_id": answer.trace_id,
            "total_ms": answer.total_ms,
            "answer_mode": answer.answer_mode,
            "refs": answer.refs,
        }
        print(pretty_json(payload))
    else:
        print(answer.text)
        print(f"\n[trace_id={answer.trace_id}  total_ms={answer.total_ms}]", file=sys.stderr)
    return 0
