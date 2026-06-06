# Copy-Paste AI Agent Recipes

一套可以直接复制使用的 AI Agent 工作流模板。

适用于 ChatGPT、Claude、Gemini、Codex、Cursor、Windsurf 等可以遵循结构化指令的 AI 工具。

这个仓库把常见工作场景整理成可复用的 AI Agent recipe：每个 recipe 都包含输入、执行步骤、输出格式和质量检查。

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
| [Context Pack Builder Agent](recipes/context-pack-builder.md) | 把杂乱资料整理成给下一个 Agent 用的上下文包 |
| [Agent Skill Author Agent](recipes/agent-skill-author.md) | 把重复工作流沉淀成可复用的 Agent Skill |
| [MCP Server Review Agent](recipes/mcp-server-review.md) | 接入 MCP Server 前做权限和风险审查 |
| [Agent Evals Agent](recipes/agent-evals.md) | 给 Agent 工作流设计评测用例和评分标准 |
| [Browser QA Agent](recipes/browser-qa.md) | 用浏览器 Agent 测试真实网页流程 |
| [AI Agent Security Review Agent](recipes/ai-agent-security-review.md) | 审查 Agent 的工具、数据、权限和安全风险 |

## 为什么需要它

很多 AI 提示词只告诉模型“你是某某专家”，但真正工作时还需要更完整的结构：要给什么输入、按什么步骤做、输出成什么格式、如何检查答案质量。

这个仓库的目标是把这些结构沉淀下来，让个人和团队可以直接复用。

## 怎么用

1. 打开任意 recipe。
2. 替换 `<repo>`、`<goal>`、`<customer_message>` 这类占位符。
3. 粘贴到 ChatGPT、Claude、Gemini、Codex、Cursor、Windsurf 等 AI 工具。
4. 要求模型严格按照 Output Contract 输出。

## 贡献

如果要添加新 recipe，请参考 [recipes/_template.md](recipes/_template.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)。
