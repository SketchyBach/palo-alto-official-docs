---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-openapi-9
fetched_at: 2026-09-06T11:12:23Z
source: cortex-platform
---

# Security scopes of operations are not defined in securityDefinition misconfiguration detected in cod | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Security scopes of operations are not defined in securityDefinition misconfiguration detected in cod 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_OPENAPI_9 

 Category - Subcategory 

 Public Exposure - APIs 

 Provider 

 OTHER 

 Severity 

 MEDIUM 

 Framework 

 OpenAPI 

 Impact 

 This rule looks into the security definitions in OpenAPI 2.0 files to ensure that security scopes for operations are properly defined. If they are not properly defined, it could lead to insecure API endpoints, potentially leaving the application vulnerable to unauthorized access or breaches. This could result in unauthorized data access, manipulation, or even system takeover, hence it's crucial to ensure each operation has been mapped with the correct security scope. 

 How to Fix 

 OpenAPI 

 To fix this issue in your OpenAPI (Swagger) file, define security scopes that allow you to set the level of access for each API operation. Specifically, include each security scope within the securityDefinition block. 

 Ask Copy 

 securityDefinitions : 
 my_oauth : 
 type : oauth2 
 scopes : 
 ' read:stuff ' : Read access to the stuff 
 ' write:stuff ' : Write access to the stuff 
 flow : implicit 
 authorizationUrl : https://oauth.example.com/authorize 

 In the above code, my_oauth defines an OAuth security scheme where 'read:stuff' and 'write:stuff' are the specific scopes. The 'read:stuff' and 'write:stuff' scopes indicate the actions that can be performed when a user is granted these permissions. This structure ensures that API consumers understand what specific authorizations are required to access each operation. This is a strong practice in securing your API as it provides granularity in access control for each operation in your API specification. 

 Previous API spec includes a 'password' flow in OAuth2 authentication misconfiguration detected in code 

 Next OAuth2 security definitions includes password flow in OpenAPI 2.0 file misconfiguration detected in 

 Last updated 1 month ago 

 Was this helpful?
