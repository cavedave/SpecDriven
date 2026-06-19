---
description: "Task list for Feature 002 — Tensorix Text Hello World"
---

# Tasks: Tensorix Text Hello World

**Input**: Design documents from `specs/002-tensorix-hello/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli-hello-tensorix.md

**Tests**: REQUIRED — mock-based tests before live API wiring (constitution III).

**Organization**: User stories US1 (hello + Paris), US2 (API errors), polish.

## Path Conventions

- Repo root: `tensorix_client.py`, `hello_tensorix.py`, `.env.example`, `requirements.txt`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Dependencies and env template

- [x] T001 [P] Add `openai>=1.0` and `python-dotenv>=1.0` to `requirements.txt`
- [x] T002 [P] Create `.env.example` with `TENSORIX_API_KEY=` and `TENSORIX_MODEL=qwen/qwen3-vl-235b-a22b-instruct`

**Checkpoint**: Dependencies installable via `pip install -r requirements.txt`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Client module stub importable from tests

- [x] T003 Create `tensorix_client.py` with function stubs: `get_api_key()`, `get_model()`, `ask()` raising `NotImplementedError` until implemented

**Checkpoint**: `from tensorix_client import get_api_key` works in tests

---

## Phase 3: User Story 1 — Ask Tensorix one question (Priority: P1) — MVP

**Goal**: Run script → ask capital of France → print answer containing Paris.

**Independent Test**: `python hello_tensorix.py` with valid `.env`; stdout contains `Paris`.

### Tests for User Story 1 (REQUIRED — write first)

- [x] T004 [P] [US1] Write `tests/test_tensorix_client.py`: missing `TENSORIX_API_KEY` raises clear error in `get_api_key()`
- [x] T005 [P] [US1] Add test: mocked OpenAI client returns "Paris" from `ask("What is the capital of France?")`
- [x] T006 [US1] Run `pytest tests/test_tensorix_client.py -v` — confirm tests fail until T007–T008

### Implementation for User Story 1

- [x] T007 [US1] Implement `tensorix_client.py`: dotenv load, `get_api_key()`, `get_model()`, `create_client()`, `ask()` using `base_url=https://api.tensorix.ai/v1`
- [x] T008 [US1] Run `pytest tests/test_tensorix_client.py -v` — all tests pass
- [x] T009 [US1] Implement `hello_tensorix.py`: argparse `--question`, default capital-of-France prompt, print to stdout
- [x] T010 [US1] Live run: `python hello_tensorix.py` — stdout contains Paris (case-insensitive)

**Checkpoint**: US1 acceptance scenarios pass

---

## Phase 4: User Story 2 — Fail gracefully on API errors (Priority: P2)

**Goal**: Clear stderr messages for auth/API failures; no raw traceback-only output.

**Independent Test**: Mock or invalid key produces readable error on stderr, exit 1.

### Tests for User Story 2

- [x] T011 [P] [US2] Add test: mocked `AuthenticationError` from OpenAI SDK maps to clear error message
- [x] T012 [P] [US2] Add test: empty `message.content` raises or returns handled error

### Implementation for User Story 2

- [x] T013 [US2] Wire error handling in `tensorix_client.py` and `hello_tensorix.py` (stderr + exit 1)
- [x] T014 [US2] Run `pytest -v` — all tests pass

**Checkpoint**: FR-006, FR-007 satisfied

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Documentation; confirm no `app.py` changes

- [x] T015 [P] Update `readme.md` with Tensorix hello-world commands (see `quickstart.md`)
- [x] T016 Verify `app.py` unchanged; run full `pytest -v`
- [x] T017 Run validation checklist in `specs/002-tensorix-hello/quickstart.md`

---

## Dependencies & Execution Order

- **Phase 1** → **Phase 2** → **Phase 3** (T004–T006 before T007) → **Phase 4** → **Phase 5**
- **US1** does not depend on US2 for MVP; stop after T010 for minimal demo
- **Do not modify** `app.py` (FR-008)

---

## Task Summary

| Phase | Tasks | Story |
|-------|-------|-------|
| Setup | T001–T002 | — |
| Foundational | T003 | — |
| US1 MVP | T004–T010 | US1 |
| US2 | T011–T014 | US2 |
| Polish | T015–T017 | — |

**Total**: 17 tasks (17 complete)

**MVP scope**: T001–T010 (User Story 1)
