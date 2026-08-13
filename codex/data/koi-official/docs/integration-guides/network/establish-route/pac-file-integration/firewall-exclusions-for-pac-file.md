<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/firewall-exclusions-for-pac-file.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/firewall-exclusions-for-pac-file.md).

# Firewall Exclusions for PAC File

{% hint style="warning" %}
Establish trust before configuring any route. See [Establishing Trust](/integration-guides/network/establishing-trust.md).
{% endhint %}

***

### Required exclusions

Allow the following through your firewall.

#### 1. PAC file URL

Allow endpoints to retrieve the **PAC file URL** *(found in your Koi deployment portal → Network Integration)*. If the firewall blocks or filters this URL, clients can't load the PAC file and fall back to direct routing, bypassing Koi.

Looks something like [https://assets.koi.security/pac/xxxx.pac](https://assets.koi.security/pac/5ee433a5-c889-4283-9482-8844e56cb114.pac)

#### 2. Marketplace domains

Explicitly allow the covered **marketplace domains**. This is important: if these domains are blocked or filtered by web-filtering or URL-category rules, installs and updates fail even when routing is correct.\
Explicitly allow these domains to the Koi Proxy ports (8090-8100).

See the full list of domains in your deployment portal.

#### 3. Koi proxy URL and ports

Allow outbound traffic to the **Koi proxy FQDN/IP** on TCP ports **8090–8100**. The PAC file dynamically selects a port within this range per environment, so the entire range must be open - not just a single port.

Your proxy url can be found on your deployment portal.

#### 4. Application / URL-category coupling

On firewalls that classify traffic by application or URL category (such as Palo Alto App-ID), an allow rule based on host and port alone may not match. Couple the rule to the relevant applications/categories - for example `http-proxy`, `web-browsing`, and `ssl`, plus the Google-based categories used by Chrome/Google marketplace domains.

***

### Troubleshooting

If marketplace access still fails after applying the exclusions above:

* **Allow the HTTP `CONNECT` method to ports 8090–8100.** Some proxy or application policies restrict which ports `CONNECT` may target even when the host and port are otherwise permitted.
* **Write the allow rules using domain names, not hardcoded IP addresses.** The marketplace domains and the Koi proxy are usually served from CDNs, so the IP address behind a given hostname changes often. If you allow a specific IP, the rule works at first and then silently breaks the next time the IP rotates, causing intermittent failures. Instead, create the rules against the hostnames themselves (for example Palo Alto FQDN objects) so the firewall periodically re-resolves each name via DNS and keeps allowing whatever IPs it currently points to.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/firewall-exclusions-for-pac-file.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
