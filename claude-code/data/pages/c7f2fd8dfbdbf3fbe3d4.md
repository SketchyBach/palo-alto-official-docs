---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/role-based-access-control/threat-management-permissions/threat-intelligence-permissions
fetched_at: 2026-09-06T09:47:00Z
source: cortex-platform
---

# Threat Intelligence permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Threat Management permissions 

 Cortex XDR 5.x 

 Threat Intelligence permissions 

 Configure permissions for Threat Intelligence. 

 Located under Threat Management → Threat Intelligence , these permissions govern how your organization interacts with indicators (IPs, URLs, Domains, Hashes) and intelligence feeds. It allows you to transform raw data from sources like Unit 42 or AlienVault into actionable security logic. 

 This feature requires the Extended Threat Intelligence (XTI) security add-on. 

 For more information, see Extended Threat Intelligence . 

 Component 

 Description 

 None 

 No access to the Threat Intel Library, Indicators and Threat Intel Dashboard. 

 View 

 Users can search the Threat Intel Library and Indicators, and view the Threat Intel Dashboard. 

 View/Edit 

 Full control to manage indicators and indicator rules. 

 Required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission level 

 Reason 

 Cases & Issues 

 View 

 Strongly recommended. Indicator enrichment data appears in case artifacts, and editing indicators from case context requires case access. 

 Detection Rules 

 View/Edit 

 Strongly Recommended. Enables creating indicator rules directly from indicators. 

 Query Center 

 View/Edit 

 Enables investigating indicators via XQL queries. Essential for validating indicator impact before creating rules or blocking. 

 Previous Detection Rules permissions 

 Next Exceptions Configuration permissions 

 Last updated 5 days ago 

 Was this helpful?
