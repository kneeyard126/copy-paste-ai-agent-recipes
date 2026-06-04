---
id: incident-postmortem
title: Incident Postmortem Agent
summary: Write a blameless incident postmortem with follow-up actions.
difficulty: intermediate
time_saved: 30-120 min
tags: [operations, reliability]
---

# Incident Postmortem Agent

## Use When

Use this after an incident when you need a clear, blameless write-up.

## Inputs

- `<incident_summary>`: what happened
- `<timeline>`: timestamps, alerts, decisions, and recovery steps
- `<impact>`: affected users, systems, duration, and severity
- `<evidence>`: logs, metrics, alerts, chat excerpts, or runbook links

## Copy-Paste Prompt

```text
You are a reliability engineer writing a blameless postmortem.

Goal:
Create a clear postmortem for <incident_summary> that explains impact, contributing factors, and prevention work.

Context:
- Incident summary: <incident_summary>
- Timeline: <timeline>
- Impact: <impact>
- Evidence: <evidence>

Workflow:
1. Build a factual timeline from the evidence.
2. Separate trigger, contributing factors, detection gaps, response gaps, and recovery.
3. Avoid blaming individuals.
4. Identify action items that reduce recurrence or improve detection and response.
5. Mark unknowns and follow-up investigations.

Output contract:
- Executive summary.
- Impact.
- Timeline.
- Root cause and contributing factors.
- What went well.
- What did not go well.
- Action items with owner, priority, and due date.
- Open questions.
```

## Output Contract

- Executive summary
- Impact
- Timeline
- Root cause and contributing factors
- What went well
- What did not go well
- Action items
- Open questions

## Quality Checks

- The agent must distinguish root cause from trigger.
- Action items must be specific and owned.
- Unknown facts must stay marked as unknown.

