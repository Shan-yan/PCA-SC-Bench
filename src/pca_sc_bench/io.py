"""Local JSON and JSONL readers for sanitized score records."""

from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .schema import ScoreRecord


def _records_from_value(value: Any) -> list[ScoreRecord]:
    if isinstance(value, dict):
        value = value.get("records")
    if not isinstance(value, list):
        raise ValueError("JSON input must be an array or an object with a records array")
    records: list[ScoreRecord] = []
    for index, item in enumerate(value):
        if not isinstance(item, Mapping):
            raise ValueError(f"record at index {index} must be a JSON object")
        records.append(ScoreRecord.from_mapping(item))
    return records


def read_records(source: str | Path) -> list[ScoreRecord]:
    """Read score-only records from a UTF-8 JSON or JSONL file."""

    source_path = Path(source)
    if source_path.suffix.lower() == ".jsonl":
        records: list[ScoreRecord] = []
        with source_path.open("r", encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, start=1):
                if not line.strip():
                    continue
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError(f"line {line_number} must contain a JSON object")
                records.append(ScoreRecord.from_mapping(value))
        return records

    with source_path.open("r", encoding="utf-8") as stream:
        return _records_from_value(json.load(stream))
