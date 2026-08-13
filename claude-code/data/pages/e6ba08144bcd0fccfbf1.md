---
url: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api/about-the-wildfire-api/wildfire-api-changelog
fetched_at: 2026-08-13T17:48:12Z
source: palo-alto-main
---

# WildFire API Changelog Clear

WildFire API Changelog 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 WildFire API Reference 

 : 
 WildFire API Changelog 

 Updated on 

 Wed Jun 10 20:08:27 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 About the WildFire API 

 Standalone WildFire API Subscription 

 WildFire API Access Control 

 Authenticate Access 

 WildFire API Limits 

 WildFire API Resources 

 WildFire API Changelog 

 Get Started with the WildFire API 

 WildFire API Token Authentication 

 Get Your Advanced WildFire Cloud API Key for Token-Based Authentication 

 Generate an Access Token for WildFire API Requests 

 Manage Advanced WildFire Cloud API Tokens 

 View WildFire Cloud API Token Usage Statistics and Details in Strata Cloud Manager 

 WildFire API Token Authentication Example 

 WildFire API Key Authentication 

 Get Your Advanced WildFire Public Cloud API Key From the WildFire Portal 

 Get Your Advanced WildFire Public Cloud API Key From the Palo Alto Networks Support Portal 

 View WildFire API Usage Statistics From the Palo Alto Networks Support Portal 

 Advanced WildFire Cloud API Migration 

 WildFire Appliance API Authentication 

 Get Your WildFire Appliance API Key 

 Manage WildFire Appliance API Keys 

 View All API Keys 

 Disable or Enable an API Key 

 Delete an API Key 

 Export API Key using Secure Copy (SCP) 

 Import API Keys using Secure Copy (SCP) 

 Make Your First WildFire API Call 

 WildFire API Best Practices 

 Submit Files and Links through the WildFire API 

 Submit a Local File to WildFire (API) 

 Submit a Remote File to WildFire (API) 

 Submit a Website Link to WildFire (API) 

 Submit Multiple Website Links to WildFire (API) 

 Submit a Sample Verdict Change (API) 

 Get WildFire Information through the WildFire API 

 Get a WildFire Verdict (WildFire API) 

 Get Multiple WildFire Verdicts (WildFire API) 

 Get a List of Samples with Changed WildFire Appliance Verdicts (WildFire API) 

 Get a Sample (WildFire API) 

 Get a Packet Capture (WildFire API) 

 Get a WildFire Analysis Report (WildFire API) 

 Get a Malware Test File (WildFire API) 

 Get URL Web Artifacts 

 WildFire API Error Codes 

 Updated on 

 Wed Jun 10 20:08:27 PDT 2026 

 Focus 

 Home 

 WildFire 

 WildFire API Reference 

 About the WildFire API 

 WildFire API Changelog 

 Download PDF 

 WildFire API Reference 

 WildFire API Changelog 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 About the WildFire API 

 Standalone WildFire API Subscription 

 WildFire API Access Control 

 Authenticate Access 

 WildFire API Limits 

 WildFire API Resources 

 WildFire API Changelog 

 Get Started with the WildFire API 

 WildFire API Token Authentication 

 Get Your Advanced WildFire Cloud API Key for Token-Based Authentication 

 Generate an Access Token for WildFire API Requests 

 Manage Advanced WildFire Cloud API Tokens 

 View WildFire Cloud API Token Usage Statistics and Details in Strata Cloud Manager 

 WildFire API Token Authentication Example 

 WildFire API Key Authentication 

 Get Your Advanced WildFire Public Cloud API Key From the WildFire Portal 

 Get Your Advanced WildFire Public Cloud API Key From the Palo Alto Networks Support Portal 

 View WildFire API Usage Statistics From the Palo Alto Networks Support Portal 

 Advanced WildFire Cloud API Migration 

 WildFire Appliance API Authentication 

 Get Your WildFire Appliance API Key 

 Manage WildFire Appliance API Keys 

 View All API Keys 

 Disable or Enable an API Key 

 Delete an API Key 

 Export API Key using Secure Copy (SCP) 

 Import API Keys using Secure Copy (SCP) 

 Make Your First WildFire API Call 

 WildFire API Best Practices 

 Submit Files and Links through the WildFire API 

 Submit a Local File to WildFire (API) 

 Submit a Remote File to WildFire (API) 

 Submit a Website Link to WildFire (API) 

 Submit Multiple Website Links to WildFire (API) 

 Submit a Sample Verdict Change (API) 

 Get WildFire Information through the WildFire API 

 Get a WildFire Verdict (WildFire API) 

 Get Multiple WildFire Verdicts (WildFire API) 

 Get a List of Samples with Changed WildFire Appliance Verdicts (WildFire API) 

 Get a Sample (WildFire API) 

 Get a Packet Capture (WildFire API) 

 Get a WildFire Analysis Report (WildFire API) 

 Get a Malware Test File (WildFire API) 

 Get URL Web Artifacts 

 WildFire API Error Codes 

 WildFire API Changelog 

 This section describes the updates made
to the WildFire API resources. 

 September 09, 2022 

 Notice of
future WildFire API file submissions and queries change for Proofpoint
integrations. 

 The following note has been added to WildFire API Limits : “Effective
February 1, 2023, all submissions from Proofpoint integration will
be counted against daily WildFire API limits. This change affects
only Proofpoint integration through the WildFire API. It does not
affect any WildFire file submissions via other Palo Alto Networks
products, such as the NGFW platform, Prisma, or Cortex.” 

 June 10, 2022 

 Added WildFire
API Integration Support for Prisma Cloud Compute and Prisma Access. 

 Customers
with Prisma Cloud Compute and Prisma Access subscriptions can now
submit samples and query for reports using the WildFire public API. 

 July 21, 2020 

 Reverted API
Endpoints 

 The /submit/link and /submit/links endpoints
have been reverted to return SHA and MD5 hashes values in the XML
response. 

 July 2, 2020 

 Newly Added Parameters
for Existing Endpoints 

 The /get/verdict and /get/report endpoints
now support the url parameter to facilitate
retrieval of URL verdicts and a single specified WildFire URL analysis
report, respectively. 

 Notice of WildFire API Usage Discrepancies Based on Region 

 URL
Analysis is currently operational only in the WildFire global (U.S.)
cloud. Using the /get/verdicts and /get/report endpoints
to retrieve URL verdicts and reports in any of the unsupported regional
clouds might produce different results. 

 Notice of Limited Support 

 The /get/pcap and /get/verdicts endpoints
do not support URL analysis functionality at this time. 

 Modified API Response Behavior 

 The /submit/link and /submit/links endpoints
no longer returns the hash values in the response if the URL was
processed using URL analysis. Regional WildFire clouds operating
the legacy elink analyzer will continue to return the hash values. 

 New API Endpoint 

 The following API endpoint
was added to support retrieval of web artifacts generated during
URL analysis: /get/webartifacts 

 Previous 

 WildFire API Resources 

 Next 

 Get Started with the WildFire API 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
