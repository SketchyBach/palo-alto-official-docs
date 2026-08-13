<!-- KOI source: https://docs.koi.ai/guides/protect-applications-with-koi/binaries-governance-preview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-applications-with-koi/binaries-governance-preview.md).

# Binaries - Governance (Preview)

#### Table of content

[Policies](#policies)&#x20;

* [Custom Policy](#custom-policy)
* [Policies use cases](#policies-use-cases)

[Guardrails](#guardrails)

[Enforcement Modes](#enforcement-modes)

[End-User experience](#end-user-experience)

[Key Benefits](#key-benefits)

***

Koi provides organizations with comprehensive controls to manage, monitor, and enforce governance over binary execution across macOS endpoints.

Koi enables security teams to define policies that block unwanted or high-risk binaries. With these new capabilities, administrators can:

* Define which binaries, applications, or publishers are blocked
* Evaluate policy productivity impact before enforcement
* Provide end-user notifications with structured approval workflows
* Define and apply policies with granular scoping based on organizational profiles(e.g., developers, sales)

To enable this capability, please contact the Customer Experience team to have the add-on enabled.&#x20;

***

## Policies

### Custom Policy&#x20;

You can create your own block custom policies by access Binaries governance through the **Policies** page (Governance->Policies->Create New Policy) and select **Binaries** as the **Policy scope**.

<figure><img src="/files/SDVmcCrh2kmSPXDO28ee" alt=""><figcaption></figcaption></figure>

**Apply policies based on**

<table><thead><tr><th width="238.40625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>SHA256</strong></td><td>SHA-256 hash of the binary file, this is the unique identifier for each row.</td></tr><tr><td><strong>Signing ID</strong></td><td>The signing identifier of the specific application or software, covering all its versions (Example: Google chrome desktop).</td></tr><tr><td><strong>Team ID</strong></td><td>The unique identifier of the publisher that signed the binary (Example: Google).</td></tr><tr><td><strong>File name</strong></td><td>The binary file name, extracted from the execution path, for example chrome_crashpad_handler.</td></tr><tr><td><strong>Last used</strong></td><td>Last time a user in the organization executed this binary.</td></tr><tr><td><strong>Is signed</strong></td><td>Indicates whether the binary is code-signed, based on signing metadata in execution logs.</td></tr><tr><td><strong>Signing Certificate Hash</strong></td><td>Hash of the signing certificate</td></tr></tbody></table>

{% hint style="info" %}
**Note on Last used policies**

Last used is always calculated org-wide, not per group. A policy like "Block all binaries not used in 90+ days" blocks any binary unused *anywhere in the org* for that period, even when scoped to a device group.
{% endhint %}

You do not need to start from scratch. The [**Policy library**](https://docs.koi.ai/guides/governance-best-practices/policy-library) provides ready-to-use templates that help you quickly implement governance policies and adapt them to your organization’s needs.

You can start from an existing template and adjust the identifiers, scope, or enforcement settings as needed.

For example:

| Block untrusted publishers                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Start with this template to block all binaries signed by a specific publisher using a **Team ID**. This allows you to quickly prevent software from non-approved vendors. For instance, blocking Team ID `Y5PE65HELJ` will prevent all applications signed by the developer Peter Steinberger (OpenClaw) from executing. |

| Block untrusted applications                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Use this template to block a specific application based on its **Signing ID**. This is useful for preventing unwanted tools such as RMM software, VPN tools, gaming applications, or other non-approved apps. Blocking the Signing ID ensures that **all versions of the application** are prevented from executing, rather than requiring separate policies for individual SHA256 hashes. |

### Policies use cases

#### 1. Block AI and Automation Tool like OpenClaw.

[OpenClaw](https://openclaw.ai/) (formerly Clawdbot and Moltbot) is an open-source autonomous AI agent that runs on your desktop and connects to [hundreds of services](https://clawhub.ai/skills?sort=downloads), such as Slack, Google Workspace, Notion, Outlook, and more. This broad access creates a security risk since a malicious prompt injected into any connected service could exfiltrate sensitive data.\
\
you can create a block policy by `Team ID: Y5PE65HELJ`\
This blocks all binaries signed by that Team ID (publisher identifier), which is useful for preventing unauthorized software non-approved applications. In this case it will prevent Every App by this Developer: Peter Steinberger.

#### 2. Block Applications That Are No Longer Used

Applications that are no longer actively used in the organization can become unnecessary risk over time, especially if they are outdated or no longer maintained.

Using the **Last Used** field, teams can identify applications that have not been executed in the last 30, 60, or 90 days.

Security teams can then create targeted Block policies to:

* Remove outdated or abandoned software
* Reduce exposure to unused and potentially vulnerable applications

#### 3. Block Unauthorized RMM Tools

Remote management RDP-based tools can significantly increase the attack surface if they are not centrally governed. Without clear controls, different teams may adopt different tools, creating unnecessary security risk.

Use Signing ID-based Block policies to enforce the use of approved solutions only. For example, the organization can define that only TeamViewer is authorized, while all other remote access tools are blocked.

#### 4. Enforce Code-Signing Hygiene

Unsigned or invalidly signed binaries increase the risk of malicious executions.

Use the **Invalid Signature Block policy** to:

* Block binaries with broken trust chains
* Prevent execution of tampered files

***

## **Guardrails**

### Block execution from risky paths

Blocks execution of binaries from user-writable file system paths, such as `/tmp`, `/var/tmp`, `$TMPDIR`, and `/Users/Shared/`, to harden your devices against untrusted or potentially unsafe content.

<figure><img src="/files/QzoXTstSc3jWI2qRYCOY" alt=""><figcaption></figcaption></figure>

More info on this Guardrail can be found [here](/guardrails/block-execution-from-risky-paths-preview.md).

***

## Enforcement Modes

Binaries control capability requires configuring the Santa integration in your environment. Setup instructions and technical details can be found [here](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration).

Enforcement operates in **Monitor mode**. In this mode, unknown binaries (those without any policy rules) are allowed to execute. All execution events are logged for visibility and analysis in the  [Binaries executions page.](/guides/protect-applications-with-koi.md)

{% hint style="info" %}
**Built-in rules:** To avoid blocking any Apple system binaries or Santa binaries, `santad` will create 2 immutable certificate rules at startup:

* The signing certificate santad is signed with
* The signing certificate launchd is signed with

By creating these two rules at startup, Santa should never block critical Apple system binaries or other Santa components.
{% endhint %}

***

## End-User experience

When an application or binary execution is blocked, the end user get a notification stating that it was blocked by the organization security policy. If the user believes they should use the blocked binary, they can simply request it by clicking **Request Approval** to ask their administrator for review.

<figure><img src="/files/A5hqgWCVp61DxOjBwfSP" alt=""><figcaption></figcaption></figure>

***

## Key Benefits

* **Custom enforcement**\
  Define and enforce block policies based on Team ID, Signing ID and SHA-256.
* **Granular Scoping**\
  Apply different policies to specific groups such as developers, sales, or high-risk profiles.
* **Scalable applications control**\
  Control entire applications or binaries across all versions without managing individual hashes.
* **Productivity-aware enforcement**\
  Run Impact Check before enabling policies to minimize disruption to business workflows.
* **End user notification and approval workflow**\
  Provide end-user notifications with built-in request approval flows for controlled exception handling.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-applications-with-koi/binaries-governance-preview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
