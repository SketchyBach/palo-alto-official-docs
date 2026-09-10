---
url: https://cortex-docs.paloaltonetworks.com/xsiam-api/aspm-cicd-and-application-security/rules
fetched_at: 2026-09-06T10:55:59Z
source: cortex-platform
---

# Rules | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSIAM 

 XSIAM APIs 

 ASPM, CICD and Application Security 

 Rules 

 APIs for managing rules 

 Get AppSec rules 

 get https://api-yourfqdn /public_api/appsec/v1/rules 

 Get a paginated list of Application Security (AppSec) rules. Supports filtering by enabled state, custom flag, categories, sub-categories, cloud providers, scanners, severities, frameworks, and labels. 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. Not supported in XSIAM Enterprise Plus. 

 Query parameters 

 enabled boolean Optional 

 Filter rules by their enabled state. Set to true to return only active rules, or false to return only disabled rules. If omitted, rules of both states are returned. 

 isCustom boolean Optional 

 Filter rules by type. Set to true to return only custom rules, or false to return only out-of-the-box rules. If omitted, both rule types are returned. 

 categories string · enum[] Optional 

 Custom AppSec rule category. 

 Show properties 

 subCategories string[] Optional 

 Filter rules by subcategory. Subcategories further classify the type of security issue within a category and are applicable to IAC rules only. The supported subcategory values depend on the selected categories filter. CICD , SCA , and SECRETS rules do not have subcategories and are retured with a null value. 

 cloudProviders string · enum[] Optional 

 Cloud provider associated with the rule. 

 Show properties 

 scanners string · enum[] Optional 

 Filter rules by the type of security scanner used to detect findings. 

 Show properties 

 severities string · enum[] Optional 

 The priority level assigned to findings identified by the rule 

 Show properties 

 frameworks string · enum[] Optional 

 Filter rules by the IaC framework or language they apply to. Returns only rules that have a definition for at least one of the specified frameworks. 

 Example: TERRAFORM 

 Show properties 

 labels string[] Optional 

 Filter rules by one or more labels. Returns only rules that have all specified labels assigned. 

 offset number · double Optional 

 The number of rules to skip before returning results. Used for pagination together with limit . Set to 0 to start from the first result. 

 Default: 0 

 limit number · double Optional 

 The maximum number of rules to return per page. Used for pagination together with offset . 

 Default: 100 

 sortBy string · enum Optional 

 The field by which to sort the returned rules. 

 Default: name Possible values : created_at name labels 

 sortOrder integer · enum Optional 

 The sort direction for the results. Use 1 for ascending order and -1 for descending order. 

 Possible values : -1 1 

 Header parameters 

 Authorization string Required 

 {api_key} 

 Example: your-api-key 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Example: 1 

 get-scanner-rule-id boolean Optional 

 Unique identifier for a scanner rule. When set to true , the scannerRuleId field is included in each rule object returned in the response. If omitted or set to false , the scannerRuleId field is excluded from the response. 

 Responses 

 200 

 Ok 

 application/json 

 offset number Optional 

 The starting position of the current page of results. 

 nextOffset number · nullable Optional 

 The offset to use in the next request to retrieve the next page of results. Returns null if there are no more results. 

 Example: 100 

 rules object · DetectionRule[] Optional 

 Details of the Application Security rule 

 Show properties 

 get /public_api/appsec/v1/rules 

 HTTP 

 Ask Copy 

 GET /public_api/appsec/v1/rules HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: your-api-key 
 x-xdr-auth-id: 1 
 Accept: */* 

 200 

 Ok 

 Ask Copy 

 { 
 "offset": 1, 
 "nextOffset": 100, 
 "rules": [ 
 { 
 "category": "text", 
 "cloudProvider": "GCP", 
 "createdAt": "2026-01-01T00:00:00.000Z", 
 "description": "text", 
 "shortDescription": "text", 
 "detectionMethod": "IaC Security", 
 "docLink": "text", 
 "domain": "POSTURE", 
 "findingCategory": "Code", 
 "findingDocs": "Custom IaC rule for Public Exposure Storage Buckets", 
 "findingTypeId": 30040031, 
 "findingTypeName": "text", 
 "frameworks": [ 
 { 
 "frameworkDetails": { 
 "definition": "text", 
 "definition_link": "text", 
 "name": "TERRAFORM", 
 "remediation_description": "text", 
 "remediation_ids": [ 
 "text" 
 ], 
 "resource_types": [ 
 "text" 
 ] 
 } 
 } 
 ], 
 "id": "text", 
 "isCustom": true, 
 "isEnabled": true, 
 "labels": [ 
 "text" 
 ], 
 "updatedAt": "2026-01-01T00:00:00.000Z", 
 "mitreTactics": [ 
 "text" 
 ], 
 "mitreTechniques": [ 
 "text" 
 ], 
 "name": "text", 
 "owner": "CAS", 
 "scanner": "CICD", 
 "severity": "CRITICAL", 
 "subCategory": "STORAGE_BUCKETS", 
 "complianceStandards": { 
 "standardName": "CIS Amazon Elastic Kubernetes Service (EKS) Benchmark v1.4_copy v1.4", 
 "controls": [ 
 { 
 "controlName": "The default namespace should not be used", 
 "controlDefinition": "Kubernetes provides a default namespace, where objects are placed if no namespace is specified for them. Placing objects in this namespace makes application of RBAC and other controls more difficult." 
 } 
 ] 
 }, 
 "cspmRuleId": "text", 
 "cspmTypeId": 60100018 
 } 
 ] 
 } 

 Create an AppSec rule 

 post https://api-yourfqdn /public_api/appsec/v1/rules 

 Create a new Application Security Rule. Application Security rules are designed to detect security threats within your application security environment. Application Security rules identify and flag issues based on predefined criteria. 

 Limitation : This API supports creating custom rules only for IaC Security and Secrets Security . CI/CD Security custom rules are not supported. 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. Not supported in XSIAM Enterprise Plus. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 Example: your-api-key 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Example: 1 

 Body 

 application/json 

 Define the Application Security custom rule. The category option should match your selection for scanner . 

 name string Required 

 A unique name for the Appsec rule. 

 Example: S3 Bucket Public Access Check 

 description string Optional 

 Description of the rule 

 Example: Detects S3 buckets with public access enabled 

 severity string · enum Required 

 Severity level of the rule 

 Possible values : CRITICAL HIGH LOW MEDIUM 

 labels string[] Optional 

 Labels to be assigned to the rule 

 Example: S3-Security 

 scanner string · enum Required 

 The type of security scanner used to detect findings of this rule. Choose any one of the scanners. 

 Possible values : IAC SECRETS 

 frameworks object · FrameworkRequestParams Required 

 Show properties 

 category any of Required 

 string · enum Optional 

 Custom rule IaC category. Applicable only when scanner is set to IAC . 

 Example: PUBLIC Possible values : AI_ML COMPUTE IAM KUBERNETES LOGGING MONITORING NETWORKING PUBLIC STORAGE 

 or 

 string · enum Optional 

 Custom rule secret category. Applicable only when scanner is set to SECRETS . 

 Possible values : API_KEYS DATABASE_CREDENTIALS ENCRYPTION_KEYS CLOUD_SERVICE_PROVIDER_KEYS SSH_KEYS ENVIRONMENT_VARIABLES SENSITIVE_TOKENS THIRD_PARTY_SERVICES 

 subCategory string · enum Required 

 Custom rule subcategory. The supported values depend on the selected category. Refer to the following table for the valid subcategories for each category. 

 Note: This field is applicable only when scanner is set to IAC . 

 Category and Subcategory Table for IaC Scanner 

 Category Subcategory 

 AI and Machine Learning ( AI_ML ) Guardrails ( GUARDRAILS ) 

 AI and Machine Learning ( AI_ML ) Risky models ( RISKY_MODELS ) 

 AI and Machine Learning ( AI_ML ) Public Exposure ( PUBLIC_EXPOSURE ) 

 AI and Machine Learning ( AI_ML ) Permissions ( PERMISSIONS ) 

 Logging ( LOGGING ) Encryption ( ENCRYPTION ) 

 Logging ( LOGGING ) Permissions ( PERMISSIONS ) 

 Logging ( LOGGING ) Retention ( RETENTION ) 

 Logging ( LOGGING ) Formats ( FORMATS ) 

 Logging ( LOGGING ) Disabled or missing ( DISABLED_OR_MISSING ) 

 Logging ( LOGGING ) Public Exposure ( PUBLIC_EXPOSURE ) 

 Logging ( LOGGING ) Under Use ( UNDER_USE ) 

 Kubernetes ( KUBERNETES ) Network Policies ( NETWORK_POLICIES ) 

 Kubernetes ( KUBERNETES ) Access Control ( ACCESS_CONTROL ) 

 Kubernetes ( KUBERNETES ) Logging and Monitoring ( LOGGING_AND_MONITORING ) 

 Kubernetes ( KUBERNETES ) Resource Management ( RESOURCE_MANAGEMENT ) 

 Kubernetes ( KUBERNETES ) Native Security Controls ( NATIVE_SECURITY_CONTROLS ) 

 Kubernetes ( KUBERNETES ) Management Services Exposure ( MANAGEMENT_SERVICES_EXPOSURE ) 

 Compute ( COMPUTE ) Overprovisioned ( OVERPROVISIONED ) 

 Compute ( COMPUTE ) Startup Script Leaks ( STARTUP_SCRIPT_LEAKS ) 

 Compute ( COMPUTE ) Default Credentials or Auth ( DEFAULT_CREDENTIALS_OR_AUTH ) 

 Compute ( COMPUTE ) Unsanctioned Resource or Type ( UNSANCTIONED_RESOURCE_OR_TYPE ) 

 Storage ( STORAGE ) Encryption ( ENCRYPTION ) 

 Storage ( STORAGE ) Permissions ( PERMISSIONS ) 

 Storage ( STORAGE ) Backups ( BACKUPS ) 

 Storage ( STORAGE ) Versioning ( VERSIONING ) 

 Storage ( STORAGE ) Replication ( REPLICATION ) 

 Storage ( STORAGE ) Alerting ( ALERTING ) 

 Storage ( STORAGE ) Redundancy ( REDUNDANCY ) 

 Public ( PUBLIC ) Admin Interfaces ( ADMIN_INTERFACES ) 

 Public ( PUBLIC ) Database Endpoints ( DATABASE_ENDPOINTS ) 

 Public ( PUBLIC ) Storage Buckets ( STORAGE_BUCKETS ) 

 Public ( PUBLIC ) APIs ( APIS ) 

 Public ( PUBLIC ) Sensitive Ports ( SENSITIVE_PORTS ) 

 Networking ( NETWORKING ) Load Balancing ( LOAD_BALANCING ) 

 Networking ( NETWORKING ) Ingress Controls ( INGRESS_CONTROLS ) 

 Networking ( NETWORKING ) Egress Controls ( EGRESS_CONTROLS ) 

 Networking ( NETWORKING ) Encryption and Protocols ( ENCRYPTION_AND_PROTOCOLS ) 

 Networking ( NETWORKING ) VPC/VCN/VNET ( VPC_VCN_VNET ) 

 Networking ( NETWORKING ) Flow Logs ( FLOW_LOGS ) 

 Monitoring ( MONITORING ) Tags and metadata ( TAGS_AND_METADATA ) 

 Monitoring ( MONITORING ) Resource Health ( RESOURCE_HEALTH ) 

 Monitoring ( MONITORING ) Performance Monitoring ( PERFORMANCE_MONITORING ) 

 Monitoring ( MONITORING ) Alerting and Notifications ( ALERTING_AND_NOTIFICATIONS ) 

 Monitoring ( MONITORING ) Unintegrated ( UNINTEGRATED ) 

 Monitoring ( MONITORING ) Storage ( STORAGE ) 

 IAM ( IAM ) Overly Permissive ( OVERLY_PERMISSIVE ) 

 IAM ( IAM ) Unused ( UNUSED ) 

 IAM ( IAM ) Credential Exposure ( CREDENTIAL_EXPOSURE ) 

 IAM ( IAM ) MFA ( MFA ) 

 IAM ( IAM ) Role Separation ( ROLE_SEPARATION ) 

 IAM ( IAM ) Shared ( SHARED ) 

 IAM ( IAM ) Expired Key Controls ( EXPIRED_KEY_CONTROLS ) 

 IAM ( IAM ) Authentication Policies ( AUTHENTICATION_POLICIES ) 

 Example: STORAGE_BUCKETS Possible values : GUARDRAILS RISKY_MODELS PUBLIC_EXPOSURE PERMISSIONS ENCRYPTION RETENTION FORMATS DISABLED_OR_MISSING UNDER_USE NETWORK_POLICIES ACCESS_CONTROL LOGGING_AND_MONITORING RESOURCE_MANAGEMENT NATIVE_SECURITY_CONTROLS MANAGEMENT_SERVICES_EXPOSURE OVERPROVISIONED STARTUP_SCRIPT_LEAKS DEFAULT_CREDENTIALS_OR_AUTH UNSANCTIONED_RESOURCE_OR_TYPE BACKUPS VERSIONING REPLICATION ALERTING REDUNDANCY ADMIN_INTERFACES DATABASE_ENDPOINTS STORAGE_BUCKETS APIS SENSITIVE_PORTS LOAD_BALANCING INGRESS_CONTROLS EGRESS_CONTROLS ENCRYPTION_AND_PROTOCOLS VPC_VCN_VNET FLOW_LOGS TAGS_AND_METADATA RESOURCE_HEALTH PERFORMANCE_MONITORING ALERTING_AND_NOTIFICATIONS UNINTEGRATED STORAGE OVERLY_PERMISSIVE UNUSED CREDENTIAL_EXPOSURE MFA ROLE_SEPARATION SHARED EXPIRED_KEY_CONTROLS AUTHENTICATION_POLICIES 

 cspmRuleId string · nullable Optional 

 The unique identifier of the Cloud Security rule to which the custom Application Security rule will be mapped. Applicable only when scanner is set to IAC . 

 Example: ff6a26a5-f036-4d3a-a650-d5de1d568bab 

 clonedFromRuleId string · nullable Optional 

 Optional. ID of the source rule from which this rule was cloned. This field is present only for cloned rules. 

 Responses 

 201 

 Created. A new resource was created successfully. 

 application/json 

 Details of the Application Security rule 

 category string Optional 

 Custom Appsec rule category. 

 cloudProvider string · enum Optional 

 The cloud provider associated with the rule. If the rule is not cloud-provider-specific, this field is null. 

 Example: GCP Possible values : ALIBABA_CLOUD AWS Azure GCP IBM ORACLE OTHER 

 createdAt string · date-time Optional 

 The timestamp when the AppSec rule was created. 

 description string Optional 

 The rule description. 

 shortDescription string · nullable Optional 

 A brief summary of the rule. If not provided, this field is null. 

 detectionMethod string Optional 

 Security scanner used to detect findings for this rule. 

 Example: IaC Security 

 docLink string Optional 

 A URL linking to the relevant Cortex Cloud documentation page. 

 domain string Optional 

 The domain associated with the rule. 

 Example: POSTURE 

 findingCategory string · enum Optional 

 Category of findings this rule generates. 

 Possible values : Code Configuration Data Vulnerability 

 findingDocs string Optional Example: Custom IaC rule for Public Exposure Storage Buckets 

 findingTypeId number · double Optional 

 The numeric identifier of the finding type associated with this rule. 

 Example: 30040031 

 findingTypeName string Optional 

 Display name of the finding type associated with this rule. Matches the rule name for custom rules. 

 frameworks object · Frameworks[] Optional 

 Framework objects containing the rule definition and remediation details for each supported IaC framework or secrets detection framework. 

 Show properties 

 id string Optional 

 Unique identifier of the AppSec rule. 

 isCustom boolean Optional 

 Indicates whether the rule is a custom rule created by the user (true) or an out-of-the-box rule (false). 

 isEnabled boolean Optional 

 Indicates whether the rule is currently active and will generate findings during scans. 

 labels string[] Optional 

 Labels assigned to the rule. 

 updatedAt string · date-time Optional 

 The timestamp when the AppSec rule was last modified. 

 mitreTactics string[] · nullable Optional 

 The MITRE ATT&CK tactic identifiers associated with this rule. Returns an empty array if no tactics are mapped. 

 mitreTechniques string[] · nullable Optional 

 The MITRE ATT&CK technique identifiers associated with this rule. Returns an empty array if no techniques are mapped. 

 name string Optional 

 Name of the Appsec rule. 

 owner string Optional 

 The internal service owner of the rule. 

 Example: CAS 

 scanner string · enum Optional 

 The scanner type used by this rule to detect security issues. 

 Possible values : CICD IAC SCA SECRETS 

 severity string · enum Optional 

 Severity level of the rule 

 Possible values : CRITICAL HIGH LOW MEDIUM 

 subCategory string Optional 

 Custom rule subcategory. 

 Example: STORAGE_BUCKETS 

 complianceStandards object · ComplianceStandard Optional 

 An array of compliance standards associated with this rule. 

 Show properties 

 cspmRuleId string · nullable Optional 

 The ID of the mapped Cloud Security rule. When set, findings from this AppSec rule are correlated with the corresponding Cloud Security rule. Returns null if no rule is mapped. 

 cspmTypeId number · nullable Optional 

 The numeric type identifier of the mapped Cloud Security rule. Returned only when the AppSec rule is linked to a rule via cspmRuleId . 

 Example: 60100018 

 400 

 Bad Request 

 application/json 

 post /public_api/appsec/v1/rules 

 HTTP 

 Ask Copy 

 POST /public_api/appsec/v1/rules HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: your-api-key 
 x-xdr-auth-id: 1 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 597 

 { 
 "name": "S3 Bucket Public Access Check", 
 "description": "Detects S3 buckets with public access enabled", 
 "severity": "HIGH", 
 "scanner": "IAC", 
 "category": "PUBLIC", 
 "subCategory": "STORAGE_BUCKETS", 
 "cspmRuleId": "fddd75de-c838-472c-9b24-5c9127ba5405", 
 "labels": [ 
 "Custom-Rule", 
 "S3-Security" 
 ], 
 "frameworks": [ 
 { 
 "name": "TERRAFORM", 
 "definition": "definition:\n cond_type: attribute\n resource_types:\n - aws_s3_bucket_public_access_block\n attribute: block_public_acls\n operator: equals\n value: false", 
 "remediationDescription": "Set block_public_acls to true in aws_s3_bucket_public_access_block resource" 
 } 
 ] 
 } 

 IaC Security Rule 

 201 

 Created. A new resource was created successfully. 

 Get an AppSec rule 

 get https://api-yourfqdn /public_api/appsec/v1/rules/ {ruleId} 

 Get the details of the specified Application Security rule. 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. Not supported in XSIAM Enterprise Plus. 

 Path parameters 

 ruleId string Required 

 Unique identifier of the Application Security rule 

 Header parameters 

 Authorization string Required 

 {api_key} 

 Example: your-api-key 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Example: 1 

 Responses 

 200 

 Ok 

 application/json 

 Details of the Application Security rule 

 category string Optional 

 Custom Appsec rule category. 

 cloudProvider string · enum Optional 

 The cloud provider associated with the rule. If the rule is not cloud-provider-specific, this field is null. 

 Example: GCP Possible values : ALIBABA_CLOUD AWS Azure GCP IBM ORACLE OTHER 

 createdAt string · date-time Optional 

 The timestamp when the AppSec rule was created. 

 description string Optional 

 The rule description. 

 shortDescription string · nullable Optional 

 A brief summary of the rule. If not provided, this field is null. 

 detectionMethod string Optional 

 Security scanner used to detect findings for this rule. 

 Example: IaC Security 

 docLink string Optional 

 A URL linking to the relevant Cortex Cloud documentation page. 

 domain string Optional 

 The domain associated with the rule. 

 Example: POSTURE 

 findingCategory string · enum Optional 

 Category of findings this rule generates. 

 Possible values : Code Configuration Data Vulnerability 

 findingDocs string Optional Example: Custom IaC rule for Public Exposure Storage Buckets 

 findingTypeId number · double Optional 

 The numeric identifier of the finding type associated with this rule. 

 Example: 30040031 

 findingTypeName string Optional 

 Display name of the finding type associated with this rule. Matches the rule name for custom rules. 

 frameworks object · Frameworks[] Optional 

 Framework objects containing the rule definition and remediation details for each supported IaC framework or secrets detection framework. 

 Show properties 

 id string Optional 

 Unique identifier of the AppSec rule. 

 isCustom boolean Optional 

 Indicates whether the rule is a custom rule created by the user (true) or an out-of-the-box rule (false). 

 isEnabled boolean Optional 

 Indicates whether the rule is currently active and will generate findings during scans. 

 labels string[] Optional 

 Labels assigned to the rule. 

 updatedAt string · date-time Optional 

 The timestamp when the AppSec rule was last modified. 

 mitreTactics string[] · nullable Optional 

 The MITRE ATT&CK tactic identifiers associated with this rule. Returns an empty array if no tactics are mapped. 

 mitreTechniques string[] · nullable Optional 

 The MITRE ATT&CK technique identifiers associated with this rule. Returns an empty array if no techniques are mapped. 

 name string Optional 

 Name of the Appsec rule. 

 owner string Optional 

 The internal service owner of the rule. 

 Example: CAS 

 scanner string · enum Optional 

 The scanner type used by this rule to detect security issues. 

 Possible values : CICD IAC SCA SECRETS 

 severity string · enum Optional 

 Severity level of the rule 

 Possible values : CRITICAL HIGH LOW MEDIUM 

 subCategory string Optional 

 Custom rule subcategory. 

 Example: STORAGE_BUCKETS 

 complianceStandards object · ComplianceStandard Optional 

 An array of compliance standards associated with this rule. 

 Show properties 

 cspmRuleId string · nullable Optional 

 The ID of the mapped Cloud Security rule. When set, findings from this AppSec rule are correlated with the corresponding Cloud Security rule. Returns null if no rule is mapped. 

 cspmTypeId number · nullable Optional 

 The numeric type identifier of the mapped Cloud Security rule. Returned only when the AppSec rule is linked to a rule via cspmRuleId . 

 Example: 60100018 

 get /public_api/appsec/v1/rules/ {ruleId} 

 HTTP 

 Ask Copy 

 GET /public_api/appsec/v1/rules/{ruleId} HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: your-api-key 
 x-xdr-auth-id: 1 
 Accept: */* 

 200 

 Ok 

 Ask Copy 

 { 
 "category": "text", 
 "cloudProvider": "GCP", 
 "createdAt": "2026-01-01T00:00:00.000Z", 
 "description": "text", 
 "shortDescription": "text", 
 "detectionMethod": "IaC Security", 
 "docLink": "text", 
 "domain": "POSTURE", 
 "findingCategory": "Code", 
 "findingDocs": "Custom IaC rule for Public Exposure Storage Buckets", 
 "findingTypeId": 30040031, 
 "findingTypeName": "text", 
 "frameworks": [ 
 { 
 "frameworkDetails": { 
 "definition": "text", 
 "definition_link": "text", 
 "name": "TERRAFORM", 
 "remediation_description": "text", 
 "remediation_ids": [ 
 "text" 
 ], 
 "resource_types": [ 
 "text" 
 ] 
 } 
 } 
 ], 
 "id": "text", 
 "isCustom": true, 
 "isEnabled": true, 
 "labels": [ 
 "text" 
 ], 
 "updatedAt": "2026-01-01T00:00:00.000Z", 
 "mitreTactics": [ 
 "text" 
 ], 
 "mitreTechniques": [ 
 "text" 
 ], 
 "name": "text", 
 "owner": "CAS", 
 "scanner": "CICD", 
 "severity": "CRITICAL", 
 "subCategory": "STORAGE_BUCKETS", 
 "complianceStandards": { 
 "standardName": "CIS Amazon Elastic Kubernetes Service (EKS) Benchmark v1.4_copy v1.4", 
 "controls": [ 
 { 
 "controlName": "The default namespace should not be used", 
 "controlDefinition": "Kubernetes provides a default namespace, where objects are placed if no namespace is specified for them. Placing objects in this namespace makes application of RBAC and other controls more difficult." 
 } 
 ] 
 }, 
 "cspmRuleId": "text", 
 "cspmTypeId": 60100018 
 } 

 Delete an AppSec rule 

 delete https://api-yourfqdn /public_api/appsec/v1/rules/ {ruleId} 

 Delete the specified Application Security rule. 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. Not supported in XSIAM Enterprise Plus. 

 Path parameters 

 ruleId string Required 

 Unique identifier of the Application Security rule 

 Header parameters 

 Authorization string Required 

 {api_key} 

 Example: your-api-key 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Example: 1 

 Responses 

 200 

 Ok 

 application/json 

 message string Required 

 delete /public_api/appsec/v1/rules/ {ruleId} 

 HTTP 

 Ask Copy 

 DELETE /public_api/appsec/v1/rules/{ruleId} HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: your-api-key 
 x-xdr-auth-id: 1 
 Accept: */* 

 200 

 Ok 

 Ask Copy 

 { 
 "message": "text" 
 } 

 Update an AppSec rule 

 patch https://api-yourfqdn /public_api/appsec/v1/rules/ {ruleId} 

 Update an existing Application Security rule. If it's an out-of-the-box rule, the only modification you can make is to add labels. For custom rules, you can modify all of the fields. 

 Note: To customize an out-of-the-box rule, you can create a custom rule by cloning the existing one. This allows you to make changes to the original rule according to your requirements. 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. Not supported in XSIAM Enterprise Plus. 

 Path parameters 

 ruleId string Required 

 Unique identifier of the Application Security rule 

 Header parameters 

 Authorization string Required 

 {api_key} 

 Example: your-api-key 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Example: 1 

 Body 

 application/json 

 object · CreateOrModifyCustomRuleRequestParams Optional 

 Define the Application Security custom rule. The category option should match your selection for scanner . 

 Show properties 

 or 

 object · ModifyRuleParams Optional 

 Show properties 

 Responses 

 200 

 Ok 

 application/json 

 Updated details of the modified Application Security rule 

 rule object · DetectionRule Optional 

 Details of the Application Security rule 

 Show properties 

 patch /public_api/appsec/v1/rules/ {ruleId} 

 HTTP 

 Ask Copy 

 PATCH /public_api/appsec/v1/rules/{ruleId} HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: your-api-key 
 x-xdr-auth-id: 1 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 633 

 { 
 "name": "S3 Bucket Public Access Check", 
 "description": "Detects S3 buckets with public access enabled", 
 "severity": "CRITICAL", 
 "labels": [ 
 "S3-Security" 
 ], 
 "scanner": "IAC", 
 "frameworks": { 
 "name": "TERRAFORM", 
 "definition": "definition:\\n cond_type: attribute\\n resource_types:\\n - aws_s3_bucket_public_access_block\\n attribute: block_public_acls\\n operator: equals\\n value: false", 
 "definitionLink": "text", 
 "remediationDescription": "Set block_public_acls to true in aws_s3_bucket_public_access_block resource" 
 }, 
 "category": "PUBLIC", 
 "subCategory": "STORAGE_BUCKETS", 
 "cspmRuleId": "ff6a26a5-f036-4d3a-a650-d5de1d568bab", 
 "clonedFromRuleId": "text" 
 } 

 200 

 Ok 

 Ask Copy 

 { 
 "rule": { 
 "category": "PUBLIC", 
 "cloudProvider": null, 
 "createdAt": { 
 "value": "2024-01-01T00:00:00.000Z" 
 }, 
 "description": "Detects S3 buckets with public access enabled", 
 "detectionMethod": "IaC Security", 
 "domain": "POSTURE", 
 "findingTypeId": 30040031, 
 "frameworks": [ 
 { 
 "definition": "definition:\n cond_type: attribute\n resource_types:\n - aws_s3_bucket_public_access_block\n attribute: block_public_acls\n operator: equals\n value: false\nmetadata:\n name: S3 Bucket Public Access Check\n category: public\n severity: high\n guidelines: Detects S3 buckets with public access enabled\n", 
 "definitionLink": null, 
 "name": "TERRAFORM", 
 "remediationDescription": "Set block_public_acls to true in aws_s3_bucket_public_access_block resource", 
 "remediationIds": [], 
 "resourceTypes": [] 
 } 
 ], 
 "id": "APPSEC_CUSTOM_<rule-id>", 
 "isCustom": true, 
 "isEnabled": true, 
 "labels": [ 
 "Custom-Rule", 
 "S3-Security" 
 ], 
 "name": "s3 bucket public access check", 
 "owner": "CAS", 
 "scanner": "IAC", 
 "severity": "HIGH", 
 "subCategory": "STORAGE_BUCKETS", 
 "updatedAt": { 
 "value": "2024-02-01T00:00:00.000Z" 
 }, 
 "findingCategory": "Configuration", 
 "findingDocs": "Custom IaC rule for Public Exposure Storage Buckets", 
 "mitreTactics": [], 
 "mitreTechniques": [], 
 "shortDescription": null, 
 "complianceStandards": [], 
 "cspmRuleId": "<cspm-rule-id>", 
 "cspmTypeId": 60100018 
 } 
 } 

 Get AppSec rule labels 

 get https://api-yourfqdn /public_api/appsec/v1/rules/rule-labels 

 Get a list of all of the Application Security rule labels. 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. Not supported in XSIAM Enterprise Plus. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 Example: UCoWpG4rkNzgCp2dsh8m02iVpZsskwKHz7N1tErPcUV3Wmf59Gc9kytmgOv0pDWoem3PBlORyRIPiir4OcYdWUOWAM3JyTgoCxQf4nQoTlKmFRKz9Bj5vIjluw66p9WP 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Example: 241 

 Responses 

 200 

 Ok 

 application/json 

 A list of labels 

 labels string[] Optional 

 get /public_api/appsec/v1/rules/rule-labels 

 HTTP 

 Ask Copy 

 GET /public_api/appsec/v1/rules/rule-labels HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: UCoWpG4rkNzgCp2dsh8m02iVpZsskwKHz7N1tErPcUV3Wmf59Gc9kytmgOv0pDWoem3PBlORyRIPiir4OcYdWUOWAM3JyTgoCxQf4nQoTlKmFRKz9Bj5vIjluw66p9WP 
 x-xdr-auth-id: 241 
 Accept: */* 

 200 

 Ok 

 Ask Copy 

 { 
 "labels": [ 
 "text" 
 ] 
 } 

 Create an AppSec rule validation 

 post https://api-yourfqdn /public_api/appsec/v1/rules/validate 

 Required license: Cortex XSIAM Premium. In Cortex XSIAM Enterprise and Cortex NG SIEM, requires the Cortex Cloud Posture Management add-on. Not supported in XSIAM Enterprise Plus. 

 Body object · ValidateCustomRuleRequestParams[] 

 application/json 

 framework string · enum Required 

 Name of the configured Infrastructure as Code (IaC) framework for this rule definition. Note: Applicable only when scanner is set to IAC . 

 Example: TERRAFORM Possible values : ARM BICEP CLOUDFORMATION KUBERNETES TERRAFORM 

 definition string Required 

 Responses 

 200 

 Ok 

 application/json 

 object Optional 

 Show properties 

 or 

 object Optional 

 Show properties 

 post /public_api/appsec/v1/rules/validate 

 HTTP 

 Ask Copy 

 POST /public_api/appsec/v1/rules/validate HTTP/1.1 
 Host: api-yourfqdn 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 47 

 [ 
 { 
 "framework": "TERRAFORM", 
 "definition": "text" 
 } 
 ] 

 200 

 Ok 

 Ask Copy 

 { 
 "frameworksErrors": [ 
 { 
 "framework": "TERRAFORM", 
 "errors": [ 
 "text" 
 ] 
 } 
 ] 
 } 

 Previous Remediations 

 Next SBOM Management 

 Last updated 12 hours ago 

 Was this helpful?
