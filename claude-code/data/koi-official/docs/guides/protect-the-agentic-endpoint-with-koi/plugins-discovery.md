<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/plugins-discovery.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/plugins-discovery.md).

# Plugins Protection

Koi provides organizations with complete visibility into **plugins** installed across AI-powered supported platforms. Plugins extend the capabilities of AI coding agents with skills, commands, subagents, hooks, and MCP servers, all bundles as one.&#x20;

***

### What is Plugin Discovery?

Plugin Discovery provides a real-time view of all known plugins installed across Claude Code and Cursor on endpoints in your organization. It helps:

* Understand what plugins your developers are using across AI coding tools
* See exactly what each plugin contains - skills, commands, subagents, hooks, and MCP servers
* Track plugin metadata including source, version, and publisher
* Map the full dependency chain behind each plugin with the supply chain graph
* Identify MCP servers introduced through plugins and navigate directly to their MCP inventory entry

#### Supported Platforms

| Platform        | Discovery Method                                   | Supported Versions |
| --------------- | -------------------------------------------------- | ------------------ |
| **Claude Code** | Configuration-based discovery from managed devices | v1.0+              |
| **Cursor**      | Filesystem-based plugin enumeration                | v1.7+              |

Koi continuously expands platform support to cover additional AI-enhanced development environments.

#### Plugin Side Panel

Clicking any plugin opens a side panel with its details, components, and supply chain data.

#### Plugin Sub Components

The side panel shows a full breakdown of what's inside each plugin:

| Component       | Description                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| **Subagents**   | Autonomous agents bundled with the plugin that can perform tasks independently (e.g. `code-reviewer`)          |
| **Skills**      | Capabilities the plugin adds to the AI agent's toolkit                                                         |
| **Commands**    | CLI-style commands the plugin exposes                                                                          |
| **Hooks**       | Lifecycle hooks that execute at specific points during agent operation (e.g. before tool use, after file read) |
| **MCP Servers** | MCP servers bundled with or referenced by the plugin                                                           |

MCP servers listed within a plugin are **clickable** - you can navigate directly to the MCP server's dedicated inventory entry for deeper inspection of its tools, authentication, and risk data.

<figure><img src="/files/cPcSUyQlrkBmQTGnNMMd" alt=""><figcaption></figcaption></figure>

***

### Why Does This Matter?

Plugins are a rapidly growing part of the AI development stack. Unlike traditional IDE extensions that operate within a sandboxed environment, AI coding plugins can:

* **Introduce new MCP servers** that expose organizational data to agents
* **Add subagents** that autonomously perform tasks with broad access
* **Execute hooks** that run code at critical points in the agent lifecycle
* **Modify agent behavior** through skills and commands that change how the AI interacts with your codebase and infrastructure

Without visibility into what plugins are installed, security teams have no way to assess what capabilities and access patterns are active across their developer fleet. By discovering and cataloging every plugin, Koi gives you the foundation to understand, evaluate, and govern the AI tools your developers rely on.

***

### Plugin Remediation

Koi enables administrators to remediate **Claude Code** plugins directly from the platform.

#### What gets removed

When Koi remediates a Claude Code plugin, it fully removes the plugin's footprint from the endpoint:

* Removes the plugin from the developer's Claude Code settings.
* Removes it from the local plugin directory.
* Deletes all associated plugin files.

The remediated plugin will be shown in the remediation page, under the 'Pending' tab:&#x20;

<figure><img src="/files/66glh9CX0uD1gFOZx0RZ" alt=""><figcaption></figcaption></figure>

#### How remediation is triggered

Plugin remediation is run manually. You can remediate a specific plugin on demand from:

* Inventory table (single or bulk)
* Endpoints table
* Endpoint card in the item side panel.

***

### Key Benefits

* **Full visibility** into Claude Code and Cursor plugin usage across your organization
* **Component-level transparency** showing exactly what each plugin contains (skills, commands, subagents, hooks, MCP servers)
* **Supply chain mapping** tracing each plugin from its source through its dependencies to the endpoints where it runs
* **MCP and Skills correlation** linking plugins to the AI artifacts they introduce, with direct navigation to the artifact report for risk assessment.
* **Plugin governance** - remediation policies for plugins

***

### Known Limitations

* Plugins installed from **local file paths** or **remote URLs** (rather than official registries) are not yet discovered.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/plugins-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
