---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/aws-route53-dns-resolver-query-logging-configuration-deletion
fetched_at: 2026-09-06T11:20:22Z
source: cortex-platform
---

# AWS Route53 DNS Resolver query logging configuration deletion | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 AWS Route53 DNS Resolver query logging configuration deletion 

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

 Cloud Log Tampering Analytics 

 ATT&CK Tactic 

 Defense Impairment (TA0112) 

 ATT&CK Technique 

 Disable or Modify Tools: Disable or Modify Cloud Log (T1685.002) 

 Severity 

 Low 

 Description 

 An AWS identity has deleted Route53 DNS Resolver query logging configuration. 

 Attacker's Goals 

 Evade detection while performing DNS traffic or tunneling. 

 Investigative actions 

 Check if there were any network attempts that fit the deleted rule. 

 Check The cloud identity activity prior/after to the configuration deletion. 

 Variations 
 Successful AWS Route53 DNS Resolver query logging configuration deletion by a non-admin identity 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Defense Impairment (TA0112) 

 ATT&CK Technique 

 Disable or Modify Tools: Disable or Modify Cloud Log (T1685.002) 

 Severity 

 Medium 

 Description 

 An AWS identity has deleted Route53 DNS Resolver query logging configuration. 

 Attacker's Goals 

 Evade detection while performing DNS traffic or tunneling. 

 Investigative actions 

 Check if there were any network attempts that fit the deleted rule. 

 Check The cloud identity activity prior/after to the configuration deletion. 

 Previous AWS root account activity 

 Next AWS S3 bucket data retention policy change through S3 Lifecycle rule 

 Was this helpful?
