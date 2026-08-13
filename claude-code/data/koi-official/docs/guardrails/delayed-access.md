<!-- KOI source: https://docs.koi.ai/guardrails/delayed-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/delayed-access.md).

# Delayed Access

### What is delayed access in Koi?

Delayed access prevents the installation of newly published items for a configurable number of days after publication. This window allows time for public scrutiny and reputation signals to accumulate.\
• Items become installable only after the configured delay period. • Ideal for non-critical workflows where immediate access isn’t required.

### Why it matters

Delaying access mitigates the risk of zero-day supply chain attacks. This delay allows items to establish reputation and undergo public scrutiny before being deployed in your environment.

Use it to block premature adoption of unverified items across your environment.

![](/files/PwlNkNQwb4XMmXSDtvhu)

#### Supported Marketplaces

* VSCode Marketplace
* JetBrains
* Chrome Web Store
* Edge Add-ons
* Firefox Add-ons
* Homebrew
* Office Add-ins
* OpenVSX
* npm&#x20;
* PyPI


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/delayed-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
