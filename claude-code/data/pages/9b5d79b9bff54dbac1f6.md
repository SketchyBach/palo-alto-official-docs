---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/denied-api-call-by-a-kubernetes-service-account
fetched_at: 2026-09-16T09:06:52Z
source: cortex-platform
---

# Denied API call by a Kubernetes service account | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Denied API call by a Kubernetes service account 

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
AWS Audit Log OR Azure Audit Log OR Gcp Audit Log OR Kubernetes Audit Logs 

 Detection Modules 

 Cloud 

 Detector Tags 

 Kubernetes - API 

 ATT&CK Tactic 

 Execution (TA0002) 

 ATT&CK Technique 

 User Execution (T1204) 

 Severity 

 Informational 

 Description 

 A Kubernetes service account API call was denied. 

 Attacker's Goals 

 Gain access to the Kubernetes cluster. 

 Investigative actions 

 Check whether the service account should be making this API call. 

 Check service account's activity, including additional executed API calls. 

 Variations 
 Denied API call by Kubernetes service account for the first time in the cluster 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Execution (TA0002) 

 ATT&CK Technique 

 User Execution (T1204) 

 Severity 

 Low 

 Description 

 A Kubernetes service account API call was denied. 

 Attacker's Goals 

 Gain access to the Kubernetes cluster. 

 Investigative actions 

 Check whether the service account should be making this API call. 

 Check service account's activity, including additional executed API calls. 

 Suspicious denied API call by a Kubernetes service account 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Execution (TA0002) 

 ATT&CK Technique 

 User Execution (T1204) 

 Severity 

 Informational 

 Description 

 A Kubernetes service account API call was denied. 

 Attacker's Goals 

 Gain access to the Kubernetes cluster. 

 Investigative actions 

 Check whether the service account should be making this API call. 

 Check service account's activity, including additional executed API calls. 

 Previous Deletion of multiple cloud resources 

 Next Device Registration Policy modification 

 Was this helpful?
