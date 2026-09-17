---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/third-party-integrations-lifecycle-administration-and-automation/reference-a-programmatic-automation-and-key-rotation
fetched_at: 2026-09-16T08:49:00Z
source: cortex-platform
---

# Reference A: Programmatic automation and key rotation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 Onboard data sources 

 Ingest third-party data sources 

 Third-party integrations lifecycle administration and automation 

 Reference A: Programmatic automation and key rotation 

 Reference for third-party integration API operations. 

 Use the API workflow for automation, bulk operations across multiple tenants, and programmatic key rotation. For comprehensive request and response schemas, query parameters, and error codes, refer to the Cortex API Documentation . 

 Automated key rotation via public REST API 

 Integrate programmatic rotation with secrets managers, such as HashiCorp Vault, through the public AppSec Integrations API. 

 SonarQube endpoint: PUT /public_api/appsec/v1/integrations/{id} updates the complete SonarQube configuration, including credentials 

 Checkmarx endpoint: PATCH /public_api/appsec/v1/data_source_instances/{instance_id}/credentials rotates Checkmarx One API keys 

 Authentication: Requests require the x-xdr-auth-id header and Authorization header. Generate both credentials with a user holding Data Sources (View/Edit) permission 

 SonarQube programmatic key rotation payload example 

 Ask Copy 

 # Retrieve the latest credentials from HashiCorp Vault 
 NEW_SONAR_TOKEN = $( vault kv get -field=token secret/cortex/sonarqube ) 

 # Update the integration credentials in Cortex Cloud 
 curl -X PUT " https://api.cortexcloud.security/public_api/appsec/v1/integrations/sonarqube-instance-123 " \ 
 -H " Authorization: Bearer ${ CORTEX_API_KEY }" \ 
 -H " x-xdr-auth-id: ${ CORTEX_API_KEY_ID }" \ 
 -H " Content-Type: application/json " \ 
 -d ' { 
 "name": "Production SonarQube Server", 
 "product_type": "SonarQube", 
 "connection_method": "Direct", 
 "base_url": "https://sonar.company.com:9000", 
 "credentials": { 
 "api_token": " '"${ NEW_SONAR_TOKEN }"' " 
 } 
 } ' --fail 

 Generic Data Source Integration CRUD Operations (Snyk, Semgrep, Veracode, Checkmarx, Custom Collectors) 

 All third-party vendor integrations, except SonarQube, use the unified generic data source endpoints under /public_api/appsec/v1/data_source_instances . 

 When programmatically provisioning or configuring instances for Snyk , Semgrep , Veracode , Checkmarx One , or Custom Collectors , use these core endpoints. 

 Operation 

 Method 

 Endpoint / Path 

 Required role 

 Description 

 List data sources 

 GET 

 /public_api/appsec/v1/data_source_instances 

 AppSec Admin 

 Lists all registered AppSec data source integrations. Scope requests with the type_category query parameter ( EXTERNAL_VENDOR_INTEGRATIONS or DEFAULT ). 

 Get data source by ID 

 GET 

 /public_api/appsec/v1/data_source_instances/{id} 

 AppSec Admin 

 Retrieves the configuration, sync status, and repository-scoping metadata for a specific instance. 

 Create data source 

 POST 

 /public_api/appsec/v1/data_source_instances 

 AppSec Admin 

 Provisions and authenticates a polling instance or custom push-based collector. 

 Update data source 

 PUT 

 /public_api/appsec/v1/data_source_instances/{id} 

 AppSec Admin 

 Modifies repository mappings, selected scan types, or active project configurations. 

 Delete data source 

 DELETE 

 /public_api/appsec/v1/data_source_instances/{id} 

 AppSec Admin 

 Permanently deletes the integration instance, invalidates credentials, and removes repository mappings. 

 Upload SAST findings 

 POST 

 /public_api/appsec/v1/collectors/{collectorId} 

 n/a (Collector Scoped) 

 Ingests custom third-party SARIF v2.1.0 payloads from CI/CD workflows. 

 Checkmarx One specialized sub-path API operations 

 While Checkmarx One instances use the generic CRUD endpoints, specialized sub-paths manage credentials and project-to-repository branch maps: 

 Operation 

 Method 

 Endpoint / Path 

 Required role 

 Description 

 Rotate Checkmarx API key 

 PATCH 

 /public_api/appsec/v1/data_source_instances/{instance_id}/credentials 

 AppSec Admin 

 Rotates the stored Checkmarx One API key or client secret without changing project or repository mappings. 

 Update project-to-repository maps 

 PUT 

 /public_api/appsec/v1/data_source_instances/{instance_id}/mappings 

 AppSec Admin 

 Maps discovered Checkmarx One projects to Cortex Cloud repositories and branches. 

 SonarQube / SonarCloud specialized API operations and Transporter workflows 

 For self-hosted SonarQube Server or SonarCloud SaaS, use these specialized endpoints to automate integrations. 

 Critical Transporter Network Paths: For an on-premises SonarQube Server behind a private domain, validate the AppSec Transporter Broker VM tunnel first. 

 Operation 

 Method 

 Endpoint / Path 

 Required role 

 Description 

 Retrieve transporter data 

 GET 

 /api/cas/v1/integrations/transporter 

 AppSec Admin 

 Transporter path only: Returns Broker VM device IDs and registered AppSec Transporter connection names. Use brokerDeviceId and connectionName in the creation payload. Served under the tenant API root. 

 Validate the domain 

 POST 

 /api/cas/v1/integrations/validate-domain/{type} 

 AppSec Admin 

 Validates the SonarQube Server base URL and transporter connectivity before instance creation. Served under the tenant API root. 

 Create SonarQube integration 

 POST 

 /public_api/appsec/v1/integrations 

 AppSec Admin 

 Creates and configures a SonarQube Server or SonarCloud SaaS integration. Served under the public API root. 

 Retrieve SonarQube integration 

 GET 

 /public_api/appsec/v1/integrations/{id} 

 AppSec Admin 

 Returns SonarQube integration properties and active connection health. Served under the public API root. 

 Update SonarQube integration 

 PUT 

 /public_api/appsec/v1/integrations/{id} 

 AppSec Admin 

 Updates SonarQube base URLs, organization keys, credentials, or transporter associations. Served under the public API root. 

 Delete SonarQube integration 

 DELETE 

 /public_api/appsec/v1/integrations/{id} 

 AppSec Admin 

 Deletes the integration and purges SonarQube findings from Code Weaknesses. Served under the public API root. 

 Previous Third-party integrations lifecycle administration and automation 

 Next Reference B: GitOps and infrastructure-as-code (IaC) 

 Last updated 19 days ago 

 Was this helpful?
