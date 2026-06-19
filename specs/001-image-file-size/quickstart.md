# Quickstart: Image Upload File Size

**Feature**: 001-image-file-size

Validate the feature end-to-end after implementation.

## Prerequisites

- Python 3.10+
- Repo root: `/Users/davidcurran/Documents/tensorix`

## Setup

```bash
cd /Users/davidcurran/Documents/tensorix
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run unit tests

```bash
pytest -v
```

**Expected**: All tests in `tests/test_file_size.py` pass.

## Run the app

```bash
streamlit run app.py
```

**Expected**: Browser opens; upload control visible; info message when empty.

## Manual acceptance (User Story 1)

1. Upload `Japan-Firebombing.jpg` from repo root.
2. Note file size on disk: `ls -l Japan-Firebombing.jpg` (bytes column on macOS).
3. Compare to displayed byte count — MUST match exactly.
4. Confirm human-readable label is shown (KB or MB).

## Manual acceptance (empty state)

1. Reload app without uploading.
2. **Expected**: Instructional info text, no stack trace.

## Manual acceptance (P2 — image filter)

1. Open file picker on uploader.
2. **Expected**: Only image types offered (jpg/jpeg/png per uploader config).

## References

- Spec: [spec.md](../spec.md)
- UI contract: [ui-upload-display.md](./ui-upload-display.md)
- Data model: [data-model.md](../data-model.md)
