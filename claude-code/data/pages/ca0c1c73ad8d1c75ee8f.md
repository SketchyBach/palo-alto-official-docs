---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/common-logs/common-system-log/common-system-syslog-fields
fetched_at: 2026-08-13T17:40:05Z
source: palo-alto-main
---

# System Syslog Default Field Order Clear

System Syslog Default Field Order 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 System Syslog Default Field Order 

 Updated on 

 Fri Jul 03 02:04:39 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Logging Service Docs 

 Activation & Onboarding 

 Administration 

 Release Notes 

 Log Reference 

 New Features 

 Updated on 

 Fri Jul 03 02:04:39 PDT 2026 

 Focus 

 Home 

 Strata Logging Service 

 Strata Logging Service Log Reference 

 Common Logs 

 System 

 System Syslog Default Field Order 

 Download PDF 

 Strata Logging Service 

 System Syslog Default Field Order 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Logging Service Docs 

 Activation & Onboarding 

 Administration 

 Release Notes 

 Log Reference 

 New Features 

 Previous 

 System 

 Next 

 System CEF Fields 

 System Syslog Default Field Order 

 Example System log in Syslog:

 Oct 13 01:17:01 xxx.xx.x.xx 344 <142>1 2020-10-13T01:17:01.322Z stream-logfwd20-156653024-10121421-eq28-harness-16kn logforwarder - panwlogs - 1,​2020-10-13T01:16:46.000000Z,​007051000113358,​SYSTEM,​general,​,​2020-10-13T01:16:26.000000Z,​vsys1,​unknown,​,​,​0,​,​Informational,​EDL(red_edl) No changes to list file,​160444,​-9223372036854775808,​0,​0,​0,​0,​,​PA-VM,​,​,​2020-10-13T01:16:26.000000Z 

 The following identifies the default field order for filters 

 migrated from an earlier version of the log forwarding application. 

 For log filters created after that migration, you specify the field order when you

 create a log filter 

 by specifying the columns you want to receive.

 The fields are identified in the default order that they appear in each log
 line.

 HEADER, log_time , log_source_id , log_type.​value , sub_type.​value , config_version.​value , event_time , vsys , event_name.​value , event_component , EMPTY, event_component_id, EMPTY, vendor_severity.​value , event_description , sequence_no , action_flags, dg_hier_level_1 , dg_hier_level_2 , dg_hier_level_3 , dg_hier_level_4 , vsys_name , log_source_name , device_group.​value , template.​value , time_generated_high_res 

 Previous 

 System 

 Next 

 System CEF Fields 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Identity and Access Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Security Operations 

 Log Reference 

 Strata Logging Service 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
