<!-- KOI source: https://docs.koi.ai/guides/endpoint-removal-and-soft-delete.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/endpoint-removal-and-soft-delete.md).

# Endpoint lifecycle management (Preview)

Koi automatically manages the lifecycle of endpoints to ensure your organization's inventory stays accurate and relevant. Endpoints can be **manually archived by an admin** or **automatically archived** after a defined period of inactivity.

***

### Overview

Endpoints that no longer communicate with Koi or are intentionally decommissioned by an admin are removed from the active views and moved to the **Archive** for record keeping.

Archiving an endpoint does **not** uninstall or disable the Koi script or agent on the device. Koi's prevention and protection policies **will continue to be enforced** on the endpoint according to its assigned group configuration. Archiving only affects the endpoint's **visibility** and **management** **status** within the Koi platform.

<figure><img src="/files/FnWYnhB8LsRdobweIQRK" alt=""><figcaption></figcaption></figure>

***

### Endpoint states

| State        | Description                                                                                                                                                                                                                         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Active**   | The endpoint is actively communicating with Koi.                                                                                                                                                                                    |
| **Stale**    | The endpoint has not communicated for the configured number of days but remains visible in the active view.                                                                                                                         |
| **Archived** | The endpoint has been removed from active views and moved to the Archive. This may occur automatically after inactivity or manually when archived by an admin. Archived endpoints remain visible for historical and audit purposes. |

***

### Types of removal

| Deletion type | Trigger       | Description                                                                                                                                           |
| ------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manual**    | Admin action  | The endpoint is intentionally removed from all active views. This action is performed by an admin using **Archive endpoint** from the Endpoints page. |
| **Automatic** | System action | The endpoint is automatically archived after being inactive for the configured archive threshold. This helps maintain an up-to-date inventory.        |

> Both actions transition the endpoint into the **Archived** state.

***

### Configuration

You can configure the thresholds for **Stale** and **Archive** under:

**Settings → Advanced settings → Endpoints**

* **Stale threshold** - Defines how many days of inactivity mark an endpoint as stale.
* **Archive threshold** - Defines how many days beyond the stale period an endpoint will be automatically archived.

> The archive threshold must always be longer than the stale threshold (minimum = stale + 1 day).

<figure><img src="/files/rvnk0aJiKN8WvVl35VNU" alt=""><figcaption></figcaption></figure>

***

### Manually archiving an endpoint

Admins can archive an endpoint at any time:

1. Go to **Endpoints → Current**.
2. Click the **⋯** menu next to the endpoint.
3. Select **Archive endpoint**.
4. Confirm by typing the endpoint hostname.

The endpoint will be moved to the **Archive**, and its record will show its deletion type.

***

### Viewing archived endpoints

To review endpoints that were removed or automatically soft deleted:

1. Navigate to **Endpoints → Archive**.
2. Use filters such as **OS** or **Reason** to narrow results.

***

### Reactivating endpoints

If an endpoint was **automatically archived** after exceeding the inactivity threshold and later reconnects to Koi (for example, when the device comes back online), it will automatically reappear in the **Current** view as an **Active** endpoint. All items associated with this endpoint, including discovered extensions, packages, MCP servers, and other software components, will also be restored to the active inventory, risk, and remediation views.\
This ensures the entire endpoint context and its related components are fully reinstated and visible across the Koi platform.

***

### Audit and reporting

All endpoint archiving actions are logged in the audit log under **Endpoints** type. These logs ensure full traceability for compliance and operational auditing.

***

### Summary

Koi's endpoint removal lifecycle ensures your environment stays clean and manageable:

* Admins can **archive endpoints** when they are decommissioned or irrelevant.
* Koi automatically performs **archiving** for inactive endpoints.
* All removed endpoints remain accessible in the **Archive** for visibility and audit.

This approach balances operational hygiene with full historical accountability.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/endpoint-removal-and-soft-delete.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
