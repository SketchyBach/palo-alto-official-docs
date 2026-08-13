---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/endpoint-logs/endpoint-agent-log
fetched_at: 2026-08-13T17:40:07Z
source: palo-alto-main
---

# Troubleshooting (Prisma Access Agent) Clear

Troubleshooting (Prisma Access Agent) 

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

 Troubleshooting (Prisma Access Agent) 

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

 Troubleshooting (Prisma Access Agent) 

 Download PDF 

 Strata Logging Service 

 Troubleshooting (Prisma Access Agent) 

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

 Management LEEF Fields 

 Next 

 Troubleshooting (Prisma Access Agent) Syslog Default Field Order 

 Troubleshooting (Prisma Access Agent) 

 Prisma Access Agent troubleshooting logs contain information about any activity or
 action performed by a user on the Prisma Access Agent. 

 See the following for information related to supported log formats: 

 Troubleshooting (Prisma Access Agent) Syslog Default Field Order 

 Troubleshooting (Prisma Access Agent) CEF Fields 

 Troubleshooting (Prisma Access Agent) EMAIL Fields 

 Troubleshooting (Prisma Access Agent) HTTPS Fields 

 Troubleshooting (Prisma Access Agent) LEEF Fields 

 TROUBLESHOOTING (PRISMA ACCESS AGENT) Field

 (Display Name)

 Description

 action 

 (ACTION)

 Did we block it or allow it.

 CEF field name: PanOSAction 

 EMAIL field name: Action 

 HTTPS field name: Action 

 LEEF field name: Action 

 attempted_gateways 

 (ATTEMPTED GATEWAYS)

 String of all gateways that were available and attempted for the client location. Contains gateway name, ssl response time, and priority, separated by a semicolon.

 CEF field name: PanOSAttemptedGateways 

 EMAIL field name: AttemptedGateways 

 HTTPS field name: AttemptedGateways 

 LEEF field name: AttemptedGateways 

 auth_method 

 (AUTH METHOD)

 Authentication method used for the agent connection.

 CEF field name: PanOSAuthMethod 

 EMAIL field name: AuthMethod 

 HTTPS field name: AuthMethod 

 LEEF field name: AuthMethod 

 cloud_reportid 

 (CLOUD REPORT ID)

 System generated Id to know the unique report.

 CEF field name: PanOSCloudReportID 

 EMAIL field name: CloudReportID 

 HTTPS field name: CloudReportID 

 LEEF field name: CloudReportID 

 config_version.​value 

 (CONFIG VERSION)

 Config version converted to string represented as major.minor.patch.build in value and as hex in id.

 CEF field name: PanOSConfigVersion 

 EMAIL field name: ConfigVersion 

 HTTPS field name: ConfigVersion 

 LEEF field name: ConfigVersion 

 connect_method 

 (CONNECTION METHOD)

 .

 CEF field name: PanOSConnectionMethod 

 EMAIL field name: ConnectionMethod 

 HTTPS field name: ConnectionMethod 

 LEEF field name: ConnectionMethod 

 connection_error.​id 

 (CONNECTION ERROR ID)

 Enumeration integer assigned to the connection_error field value.

 CEF field name: PanOSConnectionErrorID 

 EMAIL field name: ConnectionErrorID 

 HTTPS field name: ConnectionErrorID 

 LEEF field name: ConnectionErrorID 

 connection_error.​value 

 (CONNECTION ERROR)

 Error information for unsuccessful connection.

 CEF field name: PanOSConnectionError 

 EMAIL field name: ConnectionError 

 HTTPS field name: ConnectionError 

 LEEF field name: ConnectionError 

 count_of_repeats 

 (COUNT OF REPEATS)

 Number of sessions with same Source IP, Destination IP, Application, and Content/Threat Type seen for the summary interval.

 CEF field name: PanOSCountOfRepeats 

 EMAIL field name: CountOfRepeats 

 HTTPS field name: CountOfRepeats 

 LEEF field name: CountOfRepeats 

 customer_id 

 (TENANT ID)

 The ID that uniquely identifies the Cortex Data Lake instance which received this log record.

 CEF field name: PanOSTenantID 

 EMAIL field name: TenantID 

 HTTPS field name: TenantID 

 LEEF field name: TenantID 

 data_profile_name 

 (DATA PROFILE NAME)

 Name of the Data Profile.

 CEF field name: PanOSDataProfileName 

 EMAIL field name: DataProfileName 

 HTTPS field name: DataProfileName 

 LEEF field name: DataProfileName 

 dest_type.​value 

 (DESTINATION TYPE)

 Destination type USB/Printer/Network Share.

 CEF field name: PanOSDestType 

 EMAIL field name: DestType 

 HTTPS field name: DestType 

 LEEF field name: DestType 

 dg_hier_level_1 

 (DG HIERARCHY LEVEL 1)

 A sequence of identification numbers that indicate the device groupâ€™s location within a device group hierarchy.

 CEF field name: PanOSDGHierarchyLevel1 

 EMAIL field name: DGHierarchyLevel1 

 HTTPS field name: DGHierarchyLevel1 

 LEEF field name: DGHierarchyLevel1 

 dg_hier_level_2 

 (DG HIERARCHY LEVEL 2)

 A sequence of identification numbers that indicate the device groupâ€™s location within a device group hierarchy.

 CEF field name: PanOSDGHierarchyLevel2 

 EMAIL field name: DGHierarchyLevel2 

 HTTPS field name: DGHierarchyLevel2 

 LEEF field name: DGHierarchyLevel2 

 dg_hier_level_3 

 (DG HIERARCHY LEVEL 3)

 A sequence of identification numbers that indicate the device groupâ€™s location within a device group hierarchy.

 CEF field name: PanOSDGHierarchyLevel3 

 EMAIL field name: DGHierarchyLevel3 

 HTTPS field name: DGHierarchyLevel3 

 LEEF field name: DGHierarchyLevel3 

 dg_hier_level_4 

 (DG HIERARCHY LEVEL 4)

 A sequence of identification numbers that indicate the device groupâ€™s location within a device group hierarchy.

 CEF field name: PanOSDGHierarchyLevel4 

 EMAIL field name: DGHierarchyLevel4 

 HTTPS field name: DGHierarchyLevel4 

 LEEF field name: DGHierarchyLevel4 

 dlp_client_version 

 (DLP CLIENT VERSION)

 DLP version on ztna agent.

 CEF field name: PanOSDLPClientVersion 

 EMAIL field name: DLPClientVersion 

 HTTPS field name: DLPClientVersion 

 LEEF field name: DLPClientVersion 

 endpoint_device_name 

 (ENDPOINT DEVICE NAME)

 Name of the device that the user used for the connection.

 CEF field name: shost 

 EMAIL field name: EndpointDeviceName 

 HTTPS field name: EndpointDeviceName 

 LEEF field name: EndpointDeviceName 

 endpoint_gp_version 

 (PRISMA ACCESS AGENT CLIENT VERSION)

 agent client version number.

 CEF field name: PanOSZTNAClientVersion 

 EMAIL field name: ZTNAClientVersion 

 HTTPS field name: ZTNAClientVersion 

 LEEF field name: ZTNAClientVersion 

 endpoint_os_type 

 (ENDPOINT OS TYPE)

 OS type of the endpoint on which the agent client is deployed.

 CEF field name: PanOSEndpointOSType 

 EMAIL field name: EndpointOSType 

 HTTPS field name: EndpointOSType 

 LEEF field name: EndpointOSType 

 endpoint_os_version 

 (ENDPOINT OS VERSION)

 OS version of the endpoint on which the agent client is deployed.

 CEF field name: PanOSEndpointOSVersion 

 EMAIL field name: EndpointOSVersion 

 HTTPS field name: EndpointOSVersion 

 LEEF field name: EndpointOSVersion 

 endpoint_serial_number 

 (ENDPOINT SN)

 ID that uniquely identifies the endpoint on which the agent client is deployed.

 CEF field name: PanOSEndpointSN 

 EMAIL field name: EndpointSN 

 HTTPS field name: EndpointSN 

 LEEF field name: EndpointSN 

 event_id.​value 

 (EVENT ID VALUE)

 .

 CEF field name: Name 

 EMAIL field name: EventIDValue 

 HTTPS field name: EventIDValue 

 LEEF field name: EventID 

 file_name 

 (FILE NAME)

 File Name.

 CEF field name: fname 

 EMAIL field name: FileName 

 HTTPS field name: FileName 

 LEEF field name: FileName 

 file_sha_256 

 (FILE HASH)

 File Sha 256.

 CEF field name: fileHash 

 EMAIL field name: FileSHA256 

 HTTPS field name: FileSHA256 

 LEEF field name: FileSHA256 

 file_size 

 (FILE SIZE )

 Size of the file uploaded.

 CEF field name: fsize 

 EMAIL field name: FileSize 

 HTTPS field name: FileSize 

 LEEF field name: FileSize 

 gateway 

 (GATEWAY)

 Selected Gateway for the connection.

 CEF field name: PanOSGateway 

 EMAIL field name: Gateway 

 HTTPS field name: Gateway 

 LEEF field name: Gateway 

 gateway_priority.​value 

 (GATEWAY PRIORITY)

 Priority of gateway, retrieved from portal configuration.

 CEF field name: PanOSGatewayPriority 

 EMAIL field name: GatewayPriority 

 HTTPS field name: GatewayPriority 

 LEEF field name: GatewayPriority 

 gateway_selection_type 

 (GATEWAY SELECTION TYPE)

 Gateway Selection Method i.e automatic, preferred or manual.

 CEF field name: PanOSGatewaySelectionType 

 EMAIL field name: GatewaySelectionType 

 HTTPS field name: GatewaySelectionType 

 LEEF field name: GatewaySelectionType 

 gpg_location 

 (PRISMA ACCESS AGENT GATEWAY LOCATION)

 Location of the agent Gateway.

 CEF field name: PanOSZTNAGatewayLocation 

 EMAIL field name: ZTNAGatewayLocation 

 HTTPS field name: ZTNAGatewayLocation 

 LEEF field name: ZTNAGatewayLocation 

 host_id 

 (HOST ID)

 .

 CEF field name: PanOSHostID 

 EMAIL field name: HostID 

 HTTPS field name: HostID 

 LEEF field name: HostID 

 incident_id 

 (INCIDENT ID)

 Unique Id to identify the incident.

 CEF field name: PanOSIncidentID 

 EMAIL field name: IncidentID 

 HTTPS field name: IncidentID 

 LEEF field name: IncidentID 

 is_dup_log 

 (IS DUPLICATE LOG)

 Indicates whether this log data is available in multiple locations, such as from Cortex Data Lake as well as from an on-premise log collector.

 CEF field name: PanOSIsDuplicateLog 

 EMAIL field name: IsDuplicateLog 

 HTTPS field name: IsDuplicateLog 

 LEEF field name: IsDuplicateLog 

 is_exported 

 (LOG EXPORTED)

 Indicates if this log was exported from the agent using the agent's log export function.

 CEF field name: PanOSLogExported 

 EMAIL field name: LogExported 

 HTTPS field name: LogExported 

 LEEF field name: LogExported 

 is_forwarded 

 (LOG FORWARDED)

 Internal-use field that indicates if the log is being forwarded.

 CEF field name: PanOSLogForwarded 

 EMAIL field name: LogForwarded 

 HTTPS field name: LogForwarded 

 LEEF field name: LogForwarded 

 is_prisma_branch 

 (IS PRISMA NETWORKS)

 Internal-use field. If set to 1, the log was generated on a cloud-based agent. If 0, the agent was running on-premise.

 CEF field name: PanOSIsPrismaNetworks 

 EMAIL field name: IsPrismaNetworks 

 HTTPS field name: IsPrismaNetworks 

 LEEF field name: IsPrismaNetworks 

 is_prisma_mobile 

 (IS PRISMA USERS)

 Internal use field. If set to 1, the log record was generated using a cloud-based agent instance. If 0, agent was hosted on-premise.

 CEF field name: PanOSIsPrismaUsers 

 EMAIL field name: IsPrismaUsers 

 HTTPS field name: IsPrismaUsers 

 LEEF field name: IsPrismaUsers 

 log_source 

 (LOG SOURCE)

 Identifies the origin of the data. That is, the system that produced the data.

 CEF field name: sourceServiceName 

 EMAIL field name: LogSource 

 HTTPS field name: LogSource 

 LEEF field name: LogSource 

 log_source_group_id 

 (LOG SOURCE GROUP ID)

 ID that uniquely identifies the logSourceGroupId of the log. That is, the log_source_id of the group.

 CEF field name: LogSourceGroupID 

 EMAIL field name: LogSourceGroupID 

 HTTPS field name: LogSourceGroupID 

 LEEF field name: LogSourceGroupID 

 log_source_id 

 (DEVICE SN)

 ID that uniquely identifies the source of the log. That is, the serial number of the agent that generated the log.

 CEF field name: deviceExternalID 

 EMAIL field name: DeviceSN 

 HTTPS field name: DeviceSN 

 LEEF field name: DeviceSN 

 log_source_name 

 (DEVICE NAME)

 Name of the source of the log. That is, the hostname of the agent that logged the network traffic.

 CEF field name: dvchost 

 EMAIL field name: DeviceName 

 HTTPS field name: DeviceName 

 LEEF field name: DeviceName 

 log_source_tz_offset 

 (LOG SOURCE TIMEZONE OFFSET)

 Time Zone offset from GMT of the source of the log.

 CEF field name: PanOSLogSourceTimeZoneOffset 

 EMAIL field name: LogSourceTimeZoneOffset 

 HTTPS field name: LogSourceTimeZoneOffset 

 LEEF field name: LogSourceTimeZoneOffset 

 log_time 

 (TIME RECEIVED)

 Time the log was received in Cortex Data Lake. This is populated by the platform.

 CEF field name: rt 

 EMAIL field name: TimeReceived 

 HTTPS field name: TimeReceived 

 LEEF field name: TimeReceived 

 log_type.​value 

 (LOG TYPE)

 Identifies the log type.

 CEF field name: Device Event Class ID 

 EMAIL field name: LogType 

 HTTPS field name: LogType 

 LEEF field name: cat 

 login_duration 

 (LOGIN DURATION)

 Duration for which the connected user was logged on.

 CEF field name: PanOSLoginDuration 

 EMAIL field name: LoginDuration 

 HTTPS field name: LoginDuration 

 LEEF field name: LoginDuration 

 opaque 

 (DESCRIPTION)

 Description of the event (extra information not captured in other fields around an event).

 CEF field name: PanOSDescription 

 EMAIL field name: Description 

 HTTPS field name: Description 

 LEEF field name: Description 

 panorama_serial 

 (PANORAMA SN)

 Panorama Serial associated with CDL.

 CEF field name: PanOSPanoramaSN 

 EMAIL field name: PanoramaSN 

 HTTPS field name: PanoramaSN 

 LEEF field name: PanoramaSN 

 peripheral_attributes 

 (PERIPHERAL ATTRIBUTES)

 All values about peripheral: IP, USB device details, printer details.

 CEF field name: PanOSPeripheralAttributes 

 EMAIL field name: PeripheralAttributes 

 HTTPS field name: PeripheralAttributes 

 LEEF field name: PeripheralAttributes 

 peripheral_id 

 (PERIPHERAL ID)

 Unique Id to identify the peripheral device.

 CEF field name: PanOSPeripheralID 

 EMAIL field name: PeripheralID 

 HTTPS field name: PeripheralID 

 LEEF field name: PeripheralID 

 platform_type 

 (PLATFORM TYPE)

 The platform type (Valid types are VM, PA, NGFW, CNGFW).

 CEF field name: PlatformType 

 EMAIL field name: PlatformType 

 HTTPS field name: PlatformType 

 LEEF field name: PlatformType 

 policy_id 

 (POLICY ID)

 Policy ID.

 CEF field name: PanOSPolicyID 

 EMAIL field name: PolicyID 

 HTTPS field name: PolicyID 

 LEEF field name: PolicyID 

 policy_name 

 (POLICY NAME)

 Name of the policy.

 CEF field name: PanOSPolicyName 

 EMAIL field name: PolicyName 

 HTTPS field name: PolicyName 

 LEEF field name: PolicyName 

 policy_type 

 (POLICY TYPE)

 Defines types of policy - Data in Motion, Peripheral.

 CEF field name: PanOSPolicyType 

 EMAIL field name: PolicyType 

 HTTPS field name: PolicyType 

 LEEF field name: PolicyType 

 policy_version 

 (POLICY VERSION)

 Policy version.

 CEF field name: PanOSPolicyVersion 

 EMAIL field name: PolicyVersion 

 HTTPS field name: PolicyVersion 

 LEEF field name: PolicyVersion 

 portal 

 (PORTAL)

 agent Portal or Gateway that the user connected to.

 CEF field name: PanOSPortal 

 EMAIL field name: Portal 

 HTTPS field name: Portal 

 LEEF field name: Portal 

 private_ip.​value 

 (PRIVATE IPV4)

 Private IP address (v4) of the user that connected.

 CEF field name: PanOSPrivateIPv4 

 EMAIL field name: PrivateIPv4 

 HTTPS field name: PrivateIPv4 

 LEEF field name: PrivateIPv4 

 private_ipv6.​value 

 (PRIVATE IPV6)

 Private IP address (v6) of the user that connected.

 CEF field name: PanOSPrivateIPv6 

 EMAIL field name: PrivateIPv6 

 HTTPS field name: PrivateIPv6 

 LEEF field name: PrivateIPv6 

 project_name 

 (PROJECT NAME)

 Indicates the customers project name.

 CEF field name: ProjectName 

 EMAIL field name: ProjectName 

 HTTPS field name: ProjectName 

 LEEF field name: ProjectName 

 public_ip.​value 

 (PUBLIC IPV4)

 Public IP address (v4) of the user that connected.

 CEF field name: src 

 EMAIL field name: PublicIPv4 

 HTTPS field name: PublicIPv4 

 LEEF field name: PublicIPv4 

 public_ipv6.​value 

 (PUBLIC IPV6)

 Public IP address (v6) of the user that connected.

 CEF field name: c6a2 

 EMAIL field name: PublicIPv6 

 HTTPS field name: PublicIPv6 

 LEEF field name: PublicIPv6 

 quarantine_reason 

 (QUARANTINE REASON)

 Quarantine reason.

 CEF field name: PanOSQuarantineReason 

 EMAIL field name: QuarantineReason 

 HTTPS field name: QuarantineReason 

 LEEF field name: QuarantineReason 

 reason_policy 

 (REASON FOR POLICY ACTION)

 Reason behing the action taken.

 CEF field name: PanOSReasonPolicy 

 EMAIL field name: ReasonPolicy 

 HTTPS field name: ReasonPolicy 

 LEEF field name: ReasonPolicy 

 sequence_no 

 (SEQUENCE NO)

 The log entry identifier, which is incremented sequentially. Each log type has a unique number space.

 CEF field name: PanOSSequenceNo 

 EMAIL field name: SequenceNo 

 HTTPS field name: SequenceNo 

 LEEF field name: SequenceNo 

 severity.​value 

 (SEVERITY)

 High/low/medium/critical.

 CEF field name: PanOSSeverity 

 EMAIL field name: Severity 

 HTTPS field name: Severity 

 LEEF field name: Severity 

 source_region 

 (SOURCE REGION)

 Region of the Gateway (or User) that connected.

 CEF field name: PanOSSourceRegion 

 EMAIL field name: SourceRegion 

 HTTPS field name: SourceRegion 

 LEEF field name: SourceRegion 

 source_user 

 (SOURCE USER NAME)

 The username that connected.

 CEF field name: suser 

 EMAIL field name: SourceUserName 

 HTTPS field name: SourceUserName 

 LEEF field name: usrName 

 source_user_info.​domain 

 (SOURCE USER DOMAIN)

 TTBD.

 CEF fields: All of the following: sntdom , dntdom 

 EMAIL field name: SourceUserInfoDomain 

 HTTPS field name: SourceUserInfoDomain 

 LEEF field name: SourceUserInfoDomain 

 source_user_info.​name 

 (SOURCE USER INFO)

 TTBD.

 CEF fields: All of the following: suser , duser 

 EMAIL field name: SourceUserInfoName 

 HTTPS field name: SourceUserInfoName 

 LEEF field name: SourceUserInfoName 

 source_user_info.​uuid 

 (SOURCE USER UUID)

 TTBD.

 CEF fields: All of the following: suid , duid 

 EMAIL field name: SourceUserInfoUUID 

 HTTPS field name: SourceUserInfoUUID 

 LEEF field name: SourceUserInfoUUID 

 ssl_response_time 

 (SSL RESPONSE TIME)

 SSL Response Time in milliseconds.

 CEF field name: PanOSSSLResponseTime 

 EMAIL field name: SSLResponseTime 

 HTTPS field name: SSLResponseTime 

 LEEF field name: SSLResponseTime 

 stage 

 (STAGE)

 Name of the stage in the agent connection workflow.

 CEF field name: PanOSStage 

 EMAIL field name: Stage 

 HTTPS field name: Stage 

 LEEF field name: Stage 

 status.​value 

 (EVENT STATUS)

 .

 CEF field name: outcome 

 EMAIL field name: EventStatus 

 HTTPS field name: EventStatus 

 LEEF field name: EventStatus 

 sub_type.​value 

 (LOG SUBTYPE)

 Identifies the log subtype.

 CEF field name: PanOSLogSubtype 

 EMAIL field name: LogSubtype 

 HTTPS field name: LogSubtype 

 LEEF field name: SubType 

 time_generated 

 (TIME GENERATED)

 Time the log was generated on the data plane in format YYYY-MM-DDTHH:MM:SS[.DDDDDD]Z.

 CEF field name: start 

 EMAIL field name: TimeGenerated 

 HTTPS field name: TimeGenerated 

 LEEF field name: devTime 

 time_generated_high_res 

 (TIME GENERATED HIGH RESOLUTION)

 Time the log was generated in data plane with millisec granularity in format YYYY-MM-DDTHH:MM:SS[.DDDDDD]Z.

 CEF field name: PanOSTimeGeneratedHighResolution 

 EMAIL field name: TimeGeneratedHighResolution 

 HTTPS field name: TimeGeneratedHighResolution 

 LEEF field name: TimeGeneratedHighResolution 

 tunnel 

 (TUNNEL TYPE)

 Tunnel Type i.e. SSL or VPN.

 CEF field name: PanOSTunnelType 

 EMAIL field name: TunnelType 

 HTTPS field name: TunnelType 

 LEEF field name: TunnelType 

 vendor_name 

 (VENDOR NAME)

 Identifies the vendor that produced the data.

 CEF field name: Device Vendor 

 EMAIL field name: VendorName 

 HTTPS field name: VendorName 

 LEEF field name: Vendor 

 vsys 

 (VIRTUAL SYSTEM)

 String representation of the unique identifier for a virtual system on a Palo Alto Networks agent.

 CEF field name: PanOSVirtualSystem 

 EMAIL field name: VirtualSystem 

 HTTPS field name: VirtualSystem 

 LEEF field name: VirtualSystem 

 vsys_id 

 (VIRTUAL SYSTEM ID)

 A unique identifier for a virtual system on a Palo Alto Networks agent.

 CEF field name: PanOSVirtualSystemID 

 EMAIL field name: VirtualSystemID 

 HTTPS field name: VirtualSystemID 

 LEEF field name: VirtualSystemID 

 vsys_name 

 (VIRTUAL SYSTEM NAME)

 The name of the virtual system associated with the network traffic.

 CEF field name: cs3 

 EMAIL field name: VirtualSystemName 

 HTTPS field name: VirtualSystemName 

 LEEF field name: VirtualSystemName 

 Previous 

 Management LEEF Fields 

 Next 

 Troubleshooting (Prisma Access Agent) Syslog Default Field Order 

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
