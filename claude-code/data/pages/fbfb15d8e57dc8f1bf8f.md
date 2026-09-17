---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/administration/monitor-enterprise-dlp/view-enterprise-dlp-audit-logs/view-enterprise-dlp-push-logs-for-endpoint-dlp.html
fetched_at: 2026-09-16T13:01:44Z
source: palo-alto-main
---

# View Enterprise DLP Push Logs for Endpoint DLP Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 View Enterprise DLP Audit Logs 

 View Enterprise DLP Push Logs for Endpoint DLP 

 Download PDF 

 Enterprise DLP 

 View Enterprise DLP Push Logs for Endpoint DLP 

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

 View Enterprise DLP Push Logs for Endpoint DLP 

 View the Enterprise Data Loss Prevention (E-DLP) push logs for Endpoint DLP. 

 Log in to 
 Strata Cloud Manager . 

 ( Optional ) Configure syslog forwarding for Enterprise DLP audit logs. 

 Select Configuration Data Loss Prevention Audit Log Push Logs . 

 Review your Endpoint DLP Push Logs. 

 Time —Date and time the Endpoint DLP policy push was performed.
 Timestamp is in MM/DD/YY hh:mm 
 format. 

 User —Email of the administrator that performed the Endpoint
 DLP policy push. 

 Request ID —ID of the policy push operation from Strata Cloud Manager to Prisma Agent installed on
 endpoint devices. The Request ID is used for troubleshooting in the
 event you push Endpoint DLP changes but the Prisma Agent doesn't take the expected Endpoint DLP policy rule 
 action. 

 Event —Status of the Endpoint DLP policy rule and configuration
 push. For a successful push, the Event column displays
 Endpoint DLP Policy/Configuration pushed
 successfully . For a failed push, the Event column
 displays Endpoint DLP Policy/Configuration
 failed . 

 Click View Details to review detailed
 information about a specific Endpoint DLP policy rule and
 configuration push. 

 Review detailed information about a specific Endpoint DLP policy rule and
 configuration push. 

 Status —Status of the push operation; can be
 Success or
 Failure . 

 Start Time —Date and time the push operation was initiated.
 Timestamp is in MM/DD/YY hh:mm 
 format. 

 End Time —Date and time the push operation completed regardless
 of status. Timestamp is in MM/DD/YY
 hh:mm format. 

 Description —Description for the push operation added by the
 security administrator. This field is blank if description was added
 when the push was initiated. 

 Request ID —ID of the policy push operation from Strata Cloud Manager to Prisma Agent installed on
 endpoint devices. The Request ID is used for troubleshooting in the
 event you push Endpoint DLP changes but the Prisma Agent doesn't take the expected Endpoint DLP policy rule 
 action. 

 Policies —List of new or modified Endpoint DLP policy rules 
 included in the push. 

 Peripherals —List of peripheral
 devices added to Endpoint DLP. 

 Peripheral Groups —List of newly created or modified peripheral groups . 

 Settings —List of Endpoint DLP data filtering and snippet setting
 changes.
