---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/aws-ssm-send-command-attempt
fetched_at: 2026-09-16T09:06:55Z
source: cortex-platform
---

# AWS SSM send command attempt | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 AWS SSM send command attempt 

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

 3 Days 

 Required Data 

 AWS Audit Log 

 Detection Modules 

 Cloud 

 Detector Tags 

 Cloud Lateral Movement Analytics, SSM Remote Management Analytics 

 ATT&CK Tactic 

 Lateral Movement (TA0008), Execution (TA0002) 

 ATT&CK Technique 

 Remote Services: Direct Cloud VM Connections (T1021.008), Cloud Administration Command (T1651) 

 Severity 

 Informational 

 Description 

 An identity executed an AWS SSM Document. 

 Attacker's Goals 

 Gaining unauthorized access, executing unauthorized commands, or compromising sensitive information within the target system. 

 Investigative actions 

 Examine the code in the SSM document, and the target objects. 

 Validate the permissions and roles associated with the user initiating the SSM session to ensure they align with the expected level of access. 

 Follow further actions taken by the identity or on the relevant targets. 

 Variations 
 AWS SSM SendCommand targeting multiple instances 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Lateral Movement (TA0008), Execution (TA0002) 

 ATT&CK Technique 

 Remote Services: Direct Cloud VM Connections (T1021.008), Cloud Administration Command (T1651) 

 Severity 

 Low 

 Description 

 An identity executed an AWS SSM Document. 

 Attacker's Goals 

 Gaining unauthorized access, executing unauthorized commands, or compromising sensitive information within the target system. 

 Investigative actions 

 Examine the code in the SSM document, and the target objects. 

 Validate the permissions and roles associated with the user initiating the SSM session to ensure they align with the expected level of access. 

 Follow further actions taken by the identity or on the relevant targets. 

 Unusual AWS SSM send command 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Lateral Movement (TA0008), Execution (TA0002) 

 ATT&CK Technique 

 Remote Services: Direct Cloud VM Connections (T1021.008), Cloud Administration Command (T1651) 

 Severity 

 Low 

 Description 

 An identity executed an AWS SSM Document. 

 Attacker's Goals 

 Gaining unauthorized access, executing unauthorized commands, or compromising sensitive information within the target system. 

 Investigative actions 

 Examine the code in the SSM document, and the target objects. 

 Validate the permissions and roles associated with the user initiating the SSM session to ensure they align with the expected level of access. 

 Follow further actions taken by the identity or on the relevant targets. 

 Previous AWS SSM parameters retrieval 

 Next AWS Storage Gateway enumeration 

 Was this helpful?
