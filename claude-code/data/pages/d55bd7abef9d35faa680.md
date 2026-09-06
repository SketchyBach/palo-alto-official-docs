---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x-rn/cortex-xdr-release-information/features-introduced-in-2023-xdr/october-2023/feature-enhancements
fetched_at: 2026-09-06T10:53:09Z
source: cortex-platform
---

# Feature Enhancements | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XDR 

 Cortex XDR 3.x 

 Release Information 

 Features Introduced in 2023 

 October 2023 

 Feature Enhancements 

 The Cortex XDR 3.8 and Cortex XDR Agent 8.2 releases include the following enhancements: 

 Investigation and Response 

 Feature 

 Description 

 Incident page enhancements 

 The Incident Overview tab was revised to provide an improved incident response and investigation experience, including fonts, sizing, and other UI improvements. 

 New incident lifecycle widgets 

 New and improved widgets help you measure the operational efficiency of incident and alert handling, and identify issues in the incident response process. The widgets identify peaks in incident and alert creation, provide visibility into the incident lifecycle, and help balance workloads by identifying the incidents assigned to each analyst: 

 Open Incidents 

 Incidents by Status Duration 

 Open Incidents by Assignee Over Time 

 Endpoint Security 

 Feature 

 Description 

 Risky prevention policies notifications 

 Cortex XDR introduces a new feature that identifies risky prevention policies based on Palo Alto Networks best-practice policy settings. Admins can review and update flagged policies to enhance global security posture. 

 XDR Collectors 

 Windows 1.4.1.1100 and Linux 1.4.1.1046 

 For more information on maintenance releases, see Maintenance Releases 

 Feature 

 Description 

 XDR collectors upgraded Filebeat and Winlogbeat versions 

 (Requires a Cortex XDR Pro per GB license) 

 Cortex XDR now supports using Filebeat and Winlogbeat version 8.8.1 when using XDR collectors on Windows and Linux machines. 

 Updated XDR Collectors for Linux and Windows Python versions 

 (Requires a Cortex XDR Pro per GB license) 

 Cortex XDR has upgraded the XDR Collectors to use Linux Python 3.9.17 and Windows Python 3.7.17 on 32-bit or 64-bit. 

 Broker VM 

 Version 21.1.12 

 For more information on maintenance releases, see Maintenance Releases 

 Feature 

 Description 

 Broker VM 21.1.12 

 This release includes performance improvements and bug fixes. 

 External Data Ingestion and Management 

 Feature 

 Description 

 Lookup management enhancements 

 The Files and Folders Collector was enhanced with an option to automatically collect reference data into a lookup dataset. Read more in Activate the Files and Folders Collector . 

 While importing data manually from a file into an existing dataset using the Add Lookup option in the Dataset Management screen, you can now select to replace the existing data in the dataset. 

 You can now manually edit existing lookup datasets to update reference data directly from the console. 

 Cortex Query Language (XQL) 

 Feature 

 Description 

 New XQL convert_to_base_64 function 

 (Requires a Cortex XDR Pro license) 

 Corex XDR now supports a new function called convert_to_base_64 , which converts the base64-decoded input to the encoded string format. See more in convert_to_base_64 . 

 New XQL datasets subset of xdr_data 

 (Requires a Cortex XDR Pro license) 

 To provide faster query results, instead of querying the entire xdr_data dataset, Cortex XDR added the following three datasets: 

 vpn_logs : VPN logs, such as GlobalProtect. 

 auth_logs : Authentication logs, such as Okta. 

 login_logs : Login logs, such as WEC. 

 The fields contained in any of these datasets are a subset of the fields in the xdr_data dataset. 

 New system field added to XDR Collectors datasets 

 (Requires a Cortex XDR Pro per GB license) 

 A new system field called _collector_internal_ip_address was added to all XDR Collector datasets including Filebeat and Winlogbeat data. This system field provides the internal IP of the endpoint. 

 General 

 Feature 

 Description 

 New Cortex In-App documentation 

 Cortex XDR now includes in-product documentation that helps you find information about new and existing features, reference material, and common workflows. While you're working with Cortex products (XDR/XSIAM/XSOAR), the documentation will launch relative to your current location from within the product. 

 Stay tuned for the Help Chat (which will gradually be rolled out), as part of the Cortex XDR Help Center. With the AI driven Help Chat, you will be able to asks questions about features and tasks and immediately receive a response. 

 Enabling automatic backup in Cortex XDR 

 To better secure your machines against ransomware attacks, a new solution based on native operating system backup mechanisms (Time Machine from MacOS and Shadow Copy from Windows) allows customers to turn on automatic backups from Cortex XDR. 

 Cortex SSO improvements 

 For SSO configuration of Cortex XDR, you now have the option to enter a metadata URL, rather than manually providing the IdP SSO URL, issuer ID and x.509 certificate. 

 Refresh all dashboard widgets 

 Dashboards now include a refresh icon that updates the data for all dashboard widgets with a single click. 

 Analytics Detector Tags 

 A new tag type, Detector Tags, has been added to Alerts, Incidents, and Analytics BIOC Rules. This tag enables you to filter for specific detectors such as Identity Threat, Identity Analytics, Alert Analytics. The addition of Detector Tags enables more efficient data analysis and threat management. 

 Previous Release Highlights 

 Next Changed Features 

 Last updated 2 months ago 

 Was this helpful?
