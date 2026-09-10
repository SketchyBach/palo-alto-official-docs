---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/compute-activity-in-dormant-cloud-region
fetched_at: 2026-09-06T11:02:15Z
source: cortex-platform
---

# Compute activity in dormant cloud region | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Compute activity in dormant cloud region 

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

 Detector Tags 

 OCI Analytics 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Unused/Unsupported Cloud Regions (T1535) 

 Severity 

 Informational 

 Description 

 A compute resource was created or updated in a cloud region that has been dormant for this project. 

 Attacker's Goals 

 Create compute resources in unmonitored regions to evade detection for purposes such as hijacking resources or establishing persistence. 

 Investigative actions 

 Verify if compute resources are authorized in this region. 

 Terminate unauthorized compute resources and disable unused regions. 

 Variations 
 Compute activity in dormant cloud region from a non-VPN IP address 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Unused/Unsupported Cloud Regions (T1535) 

 Severity 

 Informational 

 Description 

 A compute resource was created or updated in a cloud region that has been dormant for this project. 

 Attacker's Goals 

 Create compute resources in unmonitored regions to evade detection for purposes such as hijacking resources or establishing persistence. 

 Investigative actions 

 Verify if compute resources are authorized in this region. 

 Terminate unauthorized compute resources and disable unused regions. 

 A cloud compute instance was created in a dormant region 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Unused/Unsupported Cloud Regions (T1535) 

 Severity 

 Medium 

 Description 

 A compute resource was created or updated in a cloud region that has been dormant for this project. 

 Attacker's Goals 

 Create compute resources in unmonitored regions to evade detection for purposes such as hijacking resources or establishing persistence. 

 Investigative actions 

 Verify if compute resources are authorized in this region. 

 Terminate unauthorized compute resources and disable unused regions. 

 Compute activity in dormant cloud region by a compromised AWS access key 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Unused/Unsupported Cloud Regions (T1535) 

 Severity 

 High 

 Description 

 A compute resource was created or updated in a cloud region that has been dormant for this project. 

 Attacker's Goals 

 Create compute resources in unmonitored regions to evade detection for purposes such as hijacking resources or establishing persistence. 

 Investigative actions 

 Verify if compute resources are authorized in this region. 

 Terminate unauthorized compute resources and disable unused regions. 

 Previous Compressing data using python 

 Next Conditional Access policy removed 

 Was this helpful?
