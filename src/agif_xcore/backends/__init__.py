"""Backends package."""

from .base import (
    BackendBlocked,
    BackendContractError,
    BackendError,
    BackendModelMismatch,
    BackendResponse,
    BackendTimeout,
    ChatMessage,
    ModelBackend,
)
from .ollama import OllamaBackend
from .openai_compat import OpenAICompatBackend, OpenAICompatConfig
from .registry import available_backends, resolve_backend

__all__ = [
    "BackendBlocked",
    "BackendContractError",
    "BackendError",
    "BackendModelMismatch",
    "BackendResponse",
    "BackendTimeout",
    "ChatMessage",
    "ModelBackend",
    "OllamaBackend",
    "OpenAICompatBackend",
    "OpenAICompatConfig",
    "available_backends",
    "resolve_backend",
]
