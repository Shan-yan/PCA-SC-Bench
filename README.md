<div align="center">
  <img src="assets/pca-sc-bench-header.svg" alt="PCA-SC-Bench: Perception, Cognition, Action and Safety Consistency" width="100%">

  <br>

  [![Status: Pre-release](https://img.shields.io/badge/status-pre--release-F59E0B?style=flat-square)](#release-status)
  [![Code: Public preview](https://img.shields.io/badge/code-public%20preview-38BDF8?style=flat-square)](#code-preview)
  [![Website: Online](https://img.shields.io/badge/website-research%20atlas-5EEAD4?style=flat-square)](https://gomagichub.com/pcascshow/)
  [![License: MIT](https://img.shields.io/badge/license-MIT-14B8A6?style=flat-square)](LICENSE)

  **Evaluating whether multimodal agents remain coherent from scene understanding to safe action.**

  [Explore the Research Atlas](https://gomagichub.com/pcascshow/) · [English](README.md) · [简体中文](README_zh-CN.md)
</div>

---

## Overview

PCA-SC-Bench is a research benchmark for studying the **Perception–Cognition–Action** chain and its **Safety Consistency** in visually grounded decision-making. The project focuses on a simple but important question: does an agent not only understand a scene and reason about it, but also choose an action that remains consistent with that understanding and with safety constraints?

The current research setting centers on safety-aware decision-making in station-like public environments. The framework separates evaluation into complementary views:

| Dimension | What it examines |
|:--|:--|
| **Perception** | Whether relevant scene conditions and potential hazards are recognized |
| **Cognition** | Whether goals, constraints, and safety implications are reasoned about coherently |
| **Action** | Whether the selected action is appropriate for the situation |
| **Safety Consistency** | Whether understanding, reasoning, and action remain aligned under safety constraints |

For the interactive project overview, methodology atlas, and visual walkthrough, visit the **[PCA-SC Bench Research Atlas](https://gomagichub.com/pcascshow/)**.

## Release status

> [!IMPORTANT]
> This repository is currently a **public pre-release**. It includes a small, sanitized code preview, but no benchmark samples, annotations, model outputs, prompts, experimental configurations, quantitative results, or manuscript materials.

We are preparing a documented release designed to support responsible use and reproducible evaluation. Further availability will be announced through this repository after the relevant review, licensing, and privacy checks are complete.

## Code preview

The code under [`src/pca_sc_bench`](src/pca_sc_bench) is an intentionally limited, dependency-free preview of the public evaluation interface. It currently provides:

- validated score records for the public PCA-SC dimensions;
- per-metric aggregation with missing-value coverage;
- summaries grouped by model identifier; and
- local JSON or JSONL input through a small command-line interface.

It does **not** include benchmark data, prompts, online inference, automated judging, experiment orchestration, internal configurations, or reported results.

### Install and test

Python 3.9 or newer is required.

```bash
python -m pip install .
python -m unittest discover -s tests -v
```

### Minimal example

```python
from pca_sc_bench import ScoreRecord, aggregate

# Synthetic values for API demonstration only; these are not benchmark results.
records = [
    ScoreRecord(
        sample_id="synthetic-001",
        model_id="demo-model",
        scores={"P": 1.0, "C": 1.0, "A": 0.0, "Safety": 1.0},
    )
]

print(aggregate(records))
```

To summarize a local, sanitized JSON or JSONL file after installation:

```bash
pca-sc-eval path/to/records.jsonl --pretty
```

See [CODE_RELEASE.md](CODE_RELEASE.md) for the current publication boundary and input format.

## Planned release

The public artifact is expected to include:

- benchmark task and data-format documentation;
- the complete sanitized evaluation toolkit and configuration examples;
- data and model cards covering intended use and limitations;
- reproducibility instructions and validated reference workflows; and
- citation information associated with the final publication.

The exact release scope may change following review and compliance checks. No release date is promised yet.

## Responsible use

PCA-SC-Bench is intended for research on evaluation, robustness, and safety-aware decision-making. Benchmark scores should not be treated as proof that a model is safe for deployment in a real public environment. Real-world deployment requires independent validation, domain expertise, and appropriate operational safeguards.

Please do not use this repository to request non-public datasets, manuscript drafts, reviewer materials, credentials, or unpublished results. Security or privacy concerns should be reported privately as described in [SECURITY.md](SECURITY.md).

## Contributing

The benchmark artifacts are not yet open for external contributions. Documentation corrections and non-sensitive suggestions are welcome; please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Citation

Citation metadata will be added when the associated work is publicly available. Until then, please link to this repository rather than creating an unofficial citation.

## License

The material currently present in this repository is available under the [MIT License](LICENSE). Future benchmark data, images, annotations, model outputs, and other research artifacts may be released under separate terms; their licenses will be stated explicitly at release time.

---

<div align="center">
  <sub>Built for careful evaluation. Released only when the artifacts are ready.</sub>
</div>
