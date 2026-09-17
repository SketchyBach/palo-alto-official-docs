---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/administration/monitor-enterprise-dlp/view-enterprise-dlp-audit-logs/view-enterprise-dlp-audit-logs-on-cloud-management.html
fetched_at: 2026-09-16T13:01:44Z
source: palo-alto-main
---

# View Enterprise DLP Audit Logs on Strata Cloud Manager Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 View Enterprise DLP Audit Logs 

 View Enterprise DLP Audit Logs on Strata Cloud Manager 

 Download PDF 

 Enterprise DLP 

 View Enterprise DLP Audit Logs on Strata Cloud Manager 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 View Enterprise DLP Audit Logs on Strata Cloud Manager 

 Use Enterprise Data Loss Prevention (E-DLP) audit logs to understand the change history for your Enterprise DLP deployment. 

 Log in to 
 Strata Cloud Manager . 

 ( Optional ) Configure syslog forwarding for Enterprise DLP audit logs. 

 Select Configuration Data Loss Prevention Audit Log . 

 ( Optional ) Filter Enterprise DLP audit logs as needed. 

 Enter an email in the search bar to filter the audit logs by
 user. 

 Add New Filter to filter the Enterprise DLP audit logs based on: 

 Time —Select a predefined time frame or
 specify a Custom time frame. For the
 predefine time frame, you can select Past 60
 Minutes , Past 24
 Hours , Past 7 Days ,
 Past 30 Days , or
 All 

 Channel —Select the security
 enforcement point where the change occurred. You can select
 Enterprise DLP ,
 NGFW ,
 Prisma Access ,
 SaaS Security ,
 and Strata Cloud Manager . 

 Event —Select the type of audit log
 event to view. You can select Create ,
 Update , and
 Delete . 

 Click View Details to see detailed information about a
 specific audit log. 

 You can view additional audit log details to better understand what changes
 in your Enterprise DLP configuration. When you update an existing data
 pattern, data profile, or other Enterprise DLP configuration object,
 Enterprise DLP highlights in red what the security admin deleted
 and highlights in green what the security admin added or changed. 

 Enterprise DLP generates an audit log when a data security
 administrator: 

 Create 

 Creates a new data
 pattern . 

 Creates a new data
 profile . 

 Creates a new custom
 document type . 

 Creates a new data dictionary 

 Uploads a new EDM
 dataset . 

 Enables Optical Character
 Recognition (OCR) . 

 Adds an Endpoint DLP peripheral
 device . 

 Creates an Endpoint DLP policy
 rule . 

 Creates an incident automation rule for Automatic Case
 Management . 

 Creates a new Log Forwarding Profile and Syslog Server
 Profile for Syslog
 Forwarding . 

 Creates a new Syslog Server Profile for Syslog
 Forwarding . 

 Enables ICAP Forwarding .

 Read 

 Views a data
 pattern . 

 Views a data
 profile . 

 Accesses an Enterprise DLP or Email incident incident and
 views the associated snippet. 

 Enterprise DLP generates an audit log when view
 viewing Email DLP incident snippet from Configuration Data Loss Prevention Audit Log . 

 Accesses a Data Security (SaaS API) incident and views
 the associated snippet. 

 Enterprise DLP generates an audit log when view
 viewing Email DLP incident snippet from Configuration SaaS Security Data Security Incidents Data Asset Incidents . 

 Accesses the Data Asset Explorer asset details and
 views the associated snippet. 

 Exports one or more
 data
 patterns , data
 profiles , custom
 document types , data dictionaries , or EDM
 datasets. 

 Exports all Enterprise DLP data patterns, data profiles,
 custom document types, data dictionaries, or EDM datasets . 

 Update 

 Edits the data
 filtering settings. 

 Edits the snippet
 settings. 

 Updates a data pattern. 

 Clones a data pattern. 

 Updates a data
 profile 

 Clones a data profile. 

 Tests a data
 profile. 

 Updates a DLP rule .

 Updates an Endpoint DLP peripheral
 device . 

 Updates an Endpoint DLP policy
 rule . 

 Updates an existing
 custom document type. 

 Updates an existing data
 dictionary. 

 Updates 
 an EDM dataset. 

 Updates an incident automation rule for Automatic Case
 Management . 

 Updates a Log Forwarding Profile and Syslog Server Profile
 for Syslog
 Forwarding . 

 Updates a new Syslog Server Profile for Syslog
 Forwarding . 

 Updates the ICAP Forwarding 
 configuration. 

 Renames a
 custom data pattern. 

 Archives 
 a custom data pattern. 

 Restores 
 a custom data pattern. 

 Delete 

 Disables any of the following data filtering settings: 

 File Based Settings — Log Files
 Not Scanned 

 Non-File Based Settings — Enable
 non-file based DLP and
 Log Data Not Scanned 

 Deletes a custom document type. 

 Deletes a data dictionary. 

 Deletes an EDM dataset 

 Disables Optical Character Recognition (OCR). 

 Deletes an incident automation rule for Automatic Case
 Management . 

 Deletes a Log Forwarding Profile and Syslog Server Profile
 for Syslog
 Forwarding . 

 Deletes a new Syslog Server Profile for Syslog
 Forwarding . 

 Disables ICAP Forwarding .
