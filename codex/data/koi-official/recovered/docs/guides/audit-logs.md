Source: https://docs.koi.ai/guides/audit-logs.md

# Audit logs

Koi generates audit logs across 8 categories to provide transparency, accountability, and compliance visibility. Each log includes a `type` field that maps to one of the categories below.

***

### 1. Items / Inventory

#### Description

The **Items/Inventory** audit log records activity related to inventory items. Includes installation and deletion events across your endpoints.

#### Trigger Conditions

* A new item is **installed**.
* An item is **deleted**.

#### Fields

| Field       | Description                   | Example                                                                                         |
| ----------- | ----------------------------- | ----------------------------------------------------------------------------------------------- |
| `type`      | Always `Extensions`           | `"Extensions"`                                                                                  |
| `message`   | Human-readable event message  | `"Extension ms-vscode.PowerShell version 2024.2.2 installed on device Amits-MacBook-Pro.local"` |
| `extension` | Identifier (publisher + name) | `ms-vscode.PowerShell`                                                                          |
| `version`   | Version involved              | `2024.2.2`                                                                                      |
| `action`    | `installed` or `deleted`      | `installed`                                                                                     |
| `device`    | Device hostname               | `Amits-MacBook-Pro.local`                                                                       |
| `timestamp` | UTC timestamp (if available)  | `2025-08-29T09:45:00Z`                                                                          |

#### Event Actions

* **Installed** → item added.
* **Deleted** → item removed.

#### Sample Log

```json
{
  "type": "Extensions",
  "message": "Extension KevinRose.vsc-python-indent deleted from device h-MacBook-Pro-sl-Ity.local"
}
```

#### Interpretation Guidance

* Tracks which items users install or remove.
* Deletions may be user-initiated, policy-driven, or security responses.

***

### 2. Firewall

#### Description

The **Firewall** audit log captures actions where Koi blocks or hides risky items during searches or lookups in marketplaces.

#### Trigger Conditions

* End user searches the marketplace.
* Restricted items are blocked (mitigated).

#### Fields

| Field        | Description              | Example                                                            |
| ------------ | ------------------------ | ------------------------------------------------------------------ |
| `type`       | Always `Firewall`        | `"Firewall"`                                                       |
| `message`    | Event message            | `"Mitigated 105 extensions searched by Lirons-MacBook-Pro.local."` |
| `hostname`   | Originating device       | `"Lirons-MacBook-Pro.local"`                                       |
| `mitigated`  | Count of items blocked   | `105`                                                              |
| `created_by` | User initiating search   | `"lironkaykov"`                                                    |
| `searchTerm` | (Optional) Term searched | `"gpt"`                                                            |
| `timestamp`  | UTC timestamp            | `2025-08-29T10:02:00Z`                                             |

#### Event Actions

* **Mitigated (N)** → N items blocked during a search.

#### Sample Log

```json
{
  "type": "Firewall",
  "message": "Mitigated 11 extensions searched by Amits-MacBook-Pro.local.",
  "hostname": "Amits-MacBook-Pro.local",
  "mitigated": 11,
  "created_by": "amit",
  "searchTerm": "gpt"
}
```

#### Interpretation Guidance

* Large `mitigated` values = broad searches.
* `searchTerm` helps identify blocked queries.

***

### 3. Guardrails

#### Description

The **Guardrails** audit log tracks enablement and disablement of protection mechanisms. Guardrails are global safety nets (e.g., Scan-first protection, Malware protection).

#### Trigger Conditions

* A guardrail is **enabled**.
* A guardrail is **disabled**.

#### Fields

| Field        | Description                          | Example                                         |
| ------------ | ------------------------------------ | ----------------------------------------------- |
| `type`       | Always `Guardrails`                  | `"Guardrails"`                                  |
| `message`    | Event message                        | `"Guardrail Scan-first protection was enabled"` |
| `created_by` | Actor making the change (user/email) | `"itay@koi.security"`                           |
| `timestamp`  | UTC timestamp                        | `2025-08-29T11:30:00Z`                          |

#### Event Actions

* **Enabled** → Guardrail turned on.
* **Disabled** → Guardrail turned off.

#### Sample Log

```json
{
  "type": "Guardrails",
  "message": "Guardrail Malware protection was enabled",
  "created_by": "itay@koi.security"
}
```

#### Interpretation Guidance

* Enables/Disables reflect administrative configuration changes.
* Critical for compliance audits and rollback checks.

***

### 4. Notifications

#### Description

The **Notifications** audit log records when alerts, messages, or updates are sent to users or external integrations. These logs provide visibility into which recipients received notifications about policy violations, guardrails, remediations, or test alerts.

#### Trigger Conditions

* Malware protection alert sent.
* Guardrail or policy-triggered alert sent.
* Test alert/notification triggered (for validation).
* Notifications delivered to external systems (Slack, email, API endpoint).

#### Fields

| Field       | Description                                                   | Example                                                                |
| ----------- | ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`      | Always `Notifications`                                        | `"Notifications"`                                                      |
| `message`   | Human-readable event message describing notification          | `"Malware Protection notification sent to eitan@koi.security"`         |
| `recipient` | Target recipient (email or integration endpoint)              | `"eitan@koi.security"`                                                 |
| `context`   | Notification type or alert category (inferred from `message`) | `"Malware Protection"`, `"Test alerting for 'High Severity' findings"` |
| `timestamp` | \[If available] UTC timestamp of the log                      | `2025-08-29T12:15:00Z`                                                 |

#### Event Actions

* **Sent** → Notification successfully delivered.
* **Test Sent** → Test/broadcast message delivered.

#### Sample Log Entries

```json
{
  "type": "Notifications",
  "message": "Malware Protection notification sent to eitan@koi.security"
}
```

```json
{
  "type": "Notifications",
  "message": "notification sent to monitoring-extensioln-aaaaqqpsmf4gbxtqhusvdydp2u@phaidra-workspace.slack.com"
}
```

```json
{
  "type": "Notifications",
  "message": "Test alerting for 'High Severity' findings notification sent to yoni.shiloh@mobileye.com"
}
```

#### Interpretation Guidance

* Notifications confirm which recipients were informed of an event.
* Useful for auditing **alert coverage** (who was notified of a critical finding).
* Test alerts allow validation of notification pipelines without triggering real enforcement.
* Logs can be correlated with **Policies** and **Remediation** events to understand what action was taken and who was informed.

***

### 5. Remediation

#### Description

The **Remediation** audit log tracks when Koi automatically or manually removes risky items (extensions, add-ons, or packages) from endpoints.

#### Trigger Conditions

* A blocked item is forcibly uninstalled.
* An admin initiates a remediation task.
* A guardrail or policy automatically triggers remediation.

#### Fields

| Field                   | Description                                                   | Example                                                                   |
| ----------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `type`                  | Always `Remediation`                                          | `"Remediation"`                                                           |
| `user`                  | Username of actor who initiated or was subject to remediation | `"Itay"`                                                                  |
| `message`               | Human-readable event message                                  | `"Extension save-to-pocket version 4.0.6 remediated on device LT-IttayD"` |
| `hostname`              | Endpoint where remediation occurred                           | `"LT-ItayD"`                                                              |
| `extension.version`     | Version of the remediated item                                | `"4.0.6"`                                                                 |
| `extension.extensionId` | Unique ID of the remediated item                              | `"niloccemoadcdkdjlinkgdfekeahmflj"`                                      |
| `timestamp`             | \[If present] UTC timestamp                                   | `2025-08-29T13:20:00Z`                                                    |

#### Event Actions

* **Remediated** → Item forcibly removed.

#### Sample Log

```json
{
  "type": "Remediation",
  "user": "Itay",
  "message": "Extension save-to-pocket version 4.0.6 remediated on device LT-IttayD",
  "hostname": "LT-IttayD",
  "extension": {
    "version": "4.0.6",
    "extensionId": "niloccemoadcdkdjlinkgdfekeahmflj"
  }
}
```

#### Interpretation Guidance

* **Extension details** confirm what was removed.
* **Hostname** ties action to endpoint.
* **User** shows whether it was targeted or system-wide.
* Often correlates with **Guardrails** or **Policies**.

***

### 7. Settings

#### Description

The **Settings** audit log captures administrative and configuration changes in Koi. Includes user management, group creation, role assignments, invitations, and other system changes.

#### Trigger Conditions

* Group created/removed.
* User invited/deleted/role assigned.
* Risk score updated.
* Other configuration updates applied.

#### Fields

| Field        | Description                    | Example                     |
| ------------ | ------------------------------ | --------------------------- |
| `type`       | Always `Settings`              | `"Settings"`                |
| `message`    | Message describing the action  | `"Group created"`           |
| `created_by` | Actor who performed the action | `"itay@extensiontotal.com"` |
| `timestamp`  | \[If present] UTC timestamp    | `2025-08-29T14:10:00Z`      |

#### Event Actions

* **Group Created / Removed**
* **User Invited / Deleted / Role Assigned**
* **Risk Score Updated**
* **Other Configuration Updates**

#### Sample Log Entries

```json
{
  "type": "Settings",
  "message": "Group created",
  "created_by": "itay@extensiontotal.com"
}
```

```json
{
  "type": "Settings",
  "message": "Invited a new user to the system",
  "created_by": "itay@extensiontotal.com"
}
```

```json
{
  "type": "Settings",
  "message": "User updated a finding risk score",
  "created_by": "christopher.durgin@capitalone.com"
}
```

***

### 8. Policies

#### Description

The **Policies** audit log records the lifecycle of governance policies. It tracks when policies are created, updated, removed, or when their status changes.

#### Trigger Conditions

* Policy created.
* Policy removed.
* Policy status changed (enabled/disabled).
* Allowlist mode enabled.

#### Fields

| Field        | Description                          | Example                           |
| ------------ | ------------------------------------ | --------------------------------- |
| `type`       | Always `policies`                    | `"policies"`                      |
| `message`    | Message describing the policy action | `"Policy Block GPT Code created"` |
| `created_by` | Actor who performed the action       | `"amit@koi.security"`             |
| `timestamp`  | \[If present] UTC timestamp          | `2025-08-29T15:15:00Z`            |

#### Event Actions

* **Created**
* **Removed**
* **Status Changed**
* **Allowlist Mode Enabled**

#### Sample Log Entries

```json
{
  "type": "policies",
  "message": "Policy Block GPT Code created",
  "created_by": "amit@koi.security"
}
```

```json
{
  "type": "policies",
  "message": "Policy Block deprecated extensions removed",
  "created_by": "amit@koi.security"
}
```

```json
{
  "type": "policies",
  "message": "Policy Block Publisher Test status changed",
  "created_by": "christopher.durgin@capitalone.com"
}
```

```json
{
  "type": "policies",
  "message": "Allowlist mode enabled",
  "created_by": "itay@extensiontotal.com"
}
```

#### Interpretation Guidance

* Ensures full traceability for compliance.
* Shows evolution of governance (who created/removed what).
* Highlights enforcement changes.
* Allowlist mode = strict governance baseline..

***


---
