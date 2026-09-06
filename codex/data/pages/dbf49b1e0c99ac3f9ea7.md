---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/unusual-hostname-for-the-sending-mail-server-in-the-email-headers
fetched_at: 2026-09-06T11:09:54Z
source: cortex-platform
---

# Unusual hostname for the sending mail server in the email headers | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Unusual hostname for the sending mail server in the email headers 

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

 Detector Tags 

 Spoofing 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Social Engineering: Impersonation (T1684.001) 

 Severity 

 Informational 

 Description 

 The detected mail server hostname had not been observed in the organization's emails in the past 30 days. 

 Attacker's Goals 

 Disguise the email's origin by spoofing the received header to appear as a trusted sender, impersonating a trusted source, aims to mislead recipients into disclosing private data or performing unsafe acts. 

 Investigative actions 

 Review the email's received headers, to trace its path and spot spoofing signs. 

 Examine the sender's IP address and domain reputation. 

 Closely inspect the email content for malicious links, attachments, or requests for sensitive information. 

 Monitor further actions taken, such as file downloads or access to potentially malicious links. 

 Previous Unusual file-sharing links for mailbox owner 

 Next Unusual IAM enumeration activity by a non-user Identity 

 Was this helpful?
