# CLI Contract: hello_tensorix

**Feature**: 002-tensorix-hello | **Date**: 2026-06-03

## Command

```bash
python hello_tensorix.py [--question TEXT]
```

## Arguments

| Flag | Default | Description |
|------|---------|-------------|
| `--question` | `"What is the capital of France?"` | User message sent to Tensorix |

## Environment

Requires `.env` or exported vars:

- `TENSORIX_API_KEY` (required)
- `TENSORIX_MODEL` (optional; defaults per `.env.example`)

## stdout

On success: model reply text only, one line or block, no API key.

Example (success):

```text
The capital of France is Paris.
```

## stderr

On failure: human-readable error (missing key, auth failure, network, empty response).

Exit code: `0` success, `1` failure.

## Non-goals

- JSON output mode
- Streaming
- Image input
