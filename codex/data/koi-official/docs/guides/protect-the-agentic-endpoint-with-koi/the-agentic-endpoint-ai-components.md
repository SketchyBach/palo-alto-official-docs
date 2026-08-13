<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/the-agentic-endpoint-ai-components.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/the-agentic-endpoint-ai-components.md).

# The Agentic Endpoint AI Components

#### Agent Platforms

An Agent Platform is the application where AI capabilities run. It owns the UI, manages context (files, tabs, project state), loads agents and items from multiple providers, and connects to MCP servers.

**Key test:** Can agents from different providers run on it?

**Examples:** VS Code, Cursor, Windsurf, JetBrains IDEs

**What Koi does:**

* Discovers agent platforms on endpoints
* Assesses platform configuration and security posture
* Pushes managed configuration (sandbox settings, policy hierarchy) *(coming soon)*
* Identifies which platforms have built-in autonomous capabilities (agents that can act without user approval for each step)

**Why this matters for agent security:** The platform is the trust boundary. A misconfigured platform gives every agent and items running inside it excessive permissions. Koi ensures platforms enforce least-privilege defaults before agents even start.

***

#### Agents

An Agent is an AI actor that plans and executes multi-step tasks autonomously using tools and APIs. Agents run inside a platform or standalone.

**Key test:** Does it execute multi-step tasks autonomously after a single instruction?

<table><thead><tr><th width="201.5">Subtype</th><th>Description</th><th>Examples</th></tr></thead><tbody><tr><td><strong>Agent (CLI)</strong></td><td>Standalone terminal or app agent</td><td>Claude Code, Claude Desktop, Gemini CLI</td></tr><tr><td><strong>Agent (Extension)</strong></td><td>Agent that runs inside a host platform</td><td>Cline, Junie, GitHub Copilot, Roo Code</td></tr></tbody></table>

**What Koi does:**

* Discovers agents across endpoints (CLI and extension-based)
* Monitors [agent activity](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-activity): tool invocations, command execution, file access
* Enforces behavior policies and [guardrails](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-enforcement) at runtime
* Manages agent configuration centrally across organizational, project, and user levels *(coming soon)*

**Why this matters for agent security:** Agents are the actors in your environment. Without visibility into which agents are running and what they're doing, you can't govern the agentic supply chain. Koi gives you a live inventory of every agent and the policy controls to define what they're allowed to do.

***

#### AI Extensions

An AI Extension is an add-on or feature that uses AI for single, user-triggered actions inside a host application. Unlike agents, AI extensions do not plan or execute multi-step tasks autonomously - each invocation is short-lived and requires explicit user action.

**Key test:** Does it perform one AI-powered action per user trigger, without autonomous multi-step execution?

**Examples:** JetBrains AI Assistant, ChatGPT Sidebar, IntelliCode

**What Koi does:**

* Discovers AI extensions across all supported marketplaces
* Assesses risk (permissions, data access, publisher reputation)
* Enforces allow/block [policies](https://docs.koi.ai/policies-and-supply-chain-gateway/policies) via Koi Supply Chain Gateway
* Remediates by removing extensions violating organizational policies

**Why this matters for agent security:** AI extensions run alongside agents in the same platforms. A compromised AI extension can access the same context, credentials, and files that agents work with - making it a lateral attack vector into your agentic workflows.

***

#### Agent Extensions

An Agent Extension is a plugin, skill *(coming soon)*, MCP server, or bundle that extends an agent's functionality. Unlike AI Extensions (user-triggered, installed into hosts), Agent Extensions are loaded into an agent and can be invoked by the agent itself during autonomous workflows.

Agent Extensions are unique hybrids that blend "code you run" with "text you trust." A typical extension combines instructions (natural-language directives injected into agent context), executable artifacts (scripts, templates, binaries), metadata (author, versioning), and access wiring (API keys, tokens, permissions).

**Key test:** Is it loaded into an agent and can the agent invoke it autonomously?

<table><thead><tr><th width="175.765625">Subtype</th><th>Description</th><th>Examples</th></tr></thead><tbody><tr><td><strong>MCP Server</strong></td><td>Service exposing tools and data via Model Context Protocol</td><td>github-mcp-server, Slack MCP, notion-mcp</td></tr><tr><td><strong>Plugin</strong></td><td>Bundle packaging commands, skills, hooks, and optional MCP servers</td><td>Claude Code .plugin bundles, Cursor plugins</td></tr><tr><td><strong>Skill</strong> <em>(Coming Soon)</em></td><td>A structured recipe that teaches an agent or sub-agent how to perform a specific task, with context, instructions, and clear guidance</td><td>Claude Code <code>/commit</code> skill</td></tr></tbody></table>

**What Koi does:**

* Discovers agent extensions installed on endpoints, and scans external sources ([MCP registries](https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-servers-discovery), plugin marketplaces) to fetch data and risk-assess them
* Assesses risk for each extension type (permissions, code behavior, publisher trust, instruction content)
* Enforces block [policies](https://docs.koi.ai/policies-and-supply-chain-gateway/policies) via Koi Supply Chain Gateway ([MCP registry](https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-governance), plugin marketplaces)
* Restricts extensions via managed configuration of the platform/agent
* Remediates by removing items violating organizational policies and pushing corrected config

**Why this matters for agent security:** Agent extensions are the highest-risk component in the agentic supply chain. They execute with the agent's full privileges and combine executable code with prompt-level instructions that can alter agent behavior. External extensions sourced from registries can hide malicious code or risky behaviors, but even internally developed extensions can pose risk - they may request excessive privileges or be instructed to perform dangerous tasks. Koi treats every agent extension as a supply chain artifact - discovered, assessed, and governed regardless of its origin.

***

#### AI Models

An AI Model is a local model artifact downloaded from registries or internal model stores.

**Examples:** Hugging Face models (Llama-2-7B, Granite), Ollama models, internal fine-tuned models

**What Koi does:**

* Discovers model downloads and local model files on endpoints
* Assesses risk (license, known vulnerabilities, publisher trust)
* Enforces allow/block policies via Koi SCG
* Remediates by removing blocked models

**Why this matters for agent security:** Local models power offline agents and code-completion tools. A poisoned or mislicensed model can produce unsafe outputs or expose your organization to compliance risk - and agents that rely on these models inherit that risk.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/the-agentic-endpoint-ai-components.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
