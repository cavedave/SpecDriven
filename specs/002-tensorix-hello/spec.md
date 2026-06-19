# Feature Specification: Tensorix Text Hello World

**Feature Branch**: `002-tensorix-hello`

**Created**: 2026-06-03

**Status**: Draft

**Input**: User description: "Build a standalone python script that talks to tensorix api and asks it what the capital of France is. And publishes its answer to standard output"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask Tensorix one question (Priority: P1)

A developer runs a standalone script locally. The script sends a single question to
the Tensorix LLM API and prints the model's reply to standard output. This proves
API connectivity before adding OCR or Streamlit integration.

**Why this priority**: Without a successful text call, image/OCR features cannot work.
This is the minimum viable Tensorix integration.

**Independent Test**: Run the script with a valid API key in `.env`; stdout contains
"Paris" (case-insensitive acceptable).

**Acceptance Scenarios**:

1. **Given** `TENSORIX_API_KEY` is set in `.env`, **When** the developer runs the
   script, **Then** the script prints the model's answer to standard output.

2. **Given** the script asks "What is the capital of France?", **When** the API
   responds successfully, **Then** the printed answer includes "Paris".

3. **Given** `TENSORIX_API_KEY` is missing, **When** the developer runs the script,
   **Then** the script exits with a clear message explaining how to set the key (not
   an unhandled traceback as the only output).

---

### User Story 2 - Fail gracefully on API errors (Priority: P2)

When the API rejects the request (invalid key, insufficient credits, network failure),
the developer sees a helpful error message.

**Why this priority**: Speeds up setup debugging; required by project constitution
(clear error messages).

**Independent Test**: Run with an invalid key or simulate error; user-facing message
describes the problem.

**Acceptance Scenarios**:

1. **Given** an invalid or expired API key, **When** the script runs, **Then** the
   user sees a clear error message (e.g. authentication or authorization failure).

---

### Edge Cases

- What happens when the API returns an empty response?
  The script MUST report that no content was returned.
- What happens when the network is unreachable?
  The script MUST report a connection or timeout error in plain language.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a standalone script runnable from the command
  line (not via Streamlit).
- **FR-002**: The script MUST send one user message asking what the capital of France
  is to the Tensorix API.
- **FR-003**: The script MUST print the model's reply text to standard output.
- **FR-004**: The script MUST load the API key from environment variables (via `.env`
  in local development).
- **FR-005**: The script MUST NOT print secrets (API keys) to standard output.
- **FR-006**: The script MUST show a clear error when the API key is missing.
- **FR-007**: The script MUST show a clear error when the API returns an error response.
- **FR-008**: The script MUST NOT modify the existing Streamlit image upload app
  (`app.py`) in this feature.

### Key Entities

- **API credential**: Tensorix API key, loaded from `TENSORIX_API_KEY`.
- **Chat request**: Single user message (capital of France question).
- **Chat response**: Model reply text printed to stdout.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: With a valid `.env`, a developer can run the script and see a response
  on stdout within 60 seconds (excluding first-time dependency install).
- **SC-002**: The response text includes "Paris" when asking about the capital of
  France (case-insensitive match acceptable).
- **SC-003**: With no API key configured, the script exits with an instructional
  error message in under 5 seconds without calling the network.
- **SC-004**: No API keys appear in committed project files or in script output.

## Assumptions

- Developer has a Tensorix account with API credits ([app.tensorix.ai](https://app.tensorix.ai)).
- Tensorix exposes an OpenAI-compatible chat completions API.
- Default model is Qwen on Tensorix (exact model ID decided in plan phase; target for
  later OCR is `qwen/qwen3-vl-235b-a22b-instruct`).
- One question per script run is sufficient for hello-world; no conversation history.
- Implementation details (OpenAI SDK, file names, `.env.example`) belong in plan phase.
- Image upload, OCR, and Streamlit UI changes are out of scope for this feature.
