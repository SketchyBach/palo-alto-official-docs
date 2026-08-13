<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/common-q-and-a.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/common-q-and-a.md).

# Common Q & A

Q: Do we support servers:

A: Technically, our script can run on Linux servers, but there may be some gaps. Our main focus is on workstations.

Q: What does the KOI lightweight script collect?

\
A:

The Koi agent runs on each managed endpoint on a schedule and sends back the data Koi needs for visibility and policy enforcement. It collects three things.

#### 1. Device and user identity

Hostname, OS, serial number, and Koi agent version. Local users with basic context (last logon, local admin, active sessions). On Windows, the Entra device ID so endpoints line up with your IdP.

#### 2. Installed developer and AI tooling

The core of what Koi does, an inventory of developer-facing software so we can risk-score it and apply policies:

* Browser extensions (Chrome, Edge, Firefox).
* IDE extensions and plugins (VSCode and forks, JetBrains, Notepad++).
* Packages (npm, PyPI, Homebrew, Chocolatey).
* AI coding assistants and their configs, including MCP servers (Claude Code, Cursor, Codex, Copilot).
* Other AI and dev tools: Ollama and Hugging Face models, Coder workspaces, Slack apps, Office add-ins, Git config.

For each item we capture name, ID, version, publisher, and which user installed it.

#### 3. Run results and optional AI agent activity

Structured logs of what the agent discovered, remediated, and any errors (this powers MDM run history). If AI agent guardrails are enabled, also activity logs and enforcement events from Claude Code, Cursor, Codex, and Copilot hooks.

#### What the agent does not collect

File contents, browsing history, keystrokes, screen contents, email, or chat messages. Scope is software inventory, device and user identity, and Koi's own run and enforcement telemetry.<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/common-q-and-a.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
