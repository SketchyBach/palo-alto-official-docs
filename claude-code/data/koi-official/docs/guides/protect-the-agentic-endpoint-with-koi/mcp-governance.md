<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/mcp-governance.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/mcp-governance.md).

# MCP Servers - Governance

Koi provides organizations with comprehensive controls to manage, monitor, and secure all [**Model Context Protocol (MCP)**](https://modelcontextprotocol.io/introduction) servers across their environment. Whether MCP servers are configured manually or installed from the [MCP registry](https://github.com/mcp), Koi enables security teams to define policies, enforce compliance, and automate remediation - ensuring only approved servers are used without disrupting developer workflows.

Koi governs MCP servers across multiple marketplaces, including the **GitHub MCP Registry** and the **Claude Connectors** marketplace built into the Claude desktop app, applying the same allow/block, approval, and remediation model to each.

Koi's MCP Governance capabilities give security administrators the tools to control which MCP servers can be used in the organization and how violations are handled. It helps:

* Define what MCP servers are allowed or blocked
* Enforce policies automatically across all endpoints
* Respond to policy violations with configurable remediation actions
* Maintain compliance without disrupting developer workflows

***

## Configuration Options - Marketplace mode

MCP marketplace mode is configured from the **Policies** page.&#x20;

* Each supported MCP marketplace appears as its own tile: **GitHub MCP Registry** and **Claude Connectors**.&#x20;
* On each tile you can switch that marketplace between Default mode and Allowlist mode (a per-marketplace "Block by default" switch) and configure its global allow/block lists.&#x20;
* Across marketplaces you can also create custom allow / block policies

<figure><img src="/files/zxVsm8R1q4xM0ZJK8LVG" alt=""><figcaption></figcaption></figure>

### Operating Modes

Each MCP marketplace has its own mode. The modes below describe how a marketplace behaves.

### Default Mode

All MCP servers are allowed by default unless explicitly blocked.

**How it works:**

Users can install MCP servers from registries or configure them manually. Blocked items are identified based on:

* **Global block list** - Specific servers from supported registries only, designated as prohibited across the organization
* **Custom block policies** - Rules based on metadata and findings (e.g., transport, Local/Remote, installation method)

**Remediation behavior:**

Items violating policies appear in the Remediation page for manual review and action by security administrators.

**Best for:** Organizations starting with MCP governance or teams that prefer visibility-first enforcement.

***

### Allowlist Mode

All MCP servers from that marketplace are blocked by default unless explicitly allowed.

**How it works:**

* Only MCP servers from supported marketplaces (the GitHub MCP Registry and Claude Connectors) on the global allow list can be installed or used
* New installations from the registry are blocked over network level (for supported platforms like VS Code)
* Existing manual installations that don't match the allowlist are flagged for remediation

**Remediation behavior:**

Items violating the allowlist appear in the Remediation page for manual review and action by security administrators.

**Example use case - Internal MCP gateway:**

Block all MCP servers except your organization's approved MCP gateway.

1. Add your gateway URL via allow custom policy
2. Enable Allowlist mode for the MCPs

Existing items violating the allowed custom policy list are flagged for remediation. New installations from the registry are blocked over the network.

**Best for:** Highly regulated environments or organizations with strict security requirements and mature MCP usage patterns.

***

## Global Lists

### Global Block List

Prevent specific MCP servers from the **Github MCP Registry** and **Claude connectors** marketplaces by adding them to that marketplace's block list.&#x20;

**How to add servers:**

* By GitHub MCP registry ID / Claude connector ID. Blocking an item blocks every variant published under it (e.g. both a local package and a remote endpoint).&#x20;
* By MCP server ID

Items matching the global block list will appear in the Remediation page for security teams to review and address.

### Global Allow List

In Allowlist mode, only allowed servers can be used, wether by global list or by Allow custom policy, can be used in your organization. Add approved servers to ensure teams can access the tools they need while maintaining security controls.

### Local MCP servers backed by npm or PyPI packages

A local MCP that runs from an npm or PyPI package is governed through that package ecosystem's own global list - not an MCP-specific list.&#x20;

{% hint style="info" %}
Adding the package to its global block list prevents it across all platforms. (npm/PyPI global lists are block lists only - no Allowlist mode.)
{% endhint %}

<figure><img src="/files/LmFC7ldGa7UQoKDm7fhR" alt=""><figcaption></figcaption></figure>

### Custom Policies

Organizations can leverage Koi's [Policy Library](https://docs.koi.ai/guides/index-1/policy-library) to create custom MCP governance policies tailored to their specific requirements, enabling granular control based on metadata, findings, and organizational needs.

An MCP policy scopes to MCP servers only. Beyond standard fields, MCP policies can match on:&#x20;

* **Type** (Local/Remote)
* **Transport** (stdio/http)

![](https://files.readme.io/55378a0f781b01f01d083b476f1e68f0774a1788d8f4e97c0179d42860a8e7d6-image.png)

***

## Request Approval

Instead of a hard block, admins can route blocked installs through an approval workflow. When a user attempts to install a blocked MCP server, Koi replaces the **Install** / **Update** button with **Request Approval**. The user submits a request with optional justification; the admin approves or denies it from the dashboard, and the user is notified of the outcome.

Request Approval is available for:

* **GitHub MCP Registry (VS Code)** - the Koi proxy intercepts the install action for blocked items and replaces it with a Request Approval prompt in the VS Code UI.
* **Claude Connectors** - Install and Update buttons in the Claude app marketplace are replaced with Request Approval for blocked connectors.

<figure><img src="/files/LkYoqyEBauQTnqWrdDin" alt="" width="563"><figcaption></figcaption></figure>

Each marketplace appears as a selectable **Scope** in the Request Approval form (configured under Settings → Advanced → Request Approval form).

***

## MCP Registry Enforcement

Ensure the organization only uses MCP servers from official registries.

[**Guardrail: MCP Registry Enforcement**](https://docs.koi.ai/guardrails/mcp-registry-enforcement)

**What it does:** Removes MCP servers installed outside the official MCP registry to ensure only marketplace-approved servers are used

**Scope:** The guardrail applies only to platforms that support integration with the MCP registry - currently applies to VS Code.

**Best for**: Organizations that want to enforce use of vetted, marketplace-approved MCP servers and prevent shadow IT installations.

***

## How to Handle MCP violating policies

Koi enables control over MCP servers whether they're installed manually or from the official GitHub MCP registry, with different enforcement approaches for each:

**Manual MCP configurations:**

* Manual MCPs are defined directly in configuration files
* Koi surfaces MCPs that violate your policies and provides options to remediate them by removing their instances from the configuration file
* Enforcement relies on **continuous remediation** - Koi scans configurations, identifies policy violations, and flags them for removal on the next script run

**Marketplace installations (GitHub MCP Registry & Claude Connectors):**

* Provides both prevention and remediation capabilities (for supported platforms — VS Code for the GitHub MCP Registry, the Claude app for Claude Connectors).
* Uses network-level controls to block unauthorized installs and applies marketplace governance policies before installation occurs.
* Blocked installs can be routed through **Request Approval** instead of a hard block.
* Existing violating installations are flagged for remediation. For Claude Connectors, remediation removes the local extension from the endpoint and restarts the Claude app to apply the change.

This dual approach provides comprehensive MCP governance across all installation methods while adapting to the unique characteristics of each.

***

## Key Benefits

* **Flexible enforcement** with Blocklist and Allowlist modes
* **Granular control** through global lists and custom policies
* **Safe removal** without disrupting developer productivity or breaking builds
* **Registry enforcement** to ensure only vetted, marketplace-approved servers are used


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/mcp-governance.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
