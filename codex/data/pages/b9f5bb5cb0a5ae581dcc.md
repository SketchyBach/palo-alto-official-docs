---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/multi-region-enumeration-activity
fetched_at: 2026-09-06T11:05:25Z
source: cortex-platform
---

# Multi region enumeration activity | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Multi region enumeration activity 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 30 Minutes 

 Deduplication Period 

 5 Days 

 Required Data 

 Requires one of the following data sources:
AWS Audit Log OR Azure Audit Log OR Gcp Audit Log 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Discovery (TA0007), Stealth (TA0005) 

 ATT&CK Technique 

 Cloud Infrastructure Discovery (T1580), Unused/Unsupported Cloud Regions (T1535), Cloud Service Discovery (T1526) 

 Severity 

 Informational 

 Description 

 An internal identity performed an operation on multiple regions, considerably more than usual. This may indicate an attacker's attempt to identify all available resources in the cloud environment. 

 Attacker's Goals 

 Discover cloud resources that are available within the environment and leverage them to perform additional attacks against the organization. 

 Detect unused geographic regions and leverage them to evade detection of malicious operations. 

 Investigative actions 

 Check the identity designation. 

 Verify that the identity did not perform any operation in a region that it shouldn't. 

 Previous Msiexec execution of an executable from an uncommon remote location 

 Next Multiple alerts associated with a single RDP connection 

 Was this helpful?
