"""Tests use synthetic records only; no benchmark artifacts are included."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from pca_sc_bench import ScoreRecord, aggregate, summarize_by_model
from pca_sc_bench.cli import main
from pca_sc_bench.io import read_records


class ScoreRecordTests(unittest.TestCase):
    def test_normalizes_valid_values(self) -> None:
        record = ScoreRecord(" synthetic-001 ", " demo ", {"P": 1, "C": None})
        self.assertEqual(record.sample_id, "synthetic-001")
        self.assertEqual(record.model_id, "demo")
        self.assertEqual(record.scores, {"P": 1.0, "C": None})

    def test_rejects_out_of_range_values(self) -> None:
        with self.assertRaises(ValueError):
            ScoreRecord("synthetic-001", "demo", {"Safety": 1.1})

    def test_rejects_unknown_metrics(self) -> None:
        with self.assertRaises(ValueError):
            ScoreRecord("synthetic-001", "demo", {"overall": 0.5})

    def test_mapping_rejects_non_string_identifiers(self) -> None:
        with self.assertRaises(TypeError):
            ScoreRecord.from_mapping({"sample_id": 1, "model_id": "demo"})


class AggregationTests(unittest.TestCase):
    def test_aggregate_reports_coverage(self) -> None:
        records = [
            ScoreRecord("synthetic-001", "demo", {"P": 1.0, "A": 0.0}),
            ScoreRecord("synthetic-002", "demo", {"P": None, "A": 1.0}),
        ]
        summary = aggregate(records)
        self.assertEqual(summary["record_count"], 2)
        self.assertEqual(summary["metrics"]["P"]["mean"], 1.0)
        self.assertEqual(summary["metrics"]["P"]["coverage"], 0.5)
        self.assertEqual(summary["metrics"]["A"]["mean"], 0.5)

    def test_summary_keeps_models_separate(self) -> None:
        records = [
            ScoreRecord("synthetic-001", "alpha", {"P": 1.0}),
            ScoreRecord("synthetic-002", "beta", {"P": 0.0}),
        ]
        summary = summarize_by_model(records)
        self.assertEqual(list(summary["models"]), ["alpha", "beta"])
        self.assertNotIn("overall", summary)

    def test_reads_nested_json(self) -> None:
        payload = {
            "records": [
                {
                    "sample_id": "synthetic-001",
                    "model_id": "demo",
                    "scores": {"P": 1.0, "Safety": 0.5},
                }
            ]
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "records.json"
            source.write_text(json.dumps(payload), encoding="utf-8")
            records = read_records(source)
        self.assertEqual(records[0].scores["Safety"], 0.5)

    def test_cli_emits_model_summary(self) -> None:
        payload = [
            {
                "sample_id": "synthetic-001",
                "model_id": "demo",
                "P": 1.0,
            }
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "records.json"
            source.write_text(json.dumps(payload), encoding="utf-8")
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = main([str(source)])
        self.assertEqual(exit_code, 0)
        self.assertEqual(json.loads(stdout.getvalue())["models"]["demo"]["record_count"], 1)


if __name__ == "__main__":
    unittest.main()
