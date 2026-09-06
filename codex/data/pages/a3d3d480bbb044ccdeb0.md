---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/suspicious-ai-dataset-download
fetched_at: 2026-09-06T11:07:52Z
source: cortex-platform
---

# Suspicious AI Dataset Download | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Suspicious AI Dataset Download 

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
AWS Audit Log OR Azure Audit Log OR Gcp Audit Log 

 Detection Modules 

 Cloud 

 Detector Tags 

 Cloud AI Infrastructure Analytics 

 ATT&CK Tactic 

 Impact (TA0040) 

 ATT&CK Technique 

 Data Manipulation: Stored Data Manipulation (T1565.001) 

 Severity 

 Low 

 Description 

 A model dataset was accessed by an identity that typically doesn't interact with dataset files. MITRE ATLAS Technique: AML.T0035 - ML Artifact Collection. 

 Attacker's Goals 

 Manipulate datasets used by ML models. 

 Investigative actions 

 Determine which dataset was accessed. 

 Examine the changes made to the dataset. 

 Variations 
 Suspicious First-Time AI Dataset Download by Identity 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Impact (TA0040) 

 ATT&CK Technique 

 Data Manipulation: Stored Data Manipulation (T1565.001) 

 Severity 

 Medium 

 Description 

 A model dataset was accessed by an identity that typically doesn't interact with dataset files. MITRE ATLAS Technique: AML.T0035 - ML Artifact Collection. 

 Attacker's Goals 

 Manipulate datasets used by ML models. 

 Investigative actions 

 Determine which dataset was accessed. 

 Examine the changes made to the dataset. 

 Previous Suspicious activity on logging bucket 

 Next Suspicious AI Dataset Label Modification 

 Was this helpful?
