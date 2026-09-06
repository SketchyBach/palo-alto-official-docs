---
url: https://cortex-docs.paloaltonetworks.com/xsiam-api/vulnerability-intelligence/affected-software
fetched_at: 2026-09-06T10:56:12Z
source: cortex-platform
---

# Affected Software | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSIAM 

 XSIAM APIs 

 Vulnerability Intelligence 

 Affected Software 

 APIs for managing affected software 

 Get affected software 

 post https://api-yourfqdn /public_api/uvem/v1/get_affected_software 

 Get a filtered list of the software affected by one or more vulnerabilities. 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. 

 Header parameters 

 Authorization string Required 

 {api-key} 

 x-xdr-auth-id string Required 

 {api-key-id} 

 Body 

 application/json 

 request_data object Required 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 reply object Optional 

 Show properties 

 401 

 Unauthorized access. An issue occurred during authentication. This can indicate an incorrect key, id, or other invalid authentication parameters. 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/uvem/v1/get_affected_software 

 HTTP 

 Ask Copy 

 POST /public_api/uvem/v1/get_affected_software HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 220 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "affected_cpu_archs", 
 "operator": "contains", 
 "value": [ 
 "text" 
 ] 
 } 
 ], 
 "sort": { 
 "field": "text", 
 "keyword": "text" 
 }, 
 "search_from": 0, 
 "search_to": 500, 
 "use_page_token": true, 
 "next_page_token": "text" 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "result_count": 1, 
 "total_count": 1, 
 "vulnerabilities": [ 
 { 
 "vulnerability_id": "text", 
 "cvss_score": 1, 
 "cvss_severity": "text", 
 "package_name": "text", 
 "distro": "text", 
 "release": "text", 
 "affected_cpu_archs": [ 
 {} 
 ], 
 "last_modified": null, 
 "affected_versions": [ 
 "text" 
 ] 
 } 
 ], 
 "next_page_token": null 
 } 
 } 

 Previous Vulnerability Intelligence Overview 

 Next Vulnerabilities 

 Last updated 1 month ago 

 Was this helpful?
