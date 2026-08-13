<!-- KOI source: https://docs.koi.ai/guides/agentic-runtime-control.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/agentic-runtime-control.md).

# Agentic runtime control

Koi Runtime Protection gives security teams real-time visibility and control over AI coding agents as they work - capturing what every agent does on the endpoint and intercepting actions that violate organizational policy before they execute.

Coding agents act autonomously: they read files, run shell commands, invoke MCP tools, and call out to the network with the developer's full privileges. Static configuration alone cannot govern this - security teams need to see what agents are actually doing, and stop the actions that should not happen, in the moment they happen.

***

### Why does this matter?

Agents are the most dynamic surface on the endpoint. The same agent can read a credential, push to a protected branch, install a package from an unvetted source, or invoke an MCP tool against a production database - all in a single session, without leaving traditional logs.

<figure><img src="/files/ZNisCnvHUkMDDCJmKixo" alt=""><figcaption></figcaption></figure>

Without **runtime visibility**, security teams can't answer foundational questions: Which agents are running, which tools they're invoking, and when an agent does something that should never have been allowed. Without **runtime enforcement**, visibility isn't enough - by the time a risky action surfaces in a review, it has already executed.

Runtime Protection closes both gaps. Koi captures every agent action across the fleet into a single, normalized audit trail, and intercepts actions that violate guardrails or custom policies before they execute - keeping secrets on the endpoint, dangerous commands out of production, and unvetted tools out of the agent loop, with minimal disruption to developer workflows.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/agentic-runtime-control.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
