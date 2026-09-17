---
url: https://docs.paloaltonetworks.com/ngfw/incidents-and-alerts/incidents/firewall-losing-logs
fetched_at: 2026-09-16T07:32:32Z
source: palo-alto-main
---

# Firewall losing logs Clear

Updated on 

 Thu Aug 20 10:58:28 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Incidents 

 NGFW Incidents Reference 

 Firewall losing logs 

 Download PDF 

 Next-Generation Firewall 

 Firewall losing logs 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Firewall HA Failover 

 Next 

 Firewall Traffic Disruption Detected 

 Firewall losing logs 

 Incident Code 

 INC_NGFW_LOG_LOSS 

 Severity 

 Warning 

 Category 

 Network Services 

 Subcategory 

 Logging 

 Description 

 This alert indicates that DP logs (such as traffic, threat, URL, Netflow,
 User-ID, GP, Decryption, EAL, etc.) that are supposed to be generated based on
 inspected traffic and logging configurations are being lost. When logs are
 generated in the DP, they are moved into logging queues, which are then handed
 over to the logrcvr in the Management Plane (DP to MP). To prevent the DP-to-MP
 channel from being overwhelmed, a rate-limiting mechanism was implemented to
 control the transfer of logs from the Data Plane to the Management Plane. This
 mechanism regulates either the logging count rate (logs/sec) or bandwidth usage
 (KB/sec). The control is in place to ensure that other services such as packet
 capture and any requests from DP to the cloud (e.g., URL, Wildfire, etc.), are not
 dropped due to excessive logging bandwidth consumption. 

 Raise Condition 

 Firewall is losing logs at dataplane and logs losing rate is greater than 50 logs
 per second at least for an hour. OR Dataplane(DP) to Management plane(MP) logs
 overflow and logs are lost due to rate-limiting between DP and MP. 

 Clear Condition 

 When the logs are being generated, retained and are not lost for 24 hr
 duration. 

 Probable Root Cause Incident 

 "INC_NGFW_DROPPING_LOGS_FWD_QUEUE_FAIL", 

 "INC_NGFW_ES_VLD_INGESTION_ISSUES", 

 "INC_NGFW_HIGH_LOG_RATE", 

 "INC_NGFW_INTER_LOG_COLLECTOR_DISCONNECT", 

 "INC_NGFW_LFC_LOGRCVR_OOM_KERNEL_FAILURE", 

 "INC_NGFW_LFC_LOGRCVR_OOM_PATH_MONITOR_FAILURE", 

 "INC_NGFW_LICENSE_NOT_PROVISIONED_LCAAS", 

 "INC_NGFW_LOG_CERT_MISMATCH", 

 "INC_NGFW_PAN_LC_DISCONNECTED_FROM_GROUP", 

 "INC_NGFW_PANORAMA_LOGD_THROTTLE", 

 "INC_NGFW_VLDMGR_LOGD_CONNECTION_BROKEN", 

 "INC_NGFW_VLDMGR_LOGD_CONNECTION_FLAP", 

 "INC_NGFW_VLDMGR_VLD_DISCONNECT", 

 "INC_NGFW_FAILED_TO_SCHEDULE_A_LOG_FWD_CONTROL_JOB_FOR_DEVICE" 

 Previous 

 Firewall HA Failover 

 Next 

 Firewall Traffic Disruption Detected
