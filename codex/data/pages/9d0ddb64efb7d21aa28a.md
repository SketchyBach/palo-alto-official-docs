---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/rare-ms-update-server-was-detected
fetched_at: 2026-09-16T09:08:03Z
source: cortex-platform
---

# Rare MS-Update Server was detected | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Rare MS-Update Server was detected 

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

 2 Days 

 Required Data 

 Palo Alto Networks Firewall EAL Logs 

 ATT&CK Tactic 

 Initial Access (TA0001) 

 ATT&CK Technique 

 Trusted Relationship (T1199) 

 Severity 

 Informational 

 Description 

 The endpoint requested an MS-Update operation from a rare update server. 

 Attacker's Goals 

 The Windows Server Update Services enable machines to discover and download software updates from a dedicated update server. 

 Attackers may use the MS-Update protocol to execute unauthorized code through Microsoft binaries. 

 Investigative actions 

 Inspect the legitimacy of the server as a WSUS functioning server. 

 Verify that your MS-Update network routine is HTTPS enforced* Verify that this MS-Update server is not a newly deployed server as part of a legitimate IT activity. 

 Variations 
 Rare MS-Update Server was detected 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Initial Access (TA0001) 

 ATT&CK Technique 

 Trusted Relationship (T1199) 

 Severity 

 Informational 

 Description 

 The endpoint requested an MS-Update operation from a rare update server. 

 Attacker's Goals 

 The Windows Server Update Services enable machines to discover and download software updates from a dedicated update server. 

 Attackers may use the MS-Update protocol to execute unauthorized code through Microsoft binaries. 

 Investigative actions 

 Inspect the legitimacy of the server as a WSUS functioning server. 

 Verify that your MS-Update network routine is HTTPS enforced* Verify that this MS-Update server is not a newly deployed server as part of a legitimate IT activity. 

 Previous Rare machine account creation 

 Next Rare MS-Update traffic over HTTP 

 Was this helpful?
