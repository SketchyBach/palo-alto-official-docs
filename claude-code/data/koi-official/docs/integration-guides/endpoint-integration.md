<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration.md).

# Endpoint integration

#### Overview

Endpoint integration is how Koi reaches the devices in your organization. Once a device is connected, Koi can see the software and AI components running on it, assess their risk, and apply the policies and guardrails you set.&#x20;

It allows organizations to:

* Register devices to the Koi platform.
* Discover installed platforms and items.
* Remediate items that violate defined policies.

#### Before you start

* Access to the Koi portal, with permission to reach **Settings → Deployment**.
* Admin access to the MDM or EDR your organization uses to manage devices.
* A small group of test devices to start with. Deploy to that group first, confirm it works, then roll out to the rest.

→ Continue to [Deploy Koi to your endpoints](/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
