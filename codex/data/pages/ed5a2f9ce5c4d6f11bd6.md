---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-iptag-log/network-iptag-email-fields
fetched_at: 2026-08-13T17:40:27Z
source: palo-alto-main
---

# IPtag EMAIL Fields Clear

IPtag EMAIL Fields 

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

 IPtag EMAIL Fields 

 Updated on 

 Jul 3, 2026 

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

 Jul 3, 2026 

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
