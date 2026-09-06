---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/detect-investigate-and-respond-to-threats/investigation-and-response/overview-of-cases/case-thresholds
fetched_at: 2026-09-06T10:19:09Z
source: cortex-platform
---

# Case thresholds | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Detect, Investigate, and Respond to Threats 

 Investigation and Response 

 Overview of cases 

 Cortex AgentiX 

 Case thresholds 

 Configure case grouping thresholds to keep investigations manageable in Cortex AgentiX. 

 To keep cases manageable, Cortex AgentiX implements case grouping thresholds. When the case reaches a threshold, it stops accepting issues and groups subsequent related issues in a new case. 

 30 days have passed since case creation. 

 14 days have passed since the last issue was detected. 

 A case reaches the 1,000 issue limit. 

 You can track the threshold status in the Issues Grouping Status field in the cases table. 

 Auto-resolved cases 

 If a case is resolved with the status Resolved - Auto Resolved , Cortex AgentiX reopens the case within a six-hour window if a matching issue occurs. The six-hour period is defined by the timestamp of the last issue that was grouped into the case. After the six-hour period, any new issues are linked to a new case for a new investigation. 

 Previous Case lifecycle 

 Next Case scope and impact 

 Last updated 2 months ago 

 Was this helpful?
