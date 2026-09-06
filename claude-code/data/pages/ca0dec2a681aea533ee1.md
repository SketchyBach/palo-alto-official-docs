---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/reference-docs/reference/system-diagnostics
fetched_at: 2026-09-06T10:49:35Z
source: cortex-platform
---

# System Diagnostics | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Reference Docs 

 Reference 

 Cortex XSOAR 6.12 EoL 

 System Diagnostics 

 Find and fix system performance issues in Cortex XSOAR 6.12. 

 The System Diagnostics page enables you to monitor and improve system performance and resilience. On the System Diagnostics page, you can view CPU and memory usage, the status of the Podman tool or Docker service, unusually large tasks, storage issues, etc. In some cases, the issue can be corrected within the System Diagnostics page. For issues that require more in depth troubleshooting, you can click through to a Knowledge Base article with more information and solutions. System Diagnostics thresholds can be customized . 

 You can view the System Diagnostics page at Settings → About → System Diagnostics . 

 A daily email is sent by default to all site administrators, notifying them of possible issues. If there are no issues, no email is sent. The following server configurations enable you to disable or modify email notifications. 

 Key 

 Value 

 diagnostics.notification.enabled 

 Default is true. False disables all system diagnostics email notifications. 

 diagnostics.notification.send.on.atRisk 

 Default is true. False disables notifications when status is at risk. 

 diagnostics.notification.send.to.default.admins 

 Default is true. False disables notifications to default administrators. 

 diagnostics.notification.send.to.roles 

 Default is "Administrator". Can be empty (no roles), or a list: "Role1, Role2, Role3." Will notify all users in the roles provided. If empty (no roles), default administrators will still receive notifications. 

 diagnostics.notification.hour.of.the.day 

 Default is 12. Format is HH. The hour of the day to send the notification email (server time). 

 (Multi-Tenant) To view System Diagnostics for hosts in a multi-tenant environment, go to Settings → Account Management → Hosts in the main host account. Each host has a Diagnostics page. You can also view information about CPU, Storage, and Memory usage for each tenant account on the host. 

 You can also use the getSystemDiagnostics command to create a JSON output of this data. If you have an open support ticket related to system performance, you can attach the output of this command to the ticket to provide Cortex XSOAR Customer Support with relevant information. Use the associated verbose argument to return additional information, for example, the specific IDs of incidents that have big context data. 

 Previous Widget Server Configurations 

 Next Fix System Diagnostics Issues 

 Last updated 3 days ago 

 Was this helpful?
