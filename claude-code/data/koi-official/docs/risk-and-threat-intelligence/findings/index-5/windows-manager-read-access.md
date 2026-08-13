<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/windows-manager-read-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/windows-manager-read-access.md).

# Windows Manager Read Access

**Severity**

🟢 Low (0)

**Short Description**

Flags extensions that can read window management data.

**Suggestion**

Ensure the extension’s window management read capabilities are necessary and do not compromise user privacy.

**Information**

Windows Manager read access allows extensions to track open windows and running applications, which could be exploited for user activity monitoring.

**Risks of Windows Manager Read Capability**

* **User Behavior Tracking**: Extensions could track user activity across apps.
* **Data Leakage**: Malicious extensions may extract application data.

**Recommended Actions**

1. **Validate Windows Manager Read Access**:
   * Confirm the extension needs window management data for a valid purpose.
   * Ensure compliance with privacy regulations.
2. **Enhance Controls**:
   * Restrict access to window management APIs.
   * Monitor extensions for unauthorized application tracking.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/windows-manager-read-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
