# Quickstart: Tensorix Text Hello World

**Feature**: 002-tensorix-hello

## Prerequisites

- Python 3.10+, venv active
- Tensorix API key with credits
- `.env` at repo root (copy from `.env.example`)

## Setup

```bash
cd /Users/davidcurran/Documents/tensorix
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env: set TENSORIX_API_KEY to your real key
```

Example `.env`:

```bash
TENSORIX_API_KEY=sk-...
TENSORIX_MODEL=qwen/qwen3-vl-235b-a22b-instruct
```

## Unit tests (mocked, no API call)

```bash
pytest tests/test_tensorix_client.py -v
```

**Expected**: All tests pass.

## Live hello world

```bash
python hello_tensorix.py
```

**Expected**: stdout contains `Paris` (case-insensitive).

Custom question:

```bash
python hello_tensorix.py --question "What is the capital of Ireland?"
```

**Expected**: stdout contains `Dublin`.

## Missing key check

```bash
env -u TENSORIX_API_KEY python hello_tensorix.py
```

(with dotenv not loading a key — or temporarily rename `.env`)

**Expected**: Clear error on stderr, exit code 1, no network hang.

## References

- [spec.md](../spec.md)
- [cli-hello-tensorix.md](./cli-hello-tensorix.md)
- [Tensorix chat completions](https://docs.tensorix.ai/api-reference/chat-completions)
