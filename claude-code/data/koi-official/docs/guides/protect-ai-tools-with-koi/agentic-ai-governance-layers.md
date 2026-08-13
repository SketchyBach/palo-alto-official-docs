<!-- KOI source: https://docs.koi.ai/guides/protect-ai-tools-with-koi/agentic-ai-governance-layers.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agentic-ai-governance-layers.md).

# Agentic AI Governance Layers

AI coding agents read credentials, execute commands, install packages, and push code. No single enforcement layer is enough. Security comes from stacking layers so a failure in one is caught by the next.

Koi's governance model consists of three enforcement layers stacked on a shared visibility and audit foundation. Each layer catches what the one above it misses.

### The Enforcement Stack

<figure><img src="/files/rmO9LjKJF5EXCcCV1SRp" alt=""><figcaption></figcaption></figure>

| Layer                               | Governance Question                         | Scope                                   |
| ----------------------------------- | ------------------------------------------- | --------------------------------------- |
| **Layer 1: Execution Boundaries**   | Where does the agent run?                   | Sandboxed or isolated environment       |
| **Layer 2: Pre-Execution Controls** | What is the agent allowed to use?           | Policies, configs, supply chain gateway |
| **Layer 3: Runtime Enforcement**    | What can the agent do within allowed tools? | Dynamic restrictions at execution time  |
| **Visibility & Audit**              | What is happening?                          | Discovery, telemetry, logging           |

### Enforcement Modes

Koi's governance modes determine how strictly Layers 2 and 3 are enforced:

| Mode                         | Layer 1: Execution Boundaries                                                                         | Layer 2: Pre-Execution                                                                                                                          | Layer 3: Runtime                                                            |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Monitor / Warn**           | Insights on configured agents and platforms (is your IDE configured correctly?)                       | Inventory view of MCPs, extensions, skills, plugins, packages. Alert policies, flag gaps.                                                       | Agent activity visibility                                                   |
| **Enforcement**              | Enforce where the agent runs via managed configuration of the platform/agent (sandbox, dev container) | 1. Block policies on agent extensions, AI models, AI extensions via Koi SCG. 2. Restrict items via managed configuration of the platform/agent. | Prevent actions, commands, and access patterns via policies on top of hooks |
| **Enforcement & Mitigation** | --                                                                                                    | Remove blocked items, push corrected config                                                                                                     | Kill action, revert changes, terminate sub-agent if needed                  |

### Layer 1: Execution Boundaries

This layer answers: **where does the agent run?**

When enabled, agents run in a sandboxed environment. The sandbox limits blast radius regardless of what happens at the layers above.

Koi delivers this through managed configuration of the platform/agent, with two options:

1. **Koi-managed secure sandbox** - Koi pushes configuration to the platform to run within dev containers (or execute sensitive commands within them).
2. **Customer-managed dev containers** - Customers bring their own dev containers. Koi enforces within them via managed configuration and restricts agents running outside the container.

Both options give enterprise customers flexibility while Koi maintains governance.

### Layer 2: Pre-Execution Controls

This layer answers: **what is the agent allowed to use?**

Before any execution happens, Koi determines which agent extensions, AI models, AI extensions, and packages are approved, and how the platform/agent is configured.

#### Block policies via Koi's Supply Chain Gateway

Koi SCG (Supply Chain Gateway) blocks risky installs at the network level before they reach the endpoint. Block policies apply to agent extensions (MCP registry, plugin marketplaces), AI models, and AI extensions from their marketplace.

#### Restrictions via managed configuration

* **Restrict agent extensions, agents, or AI extensions** via managed configuration of the platform/agent (e.g., unapproved MCPs, extensions, skills, plugins). Koi is the single pane to define policies, pushed into the platform config layer. Centrally managed, locally enforced. The agent cannot modify these configurations.
* **Platform-native config-level tool blocking** - Some platforms support granular tool deny/allow rules in managed config files, enforced before execution. Koi uses this where available and falls back to runtime enforcement (Layer 3) where it's not.
* **Policy hierarchy** - Most platforms support multiple config levels (org, user, project). Koi defines policies at the highest available level, the strictest baseline that lower levels inherit and cannot override.

### Layer 3: Runtime Enforcement

This layer answers: **what can the agent do within those allowed tools?**

Even approved tools can be misused. This layer enforces restrictions dynamically at execution time via policies on top of hooks for agent extensions.

* **Curated guardrails** - Out-of-the-box protections against the most common agent risks: credential access, destructive operations, privilege escalation, data exfiltration, unauthorized writes. One-click protection, adjustable per policy.
* **Custom rules** - Enforcement rules synced to endpoints on session start. Customers define restrictions per group: which actions are allowed, which need human approval, which are blocked.

### Visibility & Audit: The Foundation

Governance without observability is guesswork. Visibility is the shared foundation that powers every enforcement layer with discovery, telemetry, and logging.

1. **Agent activity visibility** - Full logs of tool invocations, command execution, file access, and policy violations across all agent types.
2. **AI component inventory** - Agent extensions, AI models, AI extensions, agents, platforms, skills, plugins, sub-agents.
3. **Runtime violation visibility** - Policy violations, blocked actions, and anomalous agent behavior surfaced across all layers in real time.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-ai-tools-with-koi/agentic-ai-governance-layers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
