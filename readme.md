# SpecDriven — Tensorix workshop

Spec-driven development workshop using the [Tensorix API](https://docs.tensorix.ai/). Target vision model: `qwen/qwen3-vl-235b-a22b-instruct`.

Repo: [github.com/cavedave/SpecDriven](https://github.com/cavedave/SpecDriven)

Development uses [Spec Kit](https://github.com/github/spec-kit): constitution → specify → plan → tasks → implement → test/review → refine spec → repeat.

https://leanpub.com/spec-driven-development-build-with-ai

## Workshop slides

Open `Tensorix.key` in Keynote (macOS) for the accompanying talk.

## Setup (virtual environment)

From the project root, create and activate a venv:

```bash
git clone https://github.com/cavedave/SpecDriven.git
cd SpecDriven
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To leave the venv:

```bash
deactivate
```

## Secrets

Copy the example env file and add your key (never commit `.env`):

```bash
cp .env.example .env
# Edit .env: set TENSORIX_API_KEY
```

Get a key from [app.tensorix.ai](https://app.tensorix.ai).

## Tensorix hello world

Prove API connectivity with a one-line question:

```bash
source .venv/bin/activate
python hello_tensorix.py
```

Expected: stdout includes **Paris**.

Custom question:

```bash
python hello_tensorix.py --question "What is the capital of Ireland?"
```

See [specs/002-tensorix-hello/quickstart.md](specs/002-tensorix-hello/quickstart.md).

## Image text extraction (Streamlit)

Upload an image and extract visible text with the Tensorix vision model:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```

Use `python -m streamlit` (not bare `streamlit`) so the app runs with the same Python as your venv. If you see `ModuleNotFoundError: dotenv`, you are likely using Homebrew’s Streamlit instead of the venv.

1. Upload a JPEG or PNG — use the workshop test receipt at `images/2026.06.09_170002748320260609132561.jpg.png` (Lidl grocery receipt).
2. Confirm file name and size are shown.
3. Click **Extract text** and wait for the spinner to finish.
4. Read extracted text in the text area below.

**Expected output** includes recognizable receipt text, e.g. **Lidl**, **Tyrrelstown**, item names (Peri Chicken, Cucumber, etc.), and a total around **46.50 EUR**.

Requires `.env` with `TENSORIX_API_KEY` and optionally `TENSORIX_MODEL` (default: `qwen/qwen3-vl-235b-a22b-instruct`).

See [specs/003-streamlit-image-ocr/quickstart.md](specs/003-streamlit-image-ocr/quickstart.md).

File name and size (Feature 001) still display after upload. Try the same test image: `images/2026.06.09_170002748320260609132561.jpg.png`. See [specs/001-image-file-size/quickstart.md](specs/001-image-file-size/quickstart.md).

## Test

```bash
source .venv/bin/activate
pytest -v
```
