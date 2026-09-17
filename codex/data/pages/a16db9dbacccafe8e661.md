---
url: https://cortex-docs.paloaltonetworks.com/xsiam-api/cortex-platform/scheduled-queries
fetched_at: 2026-09-16T09:03:58Z
source: cortex-platform
---

# Scheduled Queries | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSIAM 

 XSIAM APIs 

 Cortex Platform 

 Scheduled Queries 

 APIs for managing scheduled queries 

 Get scheduled queries 

 post https://api-yourfqdn /public_api/v1/scheduled_queries/list 

 Return a list of scheduled queries. You can return all scheduled queries or filter results. You can also return extended results with all details included. 

 You must have Instance Administrator permissions to run this endpoint. 

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

 post /public_api/v1/scheduled_queries/list 

 HTTP 

 Ask Copy 

 POST /public_api/v1/scheduled_queries/list HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 41 

 { 
 "request_data": { 
 "extended_view": "True" 
 } 
 } 

 Get all scheduled queries in extended view 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "data": [ 
 { 
 "query_def_id": "text", 
 "query_definition_name": "text", 
 "xql": "text", 
 "timeframe": { 
 "relativeTime": "text" 
 }, 
 "schedule": { 
 "run_date": 1, 
 "trigger_type": "text" 
 }, 
 "tenants": {}, 
 "enable": true 
 } 
 ], 
 "filter_count": 1, 
 "total_count": 1 
 } 
 } 

 application/json 

 Insert or update scheduled queries 

 post https://api-yourfqdn /public_api/v1/scheduled_queries/insert 

 Insert new scheduled queries or update existing scheduled queries. 

 You must have Instance Administrator permissions to run this endpoint. 

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

 reply object Optional 

 Upon successful insert or update, the reply returns each individual query_id with the query definitions. 
If the insert or update failed, the reply will include the scheduled query name and the error message. 

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

 post /public_api/v1/scheduled_queries/insert 

 HTTP 

 Ask Copy 

 POST /public_api/v1/scheduled_queries/insert HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 197 

 { 
 "request_data": [ 
 { 
 "query_definition_name": "debug_john_api", 
 "xql": "dataset = xdr_data | limit 10", 
 "timeframe": { 
 "relativeTime": 46400000 
 }, 
 "schedule": { 
 "trigger_type": "date", 
 "run_date": 4677621540000 
 } 
 } 
 ] 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "qc_0123456789_01": { 
 "query_definition_name": "test_1", 
 "xql": "dataset = xdr_data | limit 1", 
 "timeframe": { 
 "relativeTime": 86400000 
 }, 
 "schedule": { 
 "trigger_type": "date", 
 "run_date": 1824072062000 
 } 
 }, 
 "qc_0123456789_02": { 
 "query_definition_name": "test_2", 
 "xql": "dataset = xdr_data | limit 1", 
 "timeframe": { 
 "relativeTime": 86400000 
 }, 
 "schedule": { 
 "trigger_type": "date", 
 "run_date": 1824072062000 
 } 
 } 
 } 
 } 

 Delete a scheduled query 

 post https://api-yourfqdn /public_api/v1/scheduled_queries/delete 

 Delete scheduled queries. 

 You must have Instance Administrator permissions to run this endpoint. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data string[] Required 

 Responses 

 200 

 OK 

 application/json 

 reply object[] Optional 

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

 post /public_api/v1/scheduled_queries/delete 

 HTTP 

 Ask Copy 

 POST /public_api/v1/scheduled_queries/delete HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 69 

 { 
 "request_data": [ 
 "qc_1683461522_18780", 
 "qc_1677754986_6539", 
 "avram" 
 ] 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": [ 
 { 
 "scheduled_query_id": "text" 
 } 
 ] 
 } 

 application/json 

 Previous Response Action 

 Next Script Execution 

 Last updated 1 month ago 

 Was this helpful?
