---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/sharepoint-site-collection-admin-group-addition
fetched_at: 2026-09-06T11:07:35Z
source: cortex-platform
---

# SharePoint Site Collection admin group addition | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 SharePoint Site Collection admin group addition 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 N/A (single event) 

 Deduplication Period 

 1 Day 

 Required Data 

 Office 365 Audit 

 Detection Modules 

 Identity Threat Module, SaaS Threat Detection 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Account Manipulation: Additional Cloud Roles (T1098.003) 

 Severity 

 Informational 

 Description 

 A user made an addition to the site collection administrators group in SharePoint. 

 Attacker's Goals 

 Elevate permissions and establish persistence. 

 Investigative actions 

 Check the IP address from which the access originated. 

 Verify the activity with the performing user. 

 Follow further actions done by the account. 

 Variations 
 SharePoint site collection admin added to personal site 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Account Manipulation: Additional Cloud Roles (T1098.003) 

 Severity 

 Informational 

 Description 

 A user was added as a site collection admin to a personal site, indicating that the user has accessed the SharePoint service for the first time. 

 Attacker's Goals 

 Elevate permissions and establish persistence. 

 Investigative actions 

 Check the IP address from which the access originated. 

 Verify the activity with the performing user. 

 Follow further actions done by the account. 

 Abnormal SharePoint Site Collection admin group addition 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Account Manipulation: Additional Cloud Roles (T1098.003) 

 Severity 

 Low 

 Description 

 A user made an addition to the site collection administrators group in SharePoint. This user has not made any SharePoint site admin additions over the past 30 days. 

 Attacker's Goals 

 Elevate permissions and establish persistence. 

 Investigative actions 

 Check the IP address from which the access originated. 

 Verify the activity with the performing user. 

 Follow further actions done by the account. 

 Previous Setuid and Setgid file bit manipulation 

 Next Short-lived Azure AD user account 

 Was this helpful?
