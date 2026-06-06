---
id: agent-skill-author
title: Agent Skill Author Agent
summary: Convert a repeatable workflow into a reusable AI agent skill or instruction file.
difficulty: intermediate
time_saved: 30-120 min
tags: [agents, skills, documentation]
---

# Agent Skill Author Agent

## Use When

Use this when a prompt, checklist, or team practice is useful enough to become a reusable agent skill, rules file, or instruction document.

## Inputs

- `<workflow>`: the workflow the skill should teach
- `<trigger>`: when the agent should use the skill
- `<tools>`: tools, files, APIs, commands, or MCP servers the skill may rely on
- `<quality_bar>`: checks that define a good result
- `<target_agent>`: Claude Code, Codex, Cursor, Windsurf, Gemini CLI, OpenCode, or generic agent

## Copy-Paste Prompt

```text
You are an AI agent skill designer.

Goal:
Turn <workflow> into a reusable skill or instruction file for <target_agent>.

Context:
- Workflow: <workflow>
- Trigger: <trigger>
- Tools and resources: <tools>
- Quality bar: <quality_bar>
- Target agent: <target_agent>

Workflow:
1. Define when the skill should activate and when it should stay silent.
2. Write concise instructions that teach the workflow, not a one-off task.
3. Include required inputs, steps, output format, and verification checks.
4. Add guardrails for unsafe tools, secrets, private data, and destructive actions.
5. Keep the skill portable. Avoid vendor-specific syntax unless needed.
6. Provide a short example invocation.

Output contract:
- Skill name.
- Purpose.
- Use when.
- Do not use when.
- Required inputs.
- Instructions.
- Output format.
- Safety and verification checks.
- Example invocation.
```

## Output Contract

- Skill name
- Purpose
- Use when
- Do not use when
- Required inputs
- Instructions
- Output format
- Safety and verification checks
- Example invocation

## Quality Checks

- The skill must describe a repeatable capability, not a single task.
- Trigger rules must be specific enough to prevent overuse.
- Safety checks must mention secrets, permissions, and destructive actions when relevant.

