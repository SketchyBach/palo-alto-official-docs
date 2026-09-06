---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/cloud-instance-creation-attempt
fetched_at: 2026-09-06T11:01:57Z
source: cortex-platform
---

# Cloud instance creation attempt | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Cloud instance creation attempt 

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

 5 Days 

 Required Data 

 Requires one of the following data sources:
AWS Audit Log OR Azure Audit Log OR Gcp Audit Log 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Stealth (TA0005), Defense Impairment (TA0112) 

 ATT&CK Technique 

 Masquerading (T1036), Modify Cloud Compute Infrastructure: Create Cloud Instance (T1578.002) 

 Severity 

 Informational 

 Description 

 An attempt was made to create a cloud compute instance. 

 Attacker's Goals 

 Create a new cloud instance to evade detection or leverage it for further malicious activity. 

 Investigative actions 

 Review recent activity related to the identity and the created cloud instance. 

 Variations 
 EC2 instance creation with admin profile, public IP address and external security group 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Defense Impairment (TA0112) 

 ATT&CK Technique 

 Masquerading (T1036), Modify Cloud Compute Infrastructure: Create Cloud Instance (T1578.002) 

 Severity 

 High 

 Description 

 An attempt was made to create a cloud compute instance. 

 Attacker's Goals 

 Create a new cloud instance to evade detection or leverage it for further malicious activity. 

 Investigative actions 

 Review recent activity related to the identity and the created cloud instance. 

 EC2 instance creation with admin profile and public IP address 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Defense Impairment (TA0112) 

 ATT&CK Technique 

 Masquerading (T1036), Modify Cloud Compute Infrastructure: Create Cloud Instance (T1578.002) 

 Severity 

 Medium 

 Description 

 An attempt was made to create a cloud compute instance. 

 Attacker's Goals 

 Create a new cloud instance to evade detection or leverage it for further malicious activity. 

 Investigative actions 

 Review recent activity related to the identity and the created cloud instance. 

 Previous Cloud infrastructure enumeration activity 

 Next Cloud instance deletion attempt 

 Was this helpful?
