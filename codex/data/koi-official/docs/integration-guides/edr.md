<!-- KOI source: https://docs.koi.ai/integration-guides/edr.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/edr.md).

# EDR

To ensure continuous protection and visibility across all endpoints, the Koi script package must run on a recurring schedule (recommended: once per hour).

* If your EDR supports scheduled script execution, upload the Koi script package through the EDR interface and configure it to run hourly on all endpoints.
* If your EDR does not support recurring execution, you should still upload the script via the EDR where possible, and use a SOAR platform or your existing automation workflows to ensure it runs regularly.

[CrowdStrike RTR Guide](/integration-guides/edr/crowdstrike-rtr-guide.md)

[SentinelOne Guide](/integration-guides/edr/sentinelone-guide.md)

[Microsoft Defender for Endpoint Guide](broken://pages/POCyS9YXKc20THBneaqQ)

[Palo Alto Cortex XDR](/integration-guides/edr/palo-alto-cortex-xdr.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/edr.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
