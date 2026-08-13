<!-- KOI source: https://docs.koi.ai/guardrails/overview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/overview.md).

# Overview

Guardrails provides a suite of advanced security measures designed to maximize security with zero operational overhead. Once enabled, these protections operate seamlessly in the background, ensuring your enterprise environment remains secure while maintaining a smooth experience for your workforce.

Each guardrail clearly shows which marketplaces it applies to, helping you understand scope and relevance per protection.

### Guardrails

1. [Malware Protection](/guardrails/malware-protection.md) - Automatically block packages identified as malicious leveraging Koi's Supply Chain Maware Database.
2. [Scan-first protection](https://success.koi.security/docs/scan-first-protection#/) - Prevent the installation of newly published non-binary software until our agentic risk engine scan is complete, typically within minutes to a few hours of publication.
3. [Version Update Cooldown](/guardrails/version-update-cooldown.md) - Delay automatic updates to allow public scrutiny of newly pushed versions.
4. [Delayed Access](https://docs.koi.ai/guardrails/delayed-access) - Block installations of newly published non-binary software for a set minimum period, allowing them to establish reputation and undergo public scrutiny before being deployed in your environment.
5. [Auto-remediate delisted](https://success.koi.security/update/docs/auto-remediate-delisted#/) - Automatically removes items that have been delisted or removed from the marketplace to reduce exposure and maintain a trusted environment.
6. [Sideloading Monitoring](/guardrails/sideloading-visibility.md) - Automatically detect unauthorized sideloading of items.
7. [MCP Registry Enforcement (Preview)](https://docs.koi.ai/guardrails/mcp-registry-enforcement) - Remove MCP servers installed outside the official Github MCP Registry
8. [Block Execution from Risky Paths (Preview)](/guardrails/block-execution-from-risky-paths-preview.md) - Block execution of binaries from high-risk, user-writable file system paths such as `/tmp`, `/var/tmp`, `$TMPDIR`, and `/Users/Shared/`.
9. [Agent Credential Access Restriction (Preview)](/guardrails/agent-credential-access-restriction.md) - Prevents the agent from reading sensitive files storing credentials and secrets.
10. [Agent Destructive Command Restriction (Preview)](/guardrails/agent-destructive-command-restriction.md) - Prevents the agent from performing destructive commands.<br>

***

### **Enforcement methods**

Guardrails are enforced across several layers of the Koi platform. The layer determines *when* a guardrail runs and *what* it can act on - from blocking marketplace downloads before they ever reach an endpoint, to intercepting agent behavior while it happens at runtime. Each guardrail uses the layer best suited to the protection it provides, and the UI indicates which method applies so you always understand how a protection is being enforced.

| Enforcement layer                    | When it runs                           |
| ------------------------------------ | -------------------------------------- |
| **Proxy** (marketplace gateway)      | At install / download time             |
| **Script** (discovery & remediation) | Scheduled / on-demand on the endpoint  |
| **Runtime hooks** (agent control)    | During agent activity runtime activity |
| **Santa** (binaries)                 | At macOS binary execution              |

**Mapping per guardrail** -

| Guardrail                                       | Proposed enforcement layer                                      |
| ----------------------------------------------- | --------------------------------------------------------------- |
| Malware Protection                              | Proxy + Script (block at download, remediate already-installed) |
| Scan-first protection                           | Proxy                                                           |
| Version Update Cooldown                         | Proxy                                                           |
| Delayed Access                                  | Proxy                                                           |
| Delisted monitoring                             | Script                                                          |
| Sideloading Monitoring                          | Script                                                          |
| MCP Registry Enforcement (Preview)              | Script                                                          |
| Block Execution from Risky Paths (Preview)      | Santa                                                           |
| Agent Credential Access Restriction (Preview)   | Runtime hooks                                                   |
| Agent Destructive Command Restriction (Preview) | Runtime hooks                                                   |

### Advanced configuration options

Guardrails are fully configurable to fit your organization's needs:

#### Alert-only mode

Activate guardrails in passive monitoring mode for applicable guardrails. Receive alerts when items match conditions without enforcing actions. This mode allows for risk visibility with zero disruption.

* Configurable via **Settings → Notifications**
* Ideal for staging and evaluation

> **Important:** Endpoint groups are **not supported** in alert-only mode. The guardrail will apply to all devices globally for alerting purposes. If you want scoped enforcement, switch 'Alert-only mode' off and you will be able to apply an Endpoint group restriction.

#### Global allowlist override

By default, guardrails respect the global allowlist. For high-risk scenarios, override this to ensure critical guardrails like **Malware Protection** enforce blocking even on allowlisted items by default.

{% hint style="info" %}
Note: regardless of the Global allowlist override setting, Guardrails will still take precedence over the custom policy rules
{% endhint %}

#### Endpoint group targeting

Apply guardrails to specific endpoint groups ensuring tailored enforcement across your organization.

* Ideal for phased adoption
* Supports differentiated risk tolerance

#### Impact check before enabling guardrails

You can run an **impact check** for key guardrails like Malware protection, Scan-first, Auto-remediate delisted, Delayed access, and Sideloading. This lets you see how many unique items, total instances, endpoints, and endpoint groups will be affected **before** applying the guardrail - helping you make informed decisions with full visibility.

> **How to use:**
>
> When configuring a guardrail, use the **Impact check** option to preview the number of unique items, affected endpoints, and endpoint groups. This allows you to assess operational impact in advance.
>
> <img src="https://files.readme.io/ea1b2fd7cdd7ac676fbfe3dcc58ea276c77bedb54ad1c67cfd13c1260ecf0413-image.png" alt="" data-size="original">
>
> * **Unique Items**: Number of affected items matching the guardrail's criteria.
> * **Total Instances**: Total occurrences found.
> * **Endpoints**: Number of endpoints affected.
> * **Endpoint Groups**: Groups impacted by the rule.

This feature helps you avoid unexpected disruptions and fine-tune guardrail rollout by providing data-driven visibility.

***

### How to Get Started

1. Navigate to the **Guardrails** page in the portal
2. Toggle protection settings to enable the desired protections


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/overview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
