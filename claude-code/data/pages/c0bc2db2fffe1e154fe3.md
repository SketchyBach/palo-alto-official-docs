---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/unusual-url-s-sent-by-a-brand-were-observed-in-the-email
fetched_at: 2026-09-06T11:10:09Z
source: cortex-platform
---

# Unusual URL(s) sent by a brand were observed in the email | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Unusual URL(s) sent by a brand were observed in the email 

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

 Execution (TA0002), Credential Access (TA0006) 

 ATT&CK Technique 

 User Execution (T1204), Brute Force: Password Cracking (T1110.002) 

 Severity 

 Informational 

 Description 

 A URL that is not usually associated with the brand has been detected. 

 Attacker's Goals 

 Trick the user into clicking a link while avoiding detection. 

 Investigative actions 

 Examine the sender's IP address and reputation. 

 Verify whether the sender's IP address has appeared in different log sources before and if it is recognizable. 

 If the message contains attachments or links, scrutinize them for any suspicious indications. 

 Monitor further actions taken, such as file downloads or access to potentially malicious links. 

 Previous Unusual SSH Activity 

 Next Unusual use of a 'SysInternals' tool 

 Was this helpful?
