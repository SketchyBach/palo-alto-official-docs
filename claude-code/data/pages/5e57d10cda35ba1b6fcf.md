---
url: https://cortex-docs.paloaltonetworks.com/xpanse-api/xpanse-public-api/incident-management
fetched_at: 2026-09-06T10:56:29Z
source: cortex-platform
---

# Incident Management | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex Xpanse 

 Xpanse APIs 

 Xpanse Public API 

 Incident Management 

 APIs for managing incidents 

 Get Alerts 

 post https://api-{{fqdn}} /public_api/v2/alerts/get_alerts_multi_events/ 

 Get a single alert or list of alerts with multiple events. 

 Response is concatenated using AND condition (OR is not supported). 

 Maximum result set size is 100. 

 Offset is the zero-based number of alerts from the start of the result set. 

Note: You can send a request to retrieve all or filtered results.
Required license: Cortex Xpanse Expander 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · GetAlertsMultiEventsRequestData Required 

 A dictionary containing the API request fields. An empty dictionary returns all results. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 Successful response 

 application/json 

 reply object · GetAlertsMultiEventsPage Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v2/alerts/get_alerts_multi_events/ 

 HTTP 

 Ask Copy 

 POST /public_api/v2/alerts/get_alerts_multi_events/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 227 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "business_units_list", 
 "operator": "gte", 
 "value": "string" 
 } 
 ], 
 "search_from": 0, 
 "search_to": 100, 
 "sort": { 
 "field": "creation_time", 
 "keyword": "desc" 
 }, 
 "use_page_token": true, 
 "next_page_token": "string" 
 } 
 } 

 Filtering by business_unit_list and sorting by creation_time 

 200 

 Successful response 

 Ask Copy 

 { 
 "reply": { 
 "total_count": 1, 
 "result_count": 1, 
 "alerts": [ 
 { 
 "category": "text", 
 "project": "text", 
 "cloud_provider": "text", 
 "resource_sub_type": "text", 
 "resource_type": "text", 
 "action_country": [ 
 "text" 
 ], 
 "description": "text", 
 "events": "text", 
 "event_type": "text", 
 "is_whitelisted": true, 
 "image_name": "text", 
 "action_local_ip": "text", 
 "action_local_port": "text", 
 "mitre_tactic_id_and_name": [ 
 "text" 
 ], 
 "mitre_technique_id_and_name": [ 
 "text" 
 ], 
 "action_external_hostname": "text", 
 "action_remote_ip": [ 
 "text" 
 ], 
 "action_remote_port": [ 
 1 
 ], 
 "matching_service_rule_id": "text", 
 "starred": true, 
 "external_id": "text", 
 "severity": "text", 
 "matching_status": "text", 
 "end_match_attempt_ts": "text", 
 "local_insert_ts": 1, 
 "last_modified_ts": 1, 
 "case_id": 1, 
 "deduplicate_tokens": "text", 
 "filter_rule_id": "text", 
 "event_id": "text", 
 "event_timestamp": [ 
 1 
 ], 
 "action_local_ip_v6": "text", 
 "action_remote_ip_v6": [ 
 "text" 
 ], 
 "alert_type": "text", 
 "resolution_status": "text", 
 "resolution_comment": "text", 
 "dynamic_fields": "text", 
 "tags": [ 
 "text" 
 ], 
 "malicious_urls": "text", 
 "asm_alert_categories": [ 
 "text" 
 ], 
 "aws_cloud_tags": [ 
 "text" 
 ], 
 "azure_cloud_tags": [ 
 "text" 
 ], 
 "gcp_cloud_tags": [ 
 "text" 
 ], 
 "last_observed": 1, 
 "country_codes": [ 
 "text" 
 ], 
 "cloud_providers": [ 
 "text" 
 ], 
 "ipv4_addresses": [ 
 "text" 
 ], 
 "ipv6_addresses": [ 
 "text" 
 ], 
 "domain_names": [ 
 "text" 
 ], 
 "service_ids": [ 
 "text" 
 ], 
 "website_ids": [ 
 "text" 
 ], 
 "asset_ids": [ 
 "text" 
 ], 
 "certificate": { 
 "issuerName": "text", 
 "subjectName": "text", 
 "validNotBefore": 1, 
 "validNotAfter": 1, 
 "serialNumber": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "port_protocol": "text", 
 "port_number": 1, 
 "cloud_management_status": "text", 
 "business_unit_hierarchies": [ 
 [ 
 { 
 "creation_time": 1, 
 "family": "text", 
 "family_alias": "text", 
 "id": "text", 
 "is_active": 1, 
 "name": "text", 
 "parent_id": "text", 
 "update_time": 1, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ] 
 ], 
 "attack_surface_rule_name": "text", 
 "remediation_guidance": "text", 
 "attack_surface_rule_id": "text", 
 "asset_identifiers": [ 
 { 
 "domain": "text", 
 "certificate": { 
 "issuerName": "text", 
 "subjectName": "text", 
 "validNotBefore": 1, 
 "validNotAfter": 1, 
 "serialNumber": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ipv4Address": "text", 
 "ipv6Address": "text", 
 "httpPath": "text", 
 "portNumber": 1, 
 "portProtocol": "text", 
 "firstObserved": 1, 
 "lastObserved": 1, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "integration_source": "text", 
 "alert_id": "text", 
 "detection_timestamp": 1, 
 "name": "text", 
 "endpoint_id": "text", 
 "host_ip": "text", 
 "host_name": "text", 
 "action": "text", 
 "source": "text", 
 "user_name": "text", 
 "mac_addresses": "text", 
 "action_pretty": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "next_page_token": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Get Incidents 

 post https://api-{{fqdn}} /public_api/v1/incidents/get_incidents/ 

 Get details for a single incident or a list of incidents filtered by a list of severity or creation time. - The response is concatenated using AND condition (OR is not supported).
- The maximum result set size is >100.
- Offset is the zero-based number of incidents from the start of the result set.

Note: You can send a request to retrieve either all or filtered results.

Required license: Cortex Xpanse Expander 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · GetIncidentsRequestData Required 

 A dictionary containing the API request fields. An empty dictionary returns all results. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 Successful response 

 application/json 

 reply object · GetIncidentsPage Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/incidents/get_incidents/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/incidents/get_incidents/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 251 

 { 
 "request_data": { 
 "filters": [ 
 { 
 "field": "modification_time", 
 "operator": "in", 
 "value": "text" 
 } 
 ], 
 "search_from": 0, 
 "search_to": 100, 
 "sort": { 
 "field": "modification_time", 
 "keyword": "desc", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 Successful response 

 Ask Copy 

 { 
 "reply": { 
 "total_count": 1, 
 "result_count": 1, 
 "incidents": [ 
 { 
 "incident_id": "text", 
 "is_blocked": true, 
 "incident_name": "text", 
 "creation_time": 1, 
 "modification_time": 1, 
 "detection_time": 1, 
 "status": "text", 
 "severity": "text", 
 "description": "text", 
 "assigned_user_mail": "text", 
 "assigned_user_pretty_name": "text", 
 "alert_count": 1, 
 "low_severity_alert_count": 1, 
 "med_severity_alert_count": 1, 
 "high_severity_alert_count": 1, 
 "critical_severity_alert_count": 1, 
 "user_count": 1, 
 "host_count": 1, 
 "notes": "text", 
 "resolve_comment": "text", 
 "resolved_timestamp": 1, 
 "manual_severity": "text", 
 "manual_description": "text", 
 "xdr_url": "text", 
 "starred": true, 
 "starred_manually": true, 
 "hosts": [ 
 "text" 
 ], 
 "incident_sources": [ 
 "text" 
 ], 
 "rule_based_score": 1, 
 "manual_score": 1, 
 "aggregated_score": 1, 
 "alerts_grouping_status": "text", 
 "alert_categories": [ 
 "text" 
 ], 
 "original_tags": [ 
 "text" 
 ], 
 "tags": [ 
 "text" 
 ], 
 "xpanse_risk_score": 1, 
 "xpanse_risk_explainer": { 
 "cves": [ 
 { 
 "cveId": "text", 
 "cvssScore": 1, 
 "epssScore": 1, 
 "matchType": "text", 
 "exploitMaturity": "text", 
 "reportedExploitInTheWild": true, 
 "mostRecentReportedExploitDate": "text", 
 "confidence": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "riskFactors": [ 
 { 
 "attributeId": "text", 
 "attributeName": "text", 
 "issueTypes": [ 
 { 
 "displayName": "text", 
 "issueTypeId": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "versionMatched": true, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "cloud_management_status": "text", 
 "integration_source": "text", 
 "ipv4_addresses": [ 
 "text" 
 ], 
 "ipv6_addresses": [ 
 "text" 
 ], 
 "domain_names": [ 
 "text" 
 ], 
 "port_number": 1, 
 "asset_ids": [ 
 "123e4567-e89b-12d3-a456-426614174000" 
 ], 
 "ip_range_ids": [ 
 "text" 
 ], 
 "website_ids": [ 
 "text" 
 ], 
 "service_ids": [ 
 "text" 
 ], 
 "last_observed": 1, 
 "cloud_providers": [ 
 "text" 
 ], 
 "country_codes": [ 
 "text" 
 ], 
 "certificate_common_names": [ 
 "text" 
 ], 
 "certificate_issuers": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "restricted_incident_ids": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Get Extra Incident Data 

 post https://api-{{fqdn}} /public_api/v1/incidents/get_incident_extra_data/ 

 Get extra data fields for a specific incident including alerts and key artifacts. 

 Note: The API includes a limit rate of 10 API requests per minute. 

 Required license: Cortex Xpanse Expander 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · GetIncidentExtraDataRequestData Required 

 A dictionary containing the API request fields. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 OK 

 application/json 

 reply object · GetIncidentExtraDataReply Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 429 

 Exceeded 10 requests in a 60-second window. 

 If you get this response, wait 60 seconds and retry your request. 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/incidents/get_incident_extra_data/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/incidents/get_incident_extra_data/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 130 

 { 
 "request_data": { 
 "incident_id": "text", 
 "alerts_limit": 1, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "reply": { 
 "incident": { 
 "incident_id": "text", 
 "is_blocked": true, 
 "incident_name": "text", 
 "creation_time": 1, 
 "modification_time": 1, 
 "detection_time": 1, 
 "status": "text", 
 "severity": "text", 
 "description": "text", 
 "assigned_user_mail": "text", 
 "assigned_user_pretty_name": "text", 
 "alert_count": 1, 
 "low_severity_alert_count": 1, 
 "med_severity_alert_count": 1, 
 "high_severity_alert_count": 1, 
 "critical_severity_alert_count": 1, 
 "user_count": 1, 
 "host_count": 1, 
 "notes": "text", 
 "resolve_comment": "text", 
 "resolved_timestamp": 1, 
 "manual_severity": "text", 
 "manual_description": "text", 
 "xdr_url": "text", 
 "starred": true, 
 "starred_manually": true, 
 "hosts": [ 
 "text" 
 ], 
 "incident_sources": [ 
 "text" 
 ], 
 "rule_based_score": 1, 
 "manual_score": 1, 
 "aggregated_score": 1, 
 "alerts_grouping_status": "text", 
 "alert_categories": [ 
 "text" 
 ], 
 "original_tags": [ 
 "text" 
 ], 
 "tags": [ 
 "text" 
 ], 
 "xpanse_risk_score": 1, 
 "xpanse_risk_explainer": { 
 "cves": [ 
 { 
 "cveId": "text", 
 "cvssScore": 1, 
 "epssScore": 1, 
 "matchType": "text", 
 "exploitMaturity": "text", 
 "reportedExploitInTheWild": true, 
 "mostRecentReportedExploitDate": "text", 
 "confidence": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "riskFactors": [ 
 { 
 "attributeId": "text", 
 "attributeName": "text", 
 "issueTypes": [ 
 { 
 "displayName": "text", 
 "issueTypeId": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "versionMatched": true, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "cloud_management_status": "text", 
 "integration_source": "text", 
 "ipv4_addresses": [ 
 "text" 
 ], 
 "ipv6_addresses": [ 
 "text" 
 ], 
 "domain_names": [ 
 "text" 
 ], 
 "port_number": 1, 
 "asset_ids": [ 
 "123e4567-e89b-12d3-a456-426614174000" 
 ], 
 "ip_range_ids": [ 
 "text" 
 ], 
 "website_ids": [ 
 "text" 
 ], 
 "service_ids": [ 
 "text" 
 ], 
 "last_observed": 1, 
 "cloud_providers": [ 
 "text" 
 ], 
 "country_codes": [ 
 "text" 
 ], 
 "certificate_common_names": [ 
 "text" 
 ], 
 "certificate_issuers": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "alerts": { 
 "total_count": 1, 
 "data": [ 
 { 
 "category": "text", 
 "project": "text", 
 "cloud_provider": "text", 
 "resource_sub_type": "text", 
 "resource_type": "text", 
 "action_country": "text", 
 "event_type": "text", 
 "is_whitelisted": true, 
 "mac": "text", 
 "image_name": "text", 
 "action_local_ip": "text", 
 "action_local_port": "text", 
 "action_external_hostname": "text", 
 "action_remote_ip": [ 
 "text" 
 ], 
 "action_remote_port": 1, 
 "matching_service_rule_id": "text", 
 "starred": true, 
 "external_id": "text", 
 "severity": "text", 
 "matching_status": "text", 
 "end_match_attempt_ts": "text", 
 "local_insert_ts": 1, 
 "last_modified_ts": 1, 
 "case_id": 1, 
 "deduplicate_tokens": "text", 
 "filter_rule_id": "text", 
 "event_id": "text", 
 "event_timestamp": 1, 
 "action_local_ip_v6": "text", 
 "action_remote_ip_v6": "text", 
 "alert_type": "text", 
 "resolution_status": "text", 
 "resolution_comment": "text", 
 "dynamic_fields": "text", 
 "tags": "text", 
 "malicious_urls": "text", 
 "asm_alert_categories": "text", 
 "last_observed": 1, 
 "country_codes": "text", 
 "cloud_providers": "text", 
 "ipv4_addresses": "text", 
 "ipv6_addresses": "text", 
 "domain_names": "text", 
 "service_ids": "text", 
 "website_ids": "text", 
 "asset_ids": "text", 
 "certificate": { 
 "issuerName": "text", 
 "subjectName": "text", 
 "validNotBefore": 1, 
 "validNotAfter": 1, 
 "serialNumber": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "port_protocol": "text", 
 "port_number": 1, 
 "business_unit_hierarchies": [ 
 { 
 "creation_time": 1, 
 "family": "text", 
 "family_alias": "text", 
 "id": "text", 
 "is_active": 1, 
 "name": "text", 
 "parent_id": "text", 
 "update_time": 1, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "attack_surface_rule_name": "text", 
 "remediation_guidance": "text", 
 "attack_surface_rule_id": "text", 
 "asset_identifiers": { 
 "domain": "text", 
 "certificate": { 
 "issuerName": "text", 
 "subjectName": "text", 
 "validNotBefore": 1, 
 "validNotAfter": 1, 
 "serialNumber": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ipv4Address": "text", 
 "ipv6Address": "text", 
 "httpPath": "text", 
 "portNumber": 1, 
 "portProtocol": "text", 
 "firstObserved": 1, 
 "lastObserved": 1, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "alert_id": "text", 
 "detection_timestamp": 1, 
 "name": "text", 
 "endpoint_id": "text", 
 "description": "text", 
 "host_ip": "text", 
 "host_name": "text", 
 "source": "text", 
 "action": "text", 
 "action_pretty": "text", 
 "user_name": "text", 
 "events_length": 1, 
 "mitre_tactic_id_and_name": "text", 
 "mitre_technique_id_and_name": "text", 
 "cloud_management_status": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "network_artifacts": { 
 "total_count": 1, 
 "data": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "file_artifacts": { 
 "total_count": 1, 
 "data": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Update Alerts 

 post https://api-{{fqdn}} /public_api/v1/alerts/update_alerts/ 

 Update one or more alerts. You can update up to 100 alerts per request. Missing fields are ignored.
Required license: Cortex Xpanse Expander 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · UpdateAlertsData Required 

 (Required) A dictionary containing the API request fields. An empty dictionary returns all results. 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 Successful response 

 application/json 

 reply object · AlertIdsList Required 

 Show properties 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/alerts/update_alerts/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/alerts/update_alerts/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 184 

 { 
 "request_data": { 
 "alert_id_list": [ 
 "text" 
 ], 
 "update_data": { 
 "severity": "text", 
 "status": "text", 
 "comment": "text" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 Successful response 

 Ask Copy 

 { 
 "reply": { 
 "alerts_ids": [ 
 1 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Update an Incident 

 post https://api-{{fqdn}} /public_api/v1/incidents/update_incident/ 

 Update one or more fields of a specific incident. Missing fields are ignored.
Note the following: 

 assigned_user_mail field is validated by Cortex Xpanse to confirm the provided assignee email address belongs to a user that exists in the same Cortex Xpanse tenant. 

 To unassign an incident pass none or ”assigned_user_mail”: “” . 

 To remove a manually set severity pass none or “manual_severity”: “” . 

 Header parameters 

 authorization string Required 

 api-key 

 Example: {{api_key}} 

 x-xdr-auth-id string Required 

 api-key-id 

 Example: {{api_key_id}} 

 Body 

 application/json 

 request_data object · UpdateIncidentRequestData Required 

 Show properties 

 Other properties any Optional 

 Responses 

 200 

 Successful response 

 application/json 

 reply boolean Required 

 warnings string[] Optional 

 Other properties any Optional 

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

 422 

 Unprocessable Entity 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /public_api/v1/incidents/update_incident/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/incidents/update_incident/ HTTP/1.1 
 Host: api-{{fqdn}} 
 authorization: {{api_key}} 
 x-xdr-auth-id: {{api_key_id}} 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 385 

 { 
 "request_data": { 
 "incident_id": "text", 
 "update_data": { 
 "assigned_user_mail": "text", 
 "assigned_user_pretty_name": "text", 
 "manual_severity": "low", 
 "status": "resolved", 
 "resolve_comment": "text", 
 "comment": { 
 "comment_action": "add", 
 "value": "text", 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 }, 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 200 

 Successful response 

 Ask Copy 

 { 
 "reply": true, 
 "warnings": [ 
 "text" 
 ], 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Previous Audit Log 

 Next Remediation Path Rules 

 Last updated 1 month ago 

 Was this helpful?
