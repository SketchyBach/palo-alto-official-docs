---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/large-upload-generic
fetched_at: 2026-09-16T09:07:19Z
source: cortex-platform
---

# Large Upload (Generic) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Large Upload (Generic) 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 1 Day 

 Deduplication Period 

 1 Day 

 Required Data 

 Requires one of the following data sources:
Palo Alto Networks Firewall traffic Logs OR XDR Agent 

 ATT&CK Tactic 

 Exfiltration (TA0010) 

 ATT&CK Technique 

 Exfiltration Over Alternative Protocol (T1048) 

 Severity 

 Low 

 Description 

 The endpoint transferred large amounts of data to an external site using a different protocol from HTTP/s, FTP, or SMTP. (A specific detector is used for each of those protocols.) Cortex XDR Analytics assumes that data transfers out of your network are ordinarily performed using one of those three services, so it expects that data transfers over all other ports to be low. For the same reason, Cortex XDR Analytics also assumes endpoint traffic towards a specific destination should be about the same over long periods of time. An attacker may be exfiltrating data directly to the internet. 

 Attacker's Goals 

 Transfer data he has stolen from your network to a location that is convenient and useful to him. 

 Investigative actions 

 Check if the traffic is related to SSH activity, it can trigger this alert. It is possible that someone on your network is legitimately engaged in SSH activity. 

 Check if the traffic is to/from a misconfigured network. 

 Check if the traffic is to a new external service or server that has recently been adopted for use by an organization in your enterprise. 

 Identify the process/user performing the data transfer to determine if the transfer is sanctioned. 

 Variations 
 Large Upload (Generic) 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Exfiltration (TA0010) 

 ATT&CK Technique 

 Exfiltration Over Alternative Protocol (T1048) 

 Severity 

 Informational 

 Description 

 The endpoint transferred large amounts of data to an external site using a different protocol from HTTP/s, FTP, or SMTP. (A specific detector is used for each of those protocols.) Cortex XDR Analytics assumes that data transfers out of your network are ordinarily performed using one of those three services, so it expects that data transfers over all other ports to be low. For the same reason, Cortex XDR Analytics also assumes endpoint traffic towards a specific destination should be about the same over long periods of time. An attacker may be exfiltrating data directly to the internet. 

 Attacker's Goals 

 Transfer data he has stolen from your network to a location that is convenient and useful to him. 

 Investigative actions 

 Check if the traffic is related to SSH activity, it can trigger this alert. It is possible that someone on your network is legitimately engaged in SSH activity. 

 Check if the traffic is to/from a misconfigured network. 

 Check if the traffic is to a new external service or server that has recently been adopted for use by an organization in your enterprise. 

 Identify the process/user performing the data transfer to determine if the transfer is sanctioned. 

 Large Upload (Generic) Lower than 100 MB 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Exfiltration (TA0010) 

 ATT&CK Technique 

 Exfiltration Over Alternative Protocol (T1048) 

 Severity 

 Informational 

 Description 

 The endpoint transferred large amounts of data to an external site using a different protocol from HTTP/s, FTP, or SMTP. (A specific detector is used for each of those protocols.) Cortex XDR Analytics assumes that data transfers out of your network are ordinarily performed using one of those three services, so it expects that data transfers over all other ports to be low. For the same reason, Cortex XDR Analytics also assumes endpoint traffic towards a specific destination should be about the same over long periods of time. An attacker may be exfiltrating data directly to the internet. 

 Attacker's Goals 

 Transfer data he has stolen from your network to a location that is convenient and useful to him. 

 Investigative actions 

 Check if the traffic is related to SSH activity, it can trigger this alert. It is possible that someone on your network is legitimately engaged in SSH activity. 

 Check if the traffic is to/from a misconfigured network. 

 Check if the traffic is to a new external service or server that has recently been adopted for use by an organization in your enterprise. 

 Identify the process/user performing the data transfer to determine if the transfer is sanctioned. 

 Large Upload (Generic) to a Frequently Used Upload Target 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Exfiltration (TA0010) 

 ATT&CK Technique 

 Exfiltration Over Alternative Protocol (T1048) 

 Severity 

 Informational 

 Description 

 The endpoint transferred large amounts of data to an external site using a different protocol from HTTP/s, FTP, or SMTP. (A specific detector is used for each of those protocols.) Cortex XDR Analytics assumes that data transfers out of your network are ordinarily performed using one of those three services, so it expects that data transfers over all other ports to be low. For the same reason, Cortex XDR Analytics also assumes endpoint traffic towards a specific destination should be about the same over long periods of time. An attacker may be exfiltrating data directly to the internet. 

 Attacker's Goals 

 Transfer data he has stolen from your network to a location that is convenient and useful to him. 

 Investigative actions 

 Check if the traffic is related to SSH activity, it can trigger this alert. It is possible that someone on your network is legitimately engaged in SSH activity. 

 Check if the traffic is to/from a misconfigured network. 

 Check if the traffic is to a new external service or server that has recently been adopted for use by an organization in your enterprise. 

 Identify the process/user performing the data transfer to determine if the transfer is sanctioned. 

 Previous Large Upload (FTP) 

 Next Large Upload (HTTPS) 

 Was this helpful?
