---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-openapi-15
fetched_at: 2026-09-16T09:09:13Z
source: cortex-platform
---

# Operation Objects Uses Basic Auth misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Operation Objects Uses Basic Auth misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_OPENAPI_15 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 OTHER 

 Severity 

 HIGH 

 Framework 

 OpenAPI 

 Impact 

 This rule is checking for operation objects in OpenAPI version 2.0 files that are using basic authentication. Basic authentication is a simple authentication scheme built into the HTTP protocol, and involves sending user credentials (username and password) in the headers of a request. It's generally considered insecure for several reasons. Firstly, user credentials are sent as plaintext with basic encoding, making it easy for eavesdroppers to possibly intercept and see the credentials, especially if the request is sent over an unencrypted (i.e., non-HTTPS) connection. Secondly, basic authentication makes your application vulnerable to brute force attacks, as it doesn't incorporate any functionality for limiting login attempts. Overall, using a more secure authentication method, such as token-based or OAuth 2.0 authentication, is recommended. 

 How to Fix 

 Ensure that you aren't using the unencryptedScheme. For example: components: securitySchemes: 

 unencryptedScheme: 

 Ask Copy 

 type: http 

 Ask Copy 

 scheme: basic 

 paths: "/": get: security: 

 Ask Copy 

 - unencryptedScheme: [] 

 Previous Operation Objects Uses 'Implicit' Flow misconfiguration detected in code 

 Next The global security scope is not defined in the securityDefinitions misconfiguration detected in cod 

 Last updated 1 month ago 

 Was this helpful?
