---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-url-log/network-url-leef-fields
fetched_at: 2026-08-13T17:40:37Z
source: palo-alto-main
---

# URL LEEF Fields Clear

URL LEEF Fields 

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

 URL LEEF Fields 

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

 URL 

 URL LEEF Fields 

 Download PDF 

 Strata Logging Service 

 URL LEEF Fields 

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

 URL HTTPS Fields 

 Next 

 UserID 

 URL LEEF Fields 

 Example URL log in LEEF:

 Sep 21 01:52:01 gke-standard-cluster-2-pool-3-f004381a-0gw6 2646 <14>1 2021-09-21T01:52:01.328Z stream-logfwd20-d324e775--09201841-lxtx-harness-w8bx logforwarder - panwlogs - LEEF:2.0|Palo Alto Networks|Next Generation Firewall|10.1|sports| |TimeReceived=2021-09-21T01:52:00.000000Z DeviceSN=xxxxxxxxxxxxx cat=threat SubType=url ConfigVersion=10.1 devTime=2021-09-21T01:51:58.000000Z src=fe80:abcd:76cc:9802:d202:b3ff:fe1e:8329 dst=fe80:0:e426:5678:b202:b3ff:fe1e:8329 srcPostNAT=xxx.xx.x.xx dstPostNAT=xxx.xx.x.xx Rule=deny-time-wasters usrName=xxxxx\xxxxx o"'"test DestinationUser=paloaltonetwork\xxxxx Application=aerofs VirtualLocation=vsys1 FromZone=ethernet4Zone-test3 ToZone=ethernet4Zone-test1 InboundInterface=ethernet1/1OutboundInterface=ethernet1/2 LogSetting=rs-logging SessionID=631434 RepeatCount=1 srcPort=29176 dstPort=20350 srcPostNATPort=2932 dstPostNATPort=7181 proto=tcp Action=reset-both URL=www.this.is.another.wannabe.long.url.com/and/it/is/getting/there/by/adding/some/junk/at/the/end/of/the/url/dsakjhfskdjhfksjdhfkhk235hk2jh2kjhkhk23jhk5jh2435kjh45k3jh5k3j4h5k3h45kjh34kj5hkjhkj34hk5jh34k5jhk3j4h5k3jh45kjh34k5jhk34jh5kj34h5kjh43kj5hk34jh5k3j4h5k3j4hghhg4j5h3g VendorSeverity=Critical DirectionOfAttack=client to server SequenceNo=7003061085140561391 SourceLocation=AU DestinationLocation=west-coast ContentType=text/xml PacketID=0 URLCounter=1 UserAgent= identSrc= Referer= DGHierarchyLevel1=11 DGHierarchyLevel2=0 DGHierarchyLevel3=0DGHierarchyLevel4=0 VirtualSystemName= DeviceName=xxxxx SourceUUID= DestinationUUID= HTTPMethod=get IMSI=0 IMEI= ParentSessionID=0 ParentStarttime=1970-01-01T00:00:00.000000Z Tunnel=N/A InlineMLVerdict=unknown ContentVersion=50207 SigFlags=0 HTTPHeaders= URLCategoryList=sports,​travel,​health-and-medicine RuleUUID=2fb8efd4-2f01-421d-a113-097992777432 HTTP2Connection=0 DynamicUserGroupName= X-Forwarded-ForIP= SourceDeviceCategory=X-Phone SourceDeviceProfile=x-profile SourceDeviceModel=Redmi SourceDeviceVendor=Xiaomi SourceDeviceOSFamily=5 Plus SourceDeviceOSVersion=Android v8.2 SourceDeviceHost=pan-603 SourceDeviceMac=645701225660 DestinationDeviceCategory=X-Phone DestinationDeviceProfile=x-profile DestinationDeviceModel=MI DestinationDeviceVendor=Xiaomi DestinationDeviceOSFamily=A1 DestinationDeviceOSVersion=Android v9.1 DestinationDeviceHost=pan-622 DestinationDeviceMac=207974153661 ContainerID=1873cc5c-0d31 ContainerNameSpace=pns_default ContainerName=pan-dp-77754f4 SourceEDL= DestinationEDL= HostID=1010101010 EndpointSerialNumber=xxxxxxxxxxxxxx SourceDynamicAddressGroup= DestinationDynamicAddressGroup= TimeGeneratedHighResolution=2021-09-21T01:51:58.764000Z NSSAINetworkSliceType=cf devTimeFormat=YYYY-MM-DD'T'HH:mm:ss.SSSZ 

 The following table identifies the URL field names that the Log Forwarding app
 uses when you forward logs using the LEEF log format.

When you 

create a syslog forwarding profile 
 ,
you can optionally create a profile token that the Log
Forwarding app uses when it sends logs to the syslog server. If you configure a profile token,
it appears in the log line immediately after the log type information (for example,
 TRAFFIC , THREAT ,
 HIPMATCH , and so forth). The token will appear on 
a parameter called profileToken .

 LEEF Name

 Query Name

 Field Type

 Action

 action.​value 

 Custom

 Application

 app 

 Custom

 ApplicationCategory

 app_category 

 Custom

 ApplicationSubcategory

 app_sub_category 

 Custom

 CloudHostname

 cloud_hostname 

 Custom

 CloudReportID

 cloud_reportid 

 Custom

 ConfigVersion

 config_version.​value 

 Custom

 ContainerID

 container_id 

 Custom

 ApplicationContainer

 container_of_app 

 Custom

 ContentType

 content_type 

 Custom

 ContentVersion

 content_version 

 Custom

 RepeatCount

 count_of_repeats 

 Custom

 CortexDataLakeTenantID

 customer_id 

 Custom

 DestinationDeviceCategory

 dest_device_category 

 Custom

 DestinationDeviceClass

 dest_device_class 

 Custom

 DestinationDeviceHost

 dest_device_host 

 Custom

 DestinationDeviceMac

 dest_device_mac 

 Custom

 DestinationDeviceModel

 dest_device_model 

 Custom

 DestinationDeviceOS

 dest_device_os 

 Custom

 DestinationDeviceOSFamily

 dest_device_osfamily 

 Custom

 DestinationDeviceOSVersion

 dest_device_osversion 

 Custom

 DestinationDeviceProfile

 dest_device_profile 

 Custom

 DestinationDeviceVendor

 dest_device_vendor 

 Custom

 DestinationDynamicAddressGroup

 dest_dynamic_address_group 

 Custom

 DestinationEDL

 dest_edl 

 Custom

 dst

 dest_ip.​value 

 Predefined

 DestinationLocation

 dest_location 

 Custom

 dstPort

 dest_port 

 Predefined

 DestinationUser

 dest_user 

 Custom

 DestinationUserInfoDomain

 dest_user_info.​domain 

 Custom

 DestinationUserInfoName

 dest_user_info.​name 

 Custom

 DestinationUserInfoUUID

 dest_user_info.​uuid 

 Custom

 DestinationUUID

 dest_uuid 

 Custom

 DGHierarchyLevel1

 dg_hier_level_1 

 Custom

 DGHierarchyLevel2

 dg_hier_level_2 

 Custom

 DGHierarchyLevel3

 dg_hier_level_3 

 Custom

 DGHierarchyLevel4

 dg_hier_level_4 

 Custom

 DirectionOfAttack

 direction_of_attack.​value 

 Custom

 DynamicUserGroupName

 dynusergroup_name 

 Custom

 EndpointSerialNumber

 endpoint_serial_number 

 Custom

 FileURL

 file_url 

 Custom

 FlowType

 flow_type.​value 

 Custom

 FromZone

 from_zone 

 Custom

 HostID

 gp_host_id 

 Custom

 HTTP2Connection

 http2_connection 

 Custom

 HTTPHeaders

 http_headers 

 Custom

 HTTPMethod

 http_method.​value 

 Custom

 InboundInterface

 inbound_if.​value 

 Custom

 InboundInterfaceDetailsPort

 inbound_if_details.​port 

 Custom

 InboundInterfaceDetailsSlot

 inbound_if_details.​slot 

 Custom

 InboundInterfaceDetailsType

 inbound_if_details.​type.​value 

 Custom

 InboundInterfaceDetailsUnit

 inbound_if_details.​unit 

 Custom

 InlineMLVerdict

 inline_ml_verdict.​value 

 Custom

 CaptivePortal

 is_captive_portal 

 Custom

 IsClienttoServer

 is_client_to_server 

 Custom

 IsContainer

 is_container 

 Custom

 IsDecryptMirror

 is_decrypt_mirror 

 Custom

 IsDecrypted

 is_decrypted 

 Custom

 IsDuplicateLog

 is_dup_log 

 Custom

 IsEncrypted

 is_encrypted 

 Custom

 LogExported

 is_exported 

 Custom

 LogForwarded

 is_forwarded 

 Custom

 IsIPV6

 is_ipv6 

 Custom

 IsMptcpOn

 is_mptcp_on 

 Custom

 NAT

 is_nat 

 Custom

 IsNonStandardDestinationPort

 is_non_std_dest_port 

 Custom

 IsPacketCapture

 is_packet_capture 

 Custom

 IsPhishing

 is_phishing 

 Custom

 IsPrismaNetwork

 is_prisma_branch 

 Custom

 IsPrismaUsers

 is_prisma_mobile 

 Custom

 IsProxy

 is_proxy 

 Custom

 IsReconExcluded

 is_recon_excluded 

 Custom

 IsSaaSApplication

 is_saas_app 

 Custom

 IsServertoClient

 is_server_to_client 

 Custom

 IsSourceXForwarded

 is_source_x_fwded 

 Custom

 IsSystemReturn

 is_sym_return 

 Custom

 IsTransaction

 is_transaction 

 Custom

 IsTunnelInspected

 is_tunnel_inspected 

 Custom

 IsURLDenied

 is_url_denied 

 Custom

 K8SClusterID

 k8s_cluster_id 

 Custom

 Location

 location 

 Custom

 LogSetting

 log_set 

 Custom

 LogSource

 log_source 

 Custom

 LogSourceGroupID

 log_source_group_id 

 Custom

 DeviceSN

 log_source_id 

 Custom

 DeviceName

 log_source_name 

 Custom

 LogSourceTimeZoneOffset

 log_source_tz_offset 

 Custom

 TimeReceived

 log_time 

 Custom

 cat

 log_type.​value 

 Predefined

 IMEI

 monitor_tag_imei 

 Custom

 dstPostNAT

 nat_dest.​value 

 Predefined

 dstPostNATPort

 nat_dest_port 

 Predefined

 srcPostNAT

 nat_source.​value 

 Predefined

 srcPostNATPort

 nat_source_port 

 Predefined

 NonStandardDestinationPort

 non_standard_dest_port 

 Custom

 NSSAINetworkSliceType

 nssai_network_slice_type.​value 

 Custom

 OutboundInterface

 outbound_if.​value 

 Custom

 OutboundInterfaceDetailsPort

 outbound_if_details.​port 

 Custom

 OutboundInterfaceDetailsSlot

 outbound_if_details.​slot 

 Custom

 OutboundInterfaceDetailsType

 outbound_if_details.​type.​value 

 Custom

 OutboundInterfaceDetailsUnit

 outbound_if_details.​unit 

 Custom

 PanoramaSN

 panorama_serial 

 Custom

 ParentSessionID

 parent_session_id 

 Custom

 ParentStarttime

 parent_start_time 

 Custom

 Packet

 pcap 

 Custom

 PacketID

 pcap_id 

 Custom

 PlatformType

 platform_type 

 Custom

 ContainerName

 pod_name 

 Custom

 ContainerNameSpace

 pod_namespace 

 Custom

 proto

 protocol.​value 

 Predefined

 Referer

 referer 

 Custom

 HTTPRefererFQDN

 referer_fqdn 

 Custom

 HTTPRefererPort

 referer_port 

 Custom

 HTTPRefererProtocol

 referer_protocol.​value 

 Custom

 HTTPRefererURLPath

 referer_url_path 

 Custom

 ApplicationRisk

 risk_of_app 

 Custom

 Rule

 rule_matched 

 Custom

 RuleUUID

 rule_matched_uuid 

 Custom

 SanctionedStateofApp

 sanctioned_state_of_app 

 Custom

 SequenceNo

 sequence_no 

 Custom

 SessionID

 session_id 

 Custom

 Severity

 severity 

 Custom

 SigFlags

 sig_flags 

 Custom

 SourceDeviceCategory

 source_device_category 

 Custom

 SourceDeviceClass

 source_device_class 

 Custom

 SourceDeviceHost

 source_device_host 

 Custom

 SourceDeviceMac

 source_device_mac 

 Custom

 SourceDeviceModel

 source_device_model 

 Custom

 SourceDeviceOS

 source_device_os 

 Custom

 SourceDeviceOSFamily

 source_device_osfamily 

 Custom

 SourceDeviceOSVersion

 source_device_osversion 

 Custom

 SourceDeviceProfile

 source_device_profile 

 Custom

 SourceDeviceVendor

 source_device_vendor 

 Custom

 SourceDynamicAddressGroup

 source_dynamic_address_group 

 Custom

 SourceEDL

 source_edl 

 Custom

 src

 source_ip.​value 

 Predefined

 SourceLocation

 source_location 

 Custom

 srcPort

 source_port 

 Predefined

 usrName

 source_user 

 Predefined

 SourceUserInfoDomain

 source_user_info.​domain 

 Custom

 SourceUserInfoName

 source_user_info.​name 

 Custom

 SourceUserInfoUUID

 source_user_info.​uuid 

 Custom

 SourceUUID

 source_uuid 

 Custom

 SubType

 sub_type.​value 

 Custom

 ApplicationTechnology

 technology_of_app 

 Custom

 devTime

 time_generated 

 Predefined

 TimeGeneratedHighResolution

 time_generated_high_res 

 Custom

 ToZone

 to_zone 

 Custom

 Tunnel

 tunnel.​value 

 Custom

 TunneledApplication

 tunneled_app 

 Custom

 IMSI

 tunnelid_imsi 

 Custom

 URL

 uri 

 Custom

 EventID

 url_category.​value 

 Header

 URLCategoryList

 url_category_list 

 Custom

 URLDomain

 url_domain 

 Custom

 URLCounter

 url_idx 

 Custom

 UserAgent

 user_agent 

 Custom

 Users

 users 

 Custom

 Vendor

 vendor_name 

 Header

 VendorSeverity

 vendor_severity.​value 

 Custom

 VirtualLocation

 vsys 

 Custom

 VirtualSystemID

 vsys_id 

 Custom

 VirtualSystemName

 vsys_name 

 Custom

 identSrc

 xff 

 Predefined

 X-Forwarded-ForIP

 xff_ip.​value 

 Custom

 Previous 

 URL HTTPS Fields 

 Next 

 UserID 

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
