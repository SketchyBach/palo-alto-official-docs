---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-auth-log/network-auth-syslog-fields
fetched_at: 2026-08-13T17:40:18Z
source: palo-alto-main
---

# Authentication Syslog Default Field Order Clear

Authentication Syslog Default Field Order 

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

 Authentication Syslog Default Field Order 

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

 Network Logs 

 Authentication 

 Authentication Syslog Default Field Order 

 Download PDF 

 Strata Logging Service 

 Authentication Syslog Default Field Order 

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

 Authentication 

 Next 

 Authentication CEF Fields 

 Authentication Syslog Default Field Order 

 Example Authentication log in Syslog:

 Oct 13 01:21:17 gke-standard-cluster-2-pool-1-6ea9f13a-moqf 894 <142>1 2020-10-13T01:21:16.976Z stream-logfwd20-156653024-10121421-eq28-harness-16kn logforwarder - panwlogs - 1,​2020-10-13T01:21:10.000000Z,​007051000113358,​AUTH,​Unknown,​10.0,​2020-10-13T01:21:01.000000Z,​vsys1,​::11e:a8c0:ffff:0,​paloaltonetwork\xxxxx,​paloaltonetwork\xxxxx,​Authentication object4,​Captive Portal,​16777216,​-1295066367845728256,​xxxxx,​rs-logging,​deny-attackers,​www.test.com,​1,​user password failure,​3,​556392,​-9223372036854775808,​0,​0,​0,​0,​,​PA-VM,​1,​0,​,​2020-10-13T01:21:02.391000Z,​src_category_list-2,​src_profile_list-0,​src_model_list-2,​src_vendor_list-2,​src_osfamily_list-2,​src_osversion_list-2,​src_host_list-2,​src_mac_list-0 

 The following identifies the default field order for filters 

 migrated from an earlier version of the log forwarding application. 

 For log filters created after that migration, you specify the field order when you

 create a log filter 

 by specifying the columns you want to receive.

 The fields are identified in the default order that they appear in each log
 line.

 HEADER, log_time , log_source_id , log_type.​value , sub_type.​value , config_version.​value , time_generated , vsys , source_ip.​value , user , normalize_user , object , auth_policy , count_of_repeats , mfa_auth_id , mfa_vendor , log_set , auth_server_profile , auth_description , client_type , auth_event_name.​value , auth_factor_num , sequence_no , action_flags, dg_hier_level_1 , dg_hier_level_2 , dg_hier_level_3 , dg_hier_level_4 , vsys_name , log_source_name , vsys_id , auth_proto , rule_matched_uuid , time_generated_high_res , source_device_category , source_device_profile , source_device_model , source_device_vendor , source_device_osfamily , source_device_osversion , source_device_host , source_device_mac , service_region , EMPTY, user_agent , session_id 

 Previous 

 Authentication 

 Next 

 Authentication CEF Fields 

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
