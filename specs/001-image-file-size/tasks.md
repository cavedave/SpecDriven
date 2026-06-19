---
description: "Task list for Feature 001 — Image Upload File Size"
---

# Tasks: Image Upload File Size

**Input**: Design documents from `specs/001-image-file-size/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/ui-upload-display.md

**Tests**: REQUIRED per constitution — write tests before implementation for `format_file_size`.

**Organization**: Tasks grouped by user story (US1 MVP, US2 image filter, polish).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: User story from spec.md (US1, US2)

## Path Conventions

- Repo root: `app.py`, `file_size.py`, `tests/`, `requirements.txt`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization

- [x] T001 [P] Add `.gitignore` for `.venv`, `.env`, `__pycache__`, `.pytest_cache`
- [x] T002 [P] Create `requirements.txt` with `streamlit>=1.28` and `pytest>=7`
- [x] T003 Create `tests/` directory with `tests/__init__.py` (empty file)

**Checkpoint**: Dependencies installable via `pip install -r requirements.txt`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Testable helper module stub before UI work

- [x] T004 Create `file_size.py` with `format_file_size(size_bytes: int) -> str` stub (raise `NotImplementedError` or return placeholder until T006)

**Checkpoint**: `file_size.py` importable from tests and `app.py`

---

## Phase 3: User Story 1 — View uploaded image file size (Priority: P1) — MVP

**Goal**: Upload image → display byte count + human-readable size; empty-state message.

**Independent Test**: Run `streamlit run app.py`, upload `Japan-Firebombing.jpg`, compare bytes to `ls -l` on disk.

### Tests for User Story 1 (REQUIRED — write first, must fail before implementation)

- [x] T005 [P] [US1] Write tests for `format_file_size` in `tests/test_file_size.py` (0 B, bytes, KB, MB cases per plan.md)
- [x] T006 [US1] Run `pytest -v` and confirm tests fail before implementation

### Implementation for User Story 1

- [x] T007 [US1] Implement `format_file_size` in `file_size.py` (1024-based B/KB/MB, one decimal for KB/MB)
- [x] T008 [US1] Run `pytest -v` and confirm all tests pass
- [x] T009 [US1] Build upload UI in `app.py` (title, uploader, empty `st.info`, display bytes + `format_file_size`, filename)
- [x] T010 [US1] Manual test: upload `Japan-Firebombing.jpg` and verify size matches disk

**Checkpoint**: User Story 1 acceptance scenarios pass (spec.md)

---

## Phase 4: User Story 2 — Restrict uploads to images (Priority: P2)

**Goal**: File picker accepts only jpg/jpeg/png via Streamlit uploader config.

**Independent Test**: Open file picker; non-image types not offered per uploader `type` filter.

### Implementation for User Story 2

- [x] T011 [US2] Set `st.file_uploader(..., type=["jpg", "jpeg", "png"])` in `app.py` per contracts/ui-upload-display.md
- [x] T012 [US2] Manual test: confirm uploader restricts to image extensions

**Checkpoint**: FR-005 satisfied

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and quickstart validation

- [x] T013 [P] Update `readme.md` with run/test commands for this feature (if not already complete)
- [x] T014 Run validation steps in `specs/001-image-file-size/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001–T002 done; finish T003
- **Foundational (Phase 2)**: T004 after T003 — blocks US1 implementation
- **User Story 1 (Phase 3)**: T005 → T006 → T007 → T008 → T009 → T010
- **User Story 2 (Phase 4)**: T011 after T009 (extends `app.py`); may merge with T009 if uploader types set initially
- **Polish (Phase 5)**: After US1 (MVP) or after US2

### User Story Dependencies

- **US1 (P1)**: No dependency on US2 — delivers MVP alone
- **US2 (P2)**: Depends on `app.py` from US1

### Within User Story 1

1. Tests (T005) MUST be written and fail (T006) before T007
2. T007–T008 before T009 (app imports working `format_file_size`)
3. T010 manual validation last in US1

### Parallel Opportunities

- T001 and T002 were parallel (already complete)
- T005 can start once T004 stub exists
- T013 can run in parallel with T011–T012

---

## Parallel Example: User Story 1

```bash
# After T004 stub exists:
# T005: write tests/test_file_size.py

# Sequential after tests written:
pytest -v          # T006 fail → T007 implement → T008 pass → T009 app.py
```

---

## Implementation Strategy

### MVP First (User Story 1 only)

1. Complete T003–T004
2. T005 → T008 (test-first helper)
3. T009 → T010 (Streamlit UI + manual check)
4. **STOP and VALIDATE** — demo upload + file size

### Incremental Delivery

1. US1 complete → MVP shippable
2. Add US2 (T011–T012) → image-type filter
3. Polish (T013–T014) → docs + quickstart

---

## Notes

- User-requested core tasks map to: **T005** (tests), **T007** (implement helper; was T005 in user list), **T009** (app.py; was T006 in user list). IDs shifted to include setup/foundational phases.
- Do not import or use Pillow in application code (FR-008).
- Edge cases (0-byte file, re-upload) handled in T009 via `len(uploaded_file.getvalue())`.

---

## Task Summary

| Phase | Tasks | Story |
|-------|-------|-------|
| Setup | T001–T003 | — |
| Foundational | T004 | — |
| US1 MVP | T005–T010 | US1 |
| US2 | T011–T012 | US2 |
| Polish | T013–T014 | — |

**Total**: 14 tasks (14 complete)

**MVP scope**: T003–T010 (User Story 1)

**Parallel opportunities**: T005 [P], T013 [P]
