<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages.md).

# Code Packages

Koi integrates with package managers by configuring their registry settings to point to the **Koi proxy**. Instead of fetching packages directly from public registries (npmjs.org, PyPI), package managers are configured to route requests through Koi, which evaluates every request against your organization's policies.

### How it works

#### Route

Package managers are configured to use the Koi proxy URL as their registry. Package requests go through Koi rather than directly to public registries.

#### Trust

Koi serves TLS from a certificate signed by a globally recognized Root CA. No additional trust configuration is required.

#### Before you begin

Before configuring the Koi proxy, review how your developer environments are set up. Package manager configuration has multiple layers, and settings closer to the project or process level can silently override the global registry. See the "Before You Begin" section in each tool-specific guide for details.

If your organization uses a centralized artifact repository (e.g., JFrog Artifactory, Sonatype Nexus), consider configuring the Koi proxy as an upstream in that system instead of on each endpoint. See the Upstream Integration Guide for details.

### Supported Integrations

* NPM
* Python (pip)

For deploying registry configuration at scale, see Deploying Registry Configuration.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
