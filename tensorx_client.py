"""TensorX API client (OpenAI-compatible) — text calls for smoke test."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import AuthenticationError, OpenAI

TENSORX_BASE_URL_DEFAULT = "https://api.tensorx.ai/v1"
DEFAULT_MODEL = "qwen/qwen3-vl-235b-a22b-instruct"

_REPO_ROOT = Path(__file__).resolve().parent


class TensorxError(Exception):
    """User-facing TensorX client error."""


def load_env() -> None:
    load_dotenv(_REPO_ROOT / ".env")


def _env(name: str, legacy_name: str | None = None) -> str:
    value = os.environ.get(name, "").strip()
    if value or not legacy_name:
        return value
    return os.environ.get(legacy_name, "").strip()


def get_api_key() -> str:
    load_env()
    key = _env("TENSORX_API_KEY", "TENSORIX_API_KEY")
    if not key:
        raise TensorxError(
            "TENSORX_API_KEY is not set. Add it to .env (see .env.example)."
        )
    return key


def get_model() -> str:
    load_env()
    model = _env("TENSORX_MODEL", "TENSORIX_MODEL")
    return model or DEFAULT_MODEL


def get_base_url() -> str:
    load_env()
    url = _env("TENSORX_BASE_URL", "TENSORIX_BASE_URL")
    return url or TENSORX_BASE_URL_DEFAULT


def create_client(api_key: str | None = None) -> OpenAI:
    key = api_key if api_key is not None else get_api_key()
    return OpenAI(api_key=key, base_url=get_base_url())


def ask(question: str, *, client: OpenAI | None = None) -> str:
    if not question.strip():
        raise TensorxError("Question must not be empty.")

    openai_client = client or create_client()
    model = get_model()

    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            max_tokens=256,
            temperature=0,
        )
    except AuthenticationError as exc:
        raise TensorxError(
            "TensorX authentication failed. Check TENSORX_API_KEY in .env."
        ) from exc
    except Exception as exc:
        raise TensorxError(f"TensorX API request failed: {exc}") from exc

    if not response.choices:
        raise TensorxError("TensorX returned no choices.")

    content = response.choices[0].message.content
    if not content or not content.strip():
        raise TensorxError("TensorX returned an empty response.")

    return content.strip()
