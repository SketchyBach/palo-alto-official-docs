---
url: https://cortex-docs.paloaltonetworks.com/xpanse-api/xpanse-public-api/tag-management
fetched_at: 2026-09-16T09:04:11Z
source: cortex-platform
---

# Tag Management | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex Xpanse 

 Xpanse APIs 

 Xpanse Public API 

 Tag Management 

 APIs for managing tags 

 Add Tags to Assets 

 post https://api-{{fqdn}} /public_api/v1/assets/tags/assets_internet_exposure/assign/ 

 Add tags in bulk to a set of assets. 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · AssignOrRemoveTagsFromAsmAssetsRequestData Required 

 A dictionary containing the API request fields. An empty dictionary returns all results. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 OK 

 application/json 

 reply object · AssignTagsToAsmEntitiesReply Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/assets/tags/assets_internet_exposure/assign/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/assets/tags/assets_internet_exposure/assign/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 131 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "name", 
 "operator": "in", 
 "value": "text" 
 } 
 ], 
 "tags": [ 
 "text" 
 ] 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "assign_tags": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Add Tags to IP Address Ranges 

 post https://api-{{fqdn}} /public_api/v1/assets/tags/external_ip_address_ranges/assign/ 

 Add tags in bulk to owned IP ranges. 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · AssignOrRemoveTagsFromIpRangesRequestData Required 

 A dictionary containing the API request fields. An empty dictionary returns all results. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 OK 

 application/json 

 reply object · AssignTagsToAsmEntitiesReply Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/assets/tags/external_ip_address_ranges/assign/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/assets/tags/external_ip_address_ranges/assign/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 221 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "organization_handles", 
 "operator": "in", 
 "value": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "tags": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "assign_tags": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Create Asset Tag Rules 

 post https://api-{{fqdn}} /public_api/v1/assets/create_asset_tag_rules/ 

 Create tag rules that apply tags automatically to assets that match your rule criteria, including any new assets that are attributed to your organization. Tag rules can be defined for IPv4 addresses and IPv4 ranges. These fields can be the same to denote a single IP address. If the list of IP addresses exceeds 100, Expander will create multiple tag rules, each with at most 100 IP addresses per rule.
Required License: Cortex Xpanse Expander 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · CreateTagRulesForIpRangesRequestData Required 

 A dictionary containing the API request fields. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 OK 

 application/json 

 reply string Required 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/assets/create_asset_tag_rules/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/assets/create_asset_tag_rules/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 235 

 { 
 "request_data": { 
 "ip_ranges": [ 
 { 
 "from_ip": "text", 
 "to_ip": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "rule_name": "text", 
 "description": "text", 
 "tag_name": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Remove Tags from Assets 

 post https://api-{{fqdn}} /public_api/v1/assets/tags/assets_internet_exposure/remove/ 

 Remove tags in bulk from a set of assets. 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · AssignOrRemoveTagsFromAsmAssetsRequestData Required 

 A dictionary containing the API request fields. An empty dictionary returns all results. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 OK 

 application/json 

 reply object · RemoveTagsFromAsmEntitiesReply Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/assets/tags/assets_internet_exposure/remove/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/assets/tags/assets_internet_exposure/remove/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 131 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "name", 
 "operator": "in", 
 "value": "text" 
 } 
 ], 
 "tags": [ 
 "text" 
 ] 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "remove_tags": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Remove Tags from IP Address Ranges 

 post https://api-{{fqdn}} /public_api/v1/assets/tags/external_ip_address_ranges/remove/ 

 Remove tags in bulk from a set of IP address ranges. 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · AssignOrRemoveTagsFromIpRangesRequestData Required 

 A dictionary containing the API request fields. An empty dictionary returns all results. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 OK 

 application/json 

 reply object · RemoveTagsFromAsmEntitiesReply Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/assets/tags/external_ip_address_ranges/remove/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/assets/tags/external_ip_address_ranges/remove/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 221 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "organization_handles", 
 "operator": "in", 
 "value": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "tags": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "remove_tags": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Delete Unused Tags 

 post https://api-{{fqdn}} /public_api/v1/assets/delete_unused_tag/ 

 Delete unused tags by specifying tag IDs or tag names. You don't have to provide both tag_ids and tag_names, but you can use both to specify different tags. 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api-key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api-key-id}} 

 Body 

 application/json 

 request_data object Required 

 A dictionary containing the API request fields. 

 An empty dictionary returns all results. 

 Show properties 

 Responses 

 200 

 OK 

 application/json 

 reply string Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/assets/delete_unused_tag/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/assets/delete_unused_tag/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api-key}} 
 x-xdr-auth-id: {{api-key-id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 93 

 { 
 "request_data": { 
 "tag_family": "ip_ranges", 
 "tag_ids": [ 
 "IPR:abcd12345" 
 ], 
 "tag_names": [ 
 "tag-1" 
 ] 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": "succeeded" 
 } 

 Previous System Management 

 Next Vulnerability Testing 

 Last updated 1 month ago 

 Was this helpful?
