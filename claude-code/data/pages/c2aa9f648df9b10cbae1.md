---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-sctp-log/network-sctp-email-fields
fetched_at: 2026-08-13T17:40:32Z
source: palo-alto-main
---

# SCTP EMAIL Fields Clear

SCTP EMAIL Fields 

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

 SCTP EMAIL Fields 

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

 SCTP EMAIL Fields 

 Download PDF 

 Strata Logging Service 

 SCTP EMAIL Fields 

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

 SCTP CEF Fields 

 Next 

 SCTP HTTPS Fields 

 SCTP EMAIL Fields 

 Example SCTP log in EMAIL:

 TimeReceived=2021-02-23T02:45:00.000000Z
DeviceSN=xxxxxxxxxxxxx
LogType=SCTP
Subtype=
ConfigVersion=
TimeGenerated=2021-02-23T02:45:00.000000Z
SourceIP=xxxxxxxxxxxx
DestinationIP=xxx.xx.x.xx
NATSource=xxx.xx.x.xx
NATDestination=xxx.xx.x.xx
Rule=allow-business-apps
SourceUser="paloaltonetwork\xxxxx"
DestinationUser=paloaltonetworkxxxxx
Application=panorama
VirtualLocation=vsys1
FromZone=corporate
ToZone=untrust
InboundInterface=ethernet1/1
OutboundInterface=ethernet1/2
LogSetting=test
SessionID=391582
RepeatCount=1
SourcePort=3033
DestinationPort=5496
NATSourcePort=26714
NATDestinationPort=15054
Protocol=tcp
Action=alert
DGHierarchyLevel1=12
DGHierarchyLevel2=0
DGHierarchyLevel3=0
DGHierarchyLevel4=0
VirtualSystemName=
DeviceName=PA-5220
SequenceNo=6711379990526573312
EndpointAssociationID=2086888838
PayloadProtocolID=-1
VendorSeverity=Critical
SctpChunkType=9
SCTPEventType=Kerberos single sign-on failed
EventCode=3
VerificationTag1=0x3bae3042
VerificationTag2=0x1911015e
SctpCauseCode=0
DiamAppID=-1
DiameterCommandCode=-1
DiamAvpCode=0
StreamID=0
AssocationEndReason=
MapAppCode=0
SccpCallingSSN=0
SccpCallingGt=
SctpFilter=
ChunksTotal=0
ChunksSent=0
ChunksReceived=0
PacketsTotal=0
PacketsSent=0
PacketsReceived=0
RuleUUID=
ContainerID=
ContainerNameSpace=
ContainerName=
SourceEDL=
DestinationEDL=
SourceDynamicAddressGroup=
DestinationDynamicAddressGroup=
TimeGeneratedHighResolution=2019-07-25T23:30:12.000000Z 

 The following table identifies the SCTP field names that the Log Forwarding app
 uses when you forward logs using the EMAIL log format.

 EMAIL Name

 Query Name

 Action

 action.​value 

 Application

 app 

 AssocationEndReason

 association_end_reason.​value 

 ChunksReceived

 chunks_received 

 ChunksSent

 chunks_sent 

 ChunksTotal

 chunks_total 

 ConfigVersion

 config_version.​value 

 ContainerID

 container_id 

 ContentVersion

 content_version 

 RepeatCount

 count_of_repeats 

 CortexDataLakeTenantID

 customer_id 

 DestinationDeviceClass

 dest_device_class 

 DestinationDeviceMac

 dest_device_mac 

 DestinationDeviceModel

 dest_device_model 

 DestinationDeviceOS

 dest_device_os 

 DestinationDeviceVendor

 dest_device_vendor 

 DestinationDynamicAddressGroup

 dest_dynamic_address_group 

 DestinationEDL

 dest_edl 

 DestinationIP

 dest_ip.​value 

 DestinationLocation

 dest_location 

 DestinationPort

 dest_port 

 DestinationUser

 dest_user 

 DestinationUserInfoDomain

 dest_user_info.​domain 

 DestinationUserInfoName

 dest_user_info.​name 

 DestinationUserInfoUUID

 dest_user_info.​uuid 

 DestinationUUID

 dest_uuid 

 DGHierarchyLevel1

 dg_hier_level_1 

 DGHierarchyLevel2

 dg_hier_level_2 

 DGHierarchyLevel3

 dg_hier_level_3 

 DGHierarchyLevel4

 dg_hier_level_4 

 DiamAppID

 diam_app_id 

 DiamAvpCode

 diam_avp_code 

 DiameterCommandCode

 diam_cmd_code 

 EndpointAssociationID

 ep_assoc_id 

 EventCode

 event_code 

 SCTPEventType

 event_type.​value 

 FromZone

 from_zone 

 InboundInterface

 inbound_if.​value 

 InboundInterfaceDetailsPort

 inbound_if_details.​port 

 InboundInterfaceDetailsSlot

 inbound_if_details.​slot 

 InboundInterfaceDetailsType

 inbound_if_details.​type.​value 

 InboundInterfaceDetailsUnit

 inbound_if_details.​unit 

 CaptivePortal

 is_captive_portal 

 IsClienttoServer

 is_client_to_server 

 IsContainer

 is_container 

 IsDecryptMirror

 is_decrypt_mirror 

 IsDecryptedPayloadForward

 is_decrypted_payload_fwded 

 IsDecryptedLog

 is_decryption_log 

 IsDuplicateLog

 is_dup_log 

 LogExported

 is_exported 

 LogForwarded

 is_forwarded 

 IsIPV6

 is_ipv6 

 IsInspectionBeforeSession

 is_l7_inspection_b4_session 

 IsMptcpOn

 is_mptcp_on 

 NAT

 is_nat 

 IsNonStandardDestinationPort

 is_non_std_dest_port 

 IsPacketCapture

 is_packet_capture 

 IsPhishing

 is_phishing 

 IsPrismaNetwork

 is_prisma_branch 

 IsPrismaUsers

 is_prisma_mobile 

 IsProxy

 is_proxy 

 IsReconExcluded

 is_recon_excluded 

 IsServertoClient

 is_server_to_client 

 IsSourceXForwarded

 is_source_x_fwded 

 IsSystemReturn

 is_sym_return 

 IsTransaction

 is_transaction 

 IsTunnelInspected

 is_tunnel_inspected 

 IsURLDenied

 is_url_denied 

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

 MapAppCode

 map_op_code 

 NATDestination

 nat_dest.​value 

 NATDestinationPort

 nat_dest_port 

 NATSource

 nat_source.​value 

 NATSourcePort

 nat_source_port 

 OutboundInterface

 outbound_if.​value 

 OutboundInterfaceDetailsPort

 outbound_if_details.​port 

 OutboundInterfaceDetailsSlot

 outbound_if_details.​slot 

 OutboundInterfaceDetailsType

 outbound_if_details.​type.​value 

 OutboundInterfaceDetailsUnit

 outbound_if_details.​unit 

 PacketsReceived

 packets_received 

 PacketsSent

 packets_sent 

 PacketsTotal

 packets_total 

 PanoramaSN

 panorama_serial 

 PayloadProtocolID

 payload_protocol_id 

 PlatformType

 platform_type 

 ContainerName

 pod_name 

 ContainerNameSpace

 pod_namespace 

 Protocol

 protocol.​value 

 Rule

 rule_matched 

 RuleUUID

 rule_matched_uuid 

 SccpCallingGt

 sccp_calling_gt 

 SccpCallingSSN

 sccp_calling_ssn 

 SctpCauseCode

 sctp_cause_code 

 SctpChunkType

 sctp_chunk_type 

 SctpFilter

 sctp_filter 

 SequenceNo

 sequence_no 

 SessionOwnerMidx

 sess_owner_rt_midx 

 SessionEndReason

 session_end_reason.​value 

 SessionID

 session_id 

 SessionTracker

 session_tracker 

 Severity

 severity 

 SourceDeviceClass

 source_device_class 

 SourceDeviceMac

 source_device_mac 

 SourceDeviceModel

 source_device_model 

 SourceDeviceOS

 source_device_os 

 SourceDeviceVendor

 source_device_vendor 

 SourceDynamicAddressGroup

 source_dynamic_address_group 

 SourceEDL

 source_edl 

 SourceIP

 source_ip.​value 

 SourceLocation

 source_location 

 SourcePort

 source_port 

 SourceUser

 source_user 

 SourceUserInfoDomain

 source_user_info.​domain 

 SourceUserInfoName

 source_user_info.​name 

 SourceUserInfoUUID

 source_user_info.​uuid 

 SourceUUID

 source_uuid 

 StreamID

 stream_id 

 Subtype

 sub_type.​value 

 TimeGenerated

 time_generated 

 TimeGeneratedHighResolution

 time_generated_high_res 

 ToZone

 to_zone 

 Tunnel

 tunnel.​value 

 VendorName

 vendor_name 

 VendorSeverity

 vendor_severity.​value 

 VerificationTag1

 verification_tag_1 

 VerificationTag2

 verification_tag_2 

 VirtualLocation

 vsys 

 VirtualSystemID

 vsys_id 

 VirtualSystemName

 vsys_name 

 Previous 

 SCTP CEF Fields 

 Next 

 SCTP HTTPS Fields 

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
