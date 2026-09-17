---
url: https://cortex-docs.paloaltonetworks.com/xdr-5-api/cortex-platform/indicator-rules
fetched_at: 2026-09-16T09:03:50Z
source: cortex-platform
---

# Indicator Rules | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XDR 

 XDR 5.x APIs 

 Cortex Platform 

 Indicator Rules 

 APIs for managing indicator rules 

 Insert Simple Indicators, CSV 

 post https://api-yourfqdn /public_api/v1/indicators/insert_csv 

 Upload IOCs in CSV format that you retrieved from external threat intelligence sources. 

 Note: Cortex XDR does not scan historic data, but rather only new incoming data. 

 Required license: Cortex XDR. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data string Required 

 The body of this request contains a JSON object with a single field: request_data . This field is required. Its value is as string containing two or more comma-separated lines. The first line must contain the CSV header. All subsequent lines must represent IOC data. Each line must include at a minimum the required CSV fields, which are identified below. To help you validate the upload, you can send a separate validate field to view an array of errors with an unsuccessful call. 

 For the complete list of supported fields, see Insert CSV Fields . 

 validate boolean Optional 

 Indicates whether to return an array of errors in the case of an unsuccessful update indicator API request. 

 Responses 

 200 

 SUCCESS 

 application/json 

 reply object Optional 

 Show properties 

 400 

 Bad Request. Got an invalid JSON. 

 application/json 

 401 

 Unauthorized access. An issue occurred during authentication. This can indicate an incorrect key, id, or other invalid authentication parameters. 

 application/json 

 402 

 Unauthorized access. User does not have the required license type to run this API. 

 application/json 

 403 

 Forbidden access. The provided API Key does not have the required RBAC permissions to run this API. 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/indicators/insert_csv 

 HTTP 

 Ask Copy 

 POST /public_api/v1/indicators/insert_csv HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 430 

 { 
 "request_data": "indicator,type,severity,expiration_date, comment,reputation,reliability,class,vendor.name,vendor.reputation, vendor.reliability\n B2c74bf609159f27dd89a829501ec34d6596d8b39a2cce7add73a8207088817a, HASH,HIGH,1587054895000,This is an example IOC,BAD,D,Malware,IBM, GOOD,B\n A2c74bf609159f27dd89a829501ec34d6596d8b39a2cce7add73a8207088817a, HASH,LOW,1587054895000,This is an example IOC,GOOD,D,Malware,PANW, BAD,A\n" 
 } 

 Request filtered results 

 200 

 SUCCESS 

 Ask Copy 

 { 
 "reply": { 
 "success": false, 
 "validation_errors": [ 
 { 
 "indicator": "testtest.com", 
 "error": "Got type: HASH, Indicator: testtest.com mismatch" 
 } 
 ] 
 } 
 } 

 Insert Simple Indicators, JSON 

 post https://api-yourfqdn /public_api/v1/indicators/insert_jsons 

 Upload IOCs as JSON objects that you retrieved from external threat intelligence sources. 

 Note: Cortex does not scan historic data, rather only new incoming data. 

 Required license: Cortex XDR. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object[] Required 

 Show properties 

 validate boolean Optional 

 Whether to return an array of errors in the case of an unsuccessful update indicator API request. 

 Responses 

 200 

 OK 

 application/json 

 reply object Optional 

 JSON object containing a query result. 

 Show properties 

 400 

 Bad Request. Got an invalid JSON. 

 application/json 

 401 

 Unauthorized access. An issue occurred during authentication. This can indicate an incorrect key, id, or other invalid authentication parameters. 

 application/json 

 402 

 Unauthorized access. User does not have the required license type to run this API. 

 application/json 

 403 

 Forbidden access. The provided API Key does not have the required RBAC permissions to run this API. 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/indicators/insert_jsons 

 HTTP 

 Ask Copy 

 POST /public_api/v1/indicators/insert_jsons HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 306 

 { 
 "request_data": [ 
 { 
 "indicator": "<hash_value>", 
 "type": "HASH", 
 "severity": "MEDIUM", 
 "comment": "test", 
 "reputation": "GOOD", 
 "reliability": "D", 
 "vendors": [ 
 { 
 "vendor_name": "V1", 
 "reliability": "A", 
 "reputation": "GOOD" 
 }, 
 { 
 "vendor_name": "V2", 
 "reliability": "A", 
 "reputation": "SUSPICIOUS" 
 } 
 ], 
 "class": "Malware" 
 } 
 ], 
 "validate": true 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "success": true, 
 "validation_errors": [ 
 { 
 "indicator": "testtest.com", 
 "error": "Got type: HASH, Indicator: testtest.com mismatch" 
 } 
 ] 
 } 
 } 

 Previous Endpoint Management 

 Next IOCs 

 Last updated 1 month ago 

 Was this helpful?
