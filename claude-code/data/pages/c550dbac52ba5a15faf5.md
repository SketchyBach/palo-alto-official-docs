---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x-rn/cortex-xdr-release-information/features-introduced-in-2024-xdr/april-2024/feature-enhancements
fetched_at: 2026-09-16T08:59:53Z
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

 Features Introduced in 2024 

 April 2024 

 Feature Enhancements 

 The Cortex XDR 3.10 and Cortex XDR Agent 8.4 releases include the following enhancements: 

 Endpoint Security 

 FEATURE 

 DESCRIPTION 

 Enhanced Vulnerability Assessment 

 Cortex XDR introduces the Enhanced VA mode that uses advanced algorithms and comprehensive databases to deliver in-depth analysis and extensive details on CVEs. The Enhanced VA mode is available on Windows and MacOS endpoints running Cortex XDR agent versions 8.3 and later. 

 Root detection alerts on Android-based endpoints 

 Cortex XDR now includes root detection alerts to help you identify Android devices where malicious tools could be installed using root access privileges. 

 Analytics for Containerized Environments 

 Cortex XDR enhances its container security capabilities with the introduction of a detection analytics pack designed for managed and unmanaged Kubernetes environments. This enhancement strengthens cloud workload protection by enabling proactive identification and mitigation of malicious content inside containerized applications. 

 New configuration options for the iOS malware profile 

 The endpoint iOS malware profile now includes options to configure the use of the Safari browser security module to monitor the browser traffic, and to configure the network security module options to restrict and block network traffic for unsanctioned apps on supervised iOS devices. These enhancements provide proactive gating of suspicious sites, and granular control and monitoring of network traffic. 

 Additional network filtering alerts for iOS-based endpoints 

 Network Shield and Safari Safeguard are two new protection modules in iOS that can help track malicious app activity, unwanted access to malicious web sites and URLs and monitoring of unsanctioned web access. New event alerts for these modules include: 

 Malicious network activity 

 Malicious network activity - digest 

 Company restricted network activity 

 Company restricted network activity digest 

 New dataset for auditing correlation executions 

 (Requires a Cortex XDR Pro license) 

 The new correlations_auditing dataset provides visibility into your correlation rules by logging each rule execution. The dataset records the query times, correlation start/end times, retry attempts, failure reasons, and other useful metrics. 

 Cloud Security Agent 

 (Requires Cortex XDR Cloud per Host license) 

 Unified (single) agent that reduces maintenance and resource overheads while providing runtime security and vulnerability management capabilities for cloud native environments. 

 Requirements: 

 Cortex XDR 3.10 Cloud per Host license 

 Prisma Cloud Compute 

 Cortex XDR agent 8.2.1 or above 

 Supports: 

 Host and Kubernetes Installers 

 Linux only 

 XDR Collectors 

 Windows 1.4.1.1100 and Linux 1.4.1.1089 

 For more information on maintenance releases, see Maintenance Releases . 

 FEATURE 

 DESCRIPTION 

 XDR Collectors 1.4.1 

 This release includes performance improvements and bug fixes. 

 Broker VM 

 Version 23.0.33 (reboot required) 

 For more information on maintenance releases, see Maintenance Releases 

 FEATURE 

 DESCRIPTION 

 Broker VM 23.0.33 

 This release includes performance improvements and bug fixes. 

 External Data Ingestion and Management 

 FEATURE 

 DESCRIPTION 

 TTL for lookup datasets 

 (Requires a Cortex XDR Pro license) 

 Cortex XDR now enables configuring Time To Live (TTL) for lookup datasets, which specify when lookup entries expire and are removed automatically from the dataset. The default value is forever, meaning they never expire. 

 NGFW configuration log ingestion 

 NGFW configuration logs are now ingested, to enrich the firewall data ingested into Cortex XDR. 

 Cortex Query Language (XQL) 

 FEATURE 

 DESCRIPTION 

 New Parsing Rules regexcapture function 

 (Requires a Cortex XDR Pro per GB license) 

 Cortex XDR now supports using a new Parsing Rules function called regexcapture to extract fields using regular expression named groups from a given string and return a JSON object with capturing groups.This function simplifies the Parsing Rules code for fields extraction. 

 Aligned XQL function descriptions and syntax 

 (Requires a Cortex XDR Pro license) 

 The XQL query function and syntax descriptions in Cortex XDR are now aligned with the descriptions found in the Cortex XDR XQL Language Reference guide. This ensures that the same information is provided in both places. 

 Forensics 

 FEATURE 

 DESCRIPTION 

 Forensics investigation 

 Cortex XDR introduces a new Forensic Investigations feature to the Forensics add-on. This includes: 

 Method for grouping all evidence collections and investigate notes in a single location 

 User permissions to limit access to investigation assets 

 Collections page for monitoring the progress of evidence collections 

 An alerts table which is investigation specific 

 A timeline tab containing a normalized view of all tagged rows 

 A new Key Assets & Artifacts tab, which is generated from the Investigation Timeline data 

 Export forensic collections 

 Cortex XDR can now export Hunt or Triage collections into single archives and enable users to track and manage the exported data from the server. 

 Forensic hunting 

 Cortex XDR introduces a new Forensic Hunting feature to the Forensics add-on. This includes: 

 Named collection of user-defined searches 

 Method for running artifact searches at scale 

 Support for custom search parameters across all supported artifacts 

 Configurable timeouts for each artifact search 

 Ability to schedule searches for specific days or time ranges 

 Replaces artifact and search collections in User Agent settings and Forensic searches in the Action Center 

 Previous Release Highlights 

 Next Changed Features 

 Last updated 26 days ago 

 Was this helpful?
