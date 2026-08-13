<!-- KOI source: https://docs.koi.ai/get-started/platform-coverage.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/get-started/platform-coverage.md).

# Capabilities coverage

Koi is your single pane of glass that delivers full lifecycle protection for software supply chain assets across IDEs, AI tools, browsers, code registries, binaries and applications. It provides deep visibility and governance through core capabilities:

* Discovery - Identifies installed items across all endpoints.
* Risk - Assigns dynamic, research-driven risk levels per item based on publisher reputation, composition, and behavioral indicators.
* Remediation - Enables organizations to remove high-risk or policy-violating items from endpoints using automated or manual workflows.
* Prevention - Blocks installation of unauthorized or high-risk items at source by using Koi’s gateway or block usage of items in runtime on the device.
* Guardrails - Out-of-the-box protection rules that automatically enforce security best practices across your environment with minimal effort.

***

## Visibility, Risk & Remediation

* AES gives you visibility and an AI-first risk assessment of - every component of the modern software stack and agentic activity.
* &#x20;Lets you remediate what poses a risk.
* Dependent on the [Endpoint Integration](/integration-guides/endpoint-integration.md).<br>

<table data-search="false"><thead><tr><th>Component</th><th>Agentic component</th><th>Discovery</th><th>Risk</th><th width="131.21240234375">Remediation</th></tr></thead><tbody><tr><td>Claude, Claude Code, Cursor, Codex, Kiro, Windsurf (Devin Desktop), Google Antigravity</td><td>Agents</td><td>✅</td><td>✅</td><td>✅ (IDE extensions)</td></tr><tr><td>MCPs</td><td>Agent extensions</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Skills</td><td>Agent extensions</td><td>✅</td><td>Coming soon</td><td>Coming soon</td></tr><tr><td>Plugins</td><td>Agent extensions</td><td>✅</td><td>Coming soon</td><td>✅</td></tr><tr><td>Hugging Face</td><td>AI models</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Ollama</td><td>AI models</td><td>✅</td><td>✅</td><td>-</td></tr><tr><td>Npm, PyPI</td><td>Code packages</td><td>✅</td><td>✅</td><td>Npm malware only</td></tr><tr><td>Homebrew</td><td>OS packages</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Chocolatey</td><td>OS packages</td><td>✅</td><td>✅</td><td>-</td></tr><tr><td>VSCode, JetBrains, OpenVSX</td><td>IDE extensions</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Chrome, Firefox, Edge, Prisma, Comet, Dia, ChatGPT Atlas, Arc (macOS)</td><td>Browser extensions</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Cloned Git repos</td><td>Git repos</td><td>✅</td><td>Coming soon</td><td>Coming soon</td></tr><tr><td>Windows, macOS</td><td>Applications</td><td>✅</td><td>-</td><td>-</td></tr></tbody></table>

### Prevention

* Prevention is mostly done by proxy enforcement method to secure the packages, extensions, skills, MCPs, and dependencies that developers and AI agents rely on.&#x20;
* Prevention with proxy is stopping risky components at the point of download.&#x20;
* Prevention can be applied through custom policies and through guardrails.
* Dependent on the [Network Integration](/integration-guides/network.md).<br>

<table data-search="false"><thead><tr><th>Source</th><th>Agentic component</th><th>Custom policies</th><th>Guardrails</th><th width="136.0999755859375">Enforcement method</th></tr></thead><tbody><tr><td>GitHub MCP Registry</td><td>Agent extensions - MCPs</td><td>✅</td><td>✅</td><td>Proxy</td></tr><tr><td>Claude Desktop Connectors</td><td>Agent extensions - MCPs</td><td>✅</td><td>Coming soon</td><td>Proxy</td></tr><tr><td>Skills.sh, clawhub, official skills repos (Anthropic, OpenAI, GH Copilot, Gemini CLI)</td><td>Agent extensions - Skills</td><td>Coming soon</td><td>Coming soon</td><td>-</td></tr><tr><td>Cursor plugins marketplace, Claude plugins marketplace</td><td>Agent extensions - Plugins</td><td>Coming soon</td><td>Coming soon</td><td>-</td></tr><tr><td>Hugging Face</td><td>AI models</td><td>✅</td><td>✅</td><td>Proxy</td></tr><tr><td>Ollama</td><td>AI models</td><td>-</td><td>-</td><td>Proxy</td></tr><tr><td>Npm, PyPI</td><td>Code packages</td><td>✅</td><td>✅</td><td>Proxy</td></tr><tr><td>Homebrew</td><td>OS packages</td><td>✅</td><td>✅</td><td>Endpoint script package</td></tr><tr><td>Chocolatey</td><td>OS packages</td><td>-</td><td>-</td><td>-</td></tr><tr><td>VSCode, JetBrains, OpenVSX, Cursor, Windsurf (Devin Desktop)</td><td>IDE extensions</td><td>✅</td><td>✅</td><td>Proxy</td></tr><tr><td>Chrome, Firefox, Edge, Prisma, Comet, Dia, ChatGPT Atlas, Arc</td><td>Browser extensions</td><td>✅</td><td>✅</td><td>Proxy</td></tr><tr><td>Cloned Git repos</td><td>Git repos</td><td>Coming soon</td><td>Coming soon</td><td>-</td></tr></tbody></table>

### Agent hardening & behaviour control

* Agent hardening uses runtime hooks to control what AI agents can do in real time.
* Controls can be applied through custom policies and guardrails.
* This is an out-of-the-box capability. No extra steps are needed to enable it.

<table data-search="false"><thead><tr><th>Agent</th><th>Custom policies</th><th>Guardrails</th><th>Personal account</th><th width="153.8563232421875">Enforcement method</th></tr></thead><tbody><tr><td>Claude Code</td><td>✅</td><td>✅</td><td>✅ CLI only</td><td>Runtime hooks</td></tr><tr><td>Cursor</td><td>✅</td><td>✅</td><td>✅</td><td>Runtime hooks</td></tr><tr><td>Codex</td><td>✅</td><td>✅</td><td>✅</td><td>Runtime hooks</td></tr><tr><td>Gemini CLI</td><td>✅</td><td>✅</td><td></td><td>Runtime hooks</td></tr><tr><td>GitHub Copilot</td><td>✅</td><td>✅</td><td></td><td>Runtime hooks</td></tr><tr><td>Antigravity CLI</td><td>✅</td><td>✅</td><td>✅</td><td>Runtime hooks</td></tr><tr><td>Kiro</td><td>Coming soon</td><td>Coming soon</td><td></td><td>-</td></tr><tr><td>Windsurf (Devin Desktop)</td><td>Coming soon</td><td>Coming soon</td><td></td><td>-</td></tr></tbody></table>

### App control

* App control uses Santa agent to control binary execution in real time, governing which binaries are allowed to run on the endpoint.
* Controls can be applied through custom policies and guardrails.
* Dependent on the [Santa Integration.](/integration-guides/endpoint-integration/santa-integration.md)

<table><thead><tr><th>Operating system</th><th>Custom policies</th><th>Guardrails</th><th width="142.09375">Enforcement method</th></tr></thead><tbody><tr><td>macOS</td><td>✅</td><td>✅</td><td>Santa</td></tr><tr><td>Windows</td><td>Coming soon</td><td>Coming soon</td><td>Cortex XDR</td></tr></tbody></table>

## Enforcement methods

* AES enforces policy through four complementary methods. Each operates at a different layer of the stack and at a different moment in the lifecycle of a item (Like Extensions, Code packages, MCP and more).
* Together they cover everything from the moment a developer downloads a extension to the moment an AI agent takes a runtime action.

| Proxy                                             | Public source   | When end-user try to download the item from the public source | Public source traffic (non-binaries such as extensions & code packages)         | \~1 hour                                                                              |
| ------------------------------------------------- | --------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Endpoint script package (Discovery & Remediation) | On the endpoint | On-demand when creating a block policy or remediation         | <p>Remove already-installed items</p><p>\*Prevention for OS packages & MCPs</p> | Depends on the run cadence of the script package via MDM/EDR that executes the script |
| Runtime hooks                                     | On the endpoint | Real time - AI agent activity                                 | AI Agent actions                                                                | \~1 hour from policy update, then continuous and block in real time                   |
| Santa                                             | On the device   | Real time - macOS binaries executions                         | Binary executions                                                               | \~1 hour, then continuous and block in real time                                      |

{% hint style="info" %}
Review our remediation documentation for more [information](/guides/remediation-in-koi.md)&#x20;

Review our governance best practice documentation for more [information](/guides/governance-best-practices.md)
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/get-started/platform-coverage.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
