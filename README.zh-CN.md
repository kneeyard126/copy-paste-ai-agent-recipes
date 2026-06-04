# Copy-Paste AI Agent Recipes

一套可以直接复制使用的 AI Agent 工作流模板。

这个仓库不是做一个复杂工具，而是学习 GitHub 上很多高星轻量项目的做法：把一个需求明确、经常被搜索、马上能用的东西整理成稳定格式。

## 这个仓库解决什么问题

很多 AI Agent 示例太泛，真正工作时还要自己想角色、输入、步骤、输出格式和检查标准。这个仓库把这些内容整理成可复用的 recipe。

每个 recipe 都包含：

- 适用场景
- 需要提供的输入
- 可直接复制的 Prompt
- 固定输出格式
- 质量检查点

## 首批内容

| Recipe | 用途 |
| --- | --- |
| [Code Review Agent](recipes/code-review.md) | 审查 PR，找 bug、风险和缺失测试 |
| [Test Writer Agent](recipes/test-writer.md) | 按现有代码风格补测试 |
| [Bug Hunt Agent](recipes/bug-hunt.md) | 复现、定位、修复 bug |
| [Dependency Upgrade Agent](recipes/dependency-upgrade.md) | 安全升级依赖 |
| [Docs Refresh Agent](recipes/docs-refresh.md) | 更新过期文档 |
| [Release Notes Agent](recipes/release-notes.md) | 把 commits/PR 整理成发布说明 |
| [SQL Analyst Agent](recipes/sql-analyst.md) | 写更可靠的数据分析 SQL |
| [Support Triage Agent](recipes/support-triage.md) | 客服消息分级、路由、回复草稿 |
| [Meeting to Actions Agent](recipes/meeting-to-actions.md) | 会议纪要转行动项 |
| [PRD to Tickets Agent](recipes/prd-to-tickets.md) | PRD 拆成工程 tickets |
| [Incident Postmortem Agent](recipes/incident-postmortem.md) | 写无责事故复盘 |
| [Marketing Page Critic Agent](recipes/marketing-page-critic.md) | 检查落地页文案和转化问题 |

## 为什么这种项目可能拿星

高星轻量项目通常不是赢在技术复杂度，而是赢在：

- 名字就是承诺
- 打开 README 立刻有用
- 内容结构稳定，方便收藏
- 贡献门槛低
- 选题踩中长期需求或热点趋势

这个仓库选择 AI Agent recipes，是因为它同时满足“搜索热度高”“内容容易持续扩展”“用户能马上复制使用”这三个条件。

## 怎么用

1. 打开任意 recipe。
2. 替换 `<repo>`、`<goal>`、`<customer_message>` 这类占位符。
3. 粘贴到 ChatGPT、Claude、Gemini、Codex、Cursor、Windsurf 等 AI 工具。
4. 要求模型严格按照 Output Contract 输出。

## 贡献

如果要添加新 recipe，请参考 [recipes/_template.md](recipes/_template.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)。

