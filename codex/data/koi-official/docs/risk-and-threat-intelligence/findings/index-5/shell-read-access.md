<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/shell-read-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/shell-read-access.md).

# Shell Read Access

**Severity**

🟢 Low (0)

**Short Description**

Flags extensions that can read data from the system shell.

**Suggestion**

Ensure the extension’s shell read capabilities are necessary and do not expose sensitive system information.

**Information**

Shell read access allows extensions to execute shell commands and retrieve output, which could be exploited to collect system details or monitor processes.

**Risks of Shell Read Capability**

* **System Reconnaissance**: Extensions may gather system information for exploitation.
* **Process Monitoring**: Malicious extensions could track running processes.

**Recommended Actions**

1. **Validate Shell Read Access**:
   * Ensure the extension needs to execute and read shell output.
   * Confirm compliance with security guidelines.
2. **Enhance Controls**:
   * Restrict unnecessary shell access using ExtensionTotal policies.
   * Monitor shell activity for unauthorized commands.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/shell-read-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
