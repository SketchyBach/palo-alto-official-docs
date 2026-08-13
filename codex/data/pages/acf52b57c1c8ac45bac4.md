---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/endpoint-logs/endpoint-gp-troubleshoot-log/endpoint-gp-troubleshoot-cef-fields
fetched_at: 2026-08-13T17:40:12Z
source: palo-alto-main
---

# GlobalProtect App Troubleshooting CEF Fields Clear

GlobalProtect App Troubleshooting CEF Fields 

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

 GlobalProtect App Troubleshooting CEF Fields 

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

 GlobalProtect App Troubleshooting 

 GlobalProtect App Troubleshooting CEF Fields 

 Download PDF 

 Strata Logging Service 

 GlobalProtect App Troubleshooting CEF Fields 

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

 GlobalProtect App Troubleshooting Syslog Default Field Order 

 Next 

 GlobalProtect App Troubleshooting EMAIL Fields 

 GlobalProtect App Troubleshooting CEF Fields 

 The following table identifies the GlobalProtect App Troubleshooting field names that the Log Forwarding app
 uses when you forward logs using the CEF log format.

 CEF Name

 Field Details

 PanOSAppTampered

 Query Name: app_tampered 

 Header Type: Custom 

 PanOSCaptivePortal

 Query Name: captive_portal 

 Header Type: Custom 

 PanOSCPUUsage

 Query Name: cpu_usage 

 Header Type: Custom 

 PanOSGlobalProtectCPUUsage

 Query Name: cpu_usage_gp 

 Header Type: Custom 

 PanOSCrashHistory

 Query Name: crash_history 

 Header Type: Custom 

 PanOSDebugLogFile

 Query Name: debug_log_file_name 

 Header Type: Custom 

 PanOSDisableHistory

 Query Name: disable_history 

 Header Type: Custom 

 PanOSDiskAvailable

 Query Name: disk_available 

 Header Type: Custom 

 PanOSTotalDiskSpace

 Query Name: disk_total 

 Header Type: Custom 

 PanOSDNSReachable

 Query Name: dns_reachable 

 Header Type: Custom 

 PanOSDualStackTunnelInterface

 Query Name: dual_stack_network 

 Header Type: Custom 

 PanOSEnforcerStatus

 Query Name: enforcer_status 

 Header Type: Custom 

 reason

 Query Name: error 

 Header Type: Predefined 

 Max Length: 1023 

 PanOSErrorDetails

 Query Name: error_details 

 Header Type: Custom 

 PanOSErrorStage

 Query Name: error_stage 

 Header Type: Custom 

 start

 Query Name: error_time 

 Header Type: Predefined 

 PanOSGlobalProtectMTU

 Query Name: gp_mtu 

 Header Type: Custom 

 PanOSGlobalProtectVersion

 Query Name: gp_version 

 Header Type: Custom 

 PanOSGatewayAddress

 Query Name: gw_address 

 Header Type: Custom 

 PanOSAttemptedGateways

 Query Name: gw_attempted 

 Header Type: Custom 

 PanOSGatewayAuthentication

 Query Name: gw_auth 

 Header Type: Custom 

 PanOSGatewayConfigurationName

 Query Name: gw_config_name 

 Header Type: Custom 

 PanOSDLSAstatus

 Query Name: gw_dlsa_enabled 

 Header Type: Custom 

 PanOSFallbacktoSSLReason

 Query Name: gw_fall_back_to_ssl 

 Header Type: Custom 

 PanOSIPSecEnabled

 Query Name: gw_ipsec_enabled 

 Header Type: Custom 

 PanOSIPSecFailureReason

 Query Name: gw_ipsec_failure_reason 

 Header Type: Custom 

 PanOSJitter

 Query Name: gw_jitter 

 Header Type: Custom 

 PanOSLatency

 Query Name: gw_latency 

 Header Type: Custom 

 PanOSLocation

 Query Name: gw_location 

 Header Type: Custom 

 PanOSGatewayLogoutTime

 Query Name: gw_logout_time 

 Header Type: Custom 

 PanOSPacketLoss

 Query Name: gw_packet_loss 

 Header Type: Custom 

 PanOSGatewayReachable

 Query Name: gw_reachable 

 Header Type: Custom 

 PanOSGatewaySSLCertificateValid

 Query Name: gw_server_cert 

 Header Type: Custom 

 PanOSSSLFailureReason

 Query Name: gw_ssl_failure_reason 

 Header Type: Custom 

 PanOSGatewayStatus

 Query Name: gw_status 

 Header Type: Custom 

 PanOSTunnelRename

 Query Name: gw_tunnel_renamed 

 Header Type: Custom 

 PanOSPrivileges

 Query Name: has_privileges 

 Header Type: Custom 

 dtz

 Query Name: host_gmt_timeoffset 

 Header Type: Predefined 

 Max Length: 255 

 PanOSHostID

 Query Name: host_id 

 Header Type: Custom 

 dvchost

 Query Name: host_name 

 Header Type: Predefined 

 Max Length: 100 

 PanOSInstallHistory

 Query Name: install_history 

 Header Type: Custom 

 PanOSInternalNetwork

 Query Name: internal_network 

 Header Type: Custom 

 PanOSInternetAccess

 Query Name: internet_access 

 Header Type: Custom 

 PanOSJailbrokenStatus

 Query Name: jail_broken 

 Header Type: Custom 

 PanOSLastHIPReportTime

 Query Name: last_hip_report_time 

 Header Type: Custom 

 PanOSLastLogoutTime

 Query Name: last_logout_time 

 Header Type: Custom 

 PanOSLocale

 Query Name: locale 

 Header Type: Custom 

 Device Event Class ID

 Query Name: log_type.​value 

 Header Type: Custom 

 PanOSTotalMemory

 Query Name: memory_total 

 Header Type: Custom 

 PanOSMemoryUsage

 Query Name: memory_usage 

 Header Type: Custom 

 PanOSGlobalProtectMemoryUsage

 Query Name: memory_usage_gp 

 Header Type: Custom 

 PanOSNetworkAccess

 Query Name: network_access 

 Header Type: Custom 

 PanOSPortalGatewayLatency

 Query Name: network_latency 

 Header Type: Custom 

 PanOSType

 Query Name: network_type 

 Header Type: Custom 

 PanOSOperatingSystem

 Query Name: os 

 Header Type: Custom 

 PanOSPanoramaSN

 Query Name: panorama_serial 

 Header Type: Custom 

 PanOSPortalAddress

 Query Name: portal_address 

 Header Type: Custom 

 PanOSPortalAuthentication

 Query Name: portal_auth 

 Header Type: Custom 

 PanOSCachedConfiguration

 Query Name: portal_cached_config 

 Header Type: Custom 

 PanOSPortalConfigurationName

 Query Name: portal_config_name 

 Header Type: Custom 

 PanOSConfigurationRefresh

 Query Name: portal_config_refresh 

 Header Type: Custom 

 flexDate1

 Query Name: portal_last_connect_time 

 Header Type: Predefined 

 Label: flexDate1Label 

 Label Text: Last Connect Time 

 PanOSPortalReachable

 Query Name: portal_reachable 

 Header Type: Custom 

 PanOSPortalSSLCertificateValid

 Query Name: portal_server_cert 

 Header Type: Custom 

 PanOSPortalStatus

 Query Name: portal_status 

 Header Type: Custom 

 PanOSProxyServer

 Query Name: proxy_server 

 Header Type: Custom 

 rt

 Query Name: report_id 

 Header Type: Predefined 

 PanOSReportID

 Query Name: report_time 

 Header Type: Custom 

 Name

 Query Name: report_type 

 Header Type: Custom 

 deviceExternalId

 Query Name: serial_number 

 Header Type: Predefined 

 Max Length: 255 

 PanOSServerPerformance

 Query Name: server_performance 

 Header Type: Custom 

 PanOSSplit-tunnelconfiguration

 Query Name: split_tunnel_status 

 Header Type: Custom 

 PanOSUserComment

 Query Name: user_comment 

 Header Type: Custom 

 PanOSUsername

 Query Name: user_name 

 Header Type: Custom 

 Previous 

 GlobalProtect App Troubleshooting Syslog Default Field Order 

 Next 

 GlobalProtect App Troubleshooting EMAIL Fields 

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
