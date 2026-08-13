<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/ai-agents-discovery.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/ai-agents-discovery.md).

# AI Agents Discovery

Koi automatically identifies AI agents wherever they appear in your inventory - not just the agents on a predefined list, but any autonomous AI actor, including ones the industry hasn't named yet. As new agentic tools emerge constantly, this ensures Koi keeps pace and surfaces the "next OpenClaw" the moment it shows up on an endpoint.

***

## What is Agent Identification?

Agent Identification is an intelligence layer that examines every item flowing through Koi's discovery pipeline and answers two questions:

1. **Is this an AI agent?** so Koi can catch novel agents that aren't on anyone's radar yet, rather than relying on a fixed, hand-maintained list.
2. **Which agent is it?** mapping the item to a canonical identity, so all the components Koi already collects for that agent (MCP servers, plugins, skills, hooks) can be unified under one identity - *a capability coming in a future release (see Coming soon).*

Koi classifies against a deliberately broad definition of an agent:

{% hint style="warning" %}
An AI Agent is an autonomous AI actor that plans and executes multi-step tasks using tools and APIs. Agents run inside a platform (e.g. an IDE) or standalone.
{% endhint %}

Under this definition, dedicated agents like Claude Code, Cursor, Codex, Cline, and Windsurf are agents - while the infrastructure agents *use*, such as MCP servers, Ollama, or the OpenAI SDK, are not.

***

## How It Works

Each new item discovered in your inventory is scanned by an LLM-based classifier with web-search access. For every item, the classifier returns:

* Whether the item is an AI agent
* Which canonical agent it maps to
* A short evidence string explaining the decision

Because classification is reasoning-based rather than list-based, Koi identifies agents it has never explicitly been taught about - including open-source agent harnesses (e.g. Hermes), open-source agents (e.g. Goose), and well-known commercial agents alike.

***

## Beyond the Known List

With Agent Identification, the inventory now includes **every item classified as an agent**, wether its an npm package, Application or IDE extension, based on the broad agent definition above. This dramatically widens coverage:

* **Dedicated agents** whose primary purpose is to be an agent (Cursor, Claude Code, Windsurf, …) are identified as agents.
* **Embedded-agent applications** — products that aren't agents themselves but ship an agent feature (e.g. an IDE or creative tool with an agent mode) - are recognized as **agent platforms** and kept visible in the inventory, distinct from full agents.

This separation lets you see the complete agentic footprint across your fleet while still being able to focus on the dedicated agents that matter most.

***

## Finding Agents in the Inventory

Identified agents surface in the **Agentic AI Inventory**:

* The inventory includes all items classified as agents, expanding well beyond the previous predefined set.
* A dedicated **Agent** filter narrows the view to dedicated agents. Items classified as *agent platforms* remain in the table but are intentionally excluded from this narrower Agent filter.

<figure><img src="/files/aMIntot8e3bJtTmHhdGE" alt=""><figcaption></figcaption></figure>

***

## Why Does This Matter?

The agentic landscape moves faster than any static list can track. New agents - many of them open-source and self-hosted - appear in enterprise environments constantly, often without security teams knowing. If your inventory only recognizes a hardcoded set of known tools, every new or niche agent is a blind spot.

By identifying agents through reasoning rather than a fixed list, Koi:

* **Catches new and emerging agents** - including open-source and self-hosted ones, the moment they appear, instead of waiting for them to be added to a catalog.
* **Distinguishes true agents from the infrastructure they rely on**, so the inventory reflects actual autonomous actors rather than every AI-adjacent library.
* **Lays the groundwork to unify everything Koi knows about each agent** - its MCP servers, plugins, skills, and hooks - under a single canonical identity

***

## Key Benefits

* **List-independent coverage** that identifies any agent matching Koi's definition, not just pre-cataloged ones
* **Early detection of emerging agents**, so the "next OpenClaw" is visible from day one
* **Clear separation of agents vs. agent platforms**, giving you both full visibility and a focused view of dedicated agents
* **A canonical identity foundation** that future releases build on to consolidate every component tied to an agent

***

## 💎 **Coming soon:**

* **Canonical identity unification** - consolidating all the extensions Koi already collects for an agent (MCP servers, plugins, skills, hooks) under its single identified identity
* **Agent Inventory** - view all the different agents in one central location in the portal


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/ai-agents-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
