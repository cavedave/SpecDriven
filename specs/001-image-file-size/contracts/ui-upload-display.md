# UI Contract: Image Upload and File Size Display

**Feature**: 001-image-file-size | **Date**: 2026-06-03

## Surface

Local Streamlit single-page app (`app.py`).

## Components

| Component | Streamlit API | Behavior |
|-----------|---------------|----------|
| Title | `st.title` | "Image File Size" (or equivalent) |
| Description | `st.caption` / `st.markdown` | One line: upload an image to see its size |
| Uploader | `st.file_uploader` | `type=["jpg", "jpeg", "png"]`; label "Choose an image" |
| Empty state | `st.info` | Shown when uploader returns `None` |
| Size display | `st.metric` or `st.write` | Bytes count + human-readable string |

## Display contract

When upload present:

```text
File: {filename}
Size: {size_bytes} bytes ({human_readable})
```

Where `{human_readable}` = output of `format_file_size(size_bytes)`.

## Error / edge behavior

| Condition | UI response |
|-----------|---------------|
| No file selected | Info message (not error) |
| 0-byte file | Show `0 bytes (0 B)` |
| Re-upload | Replace previous display |

## Non-goals

- Image preview/thumbnail
- Download or save
- API calls
