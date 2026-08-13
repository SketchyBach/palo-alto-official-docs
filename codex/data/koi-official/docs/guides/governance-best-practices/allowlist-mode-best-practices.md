<!-- KOI source: https://docs.koi.ai/guides/governance-best-practices/allowlist-mode-best-practices.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/governance-best-practices/allowlist-mode-best-practices.md).

# Allowlist mode best practices

Allowlist mode is designed for strict environments where everything is blocked by default unless explicitly approved. It is ideal for organizations prioritizing maximum control and precision. Blocklist mode is Koi’s default governance posture.

Here's how to get the most out of allowlist mode:

### 1. Turn on guardrails

Guardrails provide out-of-the-box protections to automatically allow low-risk items. These include:

* **Scan-first protection**\
  Prevent installation of newly published packages or extensions until they pass Koi risk scanning.
* **Malware protection**\
  Automatically block items detected as malicious by threat intelligence and advanced scanning.
* **Delayed access (30 days)**\
  Block access to items until they have aged and stabilized in the marketplace.
* **Version update cooldown (2 days)**\
  Delay updates to avoid installing risky new versions immediately.
* **Sideloading visibility**\
  Identify items that bypass official marketplaces.

These guardrails provide broad coverage across risk types and marketplaces, and are recommended as your baseline.

### 2. Use the global allow list

Maintain a curated set of trusted, always-approved items:

* Previously approved items
* Widely adopted and low-risk (e.g., >20% install base)
* Regulated categories (e.g., only allow known-safe VPNs or screen capture tools)
* IDE toolchain defaults and official ecosystem items

### 3. Define allow policies

Use the policy builder to automatically approve items that meet advanced criteria such as:

* First-party publisher
* Verified publisher + high install base
* Low risk score with no critical findings

Koi exposes rich attributes: marketplace, risk score, permissions, GitHub metadata, CVSS, vulnerabilities, and more.

### 4. Support for approval requests

If items don’t match any policy, end-users can request approval directly from their web browser, IDE, CLI, or marketplace interface. These requests can be routed via API into:

* Jira
* ServiceNow
* Slack
* Any internal workflow system

This layered approach enables strong control while keeping end users productive.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/governance-best-practices/allowlist-mode-best-practices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
