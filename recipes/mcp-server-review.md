---
id: mcp-server-review
title: MCP Server Review Agent
summary: Review an MCP server before connecting it to an AI agent.
difficulty: intermediate
time_saved: 30-150 min
tags: [agents, mcp, security, tools]
---

# MCP Server Review Agent

## Use When

Use this before installing or enabling an MCP server, connector, plugin, or tool gateway for an AI assistant.

## Inputs

- `<mcp_server>`: repository, package, manifest, or documentation
- `<intended_use>`: why the agent needs this server
- `<permissions>`: files, network, APIs, credentials, or systems it can access
- `<environment>`: local dev machine, CI, production, sandbox, or internal network

## Copy-Paste Prompt

```text
You are a security-minded AI tooling reviewer.

Goal:
Review <mcp_server> before it is connected to an AI agent.

Context:
- MCP server or tool gateway: <mcp_server>
- Intended use: <intended_use>
- Permissions requested: <permissions>
- Environment: <environment>

Workflow:
1. Identify what tools the server exposes and what each tool can change or read.
2. Check install scripts, runtime commands, network calls, credential handling, and update mechanism.
3. Look for prompt injection surfaces, command execution, file write access, data exfiltration paths, and unsafe defaults.
4. Decide whether the permissions match the intended use.
5. Recommend sandboxing, allowlists, read-only mode, logging, or human approval points.
6. Provide a go, no-go, or conditional-go recommendation.

Output contract:
- Summary.
- Tool and permission inventory.
- Main risks.
- Required mitigations.
- Safe configuration.
- Verification steps.
- Recommendation.
```

## Output Contract

- Summary
- Tool and permission inventory
- Main risks
- Required mitigations
- Safe configuration
- Verification steps
- Recommendation

## Quality Checks

- The agent must treat network, shell, file write, and credential access as high-risk by default.
- The recommendation must match the stated environment.
- The agent must not approve a tool simply because it is popular.

