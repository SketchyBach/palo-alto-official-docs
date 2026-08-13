<!-- KOI source: https://docs.koi.ai/integration-guides/network.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network.md).

# Network

Koi integrates with a wide range of network security solutions. This includes SASE, secure web gateways, enterprise proxies, and PAC file deployments.

### Network integration has 2 steps

{% stepper %}
{% step %}

### 1. Establish trust

Trust allows Koi to inspect marketplace traffic without certificate errors.

This step must be completed before any route is configured.

That applies to SASE, SWG, and PAC file deployments.

[Establishing Trust](/integration-guides/network/establishing-trust.md)
{% endstep %}

{% step %}

### 2. Establish route

After trust is in place, route supported marketplace traffic to Koi.

You can do this through your SASE or SWG platform, or with a PAC file.

[Establish Route](/integration-guides/network/establish-route.md)
{% endstep %}
{% endstepper %}

If you configure the route before trust is established, traffic inspection will not work correctly.

### Supported routing integrations

{% hint style="warning" %}
Always establish trust first. Routing Koi traffic through SASE or a PAC file is the second step.
{% endhint %}

* **PAC File** - [PAC File Integration](/integration-guides/network/establish-route/pac-file-integration.md)
* **Zscaler** - [Zscaler Guide](/integration-guides/network/establish-route/zscaler-guide.md)
* **Blue Coat (Symantec ProxySG)** - [Blue Coat Guide](/integration-guides/network/establish-route/bluecoat-guide.md)
* **Cloudflare** - [Cloudflare Guide](/integration-guides/network/establish-route/cloudflare-guide.md)
* **Cisco Umbrella** - [Cisco Umbrella Guide](/integration-guides/network/establish-route/umbrella-guide.md)
* **Prisma Access** - [Prisma Access Guide](/integration-guides/network/establish-route/prisma-access-guide.md)
* **Netskope** - [Netskope Guide](/integration-guides/network/establish-route/netskope-guide.md)
* **FortiGate** - [Fortinet FortiGate Guide](/integration-guides/network/establish-route/fortinet-fortigate-guide.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
