---
url: https://docs.paloaltonetworks.com/autofocus/autofocus-api/perform-direct-searches/get-tag-details
fetched_at: 2026-08-13T15:24:52Z
source: palo-alto-main
---

# Get Tag Details Clear

Get Tag Details 

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
 Get Tag Details 

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

 Perform Direct Searches 

 Get Tag Details 

 Download PDF 

 AutoFocus® API Reference 

 Get Tag Details 

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

 Get Tag Details 

 Use this resource to get details on a specific public
tag listed on the AutoFocus web portal. 

 Resource 

 Request
Parameters 

 JSON
Sample 

 STIX
Sample 

 Resource 

 /tag/{public_tag_name} 
/stix/tag/{public_tag_name} 

 Request
Parameters 

 The following table describes parameters for
Get Tag Details requests. 

 The public tag name request
parameter is not case-sensitive. 

 Parameters 

 Description 

 Type 

 Example or Possible
Values 

 public_tag_name 
 ( Required ) Public tag name as listed
in the AutoFocus web portal. The public tag name is visible in the
response when you Get
Tags . 

 string 

 Example: 
 Unit42.CryptoWall 

 JSON
Sample 

 Request 

 Response 

 Request 

 Include
the public tag name to the request URL and include the API key within
the request body. 

 curl -X POST -H "Content-Type: application/json" \ 
-d '{"apiKey": " apikey "}' 'https://autofocus.paloaltonetworks.com/api/v1.0/tag/Unit42.CryptoWall' 

 Response 

 The
response contains details about the specified tag. 

 { 
 "tag":{ 
 "support_id":1, 
 "tag_name":"CryptoWall", 
 "public_tag_name":"Unit42.CryptoWall", 
 "tag_definition_scope_id":4, 
 "tag_definition_scope":"unit42", 
 "tag_definition_status_id":1, 
 "tag_definition_status":"enabled", 
 "count":9279, 
 "lasthit":"2015-12-11 15:06:33", 
 "description":"CryptoWall is a ransomware family which encrypts files on the system and then demands a ransom from the victim before releasing the encryption key. \n\nMore information about CryptoWall is available at the following URLs:\n\nhttp://researchcenter.paloaltonetworks.com/2014/10/tracking-new-ransomware-cryptowall-2-0/\nhttp://malware.dontneedcoffee.com/2015/01/guess-whos-back-again-cryptowall-30.html", 
 "customer_name":"Palo Alto Networks Unit42", 
 "refs":null, 
 "tag_class_id":null, 
 "report_actions":null, 
 "source":null, 
 "comments":[ 

 ] 
 }, 
 "tag_searches":[ 
 { 
 "count":9279, 
 "lasthit":"2015-12-11 15:06:33", 
 "search_name":"1e3f1a50ae9547166d", 
 "tag_definition_search_status_id":1, 
 "tag_definition_search_status":"enabled", 
 "ui_search_definition":"{\"operator\":\"Any\",\"children\":[{\"field\":\"sample.tasks.file\",\"operator\":\"contains\",\"value\":\"3353616\\3353616.exe\"},{\"field\":\"sample.tasks.file\",\"operator\":\"contains\",\"value\":\"Users\\Administrator\\AppData\\Local\\Microsoft\\Internet Explorer\\DECRYPT_INSTRUCTION.TXT\"},{\"field\":\"sample.tasks.file\",\"operator\":\"contains\",\"value\":\"HELP_DECRYPT.PNG\"},{\"field\":\"sample.tasks.file\",\"operator\":\"contains\",\"value\":\"HELP_DECRYPT.URL\"},{\"field\":\"sample.tasks.file\",\"operator\":\"contains\",\"value\":\"HELP_DECRYPT.TXT\"},{\"field\":\"sample.tasks.file\",\"operator\":\"contains\",\"value\":\"HELP_DECRYPT.HTML\"}],\"field\":\"sample.sha256\"}" 
 } 
 ], 
 "aliases":[ 

 ], 
 "related_tags":[ 

 ], 
 "bucket_info":{ 
 "minute_points":200, 
 "daily_points":25000, 
 "minute_points_remaining":196, 
 "daily_points_remaining":24139, 
 "minute_bucket_start":"2015-12-14 15:46:06", 
 "daily_bucket_start":"2015-12-14 13:06:01" 
 } 
} 

 STIX
Sample 

 Request 

 Response 

 Request 

 Include
the public tag name to the request URL and include the API key within
the request body. 

 curl -X POST -H "Content-Type: application/xml" 
-d '<req><apiKey> apikey </apiKey></req>' "https://autofocus.paloaltonetworks.com/api/v1.0/stix/tag/Unit42.CryptoWall" 

 Response 

 The
response contains details about the specified tag. 

 <res> 
 <bucket_info> 
 <minute_points>200</minute_points> 
 <daily_points>25000</daily_points> 
 <minute_points_remaining>198</minute_points_remaining> 
 <daily_points_remaining>24998</daily_points_remaining> 
 <minute_bucket_start>2016-03-09 16:44:45</minute_bucket_start> 
 <daily_bucket_start>2016-03-09 16:44:45</daily_bucket_start> 
 </bucket_info> 
 <stix> 
 <stix:STIX_Package xmlns:stix="http://stix.mitre.org/stix-1" xmlns:autofocus="https://autofocus.paloaltonetworks.com" xmlns:cybox="http://cybox.mitre.org/cybox-2" xmlns:cyboxCommon="http://cybox.mitre.org/common-2" xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2" xmlns:indicator="http://stix.mitre.org/Indicator-2" xmlns:stixCommon="http://stix.mitre.org/common-1" xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="autofocus:Package-77c5b3d7-867d-466f-9816-2141f59cd809" version="1.1.1" timestamp="2016-03-10T00:44:46.003067+00:00"> 
 <stix:Indicators> 
 <stix:Indicator id="autofocus:indicator-73a63fc4-dea5-4a81-8e44-ca8934ba1c3c" timestamp="2016-03-06T01:24:06" xsi:type="indicator:IndicatorType"> 
 <indicator:Title>Unit42.CryptoWall</indicator:Title> 
 <indicator:Description>CryptoWall is a ransomware family which encrypts files on the system and then demands a ransom from the victim before releasing the encryption key. 

More information about CryptoWall is available at the following URLs: 

http://researchcenter.paloaltonetworks.com/2014/10/tracking-new-ransomware-cryptowall-2-0/ 
http://malware.dontneedcoffee.com/2015/01/guess-whos-back-again-cryptowall-30.html</indicator:Description> 
 <indicator:Short_Description>Tag Name: CryptoWall, Scope: unit42, Status: enabled, Aliases:</indicator:Short_Description> 
 <indicator:Composite_Indicator_Expression operator="OR"> 
 <indicator:Indicator id="autofocus:indicator-d87a50e5-ef31-454a-95bc-c5efcdde276b" timestamp="2016-03-06T01:24:06" xsi:type="indicator:IndicatorType"> 
 <indicator:Description><?xml version="1.0" encoding="UTF-8"?><query><operator>Any</operator><children><item><field>sample.tasks.file</field><operator>contains</operator><value>3353616\3353616.exe</value></item><item><field>sample.tasks.file</field><operator>contains</operator><value>Users\Administrator\AppData\Local\Microsoft\Internet Explorer\DECRYPT_INSTRUCTION.TXT</value></item><item><field>sample.tasks.file</field><operator>contains</operator><value>HELP_DECRYPT.PNG</value></item><item><field>sample.tasks.file</field><operator>contains</operator><value>HELP_DECRYPT.URL</value></item><item><field>sample.tasks.file</field><operator>contains</operator><value>HELP_DECRYPT.TXT</value></item><item><field>sample.tasks.file</field><operator>contains</operator><value>HELP_DECRYPT.HTML</value></item></children><field>sample.sha256</field></query></indicator:Description> 
 <indicator:Short_Description>Status: enabled</indicator:Short_Description> 
 <indicator:Sightings sightings_count="9676" /> 
 </indicator:Indicator> 
 </indicator:Composite_Indicator_Expression> 
 <indicator:Sightings sightings_count="9676" /> 
 <indicator:Producer> 
 <stixCommon:Description /> 
 <stixCommon:Identity> 
 <stixCommon:Name>Palo Alto Networks Unit42</stixCommon:Name> 
 </stixCommon:Identity> 
 </indicator:Producer> 
 </stix:Indicator> 
 </stix:Indicators> 
 </stix:STIX_Package> 
 </stix> 
</res> 

 Previous 

 Get Tags 

 Next 

 Get Threat Indicator Feed 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
