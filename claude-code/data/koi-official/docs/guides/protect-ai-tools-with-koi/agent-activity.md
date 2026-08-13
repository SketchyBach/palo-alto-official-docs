<!-- KOI source: https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-activity.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-activity.md).

# Agent Activity (Preview)

Koi Agent Activity provides organizations with visibility into AI coding agent behavior across all endpoints, starting with the highest-impact surface: MCP tool usage.

It aggregates MCP tool invocations from Cursor and Claude Code into a single, normalized view with clear attribution to user, endpoint, agent, and time. AI coding agents are not passive tools - they execute code, access sensitive files, and connect to external services through MCP, making them a critical surface for security and compliance. Agent Activity intercepts these actions at the agent loop level using native hooks, creating a centralized audit trail without disrupting developer workflows.

As the product evolves, Agent Activity will expand to cover additional agent lifecycle events; Shell commands, file operations, and prompts.

***

## Key Capabilities

* **MCP tool visibility:** See which tools agents are invoking, how frequently, and by whom.
* **All activity view:** Access complete activity logs covering all captured agent events in a single feed.
* **Identity attribution:** Every event is tied to a specific user and endpoint, enabling accountability.
* **Centralized view:** Aggregates activity from Cursor and Claude Code into a single, normalized feed.
* **Filtering and search:** Find relevant activity by tool, agent, user, endpoint, or time range.
* **Audit-ready logs:** Maintain complete audit trails for compliance and incident investigation.

💎 **Coming soon:** Expanded visibility into additional agent lifecycle events including shell commands, file operations, and prompts.

***

## How It Works?

Koi uses the **hooks system** built into [Cursor](https://cursor.com/docs/agent/hooks) and [Claude Code](https://code.claude.com/docs/en/hooks-guide). Hooks are intervention points in the agent execution loop that fire before or after specific actions.

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

### Cursor

Koi supports Cursor v1.7 and later through Cursor's Hooks feature. Hooks run before or after defined stages of the agent loop and allow external scripts to observe or modify behavior.

**Supported Events:**

* `beforeMCPExecution` - Fires before an MCP tool call executes.
* `afterMCPExecution` - Fires after an MCP tool call executes.
* `beforeSubmitPrompt` - Captures the user's prompt before it's sent to the model.
* `beforeShellExecution` - Fires before a shell command runs.
* `beforeReadFile` - Fires before a file is read and sent to the model.
* `afterFileEdit` - Fires after the agent modifies a file.

### Claude Code

Koi will support Claude Code through its hooks system, which provides similar lifecycle event capture.

**Supported Events:**

* `PreToolUse` - Fires before any tool execution (bash, MCP, file operations).
* `PostToolUse` - Fires after a tool completes successfully.
* `PermissionRequest` - Fires when Claude Code requests permission for an action.
* `UserPromptSubmit` - Fires when the user submits a prompt.

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

#### **Prerequisites**

* Cursor: Version 1.7 or later
* Claude Code: Version 1.0 or later

💎 **Coming soon:** Support for additional agent hosts: including Github Copilot, Gemini CLI, Kiro, Windsurf, and CLine.

#### **Deployment**

Agent Activity requires a `hooks.json` configuration file on each endpoint to intercept agent events. Koi can deploy this automatically via our script package:

* **No existing hooks:** Koi creates the hooks configuration file
* **Existing hooks:** Koi adds its command to the existing configuration, preserving your custom hooks

> **Note:** Agent Activity updates according to the script package's execution schedule, as the script retrieves the local file with each run.

#### Supported Paths

Koi deploys hooks to the enterprise configuration path, which takes the highest precedence and ensures consistent coverage across all users and projects on the endpoint.

* **Cursor:**&#x20;
  * macOS: `/Library/Application Support/cursor/hooks.json`&#x20;
  * Windows: `C:\ProgramData\Cursor\hooks.json`
* **Claude Code:** `managed-settings.json` deployed via MDM to OS-specific paths
  * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`

> **Note:** Cursor restart is required. After initial hook deployment, Cursor must be restarted once for hooks to take effect.

#### Verify Installation

*Cursor:*

1. Open Cursor → Settings → Hooks
2. Confirm hooks appear under "Configured Hooks"
3. Run any agent action (e.g., ask Cursor to read a file)
4. Check Koi dashboard → Agent Activity for the event

*Claude Code:*

1. Open managed settings file (see paths above per OS in 'Supported Paths')
2. Confirm Koi hooks appear under "hooks"
3. Run any agent action (e.g., ask Claude Code to read a file)
4. Check Koi dashboard → Agent Activity for the event


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-activity.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
