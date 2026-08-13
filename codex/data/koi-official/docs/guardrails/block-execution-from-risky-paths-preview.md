<!-- KOI source: https://docs.koi.ai/guardrails/block-execution-from-risky-paths-preview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/block-execution-from-risky-paths-preview.md).

# Block Execution from Risky Paths (Preview)

Block execution of binaries from high-risk, user-writable file system paths such as `/tmp`, `/var/tmp`, `$TMPDIR`, and `/Users/Shared/`.

### Why It Matters

* User-writable directories are commonly abused by malware droppers, drive-by downloads, and temporary payloads.
* Binaries executed from these locations are typically not part of standard day-to-day user workflows and may indicate suspicious or unintended activity.
* Blocking execution from these paths reduces exposure to untrusted or potentially unsafe content and strengthens endpoint hygiene.

### How It Works

* Blocks execution of binaries when the execution path begins with a predefined risky path.
* Enforcement is handled via Santa on macOS endpoints.
* An Impact Check can be run before enabling the guardrail to evaluate potential productivity impact.
* The Guardrail can be scoped to specific endpoint groups.
* The predefined path list can be edited by administrators:

<figure><img src="/files/XQOYkEtmBRqXfYbewqb7" alt=""><figcaption></figcaption></figure>

### Benefits

* **Stronger Endpoint Hardening**: Reduces execution from high-risk, user-writable directories.
* **Productivity-aware enforcement**: Validate impact before enforcement using Impact Check.
* **Granular Scoping**: Apply the guardrail to specific device groups.
* **Operational Flexibility**: Edit the predefined path list to match your organization’s needs.

#### Supported platform

<figure><img src="/files/QzoXTstSc3jWI2qRYCOY" alt=""><figcaption></figcaption></figure>

* macOS


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/block-execution-from-risky-paths-preview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
