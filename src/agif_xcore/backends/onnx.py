"""ONNX backend for fully offline local inference.

Ported from Tasklet's ``v4_transformer_runner.py`` (494 LOC). The
original is a fail-closed VAT classifier. XCore generalizes the
patterns — typed error codes, CPU-only provider detection, timeout
enforcement — into a ``ModelBackend`` for text generation.

Inference modes (checked at import time, no hard crash):

  1. **onnxruntime-genai** — full text generation (preferred).
     ``pip install onnxruntime-genai``
  2. **onnxruntime** — raw session-based inference (classification,
     embeddings). ``pip install onnxruntime``
  3. **Neither installed** — raises ``BackendBlocked`` at first use.

Zero runtime deps; both packages are optional extras.
"""

from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .base import (
    BackendBlocked,
    BackendContractError,
    BackendError,
    BackendResponse,
    BackendTimeout,
    ChatMessage,
)


# ---------------------------------------------------------------------------
# Error codes (ported from Tasklet v4_transformer_runner.py)
# ---------------------------------------------------------------------------

ONNX_ERROR_MODEL_NOT_FOUND = "ONNX_MODEL_NOT_FOUND"
ONNX_ERROR_MODEL_LOAD_FAILED = "ONNX_MODEL_LOAD_FAILED"
ONNX_ERROR_RUNTIME_MISSING = "ONNX_RUNTIME_MISSING"
ONNX_ERROR_INFERENCE_TIMEOUT = "ONNX_INFERENCE_TIMEOUT"
ONNX_ERROR_INFERENCE_FAILED = "ONNX_INFERENCE_FAILED"
ONNX_ERROR_OUTPUT_INVALID = "ONNX_OUTPUT_INVALID"

CPU_PROVIDER = "CPUExecutionProvider"


# ---------------------------------------------------------------------------
# Provider detection (ported from Tasklet)
# ---------------------------------------------------------------------------

def discover_onnx_providers() -> tuple[bool, list[str]]:
    """Probe for available onnxruntime execution providers.

    Returns ``(is_available, provider_list)``. Safe to call even if
    onnxruntime is not installed — returns ``(False, [])``.
    """
    try:
        import onnxruntime as ort  # type: ignore[import-untyped]
        providers = ort.get_available_providers()
        if not isinstance(providers, list):
            return True, []
        return True, [str(p) for p in providers]
    except Exception:
        return False, []


def _check_genai_available() -> bool:
    """Return True if onnxruntime-genai is importable."""
    try:
        import onnxruntime_genai  # type: ignore[import-untyped]  # noqa: F401
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Chat prompt formatting
# ---------------------------------------------------------------------------

def format_chat_prompt(messages: list[ChatMessage]) -> str:
    """Convert a list of chat messages into a plain-text prompt.

    ONNX models don't have a standardised chat template. This
    formatter is simple and works for most instruction-tuned models.
    """
    parts: list[str] = []
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if role == "system":
            parts.append(f"<|system|>\n{content}")
        elif role == "user":
            parts.append(f"<|user|>\n{content}")
        elif role == "assistant":
            parts.append(f"<|assistant|>\n{content}")
    parts.append("<|assistant|>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# OnnxBackend
# ---------------------------------------------------------------------------

@dataclass
class OnnxBootstrap:
    """Metadata from a successful ONNX model load."""

    model_path: str
    provider: str
    mode: str  # "genai" or "ort"
    onnx_hash: str
    onnxruntime_available: bool
    onnxruntime_providers: list[str] = field(default_factory=list)


class OnnxBackend:
    """Fully offline ONNX backend.

    Loads a model from a local directory. No network, no server.
    """

    name = "onnx"

    def __init__(
        self,
        model_path: str | Path,
        *,
        provider: str = CPU_PROVIDER,
        timeout_ms: int = 60_000,
        max_length: int = 512,
    ) -> None:
        self._model_path = Path(model_path).resolve()
        self._provider = provider
        self._timeout_ms = timeout_ms
        self._max_length = max_length
        self._loaded = False
        self._mode: str = ""
        self._genai_model: Any = None
        self._genai_tokenizer: Any = None
        self._ort_session: Any = None
        self._bootstrap: OnnxBootstrap | None = None

    def _ensure_loaded(self) -> None:
        """Lazy-load the model on first use."""
        if self._loaded:
            return

        if not self._model_path.exists():
            raise BackendBlocked(
                f"[{ONNX_ERROR_MODEL_NOT_FOUND}] "
                f"model path does not exist: {self._model_path}"
            )

        ort_available, ort_providers = discover_onnx_providers()
        genai_available = _check_genai_available()

        # Try onnxruntime-genai first (text generation)
        if genai_available:
            try:
                import onnxruntime_genai as og  # type: ignore[import-untyped]
                self._genai_model = og.Model(str(self._model_path))
                self._genai_tokenizer = og.Tokenizer(self._genai_model)
                self._mode = "genai"
                self._loaded = True
            except Exception as exc:
                raise BackendBlocked(
                    f"[{ONNX_ERROR_MODEL_LOAD_FAILED}] "
                    f"onnxruntime-genai failed to load model: {exc}"
                ) from exc
        elif ort_available:
            # Fall back to raw onnxruntime session
            onnx_files = list(self._model_path.glob("*.onnx")) if self._model_path.is_dir() else [self._model_path]
            if not onnx_files:
                raise BackendBlocked(
                    f"[{ONNX_ERROR_MODEL_NOT_FOUND}] "
                    f"no .onnx files found in {self._model_path}"
                )
            try:
                import onnxruntime as ort  # type: ignore[import-untyped]
                self._ort_session = ort.InferenceSession(
                    str(onnx_files[0]),
                    providers=[self._provider],
                )
                self._mode = "ort"
                self._loaded = True
            except Exception as exc:
                raise BackendBlocked(
                    f"[{ONNX_ERROR_MODEL_LOAD_FAILED}] "
                    f"onnxruntime failed to load model: {exc}"
                ) from exc
        else:
            raise BackendBlocked(
                f"[{ONNX_ERROR_RUNTIME_MISSING}] "
                "neither onnxruntime-genai nor onnxruntime is installed. "
                "Install with: pip install agif-xcore[onnx]"
            )

        # Compute model hash for audit
        model_hash = _path_hash(self._model_path)
        self._bootstrap = OnnxBootstrap(
            model_path=str(self._model_path),
            provider=self._provider,
            mode=self._mode,
            onnx_hash=model_hash,
            onnxruntime_available=ort_available,
            onnxruntime_providers=ort_providers,
        )

    def complete(
        self,
        messages: list[ChatMessage],
        *,
        model: str,
        temperature: float = 0.0,
        max_tokens: int | None = None,
        timeout_ms: int = 30_000,
        tools: list[dict[str, Any]] | None = None,
    ) -> BackendResponse:
        """Run inference on the local ONNX model.

        The ``model`` parameter is accepted for protocol compliance but
        is not used for model selection (we use ``model_path`` from
        init). It's echoed back in the response.

        Tool-calling is not supported by the ONNX backend in v0.2; passing a
        non-empty ``tools`` list raises ``BackendError`` rather than silently
        dropping tools and pretending the model could have called them.
        """
        if tools:
            raise BackendError(
                "tools not supported by the ONNX backend in v0.2; "
                "use ollama or openai_compat for governed tool calls"
            )
        self._ensure_loaded()
        effective_timeout = min(timeout_ms, self._timeout_ms)
        start = time.monotonic()

        prompt = format_chat_prompt(messages)

        if self._mode == "genai":
            text = self._complete_genai(
                prompt,
                temperature=temperature,
                max_tokens=max_tokens or self._max_length,
                timeout_ms=effective_timeout,
                start=start,
            )
        elif self._mode == "ort":
            raise BackendBlocked(
                f"[{ONNX_ERROR_INFERENCE_FAILED}] "
                "raw onnxruntime session supports classification/embedding only, "
                "not text generation. Install onnxruntime-genai for chat completions."
            )
        else:
            raise BackendBlocked(
                f"[{ONNX_ERROR_RUNTIME_MISSING}] no inference mode available"
            )

        latency_ms = int((time.monotonic() - start) * 1000)

        return BackendResponse(
            text=text.strip(),
            model_id=model,
            finish_reason="stop",
            prompt_tokens=len(prompt.split()),
            completion_tokens=len(text.split()),
            latency_ms=latency_ms,
        )

    def healthcheck(self) -> dict[str, Any]:
        """Report whether the model is loaded and what mode it's in."""
        ort_available, ort_providers = discover_onnx_providers()
        genai_available = _check_genai_available()
        return {
            "reachable": self._loaded,
            "model_path": str(self._model_path),
            "mode": self._mode or "not_loaded",
            "onnxruntime_available": ort_available,
            "onnxruntime_genai_available": genai_available,
            "onnxruntime_providers": ort_providers,
            "bootstrap": self._bootstrap.model_path if self._bootstrap else None,
        }

    # ------------------------------------------------------------------
    # Genai inference
    # ------------------------------------------------------------------

    def _complete_genai(
        self,
        prompt: str,
        *,
        temperature: float,
        max_tokens: int,
        timeout_ms: int,
        start: float,
    ) -> str:
        """Run text generation via onnxruntime-genai."""
        import onnxruntime_genai as og  # type: ignore[import-untyped]

        try:
            params = og.GeneratorParams(self._genai_model)
            search_opts: dict[str, Any] = {"max_length": max_tokens}
            if temperature > 0.01:
                search_opts["temperature"] = temperature
                search_opts["do_sample"] = True
            else:
                search_opts["do_sample"] = False
            params.set_search_options(**search_opts)

            input_tokens = self._genai_tokenizer.encode(prompt)
            params.input_ids = input_tokens

            tokenizer_stream = self._genai_tokenizer.create_stream()
            generator = og.Generator(self._genai_model, params)

            output_parts: list[str] = []
            while not generator.is_done():
                # Timeout check (ported from Tasklet's _assert_timeout)
                elapsed_ms = int((time.monotonic() - start) * 1000)
                if elapsed_ms > timeout_ms:
                    raise BackendTimeout(
                        f"[{ONNX_ERROR_INFERENCE_TIMEOUT}] "
                        f"generation exceeded timeout ({elapsed_ms}ms > {timeout_ms}ms)"
                    )
                generator.compute_logits()
                generator.generate_next_token()
                new_token = generator.get_next_tokens()[0]
                output_parts.append(tokenizer_stream.decode(new_token))

            return "".join(output_parts)

        except BackendTimeout:
            raise
        except Exception as exc:
            raise BackendError(
                f"[{ONNX_ERROR_INFERENCE_FAILED}] genai inference error: {exc}"
            ) from exc


# ---------------------------------------------------------------------------
# Helpers (ported from Tasklet)
# ---------------------------------------------------------------------------

def _path_hash(path: Path) -> str:
    """SHA-256 of the first file found (or directory name)."""
    if path.is_file():
        digest = hashlib.sha256()
        with path.open("rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                digest.update(chunk)
        return digest.hexdigest()[:16]
    elif path.is_dir():
        # Hash the directory name + file listing for audit
        listing = sorted(str(p) for p in path.rglob("*") if p.is_file())
        return hashlib.sha256(
            "\n".join(listing).encode("utf-8")
        ).hexdigest()[:16]
    return "unknown"


__all__ = [
    "CPU_PROVIDER",
    "ONNX_ERROR_INFERENCE_FAILED",
    "ONNX_ERROR_INFERENCE_TIMEOUT",
    "ONNX_ERROR_MODEL_LOAD_FAILED",
    "ONNX_ERROR_MODEL_NOT_FOUND",
    "ONNX_ERROR_OUTPUT_INVALID",
    "ONNX_ERROR_RUNTIME_MISSING",
    "OnnxBackend",
    "OnnxBootstrap",
    "discover_onnx_providers",
    "format_chat_prompt",
]
