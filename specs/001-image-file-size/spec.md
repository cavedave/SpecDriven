# Feature Specification: Image Upload File Size

**Feature Branch**: `001-image-file-size`

**Created**: 2026-06-03

**Status**: Draft

**Input**: User description: "Install streamlit and build an app that takes an image and tells you its size. use standard streamlit app.py layout. Do not install pillow yet."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - View uploaded image file size (Priority: P1)

A user opens a local web app, uploads an image file, and immediately sees how large
that file is. This proves the upload-and-process path works before adding OCR or
external APIs in later features.

**Why this priority**: This is the entire MVP for Feature 1. Without file size
display, there is no demonstrable value.

**Independent Test**: Upload a known image (e.g. `Japan-Firebombing.jpg`) and
verify the displayed size matches the file size on disk.

**Acceptance Scenarios**:

1. **Given** the app is running locally, **When** the user uploads a JPEG image,
   **Then** the app displays the file size in bytes and in a human-readable form
   (KB or MB as appropriate).

2. **Given** the app is running locally, **When** the user has not uploaded any
   file yet, **Then** the app shows a clear prompt to upload an image (not an
   error or blank screen).

3. **Given** the user uploads an image, **When** the size is shown, **Then** the
   value is greater than zero bytes.

---

### User Story 2 - Restrict uploads to images (Priority: P2)

A user can only select image file types through the upload control, reducing
mistakes before later OCR features.

**Why this priority**: Low-cost guardrail that matches the eventual OCR use case;
not required for the core “size displayed” demo but improves UX.

**Independent Test**: Attempt to upload a non-image file type via the uploader
filter and confirm only image types are offered or accepted.

**Acceptance Scenarios**:

1. **Given** the upload control is visible, **When** the user opens the file
   picker, **Then** only common image formats (e.g. JPEG, PNG) are accepted.

---

### Edge Cases

- What happens when the user uploads a very large image (e.g. tens of MB)?
  The app MUST still display the correct file size without crashing.
- What happens when the user uploads an empty (0-byte) file?
  The app MUST show zero bytes clearly, not fail silently.
- What happens when the user replaces one upload with another?
  The displayed size MUST update to match the new file.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a local web interface where users can upload
  an image file from their device.
- **FR-002**: The system MUST display the uploaded file’s size in bytes.
- **FR-003**: The system MUST display the uploaded file’s size in a human-readable
  unit (KB or MB) alongside the raw byte count.
- **FR-004**: The system MUST show a clear, friendly message when no file has been
  uploaded yet.
- **FR-005**: The upload control MUST restrict selection to image file types.
- **FR-006**: The system MUST update the displayed size when the user uploads a
  different file.
- **FR-007**: The system MUST NOT require network access to external APIs, accounts,
  or databases for this feature.
- **FR-008**: The system MUST NOT use dedicated image-processing libraries beyond
  what is needed to read upload bytes (Pillow explicitly excluded for this feature).

### Key Entities

- **Uploaded image file**: A user-selected image; attributes relevant to this
  feature are file size in bytes and original filename (for display only).
- **File size display**: The presented size in bytes and human-readable units.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can start the app locally and see the upload interface in
  under 1 minute after following README instructions (excluding dependency install
  time on first run).
- **SC-002**: Uploading a test image with a known size on disk shows a displayed
  size that matches exactly (same byte count).
- **SC-003**: 100% of acceptance scenarios in User Story 1 pass on manual test
  with at least one JPEG sample file.
- **SC-004**: When no file is uploaded, the user sees instructional text—not an
  unhandled error or stack trace.

## Assumptions

- Single user on a local developer machine; no multi-user or deployment requirements.
- “File size” means storage size of the uploaded file (bytes on wire), not pixel
  dimensions (width × height).
- Image type filtering uses upload-control constraints (e.g. file extension/MIME
  filter), not deep image decoding libraries.
- Implementation details (Streamlit, `app.py` layout, dependency list) belong in
  the technical plan phase, not this specification.
- A short README note will document how to install dependencies and run the app
  (per project constitution VII).
- OCR, Tensorix API integration, and Pillow are explicitly out of scope for this
  feature and will be specified separately.
