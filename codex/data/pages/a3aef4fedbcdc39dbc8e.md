---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/strata-logging-service/log-reference/network-logs/network-userid-log/network-userid-https-fields.html
fetched_at: 2026-09-16T11:04:47Z
source: palo-alto-main
---

# UserID HTTPS Fields Clear

Updated on 

 Mon Sep 14 22:55:52 PDT 2026 

 Focus 

 Home 

 Strata Logging Service 

 Strata Logging Service Log Reference 

 Network Logs 

 UserID 

 UserID HTTPS Fields 

 Download PDF 

 Strata Logging Service 

 UserID HTTPS Fields 

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

 UserID EMAIL Fields 

 Next 

 UserID LEEF Fields 

 UserID HTTPS Fields 

 The following table identifies the UserID field names that the Log Forwarding app
 uses when you forward logs using the HTTPS log format.

 HTTPS Name

 Query Name

 Field Type

 AuthCompletionTime

 auth_completion_time 

 timestamp

 AuthFactorNo

 auth_factor_num 

 int

 AuthenticatedUserDomain

 authenticated_user_info.​domain 

 string

 AuthenticatedUserName

 authenticated_user_info.​name 

 string

 AuthenticatedUserUUID

 authenticated_user_info.​uuid 

 long

 ConfigVersion

 config_version.​value 

 string

 RepeatCount

 count_of_repeats 

 int

 CortexDataLakeTenantID

 customer_id 

 string

 DestinationPort

 dest_port 

 int

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

 EventID

 event_id 

 string

 IsDuplicateLog

 is_dup_log 

 boolean

 IsDuplicateUser

 is_duplicate_user 

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

 MappingDataSource

 mapping_data_source.​value 

 string

 MappingDataSourceName

 mapping_data_source_name 

 string

 MappingDataSourceType

 mapping_data_source_type.​value 

 string

 MappingTimeout

 mapping_timeout 

 int

 MFAFactorType

 mfa_factor_type 

 string

 PanoramaSN

 panorama_serial 

 string

 PlatformType

 platform_type 

 string

 SequenceNo

 sequence_no 

 long

 SourceIP

 source_ip.​value 

 ip

 SourcePort

 source_port 

 int

 Subtype

 sub_type.​value 

 string

 Tag

 tag_name 

 string

 TimeGenerated

 time_generated 

 timestamp

 TimeGeneratedHighResolution

 time_generated_high_res 

 timestamp_high_res

 UGFlags

 ug_flags 

 long

 User

 user 

 string

 UserGroupFound

 user_group_found 

 boolean

 UserIdentifiedBySource

 user_identified_by_source_as 

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

 UserID EMAIL Fields 

 Next 

 UserID LEEF Fields
