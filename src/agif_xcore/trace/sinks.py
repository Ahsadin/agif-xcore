"""Trace sinks: where traces go after the turn completes.

M1 ships two sinks — stdout JSONL and file JSONL. M4 will add the
SQLite sink. Any consumer of this package can provide its own sink by
implementing the ``TraceSink`` protocol.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import IO, Protocol

from ..schemas import TraceEnvelope, canonical_json


class TraceSink(Protocol):
    """Protocol for any component that consumes trace envelopes."""

    def write(self, trace: TraceEnvelope) -> None: ...

    def close(self) -> None: ...


class NullSink:
    """Discards every trace. Useful for library callers that don't want I/O."""

    name = "null"

    def write(self, trace: TraceEnvelope) -> None:  # noqa: D401 - trivial
        return None

    def close(self) -> None:
        return None


class StdoutJsonlSink:
    """Writes one canonical JSON line per trace to a provided stream.

    Defaults to ``sys.stderr`` so that normal program output on ``stdout``
    stays clean (the CLI can still pipe answer text through ``stdout``).
    """

    name = "stdout_jsonl"

    def __init__(self, stream: IO[str] | None = None) -> None:
        self._stream = stream or sys.stderr

    def write(self, trace: TraceEnvelope) -> None:
        self._stream.write(canonical_json(trace))
        self._stream.write("\n")
        self._stream.flush()

    def close(self) -> None:
        # Do not close the underlying stream — it belongs to the caller
        # (and closing stderr is rarely what anyone actually wants).
        return None


class FileJsonlSink:
    """Appends traces to a file as canonical JSONL. Creates parent dirs as needed.

    The file is opened on first write (lazy) so constructing the sink
    has no filesystem side effects. Each turn produces exactly one line.
    """

    name = "file_jsonl"

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)
        self._handle: IO[str] | None = None

    @property
    def path(self) -> Path:
        return self._path

    def write(self, trace: TraceEnvelope) -> None:
        if self._handle is None:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._handle = self._path.open("a", encoding="utf-8")
        self._handle.write(canonical_json(trace))
        self._handle.write("\n")
        self._handle.flush()

    def close(self) -> None:
        if self._handle is not None:
            self._handle.close()
            self._handle = None


class MultiSink:
    """Fan out one trace into many sinks."""

    name = "multi"

    def __init__(self, sinks: list[TraceSink]) -> None:
        self._sinks = list(sinks)

    def write(self, trace: TraceEnvelope) -> None:
        for sink in self._sinks:
            sink.write(trace)

    def close(self) -> None:
        for sink in self._sinks:
            try:
                sink.close()
            except Exception:  # pragma: no cover - defensive
                pass
