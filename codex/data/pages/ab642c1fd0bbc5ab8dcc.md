---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-api/vulnerability-management/vulnerability-findings
fetched_at: 2026-09-06T10:55:04Z
source: cortex-platform
---

# Vulnerability Findings | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex Cloud 

 Cortex Cloud APIs 

 Vulnerability Management 

 Vulnerability Findings 

 vulnerability finding records (paginated or by ID) 

 List vulnerability findings (paginated) 

 post https://api-yourfqdn /vulnerability-management/v1/vulnerability-finding/search 

 Returns paginated vulnerability findings — one record per CVE/asset pair. Use next_page_token from the response to fetch subsequent pages. 

 Pagination: Control the number of records per page with the optional page_size field (default 1000 , maximum 10000 ). 

 Rate limit: Up to 1,000 requests per 24-hour rolling window. Exceeding this limit returns HTTP 429 . 

 Supported filter fields and filter types: 

 Each filter clause is an object with SEARCH_FIELD , SEARCH_TYPE , and SEARCH_VALUE . The SEARCH_TYPE values supported per field depend on the field's data type: 

 Filter field ( SEARCH_FIELD ) 

 Data type 

 Supported filter types ( SEARCH_TYPE ) 

 ASSET_NAME 

 string 

 EQ , NEQ , IN , NIN , CONTAINS , NCONTAINS , WILDCARD , WILDCARD_NOT 

 ASSET_GROUP_IDS 

 ID array 

 ARRAY_OVERLAPS 

 ASSET_CATEGORY 

 string 

 EQ , NEQ , IN , NIN 

 CVE_ID 

 string 

 EQ , NEQ , IN , NIN , CONTAINS 

 CVSS_SEVERITY 

 enum string 

 EQ , NEQ , IN , NIN 

 PLATFORM_ID 

 string 

 EQ , NEQ , IN , NIN 

 FIX_AVAILABLE 

 boolean 

 EQ 

 PACKAGE_IN_USE 

 boolean 

 EQ 

 HAS_KEV 

 boolean 

 EQ 

 EXPLOIT_LEVEL 

 enum string 

 EQ , NEQ , IN , NIN 

 EPSS_SCORE 

 number (0–1) 

 EQ , GT , GTE , LT , LTE , RANGE 

 INTERNET_EXPOSED 

 boolean 

 EQ 

 FIRST_OBSERVED 

 timestamp (ms) 

 GT , GTE , LT , LTE , RANGE , RELATIVE_TIMESTAMP 

 LAST_OBSERVED 

 timestamp (ms) 

 GT , GTE , LT , LTE , RANGE , RELATIVE_TIMESTAMP 

 Sortable fields: EPSS_SCORE , CVSS_SCORE , CORTEX_VULNERABILITY_RISK_SCORE . 

 Filter value reference: 

 When filtering on CVSS_SEVERITY or EXPLOIT_LEVEL with SEARCH_TYPE EQ , use the following SEARCH_VALUE values: 

 CVSS_SEVERITY : SEV_070_CRITICAL , SEV_060_HIGH , SEV_050_MEDIUM , SEV_040_LOW 

 EXPLOIT_LEVEL : WEAPONIZED , POC , NONE 

 Filtering on ASSET_GROUP_IDS : 

 ASSET_GROUP_IDS is an array field, so it only supports the ARRAY_OVERLAPS filter type. Supply SEARCH_VALUE as a list of numeric asset-group IDs; the clause matches a finding when the asset belongs to any of the listed groups. To match findings that do not belong to any of the listed groups, wrap the clause in a NOT block instead of an AND block. 

 Example (match any of the groups): 

 Example (exclude the groups): 

 Note: Response payloads return normalized severity strings (for example, HIGH or LOW ) that are not valid filter inputs. Always use the SEV_0xx_* values above when filtering by CVSS_SEVERITY . 

 Required license: Cortex Cloud Runtime Security or Cortex Cloud Posture Management. 

 Authorizations 

 ApiKeyAuth & ApiKeyNonce 

 Body 

 application/json 

 Request body for paginated vulnerability findings search. 

 filter object · FilterBlock Optional 

 Logical filter block. Supports AND / OR connectors with a list of FilterTriplet objects. 

 Show properties 

 sort object · FindingsSortObject[] Optional 

 Optional sort criteria. Sortable fields: EPSS_SCORE , CVSS_SCORE , CORTEX_VULNERABILITY_RISK_SCORE . 

 Show properties 

 page_size integer · min: 1 · max: 10000 Optional 

 Number of records to return per page. Defaults to 1000 ; the maximum allowed value is 10000 . Requests exceeding the maximum return HTTP 400 . 

 Default: 1000 Example: 1000 

 next_page_token string Optional 

 Opaque token returned by a previous response to fetch the next page. Omit on the first request. 

 Example: eyJsYXN0X2VsZW1lbnQiOiAxMjM0fQ== 

 Responses 

 200 

 Successful response with vulnerability findings. 

 application/json 

 Paginated response containing vulnerability findings. 

 reply object Optional 

 Show properties 

 400 

 Invalid filter parameters or expired page token. 

 application/json 

 429 

 Rate limit exceeded. This endpoint allows up to 1,000 requests per 24-hour rolling window. 

 application/json 

 post /vulnerability-management/v1/vulnerability-finding/search 

 HTTP 

 Ask Copy 

 POST /vulnerability-management/v1/vulnerability-finding/search HTTP/1.1 
 Host: api-yourfqdn 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 178 

 { 
 "request_data": { 
 "filter": { 
 "AND": [ 
 { 
 "SEARCH_FIELD": "LAST_OBSERVED", 
 "SEARCH_TYPE": "RELATIVE_TIMESTAMP", 
 "SEARCH_VALUE": 2592000000 
 } 
 ] 
 }, 
 "sort": [ 
 { 
 "FIELD": "CVSS_SCORE", 
 "ORDER": "DESC" 
 } 
 ] 
 } 
 } 

 Filter by last observed (relative timestamp) and sort by CVSS score 

 200 

 Successful response with vulnerability findings. 

 Ask Copy 

 { 
 "reply": { 
 "data": [ 
 { 
 "cortex_vulnerability_risk_score": null, 
 "asset_name": "SNMP Server at 89.170.90.209:161", 
 "cve_id": "CVE-2025-20169", 
 "cve_description": "A vulnerability in the SNMP subsystem of Cisco IOS Software and Cisco IOS XE Software could allow an authenticated, remote attacker to cause a DoS condition on an affected device.\r\n\r\nThis vulnerability is due to improper error handling when parsing SNMP requests. An attacker could exploit this vulnerability by sending a crafted SNMP request to an affected device. A successful exploit could allow the attacker to cause the device to reload unexpectedly, resulting in a DoS condition. \r\nThis vulnerability affects SNMP versions 1, 2c, and 3. To exploit this vulnerability through SNMP v2c or earlier, the attacker must know a valid read-write or read-only SNMP community string for the affected system. To exploit this vulnerability through SNMP v3, the attacker must have valid SNMP user credentials for the affected system.", 
 "epss_score": 0.00368, 
 "cvss_score": 7.7, 
 "cvss_severity": "HIGH", 
 "fix_versions": [], 
 "fix_date": null, 
 "published_date": 1738713600000, 
 "cve_risk_factors": [ 
 "Attack vector: network", 
 "High severity", 
 "Attack complexity: low", 
 "DoS - High" 
 ], 
 "affected_software": null, 
 "has_kev": null, 
 "exploitable": false, 
 "exploit_level": "NONE", 
 "asset_type": "SERVICE", 
 "asset_category": "Service", 
 "has_issue": false, 
 "ipv4_addresses": [ 
 "89.170.90.209" 
 ], 
 "ipv6_addresses": [], 
 "operating_system": null, 
 "os_family": null, 
 "location": null, 
 "internet_exposed": true, 
 "provider": "ON_PREM", 
 "finding_sources": [ 
 "CORTEX_ATTACK_SURFACE_MANAGEMENT" 
 ], 
 "first_observed": 1764890719158, 
 "last_observed": 1764715866000, 
 "source_tags": [ 
 "asm.attribution.organization_names:[Parameter FAKE_2332423424]" 
 ], 
 "layer_id": null, 
 "image": null, 
 "origin_package_name": null, 
 "package_file_creation_time": null, 
 "package_licenses": [], 
 "package_version": null, 
 "package_purl": null, 
 "package_type": null, 
 "cve_publish_date": 1738713600000, 
 "platform_id": "c273519c3b61adfb7dc46547fbcbfa32", 
 "asset_id": "fef704015fd52a8495025f830b7483988d170f93b5807617761e4af827275a83", 
 "fix_available": false, 
 "package_in_use": null, 
 "file_path": null, 
 "package_symbols": [], 
 "package_author": null, 
 "application_version": null, 
 "asset_type_class": "External Surface", 
 "type_id": "140000000", 
 "derived_from_base_image": null, 
 "is_derived": false, 
 "image_name": null, 
 "asset_group_ids": [], 
 "volume_asset_id": null, 
 "is_root": null, 
 "volume_path": null, 
 "partition_id": null, 
 "partition_id_type": null, 
 "disk_name": null, 
 "remediation": null, 
 "issue_id": null 
 } 
 ], 
 "filter_count": 342, 
 "total_count": 10500, 
 "next_page_token": "eyJsYXN0X2VsZW1lbnQiOiA1Njc4fQ==" 
 } 
 } 

 Response with more pages available 

 Get a single vulnerability finding by platform ID 

 post https://api-yourfqdn /vulnerability-management/v1/vulnerability-finding/ {platform_id} 

 Returns the vulnerability finding record for the given platform_id . Returns HTTP 404 when no matching finding exists. 

 Required license: Cortex Cloud Runtime Security or Cortex Cloud Posture Management. 

 Authorizations 

 ApiKeyAuth & ApiKeyNonce 

 Path parameters 

 platform_id string Required 

 Unique platform identifier for a vulnerability finding. 

 Example: abc123def456 

 Body 

 application/json 

 object Optional 

 Empty body — no request parameters required. 

 Responses 

 200 

 Vulnerability finding record. 

 application/json 

 Response containing a single vulnerability finding by platform ID. 

 reply object Optional 

 Show properties 

 400 

 Missing or invalid platform_id. 

 application/json 

 404 

 No finding found for the given platform_id. 

 application/json 

 post /vulnerability-management/v1/vulnerability-finding/ {platform_id} 

 HTTP 

 Ask Copy 

 POST /vulnerability-management/v1/vulnerability-finding/{platform_id} HTTP/1.1 
 Host: api-yourfqdn 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 2 

 {} 

 200 

 Vulnerability finding record. 

 Ask Copy 

 { 
 "reply": { 
 "data": [ 
 { 
 "cortex_vulnerability_risk_score": null, 
 "asset_name": "SNMP Server at 89.170.90.209:161", 
 "cve_id": "CVE-2025-20169", 
 "cve_description": "A vulnerability in the SNMP subsystem of Cisco IOS Software and Cisco IOS XE Software could allow an authenticated, remote attacker to cause a DoS condition on an affected device.\r\n\r\nThis vulnerability is due to improper error handling when parsing SNMP requests. An attacker could exploit this vulnerability by sending a crafted SNMP request to an affected device. A successful exploit could allow the attacker to cause the device to reload unexpectedly, resulting in a DoS condition. \r\nThis vulnerability affects SNMP versions 1, 2c, and 3. To exploit this vulnerability through SNMP v2c or earlier, the attacker must know a valid read-write or read-only SNMP community string for the affected system. To exploit this vulnerability through SNMP v3, the attacker must have valid SNMP user credentials for the affected system.", 
 "epss_score": 0.00368, 
 "cvss_score": 7.7, 
 "cvss_severity": "HIGH", 
 "fix_versions": [], 
 "fix_date": null, 
 "published_date": 1738713600000, 
 "cve_risk_factors": [ 
 "Attack vector: network", 
 "High severity", 
 "Attack complexity: low", 
 "DoS - High" 
 ], 
 "affected_software": null, 
 "has_kev": null, 
 "exploitable": false, 
 "exploit_level": "NONE", 
 "asset_type": "SERVICE", 
 "asset_category": "Service", 
 "has_issue": false, 
 "ipv4_addresses": [ 
 "89.170.90.209" 
 ], 
 "ipv6_addresses": [], 
 "operating_system": null, 
 "os_family": null, 
 "location": null, 
 "internet_exposed": true, 
 "provider": "ON_PREM", 
 "finding_sources": [ 
 "CORTEX_ATTACK_SURFACE_MANAGEMENT" 
 ], 
 "first_observed": 1764890719158, 
 "last_observed": 1764715866000, 
 "source_tags": [ 
 "asm.attribution.organization_names:[Parameter FAKE_2332423424]" 
 ], 
 "layer_id": null, 
 "image": null, 
 "origin_package_name": null, 
 "package_file_creation_time": null, 
 "package_licenses": [], 
 "package_version": null, 
 "package_purl": null, 
 "package_type": null, 
 "cve_publish_date": 1738713600000, 
 "platform_id": "c273519c3b61adfb7dc46547fbcbfa32", 
 "asset_id": "fef704015fd52a8495025f830b7483988d170f93b5807617761e4af827275a83", 
 "fix_available": false, 
 "package_in_use": null, 
 "file_path": null, 
 "package_symbols": [], 
 "package_author": null, 
 "application_version": null, 
 "asset_type_class": "External Surface", 
 "type_id": "140000000", 
 "derived_from_base_image": null, 
 "is_derived": false, 
 "image_name": null, 
 "asset_group_ids": [], 
 "volume_asset_id": null, 
 "is_root": null, 
 "volume_path": null, 
 "partition_id": null, 
 "partition_id_type": null, 
 "disk_name": null, 
 "remediation": null, 
 "issue_id": null 
 } 
 ] 
 } 
 } 

 Previous Vulnerability Management 

 Next Vulnerability Findings Snapshot 

 Last updated 16 days ago 

 Was this helpful?
