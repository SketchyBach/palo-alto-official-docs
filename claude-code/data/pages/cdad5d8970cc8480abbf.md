---
url: https://cortex-docs.paloaltonetworks.com/xdr-5-api/netscan/vulnerability-network-scan-management
fetched_at: 2026-09-16T09:04:06Z
source: cortex-platform
---

# Vulnerability Network Scan Management | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XDR 

 XDR 5.x APIs 

 Netscan 

 Vulnerability Network Scan Management 

 Public API for network scan configuration and management. 

 Get scan run status 

 get https://api-cortex.paloaltonetworks.com /public_api/netscan/v1/scan/run 

 Retrieve the current status of a scan run by its ID. Use the fields parameter to specify which fields to return in the response. 

 Query parameters 

 id integer · int64 Required 

 Scan run ID to check status for 

 fields string[] Required 

 Fields to include in the response (for example, status ). 

 Header parameters 

 User-Agent string Required 

 Responses 

 200 

 Scan status retrieved successfully 

 application/json 

 Response containing the current status of a scan run 

 DATA string Required 

 Scan status message 

 Example: Scan is in Running state 

 400 

 Bad Request 

 application/json 

 403 

 User not Authorized 

 application/json 

 404 

 Run ID not found 

 application/json 

 500 

 Internal Server Error 

 application/json 

 get /public_api/netscan/v1/scan/run 

 HTTP 

 Ask Copy 

 GET /public_api/netscan/v1/scan/run?id=1&fields=text HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 User-Agent: text 
 Accept: */* 

 200 

 Scan status retrieved successfully 

 Ask Copy 

 { 
 "DATA": "Scan is in Running state" 
 } 

 Launch a scan run 

 post https://api-cortex.paloaltonetworks.com /public_api/netscan/v1/scan/run 

 Launch a scan execution using a previously configured scan definition. Optionally override the target IP addresses for this specific run. 

 Header parameters 

 User-Agent string Required 

 Body 

 application/json 

 request_data object Required 

 Show properties 

 Responses 

 200 

 Scan launched successfully 

 application/json 

 Response returned after a scan action (launch, pause, resume, or abort) 

 DATA string Required 

 Action result message 

 Example: Scan launched successfully with run ID: 789 

 400 

 Bad Request 

 application/json 

 403 

 User not Authorized 

 application/json 

 404 

 Not found 

 application/json 

 500 

 Internal Server Error 

 application/json 

 post /public_api/netscan/v1/scan/run 

 HTTP 

 Ask Copy 

 POST /public_api/netscan/v1/scan/run HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 User-Agent: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 62 

 { 
 "request_data": { 
 "definition_id": 123, 
 "target": "1.2.3.4.0/12" 
 } 
 } 

 200 

 Scan launched successfully 

 Ask Copy 

 { 
 "DATA": "Scan launched successfully with run ID: 789" 
 } 

 Get scan run status by ID 

 get https://api-cortex.paloaltonetworks.com /public_api/netscan/v1/scan/run/ {id} 

 Retrieve the current status of a specific scan run identified by the path parameter. Use the fields parameter to specify which fields to return in the response. 

 Path parameters 

 id integer · int64 Required 

 Scan run ID 

 Query parameters 

 fields string[] Required 

 Fields to include in the response (for example, status ). 

 Header parameters 

 User-Agent string Required 

 Responses 

 200 

 Scan status retrieved successfully 

 application/json 

 Response containing the current status of a scan run 

 DATA string Required 

 Scan status message 

 Example: Scan is in Running state 

 400 

 Bad Request 

 application/json 

 403 

 User not Authorized 

 application/json 

 404 

 Run ID not found 

 application/json 

 500 

 Internal Server Error 

 application/json 

 get /public_api/netscan/v1/scan/run/ {id} 

 HTTP 

 Ask Copy 

 GET /public_api/netscan/v1/scan/run/{id}?fields=text HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 User-Agent: text 
 Accept: */* 

 200 

 Scan status retrieved successfully 

 Ask Copy 

 { 
 "DATA": "Scan is in Running state" 
 } 

 Launch a scan run by definition ID 

 post https://api-cortex.paloaltonetworks.com /public_api/netscan/v1/scan/run/ {id} 

 Launch a scan execution using a scan definition specified by the path parameter. Optionally override the target IP addresses for this run. 

 Path parameters 

 id integer · int64 Required 

 Scan definition ID 

 Header parameters 

 User-Agent string Required 

 Body 

 application/json 

 request_data object Required 

 Show properties 

 Responses 

 200 

 Scan launched successfully 

 application/json 

 Response returned after a scan action (launch, pause, resume, or abort) 

 DATA string Required 

 Action result message 

 Example: Scan launched successfully with run ID: 789 

 400 

 Bad Request 

 application/json 

 403 

 User not Authorized 

 application/json 

 404 

 Not found 

 application/json 

 500 

 Internal Server Error 

 application/json 

 post /public_api/netscan/v1/scan/run/ {id} 

 HTTP 

 Ask Copy 

 POST /public_api/netscan/v1/scan/run/{id} HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 User-Agent: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 62 

 { 
 "request_data": { 
 "definition_id": 123, 
 "target": "1.2.3.4.0/12" 
 } 
 } 

 200 

 Scan launched successfully 

 Ask Copy 

 { 
 "DATA": "Scan launched successfully with run ID: 789" 
 } 

 Create a scan definition 

 post https://api-cortex.paloaltonetworks.com /public_api/netscan/v1/scan/definition 

 Create a new scan definition with detailed settings and validation options. A scan definition specifies the targets, schedule, credentials, and scan parameters used when launching scan runs. 

 Header parameters 

 User-Agent string Required 

 Body 

 application/json; charset=UTF-8 

 Scan engine settings controlling port scanning, timeouts, and host discovery behavior 

 port_list_id integer · min: 1 Required 

 Port list ID to use 

 Example: 5 

 scan_ports object[] Required 

 Custom list of ports to scan (overrides port_list_id if provided) 

 auth_port_ssh integer · min: 1 · max: 65535 Optional 

 SSH authentication port 

 Example: 22 

 disable_cgi_cache string · enum Optional 

 Disable CGI cache ( 0 = enabled, 1 = disabled) 

 Example: 1 Possible values : 0 1 

 plugins_timeout integer · min: 1 Optional 

 Plugin timeout in minutes 

 Example: 5 

 checks_read_timeout integer · min: 1 Optional 

 Checks read timeout in minutes 

 Example: 5 

 max_hosts integer · min: 1 Optional 

 Maximum number of hosts to scan simultaneously 

 Example: 30 

 max_checks integer · min: 1 Optional 

 Maximum number of checks per host 

 Example: 4 

 scanner_plugins_timeout integer · min: 1 Optional 

 Scanner plugins timeout in seconds 

 Example: 3600 

 timeout_retry integer Optional 

 Number of timeout retries 

 Example: 5 

 open_sock_max_attempts integer · min: 1 Optional 

 Maximum attempts to open socket 

 Example: 5 

 non_simult_ports string Optional 

 Ports that should not be scanned simultaneously (comma-separated) 

 Example: 139,445,3389,Services/irc 

 strict_unauthenticated string · enum Optional 

 Strict unauthenticated mode ( 0 = disabled, 1 = enabled) 

 Example: 0 Possible values : 0 1 

 optimize_test string · enum Optional 

 Optimize test execution ( 0 = disabled, 1 = enabled) 

 Example: 1 Possible values : 0 1 

 expand_vhosts string · enum Optional 

 Expand virtual hosts ( 0 = disabled, 1 = enabled) 

 Example: 1 Possible values : 0 1 

 exclude_fragile_devices string · enum Optional 

 Exclude fragile devices ( 0 = disabled, 1 = enabled) 

 Example: 1 Possible values : 0 1 

 exclude_printers string · enum Optional 

 Exclude printers ( 0 = disabled, 1 = enabled) 

 Example: 1 Possible values : 0 1 

 safe_checks string · enum Optional 

 Enable safe checks ( 0 = disabled, 1 = enabled) 

 Example: 1 Possible values : 0 1 

 disable_win_cmd_exec string · enum Optional 

 Disable Windows command execution ( 0 = disabled, 1 = enabled) 

 Example: 1 Possible values : 0 1 

 disable_wmi_search string · enum Optional 

 Disable WMI search ( 0 = disabled, 1 = enabled) 

 Example: 1 Possible values : 0 1 

 alive_test_methods string · enum[] Optional 

 Methods to test if hosts are alive 

 Example: ["arp","icmp","tcp_ack"] 

 Show properties 

 alive_test_ports string Optional 

 Ports to use for alive testing (comma-separated or ranges) 

 Example: 21-23,25,53,80,110-111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080 

 definition_id integer Optional 

 ID of existing definition (for updates) 

 Example: 123 

 vt_config_id integer · min: 1 Required 

 Vulnerability test configuration template ID 

 Example: 4 

 name string · min: 1 · max: 100 Required 

 Name of the scan definition 

 Example: Weekly Production Scan 

 description string · max: 500 Required 

 Description of the scan definition 

 Example: Weekly security scan for production servers 

 network_scanner_ids string · uuid[] · min: 1 Required 

 Array of network scanner UUIDs to use for this scan 

 Example: ["scanner-1","scanner-2"] 

 network integer · min: 1 Required 

 Network ID 

 Example: 1 

 credential_ids integer[] Required 

 Array of credential IDs for authenticated scanning 

 Example: [1] 

 schedule_cadence string · enum Required 

 Schedule cadence frequency 

 Example: DAILY Possible values : DAILY WEEKLY MONTHLY ONCE 

 schedule_days integer · max: 127 Required 

 Scheduled days as bitmask (127 = all days) 

 Example: 127 

 schedule_dates integer[] Required 

 Array of scheduled dates (for monthly cadence) 

 schedule_start_date integer · int64 Required 

 Schedule start date as Unix timestamp in milliseconds 

 Example: 1765083183326 

 schedule_time object · ScanTime Required 

 Time of day specification for scan scheduling 

 Show properties 

 schedule_quiet_hours object[] Required 

 Array of quiet hours periods when scanning should not run 

 Show properties 

 schedule_timezone string Required 

 Timezone for scheduling (IANA timezone format) 

 Example: America/Los_Angeles 

 override_target_exclusions boolean Required 

 Whether to override global target exclusions 

 Example: false 

 target_ids integer[] Required 

 Array of target group IDs 

 targets string[] Required 

 Array of target hosts or IP ranges (CIDR notation) 

 Example: ["192.168.1.0/24","10.0.0.1-10.0.0.100"] 

 excluded_targets string[] Required 

 Array of excluded targets 

 Example: [""] 

 enable_report boolean Required 

 Whether to enable scan reporting 

 Example: true 

 asset_groups object · AssetGroup[] Optional 

 Show properties 

 Responses 

 201 

 New scan definition created successfully. 

 application/json 

 definition_id integer Optional 

 ID of the created definition 

 Example: 123 

 message string Optional 

 Success message 

 Example: Scan created successfully 

 400 

 Bad Request 

 application/json 

 403 

 User not Authorized 

 application/json 

 404 

 VT template not found or cannot create a new scan definition 

 application/json 

 422 

 Failed definition validation during scan definition creation. 

 application/json 

 500 

 Internal Server Error 

 application/json 

 post /public_api/netscan/v1/scan/definition 

 HTTP 

 Ask Copy 

 POST /public_api/netscan/v1/scan/definition HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 User-Agent: text 
 Content-Type: application/json; charset=UTF-8 
 Accept: */* 
 Content-Length: 1236 

 { 
 "port_list_id": 5, 
 "scan_ports": [], 
 "auth_port_ssh": 22, 
 "disable_cgi_cache": "1", 
 "plugins_timeout": 5, 
 "checks_read_timeout": 5, 
 "max_hosts": 30, 
 "max_checks": 4, 
 "scanner_plugins_timeout": 3600, 
 "timeout_retry": 5, 
 "open_sock_max_attempts": 5, 
 "non_simult_ports": "139,445,3389,Services/irc", 
 "strict_unauthenticated": "0", 
 "optimize_test": "1", 
 "expand_vhosts": "1", 
 "exclude_fragile_devices": "1", 
 "exclude_printers": "1", 
 "safe_checks": "1", 
 "disable_win_cmd_exec": "1", 
 "disable_wmi_search": "1", 
 "alive_test_methods": [ 
 "arp", 
 "icmp", 
 "tcp_ack" 
 ], 
 "alive_test_ports": "21-23,25,53,80,110-111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080", 
 "definition_id": 123, 
 "vt_config_id": 4, 
 "name": "Weekly Production Scan", 
 "description": "Weekly security scan for production servers", 
 "network_scanner_ids": [ 
 "scanner-1", 
 "scanner-2" 
 ], 
 "network": 1, 
 "credential_ids": [ 
 1 
 ], 
 "schedule_cadence": "DAILY", 
 "schedule_days": 127, 
 "schedule_dates": [], 
 "schedule_start_date": 1765083183326, 
 "schedule_time": { 
 "hour": 2, 
 "minute": 0, 
 "second": 0 
 }, 
 "schedule_quiet_hours": [], 
 "schedule_timezone": "America/Los_Angeles", 
 "override_target_exclusions": false, 
 "target_ids": [], 
 "targets": [ 
 "192.168.1.0/24", 
 "10.0.0.1-10.0.0.100" 
 ], 
 "excluded_targets": [ 
 "" 
 ], 
 "enable_report": true, 
 "asset_groups": [ 
 { 
 "id": 1, 
 "name": "text", 
 "count": 1 
 } 
 ] 
 } 

 201 

 New scan definition created successfully. 

 Ask Copy 

 { 
 "definition_id": 123, 
 "message": "Scan created successfully" 
 } 

 Send a command to a running scan 

 post https://api-cortex.paloaltonetworks.com /public_api/netscan/v1/scan/run/ {id} /command 

 Send a control command to a running scan execution. Supported commands are ABORT (cancel the scan), PAUSE (pause the scan), and RESUME (resume a paused scan). 

 Path parameters 

 id integer · int64 Required 

 Unique identifier of the scan run 

 Header parameters 

 User-Agent string Required 

 Body 

 application/json 

 request_data object Required 

 Show properties 

 Responses 

 200 

 Command executed successfully 

 application/json 

 Response returned after a scan action (launch, pause, resume, or abort) 

 DATA string Required 

 Action result message 

 Example: Scan launched successfully with run ID: 789 

 400 

 Bad Request 

 application/json 

 403 

 User not Authorized 

 application/json 

 404 

 Run ID not found or command cannot be performed 

 application/json 

 500 

 Internal Server Error 

 application/json 

 post /public_api/netscan/v1/scan/run/ {id} /command 

 HTTP 

 Ask Copy 

 POST /public_api/netscan/v1/scan/run/{id}/command HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 User-Agent: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 33 

 { 
 "request_data": { 
 "type": "ABORT" 
 } 
 } 

 200 

 Command executed successfully 

 Ask Copy 

 { 
 "DATA": "Scan launched successfully with run ID: 789" 
 } 

 Previous Netscan overview 

 Next Models 

 Last updated 1 month ago 

 Was this helpful?
