<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi.md).

# Protect the agentic endpoint with Koi

### Background

As AI adoption accelerates among enterprise organizations, end users use and build AI-powered software and workflows at a growing pace. **Endpoints are becoming agentic** - machines running AI agents that read credentials, execute shell commands, install packages, access APIs, and push code autonomously.\
But agents don't operate alone: they consume software from MCP registries, plugin marketplaces, skills repositories and code package registries to do their work - and your end users may not even notice when this happens.

Koi's **Agentic Endpoint Security** (AES) gives security teams a single platform to discover every AI component across the agentic endpoint, assess its risk, enforce policy, and remediate violations - so your end users adopt the latest technology, increase the org productivity without compromising on security.

***

### The Agentic Endpoint

When an agent processes a task, it often reaches beyond its built-in capabilities: it connects to an MCP server for Postgres database access, loads a plugin for deployment workflows, invokes a skill for code review, or uses an MCP server to send emails and access sensitive attachments. These items can come from external registries, internal repositories, or be configured directly by users - and each is a potential entry point for malicious code, prompt injection, or other organizational security risks.

Koi maps and secures every layer of this supply chain:

<table><thead><tr><th width="180.1796875">Source Type</th><th>What Flows Through It</th><th>Risk Profile</th></tr></thead><tbody><tr><td><strong>MCP Registries</strong></td><td>MCP servers that expose tools and data to agents</td><td>Servers can access APIs, databases, and credentials on the agent's behalf. A malicious MCP server can exfiltrate data or execute arbitrary commands.</td></tr><tr><td><strong>Plugin Marketplaces</strong></td><td>Bundles packaging commands, skills, hooks, and optional MCP servers</td><td>Plugins combine executable code with natural-language instructions injected into agent context - blending "code you run" with "text you trust."</td></tr><tr><td><strong>Code Package Registries</strong></td><td>Code packages from npm, PyPI, and other registries that agents install or depend on</td><td>Supply chain risks such as malware, typosquatting, and dependency confusion - amplified because agents can install packages autonomously without human review.</td></tr><tr><td><strong>Skills Repositories</strong> <em>(Coming Soon)</em></td><td>Prompt "recipes" that teach agents specific tasks</td><td>Skills shape agent behavior through instructions. A tampered or risky skill can redirect agent actions, leak context, or bypass guardrails.</td></tr></tbody></table>

***

### AI Components Koi Protects

Koi classifies every AI-related item on the endpoint into five component types based on its role in the agentic workflow.

![AI Components Koi Protects](https://2945959018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoCesslVFjeL8NIBlNmIK%2Fuploads%2FQJiOTUyNxKnnVvwCM10z%2Fimage.png?alt=media\&token=b7edd4e7-fc8c-410d-816b-c5fc3e7e4ebd)

#### How Koi protects AI Components

<table data-view="cards"><thead><tr><th data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="/spaces/oCesslVFjeL8NIBlNmIK/pages/WZG23fFHI4W0SemhhQwX">/spaces/oCesslVFjeL8NIBlNmIK/pages/WZG23fFHI4W0SemhhQwX</a></td></tr><tr><td><a href="/spaces/oCesslVFjeL8NIBlNmIK/pages/eRRKxYv8HJX6PslJSsXO">/spaces/oCesslVFjeL8NIBlNmIK/pages/eRRKxYv8HJX6PslJSsXO</a></td></tr><tr><td><a href="/spaces/oCesslVFjeL8NIBlNmIK/pages/scPPlQyntAdGU3WpH7BN">/spaces/oCesslVFjeL8NIBlNmIK/pages/scPPlQyntAdGU3WpH7BN</a></td></tr><tr><td><a href="/spaces/oCesslVFjeL8NIBlNmIK/pages/OomnqT14v4MGvXTtZIbl">/spaces/oCesslVFjeL8NIBlNmIK/pages/OomnqT14v4MGvXTtZIbl</a></td></tr><tr><td><a href="/spaces/oCesslVFjeL8NIBlNmIK/pages/lufeardNFjhaEx3fNvSG">/spaces/oCesslVFjeL8NIBlNmIK/pages/lufeardNFjhaEx3fNvSG</a></td></tr><tr><td><a href="/pages/TqhzYgmX9ADFWVqDrxsk">/pages/TqhzYgmX9ADFWVqDrxsk</a></td></tr><tr><td><a href="/pages/rAxxEqD2rX0UpUjoXlP3">/pages/rAxxEqD2rX0UpUjoXlP3</a></td></tr></tbody></table>

***

### Visibility: Know What Your Agents Use

Koi provides continuous visibility across the full agentic supply chain - not just what's installed, but what agents are actively consuming.

**Agentic AI Inventory** - A live inventory of every AI component across your endpoints: platforms, agents, extensions, agent extensions, and models. Filter by type, risk level, findings, etc.

<figure><img src="/files/Ui5tyCxTdwHcXfIi9IX1" alt=""><figcaption></figcaption></figure>

**Extension Sources** - See where agent extensions originate: which MCP registries, plugin marketplaces, and skills repositories *(coming soon)* your agents pull from. Identify unvetted or shadow sources.

[**Agent Activity**](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-activity) - Monitor what agents are doing in runtime: which tools they invoke, which extensions they load, and which commands they execute. Spot anomalies before they become incidents.

***

### Governance: Control installs, verify configuration, and manage agent behavior at runtime

Koi enforces governance at [three levels](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agentic-ai-governance-layers) - ensuring your agents consume secure software, are securely configured, and act safely on runtime.

[**Supply Chain Gateway (SCG)**](https://docs.koi.ai/policies-and-supply-chain-gateway/policies) - Sits between your agents and [MCP registries](https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-governance) and [package registries](https://docs.koi.ai/guides/protect-code-packages-with-koi). Enforces allow/block policies inline, before MCPs and Code packages reach the endpoint.

**Endpoint Remediation** - Identifies risky extensions already installed on endpoints and removes them. Closes the gap between policy and reality by continuously reconciling what's running against what's allowed.

**Continuous enforcement** - Koi continuously scans managed endpoints for agent extensions (MCP servers, plugins, and skills \[coming soon]) that violate organizational policies and removes them automatically. Re-installations are detected and removed on subsequent scans, ensuring persistent compliance.

**Agent Activity & Enforcement -** monitor agents behavior at runtime, block risky actions before they're taken and ensure a consistent security standard to prevent agent-based security incidents.

**Managed Configuration** *(coming soon)* - Pushes security configuration directly to agent platforms and agents. Controls which extensions can be loaded, which permissions are granted, and which behaviors are allowed - centrally managed at org, project, or user scope.

![Agentic AI Governance Layers](https://2945959018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoCesslVFjeL8NIBlNmIK%2Fuploads%2Figvzpz6DyrVVlPD5ikWo%2Fimage.png?alt=media\&token=9f567d5f-1515-4c23-aec0-b56b749db871)

***

### Related Topics

* [Agentic AI Governance Layers](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agentic-ai-governance-layers) - How Koi enforces governance across three stacked enforcement layers
* [MCP Servers - Governance](https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-governance) - Deep dive into MCP server discovery, risk, and policy
* [MCP Servers - Discovery](https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-servers-discovery) - Full MCP inventory and source tracking
* [Agent Activity](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-activity) - Monitor agent tool invocations and behavior
* [Agent Enforcement](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-enforcement) - Runtime guardrails for agent actions
* [Policies](https://docs.koi.ai/policies-and-supply-chain-gateway/policies) - Configure allow, block, and alert rules
* [Policy Library](https://docs.koi.ai/guides/governance-best-practices/policy-library) - Pre-built policies including AI-specific rules
* [Governance Best Practices](https://docs.koi.ai/guides/governance-best-practices) - Guardrails, policies, and remediation layers
* [Platform Coverage](https://docs.koi.ai/get-started/platform-coverage) - Full list of supported marketplaces and capabilities
* [Protect Code Packages with Koi](https://docs.koi.ai/guides/protect-code-packages-with-koi) - Package registry governance for npm, PyPI, and more
* [MCP Registry Enforcement](https://docs.koi.ai/guardrails/mcp-registry-enforcement) - Guardrail ensuring only registry-approved MCP servers


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
