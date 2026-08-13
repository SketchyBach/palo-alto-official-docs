---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/post-deployment/data-and-log-forwarding/forward-logs-and-data-from-cortex-xsiam-to-external-services/set-up-email-notifications-for-tenant-updates
fetched_at: 2026-08-13T14:14:07Z
source: cortex-platform
---

# Set up email notifications for tenant updates | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Set up email notifications for tenant updates | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Post-deployment checklist 

 Perform health checks 

 Cortex Marketplace 

 Manage user roles and access management 

 Dashboards and reports 

 Configure server settings 

 Configure security settings 

 Data and log forwarding 

 Forward logs and data from Cortex XSIAM to external services 

 Configure external applications for forwarding 

 Configure notification forwarding 

 Set up email notifications for tenant updates 

 Monitor administrative activity 

 Data and log notification formats 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Onboard Cortex XSIAM 

 Post-deployment 

 Data and log forwarding 

 Forward logs and data from Cortex XSIAM to external services 

 Set up email notifications for tenant updates 

 Your Cortex tenant generates Management Audit Logs throughout the tenant update lifecycle. This includes version upgrades and hotfixes, covering both the pending (before) and completed (after) phases of a scheduled update. 

 Using log forwarding, you can automatically receive an email whenever one of these events occurs, ensuring your team is notified the moment a change is scheduled or completed on your tenant. 

 Prerequisites 

 Ensure you have the following: 

 Admin privileges on the tenant. 

 The email distribution list that will receive the notifications. 

 Your tenant name (for example., acme-corp.us) to include in the email subject for easy identification. 

 How audit events are structured 

 Every forwarding rule is built by matching key fields from the Management Audit Log: 

 Field 

 What it tells you 

 Values to filter on 

 Type 

 The domain that produced the event. 

 Tenant Management 

 Subtype 

 The exact phase of the lifecycle. 

 Upgrade Pending, Upgrade Completed, Hotfix Pending, Hotfix Completed 

 Description 

 Human-readable summary of the event. 

 Contains the word downtime when downtime is involved. This enables you to build targeted rules that run only when downtime is expected. 

 How to set up email notifications for tenant updates 

 Go to Settings → Configurations → General → Notifications → + Add Forwarding Configuration . 

 In the Define step, set the forwarding configuration details. 

 Enter a name for the configuration. 

 For Log Type , select Management Audit Logs . 

 (Optional) Enter a description of the forwarding configuration. 

 Click Next . 

 In the Scope step, filter which issues, cases, or logs you want included in a notification and then click Next .
For example, for a filter set to Severity = Medium, Category = Configuration, Cortex XSIAM sends the issues or events matching this filter as a notification. 

 In the Forward Destination step, define the destination details. 

 Select the Notification Timezone . 

 Under the Add Application dropdown, enable one or more integrations. 

 Enable Email . 

 Enter the recipients in the Email distribution list field. 

 Set the Grouping timeframe to 1 minute .
A one minute timeframe ensures pre-upgrade and pre-hotfix warnings arrive in time to be actionable without unnecessary delays. 

 Clear the Use Auto Generated Subject checkbox.
Writing a custom subject that includes your tenant name and the event type (for example, <tenant_name> tenant - Pre-upgrade warning) enables recipients to instantly identify the affected tenant. 

 Enter your custom subject and add the Filter / Conditions for your specific use case from the use case configurations table below. 

 Click Create . 

 Use case configurations 

 The following table provides subject lines and filter conditions for your notification needs. For all rules below, the Entity condition must be set to Tenant Management . 

 Use case 

 When the email is sent 

 Email recipients 

 Custom email subject 

 Additional filter conditions 

 All upgrade and hotfix events 

 Any upgrade/hotfix event occurs. 

 Compliance and audit teams needing a complete record. This is the simplest approach. 

 <tenant_name> tenant - Upgrade/Hotfix audit log 

 (None) 

 Pre-upgrade warning 

 An upgrade is about to begin (~10-min warning). 

 Operations teams needing to prepare. 

 <tenant_name> tenant - Pre-upgrade warning 

 Subtype contains Upgrade Pending 

 Post-upgrade completion 

 An upgrade has successfully completed. 

 Anyone tracking version changes. 

 <tenant_name> tenant - Upgrade completed 

 Subtype contains Upgrade Completed 

 Pre-hotfix warning 

 A hotfix is about to be deployed (~10-min warning). 

 Operations teams needing to prepare. 

 <tenant_name> tenant - Pre-hotfix warning 

 Subtype contains Hotfix Pending 

 Post-hotfix completion 

 A hotfix has been successfully deployed. 

 Anyone tracking deployments. 

 <tenant_name> tenant - Hotfix completed 

 Subtype contains Hotfix Completed 

 Any event with downtime 

 An upgrade or hotfix requires downtime. 

 On-call and SRE teams tracking service interruptions. 

 <tenant_name> tenant - Upgrade/Hotfix with downtime 

 Description contains downtime 

 Example configurations: 

 description contains downtime 

 type = Tenant Management 

 subtype contains upgrade 

 OR 

 description contains downtime 

 type = Tenant Manage 

 Manage and test your rules 

 View all rules: Go to Settings → Configurations → General → Notifications . Each forwarding configuration is listed with its log type, destination, and status. 

 Edit or pause notifications: Open any rule to change recipients, adjust filters, or toggle it on/off. 

 Verify the notification is sent: The next time an upgrade or hotfix occurs, confirm the expected email arrives. You can also check the event in Settings → Management Audit Logs . 

 Audit log retention: All audit events are retained for 365 days, enabling you to review historical events in the Management Audit Logs table even if you miss an email. 

 Frequently asked questions 
 Should I create one general rule or several specific ones? 

 If you need a complete record, the use case for all upgrade and hotfix events is the simplest approach. Create individual pre-event and post-event rules only if you need to route specific phases to different teams (for example, warnings to on-call engineers or completions to compliance). 

 Can I forward these logs to other destinations? 

 Yes. You can route Management Audit Logs to a Syslog receiver by changing the destination to Syslog during setup. The filter configurations remain exactly the same. 

 Why does the time in the email differ from the tenant UI? 

 The tenant UI displays times based on your tenant timezone server setting. Forwarded emails use UTC to provide an unambiguous timestamp for all recipients. 

 Previous Configure notification forwarding Next Monitor administrative activity 

 Last updated 22 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 How audit events are structured 

 How to set up email notifications for tenant updates 

 Use case configurations 

 Manage and test your rules 

 Frequently asked questions 

 Was this helpful?
