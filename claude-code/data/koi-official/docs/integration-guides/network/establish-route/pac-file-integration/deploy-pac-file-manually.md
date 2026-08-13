<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-manually.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-manually.md).

# Deploy PAC File manually

{% hint style="warning" %}
Establish trust before configuring any route. See [Establishing Trust](/integration-guides/network/establishing-trust.md).
{% endhint %}

***

This guide explains how to manually deploy a PAC file on a single computer for testing.\
Once applied, your machine will route traffic according to the rules defined in the PAC file.

***

## Prerequisites

Before starting, ensure you have:

* The **PAC file URL**\
  \&#xNAN;*(Found in the Koi deployment portal → Network Integration)*
* Administrator privileges on your OS

***

## 1. Configure the PAC file

### MacOS

**Open System Settings**

1. Go to Network
2. Select your active interface (Wi-Fi or Ethernet)
3. Click Details / Advanced (on older Macs)
4. Open the Proxies tab
5. Check Automatic Proxy Configuration
6. Paste your PAC file URL in the URL field
7. Click OK, then Apply

### Windows

**Open Proxy Settings**

1. **Settings → Network & Internet → Proxy → Automatic proxy setup**
2. Check **Automatically detect settings** to on.
3. Click on **Use setup script** and fill in the **Koi PAC File** url.\
   Make sure it's on.

***

## 2. Verify the Configuration

{% hint style="danger" %}
**Open and close your browser for changes to take effect**
{% endhint %}

Navigate to a domain covered by the PAC file, adding `/koi` to the path.\
e.g <https://marketplace.visualstudio.com/koi>

Make sure that you can see the Koi airship.

![](https://files.readme.io/80f473027f6c410d22dc1640f1175f1f0fc8f716f5f36442481ecc8f13ed073b-image.png) *A custom page served by the Koi proxy that verifies that you are routing through Koi Proxy*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-manually.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
