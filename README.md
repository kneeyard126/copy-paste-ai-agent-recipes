# Copy-Paste AI Agent Recipes

Practical, copy-ready workflows for using AI agents on real work.

[中文说明](README.zh-CN.md)

Works with ChatGPT, Claude, Gemini, Codex, Cursor, Windsurf, and other assistants that can follow structured instructions.

[![License](https://img.shields.io/github/license/kneeyard126/copy-paste-ai-agent-recipes?style=flat-square)](LICENSE)
[![Validate](https://img.shields.io/github/actions/workflow/status/kneeyard126/copy-paste-ai-agent-recipes/validate.yml?branch=main&style=flat-square)](https://github.com/kneeyard126/copy-paste-ai-agent-recipes/actions)

Most agent examples are either too vague or too tied to one tool. This repo is a cookbook of small, reusable agent recipes you can paste into ChatGPT, Claude, Gemini, Codex, Cursor, Windsurf, or any other assistant that can follow instructions.

Each recipe gives you:

- A short use case and required inputs
- A copy-paste prompt
- A clear output contract
- Quality checks so the agent does not stop at a pretty answer

## Quick Start

1. Pick a recipe from the table below.
2. Replace the placeholders like `<repo>`, `<goal>`, or `<ticket>`.
3. Paste the prompt into your AI agent.
4. Ask the agent to follow the output contract exactly.

## Featured Recipes

| Recipe | Best for | Output |
| --- | --- | --- |
| [Code Review Agent](recipes/code-review.md) | Reviewing pull requests before merge | Findings, risks, missing tests |
| [Test Writer Agent](recipes/test-writer.md) | Adding focused tests to existing code | Test plan and implemented tests |
| [Bug Hunt Agent](recipes/bug-hunt.md) | Reproducing and fixing tricky bugs | Repro steps, root cause, patch |
| [Dependency Upgrade Agent](recipes/dependency-upgrade.md) | Updating packages without breaking behavior | Upgrade plan, diffs, verification |
| [Docs Refresh Agent](recipes/docs-refresh.md) | Turning stale docs into useful docs | Updated docs and examples |
| [Release Notes Agent](recipes/release-notes.md) | Summarizing commits for users | Human-readable release notes |
| [SQL Analyst Agent](recipes/sql-analyst.md) | Getting trustworthy data answers | Query plan, SQL, caveats |
| [Support Triage Agent](recipes/support-triage.md) | Sorting customer reports fast | Priority, owner, next action |
| [Meeting to Actions Agent](recipes/meeting-to-actions.md) | Converting notes into follow-up work | Decisions, owners, tasks |
| [PRD to Tickets Agent](recipes/prd-to-tickets.md) | Splitting product ideas into buildable work | User stories and acceptance criteria |
| [Incident Postmortem Agent](recipes/incident-postmortem.md) | Writing calm, blameless postmortems | Timeline, causes, actions |
| [Marketing Page Critic Agent](recipes/marketing-page-critic.md) | Improving a landing page before launch | Diagnosis and rewrite brief |

## Why This Exists

AI agents work best when they receive more than a role prompt. They need the right context, a workflow to follow, an output contract, and checks that catch weak answers.

This repo turns common work into repeatable recipes so teams can reuse good instructions instead of rewriting prompts from scratch.

## Recipe Format

Every recipe follows the same shape:

- `Use when`: the exact situation where this recipe is worth using
- `Inputs`: what the agent needs before it starts
- `Copy-paste prompt`: the reusable instruction block
- `Output contract`: the shape the answer must follow
- `Quality checks`: tests the agent should run before it finishes

That consistency is the product. The repo is small on purpose.

## Suggested Agent Settings

Use a stronger reasoning model when the task has production risk, such as code review, security, migrations, finance, or legal/compliance work. For simple writing and triage, a faster model is usually enough.

When your agent can access tools, give it read access first. Let it inspect the repo, docs, data, or tickets before asking it to change anything.

## Contributing

New recipes are welcome. Start with [recipes/_template.md](recipes/_template.md), then read [CONTRIBUTING.md](CONTRIBUTING.md).

Good recipes are narrow, practical, and reusable. They should help a busy person do one real workflow better in the next 10 minutes.

## License

MIT. Use these recipes in personal, internal, or commercial work.
