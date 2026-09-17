---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/an-ebs-snapshot-block-was-downloaded
fetched_at: 2026-09-16T09:06:58Z
source: cortex-platform
---

# An EBS snapshot block was downloaded | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 An EBS snapshot block was downloaded 

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

 AWS Audit Log 

 Detection Modules 

 Cloud 

 Detector Tags 

 Cloud Data Asset Exfiltration, Data Detection & Response 

 ATT&CK Tactic 

 Collection (TA0009), Exfiltration (TA0010) 

 ATT&CK Technique 

 Data from Cloud Storage (T1530), Automated Exfiltration (T1020) 

 Severity 

 Informational 

 Description 

 An EBS snapshot block was downloaded using the EBS direct API. This may indicate an attacker's attempt to exfiltrate data from a volume snapshot in the cloud environment. 

 Attacker's Goals 

 Exfiltrate sensitive data from the cloud environment. 

 Investigative actions 

 Check the accessed snapshot and corresponding volume. 

 Monitor additional snapshot blocks downloads from the snapshot. 

 Verify that the identity did not download any sensitive information that it shouldn't. 

 Variations 
 An EBS snapshot block was downloaded from a snapshot with sensitive data 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Collection (TA0009), Exfiltration (TA0010) 

 ATT&CK Technique 

 Data from Cloud Storage (T1530), Automated Exfiltration (T1020) 

 Severity 

 Medium 

 Description 

 An EBS snapshot block was downloaded using the EBS direct API. This may indicate an attacker's attempt to exfiltrate data from a volume snapshot in the cloud environment. The snapshot contains sensitive data. 

 Attacker's Goals 

 Exfiltrate sensitive data from the cloud environment. 

 Investigative actions 

 Check the accessed snapshot and corresponding volume. 

 Monitor additional snapshot blocks downloads from the snapshot. 

 Verify that the identity did not download any sensitive information that it shouldn't. 

 An unusual download of EBS snapshot block 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Collection (TA0009), Exfiltration (TA0010) 

 ATT&CK Technique 

 Data from Cloud Storage (T1530), Automated Exfiltration (T1020) 

 Severity 

 Low 

 Description 

 An EBS snapshot block was downloaded using the EBS direct API. This may indicate an attacker's attempt to exfiltrate data from a volume snapshot in the cloud environment. The operation was not performed by this identity in the last 30 days. 

 Attacker's Goals 

 Exfiltrate sensitive data from the cloud environment. 

 Investigative actions 

 Check the accessed snapshot and corresponding volume. 

 Monitor additional snapshot blocks downloads from the snapshot. 

 Verify that the identity did not download any sensitive information that it shouldn't. 

 Previous An Azure VPN Connection was modified 

 Next An Email address was added to AWS SES 

 Was this helpful?
