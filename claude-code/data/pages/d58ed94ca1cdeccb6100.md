---
url: https://cortex-docs.paloaltonetworks.com/xsoar-8-api/cortex-xsoar-8.x-apis/multi-tenant
fetched_at: 2026-09-16T09:04:07Z
source: cortex-platform
---

# Multi Tenant | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSOAR 

 XSOAR 8.x APIs 

 Cortex XSOAR 8.x APIs 

 Multi Tenant 

 APIs for multi-tenant deployments 

 Upload custom content file 

 post https://api-yourfqdn /xsoar/public/v1/content/bundle 

 Import custom content created from a Cortex XSOAR tenant. The custom content file can be obtained from the tenant in the UI at Setting > System > Custom Content > Export all custom content . 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Body 

 application/json 

 file string · binary Optional 

 Custom content file. 

 Responses 

 200 

 OK 

 application/json 

 object Optional 

 post /xsoar/public/v1/content/bundle 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/content/bundle HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 17 

 { 
 "file": "binary" 
 } 

 200 

 OK 

 Ask Copy 

 {} 

 Previous Lists 

 Next Playbooks 

 Last updated 1 month ago 

 Was this helpful?
