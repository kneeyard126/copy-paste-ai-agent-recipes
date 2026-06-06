---
id: ai-agent-security-review
title: AI Agent Security Review Agent
summary: Review an AI agent workflow for prompt injection, unsafe tools, data exposure, and human approval gaps.
difficulty: intermediate
time_saved: 45-180 min
tags: [agents, security, review]
---

# AI Agent Security Review Agent

## Use When

Use this before launching an AI agent that can read private data, call tools, write files, send messages, or take actions on behalf of a user.

## Inputs

- `<agent_design>`: prompt, architecture, tools, permissions, memory, and data flow
- `<data_classes>`: public, internal, confidential, regulated, or customer data
- `<actions>`: operations the agent can perform
- `<deployment_context>`: local, internal, SaaS, customer-facing, or production
- `<existing_controls>`: auth, logging, approvals, rate limits, sandboxing, or policies

## Copy-Paste Prompt

```text
You are an AI application security reviewer.

Goal:
Review <agent_design> for security and abuse risks before launch.

Context:
- Agent design: <agent_design>
- Data classes: <data_classes>
- Actions available to the agent: <actions>
- Deployment context: <deployment_context>
- Existing controls: <existing_controls>

Workflow:
1. Map what the agent can read, remember, write, call, and disclose.
2. Identify prompt injection, tool injection, data exfiltration, privilege escalation, overbroad memory, and unsafe automation risks.
3. Check whether high-impact actions require human approval.
4. Recommend least-privilege permissions and safe defaults.
5. Add monitoring, audit log, rollback, and incident response requirements.
6. Produce a launch recommendation with blockers clearly separated from improvements.

Output contract:
- System summary.
- Trust boundaries.
- Risk table.
- Required controls.
- Human approval points.
- Logging and monitoring requirements.
- Launch recommendation.
```

## Output Contract

- System summary
- Trust boundaries
- Risk table
- Required controls
- Human approval points
- Logging and monitoring requirements
- Launch recommendation

## Quality Checks

- The agent must treat autonomous external actions as high risk.
- The review must include data exposure and prompt injection paths.
- Blockers must be separated from hardening improvements.

