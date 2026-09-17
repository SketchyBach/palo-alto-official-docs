---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/multi-tenant/incident-management-on-the-main-tenant
fetched_at: 2026-09-16T08:52:42Z
source: cortex-platform
---

# Incident management on the Main Tenant | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 SaaS Documentation 

 Multi-Tenant 

 Cortex XSOAR 8 (SaaS) 

 Incident management on the Main Tenant 

 Manage Cortex XSOAR 8 SaaS incidents across child tenants from the main tenant in a multi-tenant deployment. 

 On the main tenant, you can create and make changes to content such as dashboards, incidents, and indicators, and propagate content to child tenants. You can view data from all your child tenants or pivot to each tenant to take certain actions. 

 On the Incidents page, you view and take action on incidents across all tenants. You can do the following: 

 Action 

 Description 

 Investigate an incident 

 When clicking on an incident you pivot to the child tenant where you take action on the incident. You can view a detailed summary, take action on the incident, add evidence, related incidents, etc. For more information about these actions, see Investigate an incident . 

 Edit an incident 

 Edit system fields such as name, owner, severity, and custom fields. When you save the changes they are propagated to the child tenant. 

 Run a command 

 Sometimes you may need to run a command across all tenants. For more information, see Run a command on multiple tenants . 

 Retention 

 You can mark multiple incidents for permanent retention, including incidents that have been deleted manually, by API call, and deleted per the Retention Policy of six months plus any additional incident retention licenses assigned to the tenant. 

 Export an incident 

 You can export to a CSV file. By default, the CSV file is generated in UTF8 format. 

 Close/delete 

 Close or delete an incident. 

 For more information about incident management generally in Cortex XSOAR, see Incident Management . 

 You can't create incidents on the main tenant. 

 Although you can't investigate incidents directly, you can pivot to the incident on the child tenant by clicking the incident. You can also go to the child tenant's incident page by clicking Main Tenant (top left of the window) and selecting the relevant child tenant. 

 By default, the Incidents page displays open incidents (from all child tenants) in the last seven days. You can filter this by changing the date and selecting the relevant tenant. 

 Previous Manage content using a remote repository 

 Next Manage main tenant users in an investigation 

 Last updated 14 days ago 

 Was this helpful?
