# Workshop documentation

Materials for the SpecDriven TensorX workshop.

## Slides

| File | Description |
|------|-------------|
| [Tensorx.pdf](Tensorx.pdf) | Talk slides (PDF export from Keynote) |
| `Tensorx.key` | Keynote source — macOS only |

## Spec-driven development loop

The **GitHub starter** is intentionally bare: only vision + smoke test + Spec Kit tooling. During the workshop you create each feature folder with [Spec Kit](https://github.com/github/spec-kit):

| Step | What you build | Spec folder (created live) |
|------|----------------|----------------------------|
| **001** | Receipt ingest — upload + file size | `specs/001-image-file-size/` |
| Smoke test | TensorX text hello | README — `hello_tensorx.py` (already in repo) |
| **002** | Receipt OCR — **Extract text** | `specs/002-receipt-ocr/` |
| **003** *(optional)* | Purchase analysis | `specs/003-purchase-analysis/` |

Loop: `constitution → specify → plan → tasks → implement → test/review → refine → repeat`

See [constitution](../.specify/memory/constitution.md) and product vision [specs/000-receipt-reader/vision.md](../specs/000-receipt-reader/vision.md).

## Further reading

- [Spec-Driven Development (Leanpub)](https://leanpub.com/spec-driven-development-build-with-ai)
- [TensorX API docs](https://docs.tensorx.ai/)
