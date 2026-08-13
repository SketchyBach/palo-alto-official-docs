<!-- KOI source: https://docs.koi.ai/guardrails/scan-first-protection.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/scan-first-protection.md).

# Scan-First Protection

Prevent the installation of newly published non-binary software until our automated risk scan is complete, typically within minutes to a few hours of publication.

### Why It Matters

* Newly published non-binary software and can introduce unknown risks and vulnerabilities.
* Threat actors are actively targeting marketplaces by publishing malicious non-binary software.

### How It Works

* Scans new packages within minutes to a few hours of publication.
* Blocks potentially malicious non-binary software before they are installed.

> *Note*: Koi does not scan private or internally developed items that are not published in official marketplaces. If your organization uses custom-built or private extensions, you should add them to the global allow list to prevent them from being blocked by the Scan-First Protection guardrail. This ensures legitimate internal tools remain accessible while maintaining security oversight.

#### Supported Marketplaces

![](https://files.readme.io/9d55e85ea4c0c3f62299fc80910870dae70885e03e01837b20948c7ac60b645b-image.png)

* VSCode Marketplace
* JetBrains
* Chrome Web Store
* Edge Add-ons
* Firefox Add-ons
* Homebrew
* Office Add-ins
* Cursor
* Windsurf
* OpenVSX


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/scan-first-protection.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
