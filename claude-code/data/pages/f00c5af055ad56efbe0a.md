---
url: https://docs.paloaltonetworks.com/autofocus/autofocus-api/get-started-with-the-autofocus-api/make-your-first-autofocus-api-calls/view-results
fetched_at: 2026-08-13T15:24:47Z
source: palo-alto-main
---

# View Results Clear

View Results 

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
 View
Results 

 Updated on 

 Aug 31, 2023 

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

 Aug 31, 2023 

 Focus 

 Home 

 AutoFocus 

 AutoFocus® API Reference 

 Get Started with the AutoFocus API 

 Make Your First AutoFocus API Calls 

 View
Results 

 Download PDF 

 AutoFocus® API Reference 

 View
Results 

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

 View
Results 

 To view the results of your search, include the search
ID ( af_cookie ) at the end of the resource
URI and include the API key in the JSON body of the request: 

 curl -X POST https://autofocus.paloaltonetworks.com/api/v1.0/samples/results/870218db-27cd-4614-ac36-1d87f3f0016e+0 \ 
-H "Content-Type: application/json" \ 
-d '{ 
 "apiKey": " apikey " 
}' 

 The response to the above request includes 50 samples from the
total number flagged as malware. In this example (truncated to the
first two results), the total number of results possible is shown
as “total”: 32811214: 

 { 
 "total": 32811214, 
 "hits": [ 
{ 
 "_id": "c8fac378e1af77b7e0b7025ceaa1edcdd402bee53a7200a38f0c3878b5bc9309", 
 "_source": { 
 "app_packagename": "com.ooedsqz.ihma.fwfl", 
 "ssdeep": "12288:/wxZYgTlF0oikgCTp58auFJMV2XzoZWnuV/YBH:/wxS8FvilK3YFJKAupO", 
 "create_date": "2016-10-14T10:21:25", 
 "sha256": "c8fac378e1af77b7e0b7025ceaa1edcdd402bee53a7200a38f0c3878b5bc9309", 
 "md5": "1400058f42f283e9c25e15d6bf28266c", 
 "filetype": "Android APK", 
 "sha1": "6961b6eadc2b577d10597cd45ce9a83d84f39a8e", 
 "app_name": "com.system.ojjnippitr", 
 "malware": 1, 
 "finish_date": "2016-10-14T10:26:18", 
 "size": 437266, 
 "region": [ 
 "us" 
 ] 
 }, 
 "visible": true 
 }, 
 { 
 "_id": "b183f65d3372f4f15c5ee56f38f0f782f7003dfb932b0166b765621519930cae", 
 "_source": { 
 "app_packagename": "iucCaZa.YfaW.dStoaET", 
 "create_date": "2016-10-14T10:21:18", 
 "sha256": "b183f65d3372f4f15c5ee56f38f0f782f7003dfb932b0166b765621519930cae", 
 "ssdeep": "98304:QJXWrEEhBYPdandOUFJlHczs5DSamn89jRYVb:QJGgEXR3lKqDe8fYB", 
 "md5": "75c2faffadd22485c8b7e98c9cd2f963", 
 "filetype": "Android APK", 
 "sha1": "a3d280dcb3b2e743acb70bfe8c59fe86c7793da6", 
 "app_name": "KYO", 
 "finish_date": "2016-10-14T10:26:12", 
 "malware": 1, 
 "size": 3523310, 
 "tag": [], 
 "region": [ 
 "us" 
 ] 
// TRUNCATED 
], 
 "took": 4744, 
 "af_message": "complete", 
 "af_in_progress": false, 
 "af_complete_percentage": 100, 
 "af_cookie": "53185127-3668-4d7d-85aa-61ef17e8158f+0", 
 "bucket_info": { 
 "minute_points": 200, 
 "daily_points": 25000, 
 "minute_points_remaining": 189, 
 "daily_points_remaining": 24941, 
 "minute_bucket_start": "2015-09-12 23:42:42", 
 "daily_bucket_start": "2015-09-12 14:47:43" 
 } 
} 

 The af_cookie expires 120
seconds after search results are complete (when af_complete_percentage is
100 and af_in_progress is false ).
Until then, you can continually make requests to view results. After
you view a complete list of results, the af_cookie expires. 

 Previous 

 Start a Search 

 Next 

 Perform AutoFocus Searches 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
