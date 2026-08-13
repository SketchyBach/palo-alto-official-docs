<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/mcp-governance/claude-connectors-governance.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/mcp-governance/claude-connectors-governance.md).

# Claude Connectors - Governance

Koi supports policy-based prevention and governance of MCP servers installed from the **Claude Connectors** marketplace on Claude desktop app. Control which connectors can be installed on managed devices and block untrusted or risky connectors at install time - so risks are stopped before they enter and become active threats in your environment.

{% hint style="info" %}
**Naming:** Connectors were previously labeled **Claude Desktop Extensions** in Koi. They now appear as **Claude Connectors** (with the Claude icon) across the MCP inventory, query builder, policies, and settings.
{% endhint %}

***

## Supported Scope

Koi supports prevention of policy-violating connectors for **Desktop connectors** (Desktop Extensions - `.dxt` / `.mcpb`) installed from the Claude Connectors marketplace (`claude.com/connectors`), as long as the Koi Proxy is configured. See below for more information.

{% hint style="warning" %}
**Web connectors** (managed server-side by Claude, e.g. `gcal.mcp.claude.com/mcp`) and **custom connectors** created by your Claude org admins are not yet supported. See [Limitations](#limitations) below.
{% endhint %}

<figure><img src="/files/oHBWXZwbmhutty6w5bia" alt=""><figcaption></figcaption></figure>

***

## How it works

1. **Traffic routing** – Installation and update attempts to the Claude Connectors marketplace are routed through the Koi proxy on your organization's endpoints.
2. **Policy lookup** – For each connector install/update request, the proxy looks up the connector in your Governance rules (block list, allow list, guardrails, and policies).
3. **Allow or block** – The proxy allows or blocks the request accordingly.
4. **Blocked installs** – For a blocked connector, the **Install** and **Update** buttons in the Claude marketplace are replaced with a **Request Approval** button. The end user can submit a request, with optional justification.

***

## Setting up Claude Connectors prevention

You can block or allow connectors by defining policies scoped to the **Claude Connectors** item type and by using a global block list.

### **Before you start: Koi Proxy required**

To block unwanted connectors at install time, Claude Connectors prevention relies on a network proxy integration. Enforcement happens over the network at install and update time, so the proxy must be able to inspect traffic to the Claude marketplace.&#x20;

Koi inspects marketplace traffic through a two-step [network integration](/integration-guides/network.md) - Complete both steps for the Claude marketplace domains:

1. Contact Koi support to update the proxy certificate with the new domains.
2. **Establish trust** - *Koi Root CA:* no action needed, the new domains are covered automatically. *CSR:* re-issue a CSR including the new domains, have it signed, and upload it to Koi. See [Establishing Trust](https://claude.ai/epitaxy/local_0cb9bb66-5218-47a7-a916-823731defad7#) for more information.
3. **Establish route** - The Claude marketplace domains `claude.ai` and `api.anthropic.com` must be routed to Koi. If you already have a network integration, these domains need to be **added** to it:
   * **SASE / SWG** (e.g. Zscaler) - add the domains to your existing configuration. See [Establish Route](https://claude.ai/epitaxy/local_0cb9bb66-5218-47a7-a916-823731defad7#) and the [supported routing integrations](https://claude.ai/epitaxy/local_0cb9bb66-5218-47a7-a916-823731defad7#).
   * **Koi-managed PAC file** - the domains are added by Koi. Contact Koi support to have an updated PAC file generated with the new domains, then deploy it to your endpoints.

{% hint style="warning" %}
**If `claude.ai` or** `api.anthropic.com` **fails to load on an enrolled endpoint**, verify the PAC configuration and confirm the Koi Root CA is trusted (including in VPN clients such as GlobalProtect) before troubleshooting anything else.
{% endhint %}

**Capabilities:** Once Koi prevention is enabled via the network integration, you can apply enforcement rules to control which connectors may be installed and proactively block potentially risky or unwanted connectors before they reach your managed endpoints.

#### 1. Policies

* Create allow/block policies using full connector analysis data & findings (dependencies, OSV vulnerabilities, license, GitHub backlink, suspected-malicious).
* Alert-mode policies with end-user notifications.

#### 2. Guardrails

* **Version update cooldown** – delay before newly published connector versions become available for update (configurable). The **Update** button is replaced with **Request Approval** during the cooldown window.
* \[💎 **Coming soon] Delayed access** – delay before newly published connectors can be installed (configurable). The **Install** button will be replaced with **Request Approval** until the connector has been available for the configured period.

#### 3. Global allow/block lists

* Set the Claude Connectors marketplace to **allowlist** or **blocklist** mode.
* Globally allow or block specific connectors.
* Only MCP servers from supported marketplaces (the GitHub MCP Registry and Claude Connectors) on the global allow list can be installed or used
* New installations from the registry are blocked over network level (for supported platforms like VS Code)
* Existing manual installations that don't match the allowlist are flagged for remediation

### Risk visibility

Connectors in the MCP inventory are enriched with their metadata, declared tools, and version history, and scored with the same scanners Koi runs on other MCP sources — **dependency**, **OSV**, **license**, **GitHub backlink**, and **suspected-malicious**. Risk findings appear in the connector's details view and can be used as conditions in policies, so you can write block rules against accurate, enriched data rather than name alone.

### Remediation

Beyond blocking new installs, admins can **remove an already-installed connector** from one or more endpoints, directly from the UI or API — consistent with Koi's existing remediation flows (audit log, remediation page status, API status). Removal cleans up the connector on the endpoint and restarts Claude Desktop so the change takes effect immediately.

### Example: Blocked connector installation

When a connector is on the global block list or matches a block policy, users attempting to install it from the Claude marketplace see the **Install** button replaced with **Request Approval**. The user can submit a request with optional justification; admins approve or deny from the dashboard, and the user is notified.

<figure><img src="/files/BqrhyiL2mvcpEvZkYJoO" alt=""><figcaption></figcaption></figure>

***

## Limitations

* **Remote connectors are not yet governed.** Remote connectors are managed server-side by Claude and don't live on the endpoint filesystem, so they aren't covered by current endpoint discovery and prevention.
* **Custom connectors** created by your own Claude org admins are not yet covered.
* Sideloading detection for unofficial `.mcpb` / `.dxt` files installed outside the marketplace is not yet supported.&#x20;


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/mcp-governance/claude-connectors-governance.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
