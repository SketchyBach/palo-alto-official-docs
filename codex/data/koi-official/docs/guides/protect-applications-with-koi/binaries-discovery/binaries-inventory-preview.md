<!-- KOI source: https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binaries-inventory-preview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binaries-inventory-preview.md).

# Binaries Inventory (Preview)

### Binaries Inventory

The Koi Binaries Inventory provides organizations with deep visibility into binary files that are executed across endpoints.

The inventory includes details such as binary file name, signing information, number of endpoints where the binary was observed, first and last execution timestamps and more. Each binary is uniquely identified by its SHA-256 hash. \
\
Koi enriches the data with applications context, publisher information so you can quickly understand what types of binaries are running across your environment, for example development tools, remote access tool, and more. This data helps teams identify binaries that are out of policy, unknown, or unsigned.

### Coverage

The Inventory include every binary that was executed across macOS endpoints in the organization- such as applications executables (`MyApp.app/Contents/MacOS/MyApp`), CLI tools (`/usr/local/bin/*`), portable apps (binaries from `~/Downloads`) and more. \
\
The inventory is built using Koi’s integration with **Santa on macOS**, which provides execution-level visibility into binary activity. Koi builds this inventory by leveraging Santa application control logs on macOS. \
\
To enable this capability, please contact the Customer Experience team to have the add-on enabled. Also, This capability requires configuring the Santa integration in your environment. Setup instructions and technical details can be found [here](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration).\
\
You can learn more about Santa [here](https://santa.dev/).

### **Inventory table fields**

<table data-search="false"><thead><tr><th width="238.40625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>File name</strong></td><td>The binary file name, extracted from the execution path, for example chrome_crashpad_handler.</td></tr><tr><td><strong>Endpoints</strong></td><td>Number of unique endpoints where this exact SHA-256 was executed.</td></tr><tr><td><strong>Last used</strong></td><td>Last time a user in the organization executed this binary.</td></tr><tr><td><strong>Is signed</strong></td><td>Indicates whether the binary is code-signed, based on signing metadata in execution logs.</td></tr><tr><td><strong>SHA256</strong></td><td>SHA-256 hash of the binary file, this is the unique identifier for each row.</td></tr><tr><td><strong>Platform</strong></td><td>OS platform, currently macOS only.</td></tr><tr><td><strong>Last seen</strong></td><td>Most recent time Koi observed an execution event for this binary across the organization.</td></tr><tr><td><strong>First seen</strong></td><td>First time Koi observed an execution event for this binary on any endpoint.</td></tr><tr><td><strong>Hostnames</strong></td><td>Hostnames of the endpoints where the binary was executed recently.</td></tr><tr><td><strong>Groups</strong></td><td>Device groups, based on the organization’s endpoint grouping.</td></tr><tr><td><strong>Path</strong></td><td>The file system path from which the binary was executed.</td></tr><tr><td><strong>Signing ID</strong></td><td>The signing identifier of the specific application or software, covering all its versions (Example: EQHXZ8M8AV:com.google.Chrome is the signing  of Google chrome desktop).</td></tr><tr><td><strong>Team ID</strong></td><td>The unique identifier of the publisher that signed the binary(Example: EQHXZ8M8AV is the Team ID of Google).</td></tr><tr><td><strong>Signing Certificate Hash</strong></td><td>Hash of the signing certificate</td></tr></tbody></table>

{% hint style="info" %}
**Built-in rules:** To avoid blocking any Apple system binaries or Santa binaries, `santad` will create 2 immutable certificate rules at startup:

* The signing certificate santad is signed with
* The signing certificate launchd is signed with

By creating these two rules at startup, Santa should never block critical Apple system binaries or other Santa components.
{% endhint %}

***

## **Why does this matter?**

Modern threats often do not rely on traditional applications alone.\
Attackers frequently use small binaries, unsigned tools, or helper executables that bypass visibility when teams rely only on application inventory.

Without execution-level visibility, security and IT teams can’t confidently answer questions like:\
What binaries are actually running in the environment, which ones are governed by policy, and which binaries may pose a risk.

The Binaries Inventory complements the Application Inventory and serves as a foundational layer for effective application control. It enables teams to first **understand what is happening in their environment**, decide on an appropriate governance approach and policies, and then validate and refine enforcement over time, without manual investigation on each endpoint.

***

## **Key benefits**

* **Full execution visibility**

  See what binaries actually run across macOS endpoints.
* **Reduced attack surface**

  Identify unknown, unsigned, unused, unwanted or high-risk binaries.
* **Stronger governance and audibility**

  Understand how application control policies affect real execution behavior across the fleet.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binaries-inventory-preview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
