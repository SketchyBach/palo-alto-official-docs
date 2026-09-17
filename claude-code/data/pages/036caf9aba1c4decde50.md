---
url: https://cortex-docs.paloaltonetworks.com/xdr-3-api/cortex-xdr-3.x-apis/lookup-datasets
fetched_at: 2026-09-16T09:03:56Z
source: cortex-platform
---

# Lookup Datasets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XDR 

 XDR 3.x APIs 

 Cortex XDR 3.x APIs 

 Lookup Datasets 

 APIs for lookup datasets 

 Add or update data in a lookup dataset 

 post https://api-yourfqdn /public_api/v1/xql/lookups/add_data 

 Add or update data in a lookup dataset. 

 When updating data, any field not specified in the data field, but specified on at least one of the rows, will be set to None . 

 The Add or update data in a lookup dataset endpoint does not support concurrent edits. Sending concurrent calls to this endpoint can cause data to be unintentionally overwritten or deleted. To allow sufficient time for each API call to complete its operation before initiating another one, assume that 1000 entries can be added per API every 10 seconds. 

 **Note: ** 

 The maximum size of a lookup dataset is 50 MB. Attemping to exceed this limit will fail. 

 Requests time out after three minutes. 

 Required license: Cortex XDR Pro per Endpoint or Cortex XDR Pro per GB 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Accept-Encoding string Optional 

 For retrieving a compressed gzipped response 

 Default: gzip 

 Body 

 application/json 

 request object Required 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 added integer Optional 

 updated integer Optional 

 skipped integer Optional 

 400 

 ad Request. Got an invalid JSON. 

 application/json 

 401 

 Unauthorized access. An issue occurred during authentication. This can indicate an incorrect key, ID, or other invalid authentication parameters. 

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

 post /public_api/v1/xql/lookups/add_data 

 HTTP 

 Ask Copy 

 POST /public_api/v1/xql/lookups/add_data HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 310 

 { 
 "request": { 
 "dataset_name": "users", 
 "key_fields": [ 
 "uid", 
 "username" 
 ], 
 "data": [ 
 { 
 "uid": "123abc", 
 "username": "john", 
 "zipcode": 58672, 
 "salary": 5.1, 
 "is_admin": false, 
 "birthday": "31-05-1982T10:22:45Z" 
 }, 
 { 
 "uid": "124abc", 
 "username": "jane", 
 "zipcode": 58642, 
 "salary": 5000000, 
 "is_admin": true, 
 "birthday": "31-03-1982T10:22:45Z" 
 } 
 ] 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "added": 1, 
 "updated": 1, 
 "skipped": 1 
 } 

 Remove data from a lookup dataset 

 post https://api-yourfqdn /public_api/v1/xql/lookups/remove_data 

 Remove data from a dataset based on the specified parameters. If any one of the filter sets are not found, the API does not delete any data. 

 The Remove data from a lookup dataset endpoint does not support concurrent edits. Sending concurrent calls to this endpoint can cause data to be unintentionally overwritten or deleted. To allow sufficient time for each API call to complete its operation before initiating another one, assume that 1000 entries can be added per API every 10 seconds. 

 Note: 

 All lookup entries matching any of the filter blocks are deleted. To match a filter block, a lookup entry must match all the specified fields as if there were an AND operator between them. 

 Requests time out after three minutes. 

 Required license: Cortex XDR Pro per Endpoint or Cortex XDR Pro per GB 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Accept-Encoding string Optional 

 For retrieving a compressed gzipped response 

 Default: gzip 

 Body 

 application/json 

 request object Required 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 deleted integer Optional 

 Number of entries deleted successfully. 

 400 

 ad Request. Got an invalid JSON. 

 application/json 

 401 

 Unauthorized access. An issue occurred during authentication. This can indicate an incorrect key, ID, or other invalid authentication parameters. 

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

 post /public_api/v1/xql/lookups/remove_data 

 HTTP 

 Ask Copy 

 POST /public_api/v1/xql/lookups/remove_data HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 110 

 { 
 "request": { 
 "dataset_name": "users", 
 "filters": [ 
 { 
 "uid": "123", 
 "username": "john" 
 }, 
 { 
 "uid": "124", 
 "zipcode": 58672 
 } 
 ] 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "deleted": 1 
 } 

 Get data from a lookup dataset 

 post https://api-yourfqdn /public_api/v1/xql/lookups/get_data 

 Get data from a lookup dataset according to the specified filter fields. All lookup entries matching any of the filter blocks are returned. To match a filter block, a lookup entry must match all the specified fields as if there were an AND operator between them. If no filters are specified, return all lookup entries. 

 Note: 

 The maximum number of entries returned is 10,000. -Requests time out after three minutes. 

 Required license: Cortex XDR Pro per Endpoint or Cortex XDR Pro per GB 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Accept-Encoding string Optional 

 For retrieving a compressed gzipped response 

 Default: gzip 

 Body 

 application/json 

 request object Required 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 data object Optional 

 Show properties 

 filter_count integer Optional 

 Number of entries that match the filter. 

 total_count integer Optional 

 Total number of entries. 

 400 

 ad Request. Got an invalid JSON. 

 application/json 

 401 

 Unauthorized access. An issue occurred during authentication. This can indicate an incorrect key, ID, or other invalid authentication parameters. 

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

 post /public_api/v1/xql/lookups/get_data 

 HTTP 

 Ask Copy 

 POST /public_api/v1/xql/lookups/get_data HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 130 

 { 
 "request": { 
 "dataset_name": "users", 
 "filters": [ 
 { 
 "uid": "123", 
 "username": "john" 
 }, 
 { 
 "department": "dev", 
 "zipcode": "58674" 
 } 
 ], 
 "limit": 20 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "data": [ 
 { 
 "uid": "uid5", 
 "salary": 5.1, 
 "zipcode": 70005, 
 "birthday": 386418165000, 
 "is_admin": true, 
 "username": "username5", 
 "_insert_time": 1718807765000, 
 "_update_time": 1718807765000, 
 "_collector_name": "Console", 
 "_collector_type": "Console" 
 }, 
 { 
 "uid": "uid6", 
 "salary": 6.1, 
 "zipcode": 70006, 
 "birthday": 386418165000, 
 "is_admin": true, 
 "username": "username6", 
 "_insert_time": 1718807765000, 
 "_update_time": 1718807765000, 
 "_collector_name": "Console", 
 "_collector_type": "Console" 
 } 
 ], 
 "filter count": 2, 
 "total count": 10 
 } 
 } 

 Previous Incident Management 

 Next Response Action 

 Last updated 1 month ago 

 Was this helpful?
