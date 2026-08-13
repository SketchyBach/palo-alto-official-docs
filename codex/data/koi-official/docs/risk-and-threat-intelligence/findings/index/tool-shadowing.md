<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-shadowing.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-shadowing.md).

# Tool Shadowing

**Severity**

🔴 High (7)

**Short Description**\
Flags MCPs where tools can be redefined, duplicated, or masked in ways that cause an LLM to invoke an unintended or misleading tool implementation. This can undermine tool selection integrity and could result in unsafe actions being executed under the appearance of a trusted capability.

**Suggestion**

This behavior may indicate malicious intent. Strongly consider removing the MCP and reviewing any actions it may have already performed on the endpoint.

**Information**

Tool shadowing occurs when a malicious or misconfigured MCP introduces tools that duplicate, override, or mimic legitimate tool names and descriptions. When an LLM selects tools based on names or descriptions, it may unknowingly invoke a shadowed implementation instead of the intended one. This attack exploits the trust relationship between the LLM and its available tools, causing the model to execute malicious logic while believing it is using a legitimate capability.

**Risks of Vulnerable to Prompt Injection**

* **Malicious Tool Execution**: The LLM invokes an attacker-controlled tool disguised as a trusted capability.
* **Data Interception**: Shadowed tools can capture sensitive parameters intended for legitimate tools.
* **Action Hijacking**: Critical operations like file writes or API calls can be redirected to malicious implementations.
* **Trust Exploitation**: Users and the LLM trust tool outputs that actually originate from compromised implementations.
* **Privilege Abuse**: Shadowed tools may perform unauthorized actions using permissions granted to legitimate tools.

**Recommended Actions**

* **Investigate the Item**:
  * Review all registered tools and check for duplicate or similar names.
  * Examine tool registration order and resolution logic.
  * Verify tool sources and whether external MCPs can override built-in tools.
* **Immediate Action**:
  * Remove or disable MCPs that allow unrestricted tool registration.
  * Revoke permissions for tools with suspicious or duplicate definitions.
* **Mitigation**:
  * Enforce tool registration validation and integrity checks.
  * Log all tool invocations and flag unexpected tool resolution patterns.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-shadowing.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
