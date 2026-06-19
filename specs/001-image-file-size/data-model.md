# Data Model: Image Upload File Size

**Feature**: 001-image-file-size | **Date**: 2026-06-03

This feature has no database. All state is ephemeral in the Streamlit session.

## Entities

### UploadedImage (transient)

Represents one user upload for the duration of the browser session.

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| name | string | `uploaded_file.name` | Display only |
| size_bytes | integer | `len(uploaded_file.getvalue())` | Must be >= 0 |
| raw_bytes | bytes | `uploaded_file.getvalue()` | Not persisted; not logged |

**Validation**:
- `size_bytes` MUST equal length of `raw_bytes`
- Empty upload: `size_bytes == 0` — display `"0 B"`, not error

### FileSizeDisplay (derived)

| Field | Type | Derivation |
|-------|------|------------|
| bytes_label | string | `f"{size_bytes:,} bytes"` or similar |
| human_label | string | `format_file_size(size_bytes)` |

## State transitions

```text
[No upload] --user selects file--> [Upload present] --user selects new file--> [Upload present]
     |                                      |
     st.info prompt                         display bytes + human label
```

## Out of scope

- Persistent storage of uploads
- Pixel dimensions (width/height)
- User accounts or sessions beyond Streamlit defaults
