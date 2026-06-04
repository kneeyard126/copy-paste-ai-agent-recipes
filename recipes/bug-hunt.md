---
id: bug-hunt
title: Bug Hunt Agent
summary: Reproduce, isolate, fix, and verify a bug.
difficulty: intermediate
time_saved: 45-180 min
tags: [engineering, debugging]
---

# Bug Hunt Agent

## Use When

Use this when you have a bug report but the root cause is unclear.

## Inputs

- `<bug_report>`: user report, ticket, or failing behavior
- `<expected_behavior>`: what should happen
- `<environment>`: browser, OS, service version, dataset, or config
- `<repo_or_logs>`: code, logs, traces, or screenshots

## Copy-Paste Prompt

```text
You are a debugging agent.

Goal:
Reproduce the bug, isolate the root cause, propose the smallest safe fix, and verify it.

Context:
- Bug report: <bug_report>
- Expected behavior: <expected_behavior>
- Environment: <environment>
- Repo, logs, or traces: <repo_or_logs>

Workflow:
1. Restate the bug as observed behavior versus expected behavior.
2. List the top three plausible causes and the evidence needed for each.
3. Try to reproduce the bug with the smallest input or path.
4. Inspect the code or system path that handles that input.
5. Make one focused fix.
6. Add or update a regression test.
7. Run the narrowest verification first, then broader checks if needed.

Output contract:
- Reproduction status.
- Root cause.
- Patch summary.
- Regression test.
- Verification.
- Risks or follow-up work.
```

## Output Contract

- Reproduction status
- Root cause
- Patch summary
- Regression test
- Verification
- Follow-up work

## Quality Checks

- The agent must not skip reproduction unless the context makes it impossible.
- The fix should be smaller than the investigation.
- The regression test must fail before the fix in principle, even if the agent cannot run it twice.

