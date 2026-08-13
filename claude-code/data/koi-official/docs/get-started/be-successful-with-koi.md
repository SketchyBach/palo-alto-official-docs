<!-- KOI source: https://docs.koi.ai/get-started/be-successful-with-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/get-started/be-successful-with-koi.md).

# Be Successful with Koi

### Koi in a nutshell

Koi's endpoint security platform provides comprehensive security capabilities for securing any software install both non-binary and binary software, allowing your teams to fly free. With Koi you can govern all software, code packages, MCPs, extensions, AI models, AI agents, securing everything before it reaches your endpoints.

### Learn how it works

Explore the sections below to learn more about Koi's capabilities and how to implement them in your organization. Whether you're just starting or looking to optimize your usage, you'll find valuable information to enhance your extension’s security and posture.

#### [🚨 Risk and Threat Intelligence](/risk-and-threat-intelligence/wings-kois-risk-engine.md)

Learn about the risk scoring, findings, and attributes of non-binary software.

#### [🛡️ Guardrails](/guardrails/overview.md)

Learn how to get started with Guardrails and the available single click protections.

#### [🔧 Integration Guide](/integration-guides/integration-overview.md)

Learn how Koi integrates with your IT and security stack to provide discovery, governance, and remediation capabilities.

#### [ Governance](/guides/governance-best-practices.md)

Learn about governance and policies for your agentic software stack.

#### [🔒 Product Security](/product-security-and-legal/product-security-overview.md)

Understand how Koi handles data and security.

#### [📖 Guides](/guides/governance-best-practices.md)

Step by step guides to help you get started with Koi to best protect your agentic endpoints.

#### [🔍 Findings](/risk-and-threat-intelligence/findings.md)

Learn about security findings, their impact, and what to do about them.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/get-started/be-successful-with-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
