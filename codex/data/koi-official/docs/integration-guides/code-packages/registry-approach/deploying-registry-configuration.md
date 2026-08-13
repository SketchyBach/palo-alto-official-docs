<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/registry-approach/deploying-registry-configuration.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/registry-approach/deploying-registry-configuration.md).

# Deploying Registry Configuration

## Before You Begin

Before deploying registry configuration manually, consider whether existing infrastructure can simplify the integration:

* **Secure Web Gateway or endpoint agent**: If your organization already routes traffic through an SWG, you may be able to integrate Koi at that layer. This handles routing and trust automatically without per-tool configuration.
* **Repository manager**: If you use a centralized repository manager, you can configure Koi as an upstream registry. This avoids deploying configuration to individual endpoints.

Check the relevant integration guides to see if these approaches fit your environment.

***

### When to Use This Guide

Deploy registry configuration directly to endpoints when:

* You use a **PAC file** integration and CLI tools (pip, npm) do not inherit proxy settings
* You need to configure **CI runners** or **containers** that do not have access to your SWG
* You want a lightweight integration without deploying additional agents

***

## Configuration Commands

The following commands are examples of how to configure pip and npm to use the Koi registry. Depending on your environment, you may need to adjust flags or add additional configuration

#### Python (pip)

```bash
pip config set global.index-url "https://koi-pypi-<customer_subdomain>.gateway.koi.security/simple"
```

> Note: The pip config set command writes to the user-level configuration, which applies across all Python environments for that user. Project-level or command-line settings will take precedence if specified.

#### NPM

```bash
npm config set registry "https://koi-npmjs-<customer_subdomain>.gateway.koi.security"
```

Replace `<customer_subdomain>` with your Koi subdomain. The actual URLs are listed in your Koi deployment portal.

> **Note**: You can optionally run `npm config set replace-registry-host always` to ensure the custom registry is saved in lock files.

***

## Deployment via MDM Examples

These commands can be deployed at scale using endpoint management tools.

#### macOS with Jamf Pro

1. In Jamf Pro, navigate to **Settings > Scripts** and create a new script
2. Add the pip and npm commands above
3. Create a new **Policy**, attach the script, and scope to target machines

#### Windows with Intune

1. In Intune, navigate to **Devices > Scripts** and add a new PowerShell script
2. Add the pip and npm commands above
3. Set "Run this script using the logged-on credentials" to **Yes**
4. Assign to target device groups

***

### Verification

```bash
pip config get global.index-url
npm config get registry
```

***

### Notes

No additional trust configuration is required. Koi serves certificates signed by a globally recognized Root CA.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/registry-approach/deploying-registry-configuration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
