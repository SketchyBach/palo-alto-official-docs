---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/code-to-cloud/code-to-cloud/references/page-reference-f-call-to-action-routing-by-asset-type1
fetched_at: 2026-09-16T08:47:40Z
source: cortex-platform
---

# Page Reference F: Call-to-action routing by asset type1 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 code-to-cloud 

 Code-to Cloud 

 References 

 Cortex Cloud Posture 

 Page Reference F: Call-to-action routing by asset type1 

 Review call-to-action routing for Code-to-Cloud assets by asset type. 

 This appendix lists the Code-to-Cloud tab's empty-state and partial-state call-to-action routing by asset type and trace condition. 

 Asset type / condition 

 Call-to-action routes to 

 Use when 

 Repository or Software Package 

 Onboard Pipeline 

 The build/deploy pipeline is not yet onboarded, breaking the Build/Deploy trace. 

 General cloud asset 

 Onboard 

 The cloud asset lacks the upstream data source needed to trace it back to code. 

 IaC Resource with YOR tag 

 Onboard 

 The IaC resource carries a YOR tag but the runtime cloud side is not yet onboarded. 

 IaC Resource without YOR tag 

 Enable Tagging Bot 

 No YOR tag exists, so the tagging bot must be enabled to write the trace tag. 

 Partial trace (any supported asset) 

 Add Data Source 

 Some phases are connected and at least one data source is missing to complete the remaining phase. 

 Previous Reference E: Code-to-Cloud Coverage public API 

 Next About Cortex Cloud Data Classification 

 Last updated 14 days ago 

 Was this helpful?
