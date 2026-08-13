<!-- KOI source: https://docs.koi.ai/integration-guides/deployment-notes.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/deployment-notes.md).

# Deployment Notes

* Koi modifies managed preferences and policies on local endpoints (e.g; Chrome managed preferences, Windows registry, Mac configuration profiles). If another tool is also managing the same settings (e.g; MDMs like JAMF, Intune, Chrome Enterprise, GPOs, custom scripts) - they could be reset, overwritten, or ignored, leading to unpredictable enforcement and troubleshooting complexity.
* Koi provides APIs for integration, but out-of-the-box integrations may not exist for every tool or workflow. If you are thinking of integrating between Koi and your existing MDMs or automation tools (e.g., ServiceNow, Torque), Koi can be configured to only certain remediation actions (e.g., delete extension, network block, but not modify local policy) to avoid conflicts.
* Cloud-managed policies often take precedence over local changes, which can render Koi’s local modifications ineffective or cause confusion. It is recommended to verify that no dualities in enforcement exists between cloud and local policies.&#x20;
* Routing the endpoint script through a proxy requires the proxy's host port and IP. Please send it to your AES representative so the script could be configured using the proxy's details.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/deployment-notes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
