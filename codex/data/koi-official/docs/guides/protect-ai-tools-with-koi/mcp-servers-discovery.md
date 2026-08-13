<!-- KOI source: https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-servers-discovery.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-servers-discovery.md).

# MCP Servers - Discovery

The Koi MCP Inventory provides organizations with complete visibility into all [**Model Context Protocol (MCP)**](https://modelcontextprotocol.io/introduction) **servers** installed.

It tracks MCP servers launched from IDEs, AI tools, CLI workflows, or other scripts, whether they were configured manually or discovered from the [MCP registry](https://github.com/mcp). MCP servers are not just packages, they are live services that expose organizational context to agents and must be discovered, analyzed, and governed like any other software. It includes MCP gateways configured via JSON, providing visibility into user-defined connections that could bypass organizational controls.

***

## What is the MCP Inventory?

The MCP Inventory is a real-time view into all known MCP servers across endpoints in your organization. It helps:

* Understand what MCP servers are in use
* Track their installation source (manual vs. registry), platform integration and package type
* Monitor usage across devices

***

## Supported platforms

MCP Inventory supports MCP discovery across a wide range of developer tools and environments:

| Category            | Supported Platforms                                                                                               | Notes                                                                                          |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **IDEs**            | VSCode, Cursor, Windsurf, JetBrains (IntelliJ, PyCharm, WebStorm, GoLand, DataGrip, RustRover), Kiro, Antigravity |                                                                                                |
| **AI Tools**        | Claude desktop, Claude code, Cline, Roo, Codex                                                                    | Claude Desktop remote MCPs are not discoverable as they are not located on the endpoint itself |
| **Package Sources** | npm, PyPI, Docker Hub, GitHub Packages, Homebrew                                                                  |                                                                                                |
| **Runtimes**        | Node.js, Python, Docker, Local Binaries                                                                           |                                                                                                |

Koi continuously expands platform support to cover emerging AI-enhanced developer environments and new MCP-compatible runtimes.

## Inventory table fields

| Field                   | Description                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Name**                | Human-readable name of the MCP server                                                                                         |
| **Type**                | Indicates whether the server is running locally or is a remote connection                                                     |
| **Risk level**          | Indicates the security risk of the item based on Koi’s Wings risk engine.                                                     |
| **Platforms**           | IDEs or clients that launched the MCP (e.g. VSCode, Cursor, Claude)                                                           |
| **Endpoints**           | Number of unique devices the MCP server was observed on                                                                       |
| **Findings**            | Individual security insights derived from analyses that contribute to the overall risk score of a software item.              |
| **Package type**        | The package ecosystem used for installation (e.g. `npm`, `PyPI`, `Docker`, `Homebrew`)                                        |
| **Package name**        | The canonical package name (e.g. `@koi/server-hubspot`)                                                                       |
| **Transport**           | MCP transport type (when the value is "http" or stdio") indicating the communication method between the client and the server |
| **Installation method** | How the server was installed: `Manual` (added by the user) or `Marketplace` (discovered from the MCP registry)                |
| **Marketplace**         | The registry or marketplace source of the server                                                                              |
| **URL**                 | The local or remote endpoint the server is listening on                                                                       |
| **First seen**          | First timestamp Koi observed this MCP server on any endpoint                                                                  |
| **Last seen**           | Most recent timestamp of activity                                                                                             |

***

## MCP Risk Data

Koi enriches MCP server inventory with security-relevant data including tool discovery, authentication methods, and capability classification.

#### Tool Visibility

Koi discovers and catalogs tools exposed by MCP servers. For each server, Koi extracts tool names, descriptions, and input schemas. This applies to both local (package-based) and remote (URL-based) MCP servers.

**Known limitation:** Remote MCPs requiring authentication (API key or OAuth) cannot currently be scanned for tool information.

#### Authentication Type

Koi identifies the authentication method configured for each MCP server:

| Auth Type         | Description                              |
| ----------------- | ---------------------------------------- |
| No Authentication | Server is accessible without credentials |
| API Key           | Server requires an API key               |
| OAuth             | Server uses OAuth 2.0                    |

#### Tool Capability Categories

Each tool is classified with one or more capability categories indicating what the tool can do:

<table><thead><tr><th width="255.390625">Category</th><th>Description</th></tr></thead><tbody><tr><td>Code Execution</td><td>Runs scripts or shell commands within host or container</td></tr><tr><td>OS Commands</td><td>Modifies OS settings, processes, or environment variables</td></tr><tr><td>Internal Data Delete</td><td>Specifically designed to remove, wipe, or destroy local files, database records, or system assets</td></tr><tr><td>Internal Data Write</td><td>Creates or modifies local files and databases. Focuses on changing the content of assets</td></tr><tr><td>Internal Data Read</td><td>Retrieves data from local files, databases, or logs</td></tr><tr><td>Data Export</td><td>Transfers internal data to external servers or channels</td></tr><tr><td>External Service Call</td><td>Interacts with external APIs to trigger remote actions or change state in third-party apps</td></tr><tr><td>Untrusted Knowledge Retriever</td><td>Ingests data from third-party sources where content can be influenced by unverified actors - primary vector for Indirect Prompt Injection</td></tr><tr><td>Trusted Knowledge Retriever</td><td>Ingests data from organization-controlled platforms not reachable by third parties</td></tr></tbody></table>

A single tool may have multiple categories.

#### Where to find this data

* **Side panel → Overview tab**: Authentication type and tool capabilities
* **Side panel → Tools tab**: Full list of tools with descriptions and capabilities per tool

***

## Why does this matter?

MCP servers are powerful, they are runtime services that expose developer tools and organizational data (e.g., connections to proprietary knowledge sources used for contextual responses, local file systems, memory, browser state, shell access and more) to AI agents or automation tools.

MCP servers are launched from underlying code packages(e.g., via pip, npm, or containers) but behave like runtime services. They are treated as a distinct runtime item type in Koi. This distinction enables safer and more hermetic remediation mode without risking developer productivity, it’s not part of the dev’s critical environment.

MCP servers are the bridge between your organizational context and external AI agents

* They **expand the attack surface** beyond traditional software or code packages
* They run as **live services**, meaning they can:
  * Exfiltrate data
  * Execute arbitrary commands
  * Stream sensitive context
  * Connect to untrusted external agents or services

By indexing every MCP across your fleet, Koi gives security teams the tools to track, evaluate, and respond.

***

## Key benefits

* **Full visibility** into official and unofficial MCP usage
* **Risk scoring** based on server capabilities and reach (starting from npm\&PyPI based server)
* **Block and enforce remediation** for confirmed malicious or high-risk MCPs, as defined by organizational policies, with end-user notification.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-servers-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
