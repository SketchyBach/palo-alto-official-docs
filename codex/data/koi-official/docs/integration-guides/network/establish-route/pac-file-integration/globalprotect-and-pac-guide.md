<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/globalprotect-and-pac-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/globalprotect-and-pac-guide.md).

# GlobalProtect & Pac Guide

{% hint style="warning" %}
Establish trust before configuring any route. See [Establishing Trust](/integration-guides/network/establishing-trust.md).
{% endhint %}

***

In most cases this works out of the box: add the required firewall exclusions, deploy the Koi PAC file, and marketplace traffic is routed to Koi's proxy. Validate on a test machine before rolling out, and use the Troubleshooting section if the PAC file isn't respected.

This guide covers the Palo Alto firewall / GlobalProtect agent scenario.

***

### Step 1 - Add the required firewall exclusions

Allow the PAC file URL, marketplace domains, Koi proxy host and ports, and related traffic through your firewall.

For the full list, see [Firewall Exclusions for PAC File](/integration-guides/network/establish-route/pac-file-integration/firewall-exclusions-for-pac-file.md).

***

### Step 2 - Deploy the PAC file and test

1. Deploy the Koi PAC file to a **test machine** (could also be your own machine) to confirm routing works before a wider rollout.\
   To manually test the pac file on a test machine, see [Manual PAC File Integration](/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-manually.md) .
2. **Refresh the GlobalProtect connection.** This step is crucial: after the PAC file is applied, GlobalProtect must refresh its connection to pick up the new proxy configuration - one the test machine, use **Refresh Connection** from the app menu, or **Disconnect** and **Connect** again. Until then, GlobalProtect keeps using the proxy state captured at the previous connection and the PAC file won't take effect.
3. To verify, browse from the test machine to a covered domain with `/koi` appended — for example <https://marketplace.visualstudio.com/koi> — and confirm you see the Koi airship page.

Once confirmed, roll out the PAC file to the rest of your endpoints. If the PAC file doesn't take effect, see Troubleshooting below.

***

### Troubleshooting

#### Koi PAC isn't taking effect when GlobalProtect is connected

First, confirm you have refreshed the GlobalProtect connection (Step 2) — this is the most common cause. If the PAC file is still not respected, whether it applies depends on the operating system and the GlobalProtect configuration. Check the following:

* **"Set Up Tunnel Over Proxy" set to bypass proxies:** This forces all HTTP/HTTPS through the tunnel and ignores PAC rules on every OS. Set it to use proxies, or deploy the PAC via the portal (Managed PAC).
* **The GlobalProtect portal pushes its own PAC file:** Administrators can configure the portal to deploy a corporate PAC (or proxy) configuration to endpoints. When the agent connects, GlobalProtect backs up the machine's existing proxy settings, applies the portal's PAC for the duration of the session, and restores the original settings on disconnect. While connected, the portal's PAC overrides your locally deployed Koi PAC, so marketplace traffic isn't routed to Koi. Instead of a separate local PAC, merge Koi's rules into the portal's PAC.
* **Verify the active proxy state while connected:** run `scutil --proxy` on macOS, or check **Settings → Network & Internet → Proxy** on Windows.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/globalprotect-and-pac-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
