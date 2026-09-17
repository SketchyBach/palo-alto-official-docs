---
url: https://cortex-docs.paloaltonetworks.com/microsoft-azure-manual-onboarding/azure-manual-onboarding-guide.md
fetched_at: 2026-09-16T09:13:10Z
source: cortex-platform
---

# Azure Manual Onboarding Guide

> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/microsoft-azure-manual-onboarding/azure-manual-onboarding-guide.md).

# Azure Manual Onboarding Guide

Manual onboarding is designed for customers who require full control over the Azure onboarding process. Instead of relying on Cortex-generated ARM (Bicep) templates, you provision every resource, including custom role definitions, role assignments, Event Hub, and the subscription diagnostic setting, yourself.

This guide has two sections:

* [Subscription scope](/microsoft-azure-manual-onboarding/azure-manual-onboarding-guide/azure-manual-onboarding-subscription-scope.md)
* [Management group or tenant scope](/microsoft-azure-manual-onboarding/azure-manual-onboarding-guide/azure-manual-onboarding-management-group-or-tenant-scope.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://cortex-docs.paloaltonetworks.com/microsoft-azure-manual-onboarding/azure-manual-onboarding-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
