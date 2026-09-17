---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-api/cortex-cloud-logging-and-collection-service-management/clcs-management
fetched_at: 2026-09-16T09:03:44Z
source: cortex-platform
---

# CLCS Management | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex Cloud 

 Cortex Cloud APIs 

 Cortex Cloud Logging and Collection Service Management 

 CLCS Management 

 The Cloud Logging and Collection Service (CLCS) Management APIs allow you to programmatically manage Next-Generation Firewalls (NGFWs) connected to your CLCS environment. 

 List connected NGFW devices 

 get https://api-yourfqdn /public_api/v1/clcs/get_connected_devices 

 Returns a list of all Next-Generation Firewalls (NGFWs) currently connected to the Cloud Logging and Collection Service (CLCS) for the authenticated tenant. 

 Each device in the response includes its serial number ( device_id ), the CSP account ID it belongs to, and the region it is deployed in. 

 Required license: This feature is included with Cortex Cloud Runtime Security or Cortex Cloud Posture Management. 

 Required permission: Data Collection > Data Sources > View 

 Header parameters 

 Authorization string Required 

 Your Cortex Cloud API key. 

 Example: {api_key} 

 x-xdr-auth-id string Required 

 Your Cortex Cloud API key ID. 

 Example: {api_key_id} 

 x-xdr-nonce string Optional 

 A unique nonce value used for request authentication. 

 Example: 0123456789abcdef 

 x-xdr-timestamp string Optional 

 The Unix timestamp in milliseconds at the time the request is sent. 

 Example: 1714118400000 

 Responses 

 200 

 A list of NGFW devices currently connected to CLCS. 

 application/json 

 The response envelope for the get connected devices operation. 

 reply object Required 

 The response payload containing the list of connected devices. 

 Example: {"devices":[{"device_id":"01234567890","csp_account_id":123456,"region":"us"}]} 

 Show properties 

 401 

 Unauthorized. The API key or key ID is missing or invalid. 

 application/json 

 403 

 Forbidden. The API key does not have the required permissions to list connected devices. Ensure the key has Data Collection > Data Sources > View permission. 

 application/json 

 500 

 Internal server error. An unexpected error occurred on the server. 

 application/json 

 get /public_api/v1/clcs/get_connected_devices 

 HTTP 

 Ask Copy 

 GET /public_api/v1/clcs/get_connected_devices HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: {api_key} 
 x-xdr-auth-id: {api_key_id} 
 Accept: */* 

 200 

 A list of NGFW devices currently connected to CLCS. 

 Ask Copy 

 { 
 "reply": { 
 "devices": [ 
 { 
 "device_id": "01234567890", 
 "csp_account_id": 123456, 
 "region": "us" 
 }, 
 { 
 "device_id": "01234567891", 
 "csp_account_id": 123456, 
 "region": "eu" 
 } 
 ] 
 } 
 } 

 Two connected devices 

 Disconnect NGFW devices from CLCS 

 post https://api-yourfqdn /public_api/v1/clcs/disconnect_devices 

 Disconnects one or more Next-Generation Firewalls (NGFWs) from the Cloud Logging and Collection Service (CLCS). This operation removes the specified devices from CLCS so they no longer forward logs to Cortex XDR. 

 The request must specify the target devices by their serial numbers ( device_ids ), along with the CSP account ID and region that the devices belong to. Up to 1000 device IDs can be submitted in a single request. 

 If a device ID in the request does not exist or is not connected, it is silently ignored. The response returns only the IDs of devices that were successfully disconnected. 

 Required license: This feature is included with Cortex Cloud Runtime Security or Cortex Cloud Posture Management. 

 Required permission: Data Collection > Data Sources > Edit 

 Validation rules: 

 device_ids : Must contain 1–1000 unique alphanumeric strings, each 1–50 characters long. 

 csp_account_id : Must be a positive integer. 

 region : Must be a non-empty string (not whitespace-only, not a number). 

 Header parameters 

 Authorization string Required 

 Your Cortex Cloud API key. 

 Example: {api_key} 

 x-xdr-auth-id string Required 

 Your Cortex Cloud API key ID. 

 Example: {api_key_id} 

 x-xdr-nonce string Optional 

 A unique nonce value used for request authentication. 

 Example: 0123456789abcdef 

 x-xdr-timestamp string Optional 

 The Unix timestamp in milliseconds at the time the request is sent. 

 Example: 1714118400000 

 Body 

 application/json 

 The request body for disconnecting NGFW devices from CLCS. 

 request_data object Required 

 The parameters specifying which devices to disconnect. 

 Example: {"device_ids":["01234567890","01234567891"],"csp_account_id":123456,"region":"us"} 

 Show properties 

 Responses 

 200 

 The operation completed. The response contains the IDs of devices that were successfully disconnected. Device IDs that were not found are silently omitted from the response. 

 application/json 

 The response envelope for the disconnect devices operation. 

 reply object Required 

 The response payload containing the IDs of successfully disconnected devices. 

 Example: {"device_ids":["01234567890","01234567891"]} 

 Show properties 

 400 

 Note: This response describes the intended validation error envelope. The backend currently raises a generic 500 Internal Server Error for these validation failures pending a fix to wrap Pydantic validation errors in the documented envelope. Treat the structure below as the contract clients should code against. 

 Bad request. The request body failed validation. Common causes include duplicate device IDs, an invalid or zero-value csp_account_id , or an empty region . 

 application/json 

 401 

 Unauthorized. The API key or key ID provided for this request is missing or invalid. 

 application/json 

 403 

 Forbidden. The API key does not have the required permissions to disconnect devices. Ensure the key has Data Collection > Data Sources > Edit permission. 

 application/json 

 500 

 Internal server error. An unexpected error occurred while processing the disconnect request. 

 application/json 

 post /public_api/v1/clcs/disconnect_devices 

 HTTP 

 Ask Copy 

 POST /public_api/v1/clcs/disconnect_devices HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: {api_key} 
 x-xdr-auth-id: {api_key_id} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 99 

 { 
 "request_data": { 
 "device_ids": [ 
 "01234567890", 
 "01234567891" 
 ], 
 "csp_account_id": 123456, 
 "region": "us" 
 } 
 } 

 Disconnect two devices 

 200 

 The operation completed. The response contains the IDs of devices that were successfully disconnected. Device IDs that were not found are silently omitted from the response. 

 Ask Copy 

 { 
 "reply": { 
 "device_ids": [ 
 "01234567890", 
 "01234567891" 
 ] 
 } 
 } 

 Two devices disconnected 

 Previous Cortex Cloud Logging and Collection Service Management overview 

 Next Models 

 Last updated 1 month ago 

 Was this helpful?
