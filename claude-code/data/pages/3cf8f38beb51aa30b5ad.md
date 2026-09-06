---
url: https://cortex-docs.paloaltonetworks.com/xdr-5-api/broker-vm-tenant-side/broker-papi-tables
fetched_at: 2026-09-06T10:55:16Z
source: cortex-platform
---

# Additional References | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XDR 

 XDR 5.x APIs 

 Broker VM (Tenant-Side) 

 Additional References 

 Action Statuses 

 Used by Get Action Status endpoint to describe the possible statuses for a Broker VM action. 

 Status 

 Meaning 

 SUBMITTED 

 Accepted by the tenant; not yet delivered to the broker. 

 IN_PROGRESS 

 Delivered to the broker, being applied. 

 COMPLETED 

 Successfully applied. 

 UP_TO_DATE 

 No-op; broker was already in the requested state. 

 FAILED 

 Could not be applied; inspect broker status for details. 

 NOT_AVAILABLE 

 Action ID unknown or expired from the actions table. 

 Broker Applet Configuration Schemas 

 Used by the Applet Configuration endpoints to list the supported applets and their corresponding configuration schemas. 

 applet_name 

 Purpose 

 Request schema 

 GET response schema 

 syslog 

 Syslog ingestion (UDP/TCP/secure_TCP) 

 SyslogConfig 

 SyslogGetConfigResponse 

 kafka 

 Kafka topic ingestion 

 KafkaConfig 

 KafkaGetConfigResponse 

 db 

 Database query ingestion 

 DbCollectorConfig 

 DbCollectorGetConfigResponse 

 ftp 

 FTP / SFTP / FTPS file collection 

 FtpConfig 

 FtpGetConfigResponse 

 file 

 Generic shared-folder log collection 

 FileConfig 

 FileGetConfigResponse 

 csv 

 CSV-specific shared-folder collection 

 CsvConfig 

 CsvGetConfigResponse 

 wec 

 Windows Event Collector 

 WecConfig 

 WecGetConfigResponse 

 netflow 

 Netflow data sources (UDP per-port) 

 NetflowConfig 

 NetflowGetConfigResponse 

 network_mapper 

 Network mapping / port scanning 

 NetworkMapperConfig 

 NetworkMapperGetConfigResponse 

 local_agent_settings 

 Local agent proxy + content caching 

 LocalAgentSettingsConfig 

 LocalAgentSettingsGetConfigResponse 

 Broker Log Bundle Status Codes 

 Used by the Get Log Bundle Status endpoint to explain the status codes returned when requesting a log bundle from a Broker VM. 

 code 

 Meaning 

 LogRequestInProgress 

 Request submitted or pulled by the broker; not yet completed. 

 LogRequestSucceeded 

 Bundle ready for download. 

 LogRequestTimedout 

 Broker did not produce the bundle in time. 

 LogBundleCollectionInVMFailed 

 The broker reported a failure during collection, or no usable request row exists (error / never requested / already GC'd). 

 Previous Models 

 Next Cases APIs overview 

 Last updated 21 days ago 

 Was this helpful?
