---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas-releases/cortex-xsoar-8-saas-releases.md
fetched_at: 2026-09-16T09:12:47Z
source: cortex-platform
---

# Cortex XSOAR 8 SaaS Releases

> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas-releases/cortex-xsoar-8-saas-releases.md).

# Cortex XSOAR 8 SaaS Releases

Major general availability releases for Cortex XSOAR 8 SaaS.

All releases below are general availability releases for Cortex XSOAR 8 SaaS.

{% updates format="full" %}
{% update date="2026-07-26" %}

## 8.15

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-this-release/july-2026.md)

* **Azure external storage support for incident export:** Export Cortex XSOAR incident data, including war room entries and attachments, directly to Azure Blob Storage to maintain cloud compliance. Available to XSOAR 8 SaaS customers at no additional charge.
* **Continuous Strata logging authentication:** Maintain uninterrupted data logging across commercial and FedRAMP Moderate environments. The platform now automatically manages secure background authentication for the Strata Logging Service, ensuring continuous data flows.
  {% endupdate %}

{% update date="2026-05-03" %}

## 8.14

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2026/may-2026.md)

* **Multi-tenant support for child-tenant name changes:** Simplify tenant management by renaming child tenants directly in the Cortex Gateway. You now have the flexibility to ensure tenant names consistently reflect current business requirements, maintaining operational clarity across large-scale SOC deployments.
* **Organized content management:** Easily distinguish between your custom work and content pack items with a dedicated workspace for each. To ensure a cleaner view, we moved all content pack items to the Content Pack Items page, while the Content Items page is now reserved exclusively for your custom creations.
* **Enhanced audit logs:** Gain full visibility and meet compliance requirements with expanded auditing for notification forwarding and content management. You can now track configuration changes for notifications and high-stakes content lifecycle events, such as pushing content to production, directly within the Management Audit log.
  {% endupdate %}

{% update date="2026-01-25" %}

## 8.13

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2026/february-2026.md)

* **Contextual playbook documentation:** We have introduced Info Mode to the playbook editor, allowing you to view detailed task and section descriptions directly within your workflow.
* **New Rapid Response Playbook:** Automate the detection and mitigation of CVE-2025-59287, a critical remote code execution vulnerability in Microsoft Windows Server Update Services (WSUS) caused by insecure deserialization.
* **Improve playbook unlocking:** Ensure your team can edit their automation workflows with automatic or manual playbook unlocking. The system now clears locks immediately when a user logs out or when a session expires.
  {% endupdate %}

{% update date="2025-11-09" %}

## 8.12

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2025/november-2025.md)

* **Conflict-free playbook:** Prevent concurrent playbook editing with this enhancement, ensuring your team can build and modify automation workflows without conflicts.
* **Unique task logos:** Boost clarity, quickly distinguish between integration commands, custom scripts, and system actions with playbook tasks that display unique logos and content pack indicators.
* **Unit 42 Threat Intelligence content pack:** A new Unit 42 content pack provides high-value integrations that leverage Unit 42’s world-class threat intelligence, research, and analysis, replacing several deprecated packs (like AutoFocus and Unit 42 ATOMs Feed). To complete this migration, configure the new Unit 42 Feed and Enrichment integrations, update all related playbooks, and disable the old integrations.
  {% endupdate %}

{% update date="2025-07-20" %}

## 8.11

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2025/july-2025.md)

* **Advanced search for playbooks and scripts:** Easily find and use existing scripts and playbooks by searching for specific text within scripts or by searching the names of scripts, tasks, and third-party integrations within playbooks.
* **Clear incidents waiting in the ingestion queue:** Regain control during incident floods, ensure critical playbooks run smoothly, prevent bottlenecks, and facilitate rapid self-recovery.
* **Generic Webhook integration enhancements:** Easily ingest external data without an API integration and connect with diverse services with support for header-based authentication and a simplified setup experience.
  {% endupdate %}

{% update date="2025-04-27" %}

## 8.10

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2025/april-2025.md)

* **Automatically export incidents:** For customers who need to store incidents beyond their retention period, XSOAR can automatically export incidents to external storage, enabling indefinite retention and continued access to historical incident data.
* **Support for additional Cortex XSOAR APIs:** The expanded API support enables organizations to reset the ROI widget, update existing lists, get a list, upload files, and clone playbooks so they can better fine-tune automated incident workflows and integrations.
  {% endupdate %}

{% update date="2025-02-02" %}

## 8.9

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2025/february-2025.md)

* **A new look and feel for playbooks:** The latest enhancements in user experience improve playbook readability and clarity through an updated look and feel.
* **Collapsible playbook sections:** The updated collapsible playbook sections enable users to stay focused on the relevant playbook details without distractions, allowing for easier navigation through complex playbooks and increased productivity.
* **Unlimited user license for development tenants:** With no license limit for users on development tenants, you can build, test, and refine automations at scale. This drives faster innovation, more reliable workflows, and scalable solutions as your organization grows.
* **Notifications for deprecated content:** New automated user notifications about deprecated playbooks, sub-playbooks, and scripts ensure updated, effective, and accurate security workflows.
  {% endupdate %}

{% update date="2024-09-22" %}

## 8.8

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2024/september-2024.md)

* **Canvas - Multilayer indicator/incident relationship graph:** SOC analysts can now create and share dynamic attack diagrams or static snapshots with incident response, forensics, and threat-hunting teams.
* **The Guard Rails page:** Cortex XSOAR 8 now includes the Guard Rails page, which shows performance-related errors and warnings that can be used as a guide to detect and prevent actions that may cause a decline in performance or instability.
* **Exclude enrichment of indicators:** Indicators can now be marked as Enrichment Excluded in Cortex XSOAR, ensuring they will not be enriched. This gives you better control over your Indicators and the ability to optimize system performance by managing the indicator enrichment process.
* **Audit logs:** Audit log coverage is expanded to capture detailed records of incident edits, including the modified fields. This improvement ensures a comprehensive record of all changes, significantly enhancing the ability to trace the incident's history and evolution.
  {% endupdate %}

{% update date="2024-06-30" %}

## 8.7

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2024/june-2024.md)

* Seamlessly migrate all your data, configurations, and settings, including indicators and incidents from Cortex XSOAR 6.13 On-prem to Cortex XSOAR 8 Cloud using a built-in wizard streamlining the migration process.
* To effectively investigate an incident and analyze associated indicators, the SOC analyst must have access to up-to-date data and a clear view of the most recent changes made to the relevant indicators, as well as the initial entries of indicator changes.
* When generating a report, you can choose the timezone to ensure accurate and localized reporting for users working in multiple geographical locations.
* Admin users can manage notification distribution by adding or removing tenant’s stakeholders' email addresses on the Server Settings page without the need to add them first on the tenant. This feature streamlines communication and simplifies administration.
  {% endupdate %}

{% update date="2024-04-14" %}

## 8.6

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2024/april-2024.md)

* You can create API keys with multiple roles to improve operational efficiency and allow dynamic RBAC management of API keys.
* The Administrator can restrict designated users' access to specific dashboards through role assignment.
* Cortex XSOAR has an API endpoint for GET, CREATE, UPDATE, and DELETE for API keys.
* You can change the color of the favicon for each tenant, which allows you to identify which tenant is being used in each tab at a glance.
  {% endupdate %}

{% update date="2024-02-11" %}

## 8.5

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2024/february-2024.md)

* **Enable communication between SOC analysts (MT/MSSP)**
* **Keep Retained Incidents**
* **Assign retention licenses for MT deployments**
* **Content repository improvements**
* **Customize system emails**
* **Use an authenticated Docker image**
  {% endupdate %}

{% update date="2023-10-29" %}

## 8.4

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2023/october-2023.md)

* **In-app documentation**
* **Private repository support in a dev/prod environment**
* **Export incidents to Excel**
* **Authenticated communication tasks**
* **Define credentials for long-running integrations**
* **SSO improvements**
  {% endupdate %}

{% update date="2023-07-09" %}

## 8.3

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2023/july-2023.md)

* **Improved Auditing**
* **Manage User Groups in the Cortex Gateway**
* **Manage RBAC settings in the Cortex Gateway**
* **Improved Navigation**
* **Improved Indicator Verdict Calculation**
  {% endupdate %}

{% update date="2023-04-23" %}

## 8.2

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2023/april-2023.md)

* XSOAR 8 now offers Cortex XSOAR multi-tenant, designed for managed security service providers and enterprises requiring strict data segregation with the flexibility to share and manage critical security practices across tenant accounts.
* Role permissions have been updated to separate some administration permissions.
* You can now subscribe to content pack updates in Marketplace.
* Improved UI for Data Collection and Ask tasks in Playbooks, and a simplified search for playbooks with free text search.
* Improvements to the Default Playbook.
  {% endupdate %}

{% update date="2023-01-01" %}

## 8.1

[**General Availability**](/cortex-xsoar-8-saas-release-notes/features-introduced-in-previous-releases/features-introduced-in-2023/january-2023.md)

* **Integration into the Cortex platform:**
  * **Improved performance and reliability**
  * **High scalability based on a revamped architecture that utilizes cloud features**
  * **Built-in Git Repository for sharing data between development and production instances**
    {% endupdate %}
    {% endupdates %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas-releases/cortex-xsoar-8-saas-releases.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
