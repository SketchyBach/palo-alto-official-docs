<!-- KOI source: https://docs.koi.ai/guides/agentic-runtime-control/agent-enforcement-custom-policies.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/agentic-runtime-control/agent-enforcement-custom-policies.md).

# Agent Enforcement Custom Policies

Koi Agent Enforcement Custom Policies let admins author and compose enforcement rules tailored to their organization. Koi intercepts each agent action before it executes and returns block or ask based on the configured rules - with clear feedback to both the developer and the agent on every decision.

Policies are organized around five composable rule types, so admins can express granular rules ("block `git push --force` on Cursor for the developer-experiments group") or broad ones ("require approval before any MCP tool runs"). Custom Policies can also be created, updated, and managed via API. See the [Agent Runtime Policies API reference](https://docs.koi.ai/api-reference/reference/agents-runtime-policies).

> 💎 **Coming soon:** Ask mode for Cursor, and out-of-the-box policy templates curated by Koi's security team for common use cases across MCP and Skills enforcement, network controls (URLs/IPs), code execution, and file access.

***

### Why does this matter?

* Agents act with the full privileges of the user they work for. They run shell commands, read files, invoke tools, and call out to internal and external systems - often across long autonomous sessions where a single misstep can be costly.
* Built-in guardrails block universally dangerous actions, but every organization has additional rules that depend on its own systems, environments, and risk tolerance. There is no built-in way for an agent to know that a specific MCP tool is restricted, that a specific repository requires approval before pushing, or that a particular command should never run outside a sandbox.
* Detecting these violations after the fact is too late. Agents act in seconds, and many actions - credential reads, force pushes, destructive commands, exfiltration via MCP - are unrecoverable once they happen.
* Custom Policies let admins encode organization-specific rules into runtime enforcement, blocking or pausing the right actions in the right scope, before they execute.

***

### Key Capabilities

* **Composable rule types:** Build a policy from one or more of five rule types - shell execution, file access, MCP tools, skills, and network requests (URLs/IPs). A single policy can combine rules across multiple types.
* **Two enforcement modes:** Block (deny the action outright) or Ask (pause and require explicit user approval). Best fit per use case - block hard-no behavior, or ask the user to explicitly approve sensitive-but-legitimate actions like `git push`.
* **Block-only model:** Anything not matched by a policy is allowed by default, so developers keep working without friction outside the rules you set. Policies stack additively, so you can tighten controls over time without disrupting current workflows.
* **Endpoint group and per-agent scoping:** Apply a policy to specific endpoint groups for phased rollouts, and scope it to specific agents (i.e. Claude Code, Cursor, or all supported agents).
* **Estimated impact check:** Before enabling a policy, preview how many agent events from the last 30 days would have matched it according to the agent activity logs, so rollout is as predictable as possible.
* **Device exclusion flow:** When a developer is blocked, they can request a time-bound exception directly from the block message, according to a configuration in the policy definition.

***

### How It Works

Koi intercepts agent tool calls before the action executes and evaluates them against active policies.

{% code overflow="wrap" %}

```
Developer prompt → Policy check → Allow / Ask / Block →  Agent continues, prompts the user, or stops
```

{% endcode %}

* Admin creates a policy in the Koi portal - choosing rule types, target values, enforcement mode, and scope.
* Koi delivers the policy configuration to the endpoint on the next script run.
* When the agent attempts an action, Koi matches it against active policies. If multiple policies match, **Block takes priority over Ask**.
* Koi returns Allow, Ask (with an inline approval prompt to the developer), or Block - with structured feedback for both the developer and the agent.
* Every decision is logged.

All evaluation is done locally on the endpoint.

***

### Rule Types

A policy is built from one or more rules. Each rule targets a specific category of agent action.

<figure><img src="/files/LpgVOt5tkoUzltlWwGwu" alt=""><figcaption></figcaption></figure>

#### **Shell execution**&#x20;

Intercepts the commands an agent runs. Useful for blocking privilege escalation, risky package installs and registry overrides, environment enumeration, interactive shell spawning, and protected branch pushes. \
Examples:&#x20;

* block `sudo`, `terraform destroy`, `git push --force`, `pip install --index-url`.&#x20;
* Ask before `git push`.&#x20;

#### **File access**

Intercepts agent access to files and directories when the agent uses file I/O tools (Read, Write, Glob, Grep, etc.). File paths are extracted from event data (directly from tool arguments for file tools), and are matched against the policy rule using glob-style patterns.

Examples:&#x20;

* Block any access to `~/.ssh/*`, `**/.env`, `/var/run/docker.sock`.&#x20;
* Allow read on `**/.env` but block write and delete.&#x20;

{% hint style="info" %}
**Handling Shell-driven File Access**

File access rules cover **only file I/O tools**, not shell commands. Shell commands that read or write files (`cat`, `cp`, `rm`, etc.) are handled by the agent's shell tool - to intercept them, use a **shell execution** rule.
{% endhint %}

#### **MCP tools**

Intercepts the MCP server tools an agent invokes. A rule can target an MCP **tool name** (the tool being invoked, like `execute_query` or `send_email`) or also an **MCP server identifier** - the URL of a remote MCP server (like `https://mcp.slack.com`) or the package name of a local MCP server (like `@modelcontextprotocol/server-filesystem`).

The rule logic is either:

* **All tools matching a name across all MCP servers** - block a capability anywhere it appears, regardless of which MCP provides it.
* **Narrowed to a specific MCP server identifier** - block a tool only when invoked from a specific server, leaving the same tool available from other servers.

Examples:&#x20;

* Block tool `execute_query` from any MCP server.&#x20;
* Block `send_message` tool from MCP with  `https://mcp.slack.com`.&#x20;
* Block `execute_query` only when the MCP server matches `@company/db-server`.

#### **Skills**

**Skills.** Intercepts skills (slash commands and custom skills) the agent invokes - both when the agent invokes a skill autonomously and when the developer triggers one directly via slash command (like `/skill-name`).

#### **Network requests (URLs /** IPs)

Intercepts web and network access through the agent's web tools and `curl`. Supports exact domains, wildcard subdomains, raw IP addresses, cloud metadata IPs, and RFC 1918 private IP ranges.&#x20;

Examples:&#x20;

* Block `pastebin.com`, `*.internal.company.com`, raw IP addresses, `169.254.169.254` (cloud metadata, a common exfiltration target on AWS and GCP), or all browser tool usage.

{% hint style="info" %}
**Restricting Non-Curl Network Commands**

Only `curl` is parsed for URL/IP patterns in shell commands. To restrict `wget`, `scp`, `nc`, or other URL-fetching CLIs, use a shell execution rule.
{% endhint %}

***

### Estimated Impact Check

Before enabling a policy, you can preview its impact on your fleet. The estimated impact check queries all agent activity events from the last 30 days and shows how many would have been blocked by the current blocklist configuration.

**What it shows:**

* Total number of events that could have been blocked
* Number of affected endpoints
* Breakdown by matched path or command, with event counts and endpoint groups

**No matches state:** If no matching events are found, a confirmation message indicates that enabling the policy will not disrupt current workflows.

> **Note:** Impact check numbers are an estimate of the lower bound - actual coverage may be higher. Some historical events use relative file paths that can't always be resolved retroactively, so they may not be counted. Enforcement is unaffected: at runtime, Koi has full context to resolve every path accurately.

<figure><img src="/files/7r95NvXce0baWTm29lmC" alt=""><figcaption></figcaption></figure>

***

### Enforcement Modes

#### **Block**

Use Block for behaviors that are never acceptable in your environment. The developer is notified with the policy name and a link to request an exception. The agent receives an explicit "do not retry" instruction with a generic context message - matched patterns are intentionally not surfaced to prevent enumeration of protected resources.

Block is supported on **Claude Code and Cursor**.

#### **Ask**

Use Ask for actions a developer can legitimately perform manually but should not run automatically without explicit intent. If approved, the action proceeds and the decision is logged; if denied, the action is blocked.&#x20;

Ask is currently supported on **Claude Code only**.

**Example Ask policy:**

<figure><img src="/files/adku9FN3Ih9HVoztnCAC" alt=""><figcaption></figcaption></figure>

**Developer Ask Experience** - the user gets prompted to explicitly approve the action:

<figure><img src="/files/fLKSC3WriXipeqCswxvb" alt=""><figcaption></figcaption></figure>

💎 **Coming soon:** Ask mode support for Cursor.

When multiple policies match the same action, **Block takes priority over Ask**.

***

### Blocking Experience

Two messages are delivered when a policy fires - one for the developer, one for the agent. The dual-message approach ensures the developer understands what happened while instructing the agent not to retry.

#### **Developer-facing (shown in the IDE)**

On Block, the policy name and a link to request an exception, with a reference ID for admin escalation. On Ask, an approval prompt with the policy name and a summary of the pending action, alongside Approve and Deny buttons.

{% hint style="info" %}
**Customizable block message**

The message a developer sees on a block can be tailored to your organization. In Settings → End-user experience → [Customize block messages](https://docs.koi.ai/guides/end-user-experience-settings#customize-block-messages), open the editor for **Agents** to edit the Markdown template developers see when an agent action is blocked.

**Note:** The agent may rephrase your message in the chat, so the exact wording and formatting aren't guaranteed.&#x20;
{% endhint %}

<figure><img src="/files/Xti9u9kfc3xUJRC3zaFy" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/ITN1Q64wM9wzd2fb6EuS" alt=""><figcaption></figcaption></figure>

#### **Agent-facing (sent to the LLM)**

On Block, an explicit "do not retry" instruction with a context message that varies by rule type - for example, "This file path is protected" or "This command is restricted." If the policy has a configured suggested alternative, the agent also receives a one-line hint to reduce retry loops. On Ask, the agent is told to wait, then told the outcome - with an explicit "do not retry" instruction if the action was denied.

<figure><img src="/files/k9OUT3MMv5ybWZ7GDqX6" alt=""><figcaption></figcaption></figure>

***

### Policy Side Panel

Once a policy is live, open its side panel from the policy list in Agent Hardening to monitor and manage it. The panel has two additional tabs:

**Policy Hits**

Every block and ask event the policy fired, grouped by endpoint and agent. Expand any group to see individual events, each showing the matched rule type (File Path, Command, MCP Tool, Skill, or URL) and the matched entity. Use this to confirm a policy is catching what you intended and to spot noisy rules before they cause friction.

<figure><img src="/files/BAhCbG25FIwsQcZg0cBS" alt=""><figcaption></figcaption></figure>

**Excluded Endpoints**

The devices currently excluded from this policy, including who approved each exclusion and the justification. This gives admins an audit trail of every exception granted against the policy.

<figure><img src="/files/CIdqDJKZIidaddnH26xr" alt=""><figcaption></figcaption></figure>

***

### Request Exclusion Flow

When a developer is blocked by a policy for a legitimate reason, they can request an exclusion instead of being stuck. The block message includes a request link, and the request resolves into a **policy exclusion** - the device is excluded from that policy so the developer can proceed.

**How a developer requests an exclusion**

1. On a block, the developer clicks the **request exclusion** link in the IDE block message (carrying the reference ID).
2. A request form opens - The form is pre-filled with the policy name, device details, the action that triggered the block, and timestamp. The developer adds a justification.
3. The request routes to a security admin through Koi's approval workflow.

**How an admin resolves it**

The admin reviews the request and either denies it or grants an exclusion. Granting an exclusion is an admin action, so security teams keep control of every exception. Excluded devices, who approved each one, and the justification are all visible in the **Excluded Endpoints** tab of the policy side panel, giving a full audit trail of exclusions against the policy.

<figure><img src="/files/Fkx56gOVdbcqYwTaYKgr" alt=""><figcaption></figcaption></figure>

***

### Supported Agents <a href="#supported-agents" id="supported-agents"></a>

<figure><img src="/files/gaPmw9HAWHpOYTCa2AYW" alt=""><figcaption></figcaption></figure>

#### Rule type support

<table><thead><tr><th width="167.5390625">Rule type</th><th width="100.29296875">Claude Code</th><th width="100.03125">Cursor</th><th width="100.2265625">Codex</th><th width="99.61328125">Copilot</th><th width="95.078125">Gemini CLI</th><th width="123.8203125">Antigravity</th></tr></thead><tbody><tr><td>Shell execution</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>File access</td><td>✅</td><td>✅</td><td>✅ ¹</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>  ↳ Per-operation (read/write/delete)</td><td>✅</td><td>✅</td><td>❌ ¹</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>MCP tools</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Skills</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Network (URLs / IPs)</td><td>✅</td><td>✅</td><td>❌ ²</td><td>✅</td><td>✅</td><td>✅</td></tr></tbody></table>

¹ **Codex file access rules apply to all operations.** On Codex, you can block or allow access to a file path, but you can't differentiate between reading, writing, and deleting. A rule that targets `**/.env` will cover every kind of access to those files. On other agents, you can narrow a rule to specific operations - for example, allow reads but block writes and deletes on the same path.&#x20;

² **Network Controls** **aren't available on Codex.** Codex performs web access through a hosted search tool that runs on OpenAI's infrastructure rather than on the developer's machine, which means Koi can't intercept those requests at the endpoint. To control outbound network access on Codex endpoints, create a shell execution rule that restricts `curl`, `wget`, and similar commands.

#### Enforcement mode support

<table><thead><tr><th>Mode</th><th width="95.52734375">Claude Code</th><th width="94.45703125">Cursor</th><th width="90.48828125">Codex</th><th width="94.65234375">Copilot</th><th width="94.9765625">Gemini CLI</th><th width="120.984375">Antigravity</th></tr></thead><tbody><tr><td>Block</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Ask</td><td>✅</td><td>💎 <em>Coming soon</em></td><td>❌</td><td>✅</td><td>❌</td><td>✅</td></tr></tbody></table>

³ **Ask mode isn't available on Codex or Gemini CLI.** Koi's Ask flow relies on the agent's own approval prompt, and neither agent exposes one natively. Policies scoped to these agents are limited to Block.

***

### Relationship to [Agent Activity](/guides/agentic-runtime-control/agent-activity.md) <a href="#relationship-to-agent-activity" id="relationship-to-agent-activity"></a>

Agent Enforcement and Agent Activity share the same underlying hooks infrastructure and work together:

* **Agent Activity** provides visibility - capturing and logging all agent events for monitoring, investigation, and audit.
* **Agent Enforcement** adds protection - evaluating agent events against policies and blocking dangerous actions before they execute.

💎 **Coming soon:** Enforcement events (both allowed and blocked) appear in the Agent Activity feed with their enforcement decision, providing a complete audit trail that includes both what happened and what was prevented.

***

### Setup

Custom Policies run on the shared Runtime Protection deployment, which can be installed automatically through the Koi MDM script package. See [**Runtime Protection: Setup & Deployment**](/guides/agentic-runtime-control/setup-and-deployment.md) for prerequisites, deployment flow, and how to verify installation.

Once Runtime Protection is in place, Custom Policies are managed entirely from the Koi portal - creating, enabling, and updating policies does not require any endpoint changes.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/agentic-runtime-control/agent-enforcement-custom-policies.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
