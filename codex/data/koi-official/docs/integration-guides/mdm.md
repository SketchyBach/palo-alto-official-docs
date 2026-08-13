<!-- KOI source: https://docs.koi.ai/integration-guides/mdm.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm.md).

# MDM

- [Jamf Guide](https://docs.koi.ai/integration-guides/mdm/jamf-guide.md): This document provides step-by-step instructions on integrating Koi into your environment with Jamf.
- [Intune Guide](https://docs.koi.ai/integration-guides/mdm/intune-guide.md): Learn how to configure Koi into your environment with Microsoft Intune
- [Intune - Deploy certificate](https://docs.koi.ai/integration-guides/mdm/intune-guide/deploy-certificate.md): This document provides step-by-step instructions on deploying a \*\*Koi certificate\*\* using InTune.
- [Kandji Guide](https://docs.koi.ai/integration-guides/mdm/kandji-guide.md)
- [SCCM Guide](https://docs.koi.ai/integration-guides/mdm/sccm-guide.md): Learn how to configure Koi into your environment with SCCM
- [Salt Guide](https://docs.koi.ai/integration-guides/mdm/salt.md): Learn how to configure Koi into your environment with Salt
- [Workspace ONE Guide](https://docs.koi.ai/integration-guides/mdm/workspace-one-guide.md): Learn how to configure Koi into your environment with Workspace ONE UEM.
- [Hexnode Guide](https://docs.koi.ai/integration-guides/mdm/hexnode-guide.md): This document provides step-by-step instructions on integrating Koi into your environment with Hexnode.
- [FleetDM Guide](https://docs.koi.ai/integration-guides/mdm/fleetdm-guide.md): This document provides step-by-step instructions on integrating Koi into your environment with FleetDM.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
