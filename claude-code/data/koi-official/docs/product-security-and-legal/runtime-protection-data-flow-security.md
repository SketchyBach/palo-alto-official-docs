<!-- KOI source: https://docs.koi.ai/product-security-and-legal/runtime-protection-data-flow-security.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/product-security-and-legal/runtime-protection-data-flow-security.md).

# Agent Runtime Protection: Data Flow & Security

### Introduction

Koi's Runtime Protection - [Runtime Agent Activity](https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity) and [Agent Enforcement Custom Policies](https://docs.koi.ai/guides/agentic-runtime-control/agent-enforcement-custom-policies), gives security teams visibility into, and control over, the actions AI agents take on employees endpoints. To do that, it observes those actions through each agent's native hooks.

Because it observes agent **actions** rather than installed-item metadata, Runtime Protection processes a more granular class of data than the rest of the Koi platform. This page documents that handling in full so it is unambiguous. For Koi's overall platform data handling and security measures, see the [Overview section](https://docs.koi.ai/security/overview).

***

### How Koi's Runtime Protection handles customer data

Three principles shape what is processed and where:

* **Enforcement happens on the endpoint.** Allow / Ask / Block decisions are computed locally, against policy already on the device. Koi's service receives a record of what happened for audit and investigation - it is not in the decision path, so a cloud disruption can never change what your endpoints permit.
* **It is scoped to the agent.** The hooks observe only the AI agents they are configured for, through those agents' own hook interfaces - not the terminal, the browser, or other applications. The only filesystem access is narrow and purpose-specific: reading local identity and configuration (such as account type and email) to attribute an event to the right user. Koi does not monitor the filesystem or capture the contents of files the agent didn't act on.
* **Data capture serves agent control.** What's recorded is the action an agent takes, focused on the input needed to enforce a policy and to make an event meaningful when a security team investigates it.

***

### What is collected

The content of each event is produced by the **agent**; Koi records what the agent passes to the hook. It falls into the action categories described in the [Agent Activity guide](https://docs.koi.ai/guides/agentic-runtime-control/agent-activity#actions):

* **Commands** - the shell command an agent runs (e.g. `git push --force`).
* **File access** - the **file path** an agent reads, writes, or deletes, and on a write or edit- the content the agent writes to it (e.g. a code diff).
* **MCP tool use** - the MCP server and tool an agent invokes.
* **Skill use** - the skill an agent invokes.
* **Network requests** - the URL or IP an agent reaches through its web tools and `curl`, and the content the agent retrieves (e.g. the body of a fetched page or search results).
* **Prompt** - the developer's prompt text, on agents that emit a prompt event.

Alongside each action, Koi records the context that makes it accountable: event type and timestamp, the agent and AI model in use, the [session](https://docs.koi.ai/guides/agentic-runtime-control/agent-activity#what-is-a-session) it belongs to, and the device, hostname, and user where available.

Two of these categories are more sensitive than the rest, and we want to be clear about them rather than let you discover the nuance later:

* **Prompts are free text** - they can contain whatever an employee types. Koi treats prompt text as the most sensitive category: it is masked in the portal view today, and stronger handling at rest is on our roadmap (see [Safeguards we're expanding](https://claude.ai/epitaxy/local_65be6415-e77a-4980-a588-35cb529045df#safeguards-were-expanding)).
* **A write or edit carries the changed text.** Koi doesn't separately scan your files - when an agent writes or edits one, the agent includes the changed text (such as a code diff) in that action, so it forms part of the recorded event. It enables effective investigation once required, investigator can view what an agent changed.
* **Fetched content comes back with the request.** When an agent uses a web-fetch or search tool, the material it retrieves - the page body or search results - is part of the recorded event, not just the address it reached. It enables effective investigation once required, investigator can view what an agent pulled into its context, not only where it went.

***

### What is not collected

* **The contents of files on disk.** Koi records the *path* an agent touches and the change it *makes*, not the content of files the agent didn't act on.
* **A separate terminal output stream.** Koi doesn't capture stdout/stderr independently of the agent's own event data.
* **Anything outside the agent.** Git, your IDE, your browser, and other applications are out of scope. Runtime Protection is an agent-runtime control for [scoped agents only](/guides/agentic-runtime-control/agent-activity.md#supported-agents).

***

### Controls

Runtime Protection inherits Koi's platform-wide protections - encryption in transit and at rest, customer data isolation, and audit logging - described in the [Security Overview](https://docs.koi.ai/security/overview#data-protection-and-security-measures). On top of those, this capability adds:

* **Tenant isolation at the source.** Every event is tagged with your tenant ID on the endpoint and stored under tenant partitioning; the portal and API are authenticated and scoped to your tenant, so one organization's activity is never accessible to another.
* **Portal Prompt redaction.** Prompt text is redacted before displaying in the sessions event view.
* **Block messages reveal nothing sensitive.** Matched patterns are intentionally not surfaced to the agent or employee, preventing enumeration of protected resources. See [Blocking Experience](https://docs.koi.ai/guides/agentic-runtime-control/agent-enforcement-custom-policies).
* **Exclusions are fully audited.** Every policy exclusion - who approved it and why - is recorded in the policy side panel. See [Request Exclusion Flow](https://docs.koi.ai/guides/agentic-runtime-control/agent-enforcement-custom-policies).

***

### Safeguards we're expanding

Koi is committed to giving you control over how your data is handled. We are continuously\
strengthening the privacy and data-governance capabilities of Runtime Protection, with an\
ongoing focus on:

* **Regional, per-tenant data storage** - so your agent activity is stored in your region and isolated to your tenancy, addressing data-residency and localization requirements.
* **Configurable retention** for agent activity, with automatic deletion at the end of the window. Until it's generally available, retention for your tenant can be arranged with your account representative.
* **Stronger at-rest handling of prompt text** - including options to redact, or to not persist, prompt bodies - for customers who want to minimize sensitive content in storage.
* **Telemetry granularity and opt-out** - including running enforcement-only without activity telemetry, and excluding prompt-submission events while keeping action telemetry.

If your organization has specific data-residency, retention, encryption, sub-processor, or internal-access requirements, your Koi account representative can provide the authoritative detail for your deployment and align these items to your timeline.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/product-security-and-legal/runtime-protection-data-flow-security.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
