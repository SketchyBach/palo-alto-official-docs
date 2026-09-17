---
url: https://cortex-docs.paloaltonetworks.com/xsiam-api/broker-vm-tenant-side/applets
fetched_at: 2026-09-16T09:04:01Z
source: cortex-platform
---

# Applets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSIAM 

 XSIAM APIs 

 Broker VM (Tenant-Side) 

 Applets 

 Configure, (de)activate, and inspect the applets that run on a broker. The same five generic endpoints ( get / config / activate / deactivate / scan_now -or-cert) are reused for every applet, with the request and response body shape determined by the applet_name path parameter. 

 See the Broker Applet Configuration Schemas table. 

 Operations that exist only for one applet are also surfaced in this tag for navigation convenience ( downloadWefCert for wec , networkMapperScanNow for network_mapper ). 

 Get an applet's configuration and status 

 get https://api-cortex.paloaltonetworks.com /public_api/v1/brokers/ {device_id} /applets/ {applet_name} / 

 Return the current configuration and runtime state of a single applet on a single broker. The response shape is determined by applet_name — see the oneOf under 200.content.schema . 

 Required permission: Data Broker > Broker Service > View/Edit. 

 400 Bad Request — applet_name is not one of the supported applets. 

 404 Not Found — broker is unknown. 

 409 Conflict — broker is disconnected. 

 Authorizations 

 XDRAuth & XDRAuthToken 

 Authorization string Required 

 The tenant API key value, sent as the literal Authorization 
header value (no Bearer prefix). 

 x-xdr-auth-id string Required 

 The tenant API key identifier corresponding to the value sent in
 Authorization . 

 Path parameters 

 device_id string · min: 1 Required 

 The broker device identifier as returned by getBrokers . 

 Example: 6f3a8c7e-1a9b-4c0d-9e21-7f5d3b1c8a02 

 applet_name string · enum Required 

 Closed set of supported PAPI applet identifiers. Each applet has
its own request and response schema, keyed by this value. 

 Possible values : syslog kafka db ftp file csv wec netflow network_mapper local_agent_settings 

 Responses 

 200 

 Applet configuration + status. The schema variant is
selected by the applet discriminator field, which always
equals the path's applet_name . 

 application/json 

 object · SyslogGetConfigResponse Optional 

 GET-config response for the syslog applet. Cert payloads
( server_cert , private_key , ca_cert ) are write-only and are
intentionally omitted; min_tls_ver is echoed for secure_TCP 
entries so a GET → unmodified PUT round-trip preserves the
stored TLS floor. 

 Show properties 

 or 

 object · KafkaGetConfigResponse Optional 

 GET-config response for the kafka applet. password and
 private_key are write-only and are omitted from the response. 

 Show properties 

 or 

 object · DbCollectorGetConfigResponse Optional 

 GET-config response for the db applet. password is write-only
and is omitted from the response. 

 Show properties 

 or 

 object · FtpGetConfigResponse Optional 

 GET-config response for the ftp applet. The password and private_key on each connection are omitted (write-only). 

 Show properties 

 or 

 object · FileGetConfigResponse Optional 

 GET-config response for the file applet. The password on each shared-folder connection is omitted (write-only). 

 Show properties 

 or 

 object · CsvGetConfigResponse Optional 

 GET-config response for the csv applet. The password field on each mounter is omitted (write-only). 

 Show properties 

 or 

 object · WecGetConfigResponse Optional 

 GET-config response for the wec applet. The subscription_manager_url is null until WEC certificate material has been generated on the broker. 

 Show properties 

 or 

 object · NetflowGetConfigResponse Optional 

 GET-config response for the netflow applet. 

 Show properties 

 or 

 object · NetworkMapperGetConfigResponse Optional 

 GET-config response for the network_mapper applet. The scheduler
 method is rendered in the user-friendly form
( Run daily / Run weekly / Run monthly ). 

 Show properties 

 or 

 object · LocalAgentSettingsGetConfigResponse Optional 

 GET-config response for the local_agent_settings applet. 

 Show properties 

 400 

 Request validation failed. errors is present when the failure
originates from Pydantic schema validation; otherwise only
 description is populated. 

 application/json 

 401 

 Missing or invalid Authorization / x-xdr-auth-id credentials. 

 application/json 

 403 

 Authenticated caller lacks the Data Broker > Broker Service > View/Edit permission, or the
targeted broker is a cluster member and the operation is rejected
at that level. 

 application/json 

 404 

 The targeted resource does not exist. 

 application/json 

 409 

 The action cannot proceed in the current state — most commonly,
the broker is disconnected, or an applet is not in the required
active/inactive state. 

 application/json 

 500 

 Unexpected server-side failure. 

 application/json 

 get /public_api/v1/brokers/ {device_id} /applets/ {applet_name} / 

 HTTP 

 Ask Copy 

 GET /public_api/v1/brokers/{device_id}/applets/{applet_name}/ HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 Authorization: YOUR_API_KEY 
 x-xdr-auth-id: YOUR_API_KEY 
 Accept: */* 

 200 

 Applet configuration + status. The schema variant is
selected by the applet discriminator field, which always
equals the path's applet_name . 

 Ask Copy 

 { 
 "device_id": "text", 
 "applet": "syslog", 
 "syslog_data_sources": [ 
 { 
 "protocol": "udp", 
 "port": "text", 
 "network_settings": [ 
 { 
 "source_network": "Any", 
 "format": "auto", 
 "vendor": "auto", 
 "product": "auto" 
 } 
 ], 
 "min_tls_ver": "1.0" 
 } 
 ] 
 } 

 Edit an applet's configuration 

 post https://api-cortex.paloaltonetworks.com /public_api/v1/brokers/ {device_id} /applets/ {applet_name} /config/ 

 Replace the configuration of an already-active applet on a broker. The request body shape is determined by applet_name — see the oneOf under requestBody.content.schema . 

 The endpoint is destructive : the new configuration replaces the prior one in full. Use getApplet first to fetch the current shape, mutate it locally, then submit. Sensitive fields such as passwords / SSH keys / private keys are returned masked or omitted by getApplet , so partial edits work as long as you either re-supply the secret or leave the masked sentinel verbatim. 

 Required permission: Data Broker > Broker Service > View/Edit. 

 400 Bad Request — applet_name is not one of the supported applets, or the body fails Pydantic validation for the targeted applet's schema. 

 404 Not Found — broker is unknown. 

 409 Conflict — broker is disconnected, or applet is not currently active (use activate instead). 

 Authorizations 

 XDRAuth & XDRAuthToken 

 Authorization string Required 

 The tenant API key value, sent as the literal Authorization 
header value (no Bearer prefix). 

 x-xdr-auth-id string Required 

 The tenant API key identifier corresponding to the value sent in
 Authorization . 

 Path parameters 

 device_id string · min: 1 Required 

 The broker device identifier as returned by getBrokers . 

 Example: 6f3a8c7e-1a9b-4c0d-9e21-7f5d3b1c8a02 

 applet_name string · enum Required 

 Closed set of supported PAPI applet identifiers. Each applet has
its own request and response schema, keyed by this value. 

 Possible values : syslog kafka db ftp file csv wec netflow network_mapper local_agent_settings 

 Body 

 application/json 

 object · SyslogConfig Optional 

 Request body for the syslog applet. Every
 (protocol, port) pair must be unique across
 syslog_data_sources . 

 Show properties 

 or 

 object · KafkaConfig Optional 

 Request body for the kafka applet — wraps a non-empty list of Kafka server connections. 

 Show properties 

 or 

 object · DbCollectorConfig Optional 

 Request body for the db applet — wraps a non-empty list of database server entries ( database_connection ). 

 Show properties 

 or 

 object · FtpConfig Optional 

 Request body for the ftp applet — wraps a non-empty list of FTP / SFTP / FTPS server connections. 

 Show properties 

 or 

 object · FileConfig Optional 

 Request body for the file (generic shared-folder Log Collector) applet — wraps a non-empty list of shared-folder connections. 

 Show properties 

 or 

 object · CsvConfig Optional 

 Request body for the csv applet — wraps csv_parameters (mounter folders + monitored CSV files). 

 Show properties 

 or 

 object · WecConfig Optional 

 Request body for the wec (Windows Event Collector) applet — wraps the TLS floor and the non-empty list of collected event subscriptions. 

 Show properties 

 or 

 object · NetflowConfig Optional 

 UDP_port values must be unique across netflow_data_sources . 

 Show properties 

 or 

 object · NetworkMapperConfig Optional 

 Request body for the network_mapper applet — wraps the single scanner configuration block. 

 Show properties 

 or 

 object · LocalAgentSettingsConfig Optional 

 At least one of proxy.enabled or caching must be true ,
otherwise the activation request is rejected. 

 Show properties 

 Responses 

 200 

 Edit accepted. The configuration is applied asynchronously —
the body is an acknowledgement { "status": "activating" } , not
the applied config. Poll getApplet (or
 getBrokers ) to observe the config once
it has been applied. 

 application/json 

 Async acknowledgement payload, e.g.
 { "status": "activating" } . 

 Other properties any Optional 

 400 

 Request validation failed. errors is present when the failure
originates from Pydantic schema validation; otherwise only
 description is populated. 

 application/json 

 401 

 Missing or invalid Authorization / x-xdr-auth-id credentials. 

 application/json 

 403 

 Authenticated caller lacks the Data Broker > Broker Service > View/Edit permission, or the
targeted broker is a cluster member and the operation is rejected
at that level. 

 application/json 

 404 

 The targeted resource does not exist. 

 application/json 

 409 

 The action cannot proceed in the current state — most commonly,
the broker is disconnected, or an applet is not in the required
active/inactive state. 

 application/json 

 500 

 Unexpected server-side failure. 

 application/json 

 post /public_api/v1/brokers/ {device_id} /applets/ {applet_name} /config/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/brokers/{device_id}/applets/{applet_name}/config/ HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 Authorization: YOUR_API_KEY 
 x-xdr-auth-id: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 235 

 { 
 "syslog_data_sources": [ 
 { 
 "protocol": "udp", 
 "port": "514", 
 "network_settings": [ 
 { 
 "source_network": "Any", 
 "format": "auto", 
 "vendor": "auto", 
 "product": "auto" 
 } 
 ], 
 "server_cert": "text", 
 "private_key": "password", 
 "ca_cert": "text", 
 "min_tls_ver": "1.0" 
 } 
 ] 
 } 

 200 

 Edit accepted. The configuration is applied asynchronously —
the body is an acknowledgement { "status": "activating" } , not
the applied config. Poll getApplet (or
 getBrokers ) to observe the config once
it has been applied. 

 Ask Copy 

 { 
 "status": "activating" 
 } 

 Activate an applet with a configuration 

 post https://api-cortex.paloaltonetworks.com /public_api/v1/brokers/ {device_id} /applets/ {applet_name} /activate/ 

 Activate an applet on a broker, supplying its configuration in the same body shape that editApplet accepts. If the applet is already active, the call is rejected with 409 (use editApplet instead). 

 Required permission: Data Broker > Broker Service > View/Edit. 

 400 Bad Request — invalid applet_name or schema validation failure. 

 404 Not Found — broker is unknown. 

 409 Conflict — broker is disconnected, or applet is already active. 

 Authorizations 

 XDRAuth & XDRAuthToken 

 Authorization string Required 

 The tenant API key value, sent as the literal Authorization 
header value (no Bearer prefix). 

 x-xdr-auth-id string Required 

 The tenant API key identifier corresponding to the value sent in
 Authorization . 

 Path parameters 

 device_id string · min: 1 Required 

 The broker device identifier as returned by getBrokers . 

 Example: 6f3a8c7e-1a9b-4c0d-9e21-7f5d3b1c8a02 

 applet_name string · enum Required 

 Closed set of supported PAPI applet identifiers. Each applet has
its own request and response schema, keyed by this value. 

 Possible values : syslog kafka db ftp file csv wec netflow network_mapper local_agent_settings 

 Body 

 application/json 

 object · SyslogConfig Optional 

 Request body for the syslog applet. Every
 (protocol, port) pair must be unique across
 syslog_data_sources . 

 Show properties 

 or 

 object · KafkaConfig Optional 

 Request body for the kafka applet — wraps a non-empty list of Kafka server connections. 

 Show properties 

 or 

 object · DbCollectorConfig Optional 

 Request body for the db applet — wraps a non-empty list of database server entries ( database_connection ). 

 Show properties 

 or 

 object · FtpConfig Optional 

 Request body for the ftp applet — wraps a non-empty list of FTP / SFTP / FTPS server connections. 

 Show properties 

 or 

 object · FileConfig Optional 

 Request body for the file (generic shared-folder Log Collector) applet — wraps a non-empty list of shared-folder connections. 

 Show properties 

 or 

 object · CsvConfig Optional 

 Request body for the csv applet — wraps csv_parameters (mounter folders + monitored CSV files). 

 Show properties 

 or 

 object · WecConfig Optional 

 Request body for the wec (Windows Event Collector) applet — wraps the TLS floor and the non-empty list of collected event subscriptions. 

 Show properties 

 or 

 object · NetflowConfig Optional 

 UDP_port values must be unique across netflow_data_sources . 

 Show properties 

 or 

 object · NetworkMapperConfig Optional 

 Request body for the network_mapper applet — wraps the single scanner configuration block. 

 Show properties 

 or 

 object · LocalAgentSettingsConfig Optional 

 At least one of proxy.enabled or caching must be true ,
otherwise the activation request is rejected. 

 Show properties 

 Responses 

 200 

 Applet activation accepted. 

 application/json 

 Handler-specific acknowledgement payload. 

 Other properties any Optional 

 400 

 Request validation failed. errors is present when the failure
originates from Pydantic schema validation; otherwise only
 description is populated. 

 application/json 

 401 

 Missing or invalid Authorization / x-xdr-auth-id credentials. 

 application/json 

 403 

 Authenticated caller lacks the Data Broker > Broker Service > View/Edit permission, or the
targeted broker is a cluster member and the operation is rejected
at that level. 

 application/json 

 404 

 The targeted resource does not exist. 

 application/json 

 409 

 The action cannot proceed in the current state — most commonly,
the broker is disconnected, or an applet is not in the required
active/inactive state. 

 application/json 

 500 

 Unexpected server-side failure. 

 application/json 

 post /public_api/v1/brokers/ {device_id} /applets/ {applet_name} /activate/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/brokers/{device_id}/applets/{applet_name}/activate/ HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 Authorization: YOUR_API_KEY 
 x-xdr-auth-id: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 235 

 { 
 "syslog_data_sources": [ 
 { 
 "protocol": "udp", 
 "port": "514", 
 "network_settings": [ 
 { 
 "source_network": "Any", 
 "format": "auto", 
 "vendor": "auto", 
 "product": "auto" 
 } 
 ], 
 "server_cert": "text", 
 "private_key": "password", 
 "ca_cert": "text", 
 "min_tls_ver": "1.0" 
 } 
 ] 
 } 

 200 

 Applet activation accepted. 

 Ask Copy 

 { 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Deactivate an applet 

 post https://api-cortex.paloaltonetworks.com /public_api/v1/brokers/ {device_id} /applets/ {applet_name} /deactivate/ 

 Deactivate a currently-active applet on a broker. The optional request body carries save_config=true|false to control whether the broker retains the prior applet config (so a subsequent activate without a body restores it). Default is true . 

 Required permission: Data Broker > Broker Service > View/Edit. 

 400 Bad Request — invalid applet_name . 

 404 Not Found — broker is unknown. 

 409 Conflict — broker is disconnected, or applet is not active. 

 Authorizations 

 XDRAuth & XDRAuthToken 

 Authorization string Required 

 The tenant API key value, sent as the literal Authorization 
header value (no Bearer prefix). 

 x-xdr-auth-id string Required 

 The tenant API key identifier corresponding to the value sent in
 Authorization . 

 Path parameters 

 device_id string · min: 1 Required 

 The broker device identifier as returned by getBrokers . 

 Example: 6f3a8c7e-1a9b-4c0d-9e21-7f5d3b1c8a02 

 applet_name string · enum Required 

 Closed set of supported PAPI applet identifiers. Each applet has
its own request and response schema, keyed by this value. 

 Possible values : syslog kafka db ftp file csv wec netflow network_mapper local_agent_settings 

 Body 

 application/json 

 Optional body for deactivateApplet .
The body itself is optional; when absent or save_config is
omitted, the broker preserves the applet's prior configuration so
a later activate without a body restores it. 

 save_config boolean Optional 

 true (default) — preserve the applet's current configuration
for later reactivation. false — drop the configuration; a
subsequent activate requires a full body. 

 Default: true 

 Responses 

 200 

 Applet deactivation accepted. 

 application/json 

 Handler-specific acknowledgement payload. 

 Other properties any Optional 

 400 

 Request validation failed. errors is present when the failure
originates from Pydantic schema validation; otherwise only
 description is populated. 

 application/json 

 401 

 Missing or invalid Authorization / x-xdr-auth-id credentials. 

 application/json 

 403 

 Authenticated caller lacks the Data Broker > Broker Service > View/Edit permission, or the
targeted broker is a cluster member and the operation is rejected
at that level. 

 application/json 

 404 

 The targeted resource does not exist. 

 application/json 

 409 

 The action cannot proceed in the current state — most commonly,
the broker is disconnected, or an applet is not in the required
active/inactive state. 

 application/json 

 500 

 Unexpected server-side failure. 

 application/json 

 post /public_api/v1/brokers/ {device_id} /applets/ {applet_name} /deactivate/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/brokers/{device_id}/applets/{applet_name}/deactivate/ HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 Authorization: YOUR_API_KEY 
 x-xdr-auth-id: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 20 

 { 
 "save_config": true 
 } 

 200 

 Applet deactivation accepted. 

 Ask Copy 

 { 
 "ANY_ADDITIONAL_PROPERTY": "anything" 
 } 

 Download the WEC/WEF client certificate as a PFX archive 

 post https://api-cortex.paloaltonetworks.com /public_api/v1/brokers/ {device_id} /applets/wec/wef_cert/ 

 Issue and stream the WEF (Windows Event Forwarder) client certificate for a broker as a PFX archive, encrypted with the export password the caller supplies in the request body. The PFX is intended to be installed on the Windows hosts that will forward events to the broker's WEC subscription manager. 

 Required permission: Data Broker > Broker Service > View/Edit. 

 400 Bad Request — password is shorter than 5 characters. 

 404 Not Found — broker is unknown. 

 409 Conflict — WEC applet is not active on the broker, or the stored certificate material was generated on a Broker VM version that does not support the export shape this endpoint uses. 

 Authorizations 

 XDRAuth & XDRAuthToken 

 Authorization string Required 

 The tenant API key value, sent as the literal Authorization 
header value (no Bearer prefix). 

 x-xdr-auth-id string Required 

 The tenant API key identifier corresponding to the value sent in
 Authorization . 

 Path parameters 

 device_id string · min: 1 Required 

 The broker device identifier as returned by getBrokers . 

 Example: 6f3a8c7e-1a9b-4c0d-9e21-7f5d3b1c8a02 

 Body 

 application/json 

 Body for downloadWefCert . The password (min 5 chars) is the PFX export password. 

 password string · password · min: 5 Required 

 Export password applied to the PFX archive returned to the
caller. The password protects the embedded private key on the
wire; the customer-facing minimum length is 5 characters. 

 Responses 

 200 

 PFX archive containing the WEF client certificate. 

 application/octet-stream 

 Headers object 

 Show Header 

 Response string · binary 

 Raw bytes of the PFX archive. 

 400 

 Request validation failed. errors is present when the failure
originates from Pydantic schema validation; otherwise only
 description is populated. 

 application/json 

 401 

 Missing or invalid Authorization / x-xdr-auth-id credentials. 

 application/json 

 403 

 Authenticated caller lacks the Data Broker > Broker Service > View/Edit permission, or the
targeted broker is a cluster member and the operation is rejected
at that level. 

 application/json 

 404 

 The targeted resource does not exist. 

 application/json 

 409 

 The action cannot proceed in the current state — most commonly,
the broker is disconnected, or an applet is not in the required
active/inactive state. 

 application/json 

 500 

 Unexpected server-side failure. 

 application/json 

 post /public_api/v1/brokers/ {device_id} /applets/wec/wef_cert/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/brokers/{device_id}/applets/wec/wef_cert/ HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 Authorization: YOUR_API_KEY 
 x-xdr-auth-id: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 36 

 { 
 "password": "<pfx-export-password>" 
 } 

 200 

 PFX archive containing the WEF client certificate. 

 Ask Copy 

 binary 

 Trigger an immediate Network Mapper scan 

 post https://api-cortex.paloaltonetworks.com /public_api/v1/brokers/ {device_id} /applets/network_mapper/scan_now/ 

 Bypass the configured scanning schedule and trigger an immediate scan from the broker's Network Mapper applet. The request has no body; the action is enqueued and acknowledged synchronously. 

 Required permission: Data Broker > Broker Service > View/Edit. 

 404 Not Found — broker is unknown. 

 409 Conflict — broker is disconnected, or the network_mapper applet is not currently active. 

 Authorizations 

 XDRAuth & XDRAuthToken 

 Authorization string Required 

 The tenant API key value, sent as the literal Authorization 
header value (no Bearer prefix). 

 x-xdr-auth-id string Required 

 The tenant API key identifier corresponding to the value sent in
 Authorization . 

 Path parameters 

 device_id string · min: 1 Required 

 The broker device identifier as returned by getBrokers . 

 Example: 6f3a8c7e-1a9b-4c0d-9e21-7f5d3b1c8a02 

 Responses 

 200 

 Action accepted; no response body content. 

 application/json 

 object Optional 

 Empty object on success. 

 401 

 Missing or invalid Authorization / x-xdr-auth-id credentials. 

 application/json 

 403 

 Authenticated caller lacks the Data Broker > Broker Service > View/Edit permission, or the
targeted broker is a cluster member and the operation is rejected
at that level. 

 application/json 

 404 

 The targeted resource does not exist. 

 application/json 

 409 

 The action cannot proceed in the current state — most commonly,
the broker is disconnected, or an applet is not in the required
active/inactive state. 

 application/json 

 500 

 Unexpected server-side failure. 

 application/json 

 post /public_api/v1/brokers/ {device_id} /applets/network_mapper/scan_now/ 

 HTTP 

 Ask Copy 

 POST /public_api/v1/brokers/{device_id}/applets/network_mapper/scan_now/ HTTP/1.1 
 Host: api-cortex.paloaltonetworks.com 
 Authorization: YOUR_API_KEY 
 x-xdr-auth-id: YOUR_API_KEY 
 Accept: */* 

 200 

 Action accepted; no response body content. 

 Ask Copy 

 {} 

 Previous Install images 

 Next Remote log bundle 

 Last updated 20 hours ago 

 Was this helpful?
