---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x-rn/cortex-xdr-release-information/features-introduced-in-2024-xdr/june-2024/feature-enhancements
fetched_at: 2026-09-06T10:53:06Z
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

 June 2024 

 Feature Enhancements 

 The Cortex XDR 3.11 and Cortex XDR Agent 8.5 release includes the following enhancements: 

 General 

 FEATURE 

 DESCRIPTION 

 Analytics Tags Highlights 

 Cortex XDR has updated the detectors inventory, introducing new analytics into both new and existing tags: 

 Chromium Extensions Analytics (New) - Detection of malicious browser extensions being loaded or installed, identifying anomalous extensions and installation methods. 

 Malicious Service Analytics (New) - Detection of malicious services being loaded or installed. 

 NDR Lateral Movement Analytics - Advanced lateral movement detection, leveraging Analytics capabilities to identify anomalies in protocols that are used for lateral movement. 

 NDR C2 Analytics - Advanced detection for abnormal network communication that resembles C2 traffic using protocols analysis, local and cross-customer machine learning, and threat intel. 

 Investigation and Response 

 FEATURE 

 DESCRIPTION 

 Combined alerts using correlation rules (Requires a Cortex XDR Pro license) 

 Using the transaction stage in scheduled correlation rules, you can now group events that come from different datasets to trigger a combined alert. 

 Endpoint Security 

 FEATURE 

 DESCRIPTION 

 Device control enhancements 

 Device control profiles for Windows and macOS endpoints now provide granular control for print jobs, in certain conditions. 

 This additional control hardens communication with these types of peripheral devices or operations. 

 Benign with low confidence actions 

 On macOS-based endpoints, new actions are available for executable files that are reported as “benign with low confidence”. This feature adds more granularity to malware detection, and provides enhanced protection against potentially malicious files. 

 XDR Collectors 

 Windows 1.4.1.1100 and Linux 1.4.1.1089 

 For more information on maintenance releases, see Maintenance Releases . 

 FEATURE 

 DESCRIPTION 

 XDR Collectors 1.4.1 

 This release includes performance improvements and bug fixes. 

 Broker VM 

 Version 24.2.8 

 For more information on maintenance releases, see Maintenance Releases . 

 FEATURE 

 DESCRIPTION 

 New ability to increase Broker VM disk size 

 Cortex XDR now supports extending the disk space allocated for data caching in the Broker VM to attain better resilience during network and connectivity issues. Read more in Increase Broker VM storage allocated for data caching . 

 External Data Ingestion and Management 

 FEATURE 

 DESCRIPTION 

 Update lookup datasets using Correlation Rules 

 (Requires a Cortex XDR Pro license) 

 Cortex XDR now enables updating lookup datasets using Correlation Rules. This includes adding and removing lookup entries so you can better correlate data from a data source you provide with the events in your environment. Read more in Create a Correlation Rule . 

 Update lookup datasets using the API 

 Cortex XDR now supports using the API to update lookup datasets, which makes it easier to correlate data from the data source to the events in your environment. The following new APIs are supported: 

 add_data - Adds or updates data in a lookup dataset 

 remove_data - Removes data from a lookup dataset 

 get_data - Gets data from a lookup dataset 

 add_dataset - Adds a lookup dataset 

 delete_dataset - Deletes a dataset 

 get_datasets - Gets a list of available datasets 

 Cortex Query Language (XQL) 

 FEATURE 

 DESCRIPTION 

 New XQL standard deviation comp aggregate functions 

 (Requires a Cortex XDR Pro license) 

 Cortex XDR now supports using the following XQL standard deviation (STD) comp aggregate functions: 

 stddev_pop: Returns the population (biased) variance of a field. 

 stddev_sample: Returns the sample (unbiased) standard deviation of a field. 

 Aligned XQL stages descriptions, syntax, and XQL Helper 

 (Requires a Cortex XDR Pro license) 

 The XQL query stages, syntax descriptions, and descriptions in the XQL Helper in Cortex XDR are now aligned with the descriptions found in the Cortex XDR XQL Language Reference guide. This ensures that the same information is provided in all places. 

 Enhancements to XQL incidr and incidr6 functions and operators 

 (Requires a Cortex XDR Pro license) 

 Cortex Query Language (XQL) now supports defining multiple CIDRs with comma separated syntax in the following functions and operators: 

 incidr and incidr6 functions, where it is now possible to run the function on comma separated CIDRs. 

 incidr , not incidr , incidr6 , and not incidr6 operators, where it is now possible to run the operator on comma separated CIDRs. 

 These changes are only supported building a XQL query with the Query Builder or in Correlation Rules. 

 Forensics 

 FEATURE 

 DESCRIPTION 

 Support Browser Collections in Agent for macOS 

 Cortex XDR now supports Web History searches in Forensic Hunts. Browsers supported are Chrome, Edge, Firefox, Internet Explorer, and Safari along with custom searches for any Chromium-based browser. 

 Previous Release Highlights 

 Next Changed Features 

 Last updated 2 months ago 

 Was this helpful?
