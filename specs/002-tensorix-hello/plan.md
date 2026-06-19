# Implementation Plan: Tensorix Text Hello World

**Branch**: `002-tensorix-hello` | **Date**: 2026-06-03 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/002-tensorix-hello/spec.md`

**Plan input**: Python + OpenAI SDK + python-dotenv. `hello_tensorix.py` and `tensorix_client.py` at repo root. `.env.example` with `TENSORIX_API_KEY` and `TENSORIX_MODEL=qwen/qwen3-vl-235b-a22b-instruct`. pytest with mocked API for missing-key errors.

## Summary

Add a standalone hello-world script that loads secrets from `.env`, calls Tensorix
via the OpenAI-compatible SDK, asks "What is the capital of France?", and prints
the reply to stdout. Thin `tensorix_client.py` module for testability; no changes
to `app.py`.

## Technical Context

**Language/Version**: Python 3.10+ (project venv on 3.13)

**Primary Dependencies**: `openai` (SDK pointed at Tensorix), `python-dotenv`, `pytest`

**Storage**: N/A

**Testing**: pytest with mocks for missing-key and client errors; manual live run for Paris

**Target Platform**: Local developer machine

**Project Type**: CLI script + small library module

**Performance Goals**: Single chat completion; response within 60s on normal network

**Constraints**: Secrets in `.env` only; no keys in stdout or git; do not modify `app.py`

**Scale/Scope**: One question, one script entrypoint, two Python modules + tests

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Simplicity**: OpenAI SDK + dotenv; no extra services
- [x] **Small files**: `tensorix_client.py`, `hello_tensorix.py`, tests
- [x] **Test-first**: pytest for missing key (and optional mock) before full wiring
- [x] **Local run**: `python hello_tensorix.py` after `pip install`
- [x] **Clear errors**: custom messages for missing key / API failures
- [x] **README note**: quickstart + readme section
- [x] **No secrets**: `.env.example` placeholders only; `.env` gitignored

**Post-design re-check**: All gates pass.

## Project Structure

### Documentation (this feature)

```text
specs/002-tensorix-hello/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── cli-hello-tensorix.md
└── tasks.md             # /speckit.tasks
```

### Source Code (repository root)

```text
tensorix_client.py       # load_config(), ask(question) -> str
hello_tensorix.py        # CLI entry: default question, print answer
.env.example             # TENSORIX_API_KEY=, TENSORIX_MODEL=
requirements.txt         # + openai, python-dotenv
tests/
└── test_tensorix_client.py
readme.md                # hello script section
```

**Structure Decision**: Flat repo root; client module reused later for OCR feature.

## Implementation Phases

### Phase A — Dependencies and env template

1. Add `openai>=1.0`, `python-dotenv>=1.0` to `requirements.txt`
2. Create `.env.example` with documented placeholders

### Phase B — Tests first

1. `tests/test_tensorix_client.py`:
   - `load_config()` raises clear error when `TENSORIX_API_KEY` missing
   - `ask()` returns content when OpenAI client mock returns Paris
   - Optional: empty response handling

### Phase C — Client module

1. `tensorix_client.py`:
   - `load_dotenv()` from repo root
   - `get_api_key()`, `get_model()` from env (default model from `.env.example`)
   - `create_client()` → `OpenAI(api_key=..., base_url="https://api.tensorix.ai/v1")`
   - `ask(question: str) -> str` → chat completion, return message content
   - Map `AuthenticationError` / API errors to readable messages

### Phase D — CLI script

1. `hello_tensorix.py`:
   - Default question: `"What is the capital of France?"`
   - Optional `--question` argparse override
   - Print answer to stdout only (no key leakage)
   - Exit code 1 on error with message to stderr

### Phase E — Docs and validation

1. Update `readme.md` with hello script commands
2. Live run: confirm stdout contains `Paris`

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
