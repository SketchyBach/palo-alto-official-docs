<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/llm-derived-code-execution.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/llm-derived-code-execution.md).

# LLM Derived Code Execution

**Severity**

🟡 Medium (6)

**Short Description**

Flags MCP servers whose tool handlers execute shell commands or code where the executed payload can be derived from LLM output, tool parameters, or other untrusted external input. That creates a path where prompt injection or manipulated context can become arbitrary execution on the host, not merely bad model text.

**Suggestion**

This behavior is high impact by design: any path from model- or user-influenced data into `exec` / `spawn` / `eval` / equivalent must be assumed exploitable. Review whether such execution is strictly necessary; if it is, constrain it aggressively or remove the MCP.

**Information**

LLM-derived code execution occurs when a tool handler takes values that may come from the LLM (e.g. tool arguments built from model output, chained tool results, or injected instructions) and passes them into system command execution, script evaluation, or dynamic code loading without strong guarantees that the payload is fixed and trusted. Because LLM outputs are not a security boundary - they can be steered by prompt injection, poisoned tools, or adversarial content - any tool that runs commands or code based on those values creates a direct path from context manipulation to code execution with the same privileges as the MCP server process.

**Risks**

* Arbitrary code execution: Injected content can cause the model to supply malicious commands or code fragments that the tool then runs on the host.
* Privilege and access: Execution runs as the MCP process, often with broad filesystem, shell, or network reach.
* Data impact: Injected operations can destroy or alter data, configs, or application state.
* Persistence and lateral movement: Attackers may install persistence, exfiltrate secrets, or pivot using shell or script primitives.
* Chain attacks: Combines cleanly with other MCP tools or credentials available to the same process.

**Recommended Actions**

* Map data flow from every tool parameter to command/code construction; assume any LLM-influenced field is attacker-controlled.
* Prefer eliminating dynamic execution; use fixed, reviewed operations with no string-to-shell or string-to-eval paths.
* If execution is unavoidable: strict allow-lists of commands and arguments, no shell where possible, sandbox the server, minimal privileges, and independent validation (not “the model said it’s OK”).
* Remove or disable MCPs that pass unsanitized model- or user-derived strings into execution APIs.
* Audit host logs for unexpected processes or commands tied to MCP activity.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/llm-derived-code-execution.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
