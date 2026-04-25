"""Tests for the OpenAI API named backend."""

from __future__ import annotations

import os
import unittest

from agif_xcore.backends.base import BackendError
from agif_xcore.backends.openai_api import OpenAIBackend
from agif_xcore.backends.registry import available_backends, resolve_backend


class OpenAIBackendConfigTests(unittest.TestCase):
    def test_requires_api_key(self) -> None:
        # Clear env to ensure no accidental key
        old = os.environ.pop("OPENAI_API_KEY", None)
        try:
            with self.assertRaises(BackendError):
                OpenAIBackend()
        finally:
            if old is not None:
                os.environ["OPENAI_API_KEY"] = old

    def test_accepts_explicit_key(self) -> None:
        backend = OpenAIBackend(api_key="sk-test-key")
        self.assertEqual(backend.name, "openai")

    def test_reads_env_key(self) -> None:
        os.environ["OPENAI_API_KEY"] = "sk-from-env"
        try:
            backend = OpenAIBackend()
            self.assertEqual(backend.name, "openai")
        finally:
            del os.environ["OPENAI_API_KEY"]


class RegistryTests(unittest.TestCase):
    def test_openai_in_available_backends(self) -> None:
        self.assertIn("openai", available_backends())

    def test_resolve_openai_requires_key(self) -> None:
        old = os.environ.pop("OPENAI_API_KEY", None)
        try:
            with self.assertRaises(BackendError):
                resolve_backend("openai")
        finally:
            if old is not None:
                os.environ["OPENAI_API_KEY"] = old

    def test_resolve_openai_with_key(self) -> None:
        backend = resolve_backend("openai", api_key="sk-test")
        self.assertEqual(backend.name, "openai")


if __name__ == "__main__":
    unittest.main()
