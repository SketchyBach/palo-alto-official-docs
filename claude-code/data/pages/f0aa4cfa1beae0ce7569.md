---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/potential-spoofing-of-internal-domain-spotted
fetched_at: 2026-09-06T11:06:39Z
source: cortex-platform
---

# Potential spoofing of internal domain spotted | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Potential spoofing of internal domain spotted 

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

 Employee Impersonation, Spear Phishing 

 ATT&CK Tactic 

 Initial Access (TA0001), Stealth (TA0005) 

 ATT&CK Technique 

 Phishing (T1566), Social Engineering: Impersonation (T1684.001) 

 Severity 

 Informational 

 Description 

 An external sender is possibly impersonating an employee by spoofing the company's internal address. 

 Attacker's Goals 

 Get credentials for internal systems. 

 Executing financial transfers from the company to the attacker's account. 

 Extracting information outside the company. 

 Encrypting critical information and demanding a ransom. 

 Investigative actions 

 Check the received header path, especially the sender host. 

 Check DMARC, SPF AND DKIM authentication results. 

 Verify whether the sender's IP address has appeared in different log sources before and its reputation. 

 If the message contains attachments or links, scrutinize them for any suspicious indications. 

 Monitor further actions taken, such as file downloads or access to potentially malicious links. 

 Previous Potential SCCM credential harvesting using WMI detected 

 Next PowerShell Initiates a Network Connection to GitHub 

 Was this helpful?
