<!-- KOI source: https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity/ai-agent-personal-account-usage.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity/ai-agent-personal-account-usage.md).

# AI Agent Personal Account Usage

Koi now detects the signed-in user account behind AI agent session, giving organizations visibility into personal (non-organizational) accounts used with AI agents like Claude Code and Cursor.

This capability is available in the AIDR (agent activity) view. For each agent session, Koi surfaces the user account, classifies the account as organizational or personal, and collects the account's subscription.

Use the Query Builder with the new **Personal user account** filter to instantly find all agent sessions running under personal accounts.

<figure><img src="/files/Lm1eoQvbFHJkKDILocrx" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/GitmSH2scUVAmkekOcsl" alt=""><figcaption></figcaption></figure>

### Why does this matter?

AI agents operate with broad access to the endpoint: they read and write files, execute shell commands, and call MCP tools. When an agent runs under a personal account, that activity happens entirely outside the organization's control.

Personal accounts introduce a real risks if **Data leakage**:

* Agents routinely ingest source code, internal org data, and customer data as context. Under a personal account, that data flows through an account the organization does not govern, which might leave your environment and depending on the account's settings it can even be used to train the model.&#x20;
* Free and personal subscription tiers of many AI providers may use conversation data for model training by default, unlike enterprise agreements that typically include data-protection and no-training commitments.

### Supported agents

Koi detects the signed-in user accounts per session for the following agents:

<table data-search="false"><thead><tr><th>Agent</th><th>User account</th><th>Subscription</th></tr></thead><tbody><tr><td>Claude Code</td><td>Supported for CLI only</td><td>Supported</td></tr><tr><td>Cursor</td><td>Supported</td><td></td></tr><tr><td>Codex</td><td>Supported</td><td>Supported</td></tr><tr><td>Antigravity</td><td>Supported</td><td></td></tr></tbody></table>

Koi continuously expands coverage to additional agents.

### &#x20;New fields in AIDR table&#x20;

| Field        | Description                                                               |
| ------------ | ------------------------------------------------------------------------- |
| User account | The email address of the account signed in to the agent for this session. |
| Subscription | The account's subscription tier (for example, Free, Pro, Enterprise).     |

These fields appear alongside the existing session details in AIDR, including agent, endpoint, actions, models, and agent extensions.

### Key benefits

**Full visibility**

See personal account used with AI agents across the organization, per session and per endpoint.

**Reduce data leakage risk**

Review sessions and learn more on the actions that where use with personal accounts.

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity/ai-agent-personal-account-usage.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
