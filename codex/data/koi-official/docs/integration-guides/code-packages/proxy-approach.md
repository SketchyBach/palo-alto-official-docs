<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/proxy-approach.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/proxy-approach.md).

# Proxy Approach

### Integration

Proxy approach forces code packages to pass through a proxy. This is either done implicitly - an already deployed solution the capture the traffic, or by explicitly configuring a proxy to pass through.

The covered guides define how to explicitly configure a proxy and how to establish trust with it.

**Remember** - the type of integration is important to know, as it dictates which steps are required to complete the integration.

### Supported Code Packages

* [Python](/integration-guides/code-packages/proxy-approach/python.md)
* [NPM](/integration-guides/code-packages/proxy-approach/npm.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/proxy-approach.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
