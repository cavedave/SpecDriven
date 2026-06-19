# Research: Image Upload File Size

**Feature**: 001-image-file-size | **Date**: 2026-06-03

## File size from Streamlit upload

**Decision**: Use `uploaded_file.getvalue()` and `len()` for byte count.

**Rationale**: Streamlit's `UploadedFile` wraps bytes in memory. No disk write or
image decode required. Matches spec FR-002/FR-008 (no Pillow).

**Alternatives considered**:
- `os.path.getsize` on saved temp file — rejected; unnecessary I/O
- Pillow `Image.open` for size — rejected; user excluded Pillow

## Human-readable size formatting

**Decision**: Pure function `format_file_size(n: int)` using 1024-based B/KB/MB with
one decimal for KB/MB.

**Rationale**: Testable without Streamlit; covers spec FR-003. Single decimal keeps
output readable (e.g. `1.5 KB`).

**Alternatives considered**:
- 1000-based SI units — rejected; less common for file sizes in dev tools
- Inline formatting in `app.py` — rejected; violates test-first constitution

## Image type restriction without Pillow

**Decision**: `st.file_uploader(..., type=["jpg", "jpeg", "png"])`.

**Rationale**: Streamlit filters file picker by extension; satisfies FR-005/P2 without
validating image structure.

**Alternatives considered**:
- MIME sniffing via stdlib — rejected; unnecessary for MVP
- Accept all files — rejected; spec P2 wants image-only

## Dependency versions

**Decision**: Pin loosely in `requirements.txt` (e.g. `streamlit>=1.28`, `pytest>=7`).

**Rationale**: Local dev project; avoid over-pinning unless reproducibility issues appear.

**Alternatives considered**:
- `pyproject.toml` + uv — deferred; `requirements.txt` matches constitution simplicity

## No Pillow for OCR path

**Decision**: Defer Pillow to a future feature if resize/validation needed for Tensorix OCR.

**Rationale**: Confirmed in spec and plan input; OCR feature will re-evaluate.
