<!-- KOI source: https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-governance.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-governance.md).

# MCP Servers - Governance

Koi provides organizations with comprehensive controls to manage, monitor, and secure all [**Model Context Protocol (MCP)**](https://modelcontextprotocol.io/introduction) servers across their environment. Whether MCP servers are configured manually or installed from the [MCP registry](https://github.com/mcp), Koi enables security teams to define policies, enforce compliance, and automate remediation - ensuring only approved servers are used without disrupting developer workflows.

Koi's MCP Governance capabilities give security administrators the tools to control which MCP servers can be used in the organization and how violations are handled. It helps:

* Define what MCP servers are allowed or blocked
* Enforce policies automatically across all endpoints
* Respond to policy violations with configurable remediation actions
* Maintain compliance without disrupting developer workflows

***

## Configuration Options

Access MCP governance through the **MCPs tile** in the Policies page under the marketplace configuration section.

Available controls:

* Switch between Default mode and Allowlist mode
* Configure global allow and block lists
* Create custom policies based on metadata and findings
* Enable automated remediation (Coming soon)

![](https://files.readme.io/8f1c30be245bc2c654721d4658b81e3c7265b02156be023e3d0f48c4c80a2382-image.png)

***

## Operating Modes

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

All MCP servers are blocked by default unless explicitly allowed.

**How it works:**

* Only MCP servers from the Github MCP Registry on the global allow list can be installed or used
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

Prevent specific MCP servers from the Github MCP Registry across your organization by adding them to the global block list.

**How to add servers:**

* By GitHub MCP registry ID
* By MCP server ID

Items matching the global block list will appear in the Remediation page for security teams to review and address.

### Global Allow List

In Allowlist mode, only allowed servers can be used, wether by global list or by Allow custom policy, can be used in your organization. Add approved servers to ensure teams can access the tools they need while maintaining security controls.

### Custom Policies

Organizations can leverage Koi's [Policy Library](https://docs.koi.ai/guides/index-1/policy-library) to create custom MCP governance policies tailored to their specific requirements, enabling granular control based on metadata, findings, and organizational needs.

![](https://files.readme.io/55378a0f781b01f01d083b476f1e68f0774a1788d8f4e97c0179d42860a8e7d6-image.png)

***

## MCP Registry Enforcement

Ensure the organization only uses MCP servers from official registries.

[**Guardrail: MCP Registry Enforcement**](https://docs.koi.ai/guardrails/mcp-registry-enforcement)

**What it does:** Removes MCP servers installed outside the official MCP registry to ensure only marketplace-approved servers are used

**Scope:** The guardrail applies only to platforms that support integration with the MCP registry

**Best for**: Organizations that want to enforce use of vetted, marketplace-approved MCP servers and prevent shadow IT installations.

***

## How to Handle MCP violating policies

Koi enables control over MCP servers whether they're installed manually or from the official GitHub MCP registry, with different enforcement approaches for each:

**Manual MCP configurations:**

* Manual MCPs are defined directly in configuration files
* Koi surfaces MCPs that violate your policies and provides options to remediate them by removing their instances from the configuration file
* Enforcement relies on **continuous remediation** - Koi scans configurations, identifies policy violations, and flags them for removal on the next script run

**MCP Registry installations:**

* Provides both **prevention** and remediation capabilities (for supported platforms like VS Code)
* Uses network-level controls to block unauthorized installations from the GitHub MCP registry
* Applies marketplace governance policies before installation occurs
* Existing violating installations are flagged for remediation

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
GET https://docs.koi.ai/guides/protect-ai-tools-with-koi/mcp-governance.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
