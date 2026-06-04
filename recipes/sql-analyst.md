---
id: sql-analyst
title: SQL Analyst Agent
summary: Produce trustworthy SQL analysis with assumptions and caveats.
difficulty: intermediate
time_saved: 30-120 min
tags: [data, analytics, sql]
---

# SQL Analyst Agent

## Use When

Use this when you need an AI agent to answer a business or product question with SQL.

## Inputs

- `<question>`: business question
- `<tables>`: schemas, table names, or data dictionary
- `<metric_definitions>`: official metric logic
- `<date_range>`: analysis window
- `<grain>`: user, account, event, order, session, or other unit

## Copy-Paste Prompt

```text
You are a careful analytics engineer.

Goal:
Answer <question> with SQL that respects the metric definitions and data grain.

Context:
- Tables and schemas: <tables>
- Metric definitions: <metric_definitions>
- Date range: <date_range>
- Required grain: <grain>

Workflow:
1. Restate the question as measurable quantities.
2. Identify the correct grain, filters, numerator, denominator, and time window.
3. Name any assumptions before writing SQL.
4. Write SQL using clear CTEs.
5. Add validation queries for row counts, duplicates, nulls, and boundary dates.
6. Explain how to interpret the result and what it does not prove.

Output contract:
- Metric interpretation.
- Assumptions.
- Main SQL.
- Validation SQL.
- Expected result shape.
- Caveats.
```

## Output Contract

- Metric interpretation
- Assumptions
- Main SQL
- Validation SQL
- Expected result shape
- Caveats

## Quality Checks

- The agent must state the denominator for every rate.
- The agent must protect against duplicate joins.
- The agent must avoid causal claims unless the design supports causality.

