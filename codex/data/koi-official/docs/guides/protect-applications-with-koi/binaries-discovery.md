<!-- KOI source: https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery.md).

# Binaries Discovery

Koi now integrates with Santa on macOS, giving you centralized visibility into binary execution across your organization. Every time a binary is launched on a macOS endpoint, the execution is logged in Koi with full context - including who executed it, on which device, path, the file’s SHA256 and more.\
\
To enable this capability, please contact the Customer Experience team to have the add-on enabled. Also, This capability requires configuring the Santa integration in your environment. Setup instructions and technical details can be found [here](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration).

## **Why does this matter?**

Modern threats often do not rely on traditional applications alone.\
Attackers frequently use small binaries, unsigned tools, or helper executables that bypass visibility when teams rely only on application inventory.

Without execution-level visibility, security and IT teams can’t confidently answer questions like:\
What binaries are actually running in the environment, which ones are governed by policy, and which binaries may pose a risk.

The Binaries Inventory complements the Application Inventory and serves as a foundational layer for effective application control. It enables teams to first **understand what is happening in their environment**, decide on an appropriate governance approach and policies, and then validate and refine enforcement over time, without manual investigation on each endpoint.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
