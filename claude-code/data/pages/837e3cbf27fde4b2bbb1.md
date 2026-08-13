---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/endpoint-logs/endpoint-events-log/endpoint-events-leef-fields
fetched_at: 2026-08-13T17:40:13Z
source: palo-alto-main
---

# Events LEEF Fields Clear

Events LEEF Fields 

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

 Events LEEF Fields 

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

 Events 

 Events LEEF Fields 

 Download PDF 

 Strata Logging Service 

 Events LEEF Fields 

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

 Events HTTPS Fields 

 Next 

 GlobalProtect App Troubleshooting 

 Events LEEF Fields 

 The following table identifies the Events field names that the Log Forwarding app
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

 ApplicationAppCategory

 application.​app_category 

 Custom

 ApplicationAppSubcategory

 application.​app_sub_category 

 Custom

 ApplicationExternalID

 application.​external_id 

 Custom

 ApplicationExternalName

 application.​external_name 

 Custom

 ApplicationID

 application.​id 

 Custom

 ApplicationName

 application.​name 

 Custom

 ApplicationProtectedAccount

 application.​protected_account 

 Custom

 ApplicationRiskOfApp

 application.​risk_of_app 

 Custom

 ApplicationSource

 application.​source 

 Custom

 ApplicationUsername

 application.​username 

 Custom

 BatchID

 batch_id 

 Custom

 BrowserExtensionAppLaunchURL

 browser_extension.​app_launch_url 

 Custom

 BrowserExtensionAvailableLaunchTypes

 browser_extension.​available_launch_types 

 Custom

 BrowserExtensionDescription

 browser_extension.​description 

 Custom

 BrowserExtensionDisabledReason

 browser_extension.​disabled_reason 

 Custom

 BrowserExtensionEnabled

 browser_extension.​enabled 

 Custom

 BrowserExtensionHomepageURL

 browser_extension.​homepage_url 

 Custom

 BrowserExtensionHostPermissions

 browser_extension.​host_permissions 

 Custom

 BrowserExtensionID

 browser_extension.​id 

 Custom

 BrowserExtensionInstallType

 browser_extension.​install_type 

 Custom

 BrowserExtensionIsApp

 browser_extension.​is_app 

 Custom

 BrowserExtensionLaunchType

 browser_extension.​launch_type 

 Custom

 BrowserExtensionMayDisable

 browser_extension.​may_disable 

 Custom

 BrowserExtensionName

 browser_extension.​name 

 Custom

 BrowserExtensionOfflineEnabled

 browser_extension.​offline_enabled 

 Custom

 BrowserExtensionOptionsURL

 browser_extension.​options_url 

 Custom

 BrowserExtensionPermissions

 browser_extension.​permissions 

 Custom

 BrowserExtensionShortName

 browser_extension.​short_name 

 Custom

 BrowserExtensionType

 browser_extension.​type 

 Custom

 BrowserExtensionUpdateURL

 browser_extension.​update_url 

 Custom

 BrowserExtensionVersion

 browser_extension.​version 

 Custom

 CertificateCreatedTime

 certificate.​created_time 

 Custom

 CertificateExpirationTime

 certificate.​expiration_time 

 Custom

 CertificateFingerprints

 certificate.​fingerprints 

 Custom

 CertificateIssuer

 certificate.​issuer 

 Custom

 CertificateSerialNumber

 certificate.​serial_number 

 Custom

 CertificateSubject

 certificate.​subject 

 Custom

 ClassificationCategory

 classification.​category 

 Custom

 ClassificationMaliciousCategories

 classification.​malicious_categories 

 Custom

 ClassificationMITRE

 classification.​mitre 

 Custom

 ClassificationReputation

 classification.​reputation 

 Custom

 ClassificationSecurityCompliance

 classification.​security_compliance 

 Custom

 ClassificationSeverity

 classification.​severity 

 Custom

 ClipboardFromURL

 clipboard.​from_url 

 Custom

 ClipboardSelectedElement

 clipboard.​selected_element 

 Custom

 ContentCategories

 content.​categories 

 Custom

 ContentLengthBytes

 content.​length_bytes 

 Custom

 ContentMIPMatchedLabel

 content.​mip_matched_label 

 Custom

 ContentScanEngine

 content.​scan_engine 

 Custom

 ContentSensitiveDataCategories

 content.​sensitive_data_categories 

 Custom

 ContentSourceElementSelector

 content.​source_element_selector 

 Custom

 ContentSourceURL

 content.​source_url 

 Custom

 CortexDataLakeTenantID

 customer_id 

 Custom

 DeviceBrowserBrand

 device.​browser_brand 

 Custom

 DeviceBrowserType

 device.​browser_type 

 Custom

 DeviceBrowserVersion

 device.​browser_version 

 Custom

 DeviceUUID

 device.​device_uuid 

 Custom

 DeviceDiskEncryptionStatus

 device.​disk_encryption_status 

 Custom

 DeviceEPPStatus

 device.​epp_status 

 Custom

 DeviceExtensionVersion

 device.​extension_version 

 Custom

 DeviceFirewallStatus

 device.​firewall_status 

 Custom

 DeviceGeoIPFromCityName

 device.​geoip_from_city_name 

 Custom

 DeviceGeoIPFromCountryName

 device.​geoip_from_country_name 

 Custom

 DeviceGeoIPFromLocationLatitude

 device.​geoip_from_location_latitude 

 Custom

 DeviceGeoIPFromLocationLongitude

 device.​geoip_from_location_longitude 

 Custom

 DeviceGroupsIDs

 device.​groups.​ids 

 Custom

 DeviceGroupsNames

 device.​groups.​names 

 Custom

 DeviceHostname

 device.​hostname 

 Custom

 DeviceIPAddress

 device.​ip_address 

 Custom

 DeviceMACAddresses

 device.​mac_addresses 

 Custom

 DeviceModel

 device.​model 

 Custom

 DeviceOSAndroidBuild

 device.​os.​android.​build 

 Custom

 DeviceOSAndroidPatch

 device.​os.​android.​patch 

 Custom

 DeviceOSAndroidRelease

 device.​os.​android.​release 

 Custom

 DeviceOSAndroidSDK

 device.​os.​android.​sdk 

 Custom

 DeviceOSiOSMajor

 device.​os.​ios.​major 

 Custom

 DeviceOSiOSMinor

 device.​os.​ios.​minor 

 Custom

 DeviceOSiOSPatch

 device.​os.​ios.​patch 

 Custom

 DeviceOSmacOSBugfix

 device.​os.​macos.​bugfix 

 Custom

 DeviceOSmacOSBuild

 device.​os.​macos.​build 

 Custom

 DeviceOSmacOSMajor

 device.​os.​macos.​major 

 Custom

 DeviceOSmacOSMinor

 device.​os.​macos.​minor 

 Custom

 DeviceOSmacOSServer

 device.​os.​macos.​server 

 Custom

 DeviceOSType

 device.​os.​type 

 Custom

 DeviceOSWindowsBuild

 device.​os.​windows.​build 

 Custom

 DeviceOSWindowsMajor

 device.​os.​windows.​major 

 Custom

 DeviceOSWindowsMinor

 device.​os.​windows.​minor 

 Custom

 DeviceOSWindowsPatch

 device.​os.​windows.​patch 

 Custom

 DeviceOSWindowsProduct

 device.​os.​windows.​product 

 Custom

 DeviceOSDisplayName

 device.​os_display_name 

 Custom

 DeviceRawUniversalID

 device.​raw_universal_id 

 Custom

 DeviceScreenLockStatus

 device.​screen_lock_status 

 Custom

 DeviceSerialNumber

 device.​serial_number 

 Custom

 DeviceType

 device.​type 

 Custom

 DeviceUserAgent

 device.​user_agent 

 Custom

 FileExtension

 file.​extension 

 Custom

 FileIsEncrypted

 file.​is_encrypted 

 Custom

 FileLocalPath

 file.​local_path 

 Custom

 FileMimeType

 file.​mime_type 

 Custom

 FileName

 file.​name 

 Custom

 FileOperation

 file.​operation 

 Custom

 FileOriginDownloadURL

 file.​origin_download_url 

 Custom

 FileSHA256

 file.​sha256 

 Custom

 FileURL

 file.​url 

 Custom

 ID

 id 

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

 TimeReceived

 log_time 

 Custom

 cat

 log_type.​value 

 Predefined

 NetworkClassifications

 network.​classifications 

 Custom

 NetworkFrameURL

 network.​frame_url 

 Custom

 NetworkHTTPMethod

 network.​http.​method 

 Custom

 NetworkHTTPStatus

 network.​http.​status 

 Custom

 NetworkProtocol

 network.​protocol 

 Custom

 NetworkTabURL

 network.​tab_url 

 Custom

 NetworkURL

 network.​url 

 Custom

 PageCaptureIsSecureScreenshot

 page.​capture.​is_secure_screenshot 

 Custom

 PageCaptureTriggeredByURL

 page.​capture.​triggered_by_url 

 Custom

 PageDevtoolsBlockReason

 page.​devtools.​block_reason 

 Custom

 PageTitle

 page.​title 

 Custom

 PincodeFailedAttempts

 pincode.​failed_attempts 

 Custom

 PincodeRegistrationTime

 pincode.​registration_time 

 Custom

 PlatformType

 platform_type 

 Custom

 PolicyAction

 policy.​action 

 Custom

 PolicyBlockReason

 policy.​block_reason 

 Custom

 PolicyBypassReason

 policy.​bypass_reason 

 Custom

 PolicyIsMonitor

 policy.​is_monitor 

 Custom

 PolicyIsSessionRecorded

 policy.​is_session_recorded 

 Custom

 PolicyRuleDescription

 policy.​rule_description 

 Custom

 PolicyRuleID

 policy.​rule_id 

 Custom

 PostureBlockReason

 posture.​block_reason 

 Custom

 PostureBlockType

 posture.​block_type 

 Custom

 PostureError

 posture.​error 

 Custom

 PrintPrinterLocation

 print.​printer_location 

 Custom

 PrintPrinterName

 print.​printer_name 

 Custom

 ProcessCLIArgs

 process.​cli_args 

 Custom

 ProcessImagePath

 process.​image_path 

 Custom

 ProcessParentProcess

 process.​parent_process 

 Custom

 ProcessPID

 process.​pid 

 Custom

 StateDeviceGroupEvaluation

 state.​device_group_evaluation 

 Custom

 StateSignInRules

 state.​sign_in_rules 

 Custom

 SubtenantID

 sub_tenant_id 

 Custom

 Subtype

 sub_type.​value 

 Custom

 TamperingType

 tampering.​type 

 Custom

 TenantID

 tenant_id 

 Custom

 devTime

 time_generated 

 Predefined

 TimeGeneratedHighResolution

 time_generated_high_res 

 Custom

 Timestamp

 timestamp 

 Custom

 TSGID

 tsg_id 

 Custom

 Type

 type 

 Custom

 UserEmail

 user.​email 

 Custom

 UserExternalID

 user.​external_id 

 Custom

 UserGroupsIDs

 user.​groups.​ids 

 Custom

 UserGroupsNames

 user.​groups.​names 

 Custom

 UserID

 user.​id 

 Custom

 UserName

 user.​name 

 Custom

 UserTenantExternalID

 user.​tenant_external_id 

 Custom

 UserTenantID

 user.​tenant_id 

 Custom

 UserTenantName

 user.​tenant_name 

 Custom

 UserTSGID

 user.​tsg_id 

 Custom

 Vendor

 vendor_name 

 Header

 Previous 

 Events HTTPS Fields 

 Next 

 GlobalProtect App Troubleshooting 

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
