---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-auth-log/network-auth-https-fields
fetched_at: 2026-08-13T17:40:18Z
source: palo-alto-main
---

# Authentication HTTPS Fields Clear

Authentication HTTPS Fields 

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

 Authentication HTTPS Fields 

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

 Authentication HTTPS Fields 

 Download PDF 

 Strata Logging Service 

 Authentication HTTPS Fields 

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

 Authentication EMAIL Fields 

 Next 

 Authentication LEEF Fields 

 Authentication HTTPS Fields 

 The following table identifies the Authentication field names that the Log Forwarding app
 uses when you forward logs using the HTTPS log format.

 HTTPS Name

 Query Name

 Field Type

 AuthenticationDescription

 auth_description 

 string

 AuthEvent

 auth_event_name.​value 

 string

 AuthFactorNo

 auth_factor_num 

 int

 AuthenticationPolicy

 auth_policy 

 string

 AuthenticationProtocol

 auth_proto 

 int

 AuthServerProfile

 auth_server_profile 

 string

 AuthenticatedUserDomain

 authenticated_user_info.​domain 

 string

 AuthenticatedUserName

 authenticated_user_info.​name 

 string

 AuthenticatedUserUUID

 authenticated_user_info.​uuid 

 long

 ClientType

 client_type 

 int

 ClientTypeName

 client_type_name.​value 

 string

 ConfigVersion

 config_version.​value 

 string

 RepeatCount

 count_of_repeats 

 int

 CortexDataLakeTenantID

 customer_id 

 string

 DGHierarchyLevel1

 dg_hier_level_1 

 int

 DGHierarchyLevel2

 dg_hier_level_2 

 int

 DGHierarchyLevel3

 dg_hier_level_3 

 int

 DGHierarchyLevel4

 dg_hier_level_4 

 int

 IsDuplicateLog

 is_dup_log 

 boolean

 LogExported

 is_exported 

 boolean

 LogForwarded

 is_forwarded 

 boolean

 IsPrismaNetworks

 is_prisma_branch 

 boolean

 IsPrismaUsers

 is_prisma_mobile 

 boolean

 Location

 location 

 string

 LogSetting

 log_set 

 string

 LogSource

 log_source 

 string

 LogSourceGroupID

 log_source_group_id 

 string

 DeviceSN

 log_source_id 

 string

 DeviceName

 log_source_name 

 string

 LogSourceTimeZoneOffset

 log_source_tz_offset 

 int

 TimeReceived

 log_time 

 timestamp

 LogType

 log_type.​value 

 string

 MFAAuthenticationID

 mfa_auth_id 

 long

 MFAVendor

 mfa_vendor 

 string

 NormalizeUser

 normalize_user 

 string

 Object

 object 

 string

 PanoramaSN

 panorama_serial 

 string

 PlatformType

 platform_type 

 string

 Rule

 rule_matched 

 string

 RuleUUID

 rule_matched_uuid 

 string

 SequenceNo

 sequence_no 

 long

 AuthCacheServiceRegion

 service_region 

 string

 SessionID

 session_id 

 int

 SourceDeviceCategory

 source_device_category 

 string

 SourceDeviceHost

 source_device_host 

 string

 SourceDeviceMac

 source_device_mac 

 string

 SourceDeviceModel

 source_device_model 

 string

 SourceDeviceOSFamily

 source_device_osfamily 

 string

 SourceDeviceOSVersion

 source_device_osversion 

 string

 SourceDeviceProfile

 source_device_profile 

 string

 SourceDeviceVendor

 source_device_vendor 

 string

 SourceIP

 source_ip.​value 

 ip

 Subtype

 sub_type.​value 

 string

 TimeGenerated

 time_generated 

 timestamp

 TimeGeneratedHighResolution

 time_generated_high_res 

 timestamp_high_res

 User

 user 

 string

 UserAgentString

 user_agent 

 string

 VendorName

 vendor_name 

 string

 VirtualLocation

 vsys 

 string

 VirtualSystemID

 vsys_id 

 int

 VirtualSystemName

 vsys_name 

 string

 Previous 

 Authentication EMAIL Fields 

 Next 

 Authentication LEEF Fields 

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
