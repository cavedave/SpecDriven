# Data Model: Tensorix Text Hello World

**Feature**: 002-tensorix-hello | **Date**: 2026-06-03

No persistent storage. Ephemeral request/response only.

## Configuration (from environment)

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `TENSORIX_API_KEY` | Yes | — | Bearer token for API |
| `TENSORIX_MODEL` | No | `qwen/qwen3-vl-235b-a22b-instruct` | Model ID in chat request |

Loaded via `python-dotenv` from `.env` at repo root.

## ChatRequest (transient)

| Field | Type | Example |
|-------|------|---------|
| question | string | "What is the capital of France?" |
| model | string | from `TENSORIX_MODEL` |

Mapped to OpenAI `messages=[{"role":"user","content": question}]`.

## ChatResponse (transient)

| Field | Type | Notes |
|-------|------|-------|
| content | string | `choices[0].message.content`; printed to stdout |

## Error states

| Condition | User-facing behavior |
|-----------|---------------------|
| Missing API key | Message: set `TENSORIX_API_KEY` in `.env`; exit 1 |
| 401 / auth error | Message: check API key; exit 1 |
| Empty content | Message: no response from model; exit 1 |
| Network failure | Message: connection failed; exit 1 |
