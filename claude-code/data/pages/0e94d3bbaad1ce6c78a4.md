---
url: https://cortex-docs.paloaltonetworks.com/cortex-api-overview/readme.md
fetched_at: 2026-09-16T09:12:58Z
source: cortex-platform
---

# Cortex API Documentation

> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/cortex-api-overview/readme.md).

# Cortex API Documentation

Explore and integrate with the Cortex platform APIs

Welcome to the Cortex API documentation. This area is the central reference for APIs across the Cortex platform.

## API Reference By Product

Choose a Cortex product below to jump to its API reference.

<table data-view="cards"><thead><tr><th></th><th></th><th align="center"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><i class="fa-cloud">:cloud:</i> Cortex Cloud</h4></td><td>Cloud security posture, runtime protection, and workload security APIs. Covers CSPM, CWP, DSPM, CIEM, AppSec, compliance, and more.</td><td align="center"></td><td><a href="https://cortex-docs.paloaltonetworks.com/cortex-cloud-api/">Cortex Cloud APIs</a></td></tr><tr><td><h4><i class="fa-shield-halved">:shield-halved:</i> Cortex XDR</h4></td><td>Extended detection and response APIs for endpoint, network, and cloud data.</td><td align="center"><a href="https://cortex-docs.paloaltonetworks.com/xdr-5-api/" class="button primary small">XDR 5</a><br><a href="https://cortex-docs.paloaltonetworks.com/xdr-3-api/" class="button primary small">XDR 3</a></td><td><a href="https://cortex-docs.paloaltonetworks.com/xdr-5-api/">XDR 5.x APIs</a></td></tr><tr><td><h4><i class="fa-shield">:shield:</i> Cortex XSIAM</h4></td><td>Unified security operations APIs for ingestion, AI-driven threat prioritization, and automated response.</td><td align="center"></td><td><a href="https://cortex-docs.paloaltonetworks.com/xsiam-api/">XSIAM APIs</a></td></tr><tr><td><h4><i class="fa-diagram-project">:diagram-project:</i> Cortex XSOAR</h4></td><td>Security orchestration, automation, and response APIs for playbooks, integrations, and incident management.</td><td align="center"><a href="https://cortex-docs.paloaltonetworks.com/xsoar-8-api/" class="button primary small">XSOAR 8</a><br><a href="https://cortex-docs.paloaltonetworks.com/xsoar-6-api/" class="button primary small">XSOAR 6</a></td><td><a href="https://cortex-docs.paloaltonetworks.com/xsoar-8-api/">XSOAR 8.x APIs</a></td></tr><tr><td><h4><i class="fa-robot">:robot:</i> Cortex AgentiX</h4></td><td>APIs for AI security workflows, analyst automation, and guided actions.</td><td align="center"></td><td><a href="https://cortex-docs.paloaltonetworks.com/agentix-api/">AgentiX APIs</a></td></tr><tr><td><h4><i class="fa-globe">:globe:</i> Cortex Xpanse</h4></td><td>Attack surface management APIs for asset discovery, exposure identification, and attack-surface remediation.</td><td align="center"></td><td><a href="https://cortex-docs.paloaltonetworks.com/xpanse-api/">Xpanse APIs</a></td></tr></tbody></table>

Developers use the **Cortex APIs** to:

* **Automate incident and case management** - Retrieve, search, create, and update issues and cases, then push security findings into your SOAR, ticketing, or automation workflows.
* **Query your data with XQL** - Run Cortex Query Language (XQL) queries programmatically for threat hunting and analytics, and pull results into custom reports and dashboards.
* **Ingest and stream security data** - Ingest alerts, assets, and telemetry, and stream data to external destinations such as SIEMs, webhooks, and data lakes for centralized monitoring.
* **Manage cloud security posture** - Onboard cloud accounts and evaluate posture across CSPM, CWP, DSPM, and CIEM, including vulnerability management across cloud, endpoints, and code.
* **Embed security into CI/CD** - Manage applications, repositories, detection rules, and scans to shift application security (AppSec/ASPM) left into your development pipelines.
* **Administer identity and access** - Programmatically manage roles, user groups, users, API keys, and scope-based access control (SBAC) across the Cortex platform.

***

<h2 align="center">Join the Discussion</h2>

> Join the Palo Alto Networks Live Community to post questions, get help, and share resources with other Cortex developers.

<p align="center"><a href="https://live.paloaltonetworks.com/" class="button secondary">Join the community</a></p>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://cortex-docs.paloaltonetworks.com/cortex-api-overview/readme.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
