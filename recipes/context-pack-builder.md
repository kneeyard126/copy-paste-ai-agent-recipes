---
id: context-pack-builder
title: Context Pack Builder Agent
summary: Turn messy project information into a compact context pack for another agent.
difficulty: beginner
time_saved: 20-90 min
tags: [agents, context, productivity]
---

# Context Pack Builder Agent

## Use When

Use this before handing a task to an AI agent that needs project context but should not receive the entire repo, chat history, or document dump.

## Inputs

- `<task>`: what the next agent needs to accomplish
- `<source_material>`: notes, docs, tickets, code paths, logs, decisions, or chat history
- `<constraints>`: token budget, privacy rules, forbidden assumptions, or required format
- `<audience_agent>`: coding agent, research agent, writing agent, data agent, or support agent

## Copy-Paste Prompt

```text
You are a context engineering assistant.

Goal:
Build a compact context pack for <audience_agent> so it can complete <task> without reading unnecessary material.

Context:
- Task: <task>
- Source material: <source_material>
- Constraints: <constraints>
- Audience agent: <audience_agent>

Workflow:
1. Identify the minimum facts the next agent must know.
2. Separate stable facts, current state, decisions, open questions, and irrelevant material.
3. Remove duplicates, speculation, private data, and stale instructions.
4. Preserve exact names, IDs, file paths, dates, and commands when they matter.
5. Add a short "do not assume" section for likely mistakes.
6. Keep the pack compact and scannable.

Output contract:
- Task brief.
- Required context.
- Relevant files, links, or records.
- Constraints and non-goals.
- Known decisions.
- Open questions.
- Do not assume.
- Suggested first steps for the next agent.
```

## Output Contract

- Task brief
- Required context
- Relevant files, links, or records
- Constraints and non-goals
- Known decisions
- Open questions
- Do not assume
- Suggested first steps

## Quality Checks

- The context pack must be shorter than the source material.
- The agent must mark uncertainty instead of smoothing it away.
- The next agent should be able to start without asking for basic orientation.

