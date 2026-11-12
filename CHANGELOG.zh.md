# 变更日志

从 0.4.0 起，条目由 release-please 根据提交信息生成。本 fork 的 release-please 只在维护者手动调度时运行：合并它开出的发版 PR 即创建标签与 GitHub Release。

本页记录本项目所有值得关注的变更。
格式遵循 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)。

版本遵循[语义化版本规范](https://semver.org/spec/v2.0.0.html)。

!!! note "完整中文翻译与权威来源"
    本页逐条翻译英文 [CHANGELOG.md](CHANGELOG.md)，保留版本、日期、分类、Issue 和提交链接，不以摘要替代历史明细。英文日志是发布记录的权威来源；除维护者在打 tag 时新增版本节外，不得手工修改英文日志或版本字段。中文页仅翻译已记录的变更，不增加发布声明或真机验证结论。

    中文页按英文日志的顺序补译，不增加发布声明；`1.0.0` 一节只有英文版，`1.1.0` 起按节同步。

<a id="113-2026-11-12"></a>
## [1.1.3](https://github.com/vibe-bimer/smart-revit/compare/v1.1.2...v1.1.3)（2026-11-12）

<a id="113-documentation"></a>
### 文档

* **changelog：** 翻译 1.1.2 的发布说明（[1789267](https://github.com/vibe-bimer/smart-revit/commit/17892676f17153f528c0767584bdc713f5962ac9)）。
* **site：** 发布 1.1.2 并重生成提到它的页面（[5125f36](https://github.com/vibe-bimer/smart-revit/commit/5125f3632d5ef66f9de8c5a0e8a2d90919dfb4e2)）。

<a id="112-2026-11-11"></a>
## [1.1.2](https://github.com/vibe-bimer/smart-revit/compare/v1.1.1...v1.1.2)（2026-11-11）

<a id="112-bug-fixes"></a>
### 错误修复

* **site：** 每个页面都写已发布版本（[eea3907](https://github.com/vibe-bimer/smart-revit/commit/eea3907ffa0cd2accedb8f440372f3ea1c07d782)）。
* **tests：** TUnit 保持在 1.81.16（[10ec651](https://github.com/vibe-bimer/smart-revit/commit/10ec651b25db27174109f77daf3af93ddb19c62d)）。

<a id="112-documentation"></a>
### 文档

* **analysis：** 记录发版 PR 如何拿到检查（[2c6dd9b](https://github.com/vibe-bimer/smart-revit/commit/2c6dd9b308ef021bf3d98e3dab761a21d5e03bda)）。
* **changelog：** 翻译 1.1.1 的发布说明（[b2dda5c](https://github.com/vibe-bimer/smart-revit/commit/b2dda5c2fa43a395d7741867fc61f5b9df06997a)）。
* 为多上下文布局补上词表地图索引（[456361d](https://github.com/vibe-bimer/smart-revit/commit/456361d0bae2280ddcd96d1c0bdbf3ad8c102536)）。
* **site：** 发布 1.1.1 并重生成提到它的页面（[7385b54](https://github.com/vibe-bimer/smart-revit/commit/7385b54276ad492fecbd2fc6a13f4b6f51fa26c8)）。
* **site：** 把参数列表的条目读作条目，而不是模型构件（[210ea5a](https://github.com/vibe-bimer/smart-revit/commit/210ea5a07fc9c8eec62e0001038e8fe96d32818a)）。
* **site：** 为 1.1.1 开发线重生成页面（[824b280](https://github.com/vibe-bimer/smart-revit/commit/824b280d3a301c1414667f14ce92e1f0cac7b756)）。

<a id="112-dependencies"></a>
### 依赖

* **deps：** 把 python 从 3.12-slim 升到 3.15-slim（[#9](https://github.com/vibe-bimer/smart-revit/issues/9)）（[988f10b](https://github.com/vibe-bimer/smart-revit/commit/988f10babb12a9d7b72b92b7a70a60cf5bb21cd9)）。
* **deps：** 把一个目录下的 12 项更新一起抬升（[#1](https://github.com/vibe-bimer/smart-revit/issues/1)）（[8204efc](https://github.com/vibe-bimer/smart-revit/commit/8204efc3abc36aa955b90afac680137492022cfc)）。
* **deps：** 把两个目录下的 3 项更新一起抬升（[#12](https://github.com/vibe-bimer/smart-revit/issues/12)）（[37ecb45](https://github.com/vibe-bimer/smart-revit/commit/37ecb458105ea16343d08a794e1dac03cdbeeb23)）。
* **deps：** 抬升整组里的 1 项更新（[#10](https://github.com/vibe-bimer/smart-revit/issues/10)）（[8e2aa1f](https://github.com/vibe-bimer/smart-revit/commit/8e2aa1f9a04aeb8deda47c3dd86e724111f588e4)）。
* **deps：** 抬升整组里的 4 项更新（[#2](https://github.com/vibe-bimer/smart-revit/issues/2)）（[b7187c5](https://github.com/vibe-bimer/smart-revit/commit/b7187c56bfeda943068595dfbd365b9677b5aab9)）。

<a id="111-2026-11-11"></a>
## [1.1.1](https://github.com/vibe-bimer/smart-revit/compare/v1.1.0...v1.1.1)（2026-11-11）

<a id="111-bug-fixes"></a>
### 错误修复

* **ci：** 给发布构建补上预算测试需要的历史（[cb6cce0](https://github.com/vibe-bimer/smart-revit/commit/cb6cce04648be2fa0e9e40704ed164c49caafb82)）。

<a id="111-documentation"></a>
### 文档

* **release：** 描述本 fork 实际运行的发布流程（[a17e4ae](https://github.com/vibe-bimer/smart-revit/commit/a17e4aec51ff96ab18da14c23a2746c580513f0f)）。

<a id="110-2026-11-11"></a>
## [1.1.0](https://github.com/vibe-bimer/smart-revit/compare/v1.0.0...v1.1.0)（2026-11-11）

<a id="110-features"></a>
### 新功能

* **actions：** 新增 `revit_copy_elements`（[bc2078c](https://github.com/vibe-bimer/smart-revit/commit/bc2078cff5501fd4b78803dcce120c165f825117)）。
* **docs：** 把文档站发布到 GitLab Pages（[1f51282](https://github.com/vibe-bimer/smart-revit/commit/1f512820ab122e673c8cd16a64a6a80644ed2fe6)）。
* **docs：** 把文档站发布到 GitLab Pages（[ac83ac3](https://github.com/vibe-bimer/smart-revit/commit/ac83ac3253fd6e59a5d2ae4b047e14a0fc63c254)）。
* **fork：** 为 rebuild 工具加入预热副本与逐副本种子偏移（[799dec6](https://github.com/vibe-bimer/smart-revit/commit/799dec681a2af84a1f448130f55450522d14b461)）。
* **server：** 新增验收台账，记录验证证据（[1a9966e](https://github.com/vibe-bimer/smart-revit/commit/1a9966e7eb13449a0c95813edcaab50e83450764)）。

<a id="110-bug-fixes"></a>
### 错误修复

* **addin：** 修复 2020 轮验收暴露的 fork 命令（[cd44829](https://github.com/vibe-bimer/smart-revit/commit/cd44829625da43f3265b7eb21ae73908e005d65a)）。
* **ci：** 让 fork 预算以工作树为量度对象（[09fd98b](https://github.com/vibe-bimer/smart-revit/commit/09fd98bfabddf6e8990c61d04713b6113d8a3358)）。
* **docs：** 把已发布版本推进到 1.0.0（[50baa70](https://github.com/vibe-bimer/smart-revit/commit/50baa705e8da63327ab2bff1e544c76252fddbc9)）。
* **server：** 批量作业接受已发布的 Revit 年份（[baec4e1](https://github.com/vibe-bimer/smart-revit/commit/baec4e1282c7b1e1d8b818e5b3f9a5bacacb2be1)）。
* **site：** 按快照提交的评审意见修正站点（[ae1535c](https://github.com/vibe-bimer/smart-revit/commit/ae1535cca4ed744fab2d65989ff930055c56fafa)）。
* **site：** 参数表报告类型时跟随 `$ref`（[59480b1](https://github.com/vibe-bimer/smart-revit/commit/59480b1d74b60cf7c65125c1af6fe8aa6775aec4)）。
* **site：** 让说明文字与列测试保持一致（[dd89e3a](https://github.com/vibe-bimer/smart-revit/commit/dd89e3ac4c374bff885916dd0013ce3c61d21f9b)）。
* **site：** 避免工具转储在 Windows 上死锁（[889006c](https://github.com/vibe-bimer/smart-revit/commit/889006c7ca5cc9672656bbba5bb7d0446dbc313a)）。
* **site：** 生成页面使用 LF 行尾（[9eec6f9](https://github.com/vibe-bimer/smart-revit/commit/9eec6f92c211bcfd4ab84e415080fdffb0b86cc6)）。
* **tests：** 让格式门禁在还原后的工作树上通过（[9cb8668](https://github.com/vibe-bimer/smart-revit/commit/9cb8668907b430c7ed4033e34fcbf5e237e3121c)）。

<a id="110-documentation"></a>
### 文档

* **agents：** 记录本工作区采用多上下文布局（[530dba4](https://github.com/vibe-bimer/smart-revit/commit/530dba4ad789559c73d1b1d40348dd38a84223d7)）。
* **analysis：** 研究 agent-autoloop 与本 fork 的关系（[ae6a758](https://github.com/vibe-bimer/smart-revit/commit/ae6a758069b2c78a22e6713af9b9bb70cbd1cdb4)）。
* 修正落地页表述与钩子预算（[05524a5](https://github.com/vibe-bimer/smart-revit/commit/05524a54869870032e4d92761c92de0fb392c94f)）。
* 把仓库指向 vibe-bimer/smart-revit（[f819b6b](https://github.com/vibe-bimer/smart-revit/commit/f819b6bf7986a58c655fb5d5ba3e994b858ad8d4)）。
* **release：** 为下一版标注 Revit 2020 说明的日期（[686bce2](https://github.com/vibe-bimer/smart-revit/commit/686bce27f568b037e9eec53a5c1c8d374dd57c08)）。
* **release：** 说明版本节由谁撰写（[f61ae0d](https://github.com/vibe-bimer/smart-revit/commit/f61ae0ddec07ffce8241689cc33aa076cb5252cf)）。
* **site：** 统一未发布版本行的称呼（[d29960e](https://github.com/vibe-bimer/smart-revit/commit/d29960e80d1956d27ffa0a46bf776e5e77ab20dd)）。
* **site：** 让随包资产里的未发布版本行称呼一致（[40ade1f](https://github.com/vibe-bimer/smart-revit/commit/40ade1f1682e920572bdfba1b1b7e8f61c4358d6)）。
* **validation：** 记录 Revit 2020 验收轮（[3bce8a8](https://github.com/vibe-bimer/smart-revit/commit/3bce8a86dfc67ee4e0a8594a26d1c90051bdb02b)）。

<a id="110-dependencies"></a>
### 依赖

* **deps：** 把 Ruff 0.17.4 钉到 CI、钩子与文档（[9270775](https://github.com/vibe-bimer/smart-revit/commit/9270775022d05c9a50419e08584b4aed43856304)）。

<a id="090-2026-09-30"></a>
## [0.9.0](https://github.com/vibe-bimer/revit-model-mcp/compare/v0.8.1...v0.9.0)（2026-09-30）

<a id="features"></a>
### 新功能

* **rebuild：** 从一个模型写出多份副本（[ca6b77b](https://github.com/vibe-bimer/revit-model-mcp/commit/ca6b77bde214f6282113e3368c3f88f1f5110f91)）。

<a id="bug-fixes"></a>
### 错误修复

* **farm：** 为每个实例提供独立的模型副本（[2357a7d](https://github.com/vibe-bimer/revit-model-mcp/commit/2357a7ddced77c1325230076bcc87e8417bbfcbd)）。
* **rebuild：** 在同一模型的各份副本之间清理已粘贴类型（[b9867de](https://github.com/vibe-bimer/revit-model-mcp/commit/b9867de130ff6b7f142bb9d171c52432cf19f621)）。
* **rebuild：** 确保每一批副本都完整生成（[20354ec](https://github.com/vibe-bimer/revit-model-mcp/commit/20354ecc6d009a96d8d4edfdfcefdca3555d885b)）。
* **rebuild：** 仅在映射确实失败时重复复制（[437b78b](https://github.com/vibe-bimer/revit-model-mcp/commit/437b78b027725e4139a52131e22ce793a60c7fbf)）。

<a id="performance"></a>
### 性能

* **rebuild：** 回答 Revit 的重名询问，而不是重命名模板（[5aaea7c](https://github.com/vibe-bimer/revit-model-mcp/commit/5aaea7c8b64bed81846b3b5d937b9960e2efa235)）。
* **rebuild：** 在逐元素处理前，先重试被拒绝的复制（[2bc8cc8](https://github.com/vibe-bimer/revit-model-mcp/commit/2bc8cc88ae762b523bf0796103e37aa6569984ee)）。
* **rebuild：** 复用已粘贴类型，并保留一份备份（[a15fdb8](https://github.com/vibe-bimer/revit-model-mcp/commit/a15fdb821e38c40a48140f806304d5b4de72bdf7)）。

<a id="081-2026-09-29"></a>
## [0.8.1](https://github.com/vibe-bimer/revit-model-mcp/compare/v0.8.0...v0.8.1)（2026-09-29）

<a id="bug-fixes_1"></a>
### 错误修复

* **actions：** 防止重建操作等待重名询问对话框（[13194e4](https://github.com/vibe-bimer/revit-model-mcp/commit/13194e4cd91938135311e36f3182fc40a188d3fc)）。

<a id="documentation"></a>
### 文档

* 记录导出、重置和重建工具的 Revit 2020 验证证据（[f1ea0f9](https://github.com/vibe-bimer/revit-model-mcp/commit/f1ea0f92ae04b5fbf647184566a8e8563aff7086)）。

<a id="080-2026-09-28"></a>
## [0.8.0](https://github.com/vibe-bimer/revit-model-mcp/compare/v0.7.0...v0.8.0)（2026-09-28）

<a id="features_1"></a>
### 新功能

* **actions：** 新增可试运行的元素 ID 重置功能（[0c8d92a](https://github.com/vibe-bimer/revit-model-mcp/commit/0c8d92aaf8a8147b061a1768fab5795997e9921d)）。
* **actions：** 重建模型，让 Revit 为每个元素分配新的 ID（[b1c0b5d](https://github.com/vibe-bimer/revit-model-mcp/commit/b1c0b5d408e1746c4e9a00777147a4c58dece0f3)）。
* **actions：** 为副本重新关联宿主、恢复连接，并报告重置成本（[a405693](https://github.com/vibe-bimer/revit-model-mcp/commit/a405693fe07a29af90964714c2d7b8ed87876566)）。
* **read：** 将元素标识符清单导出到工作簿（[6fb4560](https://github.com/vibe-bimer/revit-model-mcp/commit/6fb456010c128b23fc83aedc2921303a7e783466)）。

<a id="bug-fixes_2"></a>
### 错误修复

* **actions：** 将系统成员集合按元素读取，并检查连接器（[dc9d34c](https://github.com/vibe-bimer/revit-model-mcp/commit/dc9d34c405eedef34e573e3414d9dcc45d4558d6)）。
* **actions：** 拒绝所有 MEP 系统成员，而不仅是 MEP 曲线（[c81fa91](https://github.com/vibe-bimer/revit-model-mcp/commit/c81fa91dac1f50eb2ee38eba1546b0270b6bf782)）。
* **actions：** 在各自的子事务中替换每个元素（[c0ac48a](https://github.com/vibe-bimer/revit-model-mcp/commit/c0ac48a207e3d86b4ec8a3c0b8678a6ab1ea4545)）。
* **bundle：** 在 bundle 清单中列出新的导出工具（[aa7f8ce](https://github.com/vibe-bimer/revit-model-mcp/commit/aa7f8ce5b6698eb33a90938e844707885eb251f0)）。
* **read：** 将草图线和辅助线排除在构件清单之外（[a141ea1](https://github.com/vibe-bimer/revit-model-mcp/commit/a141ea1fc2cd9f4430da5ec07e3ec30fd099030b)）。

<a id="070-2026-09-28"></a>
## [0.7.0](https://github.com/vibe-bimer/revit-model-mcp/compare/v0.6.0...v0.7.0)（2026-09-28）

<a id="features_2"></a>
### 新功能

* **channel：** 报告插件构建版本（[155a7e9](https://github.com/vibe-bimer/revit-model-mcp/commit/155a7e9ef514afd10cb9d2b6481091565cd13e84)）。

<a id="bug-fixes_3"></a>
### 错误修复

* **server：** 显示插件构建信息，并停止阻塞心跳写入（[5c9f4c1](https://github.com/vibe-bimer/revit-model-mcp/commit/5c9f4c13fee05fa77ccc678eb06f96f863e37aea)）。

<a id="060-2026-09-28"></a>
## [0.6.0](https://github.com/vibe-bimer/revit-model-mcp/compare/v0.5.0...v0.6.0)（2026-09-28）

<a id="features_3"></a>
### 新功能

* **actions：** 新增 `revit_create_floor` 动作工具（[a63c580](https://github.com/vibe-bimer/revit-model-mcp/commit/a63c580cab5829ca424c48276cc192ca3f10b0e8)）。
* **actions：** 新增 `set_phase` 和 `merge_phases` 工具（[afd83c0](https://github.com/vibe-bimer/revit-model-mcp/commit/afd83c0526072f6314a1b18a9efd6a636286d915)）。
* **addin：** 新增 Revit 2020 支持（[14ed865](https://github.com/vibe-bimer/revit-model-mcp/commit/14ed8657aec52e589cdc60c9ef137f408101738e)）。
* **channel：** 根据任务 ID 关联响应，并以原子方式发布（[#61](https://github.com/vibe-bimer/revit-model-mcp/issues/61)，[5a65afc](https://github.com/vibe-bimer/revit-model-mcp/commit/5a65afc47789f07c2df495e2779e69dafd2e58b0)）。
* **read：** 在文档信息中公开文档的 `isModified`（[04550e4](https://github.com/vibe-bimer/revit-model-mcp/commit/04550e43edc1a6e8ebd496da22de4d67633683a9)）。

<a id="bug-fixes_4"></a>
### 错误修复

* **addin：** 将写入动作指向寻址的文档，而不是当前活动文档（[#60](https://github.com/vibe-bimer/revit-model-mcp/issues/60)，[d558ee9](https://github.com/vibe-bimer/revit-model-mcp/commit/d558ee955e29f60a194d7280df88791c2fc9c1d9)）。
* **ci：** 断言已安装年份数与 CI 实际构建数量一致（[ca65487](https://github.com/vibe-bimer/revit-model-mcp/commit/ca6548752f73dc725aefff7a996cabfd18dfce04)）。
* 解决人工测试中的读取及 HTTP 安装失败（[#45](https://github.com/vibe-bimer/revit-model-mcp/issues/45)，[61bd2ba](https://github.com/vibe-bimer/revit-model-mcp/commit/61bd2ba13c1c668b0a3d5e53f06ee6a8011f4292)）。

<a id="documentation_1"></a>
### 文档

* 添加 Revit API 语料库工作流程和项目分析（[e0b821a](https://github.com/vibe-bimer/revit-model-mcp/commit/e0b821a535d301be30430c57ad6aeaf1caf77dd0)）。
* 修正 Linux 构建标志，并记录部署经验（[e0848f8](https://github.com/vibe-bimer/revit-model-mcp/commit/e0848f88e7344c8fd669d0c171650d50a8feb4b9)）。
* 记录 Linux 下 `dotnet format` 的替代方案（[679b4fc](https://github.com/vibe-bimer/revit-model-mcp/commit/679b4fcff154b3b6af02bf63f7e55a80c9b1f0c6)）。
* 记录 Revit 2020 支持（[5ac9a55](https://github.com/vibe-bimer/revit-model-mcp/commit/5ac9a55ce5804cda986ddb31f6c4986ca40121ac)）。
* 枚举动作工具，并链接工具新增指南（[f437d63](https://github.com/vibe-bimer/revit-model-mcp/commit/f437d639963c4fb8cd2b25519ad794a8ac11136d)）。
* 记录插件签名和自动重启流程（[e4139f3](https://github.com/vibe-bimer/revit-model-mcp/commit/e4139f30a51248b9d524bd220f8b9395dd71a754)）。
* 记录已经确定的 Revit 阶段 API 限制（[b820aaf](https://github.com/vibe-bimer/revit-model-mcp/commit/b820aaf2366413732668e25eb052a8540f514b8d)）。
* 要求远程重启 Revit 前检查 `isModified`（[70b6582](https://github.com/vibe-bimer/revit-model-mcp/commit/70b6582002e5f3df5e8eeb22e798671df47dbc7a)）。

<a id="050-2026-09-14"></a>
## [0.5.0](https://github.com/sharafutdinovdi/revit-model-mcp/compare/v0.4.0...v0.5.0)（2026-09-14）

<a id="features_4"></a>
### 新功能

* 为目录审核准备桌面 bundle（[#40](https://github.com/sharafutdinovdi/revit-model-mcp/issues/40)，[fcd5db9](https://github.com/sharafutdinovdi/revit-model-mcp/commit/fcd5db91a52c904193d86f1ba804e25161ec6a32)）。

<a id="bug-fixes_5"></a>
### 错误修复

* 使用每个年份可用的最低 Revit API 构建版本作为目标（[#42](https://github.com/sharafutdinovdi/revit-model-mcp/issues/42)，[e17d8a7](https://github.com/sharafutdinovdi/revit-model-mcp/commit/e17d8a75be7ea9db058a5478537c2c3449ebfa67)）。

<a id="040-2026-09-14"></a>
## [0.4.0](https://github.com/sharafutdinovdi/revit-model-mcp/compare/v0.3.0...v0.4.0)（2026-09-14）

<a id="features_5"></a>
### 新功能

* 添加 Claude Desktop bundle、发布来源证明和 Scorecard（[#34](https://github.com/sharafutdinovdi/revit-model-mcp/issues/34)，[15f1ff4](https://github.com/sharafutdinovdi/revit-model-mcp/commit/15f1ff4710b971d2f29f5b8558050207c2f9f05b)）。

<a id="documentation_2"></a>
### 文档

* 添加品牌标志、分组文档导航，并移除过时安装说明（[#21](https://github.com/sharafutdinovdi/revit-model-mcp/issues/21)，[5f5e67b](https://github.com/sharafutdinovdi/revit-model-mcp/commit/5f5e67b69638b8279e44ad1161e2a9aa38453816)）。
* **brand：** 将标志改为叠放的楼板（[#22](https://github.com/sharafutdinovdi/revit-model-mcp/issues/22)，[5003907](https://github.com/sharafutdinovdi/revit-model-mcp/commit/5003907a165cb3cf7d72b77e590f899d099323ad)）。

<a id="030-2026-09-13"></a>
## [0.3.0] - 2026-09-13

<a id="added"></a>
### 新增

- 使用 MkDocs Material 的 GitHub Pages 文档，包括服务器参考、搜索，以及 llms.txt 和 llms-full.txt 导出。
- Contributor Covenant 2.1，以及面向编码 Agent 的仓库说明。
- 从带标签的变更日志小节提取发布亮点，并提供直接安装链接。
- 单用户和多用户 MSI 发布资产，以及 CI 中的解包、安装和卸载冒烟测试。
- 按年份 ZIP、MSI、Python wheel 和源码发行包的 SHA256 校验和。
- 稳定发布通过 GitHub OIDC 进行 PyPI 可信发布，以及尽力而为的 MCP Registry 发布。
- MCP Registry 清单，以及适用于 Claude Code 和 Claude Desktop 的 uvx 配置。
- WinGet 清单模板、生成、校验，以及通过 `WINGET_TOKEN` 可选提交。

<a id="changed"></a>
### 变更

- README 展示安装与分组工具；详细动作、安全和验证参考放在 `docs/` 中。
- 贡献指南加入测试覆盖和发布流程。

<a id="fixed"></a>
### 修复

- Python 发行包包含 MIT 许可证文件，并声明已经测试的 Python 3.13 支持。

<a id="020-2026-09-12"></a>
## [0.2.0] - 2026-09-12

<a id="added_1"></a>
### 新增

- Revit 2027 构建配置及 CI／发布打包。
- `install.ps1`，支持构建／发布来源、可选程序集签名和 Claude Code 注册。
- 默认只读协调工具：`revit_model_health`、`revit_links_status`、`revit_shared_coordinates` 和 `revit_parameter_fill_check`。
- `revit_move`、`revit_place_family`、`revit_create_wall`、`revit_set_parameter` 和 `revit_delete` 的 `dry_run`：成功的预览在事务内执行，随后回滚，并返回同样的校验块。
- `verification`：变更前采集 `before`，提交后重新读取 `after`（试运行则在回滚前读取）。
- 提交后重新读取失败时返回 `verification.error`。
- `revit_batch`：在单个 `TransactionGroup` 中最多执行 50 个动作，合并为一次撤销，在第一个步骤失败时回滚。

<a id="changed_1"></a>
### 变更

- README 快速入门使用安装脚本。
- MCP 握手版本来自包元数据。
- `install.ps1` 在缺少某个 Revit 年份的发布资产时给出清楚提示。

<a id="010-2026-09-11"></a>
## [0.1.0] - 2026-09-11

<a id="added_2"></a>
### 新增

- Windows Revit 插件，包含 Revit 2022–2026 构建配置。
- Python MCP 服务器，提供 14 个默认读取工具，覆盖目录、查询、聚合、参数、警告、关系、视图和实例发现。
- PNG 视图导出，以及以模型毫米为单位的可选元素几何信息。
- 八个主动启用的动作工具，由服务器标志和工作站门禁文件保护。
- 面向远程工作站的本地 PowerShell、SSH 文件通道及带认证 HTTP 传输。
- 每用户 HTTP 令牌、回环监听器、路径脱敏和可配置通道目录。
- Core 测试、服务器测试，以及 Revit 2022 和 2026 的 CI 产物。
- 标签触发的五个 Revit 版本发布打包，以及一个 Python wheel。
- 安装、传输、协议、安全及贡献文档。
