<!-- KOI source: https://docs.koi.ai/guides/end-user-notifications.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/end-user-notifications.md).

# End-user notifications

Koi is built to balance organizational security and end-user productivity. Koi supports notifying end-users directly when an item has been removed from their device, or when it violates an organizational policy. This capability helps security teams educate users, offer safe alternatives, and guide remediation without interrupting workflows.

Balancing strong security with a great end-user experience is one of Koi’s core values. We believe organizations should be able to enforce governance while empowering their workforce to stay productive. End-user notifications are designed to support this philosophy by enabling gradual adoption of policies with transparency, education, and collaboration between security teams and users.

***

### Notification types

Koi supports multiple types of notifications to communicate directly with end users when items are removed or violate company policy.

#### Remediated items

If an item has been removed from an endpoint based on a guardrail (e.g. Malware protection) or due to policy enforcement, Koi can send a notification to the user who had it installed.

**Channels supported:**

* Slack (Desktop app only for Mac and Windows)
* Emails (based on [Okta](/integration-guides/okta.md) or [Entra](/integration-guides/entra-id-integration.md) integrations)

***

#### Policy violations

**Item violating a policy**

For items that are currently installed and violate a configured alerting policy, Koi will support notifying the end user with educational and actionable context.

**When this applies:**

* An item is installed on the user’s device and violates an existing risk-based alerting policy
* Admins choose to send a notification for end users for the same alerting policy:

![](https://files.readme.io/9a23441a5f3d85b6b6299e145815fb7544bc70b987a615b5a1ab949f6616272f-image.png)

**Item under block status**

For items that are currently installed but violating blocking policy or guardrails, Koi will support notifying the end user with educational and actionable context.

**When this applies:**

* An item is installed on the user’s device and violates an existing block policy or blocking guardrails.
* Admins choose to send a notification for end users for blocked items:

![](https://files.readme.io/b78896a23b6ee3999a5066d2ae001ed099af9fc3695af99bd359b64bcc7fc0ee-image.png)

**Notification will include:**

* Item metadata
* Platform
* Guidance to remove it

**User response options:**

* "Request approval": Submit a justification to keep it, routed to security team

**Channels supported:**

* Slack (Desktop app only for Mac and Windows)

**Admin control:**

* Configure notification channels (Settings → Notifications)
* Enable end-user notifications for relevant policy types

> Note: Notifications only apply to items that are already installed on a user’s device. For blocked items, Koi already surfaces a block message during the install flow.

***

#### Item request approval update (Preview)

Notifies the end-user when an admin approves or rejects an item request they submitted via the request form.

**When this applies:**

* End-user has submitted a request to keep or install an item.
* Admin has taken an approval or rejection action.

**Notification will include:**

* Item details
* Approval or rejection decision
* Admin comments (if provided)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/end-user-notifications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
