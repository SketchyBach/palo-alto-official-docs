<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/old-overview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/old-overview.md).

# Old overview

The MDM Script Package is Koi’s agentless tool for enforcing visibility and remediation for items installed on all the platforms supported by Koi.

It allows organizations to:

* Register devices to the Koi platform.
* Discover installed platforms and items.
* Remediate items that violate defined policies.

The script is meant to run recurrently, typically on a schedule defined by the organization’s deployment system. Because it is a readable and auditable script package, it offers complete transparency into what it does, when, and how - giving security teams full clarity over each operation.

The script package is found under the deployment portal in your tenant. The script is available in two modes - managed and manual. Alongside its flavors it has different variations based on the deployed operating system.

## Development principles:

* **Transparent** - we share the source code of the script package via our deployment portal. We want you to be comfortable with what you are running.
* **Lightweight** - the script package is simply a set of instructions that are responsible to report what it found and execute what needs to be removed.
* **Agentless** - it uses your current MDM / Security Tool deployment that you are already used to working with.
* **Cross Platform** - the same script package for different operating systems.
* **Flexible** - it is configurable to make it suitable for your organizational structure.

## How does it work?

### Registration

Onboards a new device by registering to Koi’s system. Once a device is successfully registered it will be reflected in the endpoints tab under the deployment portal and also under the endpoint page in the main application. Each device is coupled with a unique identifier to further associate it with future executions and policy execution.

### Discovery

Quickly iterates over the endpoint to discover installed applications and platforms, their respective items, and their installed version. The script makes a distinction between each user that is configured on the endpoint, providing a better resolution to understand what is installed and on whom it is installed on.

### Remediation

The script package acts as the policy executioner. It gets a list of items it needs to remove, and removes them. The removal is a “hard” removal process - deletes the item’s files and folders from disk. This grants a robust level of protection compared to simply disabling items which keep them disk. The script knows which items need to be removed as a result of the following process:

1. It sends Koi all installed items as a result of the Discovery module.
2. Koi processes the items against the defined policies.
3. Koi sends a response to the script package - a list of all items that need to be removed, because they did not meet the policies.
4. The package removes the items.
5. A configurable notification can be sent to the end user for a clean transparent experience.\
   The script package default remediation setting is turned off. It cannot do anything unless you instruct it to do so via Koi’s application.

{% hint style="info" %}

## **Browser marketplace endpoint management**&#x20;

As part of Koi’s extension discovery and governance capabilities, when browser marketplace coverage is enabled, the Koi script actively manages browser extension policies on the endpoint. **This includes modifying specific registry keys (Windows) and managed preference files (macOS) related to extension allowlists and blocklists.**

On each run, Koi writes and replaces the browser’s extension policies (it does not merge with existing values), including:

* ExtensionInstallBlocklist
* ExtensionInstallAllowlist
* (Firefox) ExtensionSettings<br>

If these settings are also managed by other tools (e.g., GPO, Intune, Jamf), conflicts may occur. Koi will overwrite those values on each script run, and external management tools may overwrite Koi’s values on their next sync cycle.<br>

#### Configuration Options

If your organization already manages browser extension policies externally, you can choose one of the following:

* **Disable browser marketplace coverage**

  Contact your Koi representative to disable this feature. This will prevent Koi from reading or modifying any browser-related policy keys.

  *Note: This will also disable extension discovery for those browsers.*
* **Consolidate policy management into Koi**

  Use Koi as the single source of truth for extension allow/block lists to avoid conflicts with other management tools.
  {% endhint %}

## Putting it together

### Secure Connection

The script identifies itself to Koi's platform using your device's unique characteristics (hostname, serial number, users). This establishes a secure, authenticated connection and retrieves your organization's current policies.

### Discovery Sweep

The script systematically scans the device to understand what's installed:

1. Platforms: Identifies which browsers, IDEs, and applications are present.
2. Items: Catalogs all installed items, plugins, and add-ons.
3. Users: Covers all user profiles on the device for complete visibility.

This discovery process is read-only - nothing is changed during this phase.

### Policy Evaluation

The script sends its findings to Koi's backend, which evaluates everything against your defined policies and guardrails. The response is simple: a list of specific items that need to be removed because they violate your governance rules.

### Targeted Remediation

Only items that violate policies are removed. The script:

1. Removes files: Completely deletes item files from disk.
2. Blocks reinstallation: Configures platform policies to prevent unauthorized reinstalls. Chromium based browsers support adding items to a local block list.
3. Notifies users: Optionally displays friendly notifications about removed items.

### Clean Finish

The script reports back what actions were taken, logs everything for audit purposes, and exits cleanly. Your endpoints are now compliant with your policies.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/old-overview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
