---
id: release-notes
title: Release Notes Agent
summary: Turn commits and pull requests into useful release notes.
difficulty: beginner
time_saved: 15-60 min
tags: [documentation, release]
---

# Release Notes Agent

## Use When

Use this when you need release notes that explain user impact instead of listing raw commits.

## Inputs

- `<version>`: release version or date
- `<changes>`: commits, pull requests, tickets, or changelog draft
- `<audience>`: end users, developers, admins, internal stakeholders
- `<known_issues>`: open bugs, migrations, or compatibility notes

## Copy-Paste Prompt

```text
You are a release notes editor.

Goal:
Write clear release notes for <version> that explain what changed and why users should care.

Context:
- Changes: <changes>
- Audience: <audience>
- Known issues: <known_issues>

Workflow:
1. Group changes by user impact, not by commit order.
2. Translate technical details into practical outcomes.
3. Separate new features, improvements, fixes, breaking changes, and known issues.
4. Call out actions users need to take.
5. Avoid marketing claims that are not supported by the change list.

Output contract:
- Release title.
- Highlights.
- New features.
- Improvements.
- Fixes.
- Breaking changes or migration notes.
- Known issues.
- Upgrade checklist.
```

## Output Contract

- Release title
- Highlights
- New features
- Improvements
- Fixes
- Breaking changes
- Known issues
- Upgrade checklist

## Quality Checks

- Every highlight must map to at least one provided change.
- The notes should be useful even to someone who never saw the pull requests.
- Breaking changes must be easy to find.

