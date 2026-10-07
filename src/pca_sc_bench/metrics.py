"""Dependency-free aggregation for sanitized PCA-SC score records."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Sequence
from typing import Any

from .schema import METRIC_NAMES, ScoreRecord


def _mean(values: Sequence[float]) -> float | None:
    return sum(values) / len(values) if values else None


def aggregate(records: Iterable[ScoreRecord]) -> dict[str, Any]:
    """Aggregate each public metric independently.

    Missing values are excluded from means and reported through ``count`` and
    ``coverage``. No combined or official overall score is produced.
    """

    materialized = list(records)
    total = len(materialized)
    metrics: dict[str, dict[str, float | int | None]] = {}

    for name in METRIC_NAMES:
        values = [
            value
            for record in materialized
            if (value := record.scores.get(name)) is not None
        ]
        metrics[name] = {
            "mean": _mean(values),
            "count": len(values),
            "coverage": len(values) / total if total else None,
        }

    return {"record_count": total, "metrics": metrics}


def summarize_by_model(records: Iterable[ScoreRecord]) -> dict[str, Any]:
    """Return independent metric summaries grouped by model identifier."""

    groups: dict[str, list[ScoreRecord]] = defaultdict(list)
    for record in records:
        groups[record.model_id].append(record)

    return {
        "schema_version": "0.1",
        "models": {
            model_id: aggregate(groups[model_id])
            for model_id in sorted(groups)
        },
    }
