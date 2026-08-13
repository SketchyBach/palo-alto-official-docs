<!-- KOI source: https://docs.koi.ai/integration-guides/integration-overview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/integration-overview.md).

# Overview

![](https://files.readme.io/92123209e999aa2c300cd9db043df2b0aa5135c2d10ba9f78c394b2704d28074-image.png)

Koi integrates with two core components: an endpoint piece, delivered as a script package (typically deployed via MDM or EDR), and a network integration. Both components are designed to work together to provide full visibility and control. However, Koi can operate effectively with either one independently, allowing organizations to start with what’s most accessible and expand later. For maximum visibility and control, both should be deployed together.

| Capability                  | Script package              | Network integration | Both |
| --------------------------- | --------------------------- | ------------------- | ---- |
| Marketplace items discovery | ✅                           | ✅                   | ✅    |
| Marketplace items inventory | ✅                           | ✅                   | ✅    |
| Endpoints inventory         | ✅                           |                     | ✅    |
| Insights dashboard          | ✅                           | ✅                   | ✅    |
| Risk assessments            | ✅                           | ✅                   | ✅    |
| Item risk report            | ✅                           | ✅                   | ✅    |
| Manual remediation          | ✅                           |                     |      |
| Guardrails                  | Detection / Remediation     | Prevention          | ✅    |
| Policies                    | Alert / Alert and Remediate | Allow/Block         | ✅    |
| Device group-based policies | ✅                           | ✅                   | ✅    |
| Audit log                   | ✅                           | ✅                   | ✅    |
| API                         | ✅                           | ✅                   | ✅    |
| Koidex                      | ✅                           | ✅                   | ✅    |
| Provision                   | ✅                           |                     |      |
| Commands                    | ✅                           |                     |      |
| Prevention search filtering | ✅                           | ✅                   | ✅    |
| Publish (VSCode)            | ✅                           | ✅                   | ✅    |
| Version Pinning             | Platform based              | Platform based      | ✅    |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/integration-overview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
