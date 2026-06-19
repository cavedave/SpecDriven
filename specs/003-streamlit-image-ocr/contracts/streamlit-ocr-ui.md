# UI Contract: Streamlit OCR

**Feature**: 003-streamlit-image-ocr | **Date**: 2026-06-03

## Layout (top to bottom)

1. Title + caption
2. File uploader (`jpg`, `jpeg`, `png`)
3. If upload: file name + size (Feature 1)
4. Button: **Extract text** (primary)
5. If extraction succeeded: subheader **Extracted text** + read-only text area
6. Errors: `st.error` / warnings: `st.warning`

## Submit behavior

| Condition | Action |
|-----------|--------|
| No upload + button click | `st.warning("Upload an image first.")` — no API |
| Upload + button click | spinner → `extract_text_from_image` → show text |
| API error | `st.error(message)` |

## Spinner text

`Extracting text from image...`

## Non-goals

- Image preview thumbnail
- Download extracted text
- Edit/re-run without re-clicking Submit
