---
url: https://cortex-docs.paloaltonetworks.com/agentix-api/cortex-agentix/issues
fetched_at: 2026-09-16T09:04:10Z
source: cortex-platform
---

# Issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex AgentiX 

 AgentiX APIs 

 Cortex Agentix 

 Issues 

 APIs for managing issues 

 Create a new issue 

 post https://api-{{fqdn}} /public_api/v1/issue 

 This endpoint allows users to create a new issue by providing the necessary details. Users can only create one issue at a time. 

 The request must include the following required fields: 

 name 

 description 

 observation_time 

 domain 

 category 

 Body 

 application/json 

 request_data object Optional 

 Show properties 

 Responses 

 202 

 Issue created successfully 

 application/json 

 external_id string Optional 

 detection_method string Optional 

 400 

 Bad request 

 application/json 

 401 

 Unauthorized access 

 application/json 

 500 

 Internal server error 

 application/json 

 post /public_api/v1/issue 

 HTTP 

 Ask Copy 

 POST /public_api/v1/issue HTTP/1.1 
 Host: api-{{fqdn}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 5106 

 { 
 "request_data": { 
 "issue": { 
 "owner": "CWP", 
 "name": "Unauthorized Access Detected", 
 "description": "An unauthorized login attempt was detected from an unknown IP address.", 
 "observation_time": 1700000000000, 
 "domain": "SECURITY", 
 "category": "CONFIGURATION", 
 "asset_ids": [ 
 "asset-456" 
 ], 
 "mitre_tactics": [ 
 "TA0001", 
 "TA0002" 
 ], 
 "mitre_techniques": [ 
 "T1003", 
 "T1059" 
 ], 
 "type": "Threat Intelligence", 
 "extended_description": "This alert was triggered due to multiple failed login attempts within a short time frame.", 
 "impact": "Potential unauthorized system access", 
 "tags": [ 
 "critical", 
 "network" 
 ], 
 "is_excluded": false, 
 "is_starred": true, 
 "assigned_to": "security_team_lead", 
 "assigned_to_pretty": "Alice Smith", 
 "severity": "HIGH", 
 "normalized_fields": { 
 "xdm.source.location.country": "US", 
 "xdm.source.ipv4": "192.168.1.1", 
 "xdm.source.host.ipv4_addresses": [ 
 "192.168.1.2", 
 "192.168.1.3" 
 ], 
 "xdm.source.identity.username": "admin", 
 "xdm.source.process.causality_id": "abc123", 
 "xdm.source.process.command_line": "/usr/bin/process -arg1 -arg2", 
 "xdm.source.process.executable.filename": "process_executable", 
 "xdm.source.process.name": "process_name", 
 "xdm.source.process.executable.path": "/usr/bin/process_executable", 
 "xdm.source.process.executable.sha256": "f9c7b6e24f7e93d8d3e5c76f8b1b88cd8f17b34a7a4a2e3d5b2dbf09f5b8fdc2", 
 "xdm.source.host.hostname": "hostname1", 
 "xdm.source.host.os_family": "Linux", 
 "xdm.source.agent.identifier": "agent123", 
 "xdm.source.agent.installation_id": "installation123", 
 "xdm.source.host.fqdn": "hostname1.domain.com", 
 "xdm.source.process.executable.signature_status": "Valid", 
 "xdm.target.file.filename": "target_file.txt", 
 "xdm.target.module.filename": "target_module.so", 
 "xdm.target.file.sha256": "d4bfc6fabe8d6d1b76e5b441dc8d01758276281f56c929b282ac5c3ee704c431", 
 "xdm.target.module.sha256": "7f4eafdad74bfedabf370a3725a5077c", 
 "xdm.target.process.command_line": "/usr/bin/target_process -option", 
 "xdm.target.process.executable.sha256": "7b21d50d6270f95b5a2cf582bf94b315cd75a034dd9478c0e5b4089bbd9b59ac", 
 "xdm.target.process.executable.signature_status": "Signed", 
 "xdm.target.process.executable.signer": [ 
 "text" 
 ], 
 "xdm.target.process.executable.path": [ 
 "text" 
 ], 
 "xdm.target.ipv4": [ 
 "text" 
 ], 
 "xdm.target.host.ipv4_addresses": [ 
 "10.0.0.2", 
 "10.0.0.3" 
 ], 
 "xdm.target.host.ipv6_addresses": [ 
 "text" 
 ], 
 "xdm.target.ipv6": [ 
 "10.0.0.2", 
 "10.0.0.3" 
 ], 
 "xdm.target.port": 8080, 
 "xdm.target.location.country": "US", 
 "xdm.target.host.hostname": "hostname", 
 "xdm.target.identity.username": "user1", 
 "xdm.target.url": "https://example.com", 
 "xdm.target.process.executable.filename": "target_process", 
 "xdm.target.process.name": "target_process", 
 "xdm.target.agent.identifier": "target_agent", 
 "xdm.target.registry.value": "registry_value", 
 "xdm.target.registry.data": "registry_data", 
 "xdm.target.registry.key": "registry_key", 
 "xdm.email.attachment.sha256": "a1b2c3d4e5f6789abcde1234567890f2", 
 "xdm.email.attachment.filename": "attachment.pdf", 
 "xdm.email.sender": "sender@example.com", 
 "xdm.event.type": "Intrusion", 
 "xdm.cloud.provider": "AWS", 
 "xdm.cloud.project": "CloudProject1", 
 "xdm.cloud.project_id": "cloud_project_id_123", 
 "xdm.cloud.region": "us-east-1", 
 "xdm.cloud.function.id": "cloud_func_123", 
 "xdm.cloud.function.name": "cloud_function", 
 "xdm.cloud.function.version": "v1.0.0", 
 "xdm.cloud.function.request_id": "req_123", 
 "xdm.cloud.function.runtime": "nodejs", 
 "xdm.observer.unique_identifier": "observer123", 
 "xdm.observer.type": "Server", 
 "xdm.observer.sub_type": "Linux", 
 "xdm.observer.name": "Observer 1", 
 "xdm.vulnerability.cve_id": "CVE-2021-12345", 
 "xdm.vulnerability.severity": "HIGH", 
 "xdm.vulnerability.fix_versions": [ 
 "1.0.1", 
 "1.0.2" 
 ], 
 "xdm.vulnerability.cve_risk_factors": [ 
 "Exploitability", 
 "Impact" 
 ], 
 "xdm.vulnerability.cvss_score": 7.8, 
 "xdm.vulnerability.cvss_vector": "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", 
 "xdm.software_package.version": "1.0.0", 
 "xdm.software_package.purl": "pkg:maven/com.example/software@1.0.0", 
 "xdm.software_package.layer_id": "layer123", 
 "xdm.software_package.type": "Library", 
 "xdm.software_package.installation_type": "Automatic", 
 "xdm.software_package.package_manager": "npm", 
 "xdm.software_package.dependency_type": "Direct", 
 "xdm.software_package.language": "JavaScript", 
 "xdm.malware.verdict": "Malicious", 
 "xdm.malware.virus_total_link": "https://www.virustotal.com/gui/file/abcd1234", 
 "xdm.malware.layer_id": "malware_layer123", 
 "xdm.secret.secret_type": "API Key", 
 "xdm.secret.unique_identifier": "secret_id_123", 
 "xdm.secret.snippet": "API Key: 12345", 
 "xdm.secret.layer_id": "secret_layer123", 
 "xdm.file.filename": "file.txt", 
 "xdm.file.path": "/path/to/file.txt", 
 "xdm.file.sha256": "abc1234567890def0987654321", 
 "xdm.file.size": 1024, 
 "xdm.file.last_modified": 1615465123, 
 "xdm.file.metadata_change_time": 1615465000, 
 "xdm.file.owner_id": "user1", 
 "xdm.file.owner_name": "fileowner", 
 "xdm.file.group_id": "group1", 
 "xdm.file.group_name": "groupname", 
 "xdm.file.permissions.owner": [ 
 "read", 
 "write" 
 ], 
 "xdm.file.permissions.group": [ 
 "read" 
 ], 
 "xdm.file.permissions.others": [ 
 "read" 
 ], 
 "xdm.file.position.start.line": 1, 
 "xdm.file.position.start.character": 0, 
 "xdm.file.position.end.line": 100, 
 "xdm.file.position.end.character": 80, 
 "xdm.url": "https://example.com", 
 "xdm.domain": "example.com", 
 "xdm.application_protocol": "HTTPS" 
 }, 
 "custom_fields": {} 
 } 
 } 
 } 

 202 

 Issue created successfully 

 Ask Copy 

 { 
 "external_id": "7c96737d50f74c7b9487450426e9eafb", 
 "detection_method": "CREATE_ALERT_PUBLIC_API" 
 } 

 Retrieve issues based on filters 

 post https://api-{{fqdn}} /public_api/v1/issue/search 

 This endpoint retrieves a list of issues that match the specified filter criteria. It supports filtering by issue_id , external_id , detection_method , domain , source , severity , and _insert_time , along with sorting and pagination. 

 Request Body: 

 request_data : Object containing filter criteria 

 filters : Array of filter objects 

 field : String (enum: 'issue_id', 'external_id', 'detection_method', 'domain', 'severity', '_insert_time', 'status') 

 operator : String (enum: 'in', 'gte', 'lte') 

 value : Array of integers/strings or single integer 

 search_from : Integer (default: 0) - Starting index for pagination 

 search_to : Integer (default: 100) - Ending index for pagination 

 sort : Object for sorting results 

 field : String (enum: '_insert_time', 'severity', 'issue_id') 

 keyword : String (enum: 'asc', 'desc') - Sort order 

 include_fields : Array of strings (enum: 'normalized_fields', 'custom_fields', default: []) - Fields to include in response 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object Optional 

 Show properties 

 Responses 

 200 

 Successful response with issues 

 application/json 

 reply object Optional 

 Show properties 

 400 

 Bad request 

 application/json 

 401 

 Unauthorized access 

 application/json 

 500 

 Internal server error 

 application/json 

 post /public_api/v1/issue/search 

 HTTP 

 Ask Copy 

 POST /public_api/v1/issue/search HTTP/1.1 
 Host: api-{{fqdn}} 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 186 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "issue_id", 
 "operator": "in", 
 "value": [ 
 1 
 ] 
 } 
 ], 
 "search_from": 1, 
 "search_to": 1, 
 "sort": { 
 "field": "id", 
 "keyword": "asc" 
 }, 
 "include_fields": [ 
 "normalized_fields" 
 ] 
 } 
 } 

 200 

 Successful response with issues 

 Ask Copy 

 { 
 "reply": { 
 "total_count": 1, 
 "result_count": 1, 
 "issues": [ 
 { 
 "_insert_time": "2023-05-15T10:30:00Z", 
 "owner": "CWP", 
 "external_id": "EXT-12345", 
 "name": "Suspicious Network Activity", 
 "description": "Unusual outbound traffic detected from internal server", 
 "observation_time": 1621234567890, 
 "domain": "SECURITY", 
 "detection_method": "CSPM_SCANNER", 
 "detection_rule_id": "RULE-9876", 
 "category": "CONFIGURATION", 
 "finding_ids": [ 
 "013543ea00ea9893bcde59cbfdc5992f" 
 ], 
 "asset_ids": [ 
 "123" 
 ], 
 "mitre_tactics": [ 
 "COLLECTION" 
 ], 
 "mitre_techniques": [ 
 "ABUSE_ELEVATION_CONTROL_MECHANISM" 
 ], 
 "type": "Identity Security", 
 "remediation": "Isolate affected system and investigate traffic patterns", 
 "extended_description": "Detailed analysis of the network traffic patterns and potential impact", 
 "impact": "Potential data exfiltration or command and control activity", 
 "issue_id": 123, 
 "last_modified": 1621235678901, 
 "tags": [ 
 "critical", 
 "investigation_required" 
 ], 
 "is_excluded": false, 
 "is_starred": true, 
 "assigned_to": "alice.smith@example.com", 
 "assigned_to_pretty": "Alice Smith", 
 "status": "Resolved", 
 "status_resolution_reason": "RESOLVED_OTHER", 
 "status_resolution_comment": "Investigating the source of suspicious traffic", 
 "severity": "HIGH", 
 "resolution_time": 1621240000000, 
 "normalized_fields": { 
 "xdm.source.location.country": "US", 
 "xdm.source.ipv4": "192.168.1.1", 
 "xdm.source.host.ipv4_addresses": [ 
 "192.168.1.2", 
 "192.168.1.3" 
 ], 
 "xdm.source.identity.username": "admin", 
 "xdm.source.process.causality_id": "abc123", 
 "xdm.source.process.command_line": "/usr/bin/process -arg1 -arg2", 
 "xdm.source.process.executable.filename": "process_executable", 
 "xdm.source.process.name": "process_name", 
 "xdm.source.process.executable.path": "/usr/bin/process_executable", 
 "xdm.source.process.executable.sha256": "f9c7b6e24f7e93d8d3e5c76f8b1b88cd8f17b34a7a4a2e3d5b2dbf09f5b8fdc2", 
 "xdm.source.host.hostname": "hostname1", 
 "xdm.source.host.os_family": "Linux", 
 "xdm.source.agent.identifier": "agent123", 
 "xdm.source.agent.installation_id": "installation123", 
 "xdm.source.host.fqdn": "hostname1.domain.com", 
 "xdm.source.process.executable.signature_status": "Valid", 
 "xdm.target.file.filename": "target_file.txt", 
 "xdm.target.module.filename": "target_module.so", 
 "xdm.target.file.sha256": "d4bfc6fabe8d6d1b76e5b441dc8d01758276281f56c929b282ac5c3ee704c431", 
 "xdm.target.module.sha256": "7f4eafdad74bfedabf370a3725a5077c", 
 "xdm.target.process.command_line": "/usr/bin/target_process -option", 
 "xdm.target.process.executable.sha256": "7b21d50d6270f95b5a2cf582bf94b315cd75a034dd9478c0e5b4089bbd9b59ac", 
 "xdm.target.process.executable.signature_status": "Signed", 
 "xdm.target.process.executable.signer": [ 
 "text" 
 ], 
 "xdm.target.process.executable.path": [ 
 "text" 
 ], 
 "xdm.target.ipv4": [ 
 "text" 
 ], 
 "xdm.target.host.ipv4_addresses": [ 
 "10.0.0.2", 
 "10.0.0.3" 
 ], 
 "xdm.target.host.ipv6_addresses": [ 
 "text" 
 ], 
 "xdm.target.ipv6": [ 
 "10.0.0.2", 
 "10.0.0.3" 
 ], 
 "xdm.target.port": 8080, 
 "xdm.target.location.country": "US", 
 "xdm.target.host.hostname": "hostname", 
 "xdm.target.identity.username": "user1", 
 "xdm.target.url": "https://example.com", 
 "xdm.target.process.executable.filename": "target_process", 
 "xdm.target.process.name": "target_process", 
 "xdm.target.agent.identifier": "target_agent", 
 "xdm.target.registry.value": "registry_value", 
 "xdm.target.registry.data": "registry_data", 
 "xdm.target.registry.key": "registry_key", 
 "xdm.email.attachment.sha256": "a1b2c3d4e5f6789abcde1234567890f2", 
 "xdm.email.attachment.filename": "attachment.pdf", 
 "xdm.email.sender": "sender@example.com", 
 "xdm.event.type": "Intrusion", 
 "xdm.cloud.provider": "AWS", 
 "xdm.cloud.project": "CloudProject1", 
 "xdm.cloud.project_id": "cloud_project_id_123", 
 "xdm.cloud.region": "us-east-1", 
 "xdm.cloud.function.id": "cloud_func_123", 
 "xdm.cloud.function.name": "cloud_function", 
 "xdm.cloud.function.version": "v1.0.0", 
 "xdm.cloud.function.request_id": "req_123", 
 "xdm.cloud.function.runtime": "nodejs", 
 "xdm.observer.unique_identifier": "observer123", 
 "xdm.observer.type": "Server", 
 "xdm.observer.sub_type": "Linux", 
 "xdm.observer.name": "Observer 1", 
 "xdm.vulnerability.cve_id": "CVE-2021-12345", 
 "xdm.vulnerability.severity": "HIGH", 
 "xdm.vulnerability.fix_versions": [ 
 "1.0.1", 
 "1.0.2" 
 ], 
 "xdm.vulnerability.cve_risk_factors": [ 
 "Exploitability", 
 "Impact" 
 ], 
 "xdm.vulnerability.cvss_score": 7.8, 
 "xdm.vulnerability.cvss_vector": "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", 
 "xdm.software_package.version": "1.0.0", 
 "xdm.software_package.purl": "pkg:maven/com.example/software@1.0.0", 
 "xdm.software_package.layer_id": "layer123", 
 "xdm.software_package.type": "Library", 
 "xdm.software_package.installation_type": "Automatic", 
 "xdm.software_package.package_manager": "npm", 
 "xdm.software_package.dependency_type": "Direct", 
 "xdm.software_package.language": "JavaScript", 
 "xdm.malware.verdict": "Malicious", 
 "xdm.malware.virus_total_link": "https://www.virustotal.com/gui/file/abcd1234", 
 "xdm.malware.layer_id": "malware_layer123", 
 "xdm.secret.secret_type": "API Key", 
 "xdm.secret.unique_identifier": "secret_id_123", 
 "xdm.secret.snippet": "API Key: 12345", 
 "xdm.secret.layer_id": "secret_layer123", 
 "xdm.file.filename": "file.txt", 
 "xdm.file.path": "/path/to/file.txt", 
 "xdm.file.sha256": "abc1234567890def0987654321", 
 "xdm.file.size": 1024, 
 "xdm.file.last_modified": 1615465123, 
 "xdm.file.metadata_change_time": 1615465000, 
 "xdm.file.owner_id": "user1", 
 "xdm.file.owner_name": "fileowner", 
 "xdm.file.group_id": "group1", 
 "xdm.file.group_name": "groupname", 
 "xdm.file.permissions.owner": [ 
 "read", 
 "write" 
 ], 
 "xdm.file.permissions.group": [ 
 "read" 
 ], 
 "xdm.file.permissions.others": [ 
 "read" 
 ], 
 "xdm.file.position.start.line": 1, 
 "xdm.file.position.start.character": 0, 
 "xdm.file.position.end.line": 100, 
 "xdm.file.position.end.character": 80, 
 "xdm.url": "https://example.com", 
 "xdm.domain": "example.com", 
 "xdm.application_protocol": "HTTPS" 
 }, 
 "custom_fields": {} 
 } 
 ] 
 } 
 } 

 Update existing issue 

 post https://api-{{fqdn}} /public_api/v1/issue/{issue-id} 

 Update an existing issue in the system. Users can only update one issue at a time. 

 At least one of the following fields is mandatory : 

 severity 

 status 

 Path parameters 

 issue-id integer Required 

 Numeric ID of the user to get 

 Body 

 application/json 

 request_data object Optional 

 Show properties 

 Responses 

 204 

 Issues updated successfully 

 No content 

 400 

 Bad request 

 application/json 

 401 

 Unauthorized access 

 application/json 

 500 

 Internal server error 

 application/json 

 post /public_api/v1/issue/{issue-id} 

 HTTP 

 Ask Copy 

 POST /public_api/v1/issue/{issue-id} HTTP/1.1 
 Host: api-{{fqdn}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 189 

 { 
 "request_data": { 
 "update_data": { 
 "severity": "HIGH", 
 "status": "Resolved", 
 "status_resolution_reason": "RESOLVED_OTHER", 
 "status_resolution_comment": "Issue has been marked as a false positive." 
 } 
 } 
 } 

 204 

 Issues updated successfully 

 No content 

 Create a new issue exception 

 post https://api-{{fqdn}} /public_api/v1/issue_exceptions/ 

 This endpoint allows users to create a new issue exception by providing the necessary details. Users can only create one exception at a time. 

 The request must include the following required fields: 

 name 

 rule 

 justification_text 

 justification_category 

 expiration_ts 

 approver_email 

 Optional fields: 

 external_exception_id 

 If the tenant has approval required enabled, the approver_email field is mandatory and the exception will be created with Pending Status status. Otherwise, the exception is Self Approved automatically. 

 The requestor_name and requestor_email fields are automatically populated from the API key context. 

 Required permission: Exception Management Admin View/Edit , Exception Approver Admin View/Edit 

 For the complete list of fields you can use as SEARCH_FIELD in the rule parameter, see Issue exception supported fields . 

 Required license: Cortex AgentiX Enterprise or Cortex AgentiX Base 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object · CreateIssueException Optional 

 Request data for creating a new issue exception. 

 Show properties 

 Responses 

 200 

 Exception created successfully 

 application/json 

 reply object Optional 

 Show properties 

 400 

 Bad request 

 application/json 

 401 

 Unauthorized access 

 application/json 

 500 

 Internal server error 

 application/json 

 post /public_api/v1/issue_exceptions/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/issue_exceptions/ HTTP/1.1 
 Host: api-{{fqdn}} 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 374 

 { 
 "request_data": { 
 "name": "CVE-2024-1234 Exception for legacy hosts", 
 "rule": "{\"filter\":{\"AND\":[{\"SEARCH_FIELD\":\"cve_id\",\"SEARCH_TYPE\":\"EQ\",\"SEARCH_VALUE\":\"CVE-2024-1234\"}]}}", 
 "justification_text": "Legacy hosts scheduled for decommission in Q2", 
 "justification_category": "RISK_ACCEPTED", 
 "approver_email": "security-lead@example.com", 
 "expiration_ts": "2025-06-30" 
 } 
 } 

 Create basic issue exception 

 200 

 Exception created successfully 

 Ask Copy 

 { 
 "reply": { 
 "exception_id": 42 
 } 
 } 

 Disable an issue exception 

 post https://api-{{fqdn}} /public_api/v1/issue_exceptions/disable/ 

 This endpoint allows users to disable an existing issue exception. This will trigger a reversion scan to restore matching issues that were previously suppressed by this exception. A disabled exception cannot be reactivated. 

 Required permission: Exception Management Admin View/Edit , Exception Approver Admin View/Edit 

 Required license: Cortex AgentiX Enterprise or Cortex AgentiX Base 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object Optional 

 Show properties 

 Responses 

 200 

 Exception disabled successfully 

 application/json 

 reply object Optional 

 Show properties 

 400 

 Bad request 

 application/json 

 401 

 Unauthorized access 

 application/json 

 500 

 Internal server error 

 application/json 

 post /public_api/v1/issue_exceptions/disable/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/issue_exceptions/disable/ HTTP/1.1 
 Host: api-{{fqdn}} 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 36 

 { 
 "request_data": { 
 "exception_id": 26 
 } 
 } 

 200 

 Exception disabled successfully 

 Ask Copy 

 { 
 "reply": { 
 "rows_affected": 1, 
 "status": "DISABLED" 
 } 
 } 

 Retrieve issue exceptions based on filters 

 post https://api-{{fqdn}} /public_api/v1/issue_exceptions/search/ 

 This endpoint retrieves a list of issue exceptions that match the specified filter criteria. It supports filtering along with sorting and pagination. 

 Required permission: Exception Management Admin View , Exception Approver Admin View 

 Required license: Cortex AgentiX Enterprise or Cortex AgentiX Base 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 request_data object Optional 

 Show properties 

 Responses 

 200 

 Exceptions retrieved successfully 

 application/json 

 reply object Optional 

 Show properties 

 400 

 Bad request 

 application/json 

 401 

 Unauthorized access 

 application/json 

 500 

 Internal server error 

 application/json 

 post /public_api/v1/issue_exceptions/search/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/issue_exceptions/search/ HTTP/1.1 
 Host: api-{{fqdn}} 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 19 

 { 
 "request_data": {} 
 } 

 Default search (all exceptions, first 100) 

 200 

 Exceptions retrieved successfully 

 Ask Copy 

 { 
 "reply": { 
 "exceptions": [ 
 { 
 "exception_id": 1, 
 "external_exception_id": null, 
 "name": "CVE-2024-1234 Exception", 
 "status": "APPROVED", 
 "rule": "{\"filter\":{\"AND\":[{\"SEARCH_FIELD\":\"cve_id\",\"SEARCH_TYPE\":\"EQ\",\"SEARCH_VALUE\":\"CVE-2024-1234\"}]}}", 
 "pretty_rule": "[\"cve_id = CVE-2024-1234\"]", 
 "justification_text": "Risk accepted for legacy hosts", 
 "justification_category": "RISK_ACCEPTED", 
 "approval_justification": null, 
 "requestor_name": "John Doe", 
 "requestor_email": "john.doe@example.com", 
 "approver_email": "security-lead@example.com", 
 "approver_name": "Jane Smith", 
 "created_ts": "2025-01-15T10:30:00Z", 
 "modified_ts": "2025-01-15T10:30:00Z", 
 "approval_ts": "2025-01-15T11:00:00Z", 
 "expiration_ts": "2025-06-30T23:59:59Z", 
 "impacted_issues_count": 150, 
 "backward_scan_status": "COMPLETED", 
 "backward_scan_ts": "2025-01-15T11:05:00Z", 
 "reversion_scan_status": null, 
 "reversion_scan_ts": null 
 } 
 ], 
 "filter_count": 1, 
 "total_count": 10 
 } 
 } 

 Insert parsed alerts 

 post https://api-yourfqdn /public_api/v1/alerts/insert_parsed_alerts/ 

 Upload alerts from external alert sources in Cortex XDR format. Cortex XDR displays alerts that are parsed successfully in related incidents and views. 

 You can send 600 alerts per minute. Each request can contain a maximum of 60 alerts. 

 Required license: Cortex XDR Pro per Endpoint or Cortex XDR Pro per GB 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 request_data object Optional 

 The request payload containing the alerts to upload. 

 Show properties 

 Responses 

 200 

 Successful response 

 application/json 

 boolean Optional 

 true indicates the upload was successful. 

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

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/alerts/insert_parsed_alerts/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/alerts/insert_parsed_alerts/ HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 396 

 { 
 "request_data": { 
 "alerts": [ 
 { 
 "product": "VPN & Firewall-1", 
 "vendor": "<vendor name>", 
 "local_ip": "<IP address>", 
 "local_port": "<port>", 
 "remote_ip": "<IP address>", 
 "remote_port": "<port>", 
 "event_timestamp": 1543270652000, 
 "severity": "Low", 
 "alert_name": "Alert Name Example", 
 "alert_description": "Alert Description", 
 "action_status": "Reported", 
 "local_ip_v6": "<IPv6 address>", 
 "remote_ip_v6": "<IPv6 address>" 
 } 
 ] 
 } 
 } 

 200 

 Successful response 

 Ask Copy 

 true 

 Previous Dataset Management 

 Next Lookup Datasets 

 Last updated 1 month ago 

 Was this helpful?
