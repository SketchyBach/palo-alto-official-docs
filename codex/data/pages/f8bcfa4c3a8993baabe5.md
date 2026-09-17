---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/outbound-email-contains-file-sharing-service-link-sent-to-external-recipient
fetched_at: 2026-09-16T09:07:43Z
source: cortex-platform
---

# Outbound email contains file-sharing service link sent to external recipient | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Outbound email contains file-sharing service link sent to external recipient 

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

 1 Hour 30 Minutes 

 Required Data 

 Microsoft 365 Emails 

 Detection Modules 

 Email 

 Detector Tags 

 Exfiltration 

 ATT&CK Tactic 

 Execution (TA0002), Credential Access (TA0006) 

 ATT&CK Technique 

 User Execution (T1204), Brute Force: Password Cracking (T1110.002) 

 Severity 

 Informational 

 Description 

 Identifies outbound emails that include links to file-sharing services sent externally. 

 Attacker's Goals 

 Exfiltrate data by sharing a link to a file-sharing service with external recipients, bypassing attachment inspection and potentially evading visibility controls. 

 Investigative actions 

 Review the shared URL to determine if the file is publicly accessible or shared outside the organization. 

 Check if the file-sharing domain has been previously used by this sender or others in the organization. 

 Investigate recent outbound emails for similar use of file-sharing services or unusual external recipients. 

 Variations 
 Outbound email to external recipient(s) uses first-seen for organization file-sharing service 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Execution (TA0002), Credential Access (TA0006) 

 ATT&CK Technique 

 User Execution (T1204), Brute Force: Password Cracking (T1110.002) 

 Severity 

 Informational 

 Description 

 Identifies outbound emails that include links to file-sharing services sent externally. 

 Attacker's Goals 

 Exfiltrate data by sharing a link to a file-sharing service with external recipients, bypassing attachment inspection and potentially evading visibility controls. 

 Investigative actions 

 Review the shared URL to determine if the file is publicly accessible or shared outside the organization. 

 Check if the file-sharing domain has been previously used by this sender or others in the organization. 

 Investigate recent outbound emails for similar use of file-sharing services or unusual external recipients. 

 Outbound email to external recipient(s) uses first-seen for sender file-sharing service 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Execution (TA0002), Credential Access (TA0006) 

 ATT&CK Technique 

 User Execution (T1204), Brute Force: Password Cracking (T1110.002) 

 Severity 

 Informational 

 Description 

 Identifies outbound emails that include links to file-sharing services sent externally. 

 Attacker's Goals 

 Exfiltrate data by sharing a link to a file-sharing service with external recipients, bypassing attachment inspection and potentially evading visibility controls. 

 Investigative actions 

 Review the shared URL to determine if the file is publicly accessible or shared outside the organization. 

 Check if the file-sharing domain has been previously used by this sender or others in the organization. 

 Investigate recent outbound emails for similar use of file-sharing services or unusual external recipients. 

 Previous OneDrive folder creation 

 Next Outbound email includes an external BCC recipient observed for the first time 

 Was this helpful?
