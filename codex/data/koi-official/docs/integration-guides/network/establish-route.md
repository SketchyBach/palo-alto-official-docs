<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route.md).

# Establish Route

- [Zscaler Guide](https://docs.koi.ai/integration-guides/network/establish-route/zscaler-guide.md): Easily integrate Koi with Zscaler ZIA using proxy chaining
- [Cisco Umbrella Guide](https://docs.koi.ai/integration-guides/network/establish-route/umbrella-guide.md): This guide explains how to integrate Koi with Cisco Umbrella SWG using the Bypass mode to direct marketplace traffic to Koi's proxy. Follow the steps below to ensure a smooth and secure configuration.
- [Fortinet FortiGate Guide](https://docs.koi.ai/integration-guides/network/establish-route/fortinet-fortigate-guide.md): Easily integrate Koi with FortiGate using supported moethods
- [Netskope Guide](https://docs.koi.ai/integration-guides/network/establish-route/netskope-guide.md): Easily integrate Koi with Netskope using supported methods
- [Prisma Access Guide](https://docs.koi.ai/integration-guides/network/establish-route/prisma-access-guide.md): Easily integrate Koi with Prsima Access using supported methods
- [Cloudflare Guide](https://docs.koi.ai/integration-guides/network/establish-route/cloudflare-guide.md): Easily integrate Koi with Cloudflare Zero Trust using a DNS override policy
- [BlueCoat Guide](https://docs.koi.ai/integration-guides/network/establish-route/bluecoat-guide.md): Easily integrate Koi with Blue Coat ProxySG using proxy chaining
- [PAC File Integration](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration.md): Route marketplace traffic to Koi using Proxy Auto-Configuration files
- [Deploy PAC File using Jamf Pro](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-using-jamf-pro.md): Easily deploy Koi PAC File using Jamf Pro
- [Deploy PAC File manually](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-manually.md): Manually configure PAC file for Mac and Windows.
- [Firewall Exclusions for PAC File](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/firewall-exclusions-for-pac-file.md): When a PAC file routes marketplace traffic to Koi from behind a firewall (for example Palo Alto, Prisma Access, or GlobalProtect), the firewall can block or filter the traffic the PAC file depends on.
- [GlobalProtect & Pac Guide](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/globalprotect-and-pac-guide.md): This guide explains how to route Koi marketplace traffic through a PAC file on endpoints running Palo Alto GlobalProtect.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
