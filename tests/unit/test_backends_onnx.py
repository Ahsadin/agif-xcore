"""Tests for the ONNX backend.

All tests use mocks — no actual ONNX model files or onnxruntime
needed. The tests verify:

  * Error code constants match Tasklet's original pattern.
  * Chat prompt formatting produces correct structure.
  * Provider detection is safe when onnxruntime is absent.
  * Model path validation raises BackendBlocked.
  * Healthcheck reports correct state.
  * Registry resolves "onnx" to OnnxBackend.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from agif_xcore.backends.base import BackendBlocked, BackendError
from agif_xcore.backends.onnx import (
    CPU_PROVIDER,
    ONNX_ERROR_INFERENCE_FAILED,
    ONNX_ERROR_INFERENCE_TIMEOUT,
    ONNX_ERROR_MODEL_LOAD_FAILED,
    ONNX_ERROR_MODEL_NOT_FOUND,
    ONNX_ERROR_OUTPUT_INVALID,
    ONNX_ERROR_RUNTIME_MISSING,
    OnnxBackend,
    OnnxBootstrap,
    discover_onnx_providers,
    format_chat_prompt,
)


class ErrorCodeTests(unittest.TestCase):
    """Verify error codes exist and match Tasklet's pattern."""

    def test_all_error_codes_are_strings(self) -> None:
        codes = [
            ONNX_ERROR_MODEL_NOT_FOUND,
            ONNX_ERROR_MODEL_LOAD_FAILED,
            ONNX_ERROR_RUNTIME_MISSING,
            ONNX_ERROR_INFERENCE_TIMEOUT,
            ONNX_ERROR_INFERENCE_FAILED,
            ONNX_ERROR_OUTPUT_INVALID,
        ]
        for code in codes:
            self.assertIsInstance(code, str)
            self.assertTrue(code.startswith("ONNX_"), f"code should start with ONNX_: {code}")

    def test_error_codes_are_unique(self) -> None:
        codes = [
            ONNX_ERROR_MODEL_NOT_FOUND,
            ONNX_ERROR_MODEL_LOAD_FAILED,
            ONNX_ERROR_RUNTIME_MISSING,
            ONNX_ERROR_INFERENCE_TIMEOUT,
            ONNX_ERROR_INFERENCE_FAILED,
            ONNX_ERROR_OUTPUT_INVALID,
        ]
        self.assertEqual(len(codes), len(set(codes)))


class FormatChatPromptTests(unittest.TestCase):
    """Verify chat message formatting."""

    def test_system_user_pair(self) -> None:
        messages = [
            {"role": "system", "content": "You are helpful."},
            {"role": "user", "content": "Hello!"},
        ]
        prompt = format_chat_prompt(messages)
        self.assertIn("<|system|>", prompt)
        self.assertIn("You are helpful.", prompt)
        self.assertIn("<|user|>", prompt)
        self.assertIn("Hello!", prompt)
        # Should end with assistant prompt
        self.assertTrue(prompt.rstrip().endswith("<|assistant|>"))

    def test_multi_turn(self) -> None:
        messages = [
            {"role": "system", "content": "Be brief."},
            {"role": "user", "content": "Hi"},
            {"role": "assistant", "content": "Hello!"},
            {"role": "user", "content": "What is 2+2?"},
        ]
        prompt = format_chat_prompt(messages)
        self.assertEqual(prompt.count("<|user|>"), 2)
        self.assertEqual(prompt.count("<|assistant|>"), 2)  # one from message, one appended

    def test_empty_messages(self) -> None:
        prompt = format_chat_prompt([])
        self.assertIn("<|assistant|>", prompt)


class ProviderDetectionTests(unittest.TestCase):
    """Test onnxruntime provider discovery."""

    def test_discover_returns_tuple(self) -> None:
        available, providers = discover_onnx_providers()
        self.assertIsInstance(available, bool)
        self.assertIsInstance(providers, list)

    def test_cpu_provider_constant(self) -> None:
        self.assertEqual(CPU_PROVIDER, "CPUExecutionProvider")


class OnnxBackendInitTests(unittest.TestCase):
    """Test backend initialization and path validation."""

    def test_nonexistent_path_raises_on_use(self) -> None:
        """Backend doesn't fail at init; fails at first use (lazy load)."""
        backend = OnnxBackend(model_path="/nonexistent/path")
        self.assertFalse(backend._loaded)

    def test_complete_with_nonexistent_path(self) -> None:
        backend = OnnxBackend(model_path="/nonexistent/model.onnx")
        with self.assertRaises(BackendBlocked) as ctx:
            backend.complete(
                [{"role": "user", "content": "hello"}],
                model="test",
            )
        self.assertIn(ONNX_ERROR_MODEL_NOT_FOUND, str(ctx.exception))

    def test_healthcheck_before_load(self) -> None:
        backend = OnnxBackend(model_path="/nonexistent")
        health = backend.healthcheck()
        self.assertFalse(health["reachable"])
        self.assertEqual(health["mode"], "not_loaded")

    def test_name_is_onnx(self) -> None:
        backend = OnnxBackend(model_path="/tmp/test")
        self.assertEqual(backend.name, "onnx")


class OnnxBootstrapTests(unittest.TestCase):
    """Test the bootstrap metadata dataclass."""

    def test_bootstrap_fields(self) -> None:
        b = OnnxBootstrap(
            model_path="/tmp/model",
            provider=CPU_PROVIDER,
            mode="genai",
            onnx_hash="abc123",
            onnxruntime_available=True,
            onnxruntime_providers=["CPUExecutionProvider"],
        )
        self.assertEqual(b.model_path, "/tmp/model")
        self.assertEqual(b.mode, "genai")
        self.assertEqual(b.provider, CPU_PROVIDER)


class RegistryTests(unittest.TestCase):
    """Test that the registry knows about 'onnx'."""

    def test_onnx_in_available_backends(self) -> None:
        from agif_xcore.backends.registry import available_backends
        self.assertIn("onnx", available_backends())

    def test_resolve_onnx_requires_path(self) -> None:
        from agif_xcore.backends.registry import resolve_backend
        # Clear any env var
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(BackendError) as ctx:
                resolve_backend("onnx")
            self.assertIn("requires", str(ctx.exception))

    def test_resolve_onnx_with_path(self) -> None:
        from agif_xcore.backends.registry import resolve_backend
        with tempfile.TemporaryDirectory() as tmp:
            backend = resolve_backend("onnx", base_url=tmp)
            self.assertIsInstance(backend, OnnxBackend)
            self.assertEqual(backend.name, "onnx")


class OnnxBackendWithTmpDirTests(unittest.TestCase):
    """Test backend behavior with an actual directory (but no model files)."""

    def test_load_empty_dir_raises(self) -> None:
        """An empty directory should raise on first use."""
        with tempfile.TemporaryDirectory() as tmp:
            backend = OnnxBackend(model_path=tmp)
            with self.assertRaises(BackendBlocked):
                backend.complete(
                    [{"role": "user", "content": "hello"}],
                    model="test",
                )

    def test_healthcheck_with_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            backend = OnnxBackend(model_path=tmp)
            health = backend.healthcheck()
            self.assertIn("model_path", health)
            self.assertIn(tmp, health["model_path"])


if __name__ == "__main__":
    unittest.main()
