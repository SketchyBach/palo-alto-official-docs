<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/prisma-access-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/prisma-access-guide.md).

# Prisma Access Guide

## Prisma Access Guide

This guide explains how to integrate Koi with Prisma Access (Strata).

In most cases the integration is PAC-based: establish trust, add the required firewall exclusions, and deploy the Koi PAC file — marketplace traffic is then routed to Koi's proxy. PAC file deployment has two approaches:

* **Managed PAC** — If the environment uses GlobalProtect in **Tunnel + Proxy** or **Proxy** mode (Prisma Access Explicit Proxy), deploy the PAC via the Explicit Proxy forwarding profile.
* **External PAC Deployment** — If GlobalProtect is in **Tunnel-only** mode or Explicit Proxy is not used, deploy the PAC file separately.

***

### Prerequisites

Before starting the integration, ensure you have the following:

* **Access to Prisma Strata Admin Console** with Explicit Proxy policies enabled.
* **List of marketplace domains** provided by Koi.
* **Koi proxy IP/FQDN and port** provided by Koi.
* **Trusted Certificate Authority (CA) readiness** – You must have one of the following in place to establish trust between endpoints and Koi’s proxy:
  * **An Organizational Root CA** and the ability to use it to sign certificates when required during setup.
  * **The Koi Root CA**, provided by Koi for download and deployment to all managed endpoints.

***

### 1. Establish Trust

Trust establishment can be done via settings up Koi’s CA in the connecting devices. Another approach is available by signing a CSR by a root CA, that is already installed on your devices in the organization.

For more information, see: [Establishing Trust](/integration-guides/network/establishing-trust.md)

***

### 2. Add the Required Firewall Exclusions

Allow the PAC file URL, marketplace domains, and Koi proxy traffic through your firewall so PAC-based routing works.

For the full list, see [Firewall Exclusions for PAC File](/integration-guides/network/establish-route/pac-file-integration/firewall-exclusions-for-pac-file.md).

***

### 3. Deploy the PAC File

#### Option 1: Managed PAC Deployment via Explicit Proxy

If your organization already uses Explicit Proxy with Prisma Access:

1. Navigate to **Workflows → Prisma Access Setup → Explicit Proxy → Forwarding Profiles Setup**.
2. Click Add Forwarding Profile or edit the existing one.
3. **Upload or edit the PAC file** provided by Koi.
4. **Save** the changes.
5. Commit changed by clicking on **Push Config** at the top right side of the screen.

Validate your profile is included in the agent's app settings:

1. Navigate to **Workflows → Prisma Access Setup → GlobalProtect → GlobalProtect App**.
2. **Open the relevant App Settings profile** for your target OS/User group.
3. Under the profile's page, scroll down and click **Show Advances Options**, ensure the Agent Settings mode is set to Tunnel + Proxy or Proxy.
4. Under **Proxy → Forwarding Profiles**, select the forwarding profile you configured earlier.
5. If you have made any changes:
   1. **Save** the changes.
   2. Commit changed by clicking on **Push Config** at the top right side of the screen.

#### Option 2: External PAC Deployment

When Explicit Proxy is not used, deploy a PAC file separately so marketplace domains are routed directly to Koi’s proxy.

For more information, see [PAC File Integration](/integration-guides/network/establish-route/pac-file-integration.md) and [GlobalProtect & Pac Guide](/integration-guides/network/establish-route/pac-file-integration/globalprotect-and-pac-guide.md)

***

### Summary

This guide outlines how to integrate Koi with Prisma Access using a PAC file deployment so marketplace traffic is routed to Koi’s proxy.

* **Ensure trust** is established with Koi’s proxy.
* **Add firewall exclusions** for the PAC file URL, marketplace domains, and Koi proxy.
* **Deploy the PAC file** — Managed PAC via Explicit Proxy, or External PAC.

These steps provide a secure, reliable, and seamless connection between endpoints and Koi services.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/prisma-access-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
