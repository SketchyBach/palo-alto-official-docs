---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/multiple-failed-logins-from-a-single-ip
fetched_at: 2026-09-06T11:05:33Z
source: cortex-platform
---

# Multiple failed logins from a single IP | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Multiple failed logins from a single IP 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 1 Hour 

 Deduplication Period 

 5 Days 

 Required Data 

 Requires one of the following data sources:
AWS Audit Log OR Azure Audit Log OR Gcp Audit Log 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Initial Access (TA0001) 

 ATT&CK Technique 

 Trusted Relationship (T1199), Valid Accounts: Cloud Accounts (T1078.004) 

 Severity 

 Informational 

 Description 

 Multiple failed logins were observed in a short period of time from a single external IP. The IP is not a known identity provider. 

 Attacker's Goals 

 Gain initial access to the cloud console. 

 Investigative actions 

 Check if the IP is a known IP. 

 Check if a successful login from the same IP occurred after the failed login attempts. 

 Variations 
 Multiple failed logins from an unknown IP 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Initial Access (TA0001) 

 ATT&CK Technique 

 Trusted Relationship (T1199), Valid Accounts: Cloud Accounts (T1078.004) 

 Severity 

 Medium 

 Description 

 Multiple failed logins were observed in a short period of time from a single external IP. The IP is not a known identity provider. The IP is not a known IP in the organization. This could indicate on an active brute force attempt. 

 Attacker's Goals 

 Gain initial access to the cloud console. 

 Investigative actions 

 Check if the IP is a known IP. 

 Check if a successful login from the same IP occurred after the failed login attempts. 

 Multiple failed logins from a single IP by a compromised AWS access key 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Initial Access (TA0001) 

 ATT&CK Technique 

 Trusted Relationship (T1199), Valid Accounts: Cloud Accounts (T1078.004) 

 Severity 

 High 

 Description 

 Multiple failed logins were observed in a short period of time from a single external IP. The IP is not a known identity provider. 

 Attacker's Goals 

 Gain initial access to the cloud console. 

 Investigative actions 

 Check if the IP is a known IP. 

 Check if a successful login from the same IP occurred after the failed login attempts. 

 Previous Multiple failed AWS assume role attempts 

 Next Multiple mail items were accessed in a short period of time 

 Was this helpful?
