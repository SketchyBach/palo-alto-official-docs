<!-- KOI source: https://docs.koi.ai/product-security-and-legal/monitoring-controls-in-extensiontotal.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/product-security-and-legal/monitoring-controls-in-extensiontotal.md).

# Monitoring Controls in Koi

Koi provides various monitoring controls to help organizations enforce policies effectively while minimizing disruptions. These controls detect and alert about potential policy conflicts, unintended mass removals, overly permissive rules, unauthorized installations, and more. By leveraging these mechanisms, organizations can maintain security, consistency, and compliance without negatively impacting productivity.

### Destructive Policy Monitoring

One of the key monitoring mechanisms is destructive policy monitoring. This feature detects policies that could result in the mass removal of extensions and generates alerts when a policy removes a significant percentage of extensions (>10%). It provides an option to review and revert unintended removals before execution, ensuring no disruption to business operations.

### Over-Allowing Policy Monitoring

We also monitor for policies that are overly permissive. If an allowlist is too broad, it may introduce security risks by permitting extensions that should be restricted. We receive alerts when such policies are detected, along with suggestions to refine the policy and maintain a secure environment.

### Widely Used Extension Monitoring

Monitoring widely used extensions ensures that policies do not inadvertently impact essential tools installed on many devices. If an extension is detected across a significant number of devices, we receive alerts before any restrictive policy is enforced. This helps prevent unintended disruptions to workflows and ensures that critical extensions remain available when needed.

### Recurring Side-Loading Attempt Monitoring

Another critical control is the monitoring of recurring side-loading attempts. This detects repeated efforts to install extensions outside of policy guidelines, flagging any unauthorized or potentially risky behavior. If certain users or groups frequently attempt to bypass security measures, we are notified so you can take appropriate action.

### Policy Deployment Simulation

To ensure consistency across different environments, Koi detects inconsistencies in policy deployment. If policies vary between testing, staging, and production environments, alerts are generated to prevent unintended behavior. This helps maintain a predictable and secure implementation across all systems.

### Impact Analysis & Rollback Options

Before deploying policy changes, Koi provides impact analysis and rollback options. Real-time reports help understand the potential consequences of changes, and rollback options are available in case an adjustment leads to unintended disruptions. Every change is logged for audit and compliance tracking, ensuring accountability and traceability.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/product-security-and-legal/monitoring-controls-in-extensiontotal.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
