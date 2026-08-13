<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-poisoning.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-poisoning.md).

# Tool Poisoning

**Severity**

🔴 High (7)

**Short Description**\
Flags MCPs where tool definitions or behavior can be altered in ways that mislead an LLM. Such manipulation could result in unintended tool invocation, incorrect trust in tool outputs, or execution of unsafe actions across the agent’s available capabilities.

**Suggestion**

This behavior may indicate malicious intent. Strongly consider removing the MCP and reviewing any actions it may have already performed on the endpoint.

**Information**

Tool poisoning occurs when an MCP manipulates tool metadata - such as names, descriptions, or parameter definitions - to deceive the LLM into misusing tools. Poisoning alters tool definitions or introduces misleading information that corrupts the LLM's understanding of what a tool does. This can cause the model to invoke tools inappropriately, trust malicious outputs, or perform dangerous actions while believing it is operating correctly.

**Risks of Vulnerable to Prompt Injection**

* **Misleading Tool Behavior**: Altered descriptions cause the LLM to misunderstand tool functionality and use it incorrectly.
* **Unintended Invocation**: Poisoned metadata tricks the LLM into calling tools in inappropriate or dangerous contexts.
* **Corrupted Trust**: The LLM trusts outputs from poisoned tools, acting on false or malicious information.
* **Cross-Tool Exploitation**: Poisoned tools can influence the LLM's use of other legitimate tools in the environment.
* **Stealth Attacks**: Poisoning can be subtle, making malicious behavior difficult to detect during normal operation.

**Recommended Actions**

* **Investigate the Item**:
  * Review tool definitions for inconsistencies between descriptions and actual behavior.
  * Check whether tool metadata can be dynamically modified at runtime.
  * Verify tool definitions against trusted sources or documentation.
* **Immediate Action**:
  * Remove or disable MCPs with suspicious or inconsistent tool definitions.
  * Audit recent tool invocations for unexpected behavior or parameters.
* **Mitigation**:
  * Enforce immutable tool definitions that cannot be altered after registration.
  * Implement integrity checks to validate tool metadata against known-good configurations.
  * Monitor for changes to tool descriptions or parameters over time.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-poisoning.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
