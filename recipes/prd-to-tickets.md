---
id: prd-to-tickets
title: PRD to Tickets Agent
summary: Break a product brief into buildable engineering tickets.
difficulty: intermediate
time_saved: 45-180 min
tags: [product, planning, engineering]
---

# PRD to Tickets Agent

## Use When

Use this when a product requirements document needs to become engineering work.

## Inputs

- `<prd>`: product brief or requirements document
- `<constraints>`: timeline, team size, platform, tech limits, or scope boundaries
- `<existing_system>`: relevant architecture, APIs, or UX flows
- `<definition_of_done>`: release criteria

## Copy-Paste Prompt

```text
You are a product-minded engineering lead.

Goal:
Turn <prd> into buildable tickets with acceptance criteria, dependencies, and risks.

Context:
- PRD: <prd>
- Constraints: <constraints>
- Existing system: <existing_system>
- Definition of done: <definition_of_done>

Workflow:
1. Extract the user goal, non-goals, constraints, and success metrics.
2. Identify the smallest releasable slice.
3. Split work by user-visible behavior and technical dependency.
4. Write tickets that an engineer can estimate.
5. Include acceptance criteria that can be tested.
6. Flag missing decisions before they become hidden scope.

Output contract:
- Scope summary.
- Assumptions.
- Milestones.
- Tickets with title, user story, acceptance criteria, dependencies, estimate hint, and test notes.
- Risks.
- Open product questions.
```

## Output Contract

- Scope summary
- Assumptions
- Milestones
- Tickets
- Risks
- Open product questions

## Quality Checks

- Each ticket must produce a reviewable change.
- Acceptance criteria must be observable.
- The agent must separate MVP from later improvements.

