<!-- KOI source: https://docs.koi.ai/guides/protect-ai-tools-with-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-ai-tools-with-koi.md).

# Protect AI tools with Koi

### Why It Matters

AI adoption on developer endpoints has moved beyond simple autocomplete extensions. Today's agentic tools can read credentials, execute shell commands, install packages, access APIs, and push code, all autonomously. The attack surface now spans five distinct component types, each with different risk profiles and governance needs.

Koi gives security teams a single platform to discover every AI component, assess its risk, enforce policy, and remediate violations across the full agentic workflow.

***

### AI Components Koi Protects

Koi classifies every AI-related item on the endpoint into one of five component types based on its role in the agentic workflow.

<figure><img src="https://2945959018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoCesslVFjeL8NIBlNmIK%2Fuploads%2FQJiOTUyNxKnnVvwCM10z%2Fimage.png?alt=media&#x26;token=b7edd4e7-fc8c-410d-816b-c5fc3e7e4ebd" alt=""><figcaption></figcaption></figure>

#### Agent Platforms

An Agent Platform is the application where AI capabilities run. It owns the UI, manages context (files, tabs, project state), can load agents and extensions from multiple providers, and connects to MCP servers.

**Key test:** Can agents from different providers be installed into it?

**Examples:** VS Code, Cursor, Windsurf, JetBrains IDEs, Warp

**What Koi does:**

* Discovers all agent platforms on endpoints
* Assesses platform configuration and security posture
* Pushes managed configuration (sandbox settings, policy hierarchy)
* Surfaces built-in agentic capabilities via the Autonomous flag

#### Agents

An Agent is an AI actor that plans and executes multi-step tasks autonomously using tools and APIs. Agents run inside a platform or standalone.

**Key test:** Does it execute multi-step tasks autonomosly after a single instruction?

| Subtype               | Description                            | Examples                                |
| --------------------- | -------------------------------------- | --------------------------------------- |
| **Agent (CLI)**       | Standalone terminal or app agent       | Claude Code, Claude Desktop, Gemini CLI |
| **Agent (Extension)** | Agent that runs inside a host platform | Cline, Junie, GitHub Copilot, Roo Code  |

**What Koi does:**

* Discovers all agents across endpoints (CLI and extension-based)
* Monitors agent activity: tool invocations, command execution, file access
* Enforces behavior policies and guardrails at runtime
* Manages agent configuration centrally (org > project > user)

#### AI Extensions

An AI Extension is a plugin or feature that uses AI for single, user-triggered actions inside a host application. No multi-step autonomy: each invocation is short-lived and user-driven.

**Key test:** One action per user trigger, installed into a host (not an agent)?

**Examples:** JetBrains AI Assistant, ChatGPT Sidebar, IntelliCode

**What Koi does:**

* Discovers AI extensions across all supported marketplaces
* Assesses risk (permissions, data access, publisher reputation)
* Enforces allow/block policies via Koi Supply Chain Gateway
* Remediates by removing extensions violating organizational policies

#### Agent Extensions

An Agent Extension is a plugin, skill, MCP server, or bundle that extends an agent's functionality. Unlike AI Extensions (user-triggered, installed into hosts), Agent Extensions are loaded into an agent and can be invoked by the agent itself during autonomous workflows.

Agent Extensions are unique hybrids that blend "code you run" with "text you trust." A typical extension combines instructions (natural-language directives injected into agent context), executable artifacts (scripts, templates, binaries), metadata (author, versioning), and access wiring (API keys, tokens, permissions).

**Key test:** Is it loaded into an agent and can the agent invoke it autonomously?

| Subtype                 | Description                                                                                                          | Examples                                 |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **MCP Server**          | Service exposing tools and data via Model Context Protocol                                                           | github-mcp-server, Slack MCP, notion-mcp |
| **Plugin**              | Bundles packaging commands, skills, hooks, and optional MCP servers.                                                 | Claude Code .plugin bundles              |
| **Skill (Coming Soon)** | A folder containing a SKILL.md file - essentially a prompt recipe that teaches an AI agent how to do a specific task | Claude Code `/commit` skill              |

**What Koi does:**

* Discovers agent extensions across MCP registries, plugin marketplaces, and endpoint scans
* Assesses risk for each extension type
* Enforces block policies via Koi Supply Chain Gateway (MCP registry, plugin marketplaces)
* Restricts extensions via managed configuration of the platform/agent
* Remediates by removing items violating organizational policies and pushing corrected config

#### AI Models

An AI Model is a local model artifact from registries or internal model stores.

**Examples:** Hugging Face models (Llama-2-7B, Granite), Ollama models, internal fine-tuned models

**What Koi does:**

* Discovers model downloads and local model files on endpoints
* Assesses risk (license, known vulnerabilities, publisher trust)
* Enforces allow/block policies via Koi SCG
* Remediates by removing blocked models

***

### Related Topics

* Agentic AI Governance Layers - How Koi enforces governance across three stacked enforcement layers
* MCP Servers - Governance - Deep dive into MCP server discovery, risk, and policy
* Policies
* Platform Coverage

***

## Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://docs.koi.ai/~/revisions/78dC1f2IregEAnf3UqxL/guides/protect-ai-tools-with-koi.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-ai-tools-with-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
