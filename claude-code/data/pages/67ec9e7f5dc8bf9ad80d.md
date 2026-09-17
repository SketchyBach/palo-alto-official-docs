---
url: https://cortex-docs.paloaltonetworks.com/cortex-xpanse-expander-rn/features-introduced-before-2026/2023-releases/expander-release-21-march
fetched_at: 2026-09-16T09:02:23Z
source: cortex-platform
---

# Expander Release 2.1 (March 2023) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex Xpanse 

 Cortex Xpanse Expander 

 Features introduced before 2026 

 Features introduced in 2023 

 Expander Release 2.1 (March 2023) 

 The table below describes the features and enhancements introduced in the Expander 2.1 release in March 2023. 

 Feature 

 Description 

 Threat Response Center 

 The Threat Response Center in Cortex Xpanse Expander simplifies and streamlines your response to threat events by aggregating the most important information about a threat and its impact on your organization in one place. From the Threat Response Center, you can: 

 Review a curated list of emergent and global threat events , and quickly identify the events that impact your organization. 

 Research a threat event. The Xpanse Security Research Team provides a threat summary, potential exploit consequences, previous exploit activity, and links to other reputable sources for additional information. 

 Assess the impact of a threat event on your organization. Review a detailed list of the affected software, turn on relevant attack surface rules, identify relevant incidents and alerts, and see how the risk is distributed across your organization. 

 Build a Remediation Plan. The Threat Response Center provides remediation guidance for the event, lists of relevant alerts and incidents by status and assignee, and click-throughs to incident and alert pages to begin remediation. 

 See title_title in the Cortex Xpanse Expander User Guide for more information. 

 Automation Configuration Wizard 

 The Automation Configuration Wizard simplifies the automation integration configuration process by providing s a step-by-step, guided experience for installing and configuring the integrations. 

 See title_title for more information. 

 Remediation Path Rules 

 Cortex Xpanse Active Response automates ASM alert investigation and resolution. You can now create Remediation Path Rules to customize Active Response to automatically respond to alerts with actions that meet your specific business requirements and context. 

 See title_title for more information. 

 Remediation Content 

 The Active Response module has been enhanced to include support for the following: 

 Use case coverage for SSH Servers, OpenSSH, Unencrypted FTP, and Unclaimed S3, SMTP servers 

 Azure and Google cloud service providers 

 Enrichment integrations with Tenable.io, Rapid7, splunk 

 See the title_title for more information. 

 Web Attack Surface Management Enhancements 

 Expander now supports alerts and incidents for websites. Two categories of Attack Surface Rules have been created for websites: 

 Web Security Assessments—Detect website security best practice failures. 

 Web Technology CVE Inferences—Alert on web technologies that have inferred CVEs that are both high-confidence matches and high-severity CVEs. 

 An important benefit of Web Technology CVE Inferences is that when they are enabled, Xpanse creates an alert on any new CVE that matches on these criteria. This means you will be notified immediately about zero-day vulnerabilities that are an exact version match. 

 Attack Surface Rules for website are disabled by default. 

 Business Unit (BU) tags are now applied to websites, enabling you to filter and sort websites by BU and to provide scope-based access control by BU. 

 See title_title for details. 

 Asset Explainability 

 Cortex Xpanse provides attribution information about each asset in your asset inventory, so you know at-a-glance why Xpanse believes an asset belongs to your organization. Xpanse displays the following attribution data on the asset details panel and on the assets tab in an incident: 

 Asset Attribution Evidence—Explains how and why an asset was attributed to your organization. 

 Asset Confidence Labels—Enable you to quickly see how confident Xpanse is that an asset belongs to your organization based on specific attribution criteria. 

 Attribution-Related Tags—Enables you to use attribution criteria to filter and sort assets and incidents and to provide scope-based access control. 

 Asset attribution information is provided for all asset types except websites and services. 

 See title_title for details. 

 Risk Scoring 

 You can now prioritize incidents and quantify your organization's relative risk using Risk Scoring. By default, Expander assigns an Xpanse Risk score to every incident using threat and exploit intelligence relevant to the alerts in the incident. In addition to the Xpanse Risk Score that is assigned to each incident, you can also create custom risk-scoring rules and manually assign risk scores. 

 See the following documents for more information about Xpanse Risk Scoring: 

 title_title 

 Customize Risk Scoring 

 XSOAR support for Expander 2.x 

 A new XSOAR Pack has been released to support the new Expander 2.x APIs. This Pack includes the necessary commands and incident fetching capabilities to support Expander 2.x customers who would like to automate the response to Expander findings as well as enrich their incidents with ASM asset and service details. 

 Asset Name Changes 

 The following changes were made to asset names in the Asset Inventory and some dashboards in Expander and the Expander API: 

 Owned Responsive IPs—Previously called Unassociated Responsive IPs 

 Owned IP Ranges—Previously called External IP Ranges 

 You may still see some references to the old names. These will be updated in the next release. 

 See title_title for more information about ASM assets. 

 Syslog Forwarding for Alerts and Management Audit Logs 

 Cortex Xpanse now supports the ability to forward alerts and management audit logs to a syslog receiver. 

 See title_title for details. 

 Cortex Xpanse Expander API Reference, 2.x 

 The Cortex Xpanse API Reference, 2.x , for Expander 2.x is now available. 

 Previous Expander Release 2.2 (June 2023) 

 Next Features introduced in 2022 

 Last updated 3 months ago 

 Was this helpful?
