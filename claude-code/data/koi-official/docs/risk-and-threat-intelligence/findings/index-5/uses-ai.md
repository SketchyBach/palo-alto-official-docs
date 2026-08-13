<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/uses-ai.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/uses-ai.md).

# Uses AI

**Severity**

🟠 Medium (4)

**Short Description**

Flags extensions that process data using third-party AI models.

**Suggestion**

Evaluate the AI usage and ensure it aligns with your organization’s security policies and requirements.

**Information**

AI models can be used to process data in a way that may not be transparent to the user. This can lead to organization policy violation, data leakage, privacy concerns and potential misuse of data.

**Risks of Uses AI**

* **Data Privacy**: AI-based extensions may require sensitive data to function, increasing exposure risks.
* **Unintended Behavior**: The AI model may generate unpredictable outputs or actions.
* **Dependency on External Services**: AI-powered extensions often rely on third-party APIs, which could introduce vulnerabilities.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review AI Usage**: Understand how the extension uses AI and what data it processes.
   * **Verify the Publisher**: Ensure the publisher’s practices align with security and privacy standards.
2. **Immediate Action**:
   * **Limit Sensitive Data**: Avoid using the extension with sensitive information if possible.
   * **Monitor Behavior**: Regularly review the extension’s outputs and interactions.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/uses-ai.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
