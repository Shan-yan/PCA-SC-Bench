<div align="center">
  <img src="assets/pca-sc-bench-header.svg" alt="PCA-SC-Bench: Perception, Cognition, Action and Safety Consistency" width="100%">

  <br>

  [![Status: Pre-release](https://img.shields.io/badge/status-pre--release-F59E0B?style=flat-square)](#release-status)
  [![Artifacts: Coming soon](https://img.shields.io/badge/artifacts-coming%20soon-475569?style=flat-square)](#planned-release)
  [![License: MIT](https://img.shields.io/badge/license-MIT-14B8A6?style=flat-square)](LICENSE)

  **Evaluating whether multimodal agents remain coherent from scene understanding to safe action.**

  [English](README.md) · [简体中文](README_zh-CN.md)
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

## Release status

> [!IMPORTANT]
> This repository is currently a **public pre-release landing page**. The manuscript and research artifacts are not included at this stage. No benchmark samples, annotations, model outputs, prompts, experimental configurations, quantitative results, or manuscript materials are published here.

We are preparing a documented release designed to support responsible use and reproducible evaluation. Availability will be announced through this repository after the relevant review, licensing, and privacy checks are complete.

## Planned release

The public artifact is expected to include:

- benchmark task and data-format documentation;
- a sanitized evaluation toolkit and configuration examples;
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
