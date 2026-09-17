---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/role-based-access-control/inventory-agent-permissions/host-firewall
fetched_at: 2026-09-16T08:37:40Z
source: cortex-platform
---

# Host Firewall | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Inventory - Agent permissions 

 Cortex XSIAM 

 Host Firewall 

 Configure host firewall rules and review firewall events in Cortex XSIAM. 

 Provides endpoint-level network protection, such as defining inbound and outbound firewall rules and creating application-based rules in the Host Firewall page ( Inventory → Endpoints → Host Firewall) . Users can also Collect Detailed Host Firewall Logs from Inventory → Endpoints → Endpoint Control . 

 Caution 

 Misconfigured firewall rules can block legitimate traffic or allow malicious connections. Implement change management processes and test rules before deployment. 

 Permissions 

 Description 

 Roles Example 

 None 

 Cannot view the Host Firewall page, which includes firewall pages, firewall rules, and events, or Collect Detailed Host Firewall Logs. 

 View 

 View the Host Firewall menu, which includes read-only access for Rule Groups and Host Firewall Events. 

 SOC Tier-1 Analyst: Firewall rules may provide context for network-related alerts. Helpful when triaging blocked connection issues. 

 SOC Tier-2 Analyst: Understanding firewall rules is important for investigating network-based threats. Critical for lateral movement investigations 

 Threat Hunter: Firewall rules help understand network protection posture for hunting. Hunters need to know what network traffic is allowed/blocked. 

 View/Edit 

 All view capabilities, plus creating, editing, deleting, and enabling Host Firewall Rules Groups, and managing Host Firewall Events. Also can Collect Detailed Host Firewall Logs . 

 SOC Tier-3 Analyst: May need for emergency containment (blocking malicious IPs), but should require approval and documentation. 

 Security Engineer: Responsible for firewall rule development and maintenance. Creates and optimizes firewall policies. 

 Required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Agent Groups 

 View 

 Required. Must understand group structure to target firewall rules correctly. Incorrect targeting can block legitimate traffic or allow malicious connections. 

 Agent Extension Policies 

 View 

 Required. Host Firewall profiles are managed through extension policies. Without extension policy visibility, firewall rule changes may conflict with profile settings. 

 Agent Administrations 

 View 

 Strongly Recommended. View endpoints to understand firewall rule deployment and correlate firewall events with endpoint data. 

 Network Configuration 

 View 

 Strongly Recommended. Network topology context is essential for designing effective firewall rules. Understanding network zones prevents blocking legitimate traffic. 

 Cases & Issues 

 View 

 Strongly Recommended. Review security events to inform firewall rule decisions. Understanding attack patterns helps create effective rules. 

 Previous Agent Installations 

 Next Device Control 

 Last updated 20 days ago 

 Was this helpful?
