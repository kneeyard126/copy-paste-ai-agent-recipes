---
id: agent-evals
title: Agent Evals Agent
summary: Create evaluation cases for an AI agent workflow or prompt.
difficulty: intermediate
time_saved: 45-180 min
tags: [agents, evals, quality]
---

# Agent Evals Agent

## Use When

Use this when an AI agent prompt, recipe, skill, or workflow needs regression tests before a team depends on it.

## Inputs

- `<agent_workflow>`: the prompt, recipe, skill, or tool flow to evaluate
- `<success_criteria>`: what a good answer must do
- `<failure_modes>`: mistakes the agent often makes
- `<real_examples>`: tickets, tasks, conversations, traces, or outputs to turn into test cases

## Copy-Paste Prompt

```text
You are an AI evaluation designer.

Goal:
Create a practical eval set for <agent_workflow>.

Context:
- Agent workflow: <agent_workflow>
- Success criteria: <success_criteria>
- Known failure modes: <failure_modes>
- Real examples: <real_examples>

Workflow:
1. Define the behavior the eval should measure.
2. Create a balanced set of easy, typical, edge, and adversarial cases.
3. For each case, specify input, expected behavior, unacceptable behavior, and scoring rubric.
4. Include at least one regression case for each known failure mode.
5. Recommend how to run the eval manually or in CI.
6. Keep the eval small enough to run repeatedly.

Output contract:
- Evaluation goal.
- Test case table.
- Scoring rubric.
- Pass/fail threshold.
- Regression cases.
- Suggested run cadence.
- Gaps and limitations.
```

## Output Contract

- Evaluation goal
- Test case table
- Scoring rubric
- Pass/fail threshold
- Regression cases
- Suggested run cadence
- Gaps and limitations

## Quality Checks

- Each test case must have observable pass/fail criteria.
- The eval must include negative cases, not only happy paths.
- The rubric must punish confident unsupported claims.

