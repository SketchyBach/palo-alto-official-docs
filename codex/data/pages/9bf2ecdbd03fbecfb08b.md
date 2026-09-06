---
url: https://cortex-docs.paloaltonetworks.com/xsiam-api/cortex-platform/biocs
fetched_at: 2026-09-06T10:55:33Z
source: cortex-platform
---

# BIOCs | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSIAM 

 XSIAM APIs 

 Cortex Platform 

 BIOCs 

 APIs for managing BIOCs 

 Get BIOCs 

 post https://api-yourfqdn /public_api/v1/bioc/get 

 Return a list of BIOCs. You can return all BIOCs or filter results. You can also return extended results with all details included.- The response is concatenated using AND condition (OR is not supported). 

 The maximum result set size is >100. 

 Offset is the zero-based number of incidents from the start of the result set. 

 You must have Rules Edit permissions to run this endpoint. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object Required 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 objects_count integer Optional 

 objects object[] Optional 

 Show properties 

 objects_type string Optional 

 400 

 Bad Request. Got invalid JSON. 

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

 post /public_api/v1/bioc/get 

 HTTP 

 Ask Copy 

 POST /public_api/v1/bioc/get HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 40 

 { 
 "request_data": { 
 "extended_view": false 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "objects_count": 2, 
 "objects": [ 
 { 
 "rule_id": 376, 
 "name": "TestDataSourceTags", 
 "type": "OTHER", 
 "severity": "SEV_030_MEDIUM", 
 "comment": "", 
 "status": "DISABLED", 
 "is_xql": false, 
 "indicator": { 
 "runOnCGO": true, 
 "investigationType": "PROCESS_EXECUTION_EVENT", 
 "investigation": { 
 "PROCESS_EXECUTION_EVENT": { 
 "filter": { 
 "AND": [ 
 { 
 "SEARCH_FIELD": "action_process_username", 
 "SEARCH_TYPE": "EQ", 
 "SEARCH_VALUE": "guyk", 
 "EXTRA_FIELDS": [], 
 "isExtended": false 
 } 
 ] 
 } 
 } 
 } 
 }, 
 "mitre_tactic_id_and_name": [], 
 "mitre_technique_id_and_name": [] 
 }, 
 { 
 "rule_id": 421, 
 "name": "new_bioc_test", 
 "type": "EXECUTION", 
 "severity": "SEV_020_LOW", 
 "comment": "", 
 "status": "ENABLED", 
 "is_xql": true, 
 "indicator": "dataset = xdr_data | filter event_type = 1 and actor_process_image_name = \"SDFDSGFHFN\"", 
 "mitre_tactic_id_and_name": [ 
 "12 - Tactic", 
 "45 - Another Tactic" 
 ], 
 "mitre_technique_id_and_name": [ 
 "123 - Test", 
 "12 - Another Test" 
 ] 
 } 
 ], 
 "objects_type": "bioc" 
 } 

 Insert or update BIOCs 

 post https://api-yourfqdn /public_api/v1/bioc/insert 

 Insert new BIOCs or update existing BIOCs. 

 Note: The BIOC rule_id is tenant specific and can't be used across tenants. Inserting BIOCs with the same rule_id as an existing BIOC on that tenant will overwrite the existing BIOC. 

 Requires the granular RBAC permission for this feature. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object[] Required 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 added_objects object[] Optional 

 List of BIOC objects added. 

 Show properties 

 updated_objects object[] Optional 

 List of BIOC objects updated. 

 Show properties 

 errors string[] Optional 

 A list of errors. 

 400 

 Bad Request. Got invalid JSON. 

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

 post /public_api/v1/bioc/insert 

 HTTP 

 Ask Copy 

 POST /public_api/v1/bioc/insert HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 891 

 { 
 "request_data": [ 
 { 
 "name": "TestBIOC", 
 "type": "EXECUTION", 
 "severity": "SEV_020_LOW", 
 "comment": "", 
 "status": "ENABLED", 
 "is_xql": false, 
 "indicator": { 
 "runOnCGO": true, 
 "investigationType": "FILE_EVENT", 
 "investigation": { 
 "FILE_EVENT": { 
 "filter": { 
 "AND": [ 
 { 
 "OR": [ 
 { 
 "SEARCH_FIELD": "event_sub_type", 
 "SEARCH_TYPE": "EQ", 
 "SEARCH_VALUE": "1", 
 "isExtended": false 
 }, 
 { 
 "SEARCH_FIELD": "event_sub_type", 
 "SEARCH_TYPE": "EQ", 
 "SEARCH_VALUE": "2", 
 "isExtended": false 
 }, 
 { 
 "SEARCH_FIELD": "event_sub_type", 
 "SEARCH_TYPE": "EQ", 
 "SEARCH_VALUE": "3", 
 "isExtended": false 
 }, 
 { 
 "SEARCH_FIELD": "event_sub_type", 
 "SEARCH_TYPE": "EQ", 
 "SEARCH_VALUE": "5", 
 "isExtended": false 
 }, 
 { 
 "SEARCH_FIELD": "event_sub_type", 
 "SEARCH_TYPE": "EQ", 
 "SEARCH_VALUE": "6", 
 "isExtended": false 
 } 
 ] 
 }, 
 { 
 "SEARCH_FIELD": "action_file_name", 
 "SEARCH_TYPE": "EQ", 
 "SEARCH_VALUE": "aaaaaa", 
 "EXTRA_FIELDS": [], 
 "isExtended": false 
 } 
 ] 
 } 
 } 
 } 
 }, 
 "mitre_tactic_id_and_name": [ 
 "" 
 ], 
 "mitre_technique_id_and_name": [ 
 "" 
 ] 
 } 
 ] 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "added_objects": [ 
 { 
 "id": 34, 
 "status": "Created a new BIOC rule with the ID: 34 successfully" 
 } 
 ], 
 "updated_objects": [], 
 "errors": [] 
 } 

 Delete BIOCs 

 post https://api-yourfqdn /public_api/v1/bioc/delete 

 Delete BIOCs selected by filter. 

 Requires the granular RBAC permission for this feature. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object Required 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 objects_count integer Optional 

 Number of BIOC objects deleted. 

 objects integer[] Optional 

 400 

 Bad Request. Got invalid JSON. 

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

 post /public_api/v1/bioc/delete 

 HTTP 

 Ask Copy 

 POST /public_api/v1/bioc/delete HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 111 

 { 
 "request_data": { 
 "extended_view": false, 
 "filters": [ 
 { 
 "field": "severity", 
 "operator": "EQ", 
 "value": "SEV_020_LOW" 
 } 
 ] 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "objects_count": 3, 
 "objects": [ 
 1, 
 3, 
 7 
 ] 
 } 

 Previous Authentication Settings 

 Next Correlation Rules 

 Last updated 1 month ago 

 Was this helpful?
