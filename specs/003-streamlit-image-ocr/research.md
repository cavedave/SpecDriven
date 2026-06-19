# Research: Streamlit Image OCR

**Feature**: 003-streamlit-image-ocr | **Date**: 2026-06-03

## Multimodal API format

**Decision**: OpenAI-compatible `image_url` with base64 data URL.

**Rationale**: Tensorix documents OpenAI-compatible chat completions; Qwen VL
accepts `content` array with `text` + `image_url`. Matches Feature 2 client.

**Alternatives considered**:
- Public HTTPS URL — requires hosting image; rejected
- Pillow resize — out of scope per Feature 1; retry if timeouts occur

## MIME types

**Decision**: Derive from upload filename extension; default `image/jpeg`.

**Rationale**: Streamlit uploader provides `name` and bytes; no Pillow decode needed.

## Submit vs auto-trigger

**Decision**: Explicit `st.button` on click only.

**Rationale**: Spec FR-002; avoids API cost on every re-render/upload change.

## Token limits

**Decision**: `max_tokens=4096` for OCR (vs 256 for text hello).

**Rationale**: Map image has dense text; caption + many city labels.

## Streamlit spinner

**Decision**: `st.spinner` context manager around API call.

**Rationale**: Spec US2; OCR latency 30–120s typical.

## Model

**Decision**: `TENSORIX_MODEL` from `.env` (default qwen3-vl).

**Rationale**: Same model as planned OCR path; validated in Feature 2 text call.
