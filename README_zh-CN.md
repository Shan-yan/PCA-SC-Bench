<div align="center">
  <img src="assets/pca-sc-bench-header.svg" alt="PCA-SC-Bench：感知、认知、行动与安全一致性评测" width="100%">

  <br>

  [![状态：预发布](https://img.shields.io/badge/status-pre--release-F59E0B?style=flat-square)](#发布状态)
  [![代码：公开预览](https://img.shields.io/badge/code-public%20preview-38BDF8?style=flat-square)](#代码预览)
  [![展示网页：已上线](https://img.shields.io/badge/website-research%20atlas-5EEAD4?style=flat-square)](https://gomagichub.com/pcascshow/)
  [![许可证：MIT](https://img.shields.io/badge/license-MIT-14B8A6?style=flat-square)](LICENSE)

  **评估多模态智能体能否从场景理解一贯地走向安全行动。**

  [浏览研究图谱](https://gomagichub.com/pcascshow/) · [English](README.md) · [简体中文](README_zh-CN.md)
</div>

---

## 项目概览

PCA-SC-Bench 是一项研究型基准，用于分析视觉场景决策中的**感知–认知–行动**链路及其**安全一致性**。项目关注一个简单但重要的问题：智能体不仅要能理解场景并进行推理，其最终行动是否也能与理解结果及安全约束保持一致？

当前研究场景聚焦于车站类公共环境中的安全决策。评测框架从以下互补视角进行分析：

| 维度 | 关注内容 |
|:--|:--|
| **感知** | 能否识别与任务相关的场景条件和潜在风险 |
| **认知** | 能否对目标、约束与安全影响进行连贯推理 |
| **行动** | 所选行动是否符合当前情境 |
| **安全一致性** | 感知、推理与行动在安全约束下是否保持一致 |

交互式项目概览、方法图谱与可视化演示请访问 **[PCA-SC Bench Research Atlas](https://gomagichub.com/pcascshow/)**。

## 发布状态

> [!IMPORTANT]
> 本仓库目前处于**公开预发布**阶段。仓库包含小型脱敏代码预览，但不包含基准样本、标注、模型输出、提示词、实验配置、定量结果或稿件材料。

团队正在准备兼顾责任使用与可复现性的公开版本。待相关评审、授权与隐私检查完成后，将通过本仓库公布更多可用性信息。

## 代码预览

[`src/pca_sc_bench`](src/pca_sc_bench) 中的代码是一份刻意保持最小化、不依赖第三方库的公开评测接口预览，目前提供：

- PCA-SC 公开维度的评分记录与区间校验；
- 支持缺失值覆盖率的逐指标聚合；
- 按模型标识符分组的摘要；
- 通过轻量命令行接口读取本地 JSON 或 JSONL。

它**不包含**基准数据、提示词、在线推理、自动判分、实验编排、内部配置或已报告结果。

### 安装与测试

需要 Python 3.9 或更高版本。

```bash
python -m pip install .
python -m unittest discover -s tests -v
```

### 最小示例

```python
from pca_sc_bench import ScoreRecord, aggregate

# 仅为演示 API 而构造的合成值，不是基准实验结果。
records = [
    ScoreRecord(
        sample_id="synthetic-001",
        model_id="demo-model",
        scores={"P": 1.0, "C": 1.0, "A": 0.0, "Safety": 1.0},
    )
]

print(aggregate(records))
```

安装后，可以通过以下命令汇总本地已脱敏的 JSON 或 JSONL 文件：

```bash
pca-sc-eval path/to/records.jsonl --pretty
```

当前代码公开边界与输入格式见 [CODE_RELEASE.md](CODE_RELEASE.md)。

## 计划公开内容

未来的公开资料预计包含：

- 基准任务与数据格式说明；
- 完整的脱敏评测工具和配置示例；
- 说明预期用途和局限性的数据卡与模型卡；
- 可复现说明与经验证的参考流程；
- 与最终发表版本对应的引用信息。

具体公开范围可能根据评审与合规检查进行调整，目前尚未承诺发布日期。

## 责任使用

PCA-SC-Bench 面向评测、鲁棒性和安全决策研究。基准分数不应被视为模型已可在现实公共环境中安全部署的证明。真实部署仍需独立验证、领域专家参与及合适的运行保障。

请勿通过本仓库索取未公开数据集、稿件草稿、评审材料、凭据或未发表结果。如发现安全或隐私问题，请按 [SECURITY.md](SECURITY.md) 中的方式私下报告。

## 参与贡献

基准资料尚未开放外部贡献。欢迎提交不涉及敏感信息的文档修正与建议；发起 Pull Request 前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 引用

与本项目相关的研究正式公开后，我们会补充引用信息。在此之前，请直接链接本仓库，不建议创建非官方引用。

## 许可证

本仓库当前已包含的内容使用 [MIT License](LICENSE)。未来公开的基准数据、图像、标注、模型输出及其他研究资料可能使用不同条款，届时将单独说明。

---

<div align="center">
  <sub>为审慎评测而构建，只在资料准备完善后发布。</sub>
</div>
