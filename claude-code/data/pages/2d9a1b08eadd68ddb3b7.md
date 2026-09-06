---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-api/restore-distributions
fetched_at: 2026-09-06T11:20:05Z
source: cortex-platform
---

# Restore Distributions overview | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex Cloud 

 Cortex Cloud APIs 

 Restore Distributions 

 Restore Distributions overview 

 The Restore Distributions API lets you restore a previously deleted agent installation package (distribution) in Cortex Cloud. 

 When a distribution is deleted — either via the Delete agent installation packages API or from the Agent Installations screen in Cortex Cloud — agents that reference that package can no longer register. Restoring the distribution re-enables agent registration. 

 If the distribution is already in an active state, the API returns a message indicating it is already restored rather than returning an error. 

 Using this API, you can: 

 Restore a deleted agent installation package by its distribution ID. 

 Required license: Cortex Cloud Runtime Security. In Cortex Cloud Posture Security, you need the Cortex Cloud Runtime Security add-on. 

 Previous Models 

 Next Restore Distributions 

 Last updated 16 days ago 

 Was this helpful?
