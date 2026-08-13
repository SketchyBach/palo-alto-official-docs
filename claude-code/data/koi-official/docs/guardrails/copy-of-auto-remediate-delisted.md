<!-- KOI source: https://docs.koi.ai/guardrails/copy-of-auto-remediate-delisted.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/copy-of-auto-remediate-delisted.md).

# Delisted monitoring

Detect and surface items that have been removed or delisted from public marketplaces for review. Security teams can evaluate and remediate as needed, maintaining control while minimizing disruption to end users.

## Why It Matters

* Many extensions and packages are delisted after being flagged for policy violations or confirmed malicious behavior.
* On platforms like browsers, removed marketplace items often remain installed indefinitely, posing a silent and persistent threat.
* Keeping delisted items allows outdated or dangerous software to linger unnoticed in your environment.
* This guardrail ensures you have visibility into delisted items in your inventory, enabling informed decisions about their removal in line with your organization's security posture.

## How It Works

* Detects extensions and packages that are no longer available in their original marketplaces, based on continuous discovery.
* Surfaces delisted items for visibility and controlled remediation, allowing you to make informed decisions about removal.
* Presents delisted items under the **Open** tab in the remediation page for controlled remediation workflows.
* Continuously syncs with marketplace data to identify newly delisted items, including those removed for policy violations or malicious behavior.
* Offers remediation options so you can address delisted items according to your organization's policies and timeline.

### Supported Marketplaces

![](https://files.readme.io/01f8858174d6c4ef531e942fb8f766e7b599b3811c96ea81367b4c6fb678a0d8-image.png)

* VSCode Marketplace
* Chrome Web Store
* Cursor
* Windsurf
* OpenVSX
* Edge Add-ons


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/copy-of-auto-remediate-delisted.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
