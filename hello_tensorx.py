#!/usr/bin/env python3
"""Hello-world script: ask TensorX a question and print the answer."""

from __future__ import annotations

import argparse
import sys

from tensorx_client import TensorxError, ask

DEFAULT_QUESTION = "What is the capital of France?"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ask TensorX a question and print the answer."
    )
    parser.add_argument(
        "--question",
        default=DEFAULT_QUESTION,
        help=f"Question to send (default: {DEFAULT_QUESTION!r})",
    )
    args = parser.parse_args()

    try:
        answer = ask(args.question)
    except TensorxError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
