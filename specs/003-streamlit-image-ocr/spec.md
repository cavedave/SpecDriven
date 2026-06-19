# Feature Specification: Streamlit Image Text Extraction

**Feature Branch**: `003-streamlit-image-ocr`

**Created**: 2026-06-03

**Status**: Draft

**Input**: User description: "When the user clicks submit in the streamlit app send the image they have uploaded to the tensorix model and ask the model to return the text contained in the image."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Extract text from uploaded image (Priority: P1)

A user uploads an image in the Streamlit app, clicks Submit, and sees the text
the model finds in that image displayed on the page. This is the core OCR flow for
the project.

**Why this priority**: Primary product goal — image in, text out — building on
Feature 1 (upload) and Feature 2 (Tensorix connectivity).

**Independent Test**: Upload `Japan-Firebombing.jpg`, click Submit, verify the
output includes recognizable city names (e.g. TOKYO) and caption text about B-29
attacks.

**Acceptance Scenarios**:

1. **Given** the app is running and the user has uploaded a JPEG or PNG, **When**
   the user clicks Submit, **Then** the app sends the image to Tensorix and
   displays extracted text on the page.

2. **Given** a successful extraction, **When** results are shown, **Then** the
   displayed text is readable plain text (not raw JSON or binary).

3. **Given** the user has not uploaded an image, **When** the user clicks Submit,
   **Then** the app shows a clear message to upload an image first (no API call).

---

### User Story 2 - Show progress and errors (Priority: P2)

While waiting for the model, the user sees that work is in progress. If the API
fails, the user sees a helpful error—not only a stack trace.

**Why this priority**: OCR calls can take tens of seconds; errors (missing key,
credits, timeout) must be debuggable per constitution.

**Independent Test**: Submit without `.env` key → instructional error; submit with
valid setup → spinner visible during request.

**Acceptance Scenarios**:

1. **Given** a valid upload and Submit clicked, **When** the API request is in
   flight, **Then** the user sees a loading indicator.

2. **Given** `TENSORIX_API_KEY` is missing or invalid, **When** Submit is clicked,
   **Then** the user sees a clear error message on the page.

---

### User Story 3 - Keep file size display (Priority: P3)

The existing file size information remains visible after upload so the user still
sees upload metadata from Feature 1.

**Why this priority**: Preserve working behavior; low effort regression guard.

**Independent Test**: Upload image without clicking Submit — file size still shown.

**Acceptance Scenarios**:

1. **Given** an uploaded image, **When** the page renders, **Then** file name and
   size (bytes and human-readable) are still displayed as in Feature 1.

---

### Edge Cases

- Very large images: app SHOULD still attempt extraction or show a clear message
  if the payload is too large or times out.
- User clicks Submit twice quickly: app SHOULD not duplicate confusing state;
  second click replaces or waits for first request.
- Model returns empty text: app SHOULD show a message that no text was detected.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The Streamlit app MUST retain image upload (jpg/jpeg/png) from Feature 1.
- **FR-002**: The app MUST provide a Submit control to trigger text extraction.
- **FR-003**: On Submit, the app MUST send the uploaded image to the Tensorix vision
  model with a prompt asking for all visible text in the image.
- **FR-004**: The app MUST display the model's text response on the page.
- **FR-005**: The app MUST NOT call Tensorix when no image is uploaded.
- **FR-006**: API credentials MUST load from `.env` (same as Feature 2); never
  displayed in the UI or committed to the repo.
- **FR-007**: The app MUST show user-friendly errors for missing keys and API failures.
- **FR-008**: File size display from Feature 1 MUST remain after upload.

### Key Entities

- **Uploaded image**: Bytes + filename from Streamlit uploader.
- **Extraction request**: Image + instruction to return contained text.
- **Extracted text**: Model reply shown to the user.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: User can upload `Japan-Firebombing.jpg`, click Submit, and see
  extracted text within 120 seconds on a normal connection.
- **SC-002**: Extracted text includes at least three recognizable city labels from
  the test image (e.g. TOKYO, HIROSHIMA, OSAKA) or the bottom caption about
  B-29 incendiary attacks.
- **SC-003**: With no image uploaded, Submit shows guidance without an API call.
- **SC-004**: File size still displays for uploads (Feature 1 regression pass).

## Assumptions

- Tensorix vision model `qwen/qwen3-vl-235b-a22b-instruct` (or `TENSORIX_MODEL` from
  `.env`) supports image+text chat completions.
- Reuse `tensorix_client.py` from Feature 2 where possible; extend for multimodal input.
- Submit is explicit (button), not automatic on upload — avoids surprise API charges.
- Implementation details (base64 encoding, Streamlit `st.button`, prompt wording)
  belong in plan phase.
- Standalone CLI OCR script is out of scope unless needed for testing; focus is
  Streamlit UX.

## Dependencies

- Feature 001: Streamlit upload + file size ([`app.py`](/Users/davidcurran/Documents/tensorix/app.py))
- Feature 002: Tensorix client + `.env` ([`tensorix_client.py`](/Users/davidcurran/Documents/tensorix/tensorix_client.py))
