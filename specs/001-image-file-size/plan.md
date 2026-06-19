# Implementation Plan: Image Upload File Size

**Branch**: `001-image-file-size` | **Date**: 2026-06-03 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-image-file-size/spec.md`

**Plan input**: Python + Streamlit, single `app.py` at repo root, `requirements.txt`, pytest for human-readable size formatting helper. No Pillow. Run with `streamlit run app.py`.

## Summary

Build a minimal local Streamlit app that accepts an image upload and displays the
file size in bytes and human-readable units (KB/MB). Extract size-formatting logic
into a small testable module; keep UI in `app.py`. No external APIs, no Pillow, no
persistence.

## Technical Context

**Language/Version**: Python 3.11+ (3.10+ acceptable)

**Primary Dependencies**: streamlit (UI), pytest (tests)

**Storage**: N/A — in-memory upload bytes only; no database or files written

**Testing**: pytest for `format_file_size()` in `file_size.py`; manual quickstart for UI

**Target Platform**: Local developer machine (macOS/Linux; Windows untested but expected to work)

**Project Type**: Single-file Streamlit web app + one helper module

**Performance Goals**: Instant display for files up to ~50 MB (read bytes once via Streamlit uploader)

**Constraints**: No Pillow; no Tensorix; no `.env` secrets required for this feature; offline-capable after `pip install`

**Scale/Scope**: Single user, one page, two source files + tests

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify against `.specify/memory/constitution.md`:

- [x] **Simplicity**: Streamlit + stdlib only for size logic; no external services
- [x] **Small files**: `app.py`, `file_size.py`, tests — no `src/` tree yet
- [x] **Test-first**: pytest for `format_file_size` before wiring Streamlit UI
- [x] **Local run**: `pip install -r requirements.txt && streamlit run app.py`
- [x] **Clear errors**: `st.info` when no upload; no bare tracebacks for normal paths
- [x] **README note**: quickstart + README section planned
- [x] **No secrets**: Feature needs no API keys; `.gitignore` for `.env` when added later

**Post-design re-check**: All gates still pass. No Complexity Tracking entries required.

## Project Structure

### Documentation (this feature)

```text
specs/001-image-file-size/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── ui-upload-display.md
└── tasks.md             # Created by /speckit.tasks
```

### Source Code (repository root)

```text
app.py                   # Streamlit UI: title, uploader, size display
file_size.py             # format_file_size(bytes) -> str (pure, testable)
requirements.txt         # streamlit, pytest
tests/
└── test_file_size.py    # Unit tests for format_file_size
readme.md                # Short "Image file size app" run instructions (append section)
.gitignore               # .env, __pycache__, .pytest_cache, .venv
```

**Structure Decision**: Flat repo root per user request (standard Streamlit `app.py`
layout). Helper module separated only to satisfy constitution test-first and keep
`app.py` thin.

## Implementation Phases

### Phase A — Setup

1. Create `requirements.txt` with pinned minimum versions: `streamlit`, `pytest`
2. Add `.gitignore` entries if missing
3. Create `file_size.py` with `format_file_size(size_bytes: int) -> str`

### Phase B — Tests first (constitution III)

1. Write `tests/test_file_size.py` covering:
   - 0 bytes → `"0 B"`
   - values < 1024 → `"N B"`
   - KB range (e.g. 1536 → `"1.5 KB"`)
   - MB range (e.g. 1_048_576 → `"1.0 MB"`)
2. Run `pytest` — tests fail until `format_file_size` implemented

### Phase C — Helper implementation

1. Implement `format_file_size` using powers of 1024 (B, KB, MB)
2. Run `pytest` — all green

### Phase D — Streamlit UI

1. Create `app.py`:
   - Page title and short description
   - `st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])`
   - If `uploaded_file is None`: `st.info("Upload an image to see its file size.")`
   - Else: `data = uploaded_file.getvalue()`, show `len(data)` bytes + `format_file_size(len(data))`
   - Optionally show filename via `uploaded_file.name`
2. Manual test with `Japan-Firebombing.jpg`

### Phase E — Documentation

1. Add README section: install, run, test commands
2. Validate against [quickstart.md](./quickstart.md)

## Complexity Tracking

> No constitution violations. Table intentionally empty.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
