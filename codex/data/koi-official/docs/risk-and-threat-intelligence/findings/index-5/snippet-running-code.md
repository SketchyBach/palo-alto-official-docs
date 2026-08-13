<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/snippet-running-code.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/snippet-running-code.md).

# Snippet Running Code

**Severity**

🟠 Medium (4)

**Short Description**

Flags Snippet type extensions that run code on the user's machine.

**Suggestion**

Review the extension’s code and remove it if execution is unnecessary or harmful.

**Information**

Snippet extensions should be static JSON files and not execute any code. Snippet extensions that run code may be suspicious or introduce unnecessary risks.

**Risks of Snippet Running Code**

* **Unintended Behavior**: Code execution in snippet may introduce unwanted functionality.
* **System Exploitation**: Executing code can lead to privilege escalation or malicious actions.
* **Reduced Trust**: Snippet running code deviate from expected behavior, reducing user confidence.

**Recommended Actions**

1. **Investigate the Item**:
   * **Analyze Behavior**: Review the purpose of the code being executed and its necessity.
   * **Verify the Publisher**: Confirm the extension is from a trusted source.
   * **Evaluate Usage**: Assess the impact on systems and users.
2. **Immediate Action**:
   * **Remove the Extension**: If code execution is unnecessary or risky, remove the snippet.
   * **Notify Stakeholders**: Inform relevant users or teams about the risks and actions taken.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/snippet-running-code.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
