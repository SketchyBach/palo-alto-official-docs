---
url: https://cortex-docs.paloaltonetworks.com/upgrade-to-cortex-xdr-5/improved-incident-management-workflow-with-cases-and-issues
fetched_at: 2026-09-06T09:52:30Z
source: cortex-platform
---

# Improved incident management workflow with cases and issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Upgrade to Cortex XDR 5 

 Improved incident management workflow with cases and issues 

 In an effort to support a wider range of security use cases, reduce noise in your environment, and provide a seamless workflow experience, the incident management workflow has been redesigned to provide a more comprehensive and flexible solution, covering everything from active threat response to proactive risk reduction. The following sections describe the main changes. 

 Cases and issues 

 Cases and issues form the core framework for identifying and managing threats and risks in your environment: 

 Cases (formerly known as Incidents) are the primary working unit in the platform. They represent one or more related issues, providing a broader context for investigation and response. 

 Issues (formerly known as Alerts) represent individual detections of threats, risks, or policy violations. 

 For customers using Cortex XDR to manage cloud security operations and the SOC, Cases and Issues are now the standardized concepts for identifying and managing problems across your environment. 

 Existing data, configurations, dashboards, queries, playbooks, and APIs will continue to function as before, with no impact. 

 Read more: Overview of cases 

 New workflow experience 

 To streamline investigations and focus on relevant information, Cortex XDR 5 provides an enhanced navigation experience and a new layout for cases and issues. The new navigation panel enables seamless, in-context exploration, allowing you to investigate related data without switching between views or contexts. This helps maintain workflow continuity and keeps investigations on track. For example, when you are investigating an issue, from the issue card, you can click an associated asset to open the asset card in a new tab and switch between tabs without changing the view. 

 In addition, the issue layout has been redesigned to consolidate all relevant information into a single, structured view — reducing clicks and helping you quickly understand the situation and take confident, informed action. Each issue now clearly addresses what happened, how it affects your environment, the supporting evidence, and recommended next steps. 

 Read more: Analyze and resolve cases 

 Schema enhancements and field-level changes 

 As part of this update, we’ve expanded the schema with new data fields that enhance clarity and ensure greater consistency. You can explore these fields by running Cortex Query Language (XQL) queries on the Cases and Issues datasets. 

 All existing fields, including user-defined fields, continue to be fully supported. Notably, the Alert Source field has been renamed to Detection Method to more accurately reflect the data that it represents. 

 API compatibility and new API endpoints 

 When you upgrade to Cortex XDR 5, your existing APIs will continue to function as expected. This ensures uninterrupted support for your automation use cases, including the Alerts API and Incidents API. 

 This release also introduces new Issues and Cases APIs that align with our updated concepts. While your current integrations will remain supported, we recommend transitioning to these new APIs to fully leverage the enhanced data model and capabilities. 

 Read more: Issues APIs and Cases APIs 

 Previous Integrated Cloud Posture capabilities 

 Next Navigation bar and menu enhancements 

 Last updated 1 month ago 

 Was this helpful?
