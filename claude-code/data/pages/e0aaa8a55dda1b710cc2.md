---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-openapi-14
fetched_at: 2026-09-06T11:12:24Z
source: cortex-platform
---

# Operation Objects Uses 'Implicit' Flow misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Operation Objects Uses 'Implicit' Flow misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_OPENAPI_14 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 OTHER 

 Severity 

 MEDIUM 

 Framework 

 OpenAPI 

 Impact 

 This rule is checking for the usage of 'implicit' flow in operation objects within OpenAPI 2.0 files. The 'implicit' flow is an authorization method used in OpenAPI operations which has since been deprecated due to inherent security vulnerabilities. It relies on redirection-based flows that make an application more susceptible to access and refresh token interception. When these tokens are stolen, a malicious actor can impersonate a user and conduct activities without consent. Therefore, using a more secure method like 'authorization code' flow is recommended, which adds an additional layer of security and prevents direct exposure of tokens. The rule thus helps in maintaining good API security practices in the OpenAPI specifications. 

 How to Fix 

 To fix this issue, you will have to specify a maximum number of items for each array in your API's schema definition. 

 The above code is secure because it ensures that there is a limit on the number of items that can be returned in a response from the "/temperatures" endpoint. Without this limit, larger-than-expected responses could lead to performance issues or even application crashes. openapi: "3.0.0" info: version: "1.0.0" title: "An API for temperature measurements" paths: /temperatures: get: responses: "200": content: application/json: schema: type: "array" maxItems: 10 items: $ref: "#/components/schemas/Temperature" components: schemas: Temperature: type: "object" properties: id: type: "string" value: type: "number" 

 Previous Security definitions uses basic auth misconfiguration detected in code 

 Next Operation Objects Uses Basic Auth misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
