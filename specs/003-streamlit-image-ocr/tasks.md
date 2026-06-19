---
description: "Task list for Feature 003 — Streamlit Image Text Extraction"
---

# Tasks: Streamlit Image Text Extraction

**Input**: Design documents from `specs/003-streamlit-image-ocr/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/streamlit-ocr-ui.md

**Tests**: REQUIRED — mock multimodal tests before client/UI implementation (constitution III).

**Organization**: User stories US1 (OCR flow), US2 (spinner + errors), US3 (file size regression), polish.

## Path Conventions

- Repo root: `app.py`, `tensorix_client.py`, `file_size.py`, `tests/test_tensorix_client.py`, `readme.md`
- Test asset: `Japan-Firebombing.jpg` (repo root)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Confirm dependencies and test asset from Features 001–002

- [x] T001 Verify `requirements.txt` includes `streamlit`, `openai`, `python-dotenv`, `pytest` (no new packages expected)
- [x] T002 [P] Confirm `Japan-Firebombing.jpg` exists at repo root for manual E2E

**Checkpoint**: `pip install -r requirements.txt` and test image available

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Client stub importable; tests can target `extract_text_from_image` before full implementation

- [x] T003 Add to `tensorix_client.py`: `OCR_PROMPT` constant, `mime_from_filename(name: str) -> str`, and `extract_text_from_image(image_bytes, mime_type, *, client=None)` stub raising `NotImplementedError`

**Checkpoint**: `from tensorix_client import extract_text_from_image` works in tests

---

## Phase 3: User Story 1 — Extract text from uploaded image (Priority: P1) — MVP

**Goal**: Upload image → click Extract text → see model OCR output on page.

**Independent Test**: Upload `Japan-Firebombing.jpg`, click Extract text; output includes city names (e.g. TOKYO) or B-29 caption.

### Tests for User Story 1 (REQUIRED — write first)

- [x] T004 [P] [US1] Add test in `tests/test_tensorix_client.py`: mocked client returns text containing `TOKYO` from `extract_text_from_image(b"fake", "image/jpeg")`
- [x] T005 [P] [US1] Add test: assert `chat.completions.create` called with multimodal `content` array (`type: text` + `type: image_url` with base64 data URL)
- [x] T006 [P] [US1] Add test: empty `image_bytes` raises `TensorixError`
- [x] T007 [US1] Run `pytest tests/test_tensorix_client.py -v` — confirm new tests fail until T008

### Implementation for User Story 1

- [x] T008 [US1] Implement `extract_text_from_image()` in `tensorix_client.py`: base64 data URL, multimodal messages, `max_tokens=4096`, `temperature=0`, reuse error handling from `ask()`
- [x] T009 [US1] Run `pytest tests/test_tensorix_client.py -v` — multimodal tests pass
- [x] T010 [US1] Update `app.py`: import `extract_text_from_image`, `mime_from_filename`, `TensorixError`; add **Extract text** button; on click with upload call client and show `st.subheader` + `st.text_area`; on click without upload show `st.warning("Upload an image first.")` (no API call)
- [x] T011 [US1] Live E2E: `streamlit run app.py`, upload `Japan-Firebombing.jpg`, Extract text — output includes recognizable map text (SC-002)

**Checkpoint**: US1 acceptance scenarios pass (FR-002–FR-005)

---

## Phase 4: User Story 2 — Show progress and errors (Priority: P2)

**Goal**: Spinner during OCR; clear `st.error` for missing key / API failures.

**Independent Test**: Submit with valid setup shows spinner; missing/invalid key shows instructional error (no raw traceback).

### Tests for User Story 2

- [x] T012 [P] [US2] Add test: `extract_text_from_image` with mocked empty `message.content` raises `TensorixError`
- [x] T013 [P] [US2] Add test: mocked `AuthenticationError` on multimodal call maps to clear authentication message

### Implementation for User Story 2

- [x] T014 [US2] Wrap API call in `app.py` with `st.spinner("Extracting text from image...")`
- [x] T015 [US2] Catch `TensorixError` in `app.py` and display `st.error(str(exc))` (no uncaught traceback)
- [x] T016 [US2] Run `pytest -v` — all tests pass

**Checkpoint**: US2 acceptance scenarios pass (FR-007)

---

## Phase 5: User Story 3 — Keep file size display (Priority: P3)

**Goal**: Feature 1 upload metadata unchanged when OCR UI is added.

**Independent Test**: Upload image without clicking Extract text — file name and size still shown.

### Implementation for User Story 3

- [x] T017 [US3] Verify `app.py` retains Feature 1 block: `format_file_size`, file name, bytes + human-readable size after upload (adjust layout only if needed; no regression)
- [x] T018 [US3] Manual regression: upload only, no Submit — size display matches Feature 001 behavior (SC-004)

**Checkpoint**: FR-008 satisfied

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, copy, full validation

- [x] T019 [P] Update `readme.md` with Streamlit OCR usage (upload, Extract text, `.env` vars) per `quickstart.md`
- [x] T020 [P] Update `app.py` title/caption to reflect image text extraction (per plan Phase C optional)
- [x] T021 Run full `pytest -v` (file_size + tensorix_client)
- [x] T022 Run validation checklist in `specs/003-streamlit-image-ocr/quickstart.md`

---

## Dependencies & Execution Order

- **Phase 1** → **Phase 2** → **Phase 3** (T004–T007 before T008) → **Phase 4** → **Phase 5** → **Phase 6**
- **US1** MVP: stop after T011 for first working OCR demo
- **US2** depends on US1 `app.py` wiring (T010) for spinner/error UI
- **US3** is a regression check on T010 layout — can run in parallel with US2 tests after T010

### Parallel opportunities

```bash
# US1 tests together (T004–T006):
pytest tests/test_tensorix_client.py -k extract  # after T004–T006 written

# US2 tests together (T012–T013):
pytest tests/test_tensorix_client.py -k "empty_response or authentication"
```

---

## Task Summary

| Phase | Tasks | Story |
|-------|-------|-------|
| Setup | T001–T002 | — |
| Foundational | T003 | — |
| US1 MVP | T004–T011 | US1 |
| US2 | T012–T016 | US2 |
| US3 | T017–T018 | US3 |
| Polish | T019–T022 | — |

**Total**: 22 tasks (22 complete)

**MVP scope**: T001–T011 (User Story 1)
