---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/threat-management/detection-rules/what-are-detection-rules/whats-an-ioc
fetched_at: 2026-09-06T09:33:42Z
source: cortex-platform
---

# What's an IOC? | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Detect, Investigate, and respond to threats 

 Threat management 

 Detection rules 

 What are detection rules? 

 Cortex XSIAM 

 What's an IOC? 

 Learn how Cortex XSIAM IOC rules detect known malicious or suspicious artifacts. 

 Indicators of compromise (IOCs) enable Cortex XSIAM to generate issues about known malicious objects on endpoints across the organization. You can load collections of IOCs from threat-intelligence sources into Cortex XSIAM or define them individually. 

 Note 

 Cortex XSIAM supports a maximum of 4,000,000 IOCs. 

 You can define the following types of IOCs: 

 Full path 

 File name 

 Domain 

 Destination IP address 

 MD5 hash 

 SHA256 hash 

 After you load or define IOCs, the tenant checks for matches in the xdr_data dataset that contains all the information collected about the endpoints and the network. Cortex XSIAM looks for IOC matches in all data collected in the past and continues to evaluate any new data it receives in the future. 

 Issues for IOCs are identified by the source type of the IOC. 

 Previous What are detection rules? 

 Next IOC rule details 

 Last updated 1 month ago 

 Was this helpful?
