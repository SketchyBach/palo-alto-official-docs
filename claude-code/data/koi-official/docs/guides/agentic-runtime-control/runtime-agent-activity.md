<!-- KOI source: https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity.md).

# Runtime Agent Activity (AIDR)

Session-centric visibility into what AI coding agents actually did across your organization - every shell command, file access, MCP tool call, skill, and network request, correlated into the coding session that produced it.

Koi Runtime Agent Activity gives security teams a clear, normalized record of AI coding agent behavior across all endpoints, organized around **sessions** as the primary unit. Instead of a flat stream of disconnected events, every action an agent takes is grouped into the originating session it belongs to, so you can see the full arc of an agent's work from start to finish: what the end user asked for, which tools and extensions the agent reached for, which files it touched, what ran on the endpoint, and what was blocked. Koi captures this at the agent loop level using each agent's native hooks, with no disruption to developer workflows.

***

## Why does this matter?

* AI coding agents act with the full privileges of the developer they work for. In a single session an agent can run shell commands, read and write files, invoke MCP tools, trigger skills, and reach out to internal and external systems, often across long autonomous runs.
* When one of those actions looks suspicious, a flat event log forces investigators to reconstruct the story by hand, stitching events together by timestamp and endpoint with no way to see what else happened in the same conversation.
* Context is what makes an event meaningful. A single MCP tool call or file read is hard to judge in isolation; the same action inside its session, alongside the prompt that led to it and the actions around it, tells you whether it was routine or a problem.
* Runtime Agent Activity correlates events into sessions automatically, so security teams get the complete picture in one place and can answer "what did this agent actually do, and was any of it stopped?" in seconds.

***

## What is a session?

A session is a single continuous conversation between a developer and a coding agent, scoped to a project or repository. It is what a developer experiences as "one chat with the agent," and it is the unit Koi uses to group everything that agent did on the endpoint.

Koi does not invent its own session concept. Every supported coding agent already issues a native session identifier through its hooks, and Koi adopts that identifier directly. A Koi session begins on the first event that carries a given session identifier and ends when the agent signals that the session is over (a session-end event or the process exiting). When no end signal arrives, Koi closes the session after a configurable period of inactivity (30 minutes by default).

### Session boundaries per agent

Each agent uses its own hooks system and its own wording for a session. Koi normalizes all of them into one shared session schema, so the feed reads consistently no matter which agent produced the activity.

#### [Cursor](https://cursor.com/docs/agent/hooks)

* **Session terminology:** Chat or conversation
* **Session identifier:** `conversation_id` per chat, `generation_id` per prompt, and `session_id` on session start and end
* **When a session starts and ends:** Starts on a new chat. Ends when the chat closes or a new chat opens.
* **Resume behavior:** Cursor issues a new identifier on resume. Koi links the continuation to the original conversation so it stays one session.

#### [Claude Code](https://code.claude.com/docs/en/hooks-guide)

* **Session terminology:** Session
* **Session identifier:** `session_id` on every event
* **When a session starts and ends:** Starts on launch. Ends on `/clear` or when the process exits.
* **Resume behavior:** Claude Code issues a new identifier on resume. Koi links the continuation to the original conversation so it stays one session.

#### [Codex CLI](https://developers.openai.com/codex/changelog)

* **Session terminology:** Session
* **Session identifier:** `session_id` on all events, plus `turn_id` per turn
* **When a session starts and ends:** Starts on a `codex` run. Ends when the process exits.
* **Resume behavior:** Codex keeps the same identifier on resume, so a resumed conversation stays one session automatically.

#### [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks)

* **Session terminology:** Session
* **Session identifier:** `sessionId` on every event, with a start reason and an end reason
* **When a session starts and ends:** Starts on a new chat or assigned task. Ends on completion or stop.
* **Resume behavior:** Copilot CLI keeps the same identifier on resume, so a resumed conversation stays one session automatically.

#### [Gemini CLI](https://developers.googleblog.com/en/tailor-gemini-cli-to-your-workflow-with-hooks/)

* **Session terminology:** Session
* **Session identifier:** `session_id` on all events
* **When a session starts and ends:** Starts on launch. Ends when the process exits.
* **Resume behavior:** Gemini CLI issues a new identifier on resume. Koi links the continuation to the original conversation so it stays one session.

### Resuming a conversation

Developers often pick up an earlier conversation rather than starting fresh. Some agents keep the same session identifier when a conversation is resumed, and others issue a new one. Koi recognizes both behaviors and keeps a resumed conversation as part of the same session, so a long piece of work that spans several restarts appears as one continuous session rather than fragmenting into unrelated pieces. This keeps the timeline complete and makes long-running sessions investigable end to end.

For version requirements and deployment paths per agent, see [Runtime Protection: Setup & Deployment](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/runtime-protection/setup-and-deployment).<br>

***

## Key Capabilities

* **Session-centric view:** One row per coding session, so the full arc of an agent's work is the default unit of investigation.
* **Full session timeline:** Open any session to see every action in order - file read, write, and delete, code execution, MCP tool use, skill use, and network requests - each with its timestamp and the target or resource it touched (path, URL, or tool name).
* **Agent extensions per session:** See which MCP servers, skills, and plugins a session used.
  * \[💎 Coming soon] Link directly to the Agentic AI Inventory item for each one, to see the it's risk report.
* **Blocked actions in context:** Actions stopped by an enforcement policy are clearly marked with the reason and the policy that triggered them, right inside the session timeline.
* **Centralized and normalized:** Activity from all supported agents is aggregated into one shared schema, so the feed is consistent regardless of which agent produced it.
* **Filtering, search, and saved queries:** Find sessions by agent, endpoint, user, action category, extension, duration, or time range, and save the queries you use often.
* **Identity attribution:** Every session and every event is tied to a specific agent, endpoint and user (when available), so activity is always accountable.
* **Audit-ready logs:** Complete, session-correlated audit trails for compliance and incident investigation.

***

## How It Works

Koi uses the **hooks system** built into each supported agent. Hooks are intervention points in the agent execution loop that fire before or after specific actions.

```
Developer prompt → [Hook fires] → Agent executes → [Hook fires] → Response
```

**The flow:**

* Koi deploys a lightweight hook script to endpoints.
* Hooks capture events locally as structured data, each tagged with the agent's native session identifier.
* Koi collects the events centrally, normalizes them into a shared schema, and correlates them into sessions, keeping resumed work as part of the same session.
* Sessions and their timelines appear in the Runtime Agent Activity inventory.

Capture runs locally on the endpoint with minimal overhead, so there is no impact on developer workflows.

***

## Actions&#x20;

Each action in a session timeline is classified into one of six categories, detected from the agent's own event for that action:

* **Commands** - the commands an agent runs.
* **File access** - reads, writes, and deletes through the agent's file tools, identified by file path.
* **MCP tool use** - the MCP server tools an agent invokes, identified by tool name.
* **Skill use** - skills and slash commands the agent invokes, identified by skill name.
* **URLs and IPs** - web and network access through the agent's web tools, identified by **URL** or **IP**.

Coverage varies by agent based on what each agent exposes through its hooks. For example, Codex reports file access without distinguishing read from write or delete, and performs web search on hosted infrastructure that does not pass through endpoint hooks.

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

#### Sessions table

The primary view lists one row per session over the time window you select. Columns include the session, the agent, the endpoint, the action categories present in the session, the agent extensions used, the number of events, the duration, and when it started. Above the table, aggregates for the selected window show total sessions, distinct endpoints, distinct users, and average session duration.

The Query Builder lets you filter sessions by agent, endpoint, action category, extension, duration, and more, with saved queries supported. Key columns are sortable, and the existing column picker and export controls are available.

#### Session detail panel

Selecting a session opens a side panel, with navigation to move to the previous or next session in your filtered list without closing it:

* **Overview** - session metadata (agent, endpoint, user, model, duration, and start time), the action categories present, and the list of agent extensions used.
* **Events timeline** - every event in the session in chronological order, each with its timestamp and the resource it touched. Expanding an event shows its detail, such as a code diff or a tool's input and output. Blocked events are clearly marked with the reason and the policy that stopped them.

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
GET https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
