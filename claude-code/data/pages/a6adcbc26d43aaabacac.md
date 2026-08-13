---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-sctp-log/network-sctp-cef-fields
fetched_at: 2026-08-13T17:40:32Z
source: palo-alto-main
---

# SCTP CEF Fields Clear

SCTP CEF Fields 

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

 SCTP CEF Fields 

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

 SCTP 

 SCTP CEF Fields 

 Download PDF 

 Strata Logging Service 

 SCTP CEF Fields 

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

 SCTP Syslog Default Field Order 

 Next 

 SCTP EMAIL Fields 

 SCTP CEF Fields 

 Example SCTP log in CEF:

 Mar 1 21:22:04 xxx.xx.x.xx 3429 <14>1 2021-03-01T21:22:04.531Z stream-logfwd20-587718190-03011312-b28y-harness-x4nx logforwarder - panwlogs - CEF:0|Palo Alto Networks|LF|2.0|SCTP||9|ProfileToken=xxxxx dtz=UTC rt=Mar 01 2021 21:22:02 deviceExternalId=xxxxxxxxxxxxx PanOSCaptivePortal= PanOSContentVersion= PanOSCortexDataLakeTenantID=xxxxxxxxxxxxx PanOSDestinationDeviceClass= PanOSDestinationDeviceMac= PanOSDestinationDeviceModel= PanOSDestinationDeviceOS= PanOSDestinationDeviceVendor= PanOSDestinationLocation=IN PanOSDestinationUUID= PanOSDestinationUserDomain=paloaltonetwork PanOSDestinationUserName=xxxxx PanOSDestinationUserUUID= PanOSInboundInterfaceDetailsPort=1 PanOSInboundInterfaceDetailsSlot=1 PanOSInboundInterfaceDetailsType=ethernet PanOSInboundInterfaceDetailsUnit=0 PanOSIsClienttoServer= PanOSIsContainer= PanOSIsDecryptMirror= PanOSIsDecryptedLog= PanOSIsDecryptedPayloadForward= PanOSIsDuplicateLog=false PanOSIsIPV6= PanOSIsInspectrionBeforeSession= PanOSIsMptcpOn= PanOSIsNonStandardDestinationPort= PanOSIsPacketCapture= PanOSIsPhishing= PanOSIsPrismaNetwork=false PanOSIsPrismaUsers=false PanOSIsProxy= PanOSIsReconExcluded= PanOSIsServertoClient= PanOSIsSourceXForwarded= PanOSIsSystemReturn= PanOSIsTransaction= PanOSIsTunnelInspected= PanOSIsURLDenied= PanOSLogExported=false PanOSLogForwarded=true PanOSLogSource=firewall PanOSLogSourceTimeZoneOffset= PanOSNAT= PanOSOutboundInterfaceDetailsPort=2 PanOSOutboundInterfaceDetailsSlot=1 PanOSOutboundInterfaceDetailsType=ethernet PanOSOutboundInterfaceDetailsUnit=0 PanOSSessionEndReason= PanOSSessionOwnerMidx= PanOSSessionTracker= PanOSSeverity=Critical PanOSSourceDeviceClass= PanOSSourceDeviceMac= PanOSSourceDeviceModel= PanOSSourceDeviceOS= PanOSSourceDeviceVendor= PanOSSourceLocation=US PanOSSourceUUID= PanOSSourceUserDomain=paloaltonetwork PanOSSourceUserName=xxxxx PanOSSourceUserUUID= PanOSTunnel=N/A PanOSVirtualSystemID=1 PanOSConfigVersion= start=Mar 01 2021 21:22:02 src=xxx.xx.x.xx dst=xxx.xx.x.xx PanOSNATSource=xxx.xx.x.xx PanOSNATDestination=xxx.xx.x.xx cs1=allow-business-apps cs1Label=Rule PanOSSourceUser=paloaltonetwork\\xxxxx PanOSDestinationUser=paloaltonetworkxxxxx PanOSApplication=panorama cs3=vsys1 cs3Label=VirtualLocation cs4=corporate cs4Label=FromZone cs5=untrust cs5Label=ToZone PanOSInboundInterface=ethernet1/1 deviceOutboundInterface=ethernet1/2 cs6=test cs6Label=LogSetting PanOSSessionID=391582 cnt=1 spt=3033 dpt=5496 PanOSNATSourcePort=26714 PanOSNATDestinationPort=15054 proto=tcp act=alert PanOSDGHierarchyLevel1=12 PanOSDGHierarchyLevel2=0 PanOSDGHierarchyLevel3=0 PanOSDGHierarchyLevel4=0 PanOSVirtualSystemName= dvchost=PA-5220 externalId=xxxxxxxxxxxxx PanOSEndpointAssociationID=2086888838 PanOSPayloadProtocolID=-1 PanOSSctpChunkType=9 PanOSSCTPEventType=Kerberos single sign-on failed PanOSEventCode=3 PanOSVerificationTag1=0x3bae3042 PanOSVerificationTag2=0x1911015e PanOSSctpCauseCode=0 PanOSDiamAppID=-1 PanOSDiameterCommandCode=-1 PanOSDiamAvpCode=0 PanOSStreamID=0 PanOSAssocationEndReason= PanOSMapAppCode=0 PanOSSccpCallingSSN=0 PanOSSccpCallingGt= PanOSSctpFilter= PanOSChunksTotal=0 PanOSChunksSent=0 PanOSChunksReceived=0 PanOSPacketsTotal=0 PanOSPacketsSent=0 PanOSPacketsReceived=0 PanOSRuleUUID= PanOSContainerID= PanOSContainerNameSpace= PanOSContainerName= PanOSSourceEDL= PanOSDestinationEDL= PanOSSourceDynamicAddressGroup= PanOSDestinationDynamicAddressGroup= PanOSTimeGeneratedHighResolution=Jul 25 2019 23:30:12 

 The following table identifies the SCTP field names that the Log Forwarding app
 uses when you forward logs using the CEF log format.

 CEF Name

 Field Details

 act

 Query Name: action.​value 

 Header Type: Predefined 

 Max Length: 63 

 PanOSApplication

 Query Name: app 

 Header Type: Custom 

 PanOSAssocationEndReason

 Query Name: association_end_reason.​value 

 Header Type: Custom 

 PanOSChunksReceived

 Query Name: chunks_received 

 Header Type: Custom 

 PanOSChunksSent

 Query Name: chunks_sent 

 Header Type: Custom 

 PanOSChunksTotal

 Query Name: chunks_total 

 Header Type: Custom 

 PanOSConfigVersion

 Query Name: config_version.​value 

 Header Type: Custom 

 PanOSContainerID

 Query Name: container_id 

 Header Type: Custom 

 PanOSContentVersion

 Query Name: content_version 

 Header Type: Custom 

 cnt

 Query Name: count_of_repeats 

 Header Type: Predefined 

 PanOSCortexDataLakeTenantID

 Query Name: customer_id 

 Header Type: Custom 

 PanOSDestinationDeviceClass

 Query Name: dest_device_class 

 Header Type: Custom 

 PanOSDestinationDeviceMac

 Query Name: dest_device_mac 

 Header Type: Custom 

 PanOSDestinationDeviceModel

 Query Name: dest_device_model 

 Header Type: Custom 

 PanOSDestinationDeviceOS

 Query Name: dest_device_os 

 Header Type: Custom 

 PanOSDestinationDeviceVendor

 Query Name: dest_device_vendor 

 Header Type: Custom 

 PanOSDestinationDynamicAddressGroup

 Query Name: dest_dynamic_address_group 

 Header Type: Custom 

 PanOSDestinationEDL

 Query Name: dest_edl 

 Header Type: Custom 

 dst or c6a3

 Query Name: dest_ip.​value 

 Header Type: Predefined 

 Label: || c6a3Label 

 Label Text: || Destination IPv6 Address 

 PanOSDestinationLocation

 Query Name: dest_location 

 Header Type: Custom 

 dpt

 Query Name: dest_port 

 Header Type: Predefined 

 PanOSDestinationUser

 Query Name: dest_user 

 Header Type: Custom 

 PanOSDestinationUserDomain

 Query Name: dest_user_info.​domain 

 Header Type: Custom 

 PanOSDestinationUserName

 Query Name: dest_user_info.​name 

 Header Type: Custom 

 PanOSDestinationUserUUID

 Query Name: dest_user_info.​uuid 

 Header Type: Custom 

 PanOSDestinationUUID

 Query Name: dest_uuid 

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

 PanOSDiamAppID

 Query Name: diam_app_id 

 Header Type: Custom 

 PanOSDiamAvpCode

 Query Name: diam_avp_code 

 Header Type: Custom 

 PanOSDiameterCommandCode

 Query Name: diam_cmd_code 

 Header Type: Custom 

 PanOSEndpointAssociationID

 Query Name: ep_assoc_id 

 Header Type: Custom 

 PanOSEventCode

 Query Name: event_code 

 Header Type: Custom 

 PanOSSCTPEventType

 Query Name: event_type.​value 

 Header Type: Custom 

 cs4

 Query Name: from_zone 

 Header Type: Predefined 

 Label: cs4Label 

 Label Text: FromZone 

 Max Length: 4000 

 PanOSInboundInterface

 Query Name: inbound_if.​value 

 Header Type: Custom 

 PanOSInboundInterfaceDetailsPort

 Query Name: inbound_if_details.​port 

 Header Type: Custom 

 PanOSInboundInterfaceDetailsSlot

 Query Name: inbound_if_details.​slot 

 Header Type: Custom 

 PanOSInboundInterfaceDetailsType

 Query Name: inbound_if_details.​type.​value 

 Header Type: Custom 

 PanOSInboundInterfaceDetailsUnit

 Query Name: inbound_if_details.​unit 

 Header Type: Custom 

 PanOSCaptivePortal

 Query Name: is_captive_portal 

 Header Type: Custom 

 PanOSIsClienttoServer

 Query Name: is_client_to_server 

 Header Type: Custom 

 PanOSIsContainer

 Query Name: is_container 

 Header Type: Custom 

 PanOSIsDecryptMirror

 Query Name: is_decrypt_mirror 

 Header Type: Custom 

 PanOSIsDecryptedPayloadForward

 Query Name: is_decrypted_payload_fwded 

 Header Type: Custom 

 PanOSIsDecryptedLog

 Query Name: is_decryption_log 

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

 PanOSIsIPV6

 Query Name: is_ipv6 

 Header Type: Custom 

 PanOSIsInspectrionBeforeSession

 Query Name: is_l7_inspection_b4_session 

 Header Type: Custom 

 PanOSIsMptcpOn

 Query Name: is_mptcp_on 

 Header Type: Custom 

 PanOSNAT

 Query Name: is_nat 

 Header Type: Custom 

 PanOSIsNonStandardDestinationPort

 Query Name: is_non_std_dest_port 

 Header Type: Custom 

 PanOSIsPacketCapture

 Query Name: is_packet_capture 

 Header Type: Custom 

 PanOSIsPhishing

 Query Name: is_phishing 

 Header Type: Custom 

 PanOSIsPrismaNetwork

 Query Name: is_prisma_branch 

 Header Type: Custom 

 PanOSIsPrismaUsers

 Query Name: is_prisma_mobile 

 Header Type: Custom 

 PanOSIsProxy

 Query Name: is_proxy 

 Header Type: Custom 

 PanOSIsReconExcluded

 Query Name: is_recon_excluded 

 Header Type: Custom 

 PanOSIsServertoClient

 Query Name: is_server_to_client 

 Header Type: Custom 

 PanOSIsSourceXForwarded

 Query Name: is_source_x_fwded 

 Header Type: Custom 

 PanOSIsSystemReturn

 Query Name: is_sym_return 

 Header Type: Custom 

 PanOSIsTransaction

 Query Name: is_transaction 

 Header Type: Custom 

 PanOSIsTunnelInspected

 Query Name: is_tunnel_inspected 

 Header Type: Custom 

 PanOSIsURLDenied

 Query Name: is_url_denied 

 Header Type: Custom 

 cs6

 Query Name: log_set 

 Header Type: Predefined 

 Label: cs6Label 

 Label Text: LogSetting 

 Max Length: 4000 

 PanOSLogSource

 Query Name: log_source 

 Header Type: Custom 

 LogSourceGroupID

 Query Name: log_source_group_id 

 Header Type: Custom 

 Max Length: 255 

 deviceExternalId

 Query Name: log_source_id 

 Header Type: Predefined 

 Max Length: 255 

 dvchost

 Query Name: log_source_name 

 Header Type: Predefined 

 Max Length: 100 

 PanOSLogSourceTimeZoneOffset

 Query Name: log_source_tz_offset 

 Header Type: Custom 

 rt

 Query Name: log_time 

 Header Type: Predefined 

 Device Event Class ID

 Query Name: log_type.​value 

 Header Type: Custom 

 PanOSMapAppCode

 Query Name: map_op_code 

 Header Type: Custom 

 PanOSNATDestination

 Query Name: nat_dest.​value 

 Header Type: Custom 

 PanOSNATDestinationPort

 Query Name: nat_dest_port 

 Header Type: Custom 

 PanOSNATSource

 Query Name: nat_source.​value 

 Header Type: Custom 

 PanOSNATSourcePort

 Query Name: nat_source_port 

 Header Type: Custom 

 deviceOutboundInterface

 Query Name: outbound_if.​value 

 Header Type: Predefined 

 Max Length: 128 

 PanOSOutboundInterfaceDetailsPort

 Query Name: outbound_if_details.​port 

 Header Type: Custom 

 PanOSOutboundInterfaceDetailsSlot

 Query Name: outbound_if_details.​slot 

 Header Type: Custom 

 PanOSOutboundInterfaceDetailsType

 Query Name: outbound_if_details.​type.​value 

 Header Type: Custom 

 PanOSOutboundInterfaceDetailsUnit

 Query Name: outbound_if_details.​unit 

 Header Type: Custom 

 PanOSPacketsReceived

 Query Name: packets_received 

 Header Type: Custom 

 PanOSPacketsSent

 Query Name: packets_sent 

 Header Type: Custom 

 PanOSPacketsTotal

 Query Name: packets_total 

 Header Type: Custom 

 PanOSPanoramaSN

 Query Name: panorama_serial 

 Header Type: Custom 

 PanOSPayloadProtocolID

 Query Name: payload_protocol_id 

 Header Type: Custom 

 PlatformType

 Query Name: platform_type 

 Header Type: Custom 

 PanOSContainerName

 Query Name: pod_name 

 Header Type: Custom 

 PanOSContainerNameSpace

 Query Name: pod_namespace 

 Header Type: Custom 

 proto

 Query Name: protocol.​value 

 Header Type: Predefined 

 Max Length: 31 

 cs1

 Query Name: rule_matched 

 Header Type: Predefined 

 Label: cs1Label 

 Label Text: Rule 

 Max Length: 4000 

 PanOSRuleUUID

 Query Name: rule_matched_uuid 

 Header Type: Custom 

 PanOSSccpCallingGt

 Query Name: sccp_calling_gt 

 Header Type: Custom 

 PanOSSccpCallingSSN

 Query Name: sccp_calling_ssn 

 Header Type: Custom 

 PanOSSctpCauseCode

 Query Name: sctp_cause_code 

 Header Type: Custom 

 PanOSSctpChunkType

 Query Name: sctp_chunk_type 

 Header Type: Custom 

 PanOSSctpFilter

 Query Name: sctp_filter 

 Header Type: Custom 

 externalId

 Query Name: sequence_no 

 Header Type: Predefined 

 Max Length: 40 

 PanOSSessionOwnerMidx

 Query Name: sess_owner_rt_midx 

 Header Type: Custom 

 PanOSSessionEndReason

 Query Name: session_end_reason.​value 

 Header Type: Custom 

 PanOSSessionID

 Query Name: session_id 

 Header Type: Custom 

 PanOSSessionTracker

 Query Name: session_tracker 

 Header Type: Custom 

 PanOSSeverity

 Query Name: severity 

 Header Type: Custom 

 PanOSSourceDeviceClass

 Query Name: source_device_class 

 Header Type: Custom 

 PanOSSourceDeviceMac

 Query Name: source_device_mac 

 Header Type: Custom 

 PanOSSourceDeviceModel

 Query Name: source_device_model 

 Header Type: Custom 

 PanOSSourceDeviceOS

 Query Name: source_device_os 

 Header Type: Custom 

 PanOSSourceDeviceVendor

 Query Name: source_device_vendor 

 Header Type: Custom 

 PanOSSourceDynamicAddressGroup

 Query Name: source_dynamic_address_group 

 Header Type: Custom 

 PanOSSourceEDL

 Query Name: source_edl 

 Header Type: Custom 

 src or c6a2

 Query Name: source_ip.​value 

 Header Type: Predefined 

 Label: || c6a2Label 

 Label Text: || Source IPv6 Address 

 PanOSSourceLocation

 Query Name: source_location 

 Header Type: Custom 

 spt

 Query Name: source_port 

 Header Type: Predefined 

 PanOSSourceUser

 Query Name: source_user 

 Header Type: Custom 

 PanOSSourceUserDomain

 Query Name: source_user_info.​domain 

 Header Type: Custom 

 PanOSSourceUserName

 Query Name: source_user_info.​name 

 Header Type: Custom 

 PanOSSourceUserUUID

 Query Name: source_user_info.​uuid 

 Header Type: Custom 

 PanOSSourceUUID

 Query Name: source_uuid 

 Header Type: Custom 

 PanOSStreamID

 Query Name: stream_id 

 Header Type: Custom 

 Name

 Query Name: sub_type.​value 

 Header Type: Custom 

 start

 Query Name: time_generated 

 Header Type: Predefined 

 PanOSTimeGeneratedHighResolution

 Query Name: time_generated_high_res 

 Header Type: Custom 

 cs5

 Query Name: to_zone 

 Header Type: Predefined 

 Label: cs5Label 

 Label Text: ToZone 

 Max Length: 4000 

 PanOSTunnel

 Query Name: tunnel.​value 

 Header Type: Custom 

 Device Vendor

 Query Name: vendor_name 

 Header Type: Custom 

 PanOSVendorSeverity

 Query Name: vendor_severity.​value 

 Header Type: Custom 

 PanOSVerificationTag1

 Query Name: verification_tag_1 

 Header Type: Custom 

 PanOSVerificationTag2

 Query Name: verification_tag_2 

 Header Type: Custom 

 cs3

 Query Name: vsys 

 Header Type: Predefined 

 Label: cs3Label 

 Label Text: VirtualLocation 

 Max Length: 4000 

 PanOSVirtualSystemID

 Query Name: vsys_id 

 Header Type: Custom 

 PanOSVirtualSystemName

 Query Name: vsys_name 

 Header Type: Custom 

 Previous 

 SCTP Syslog Default Field Order 

 Next 

 SCTP EMAIL Fields 

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
