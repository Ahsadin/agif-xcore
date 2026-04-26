"""`agif-xcore serve` — run the OpenAI-compatible proxy server."""

from __future__ import annotations

import argparse
import os
import sys

from ..backends.base import BackendError
from ..backends.registry import available_backends
from ..policies.tool_policy import (
    SCHEMA_VERSION as TOOL_POLICY_SCHEMA_VERSION,
    ToolPolicy,
    load_tool_policy,
    tool_policy_from_allowlist,
)
from ..proxy.server import ProxyConfig, _is_loopback_host, build_proxy_server


def add_serve_parser(subparsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
    parser = subparsers.add_parser(
        "serve",
        help="Run an OpenAI-compatible proxy server that governs upstream calls.",
        description=(
            "Start an HTTP server on the specified port that accepts "
            "OpenAI-compatible /v1/chat/completions requests, runs them "
            "through the XCore governance pipeline, and returns "
            "OpenAI-shaped responses. Any client that speaks the OpenAI "
            "protocol (the official SDK, LangChain, llama-index, curl) "
            "can point at this server transparently."
        ),
    )
    parser.add_argument(
        "--backend",
        default="ollama",
        help=f"Upstream backend. One of: {', '.join(available_backends())}.",
    )
    parser.add_argument(
        "--model",
        required=True,
        help="Model id for the upstream backend.",
    )
    parser.add_argument("--base-url", default=None, help="Override the backend base URL.")
    parser.add_argument("--api-key", default=None, help="API key for the upstream backend.")
    parser.add_argument(
        "--model-enforcement",
        choices=("strict", "prefix", "off"),
        default="prefix",
        help="Model id enforcement mode. Default: prefix.",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind. Default: 127.0.0.1.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8088,
        help="Port to listen on. Default: 8088.",
    )
    parser.add_argument(
        "--governance",
        action="store_true",
        default=True,
        help="Enable governance (default: on). Use --no-governance to disable.",
    )
    parser.add_argument(
        "--no-governance",
        dest="governance",
        action="store_false",
        help="Disable governance — proxy passes through raw LLM answers.",
    )
    parser.add_argument(
        "--grounding",
        nargs="+",
        default=None,
        metavar="PATH",
        help="Grounding evidence paths.",
    )
    parser.add_argument(
        "--trace-file",
        default=None,
        help="Append trace JSONL to this file.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Default temperature. Default: 0.0.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help="Default max tokens.",
    )
    parser.add_argument(
        "--openclaw-profile",
        action="store_true",
        default=False,
        help=(
            "Lock the proxy down for use behind OpenClaw: single served "
            "model id, memory off, tool calls refused, wildcard CORS off, "
            "optional bearer auth. Requires --served-model-id and "
            "--trace-file."
        ),
    )
    parser.add_argument(
        "--served-model-id",
        default=None,
        help=(
            "Model id advertised by /v1/models and accepted in request "
            "bodies. Required with --openclaw-profile."
        ),
    )
    parser.add_argument(
        "--trace-visibility",
        choices=("metadata", "footer", "both"),
        default="metadata",
        help=(
            "Where to surface the AGIF trace pointer in responses. "
            "metadata: x_agif_trace only (default). footer: append a "
            "short footer to the assistant message. both: emit both."
        ),
    )
    parser.add_argument(
        "--proxy-api-key-env",
        default=None,
        metavar="ENV_VAR",
        help=(
            "Name of an env var holding a bearer token. When set, /v1/* "
            "requires 'Authorization: Bearer <value>'. The token value "
            "is never printed or logged."
        ),
    )
    parser.add_argument(
        "--unsafe-bind",
        action="store_true",
        default=False,
        help=(
            "Required when --openclaw-profile binds to a non-loopback "
            "host. Binding beyond loopback exposes the proxy; use only "
            "with explicit auth and network controls."
        ),
    )
    parser.add_argument(
        "--tool-allowlist",
        action="append",
        default=None,
        metavar="NAME[,NAME...]",
        help=(
            "v0.2 sugar: comma-separated list of tool names allowed in "
            "OpenClaw profile. Repeatable. Mutually exclusive with "
            "--tool-policy-file. Internally synthesizes a ToolPolicy with "
            "default=block."
        ),
    )
    parser.add_argument(
        "--tool-policy-file",
        default=None,
        metavar="PATH",
        help=(
            "v0.3: path to a JSON tool-policy bundle "
            f"(schema_version={TOOL_POLICY_SCHEMA_VERSION}). Declares "
            "per-tool decisions (allow/soften/block) and per-argument "
            "regex deny patterns. Mutually exclusive with --tool-allowlist."
        ),
    )
    parser.set_defaults(func=_run_serve)
    return parser


def _run_serve(args: argparse.Namespace) -> int:
    resolved_proxy_api_key: str | None = None

    if args.openclaw_profile:
        if not args.governance:
            print(
                "error: --openclaw-profile requires governance; remove --no-governance",
                file=sys.stderr,
            )
            return 2
        if not args.served_model_id:
            print(
                "error: --openclaw-profile requires --served-model-id",
                file=sys.stderr,
            )
            return 2
        if not args.trace_file:
            print(
                "error: --openclaw-profile requires --trace-file",
                file=sys.stderr,
            )
            return 2
        if not _is_loopback_host(args.host) and not args.unsafe_bind:
            print(
                "error: refusing to bind OpenClaw profile to non-loopback "
                "host without --unsafe-bind",
                file=sys.stderr,
            )
            return 2
        if args.proxy_api_key_env:
            resolved_proxy_api_key = os.environ.get(args.proxy_api_key_env)
            if not resolved_proxy_api_key:
                print(
                    f"error: env var {args.proxy_api_key_env} is unset or empty",
                    file=sys.stderr,
                )
                return 2
    else:
        if args.proxy_api_key_env:
            resolved_proxy_api_key = os.environ.get(args.proxy_api_key_env)
            if not resolved_proxy_api_key:
                print(
                    f"error: env var {args.proxy_api_key_env} is unset or empty",
                    file=sys.stderr,
                )
                return 2

    # v0.3: --tool-allowlist and --tool-policy-file are mutually exclusive.
    if args.tool_allowlist and args.tool_policy_file:
        print(
            "error: --tool-allowlist and --tool-policy-file are mutually "
            "exclusive; pass one or the other",
            file=sys.stderr,
        )
        return 2

    tool_allowlist: tuple[str, ...] = ()
    tool_policy: ToolPolicy | None = None
    if args.tool_policy_file:
        try:
            tool_policy = load_tool_policy(args.tool_policy_file)
        except FileNotFoundError:
            print(
                f"error: tool policy file not found: {args.tool_policy_file}",
                file=sys.stderr,
            )
            return 2
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    elif args.tool_allowlist:
        # Flatten the v0.2 sugar form into a single tuple of unique names.
        seen: list[str] = []
        for item in args.tool_allowlist:
            for piece in str(item).split(","):
                name = piece.strip()
                if name and name not in seen:
                    seen.append(name)
        tool_allowlist = tuple(seen)
        if tool_allowlist:
            tool_policy = tool_policy_from_allowlist(tool_allowlist)

    try:
        config = ProxyConfig(
            backend=args.backend,
            model=args.model,
            base_url=args.base_url,
            api_key=args.api_key,
            model_enforcement=args.model_enforcement,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            governance_enabled=args.governance,
            grounding_paths=args.grounding,
            trace_file=args.trace_file,
            openclaw_profile=args.openclaw_profile,
            served_model_id=args.served_model_id,
            trace_visibility=args.trace_visibility,
            proxy_api_key=resolved_proxy_api_key,
            memory_enabled=False if args.openclaw_profile else None,
            unsafe_bind=args.unsafe_bind,
            tool_policy=tool_policy,
        )
        server = build_proxy_server(config, host=args.host, port=args.port)
    except (BackendError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.openclaw_profile:
        host_safe = _is_loopback_host(args.host) or args.unsafe_bind
        if tool_policy is None:
            tool_state = "OFF (every tool call fail-closed; v0.1 behaviour)"
        else:
            counts = {"allow": 0, "soften": 0, "block": 0}
            for td in tool_policy.tools.values():
                counts[td.decision] = counts.get(td.decision, 0) + 1
            tool_state = (
                f"{len(tool_policy.tools)} tools "
                f"(default={tool_policy.default}) "
                f"allow={counts['allow']} soften={counts['soften']} "
                f"block={counts['block']}"
            )
        print(
            f"AGIF-XCore proxy (OpenClaw profile) at http://{args.host}:{args.port}\n"
            f"  served model id : {args.served_model_id}\n"
            f"  upstream        : {args.backend} -> {args.model}\n"
            f"  governance      : ON\n"
            f"  memory          : OFF (hard-off in OpenClaw MVP)\n"
            f"  trace file      : {args.trace_file}\n"
            f"  trace visibility: {args.trace_visibility}\n"
            f"  auth            : {'ON' if resolved_proxy_api_key else 'OFF'}\n"
            f"  host safe       : {host_safe}\n"
            f"  tool policy     : {tool_state}\n"
            f"\n"
            f"OpenClaw provider base_url: http://{args.host}:{args.port}/v1\n"
            f"\n"
            f"Press Ctrl+C to stop.",
            file=sys.stderr,
        )
    else:
        gov_label = "ON" if args.governance else "OFF"
        print(
            f"AGIF-XCore proxy running at http://{args.host}:{args.port}\n"
            f"  upstream : {args.backend} -> {args.model}\n"
            f"  governance: {gov_label}\n"
            f"  grounding : {len(args.grounding or [])} path(s)\n"
            f"\n"
            f"Any OpenAI-compatible client can now point at:\n"
            f"  base_url = http://{args.host}:{args.port}/v1\n"
            f"\n"
            f"Press Ctrl+C to stop.",
            file=sys.stderr,
        )

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nshutting down...", file=sys.stderr)
        server.shutdown()
    return 0
