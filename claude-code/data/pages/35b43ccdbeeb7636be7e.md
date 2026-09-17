---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-to-cloud/code-to-cloud/api-endpoints-for-c2c
fetched_at: 2026-09-16T08:49:03Z
source: cortex-platform
---

# API endpoints for C2C | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 code-to-cloud 

 Code-to-Cloud 

 API endpoints for C2C 

 Retrieve Code-to-Cloud coverage programmatically. 

 Retrieve Code-to-Cloud coverage in automation and reporting workflows. 

 Coverage 

 Operation 

 Method 

 Endpoint 

 Get the Code-to-Cloud coverage ratio 

 GET 

 /public_api/appsec/v1/code-to-cloud/coverage 

 The response returns a ratio from 0 to 1 . Multiply it by 100 for a percentage. 

 Required query parameters 

 direction : code_to_cloud or cloud_to_code . 

 type : artifact or infrastructure . 

 Optional query parameters 

 only_onboarded : Limits artifact Code-to-Cloud results to onboarded repositories. 

 application : Limits results to an application name. 

 provider : Limits results to a provider name. 

 only_onboarded applies only to code_to_cloud with artifact . 

 Use Authorization and x-xdr-auth-id headers for authentication. 

 Required license: Cortex Cloud Posture Management or Cortex Cloud Runtime Security with Application Security add-on. 

 For request schemas and response details, see Cloud Coverage . 

 Previous Enforce policies with C2C 

 Next Troubleshooting 

 Last updated 1 month ago 

 Was this helpful?
