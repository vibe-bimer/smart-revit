# 领域文档

本页说明工程技能在探索代码库时，应如何使用本仓库的领域文档。

<a id="layout"></a>
## 布局：multi-context

本仓库采用多上下文布局（multi-context）：子项目各一份 `GLOSSARY.md`，根目录使用 `GLOSSARY-MAP.md`。架构决策记录放在仓库根目录的 `adr/`。

<a id="before-exploring-read-these"></a>
## 探索前先阅读这些资料

- 若根目录存在 **`GLOSSARY-MAP.md`**，先读它——它指向各子项目的 `GLOSSARY.md`。阅读与当前主题相关的每一份。
- 若根目录存在 **`GLOSSARY.md`**，阅读其中适用的领域术语。
- **`adr/`**——阅读涉及即将工作区域的 ADR。本仓库把决策记录放在仓库根目录的 `adr/`，不放在 `docs/adr/`：`docs/` 下的每个页面都是要发布的中英双语站点页，而 ADR 是工程记录，只写英文、不进导航。下文示意图中的 `docs/adr/` 请按 `adr/` 理解。
- **`docs/adr/`**——上游与本仓库都未使用该位置；若将来出现，按上下文专属决策处理。在多上下文仓库中，也要检查 `src/<context>/docs/adr/` 中限定于该上下文的决策。

如果其中某些文件不存在，**直接继续，不必提示**。不要专门报告缺失，也不要一开始就建议创建。`/domain-modeling` 技能（通过 `/grill-with-docs` 和 `/improve-codebase-architecture` 进入）会在术语或决策真正确定时按需创建这些文档。

<a id="file-structure"></a>
## 文件结构

单上下文仓库示例：

```text
/
├── GLOSSARY.md
├── adr/
│   ├── 0001-base-on-upstream-with-a-bounded-fork-layer.md
│   └── 0003-ship-read-only-by-default-through-the-policy.md
└── src/
```

多上下文仓库（根目录存在 `GLOSSARY-MAP.md` 时）：

```text
/
├── GLOSSARY-MAP.md
├── docs/adr/                          ← 系统级决策
└── src/
    ├── ordering/
    │   ├── GLOSSARY.md
    │   └── docs/adr/                  ← 上下文专属决策
    └── billing/
        ├── GLOSSARY.md
        └── docs/adr/
```

<a id="use-the-glossarys-vocabulary"></a>
## 使用词表中的术语

当输出中需要命名领域概念时（例如 Issue 标题、重构提案、假设或测试名称），使用 `GLOSSARY.md` 定义的术语。不要改用词表明确避免的同义词。

如果需要的概念尚未出现在词表中，这本身就是一个信号：要么正在创造项目并不使用的语言（需要重新考虑），要么确实存在词表缺口（记录下来，交给 `/domain-modeling`）。

<a id="flag-adr-conflicts"></a>
## 明确指出 ADR 冲突

如果输出与已有 ADR 冲突，应明确指出，而不是默默覆盖原决策：

> _与 ADR-0007（事件溯源订单）冲突——但值得重新讨论，因为……_
