---
url: https://cortex-docs.paloaltonetworks.com/xsiam-api/compliance-controls/categories
fetched_at: 2026-09-16T09:04:03Z
source: cortex-platform
---

# Categories | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSIAM 

 XSIAM APIs 

 Compliance Controls 

 Categories 

 Operations for retrieving categories and subcategories 

 Get categories and subcategories (v1) 

 post https://api.xdr.us.paloaltonetworks.com /public_api/v1/compliance/get_control_categories_and_subcategories 

 Retrieve available compliance control categories and subcategories. 

 Required license: Cortex Cloud Runtime Security or Cortex Cloud Posture Management 

 Authorizations 

 XDRAuth & XDRAuthToken 

 x-xdr-auth-id string Required 

 API Key ID for authentication 

 Authorization string Required 

 API Key for authentication 

 Body 

 application/json 

 request_data object Optional 

 Responses 

 200 

 Successfully retrieved categories and subcategories 

 application/json 

 reply object Optional 

 Show properties 

 500 

 Internal server error 

 application/json 

 post /public_api/v1/compliance/get_control_categories_and_subcategories 

 HTTP 

 Ask Copy 

 POST /public_api/v1/compliance/get_control_categories_and_subcategories HTTP/1.1 
 Host: api.xdr.us.paloaltonetworks.com 
 x-xdr-auth-id: YOUR_API_KEY 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 19 

 { 
 "request_data": {} 
 } 

 200 

 Successfully retrieved categories and subcategories 

 Ask Copy 

 { 
 "reply": { 
 "data": { 
 "categories": [ 
 "text" 
 ], 
 "subcategories": [ 
 "text" 
 ] 
 } 
 } 
 } 

 Previous Assessment Results 

 Next Compliance Assets 

 Last updated 5 days ago 

 Was this helpful?
