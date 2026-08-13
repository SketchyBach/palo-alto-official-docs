---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/endpoint-logs/endpoint-epm-log/endpoint-epm-cef-fields
fetched_at: 2026-08-13T17:40:08Z
source: palo-alto-main
---

# Management CEF Fields Clear

Management CEF Fields 

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

 Management CEF Fields 

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

 Endpoint Logs 

 Management 

 Management CEF Fields 

 Download PDF 

 Strata Logging Service 

 Management CEF Fields 

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

 Management Syslog Default Field Order 

 Next 

 Management EMAIL Fields 

 Management CEF Fields 

 The following table identifies the Management field names that the Log Forwarding app
 uses when you forward logs using the CEF log format.

 CEF Name

 Field Details

 PanOSAttemptedGateways

 Query Name: attempted_gateways 

 Header Type: Custom 

 PanOSAuthMethod

 Query Name: auth_method 

 Header Type: Custom 

 PanOSConfigVersion

 Query Name: config_version.​value 

 Header Type: Custom 

 PanOSConnectionMethod

 Query Name: connect_method 

 Header Type: Custom 

 PanOSConnectionErrorID

 Query Name: connection_error.​id 

 Header Type: Custom 

 PanOSConnectionError

 Query Name: connection_error.​value 

 Header Type: Custom 

 PanOSCountOfRepeats

 Query Name: count_of_repeats 

 Header Type: Custom 

 PanOSTenantID

 Query Name: customer_id 

 Header Type: Custom 

 PanOSDGHierarchyLevel1

 Query Name: dg_hier_level_1 

 Header Type: Custom 

 PanOSDGHierarchyLevel2

 Query Name: dg_hier_level_2 

 Header Type: Custom 

 PanOSDGHierarchyLevel3

 Query Name: dg_hier_level_3 

 Header Type: Custom 

 PanOSDGHierarchyLevel4

 Query Name: dg_hier_level_4 

 Header Type: Custom 

 shost

 Query Name: endpoint_device_name 

 Header Type: Predefined 

 PanOSGlobalProtectClientVersion

 Query Name: endpoint_gp_version 

 Header Type: Custom 

 PanOSEndpointOSType

 Query Name: endpoint_os_type 

 Header Type: Custom 

 PanOSEndpointOSVersion

 Query Name: endpoint_os_version 

 Header Type: Custom 

 PanOSEndpointSN

 Query Name: endpoint_serial_number 

 Header Type: Custom 

 Name

 Query Name: event_id.​value 

 Header Type: Custom 

 PanOSGateway

 Query Name: gateway 

 Header Type: Custom 

 PanOSGatewayPriority

 Query Name: gateway_priority.​value 

 Header Type: Custom 

 PanOSGatewaySelectionType

 Query Name: gateway_selection_type 

 Header Type: Custom 

 PanOSGlobalProtectGatewayLocation

 Query Name: gpg_location 

 Header Type: Custom 

 PanOSHostID

 Query Name: host_id 

 Header Type: Custom 

 PanOSIsDuplicateLog

 Query Name: is_dup_log 

 Header Type: Custom 

 PanOSLogExported

 Query Name: is_exported 

 Header Type: Custom 

 PanOSLogForwarded

 Query Name: is_forwarded 

 Header Type: Custom 

 PanOSIsPrismaNetworks

 Query Name: is_prisma_branch 

 Header Type: Custom 

 PanOSIsPrismaUsers

 Query Name: is_prisma_mobile 

 Header Type: Custom 

 sourceServiceName

 Query Name: log_source 

 Header Type: Predefined 

 LogSourceGroupID

 Query Name: log_source_group_id 

 Header Type: Custom 

 Max Length: 255 

 deviceExternalID

 Query Name: log_source_id 

 Header Type: Predefined 

 dvchost

 Query Name: log_source_name 

 Header Type: Predefined 

 PanOSLogSourceTimeZoneOffset

 Query Name: log_source_tz_offset 

 Header Type: Custom 

 rt

 Query Name: log_time 

 Header Type: Predefined 

 Device Event Class ID

 Query Name: log_type.​value 

 Header Type: Custom 

 PanOSLoginDuration

 Query Name: login_duration 

 Header Type: Custom 

 PanOSDescription

 Query Name: opaque 

 Header Type: Custom 

 PanOSPanoramaSN

 Query Name: panorama_serial 

 Header Type: Custom 

 PlatformType

 Query Name: platform_type 

 Header Type: Custom 

 PanOSPortal

 Query Name: portal 

 Header Type: Custom 

 PanOSPrivateIPv4

 Query Name: private_ip.​value 

 Header Type: Custom 

 PanOSPrivateIPv6

 Query Name: private_ipv6.​value 

 Header Type: Custom 

 ProjectName

 Query Name: project_name 

 Header Type: Custom 

 src

 Query Name: public_ip.​value 

 Header Type: Predefined 

 c6a2

 Query Name: public_ipv6.​value 

 Header Type: Predefined 

 PanOSQuarantineReason

 Query Name: quarantine_reason 

 Header Type: Custom 

 PanOSSequenceNo

 Query Name: sequence_no 

 Header Type: Custom 

 PanOSSourceRegion

 Query Name: source_region 

 Header Type: Custom 

 suser

 Query Name: source_user 

 Header Type: Predefined 

 sntdom and dntdom

 Query Name: source_user_info.​domain 

 Header Type: Predefined 

 suser and duser

 Query Name: source_user_info.​name 

 Header Type: Predefined 

 suid and duid

 Query Name: source_user_info.​uuid 

 Header Type: Predefined 

 PanOSSSLResponseTime

 Query Name: ssl_response_time 

 Header Type: Custom 

 PanOSStage

 Query Name: stage 

 Header Type: Custom 

 outcome

 Query Name: status.​value 

 Header Type: Predefined 

 PanOSLogSubtype

 Query Name: sub_type.​value 

 Header Type: Custom 

 start

 Query Name: time_generated 

 Header Type: Predefined 

 PanOSTimeGeneratedHighResolution

 Query Name: time_generated_high_res 

 Header Type: Custom 

 PanOSTunnelType

 Query Name: tunnel 

 Header Type: Custom 

 Device Vendor

 Query Name: vendor_name 

 Header Type: Custom 

 PanOSVirtualSystem

 Query Name: vsys 

 Header Type: Custom 

 PanOSVirtualSystemID

 Query Name: vsys_id 

 Header Type: Custom 

 cs3

 Query Name: vsys_name 

 Header Type: Predefined 

 Previous 

 Management Syslog Default Field Order 

 Next 

 Management EMAIL Fields 

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

 Strata Logging Service 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
