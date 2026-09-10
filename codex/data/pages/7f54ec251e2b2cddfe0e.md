---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/aws-systems-manager-hosts-enumeration
fetched_at: 2026-09-06T11:01:08Z
source: cortex-platform
---

# AWS Systems Manager hosts enumeration | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 AWS Systems Manager hosts enumeration 

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

 AWS Audit Log 

 Detection Modules 

 Cloud 

 Detector Tags 

 SSM Remote Management Analytics 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Cloud Infrastructure Discovery (T1580) 

 Severity 

 Informational 

 Description 

 A cloud identity enumerated hosts managed by AWS Systems Manager. Adversaries may use this API to discover SSM managed instances as a precursor to lateral movement or remote code execution. 

 Attacker's Goals 

 Discover SSM managed instances to plan lateral movement, remote command execution, or further reconnaissance. 

 Investigative actions 

 Determine whether the identity legitimately needs to enumerate SSM managed instances. 

 Review subsequent activity by the identity, especially SSM SendCommand, StartSession, or instance profile modifications. 

 Validate the source IP and user-agent of the API call. 

 Variations 
 AWS Systems Manager hosts enumeration via programmatic access 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Cloud Infrastructure Discovery (T1580) 

 Severity 

 Low 

 Description 

 A cloud identity enumerated hosts managed by AWS Systems Manager. Adversaries may use this API to discover SSM managed instances as a precursor to lateral movement or remote code execution. 

 Attacker's Goals 

 Discover SSM managed instances to plan lateral movement, remote command execution, or further reconnaissance. 

 Investigative actions 

 Determine whether the identity legitimately needs to enumerate SSM managed instances. 

 Review subsequent activity by the identity, especially SSM SendCommand, StartSession, or instance profile modifications. 

 Validate the source IP and user-agent of the API call. 

 Previous AWS support case creation 

 Next AWS Transfer Family server created 

 Was this helpful?
