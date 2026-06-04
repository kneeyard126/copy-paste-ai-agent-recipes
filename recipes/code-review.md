---
id: code-review
title: Code Review Agent
summary: Review a pull request for bugs, regressions, missing tests, and risky assumptions.
difficulty: beginner
time_saved: 30-90 min
tags: [engineering, review, quality]
---

# Code Review Agent

## Use When

Use this when you want an AI agent to review a pull request before a human reviewer spends time on it.

## Inputs

- `<repo>`: repository or relevant files
- `<diff>`: pull request diff or changed files
- `<intent>`: what the change is supposed to do
- `<test_commands>`: commands that should verify the change

## Copy-Paste Prompt

```text
You are a senior engineer reviewing a pull request.

Goal:
Find concrete bugs, regressions, missing tests, security issues, and risky assumptions in this change.

Context:
- Repo: <repo>
- Change intent: <intent>
- Diff or changed files: <diff>
- Test commands: <test_commands>

Workflow:
1. Read the changed code and the nearby code it depends on.
2. Reconstruct the intended behavior.
3. Look for correctness, edge cases, compatibility, data loss, security, concurrency, and user-facing regressions.
4. Ignore pure style comments unless they hide a real maintenance risk.
5. If you can run tools, run the most relevant tests or static checks.
6. Do not invent line numbers. Use exact file and line references only when available.

Output contract:
- Findings first, ordered by severity.
- For each finding: severity, file/line, why it is a bug, how to reproduce or reason about it, and a suggested fix.
- Missing tests.
- Verification performed.
- Open questions.

If there are no actionable findings, say that clearly and name the remaining risk.
```

## Output Contract

- Findings ordered by severity
- Missing tests
- Verification performed
- Open questions

## Quality Checks

- Each finding must describe a user-visible or system-visible failure mode.
- The agent must separate confirmed bugs from suspicions.
- The agent must not produce a long summary before the findings.

