"""Public score-record schema.

This module intentionally contains no benchmark samples, judging prompts, or
experiment-specific configuration.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

METRIC_NAMES = ("P", "C", "A", "Safety", "PC", "CA", "PA")


@dataclass(frozen=True)
class ScoreRecord:
    """A validated, model-and-sample-level collection of public PCA-SC scores.

    Values may be omitted with ``None``. Present values must lie in ``[0, 1]``.
    The record stores no raw model output, prompt, image, or reference answer.
    """

    sample_id: str
    model_id: str
    scores: Mapping[str, float | None] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.sample_id.strip():
            raise ValueError("sample_id must not be empty")
        if not self.model_id.strip():
            raise ValueError("model_id must not be empty")

        unknown = sorted(set(self.scores) - set(METRIC_NAMES))
        if unknown:
            raise ValueError(f"unknown metric name(s): {', '.join(unknown)}")

        normalized: dict[str, float | None] = {}
        for name, value in self.scores.items():
            if value is None:
                normalized[name] = None
                continue
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be a number in [0, 1] or None")
            numeric = float(value)
            if not 0.0 <= numeric <= 1.0:
                raise ValueError(f"{name} must be in [0, 1], got {numeric}")
            normalized[name] = numeric

        object.__setattr__(self, "sample_id", self.sample_id.strip())
        object.__setattr__(self, "model_id", self.model_id.strip())
        object.__setattr__(self, "scores", normalized)

    @classmethod
    def from_mapping(cls, item: Mapping[str, Any]) -> "ScoreRecord":
        """Build a record from a flat or nested JSON-compatible mapping."""

        nested = item.get("scores")
        if nested is not None:
            if not isinstance(nested, Mapping):
                raise TypeError("scores must be an object")
            scores = dict(nested)
        else:
            scores = {name: item.get(name) for name in METRIC_NAMES if name in item}

        sample_id = item.get("sample_id", "")
        model_id = item.get("model_id", "")
        if not isinstance(sample_id, str):
            raise TypeError("sample_id must be a string")
        if not isinstance(model_id, str):
            raise TypeError("model_id must be a string")

        return cls(
            sample_id=sample_id,
            model_id=model_id,
            scores=scores,
        )

    def to_mapping(self) -> dict[str, Any]:
        """Return a JSON-compatible representation."""

        return {
            "sample_id": self.sample_id,
            "model_id": self.model_id,
            "scores": dict(self.scores),
        }
