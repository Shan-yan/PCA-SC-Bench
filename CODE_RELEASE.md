# Public code preview

This repository currently publishes a small, sanitized interface for working with already-scored PCA-SC records. It is intended to make the future package shape inspectable without releasing private research artifacts prematurely.

## Included

- `ScoreRecord`, a score-only record with range validation;
- independent aggregation for `P`, `C`, `A`, `Safety`, `PC`, `CA`, and `PA`;
- missing-value counts and coverage;
- per-model summaries; and
- local JSON and JSONL reading plus a command-line interface.

No official combined score is calculated by this preview.

## Not included

The preview does not contain benchmark samples or images, reference annotations, prompts, raw model responses, judge implementations, model-provider integrations, experiment configurations, internal paths, credentials, result tables, plots, or manuscript text.

## Input format

The command-line interface accepts either a JSON array, an object containing a `records` array, or one object per line in JSONL. Each record must contain non-empty `sample_id` and `model_id` strings. Scores may be nested under `scores` or supplied as top-level metric keys.

```json
{
  "sample_id": "synthetic-001",
  "model_id": "demo-model",
  "scores": {
    "P": 1.0,
    "C": 1.0,
    "A": 0.0,
    "Safety": 1.0,
    "PC": null,
    "CA": null,
    "PA": null
  }
}
```

The object above is synthetic and illustrates the file format only. It is not a benchmark sample or experimental result.
