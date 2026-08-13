<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-2/repo-doesnt-exist.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-2/repo-doesnt-exist.md).

# Repo Doesn’t Exist

**Severity**

🟠 Medium (4)

**Short Description**

Flags extensions that have claimed to be open-source but the repository does not exist.

**Suggestion**

Review the extension’s necessity and remove it if it is no longer maintained or trusted.

**Information**

An unavailable repository indicates that the extension is no longer actively supported. This increases the risk of using outdated or potentially vulnerable code.

**Risks of Repo Doesn’t Exist**

* **Lack of Updates**: The extension will not receive patches or improvements.
* **Trust Issues**: The absence of a repository undermines the credibility of the extension.
* **Increased Exploitation Risk**: Vulnerabilities in the extension may go unpatched, making it a target for attackers.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Usage**: Assess whether the extension is essential.
   * **Check Alternatives**: Identify actively maintained extensions with similar functionality.
2. **Immediate Action**:
   * **Remove the Extension**: If the repository is unavailable, consider removing the extension.
   * **Notify Stakeholders**: Inform teams about the risks and actions taken.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-2/repo-doesnt-exist.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
