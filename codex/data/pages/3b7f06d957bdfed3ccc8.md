---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/usage-of-homograph-characters-detected-in-an-email-attachment-s-name
fetched_at: 2026-09-06T11:10:15Z
source: cortex-platform
---

# Usage of homograph characters detected in an email attachment(s) name | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Usage of homograph characters detected in an email attachment(s) name 

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

 Evasion, Phishing 

 ATT&CK Tactic 

 Execution (TA0002), Credential Access (TA0006) 

 ATT&CK Technique 

 User Execution (T1204), Brute Force: Password Cracking (T1110.002) 

 Severity 

 Informational 

 Description 

 Detected characters resembling Latin letters within an email attachment(s) name. This method could be used as a method to evade text or file scanners and analyzers. 

 Attacker's Goals 

 Evade file scanner defenses, tricking recipients into running malicious attachments. 

 Investigative actions 

 Examine the sender's IP address and reputation. 

 Verify whether the sender's IP address has appeared in different log sources before, and if it is recognizable. 

 Check the domain the email came from, and if this domain is recognized within the organization. 

 Scrutinize the attachments related to the email message. 

 Monitor file-related actions taken related to the attachment. 

 Variations 
 Usage of homograph characters detected in an email attachment(s) extension 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Execution (TA0002), Credential Access (TA0006) 

 ATT&CK Technique 

 User Execution (T1204), Brute Force: Password Cracking (T1110.002) 

 Severity 

 Low 

 Description 

 Detected non-latin characters within an email attachment's extension(s). Detected characters resembling Latin letters within an email attachment(s) name. This method could be used as a method to evade text or file scanners and analyzers. 

 Attacker's Goals 

 Evade file scanner defenses, tricking recipients into running malicious attachments. 

 Investigative actions 

 Examine the sender's IP address and reputation. 

 Verify whether the sender's IP address has appeared in different log sources before, and if it is recognizable. 

 Check the domain the email came from, and if this domain is recognized within the organization. 

 Scrutinize the attachments related to the email message. 

 Monitor file-related actions taken related to the attachment. 

 Previous Upload pattern that resembles Peer to Peer traffic 

 Next Usage of homograph characters detected in an email's from header 

 Was this helpful?
