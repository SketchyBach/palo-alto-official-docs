<!-- KOI source: https://docs.koi.ai/guardrails/mcp-registry-enforcement.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/mcp-registry-enforcement.md).

# MCP Registry Enforcement

Automatically removes MCP servers that are installed outside the [official Github MCP Registry](https://github.com/mcp) to maintain a trusted environment with only verified and approved servers.

## Why It Matters

* MCP servers installed outside the official registry bypass standard vetting and security processes.
* Manually installed or unofficial MCP servers can introduce security vulnerabilities, malicious code, or unstable functionality.
* The official MCP registry provides verified, tested, and maintained servers that meet security and quality standards.
* Organizations need assurance that only approved and trusted MCP servers are running in their environment.
* This guardrail ensures your MCP ecosystem includes only registry-approved servers, maintaining your organization's security posture.

## How It Works

* Detects MCP servers that are installed manually or from sources outside the official MCP registry.
* Automatically removes non-registry MCP servers from your endpoints to reduce security exposure.
* Continuously monitors for newly installed unofficial MCP servers and remediates them based on script execution cycles.

#### Supported Marketplaces

![](https://files.readme.io/39ca343d36afadee94bdc41479805ff30c72038dc2e0144530ee486ca8a115b8-image.png)

* VSCode (with more platforms to be added as MCP registry support expands)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/mcp-registry-enforcement.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
