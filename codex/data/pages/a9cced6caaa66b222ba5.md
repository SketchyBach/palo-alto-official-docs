---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/analyze-and-resolve-cases/resolve-the-case/monitor-and-track-resolution-times
fetched_at: 2026-08-13T15:17:07Z
source: cortex-platform
---

# Monitor and track resolution times | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Monitor and track resolution times | Cortex Documentation Portal 

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

 Analyze and resolve cases 

 Review all cases 

 Start case analysis 

 Establish case context 

 Analyze case details 

 Resolve the case 

 Resolution Center 

 Collaborative notes and comments 

 How to resolve a case 

 Resolution reasons for cases and issues 

 Monitor and track resolution times 

 Cortex Response and Remediation content pack 

 Additional case actions 

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

 Analyze and resolve cases 

 Resolve the case 

 Monitor and track resolution times 

 By default, the system tracks the resolution of cases and issues using built-in fields: Resolution Timer and Resolution SLA . You can use these fields to monitor deadlines at a glance or sort by SLA status. These fields are available for tracking case resolution on the Cases page, and issue resolution on the Issues page. 

 Resolution Timer 

 Automatically tracks the total duration from creation to resolution. The timer stops when the status changes to Resolved. 

 Timer behavior after reopening 

 If a case or issue is reopened, the timer resumes and includes the entire elapsed time, including the period when it was closed. 

 Resolution SLA 

 Measures your compliance against defined SLA targets. By default, no SLA rules are preconfigured, giving you the flexibility to define SLAs that work best for your environment. 

 Once configured, the system evaluates the rules in order and the first matching rule is applied. You can configure SLAs for your cases and issues, as explained in Create an SLA rule . 

 Case SLAs 

 To ensure high-level visibility and help you adhere to your organizational goals, all active SLAs are visible directly within the product workflows: 

 Real-time visibility: When you open a case, the status of all active SLAs are displayed directly in the case header. 

 Parallel SLA tracking: Cases support running multiple SLAs concurrently. While the default Resolution SLA tracks the baseline lifecycle, you can create additional SLA fields to measure separate milestones, such as initial response times, or to enforce unique targets for specific customer tiers. For more information about setting up additional case SLAs, see Create case timers and SLAs . 

 Table filtering and sorting: The predefined Resolution SLA field and any additional SLA fields can be monitored in the Cases table, allowing you to filter, sort, and prioritize your queue by custom compliance metrics. For more information, see Monitor the status of issue resolution SLAs . 

 Previous Resolution reasons for cases and issues Next Cortex Response and Remediation content pack 

 Last updated 19 days ago 

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

 Resolution Timer 

 Resolution SLA 

 Was this helpful?
