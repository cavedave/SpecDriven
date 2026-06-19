# Implementation Plan: Streamlit Image Text Extraction

**Branch**: `003-streamlit-image-ocr` | **Date**: 2026-06-03 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/003-streamlit-image-ocr/spec.md`

**Plan input**: Extend `app.py` with Submit button. Extend `tensorix_client.py` with `extract_text_from_image(bytes, mime_type)` using OpenAI-style `image_url` + qwen3-vl. Reuse `.env`. `st.spinner` on submit. pytest with mocked multimodal response. Test with `Japan-Firebombing.jpg`.

## Summary

Extend the existing Streamlit app so users upload an image (Feature 1 metadata
preserved), click Submit, and see text extracted via Tensorix Qwen VL. Add
`extract_text_from_image()` to `tensorix_client.py` using base64 data URLs in
multimodal chat completions. Unit-test the client with mocks; manual E2E with
`Japan-Firebombing.jpg`.

## Technical Context

**Language/Version**: Python 3.10+ (venv 3.13)

**Primary Dependencies**: streamlit, openai, python-dotenv, pytest (existing)

**Storage**: N/A — image bytes in memory only

**Testing**: pytest mocks for `extract_text_from_image`; manual Streamlit + live API for map image

**Target Platform**: Local developer machine

**Project Type**: Streamlit app + shared Tensorix client module

**Performance Goals**: OCR response within 120s for ~600KB JPEG

**Constraints**: No Pillow in app code; secrets from `.env`; reuse Feature 2 client patterns

**Scale/Scope**: Single page, one new button, one new client function, extend tests

## Constitution Check

- [x] **Simplicity**: Extend two existing files + tests
- [x] **Small files**: Logic in `tensorix_client.py`, thin UI in `app.py`
- [x] **Test-first**: mock multimodal tests before/alongside UI wiring
- [x] **Local run**: `streamlit run app.py`
- [x] **Clear errors**: `st.error` for TensorixError
- [x] **README note**: quickstart section update
- [x] **No secrets**: `.env` only

## Project Structure

### Documentation

```text
specs/003-streamlit-image-ocr/
├── plan.md, research.md, data-model.md, quickstart.md
├── contracts/streamlit-ocr-ui.md
└── tasks.md
```

### Source changes

```text
tensorix_client.py    # + extract_text_from_image(image_bytes, mime_type)
app.py                # + Submit, spinner, st.text_area for result
tests/test_tensorix_client.py   # + multimodal mock tests
readme.md             # OCR usage note
```

## Implementation Phases

### Phase A — Client: multimodal extraction

1. Add `import base64` to `tensorix_client.py`
2. Add constant OCR prompt:

   ```text
   Extract all visible text from this image. Preserve labels and captions.
   ```

3. Implement `extract_text_from_image(image_bytes: bytes, mime_type: str, *, client=None) -> str`:
   - Validate non-empty bytes
   - Build `data:{mime_type};base64,{b64}` URL
   - POST multimodal message:

     ```python
     messages=[{"role": "user", "content": [
       {"type": "text", "text": OCR_PROMPT},
       {"type": "image_url", "image_url": {"url": data_url}},
     ]}]
     ```

   - `max_tokens=4096`, `temperature=0`
   - Reuse error handling from `ask()`

4. Helper `_mime_from_filename(name: str) -> str` in `app.py` or client:
   - `.jpg`/`.jpeg` → `image/jpeg`, `.png` → `image/png`

### Phase B — Tests first

1. `tests/test_tensorix_client.py`:
   - Mock client returns text containing `TOKYO`
   - Verify `chat.completions.create` called with multimodal content array
   - Empty bytes → `TensorixError`
   - Empty model response → `TensorixError`

### Phase C — Streamlit UI

1. Update `app.py`:
   - Keep upload + file size block (Feature 1)
   - Add `st.button("Extract text", type="primary")` (label: Submit / Extract text)
   - If button clicked and no upload → `st.warning("Upload an image first.")`
   - If upload + clicked:

     ```python
     with st.spinner("Extracting text from image..."):
         text = extract_text_from_image(data, mime)
     st.subheader("Extracted text")
     st.text_area(..., value=text, height=300)
     ```

   - Wrap `TensorixError` → `st.error(str(exc))`

2. Optional: update page title/caption to reflect OCR purpose

### Phase D — Validation

1. `pytest -v` all green
2. Manual: `streamlit run app.py`, upload `Japan-Firebombing.jpg`, Submit
3. Confirm city names or B-29 caption in output

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
