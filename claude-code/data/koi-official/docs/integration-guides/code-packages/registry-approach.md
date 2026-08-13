<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/registry-approach.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/registry-approach.md).

# Registry Approach

### Integration

With the registry approach, package managers are configured to use the Koi proxy as their registry. Package requests go through Koi, where they are evaluated against your organization's policies before being served.

Before applying the registry configuration, review the "Before You Begin" section in each tool-specific guide. Package manager configuration has multiple layers, and settings closer to the project or process level can silently override the global registry.

### Supported Integrations

* [Python](/integration-guides/code-packages/registry-approach/python.md)
* [NPM](/integration-guides/code-packages/registry-approach/npm.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/registry-approach.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
