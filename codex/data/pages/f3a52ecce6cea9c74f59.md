---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/case-concepts/case-grouping
fetched_at: 2026-08-13T15:16:41Z
source: cortex-platform
---

# Case grouping | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Case grouping | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Overview of cases 

 Case concepts 

 Issues, findings, and events 

 Case grouping 

 Case scoring 

 Case starring 

 SLAs and tracking 

 What is Causality? 

 Analyze and resolve cases 

 Investigate issues 

 Review findings 

 Investigate artifacts and assets 

 Investigate endpoints 

 Investigate files 

 Cortex Assistant 

 Response actions 

 Forensics 

 Notebooks 

 Build XQL queries 

 Research a known threat 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Detect, Investigate, and respond to threats 

 Investigation and response 

 Case concepts 

 Case grouping 

 Case grouping is a Precision AI™-powered capability that eliminates alert fatigue by automatically consolidating related issues and artifacts into a single unified case. Case grouping links issues that originate from the same attack flow or involve the same entity to reveal the full scope of a case. This approach replaces manual correlation with automated context, allowing you to focus on resolving complete problems rather than triaging isolated events. 

 Grouping methodologies 

 The key grouping methodologies of case grouping are: 

 Artifact association: Groups issues that share core artifacts (for example, SHA256, HostName, UserName). 

 Exact match detection: Groups similar detections for the same entities. 

 Related entities: Groups detections involving related assets within a close timeframe to highlight possible connections. 

 Case qualification for issues 

 Not all issues create cases. When a new issue is created, it is evaluated to determine if it meets the criteria for case promotion. If the issue qualifies, the system attempts to correlate it with an existing case; if no match is found, a new case is generated. Issues that do not meet these requirements are categorized as Insights. 

 The qualification logic varies by domain. For the Security domain, the system promotes issues with Medium severity and above, as well as select Low-severity analytics. Other domains employ more selective promotion based on specific criteria. This logic is dynamic and may be updated to reflect ongoing research and threat relevance. 

 Cortex XSIAM applies the following logic when building cases: 

 Automatic promotion criteria: Issues with the following conditions automatically generate a new case, or join existing cases: 

 Assigned to the Security domain with Medium severity or higher 

 Assigned to the Posture domain and with High severity. 

 Generated from the public API or created from correlations . 

 Low severity handling: Most low severity issues do not initiate case creation, unless specific analytic rules deem action necessary. Low severity issues generated from correlation rules are not grouped into cases. 

 Case grouping thresholds: To keep cases manageable, Cortex XSIAM enforces specific grouping thresholds. For more information see Case thresholds . 

 Grouping artifacts 

 The grouping algorithm evaluates extracted artifacts to determine whether an issue should join an existing case or initiate a new one. Each artifact type is governed by specific logic that accounts for its unique lifecycle and reliability. For example, grouping by Username may be subject to temporal constraints, while IP address logic varies based on whether the address is public, private, or dynamically allocated (DHCP). 

 These proprietary grouping logics are continuously tuned and updated. As a result, artifact behavior and correlation may change over time. 

 If you set up custom detections with correlation rules that trigger issues, you can influence the grouping of the triggered issues by mapping specific fields in your configuration. For more information, see Optimize case grouping in correlations . 

 Integration with SmartScore 

 Case grouping and SmartScore work together to improve triage efficiency. While case grouping provides the full context of an attack, SmartScore assigns a numerical value to that context, indicating the urgency and impact of the case. This allows you to prioritize the most critical cases first. 

 Limitations 

 Case grouping is natively supported within built-in domains only, for example Security. 

 Previous Issues, findings, and events Next Case scoring 

 Last updated 20 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Grouping methodologies 

 Case qualification for issues 

 Grouping artifacts 

 Integration with SmartScore 

 Limitations 

 Was this helpful?
