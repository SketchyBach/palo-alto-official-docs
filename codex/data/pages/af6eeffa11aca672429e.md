---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/unusual-encrypting-file-system-remote-call-efsrpc-to-domain-controller
fetched_at: 2026-09-16T09:08:50Z
source: cortex-platform
---

# Unusual Encrypting File System Remote call (EFSRPC) to domain controller | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Unusual Encrypting File System Remote call (EFSRPC) to domain controller 

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

 XDR Agent with eXtended Threat Hunting (XTH) 

 Detection Modules 

 Identity Analytics 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Forced Authentication (T1187), Adversary-in-the-Middle: Name Resolution Poisoning and SMB Relay (T1557.001) 

 Severity 

 Low 

 Description 

 An unusual Encrypting File System Remote call (EFSRPC) was made to a domain controller. 

 Attacker's Goals 

 An attacker can abuse the Encrypting File System Remote Protocol to coerce authentication from a DC. 

 This authentication can later be used for obtaining a DC certificate for DCSync. 

 Investigative actions 

 Check for a suspicious process on the initiator. 

 Check if the source host is a vulnerability scanner. 

 Check for unusual connections from the server of the requested file location (it may be a relay server). 

 Look for unusual AD CS certificate requests. 

 Look for following suspicious connections using the DC machine account. 

 Check for possible DCSync alerts. 

 Variations 
 A suspicious Encrypting File System Remote call (EFSRPC) was made to a domain controller 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Forced Authentication (T1187), Adversary-in-the-Middle: Name Resolution Poisoning and SMB Relay (T1557.001) 

 Severity 

 Medium 

 Description 

 An unusual Encrypting File System Remote call (EFSRPC) was made to a domain controller. 

 Attacker's Goals 

 An attacker can abuse the Encrypting File System Remote Protocol to coerce authentication from a DC. 

 This authentication can later be used for obtaining a DC certificate for DCSync. 

 Investigative actions 

 Check for a suspicious process on the initiator. 

 Check if the source host is a vulnerability scanner. 

 Check for unusual connections from the server of the requested file location (it may be a relay server). 

 Look for unusual AD CS certificate requests. 

 Look for following suspicious connections using the DC machine account. 

 Check for possible DCSync alerts. 

 Abnormal Encrypting File System Remote call (EFSRPC) to domain controller using EfsRpcFileKeyInfo for the first time 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Forced Authentication (T1187), Adversary-in-the-Middle: Name Resolution Poisoning and SMB Relay (T1557.001) 

 Severity 

 Low 

 Description 

 An abnormal EfsRpcFileKeyInfo Encrypting File System Remote call (EFSRPC) was made to a domain controller for the first time. 

 Attacker's Goals 

 An attacker can abuse the Encrypting File System Remote Protocol to coerce authentication from a DC. 

 This authentication can later be used for obtaining a DC certificate for DCSync. 

 Investigative actions 

 Check for a suspicious process on the initiator. 

 Check if the source host is a vulnerability scanner. 

 Check for unusual connections from the server of the requested file location (it may be a relay server). 

 Look for unusual AD CS certificate requests. 

 Look for following suspicious connections using the DC machine account. 

 Check for possible DCSync alerts. 

 Abnormal Encrypting File System Remote call (EFSRPC) to domain controller using EfsRpcFileKeyInfo 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Forced Authentication (T1187), Adversary-in-the-Middle: Name Resolution Poisoning and SMB Relay (T1557.001) 

 Severity 

 Informational 

 Description 

 An abnormal EfsRpcFileKeyInfo Encrypting File System Remote call (EFSRPC) was made to a domain controller. 

 Attacker's Goals 

 An attacker can abuse the Encrypting File System Remote Protocol to coerce authentication from a DC. 

 This authentication can later be used for obtaining a DC certificate for DCSync. 

 Investigative actions 

 Check for a suspicious process on the initiator. 

 Check if the source host is a vulnerability scanner. 

 Check for unusual connections from the server of the requested file location (it may be a relay server). 

 Look for unusual AD CS certificate requests. 

 Look for following suspicious connections using the DC machine account. 

 Check for possible DCSync alerts. 

 Previous Unusual display name in From header 

 Next Unusual exec into a Kubernetes Pod 

 Was this helpful?
