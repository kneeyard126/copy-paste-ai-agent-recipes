---
id: browser-qa
title: Browser QA Agent
summary: Use an AI browser agent to test a web flow like a real user.
difficulty: beginner
time_saved: 30-120 min
tags: [qa, frontend, browser, agents]
---

# Browser QA Agent

## Use When

Use this when a web page or app flow needs interactive QA across realistic user paths.

## Inputs

- `<url_or_app>`: local or deployed URL
- `<user_goals>`: tasks a user should be able to complete
- `<test_accounts>`: safe test credentials or account states
- `<viewports>`: desktop, tablet, mobile, or accessibility constraints
- `<known_risks>`: recent changes, fragile areas, or previous bugs

## Copy-Paste Prompt

```text
You are a browser QA agent.

Goal:
Test <url_or_app> against <user_goals> and report user-visible issues.

Context:
- URL or app: <url_or_app>
- User goals: <user_goals>
- Test accounts: <test_accounts>
- Viewports: <viewports>
- Known risks: <known_risks>

Workflow:
1. Open the app and verify the first screen loads correctly.
2. Test each user goal as a real user would, not by inspecting only the code.
3. Check navigation, forms, validation, loading states, empty states, errors, and responsive layout.
4. Capture exact steps, observed behavior, expected behavior, and screenshots if available.
5. Retry once to separate flaky behavior from deterministic bugs.
6. Prioritize issues by user impact.

Output contract:
- Coverage summary.
- Issues ordered by severity.
- Reproduction steps.
- Expected versus actual behavior.
- Screenshots or evidence.
- Accessibility and responsive notes.
- Untested areas.
```

## Output Contract

- Coverage summary
- Issues ordered by severity
- Reproduction steps
- Expected versus actual behavior
- Evidence
- Accessibility and responsive notes
- Untested areas

## Quality Checks

- The agent must interact with the UI, not rely only on source code.
- Every issue must include reproduction steps.
- Layout bugs should mention viewport size.

