# Quickstart: Streamlit Image OCR

**Feature**: 003-streamlit-image-ocr

## Prerequisites

- Features 001–002 complete
- `.env` with valid `TENSORIX_API_KEY` and `TENSORIX_MODEL=qwen/qwen3-vl-235b-a22b-instruct`
- Venv active, dependencies installed

## Unit tests

```bash
cd /Users/davidcurran/Documents/tensorix
source .venv/bin/activate
pytest tests/test_tensorix_client.py -v
```

**Expected**: Multimodal mock tests pass (no live API).

## Manual E2E

```bash
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```

1. Upload `Japan-Firebombing.jpg` from repo root
2. Confirm file size still shows
3. Click **Extract text**
4. Wait for spinner (may take 30–120 seconds)
5. **Expected**: Extracted text includes city names (e.g. TOKYO, HIROSHIMA) and/or B-29 caption

## No-upload check

1. Reload app without uploading
2. Click **Extract text**
3. **Expected**: Warning to upload first; no API call

## References

- [spec.md](../spec.md)
- [streamlit-ocr-ui.md](./streamlit-ocr-ui.md)
