---
url: https://docs.paloaltonetworks.com/autofocus/autofocus-api/about-the-autofocus-api/autofocus-api-resources/resources-for-direct-searches
fetched_at: 2026-08-13T15:24:43Z
source: palo-alto-main
---

# Resources for Direct Searches Clear

Resources for Direct Searches 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 AutoFocus® API Reference 

 : 
 Resources for Direct Searches 

 Updated on 

 Thu Aug 31 19:09:44 PDT 2023 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 About the AutoFocus API 

 AutoFocus API Overview 

 AutoFocus API Prerequisites 

 AutoFocus API Rate Limits 

 Rate Limits and Points Allotment 

 How to Track Points 

 Points Usage 

 AutoFocus API Resources 

 Resources for Initiating Searches 

 Resources for Viewing Search Results 

 Resources for Direct Searches 

 AutoFocus API STIX Support 

 STIX Elements and Fields 

 Get Started with the AutoFocus API 

 Get Your API Key 

 Make Your First AutoFocus API Calls 

 Start a Search 

 View Results 

 Perform AutoFocus Searches 

 Search Samples and Sessions 

 Search Field Names 

 General Artifacts 

 Sample Artifacts 

 Session Artifacts 

 Analysis Artifacts 

 Linux Artifacts 

 Windows Artifacts 

 Mac Artifacts 

 Android Artifacts 

 Macro Artifacts 

 Search Parameter Types and Operators 

 Search Countries and Country Codes 

 Search Top Tags, Session Histogram, and Session Aggregate Data 

 Search for Signatures 

 View Search Results 

 Perform Direct Searches 

 Get Session Details 

 Get Sample Analysis 

 Get Tags 

 Get Tag Details 

 Get Threat Indicator Feed 

 Get Custom Threat Indicator Feed 

 Get Threat Intelligence Card Summary 

 Export List 

 Get Anti-spyware, Vulnerability, and File-Format Signature 

 Get Antivirus Signature 

 Get DNS Signature 

 Get Geolocation 

 Get Anti-spyware, Vulnerability, and File-Format Release Info 

 AutoFocus API Error Codes 

 AutoFocus API Error Codes 

 Updated on 

 Thu Aug 31 19:09:44 PDT 2023 

 Focus 

 Home 

 AutoFocus 

 AutoFocus® API Reference 

 About
the AutoFocus API 

 AutoFocus API Resources 

 Resources for Direct Searches 

 Download PDF 

 AutoFocus® API Reference 

 Resources for Direct Searches 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 About the AutoFocus API 

 AutoFocus API Overview 

 AutoFocus API Prerequisites 

 AutoFocus API Rate Limits 

 Rate Limits and Points Allotment 

 How to Track Points 

 Points Usage 

 AutoFocus API Resources 

 Resources for Initiating Searches 

 Resources for Viewing Search Results 

 Resources for Direct Searches 

 AutoFocus API STIX Support 

 STIX Elements and Fields 

 Get Started with the AutoFocus API 

 Get Your API Key 

 Make Your First AutoFocus API Calls 

 Start a Search 

 View Results 

 Perform AutoFocus Searches 

 Search Samples and Sessions 

 Search Field Names 

 General Artifacts 

 Sample Artifacts 

 Session Artifacts 

 Analysis Artifacts 

 Linux Artifacts 

 Windows Artifacts 

 Mac Artifacts 

 Android Artifacts 

 Macro Artifacts 

 Search Parameter Types and Operators 

 Search Countries and Country Codes 

 Search Top Tags, Session Histogram, and Session Aggregate Data 

 Search for Signatures 

 View Search Results 

 Perform Direct Searches 

 Get Session Details 

 Get Sample Analysis 

 Get Tags 

 Get Tag Details 

 Get Threat Indicator Feed 

 Get Custom Threat Indicator Feed 

 Get Threat Intelligence Card Summary 

 Export List 

 Get Anti-spyware, Vulnerability, and File-Format Signature 

 Get Antivirus Signature 

 Get DNS Signature 

 Get Geolocation 

 Get Anti-spyware, Vulnerability, and File-Format Release Info 

 AutoFocus API Error Codes 

 AutoFocus API Error Codes 

 Resources for Direct Searches 

 The following table describes resources available for
direct searches. 

 Resources for Direct Searches 

 Format 

 Description 

 Point Cost 

 https://autofocus.paloaltonetworks.com/api/intel/v1/ip/{ip_address}/geolocation 
 JSON 

 View geolocation details of
a specified IP address 

 2 

 https://autofocus.paloaltonetworks.com/api/intel/v1/threatvault/ips/release/{release_id} 
 JSON 

 View anti-spyware, vulnerability,
and file-format release info for a given release ID. 

 2 

 https://autofocus.paloaltonetworks.com/api/intel/v1/threatvault/dns/signature/{DNS_RTDNS_signature_id} 
 JSON 

 View DNS/RTDNS signature details for
a given signature ID. 

 2 

 https://autofocus.paloaltonetworks.com/api/intel/v1/threatvault/ips/signature/{signature_id} 
 JSON 

 View anti-spyware, vulnerability,
and file-format signature details for a given signature ID. 

 2 

 https://autofocus.paloaltonetworks.com/api/intel/v1/threatvault/panav/signature/{antivirus_signature_id} 
 JSON 

 View antivirus signature details based
on a specified signature ID or SHA256 hash. 

 2 

 https://autofocus.paloaltonetworks.com/api/intel/v1/file/{sha256}/signature 
 2 

 /session/{_id} 
 JSON 

 View details of a specified session . 

 2 

 /sample/{sample_id}/analysis/ 
 JSON 

 View file analysis data  related
to a specified sample. The results correspond to the  File Analysis tab
shown when you click a sample hash on the search editor. 

 2 

 /stix/sample/{sample_id}/analysis/ 
 STIX 

 /tags/ 
 JSON 

 View a list of all tags . 

 2 

 /stix/tags/ 
 STIX 

 /tag/{public_tag_name} 
 JSON 

 View tag details  for
the given public tag name. 

 2 

 /stix/tag/{public_tag_name} 
 STIX 

 /export/ 
 JSON 

 Export a list  based
on previously saved artifacts. 

 2 

 /output/threatFeedResult 
 JSON 

 View threat indicators added
to the feed list in the past 24 hours. 

 0 

 /IOCFeed/{outputFeedId}/{outputFeedName} 
 JSON 

 View custom threat indicator
feed details based on the feed type (URL or EDL custom feed)
and authentication details associated with the feed. 

 0 

 EDL/IOCFeed/{outputFeedId}/{outputFeedName} 

 /tic?indicatorType=​{indicator_type}&indicatorValue=​{value_of_indicator}&includeTags=​{true_or_false}' 
 JSON 

 View Threat Intelligence Card
summary based on the indicator type and value (domains, URLs,
file hash, or IP address). 

 0 

 Previous 

 Resources for Viewing Search Results 

 Next 

 AutoFocus API STIX Support 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
