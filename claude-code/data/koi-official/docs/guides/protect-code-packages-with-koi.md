<!-- KOI source: https://docs.koi.ai/guides/protect-code-packages-with-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-code-packages-with-koi.md).

# Protect code packages with Koi

### The Problem

Code packages are a growing attack surface. Developers routinely pull hundreds of dependencies directly onto their endpoints, yet most organizations have no visibility into the risks they introduce to the endpoints themselves - including malware.

Without visibility into what packages exist across your organization and a way to enforce security standards, you're flying blind.

### How Koi Helps

Koi's Code Package Protection gives security teams the tools to **discover**, **prevent**, and **remediate** supply chain risks across your organization.

* [**Discovery**](/guides/protect-code-packages-with-koi/code-packages-discovery.md)**:** Get a single view of your package inventory across all endpoints alongside the risk of each package.
* [**Governance**](/guides/protect-code-packages-with-koi/code-package-prevention.md)**:** Set your security policies and prevent developers from pulling code packages that violate them.
* [**Remediation**](/guides/protect-code-packages-with-koi/code-packages-remediation.md) **(coming soon):** Remediate malicious packages before they cause damage.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-code-packages-with-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
