# 中文传播计划

目标：让中文用户搜索“AI Agent 提示词”“AI Agent 工作流”“Agent 提示词模板”“Cursor 提示词”“Claude Code 工作流”等关键词时，更容易找到这个仓库。

## 核心定位

一句话：

> 一个可以直接复制使用的 AI Agent 工作流模板库，覆盖代码审查、写测试、排 bug、写文档、SQL 分析、客服分流、PRD 拆票、事故复盘等真实工作场景。

不要把它讲成“又一个 prompt 大全”。更好的表达是：

- 不是泛泛的角色扮演 prompt，而是带输入、步骤、输出格式、质量检查的工作流 recipe。
- 不绑定单一工具，可用于 ChatGPT、Claude、Gemini、Codex、Cursor、Windsurf。
- README 打开即用，适合收藏、转发、团队内部复用。

## 关键词矩阵

### 主关键词

- AI Agent 提示词
- AI Agent 工作流
- AI 智能体工作流
- Agent 提示词模板
- AI 工作流模板
- Prompt 模板
- 提示词工程

### 工具关键词

- ChatGPT 提示词
- Claude Code 工作流
- Cursor 提示词
- Codex 工作流
- Windsurf 工作流
- Gemini 提示词

### 场景关键词

- Code Review Prompt
- AI 代码审查提示词
- AI 写测试 Prompt
- AI 排 bug 工作流
- PRD 拆解 Prompt
- 会议纪要转行动项
- SQL 分析 Prompt
- 客服工单分流 Prompt
- 事故复盘模板

## GitHub SEO 动作

- 在仓库 description 放中英文关键词。
- README 前 100 行出现中文入口和关键词。
- 中文 README 标题附近放关键词矩阵。
- 每个 recipe 后续可以增加中文别名，例如“代码审查 Agent”“写测试 Agent”。
- issue、PR、commit、release notes 里自然使用关键词。
- 每次新增 recipe 发一个 GitHub Release，让订阅者和搜索引擎看到更新节奏。

## 首发传播渠道

### 第一优先级

- V2EX：适合“我做了一个小工具/开源项目”的真实分享，不要营销腔。
- 掘金：写一篇方法论文章，标题包含“AI Agent 工作流”和“提示词模板”。
- 知乎：回答“有哪些好用的 AI Agent 工作流/Prompt 模板？”并附项目链接。
- GitHub Discussions / README：持续更新 roadmap 和新增 recipe。
- X / Twitter：用英文发给 AI agent、developer tools、prompt engineering 圈子。
- Reddit：发到 r/AI_Agents、r/ChatGPTPromptGenius、r/PromptEngineering。

### 第二优先级

- 少数派：偏效率工具角度，写“我把常用 AI 工作流整理成了可复制模板”。
- 开源中国：中文开源项目曝光。
- CSDN / 博客园：SEO 长尾，标题要直接。
- 即刻：适合 AI、效率、独立开发圈层。
- 小红书：做“12 个打工人可复制 AI Agent 工作流”图文。
- 公众号：写“如何让 AI Agent 不只会聊天，而是按工作流交付”。

## 可直接复制的中文首发帖

### V2EX / 即刻

标题：

```text
做了一个可复制的 AI Agent 工作流模板库，想听听大家还需要哪些场景
```

正文：

```text
最近发现很多 AI Agent 示例都太泛：告诉模型“你是某某专家”，但没有输入格式、执行步骤、输出格式和质量检查。

我整理了一个开源仓库：Copy-Paste AI Agent Recipes。

目前首批 12 个场景：
- Code Review
- 写测试
- 排 bug
- 依赖升级
- 文档更新
- 发布说明
- SQL 分析
- 客服分流
- 会议纪要转行动项
- PRD 拆票
- 事故复盘
- 落地页文案诊断

每个 recipe 都是可直接复制的 Prompt，并且包含 Inputs、Workflow、Output Contract、Quality Checks。

仓库地址：
https://github.com/kneeyard126/copy-paste-ai-agent-recipes

想听听大家工作里最想补哪类 AI Agent 工作流，我可以继续加。
```

### 掘金 / 博客园 / CSDN

标题备选：

```text
我整理了 12 个可复制的 AI Agent 工作流提示词：代码审查、写测试、排 bug、SQL 分析
```

```text
别只让 AI 扮演专家：给它输入、流程、输出契约和质量检查
```

文章结构：

```text
1. 问题：普通 Prompt 为什么很难稳定产出
2. 方法：把 Prompt 写成 recipe
3. 一个完整例子：Code Review Agent
4. 12 个首发场景
5. 如何贡献新的工作流
6. GitHub 链接
```

### X / Twitter

```text
I made a small open-source cookbook of copy-paste AI agent recipes.

Not generic prompts. Each recipe includes:
- inputs
- workflow
- output contract
- quality checks

First 12 recipes cover code review, tests, debugging, docs, SQL, support, PRDs, incidents, and marketing copy.

https://github.com/kneeyard126/copy-paste-ai-agent-recipes
```

### Reddit

```text
I built a small open-source cookbook of copy-paste AI agent recipes.

The idea: most prompts are too vague, so each recipe includes required inputs, a workflow, an output contract, and quality checks.

Current recipes include code review, test writing, bug hunting, dependency upgrades, docs refresh, release notes, SQL analysis, support triage, PRD-to-tickets, incident postmortems, and landing page critique.

Repo:
https://github.com/kneeyard126/copy-paste-ai-agent-recipes

Would love suggestions for workflows that are painful enough to deserve a recipe.
```

## 发布节奏

第一周目标不是疯狂发帖，而是制造“这个项目在变好”的信号。

- Day 1：V2EX + X + GitHub topics/description/README SEO。
- Day 2：掘金长文，重点讲 Code Review Agent。
- Day 3：知乎回答 2-3 个相关问题。
- Day 4：新增 5 个中文场景 recipe，然后发 release。
- Day 5：Reddit + Hacker News Show HN。
- Day 6：小红书/即刻发图文版。
- Day 7：整理反馈，把用户提到的场景变成 issues。

## 后续增长动作

- 每周新增 5-10 个 recipe。
- 给每个 recipe 加中文标题和中文摘要。
- 做一个 `recipes.zh-CN/` 中文目录，吃中文搜索长尾。
- 维护 `good first recipe` issues，吸引贡献者。
- 给高频工具做专题页：Cursor、Claude Code、Codex、Windsurf。
- 做一个 GitHub Pages 小站，让搜索引擎更容易收录。

