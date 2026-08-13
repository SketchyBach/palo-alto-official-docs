<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/dynamic-tool-description.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/dynamic-tool-description.md).

# Dynamic Tool Description

**Severity**

🟡 Medium (6)

**Short Description**

Flags MCP servers where tool descriptions are loaded dynamically from remote URLs, runtime configuration, or external processes instead of being statically defined in source code. Since the LLM relies on tool descriptions to decide what to invoke, remotely controlled descriptions make behavior unpredictable.

**Suggestion**

This behavior may indicate malicious intent. Investigate whether the dynamic loading mechanism is legitimate, and consider pinning tool descriptions to static values or removing the MCP entirely.

**Information**

Dynamic tool descriptions occur when an MCP loads tool metadata - names, descriptions, or parameter definitions - from external sources such as remote URLs, environment variables, databases, or subprocess output rather than defining them statically in code. Because LLMs use tool descriptions to decide which tool to call and how to call it, an attacker who controls the external source can silently alter the description between runs to inject prompt-injection payloads, impersonate other tools, or redirect LLM actions — all without requiring a package update or code change.

**Risks**

* Silent Behavior Changes: A remote source can alter tool descriptions at any time, changing what the LLM believes a tool does without any visible update to the package.
* Prompt Injection via Descriptions: Dynamically loaded descriptions can embed hidden instructions that hijack the LLM's decision-making.
* Tool Impersonation: An attacker can modify a description to make one tool appear as another, tricking the LLM into routing sensitive data or actions to the wrong handler.
* Supply Chain Volatility: The MCP's behavior depends on external infrastructure, meaning a compromised CDN, API, or config server can weaponize the tool without touching its code.
* Evasion of Review: Static code review and marketplace scanning cannot catch payloads that are loaded dynamically at runtime.

**Recommended Actions**

**Investigate the Item:**

* Review the MCP source code for tool registration logic that fetches descriptions from URLs, files, environment variables, or subprocesses.
* Check whether the external source is under the publisher's control and served over authenticated HTTPS.
* Verify that descriptions cannot be modified between tool registration and invocation.

**Immediate Action:**

* Remove or disable MCPs that load descriptions from untrusted or unauthenticated external sources.
* Audit recent tool invocations for behavior inconsistent with the expected tool descriptions.

**Mitigation:**

* Require tool descriptions to be statically defined in source code and validated at build time.
* If dynamic loading is necessary, enforce integrity checks (e.g., checksums or signatures) on fetched descriptions.
* Monitor for changes in tool descriptions across successive MCP invocations.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/dynamic-tool-description.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
