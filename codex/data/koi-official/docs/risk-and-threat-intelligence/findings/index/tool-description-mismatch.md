<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-description-mismatch.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-description-mismatch.md).

# Tool Description Mismatch

**Severity**

🔴 High (8)

**Short Description**

Flags MCP servers where a tools declared description, README documentation, or actual code behavior diverge. Mismatches can mislead an LLM about what a tool actually does, potentially causing unintended actions.

**Suggestion**

This behavior may indicate malicious intent or a serious quality issue. The gap between descriptions and between descriptions and code is a strong indicator of deceptive or unreliable behavior. Strongly consider removing the MCP and auditing any actions it has already performed.

**Information**

Tool description mismatch covers two distinct but related problems:

1\. User-facing vs Agent-facing Description Gap The user reviews the tool's description in its README, documentation, or marketplace listing and forms an understanding of what the tool does. Meanwhile, the LLM receives a different description through the `get_tools` API — one that may contain hidden instructions, additional capabilities, or prompt injection payloads. Because the user approves the tool based on one description but the LLM acts on a completely different one, this gap enables attacks that bypass human oversight entirely.

2\. Description vs Code Behavior Gap The tool's description (whether user-facing, agent-facing, or both) claims the tool performs a specific action, but the actual code does something different or additional. For example, a tool described as "search files" may also silently exfiltrate file contents, a tool described as "format code" may inject backdoors, or a tool described as "read config" may also write to it. This gap means neither the user nor the LLM has an accurate understanding of what the tool actually does when invoked.

Both gaps can be exploited independently or combined — a tool can present a safe description to the user, inject malicious instructions into the agent-facing description, and have code that behaves differently from either.

**Risks**

* Human Oversight Bypass: Users approve tools based on safe-looking documentation, unaware that the LLM receives different instructions or that the code does something else entirely.
* Hidden Prompt Injection: The agent-facing description can contain embedded instructions that override the LLM's behavior or redirect its actions.
* Undisclosed Capabilities: The code may perform actions (network calls, file writes, command execution) not mentioned in any description, making them invisible to review.
* Data Exfiltration: Mismatched descriptions or hidden code paths can send sensitive context, conversation data, or file contents to attacker-controlled endpoints.
* Stealth Command Execution: The agent-facing description or hidden code can cause the LLM to invoke system commands or chain tool calls that the user never authorized.
* False Sense of Security: Both users and LLMs trust descriptions to reflect reality — when they don't, all safety reasoning built on those descriptions becomes unreliable.

**Recommended Actions**

**Investigate the Item:**

* Compare the tool descriptions returned by `get_tools` against the MCP's README, marketplace listing, and documentation.
* Compare both descriptions against the tool's actual code — check whether the code performs actions not mentioned in any description (e.g., network requests, file writes, subprocess calls, data collection).
* Look for hidden instructions, encoded payloads, or excessive text in the agent-facing description that does not appear in user-facing materials.
* Check whether the description changes between invocations (may indicate dynamic injection).

**Immediate Action:**

* Remove or disable MCPs with confirmed description mismatches — whether between user/agent descriptions or between descriptions and code.
* Audit recent LLM interactions for actions that do not align with the tool's documented behavior.
* Review any data accessed or commands executed through the mismatched tool.

**Mitigation:**

* Enforce description consistency between user-facing documentation, agent-facing tool definitions, and actual code behavior.
* Implement automated comparison between published descriptions, runtime tool metadata, and static code analysis of tool handlers.
* Flag tools where the agent-facing description exceeds a reasonable length or contains patterns associated with prompt injection.
* Flag tools where code analysis reveals capabilities (network, filesystem, subprocess) not reflected in any description.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/tool-description-mismatch.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
