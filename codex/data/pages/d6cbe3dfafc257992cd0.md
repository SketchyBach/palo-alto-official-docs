---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/email-attachment-s-with-potentially-malicious-mime-type
fetched_at: 2026-09-06T11:02:37Z
source: cortex-platform
---

# Email attachment(s) with potentially malicious MIME type | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Email attachment(s) with potentially malicious MIME type 

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

 Microsoft 365 Emails 

 Detection Modules 

 Email 

 ATT&CK Tactic 

 Stealth (TA0005), Execution (TA0002) 

 ATT&CK Technique 

 Masquerading: Masquerade File Type (T1036.008), User Execution (T1204) 

 Severity 

 Informational 

 Description 

 The email message contains an attachment(s) with a potentially malicious MIME type. 

 Attacker's Goals 

 Bypass security filters and deliver malicious content to users 

 Deploy malicious attachments through emails to compromise systems, gain unauthorized access, or facilitate cyber threats. 

 Investigative actions 

 Carefully analyze attachments for any indications of suspicious or malicious behavior. 

 Scrutinize the attachments for any suspicious indications. 

 Confirm whether the attachments were successfully delivered to the recipient's mailbox. 

 If the attachments were delivered successfully, verify whether the recipient downloaded them. 

 Variations 
 Attachment(s) with potentially malicious MIME type unusual for the organization 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Execution (TA0002) 

 ATT&CK Technique 

 Masquerading: Masquerade File Type (T1036.008), User Execution (T1204) 

 Severity 

 Informational 

 Description 

 At least one attachment with a potentially malicious file mime-type was received in an email for the first time within the organization in the past 30 days. 

 Attacker's Goals 

 Bypass security filters and deliver malicious content to users 

 Deploy malicious attachments through emails to compromise systems, gain unauthorized access, or facilitate cyber threats. 

 Investigative actions 

 Carefully analyze attachments for any indications of suspicious or malicious behavior. 

 Scrutinize the attachments for any suspicious indications. 

 Confirm whether the attachments were successfully delivered to the recipient's mailbox. 

 If the attachments were delivered successfully, verify whether the recipient downloaded them. 

 Attachment(s) with a potentially malicious MIME type that is unusual for the recipient 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Execution (TA0002) 

 ATT&CK Technique 

 Masquerading: Masquerade File Type (T1036.008), User Execution (T1204) 

 Severity 

 Informational 

 Description 

 At least one attachment with a potentially malicious file mime-type was received in an email for the first time for the recipient in the past 30 days. 

 Attacker's Goals 

 Bypass security filters and deliver malicious content to users 

 Deploy malicious attachments through emails to compromise systems, gain unauthorized access, or facilitate cyber threats. 

 Investigative actions 

 Carefully analyze attachments for any indications of suspicious or malicious behavior. 

 Scrutinize the attachments for any suspicious indications. 

 Confirm whether the attachments were successfully delivered to the recipient's mailbox. 

 If the attachments were delivered successfully, verify whether the recipient downloaded them. 

 Previous Elevation to SYSTEM via services 

 Next Email attachment with a potentially malicious file extension 

 Was this helpful?
