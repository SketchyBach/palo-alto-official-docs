---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-iptag-log/network-iptag-email-fields
fetched_at: 2026-09-16T07:51:50Z
source: strata-and-sase
---

# IPtag EMAIL Fields Clear

Updated on 

 Fri Sep 11 10:21:34 PDT 2026 

 Focus 

 Home 

 Strata Logging Service 

 Strata Logging Service Log Reference 

 Network Logs 

 IPtag 

 IPtag EMAIL Fields 

 Download PDF 

 Strata Logging Service 

 IPtag EMAIL Fields 

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

 IPtag CEF Fields 

 Next 

 IPtag HTTPS Fields 

 IPtag EMAIL Fields 

 Example IPtag log in EMAIL:

 TimeReceived=2021-02-23T02:44:43.000000Z
DeviceSN=xxxxxxxxxxxxx
LogType=IPTAG
Subtype=iptag
ConfigVersion=
TimeGenerated=2021-02-23T02:44:43.000000Z
VirtualLocation=vsys1
SourceIP=xxxxxxxxxxxx
TagName=
EventID=Unregister
CountOfRepeats=1
MappingTimeout=10
MappingDataSource=XMLAPI
MappingDataSourceType=XML-API
MappingDataSourceSubType=Unknown
SequenceNo=7743
DGHierarchyLevel1=18
DGHierarchyLevel2=0
DGHierarchyLevel3=0
DGHierarchyLevel4=0
VirtualSystemName=
DeviceName=PA-VM
VirtualSystemID=1
IPSubnetRange=
TimeGeneratedHighResolution=2019-07-25T23:30:12.000000Z 

 The following table identifies the IPtag field names that the Log Forwarding app
 uses when you forward logs using the EMAIL log format.

 EMAIL Name

 Query Name

 ConfigVersion

 config_version.​value 

 RepeatCount

 count_of_repeats 

 CortexDataLakeTenantID

 customer_id 

 DGHierarchyLevel1

 dg_hier_level_1 

 DGHierarchyLevel2

 dg_hier_level_2 

 DGHierarchyLevel3

 dg_hier_level_3 

 DGHierarchyLevel4

 dg_hier_level_4 

 EventID

 event_id.​value 

 IPSubnetRange

 ip_subnet_range 

 IsDuplicateLog

 is_dup_log 

 LogExported

 is_exported 

 LogForwarded

 is_forwarded 

 IsPrismaNetworks

 is_prisma_branch 

 IsPrismaUsers

 is_prisma_mobile 

 LogSetting

 log_set 

 LogSource

 log_source 

 LogSourceGroupID

 log_source_group_id 

 DeviceSN

 log_source_id 

 DeviceName

 log_source_name 

 LogSourceTimeZoneOffset

 log_source_tz_offset 

 TimeReceived

 log_time 

 LogType

 log_type.​value 

 MappingDataSource

 mapping_data_source_name 

 MappingDataSourceSubType

 mapping_data_source_sub_type.​value 

 MappingDataSourceType

 mapping_data_source_type.​value 

 MappingTimeout

 mapping_timeout 

 PanoramaSN

 panorama_serial 

 PlatformType

 platform_type 

 Rule

 rule_matched 

 RuleUUID

 rule_matched_uuid 

 SequenceNo

 sequence_no 

 SourceIP

 source_ip.​value 

 Subtype

 sub_type.​value 

 TagName

 tag_name 

 TimeGenerated

 time_generated 

 TimeGeneratedHighResolution

 time_generated_high_res 

 VendorName

 vendor_name 

 VirtualLocation

 vsys 

 VirtualSystemID

 vsys_id 

 VirtualSystemName

 vsys_name 

 Previous 

 IPtag CEF Fields 

 Next 

 IPtag HTTPS Fields
