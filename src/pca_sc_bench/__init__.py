"""Sanitized public interface preview for PCA-SC Bench."""

from .metrics import aggregate, summarize_by_model
from .schema import METRIC_NAMES, ScoreRecord

__all__ = ["METRIC_NAMES", "ScoreRecord", "aggregate", "summarize_by_model"]
__version__ = "0.1.0"
