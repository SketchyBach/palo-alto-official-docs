---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/role-based-access-control/investigation-and-response-permissions/search-permissions/forensics-permissions
fetched_at: 2026-09-06T09:46:46Z
source: cortex-platform
---

# Forensics permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Investigation and Response permissions 

 Search permissions 

 Cortex XDR 5.x 

 Forensics permissions 

 Configure permissions for forensics. 

 Controls access to Forensics ( Investigation & Response → Forensics ). Forensic investigations streamline your case response, data collection, threat hunting, and analysis of your endpoints. 

 Notice 

 You need the Forensics add-on to view Forensic investigations. 

 For more information, see Forensic investigations . 

 Permission 

 Description 

 Roles Example 

 None 

 Users cannot see forensic artifacts or trigger new collections. 

 View 

 Read-only access to forensics investigations 

 SOC Tier-1 Analyst: View forensics data for context, but cannot initiate collections. 

 SOC Tier-2 Analyst: View forensics data and escalate to Tier-3 for collections. 

 Security Engineer: View forensics for understanding data as not the primary function. 

 View/Edit 

 Full read and write access, including create, edit, and delete investigations, start, pause, and delete threat hunts. 

 SOC Tier-3 Analyst: Full forensics capabilities, including triage and hunt. 

 Threat Hunter: Full forensics for deep-dive investigations. 

 Required and recommended Permissions 

 Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Agent Administrations 

 View 

 Forensics displays endpoint data extensively. Without this, endpoint information within forensics investigations will fail to load or show errors. Required. 

 Query Center 

 View 

 Strongly recommended to run queries on the host data. 

 Cases & Issues 

 View 

 Strongly recommended to view issues associated with forensic investigations. 

 Previous Query Center permissions 

 Next Host Insights permissions 

 Last updated 5 days ago 

 Was this helpful?
