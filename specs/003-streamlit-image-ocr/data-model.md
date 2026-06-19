# Data Model: Streamlit Image OCR

**Feature**: 003-streamlit-image-ocr | **Date**: 2026-06-03

## UploadedImage (from Streamlit)

| Field | Source | Notes |
|-------|--------|-------|
| name | `uploaded_file.name` | For MIME inference + display |
| bytes | `uploaded_file.getvalue()` | Sent to API |
| size_bytes | `len(bytes)` | Feature 1 display |

## ExtractionRequest

| Field | Type | Notes |
|-------|------|-------|
| image_bytes | bytes | Non-empty |
| mime_type | string | `image/jpeg` or `image/png` |
| prompt | string | Fixed OCR instruction |
| model | string | `TENSORIX_MODEL` |

## ExtractionResponse

| Field | Type | Notes |
|-------|------|-------|
| text | string | Model reply; shown in `st.text_area` |

## UI state (Streamlit session)

| State | Trigger | UI |
|-------|---------|-----|
| no_upload | uploader empty | info + disabled flow |
| ready | upload present | size shown, Submit enabled |
| loading | Submit clicked | spinner |
| success | API ok | extracted text area |
| error | TensorixError | st.error message |
