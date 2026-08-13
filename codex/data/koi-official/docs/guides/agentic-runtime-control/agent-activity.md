<!-- KOI source: https://docs.koi.ai/guides/agentic-runtime-control/agent-activity.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/agentic-runtime-control/agent-activity.md).

# Agent Activity (Preview)

Koi Agent Activity provides organizations with visibility into AI coding agent behavior across all endpoints, starting with the highest-impact surface: MCP tool usage.

It aggregates MCP tool invocations from supported AI coding agents into a single, normalized view with clear attribution to user, endpoint, agent, and time. AI coding agents are not passive tools - they execute code, access sensitive files, and connect to external services through MCP, making them a critical surface for security and compliance. Agent Activity intercepts these actions at the agent loop level using native hooks, creating a centralized audit trail without disrupting developer workflows.

As the product evolves, Agent Activity will expand to cover additional agent lifecycle events; Shell commands, file operations, and prompts.

***

## Key Capabilities

* **MCP tool visibility:** See which tools agents are invoking, how frequently, and by whom.
* **All activity view:** Access complete activity logs covering all captured agent events in a single feed.
* **Identity attribution:** Every event is tied to a specific user and endpoint, enabling accountability.
* **Centralized view:** Aggregates activity from all supported agents into a single, normalized feed.
* **Filtering and search:** Find relevant activity by tool, agent, user, endpoint, or time range.
* **Audit-ready logs:** Maintain complete audit trails for compliance and incident investigation.

***

## How It Works

Koi uses the **hooks system** built into each supported agent. Hooks are intervention points in the agent execution loop that fire before or after specific actions.

```
Developer prompt → [Hook fires] → Agent executes → [Hook fires] → Response
```

**The flow:**

1. Koi deploys a lightweight hook script to endpoints
2. Hooks capture events locally as structured JSON
3. Koi collects and normalizes events centrally
4. Events appear in the Agent Activity inventory

No performance impact - hooks write to a local file with minimal overhead.

***

## Supported Agents

Agent Activity is supported across several different coding agents. Each uses its own native hooks system; Koi normalizes events into a shared schema so the feed is consistent regardless of which agent produced the event.

* **Cursor** - [Cursor Hooks](https://cursor.com/docs/agent/hooks)
* **Claude Code** - [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
* **Codex CLI** - [Codex hooks](https://developers.openai.com/codex/changelog)
* **GitHub Copilot CLI** - [Copilot CLI hooks](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks)
* **Gemini CLI** - [Gemini CLI hooks](https://developers.googleblog.com/en/tailor-gemini-cli-to-your-workflow-with-hooks/)

For version requirements and deployment paths per agent, see [Runtime Protection: Setup & Deployment](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/runtime-protection/setup-and-deployment).

***

## Using Agent Activity

Agent Activity provides two dedicated views to help security teams monitor and investigate AI coding agent behavior:

#### All Activity View

Aggregates all captured events across your fleet into a single searchable feed. Filter by user, endpoint, time range, and event type to investigate specific behavior or monitor trends. This view supports compliance requirements, incident investigation, and behavioral analysis across the full agent lifecycle.

#### Tool Activity View

Focuses specifically on tool usage, providing detailed visibility into the MCPs and tools agents are invoking. It distinguishes between built-in agent tools and MCP-connected tools, and surfaces execution outcomes for each invocation. Use this view to track tool adoption, identify shadow tool usage, and investigate suspicious tool behavior.

#### Understanding MCP Tool Risks

Agent Activity starts with **MCP tool usage**, the highest-impact surface for agentic AI security. MCP tools enable AI agents to execute actions on external systems or resources like filesystems, databases, and email. A compromised or malicious MCP can exfiltrate credentials, access sensitive files, or manipulate agent behavior without user awareness. Key risks include:

* **Tool poisoning** – malicious instructions embedded in tool metadata, invisible to users but interpreted by AI models
* **Tool shadowing** – a malicious MCP manipulates agent behavior toward trusted tools without appearing in logs
* **Rug pulls** – tools that change behavior after initial approval
* **Supply chain compromise** – unvetted tools from public repositories

<figure><img src="/files/Pq8vZUjS2SyNbHFjBSNr" alt=""><figcaption></figcaption></figure>

#### Use Cases

**Tool Visibility**&#x20;

Track MCP tool invocations across your fleet to understand how agents are using tools in practice.

Agent Activity helps teams answer foundational questions: Which tools are agents using most? Which are configured but rarely used? Are agents invoking tools we didn't expect? Are certain tools behaving differently across users or environments?

Instead of relying on static configuration or assumptions, you get visibility into what actions actually occurred, who triggered them, and where they ran. This surfaces shadow AI activity: Where developers connect agents to unauthorized tools, and agents being manipulated into misusing legitimate tools before damage occurs.

💎 *Coming soon: Enforce tool policies directly from Koi's policy engine.*

**Shell Command Auditing** - 💎 Coming soon

Monitor shell commands executed by AI coding agents across endpoints. Agents run commands with developer privileges, creating risk of credential theft, destructive operations, or privilege escalation. Agent Activity surfaces dangerous patterns like `rm -rf`, external network calls, or chained commands. Governance layer can be added on top to block risky commands before execution.

**Behavioral Baselining -** 💎 Coming soon&#x20;

Establish normal agent behavior per user and machine to detect anomalies. Compromised or poisoned agents deviate subtly over time, making them difficult to identify. Agent Activity provides the data needed to spot outliers and investigate potential compromise.

***

## Setup

Agent Activity runs on the shared Runtime Protection deployment, which can be installed automatically through the Koi MDM script package. See [**Runtime Protection: Setup & Deployment**](/guides/agentic-runtime-control/setup-and-deployment.md) for prerequisites, deployment paths, and how to verify installation.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/agentic-runtime-control/agent-activity.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
