<!-- KOI source: https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binary-executions-preview.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binary-executions-preview.md).

# Binary executions (Preview)

The Koi Binary execution view provides organizations with real-time visibility into every binary execution event across their endpoints.

Execution Events view presents **each execution as a separate log entry**. Every time a user launches a binary file, a new event is created and displayed in the UI.

This allows security and IT teams to investigate execution activity at the event level, understand user behavior,Understand who executed a binary, on which device, and when and analyze enforcement decisions in context.

<figure><img src="/files/GfcGusLR0YTvuHebFf5c" alt=""><figcaption></figcaption></figure>

***

### Coverage

The Binary events view includes **all binary execution logs collected from macOS endpoints**.

Each time a binary is launched on an endpoint, a new execution event is generated and presented in the UI.

The events are collected using Koi’s integration with **Santa on macOS**, which provides execution-level logging and enforcement decisions.&#x20;

To enable this capability, please contact the Customer Experience team to have the add-on enabled. Also, This capability requires configuring the Santa integration in your environment. Setup instructions and technical details can be found [here](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration).

You can learn more about Santa [here](https://santa.dev/).<br>

### &#x20;Binary events **table fields**

<table><thead><tr><th width="238.40625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>File name</strong></td><td>The binary file name, extracted from the execution path, for example chrome_crashpad_handler.</td></tr><tr><td><strong>Status</strong></td><td>The execution Santa decision, for example Allowed or Blocked.</td></tr><tr><td><strong>Reason</strong></td><td>Explains why the binary was allowed or blocked, and which policy was applied.</td></tr><tr><td><strong>Hostname</strong></td><td>The device name where the execution occurred.</td></tr><tr><td><strong>Is signed</strong></td><td>Indicates whether the binary is code-signed, based on signing metadata in execution logs.</td></tr><tr><td><strong>Platform</strong></td><td>OS platform, currently macOS only.</td></tr><tr><td><strong>Timestamp</strong></td><td>Date and time when the execution event occurred.</td></tr><tr><td><strong>User</strong></td><td>User account that executed the binary.</td></tr><tr><td><strong>Local user</strong></td><td>The local user account that executed the binary.</td></tr><tr><td><strong>Group</strong></td><td>Device group, based on the organization’s endpoint grouping.</td></tr><tr><td><strong>Path</strong></td><td>The file system path from which the binary was executed.</td></tr><tr><td><strong>SHA256</strong></td><td>SHA-256 hash of the binary file, this is the unique identifier for each row.</td></tr><tr><td><strong>Signing ID</strong></td><td>The signing identifier of the specific application or software, covering all its versions (Example: EQHXZ8M8AV:com.google.Chrome is the signing  of Google chrome desktop).</td></tr><tr><td><strong>Team ID</strong></td><td>The unique identifier of the publisher that signed the binary(Example: EQHXZ8M8AV is the Team ID of Google).</td></tr><tr><td><strong>Process ID</strong></td><td>The identifier of the process that executed the binary.</td></tr><tr><td><strong>Parent process name</strong></td><td>Parent process that launched the binary</td></tr><tr><td><strong>Parent process ID</strong></td><td>The identifier of the parent process that launched the binary.</td></tr><tr><td><strong>Signing Certificate Hash</strong></td><td>Hash of the signing certificate</td></tr></tbody></table>

{% hint style="info" %}
**Built-in rules:** To avoid blocking any Apple system binaries or Santa binaries, `santad` will create 2 immutable certificate rules at startup:

* The signing certificate santad is signed with
* The signing certificate launchd is signed with

By creating these two rules at startup, Santa should never block critical Apple system binaries or other Santa components.
{% endhint %}

***

### Why does this matter?

Security investigations often require **event-level context**.

This view is critical for:

* Incident investigation
* Audit and compliance validation
* Policy tuning and validation
* Understanding real execution behavior across users and devices

***

### Key benefits

* **Full event-level visibility**\
  See every binary execution event across macOS endpoints.
* **Faster investigation**\
  Filter and analyze execution logs across the organization or per device.
* **Enforcement transparency**\
  Understand exactly why a binary was allowed or blocked.
* **Deep forensic context**\
  Access detailed event metadata and raw log data when needed.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binary-executions-preview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
