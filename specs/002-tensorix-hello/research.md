# Research: Tensorix Text Hello World

**Feature**: 002-tensorix-hello | **Date**: 2026-06-03

## Tensorix API compatibility

**Decision**: Use OpenAI Python SDK with `base_url="https://api.tensorix.ai/v1"`.

**Rationale**: [Tensorix docs](https://docs.tensorix.ai/api-reference/overview) state
OpenAI-compatible chat completions. SDK reduces boilerplate for errors and JSON parsing;
same client pattern will work for future OCR multimodal messages.

**Alternatives considered**:
- `requests` only — valid; rejected for this plan per user input
- curl script — rejected; harder to unit test and extend for OCR

## Environment loading

**Decision**: `python-dotenv` loads `.env` from project root on import/call.

**Rationale**: Constitution requires secrets in `.env`; dotenv is standard for local dev.
`.env.example` documents required vars without committing secrets.

## Model selection

**Decision**: `TENSORIX_MODEL=qwen/qwen3-vl-235b-a22b-instruct` in `.env.example`.

**Rationale**: Same Qwen VL model planned for OCR; text-only hello world validates it works.
Pure text Qwen models exist on Tensorix but OCR path uses VL.

## Error handling

**Decision**: Check key before network call; catch `openai.AuthenticationError` and
generic API errors; print to stderr, exit 1.

**Rationale**: Spec FR-006, FR-007 and constitution V (clear error messages).

## Testing strategy

**Decision**: Mock `OpenAI` client in pytest; no live API in CI/unit tests.

**Rationale**: Avoids burning credits and flakiness; live Paris check is manual quickstart step.
