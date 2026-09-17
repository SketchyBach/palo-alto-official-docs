---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/kubernetes-pod-created-with-host-process-id-pid-namespace
fetched_at: 2026-09-16T09:07:18Z
source: cortex-platform
---

# Kubernetes Pod created with host process ID (PID) namespace | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Kubernetes Pod created with host process ID (PID) namespace 

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

 Privilege Escalation (TA0004), Execution (TA0002) 

 ATT&CK Technique 

 Escape to Host (T1611), Deploy Container (T1610) 

 Severity 

 Informational 

 Description 

 An identity created a Kubernetes pod with the host process ID (PID) namespace. This may indicate an adversary attempting to access processes running on the host, which could allow escalating privileges to root. 

 Attacker's Goals 

 View processes on the host. 

 View the environment variables for each pod on the host. 

 View the file descriptors for each pod on the host. 

 Kill processes on the node. 

 Investigative actions 

 Check the identity's role designation in the organization. 

 Inspect for any additional suspicious activities inside the Kubernetes Pod. 

 Variations 
 Kubernetes Pod created with host process ID (PID) namespace for the first time in the cluster 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Privilege Escalation (TA0004), Execution (TA0002) 

 ATT&CK Technique 

 Escape to Host (T1611), Deploy Container (T1610) 

 Severity 

 Low 

 Description 

 An identity created a Kubernetes pod with the host process ID (PID) namespace. This may indicate an adversary attempting to access processes running on the host, which could allow escalating privileges to root. 

 Attacker's Goals 

 View processes on the host. 

 View the environment variables for each pod on the host. 

 View the file descriptors for each pod on the host. 

 Kill processes on the node. 

 Investigative actions 

 Check the identity's role designation in the organization. 

 Inspect for any additional suspicious activities inside the Kubernetes Pod. 

 Kubernetes Pod created with host process ID (PID) namespace for the first time in the namespace 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Privilege Escalation (TA0004), Execution (TA0002) 

 ATT&CK Technique 

 Escape to Host (T1611), Deploy Container (T1610) 

 Severity 

 Low 

 Description 

 An identity created a Kubernetes pod with the host process ID (PID) namespace. This may indicate an adversary attempting to access processes running on the host, which could allow escalating privileges to root. 

 Attacker's Goals 

 View processes on the host. 

 View the environment variables for each pod on the host. 

 View the file descriptors for each pod on the host. 

 Kill processes on the node. 

 Investigative actions 

 Check the identity's role designation in the organization. 

 Inspect for any additional suspicious activities inside the Kubernetes Pod. 

 Kubernetes Pod created with host process ID (PID) namespace for the first time by the identity 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Privilege Escalation (TA0004), Execution (TA0002) 

 ATT&CK Technique 

 Escape to Host (T1611), Deploy Container (T1610) 

 Severity 

 Low 

 Description 

 An identity created a Kubernetes pod with the host process ID (PID) namespace. This may indicate an adversary attempting to access processes running on the host, which could allow escalating privileges to root. 

 Attacker's Goals 

 View processes on the host. 

 View the environment variables for each pod on the host. 

 View the file descriptors for each pod on the host. 

 Kill processes on the node. 

 Investigative actions 

 Check the identity's role designation in the organization. 

 Inspect for any additional suspicious activities inside the Kubernetes Pod. 

 Previous Kubernetes Pod Created with host Inter Process Communications (IPC) namespace 

 Next Kubernetes Pod Created With Sensitive Volume 

 Was this helpful?
