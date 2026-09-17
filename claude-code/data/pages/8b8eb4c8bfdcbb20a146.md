---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/investigate-artifacts-and-assets/investigate-a-file-and-process-hash
fetched_at: 2026-09-16T08:47:14Z
source: cortex-platform
---

# Investigate a file and process hash | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cases and issues 

 Investigation and response 

 Investigate artifacts and assets 

 Cortex Cloud Posture 

 Investigate a file and process hash 

 Investigate a file or process hash. 

 Drilldown on a file or process hash on the Hash View . On this view you can investigate and take actions on SHA256 hash processes and files, and see information about a specific SHA256 hash over a defined 24-hour or 7-day time frame. In addition, you can drill down on each of the process executions, file operations, cases, actions, and threat intelligence reports relating to the hash. 

 How to investigate a file or process hash 

 Open the Hash View . 

 Identify the file or process hash that you want to investigate and select Open Hash View . 

 In the left panel, review the overview of the hash. 

 Review the signature of the hash, if available. 

 Identify the WildFire verdict. 

 The color of the hash value is color-coded to indicate the WildFire report verdict:

 Add an Alias or Comment to the hash value. 

 Review threat intelligence for the hash. 

 Depending on the threat intelligence sources that are integrated with Cortex Cloud, the following threat intelligence might be available: 

 Virus Total score and report. 

 Note: Requires a license key. Go to Settings → Configurations → Integrations → Threat Intelligence . 

 IOC Rule, if applicable, including the IOC Severity, Number of hits, and Source according to the color-coded values: 

 WildFire analysis report. 

 Review if the hash has been added to: 

 Allow List or Block List. 

 Quarantined, select the number of endpoints to open the Quarantine Details view. 

 Review the recent open cases that contain the hash as part of the case's Key Artifacts according to the Last Updated timestamp. To dive deeper into specific cases, select the Case ID. 

 In the right hand view, use the filter criteria to refine the scope of the IP address information that you want to visualize. 

 Review the selected data. 

 To view the most recent processes executed by the hash, select Recent Process Executions. To run a query on the hash, select Search all Process Executions. 

 (Optional) Perform actions on the hash. 

 Previous Investigate an asset 

 Next Investigate a user 

 Last updated 1 month ago 

 Was this helpful?
