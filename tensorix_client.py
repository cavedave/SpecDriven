"""Tensorix API client (OpenAI-compatible) — text calls for smoke test."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import AuthenticationError, OpenAI

TENSORIX_BASE_URL = "https://api.tensorix.ai/v1"
DEFAULT_MODEL = "qwen/qwen3-vl-235b-a22b-instruct"

_REPO_ROOT = Path(__file__).resolve().parent


class TensorixError(Exception):
    """User-facing Tensorix client error."""


def load_env() -> None:
    load_dotenv(_REPO_ROOT / ".env")


def get_api_key() -> str:
    load_env()
    key = os.environ.get("TENSORIX_API_KEY", "").strip()
    if not key:
        raise TensorixError(
            "TENSORIX_API_KEY is not set. Add it to .env (see .env.example)."
        )
    return key


def get_model() -> str:
    load_env()
    return os.environ.get("TENSORIX_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL


def create_client(api_key: str | None = None) -> OpenAI:
    key = api_key if api_key is not None else get_api_key()
    return OpenAI(api_key=key, base_url=TENSORIX_BASE_URL)


def ask(question: str, *, client: OpenAI | None = None) -> str:
    if not question.strip():
        raise TensorixError("Question must not be empty.")

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
        raise TensorixError(
            "Tensorix authentication failed. Check TENSORIX_API_KEY in .env."
        ) from exc
    except Exception as exc:
        raise TensorixError(f"Tensorix API request failed: {exc}") from exc

    if not response.choices:
        raise TensorixError("Tensorix returned no choices.")

    content = response.choices[0].message.content
    if not content or not content.strip():
        raise TensorixError("Tensorix returned an empty response.")

    return content.strip()
