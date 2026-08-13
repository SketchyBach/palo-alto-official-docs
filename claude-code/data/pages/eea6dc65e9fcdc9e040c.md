---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/case-concepts/case-scoring
fetched_at: 2026-08-13T15:16:42Z
source: cortex-platform
---

# Case scoring | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Case scoring | Cortex Documentation Portal 

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

 Case scoring 

 A case score is a numeric value that indicates the urgency of a case. Scoring can help you to streamline the process of prioritizing and investigating your cases, and help you to identify the cases that require immediate attention. 

 Types of scoring 

 Cortex XSIAM uses the following scoring methods: 

 Rule-based scoring: The score is determined by user-defined scoring rules that match the issues linked to the case. 

 You create scoring rules that define scores for issues with specific attributes or assets. You can base scoring rules on: 

 Hostnames 

 Asset objects, such as asset names, classes, categories, groups, providers, and business application names. 

 IP addresses 

 Users 

 Active Directory, or Azure groups and organization units 

 (Requires the Cloud Identity Engine to be configured). 

 When an issue is created, Cortex XSIAM searches for scoring rules that match the issue. An issue can match multiple rules or sub-rules. If a match is found, Cortex XSIAM assigns the scores of the matching rules to the issue. If multiple rules match the issue, the issue score is an aggregation of the rule scores. By default, a score is applied only to the first issue in the case that matches the defined rule and sub-rule. 

 You can create a rule hierarchy by setting up sub-rules. If an issue matches one or more sub-rules, the sub-rule scores are also aggregated in the issue score. However, a sub-rule score is only applied to an issue if the top-level rule was a match. 

 To determine the case score, Cortex XSIAM calculates the combined issue score total for all issues in the case. You can see a breakdown of the score by clicking on the score in the details pane. 

 SmartScore: The score is automatically calculated, based on machine learning. 

 SmartScore relies on machine learning, statistical analysis, case attributes, and cross-customer insights to identify high-risk cases. When an issue is created, Cortex XSIAM calculates the SmartScore according to the compiled data. 

 Manual scoring: The score is defined by the user. 

 How Cortex XSIAM assigns the score 

 For Cortex XSIAM to provide effective rule-based scores, you must define accurate scoring rules that are suitable for your environment and workflows. 

 When a case is created, Cortex XSIAM searches for a match between your scoring rules and the issues linked to a case. If a match is found, a rule-based score is assigned. 

 Note 

 SmartScore requires sufficient data to calculate and display the score. On first activation, this can take up to 48 hours. If sufficient data is not available, no score is assigned. 

 If no match is found and there is sufficient data available, Cortex XSIAM assigns a SmartScore. If Cortex XSIAM doesn't have sufficient data to assign a score, you can manually assign a score. 

 To enable Cortex XSIAM to automatically assign a score to a case, you must enable SmartScore and define scoring rules. For more information, see Set up case scoring . 

 You can view the assigned score on the Cases page. 

 Previous Case grouping Next Case starring 

 Last updated 16 days ago 

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

 Types of scoring 

 How Cortex XSIAM assigns the score 

 Was this helpful?
