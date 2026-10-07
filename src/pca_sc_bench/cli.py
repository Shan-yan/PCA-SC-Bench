"""Command-line entry point for local score aggregation."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from .io import read_records
from .metrics import summarize_by_model


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pca-sc-eval",
        description="Summarize sanitized PCA-SC score records by model.",
    )
    parser.add_argument("input", help="Path to a score-only JSON or JSONL file")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Indent the JSON summary for human-readable output",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    summary = summarize_by_model(read_records(args.input))
    print(json.dumps(summary, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
