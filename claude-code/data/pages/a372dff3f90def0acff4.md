---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-cisco-dnac
fetched_at: 2026-09-16T07:23:40Z
source: palo-alto-main
---

# Cisco DNAC Attribute Reference Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Attribute Reference 

 Cisco DNAC Attribute Reference 

 Download PDF 

 Device Security 

 Cisco DNAC Attribute Reference 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 BlueCat Attribute Reference 

 Next 

 Cisco ISE Attribute Reference 

 Cisco DNAC Attribute Reference 

 This reference lists the attributes that Device Security collects from Cisco DNAC,
 their names as stored in Device Security , and the Device Security fields they map to.

 When Device Security integrates with Cisco DNA Center , it retrieves
 details about active devices to enrich the inventory. The attributes in this reference
 cover wired and wireless clients, network device health data, and network device
 configuration details. 

 The third-party attribute name in Device Security refers to the attribute name
 as it appears in the Assets Inventory table and in Query Engine. This follows the format
 of third-party-name . attribute-name .
 When viewing the attribute name in the Assets Inventory table column selector or on a
 Device Details page, where the third-party name can be found as a header for the
 attributes section, then the third-party name is removed from the attribute name.

 For example, micrsoft_defender_xdr.macAddress would appear in the
 Query Builder and in the Assets Inventory table, but under Device Details Attributes Integration Specific Attributes Microsoft Defender , the attribute would appear as macAddress .

 Dna Data Api V1 Wired Clients Attributes 

 Device Security collects dna data api v1 wired clients attributes from Cisco DNAC. The following table lists each Cisco DNAC attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNAC Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 username 

 — 

 AD Username; last_ad_username 

 Username associated with the device 

 connectionStatus 

 cisco_dnac.connectionStatus 

 connection_state 

 ConnectionStatus 

 connectionStatus 

 cisco_dnac.collectionStatus 

 connection_state 

 ConnectionStatus 

 name 

 cisco_dnac.name 

 hostname 

 Name of the device 

 ipv4Address 

 cisco_dnac.ipv4Address 

 IP Address 

 Ipv4Address 

 ipv6Addresses 

 cisco_dnac.ipv6Addresses 

 ipv6_addresses 

 Ipv6Addresses 

 lastUpdatedTime 

 cisco_dnac.lastUpdatedTime 

 Last Activity 

 LastUpdatedTime 

 siteHierarchy 

 cisco_dnac.siteHierarchy 

 Location 

 SiteHierarchy 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MacAddress 

 connection.authType 

 cisco_dnac.connection.authType 

 network_authentication_method 

 AuthType 

 connection.protocol 

 cisco_dnac.connection.protocol 

 network_connection_protocol 

 Protocol 

 osVersion 

 cisco_dnac.osVersion 

 OS Version 

 OsVersion 

 deviceType 

 cisco_dnac.type 

 raw_model 

 DeviceType 

 deviceType 

 cisco_dnac.deviceType 

 raw_model 

 DeviceType 

 osType 

 cisco_dnac.osType 

 raw_os 

 OsType 

 connection.rssi 

 cisco_dnac.connection.rssi 

 RSSI 

 Rssi 

 connection.snr 

 cisco_dnac.connection.snr 

 SNR 

 Signal-to-noise ratio of the device 

 connection.ssid 

 cisco_dnac.connection.ssid 

 SSID 

 Ssid 

 connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 Switch IP 

 ConnectedNetworkDeviceManagementIp 

 connectedNetworkDevice.connectedNetworkDeviceMac 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceMac 

 Switch MAC 

 ConnectedNetworkDeviceMac 

 connectedNetworkDevice.interfaceName 

 cisco_dnac.connectedNetworkDevice.interfaceName 

 Switch Port 

 InterfaceName 

 connectedNetworkDevice.connectedNetworkDeviceName 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceName 

 switch_name 

 ConnectedNetworkDeviceName 

 vendor 

 cisco_dnac.vendor 

 Vendor 

 Device vendor 

 connection.vlanId 

 cisco_dnac.connection.vlanId 

 VLAN ID 

 VlanId 

 connection.band 

 cisco_dnac.connection.band 

 wifi_frequency 

 Band 

 type 

 — 

 Wired - Wireless 

 Type 

 connection.wlcName 

 cisco_dnac.connection.wlcName 

 wlc_name 

 WlcName 

 connectedNetworkDevice.connectedNetworkDeviceId 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceId 

 — 

 ConnectedNetworkDeviceId 

 connectedNetworkDevice.connectedNetworkDeviceType 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceType 

 — 

 ConnectedNetworkDeviceType 

 connection.apEthernetMac 

 cisco_dnac.connection.apEthernetMac 

 — 

 ApEthernetMac 

 connection.apMac 

 cisco_dnac.connection.apMac 

 — 

 ApMac 

 connection.apMode 

 cisco_dnac.connection.apMode 

 — 

 ApMode 

 connection.channel 

 cisco_dnac.connection.channel 

 — 

 Wireless channel 

 connection.channelWidth 

 cisco_dnac.connection.channelWidth 

 — 

 ChannelWidth 

 connection.dataRate 

 cisco_dnac.connection.dataRate 

 — 

 DataRate 

 connection.isFabricClient 

 cisco_dnac.connection.isFabricClient 

 — 

 IsFabricClient 

 connection.isIosAnalyticsCapable 

 cisco_dnac.connection.isIosAnalyticsCapable 

 — 

 IsIosAnalyticsCapable 

 connection.protocolCapability 

 cisco_dnac.connection.protocolCapability 

 — 

 ProtocolCapability 

 connection.radioId 

 cisco_dnac.connection.radioId 

 — 

 RadioId 

 connection.securityGroupTag 

 cisco_dnac.connection.securityGroupTag 

 — 

 SecurityGroupTag 

 connection.sessionDuration 

 cisco_dnac.connection.sessionDuration 

 — 

 SessionDuration 

 connection.vnId 

 cisco_dnac.connection.vnId 

 — 

 VnId 

 connection.wlcId 

 cisco_dnac.connection.wlcId 

 — 

 WlcId 

 formFactor 

 cisco_dnac.formFactor 

 — 

 FormFactor 

 health.connectedScore 

 cisco_dnac.health.connectedScore 

 — 

 ConnectedScore 

 health.onboardingScore 

 cisco_dnac.health.onboardingScore 

 — 

 OnboardingScore 

 health.overallScore 

 cisco_dnac.health.overallScore 

 — 

 OverallScore 

 health.rssiThreshold 

 cisco_dnac.health.rssiThreshold 

 — 

 RssiThreshold 

 health.snrThreshold 

 cisco_dnac.health.snrThreshold 

 — 

 SnrThreshold 

 id 

 cisco_dnac.id 

 — 

 Id 

 onboarding.aaaFailureReason 

 cisco_dnac.onboarding.aaaFailureReason 

 — 

 AaaFailureReason 

 onboarding.aaaServerIp 

 cisco_dnac.onboarding.aaaServerIp 

 — 

 AaaServerIp 

 onboarding.assocDoneTime 

 cisco_dnac.onboarding.assocDoneTime 

 — 

 AssocDoneTime 

 onboarding.assocFailureReason 

 cisco_dnac.onboarding.assocFailureReason 

 — 

 AssocFailureReason 

 onboarding.authDoneTime 

 cisco_dnac.onboarding.authDoneTime 

 — 

 AuthDoneTime 

 onboarding.dhcpDoneTime 

 cisco_dnac.onboarding.dhcpDoneTime 

 — 

 DhcpDoneTime 

 onboarding.dhcpFailureReason 

 cisco_dnac.onboarding.dhcpFailureReason 

 — 

 DhcpFailureReason 

 onboarding.dhcpServerIp 

 cisco_dnac.onboarding.dhcpServerIp 

 — 

 DhcpServerIp 

 onboarding.onboardingTime 

 cisco_dnac.onboarding.onboardingTime 

 — 

 OnboardingTime 

 onboarding.otherFailureReason 

 cisco_dnac.onboarding.otherFailureReason 

 — 

 OtherFailureReason 

 onboarding.roamingTime 

 cisco_dnac.onboarding.roamingTime 

 — 

 RoamingTime 

 siteHierarchyId 

 cisco_dnac.siteHierarchyId 

 — 

 SiteHierarchyId 

 siteId 

 cisco_dnac.siteId 

 — 

 SiteId 

 tracked 

 cisco_dnac.tracked 

 — 

 Tracked 

 Dna Data Api V1 Wireless Clients Attributes 

 Device Security collects dna data api v1 wireless clients attributes from Cisco DNAC. The following table lists each Cisco DNAC attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNAC Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 username 

 — 

 AD Username; last_ad_username 

 Username associated with the device 

 connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 ap_ip 

 ConnectedNetworkDeviceManagementIp 

 connectedNetworkDevice.connectedNetworkDeviceMac 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceMac 

 ap_mac 

 ConnectedNetworkDeviceMac 

 connectedNetworkDevice.connectedNetworkDeviceName 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceName 

 ap_name 

 ConnectedNetworkDeviceName 

 connectionStatus 

 cisco_dnac.connectionStatus 

 connection_state 

 ConnectionStatus 

 connectionStatus 

 cisco_dnac.collectionStatus 

 connection_state 

 ConnectionStatus 

 name 

 cisco_dnac.name 

 hostname 

 Name of the device 

 ipv4Address 

 cisco_dnac.ipv4Address 

 IP Address 

 Ipv4Address 

 ipv6Addresses 

 cisco_dnac.ipv6Addresses 

 ipv6_addresses 

 Ipv6Addresses 

 lastUpdatedTime 

 cisco_dnac.lastUpdatedTime 

 Last Activity 

 LastUpdatedTime 

 siteHierarchy 

 cisco_dnac.siteHierarchy 

 Location 

 SiteHierarchy 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MacAddress 

 connection.authType 

 cisco_dnac.connection.authType 

 network_authentication_method 

 AuthType 

 osVersion 

 cisco_dnac.osVersion 

 OS Version 

 OsVersion 

 connection.protocol 

 cisco_dnac.connection.protocol 

 Radio; network_connection_protocol 

 Protocol 

 osType 

 cisco_dnac.osType 

 raw_os 

 OsType 

 connection.rssi 

 cisco_dnac.connection.rssi 

 RSSI 

 Rssi 

 connection.snr 

 cisco_dnac.connection.snr 

 SNR 

 Signal-to-noise ratio of the device 

 connection.ssid 

 cisco_dnac.connection.ssid 

 SSID 

 Ssid 

 vendor 

 cisco_dnac.vendor 

 Vendor 

 Device vendor 

 connection.vlanId 

 cisco_dnac.connection.vlanId 

 VLAN ID 

 VlanId 

 connection.channel 

 cisco_dnac.connection.channel 

 wifi_channel 

 Wireless channel 

 connection.band 

 cisco_dnac.connection.band 

 wifi_frequency 

 Band 

 type 

 — 

 Wired - Wireless 

 Type 

 connection.wlcName 

 cisco_dnac.connection.wlcName 

 wireles_lan_controller_name; wlc_name 

 WlcName 

 connectedNetworkDevice.connectedNetworkDeviceId 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceId 

 — 

 ConnectedNetworkDeviceId 

 connectedNetworkDevice.connectedNetworkDeviceType 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceType 

 — 

 ConnectedNetworkDeviceType 

 connectedNetworkDevice.interfaceName 

 cisco_dnac.connectedNetworkDevice.interfaceName 

 — 

 InterfaceName 

 connection.apEthernetMac 

 cisco_dnac.connection.apEthernetMac 

 — 

 ApEthernetMac 

 connection.apMac 

 cisco_dnac.connection.apMac 

 — 

 ApMac 

 connection.apMode 

 cisco_dnac.connection.apMode 

 — 

 ApMode 

 connection.channelWidth 

 cisco_dnac.connection.channelWidth 

 — 

 ChannelWidth 

 connection.dataRate 

 cisco_dnac.connection.dataRate 

 — 

 DataRate 

 connection.isFabricClient 

 cisco_dnac.connection.isFabricClient 

 — 

 IsFabricClient 

 connection.isIosAnalyticsCapable 

 cisco_dnac.connection.isIosAnalyticsCapable 

 — 

 IsIosAnalyticsCapable 

 connection.protocolCapability 

 cisco_dnac.connection.protocolCapability 

 — 

 ProtocolCapability 

 connection.radioId 

 cisco_dnac.connection.radioId 

 — 

 RadioId 

 connection.securityGroupTag 

 cisco_dnac.connection.securityGroupTag 

 — 

 SecurityGroupTag 

 connection.sessionDuration 

 cisco_dnac.connection.sessionDuration 

 — 

 SessionDuration 

 connection.vnId 

 cisco_dnac.connection.vnId 

 — 

 VnId 

 connection.wlcId 

 cisco_dnac.connection.wlcId 

 — 

 WlcId 

 deviceType 

 cisco_dnac.deviceType 

 — 

 DeviceType 

 formFactor 

 cisco_dnac.formFactor 

 — 

 FormFactor 

 health.connectedScore 

 cisco_dnac.health.connectedScore 

 — 

 ConnectedScore 

 health.onboardingScore 

 cisco_dnac.health.onboardingScore 

 — 

 OnboardingScore 

 health.overallScore 

 cisco_dnac.health.overallScore 

 — 

 OverallScore 

 health.rssiThreshold 

 cisco_dnac.health.rssiThreshold 

 — 

 RssiThreshold 

 health.snrThreshold 

 cisco_dnac.health.snrThreshold 

 — 

 SnrThreshold 

 id 

 cisco_dnac.id 

 — 

 Id 

 onboarding.aaaFailureReason 

 cisco_dnac.onboarding.aaaFailureReason 

 — 

 AaaFailureReason 

 onboarding.aaaServerIp 

 cisco_dnac.onboarding.aaaServerIp 

 — 

 AaaServerIp 

 onboarding.assocDoneTime 

 cisco_dnac.onboarding.assocDoneTime 

 — 

 AssocDoneTime 

 onboarding.assocFailureReason 

 cisco_dnac.onboarding.assocFailureReason 

 — 

 AssocFailureReason 

 onboarding.authDoneTime 

 cisco_dnac.onboarding.authDoneTime 

 — 

 AuthDoneTime 

 onboarding.dhcpDoneTime 

 cisco_dnac.onboarding.dhcpDoneTime 

 — 

 DhcpDoneTime 

 onboarding.dhcpFailureReason 

 cisco_dnac.onboarding.dhcpFailureReason 

 — 

 DhcpFailureReason 

 onboarding.dhcpServerIp 

 cisco_dnac.onboarding.dhcpServerIp 

 — 

 DhcpServerIp 

 onboarding.onboardingTime 

 cisco_dnac.onboarding.onboardingTime 

 — 

 OnboardingTime 

 onboarding.otherFailureReason 

 cisco_dnac.onboarding.otherFailureReason 

 — 

 OtherFailureReason 

 onboarding.roamingTime 

 cisco_dnac.onboarding.roamingTime 

 — 

 RoamingTime 

 siteHierarchyId 

 cisco_dnac.siteHierarchyId 

 — 

 SiteHierarchyId 

 siteId 

 cisco_dnac.siteId 

 — 

 SiteId 

 tracked 

 cisco_dnac.tracked 

 — 

 Tracked 

 deviceType 

 cisco_dnac.type 

 — 

 DeviceType 

 Dna Intent Api V1 Device Health Attributes 

 Device Security collects dna intent api v1 device health attributes from Cisco DNAC. The following table lists each Cisco DNAC attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNAC Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 name 

 cisco_dnac.name 

 hostname 

 Name of the device 

 ipAddress 

 cisco_dnac.ipAddress 

 IP Address 

 IpAddress 

 location 

 cisco_dnac.Location 

 Location 

 Location 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MacAddress 

 model 

 cisco_dnac.model 

 Model 

 Model of the device 

 osVersion 

 cisco_dnac.osVersion 

 OS Version 

 OsVersion 

 deviceType 

 cisco_dnac.deviceType 

 raw_model 

 DeviceType 

 cpuHealth 

 cisco_dnac.cpuHealth 

 — 

 CpuHealth 

 cpuUtilization 

 cisco_dnac.cpuUtilization 

 — 

 CpuUtilization 

 deviceFamily 

 cisco_dnac.deviceFamily 

 — 

 DeviceFamily 

 interDeviceLinkAvailHealth 

 cisco_dnac.interDeviceLinkAvailHealth 

 — 

 InterDeviceLinkAvailHealth 

 memoryUtilization 

 cisco_dnac.memoryUtilization 

 — 

 MemoryUtilization 

 memoryUtilizationHealth 

 cisco_dnac.memoryUtilizationHealth 

 — 

 MemoryUtilizationHealth 

 overallHealth 

 cisco_dnac.overallHealth 

 — 

 OverallHealth 

 reachabilityHealth 

 cisco_dnac.reachabilityHealth 

 — 

 ReachabilityHealth 

 utilizationHealth 

 cisco_dnac.utilizationHealth 

 — 

 UtilizationHealth 

 uuid 

 cisco_dnac.uuid 

 — 

 Uuid 

 Dna Intent Api V1 Network Device Attributes 

 Device Security collects dna intent api v1 network device attributes from Cisco DNAC. The following table lists each Cisco DNAC attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNAC Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 apManagerInterfaceIp 

 cisco_dnac.apManagerInterfaceIp 

 ap_ip 

 ApManagerInterfaceIp 

 apEthernetMacAddress 

 cisco_dnac.apEthernetMacAddress 

 ap_mac 

 ApEthernetMacAddress 

 description 

 cisco_dnac.description 

 Description 

 Description 

 hostname 

 cisco_dnac.hostname 

 hostname 

 Name of the device 

 managementIpAddress 

 cisco_dnac.managementIpAddress 

 IP Address 

 ManagementIpAddress 

 lastUpdated 

 cisco_dnac.lastUpdated 

 Last Activity 

 LastUpdated 

 lastUpdated 

 cisco_dnac.lastUpdatedTime 

 Last Activity 

 LastUpdated 

 locationName 

 cisco_dnac.locationName 

 Location 

 LocationName 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MacAddress 

 platformId 

 cisco_dnac.platformId 

 Model 

 PlatformId 

 serialNumber 

 cisco_dnac.serialNumber 

 Serial Number 

 SerialNumber 

 vendor 

 cisco_dnac.vendor 

 Vendor 

 Device vendor 

 associatedWlcIp 

 cisco_dnac.associatedWlcIp 

 wireles_lan_controller_name; wlc_ip 

 AssociatedWlcIp 

 bootDateTime 

 cisco_dnac.bootDateTime 

 — 

 BootDateTime 

 collectionStatus 

 cisco_dnac.collectionStatus 

 — 

 CollectionStatus 

 deviceSupportLevel 

 cisco_dnac.deviceSupportLevel 

 — 

 DeviceSupportLevel 

 errorCode 

 cisco_dnac.errorCode 

 — 

 ErrorCode 

 errorDescription 

 cisco_dnac.errorDescription 

 — 

 ErrorDescription 

 family 

 cisco_dnac.family 

 — 

 Family 

 id 

 cisco_dnac.id 

 — 

 Id 

 instanceTenantId 

 cisco_dnac.instanceTenantId 

 — 

 InstanceTenantId 

 instanceUuid 

 cisco_dnac.instanceUuid 

 — 

 InstanceUuid 

 interfaceCount 

 cisco_dnac.interfaceCount 

 — 

 InterfaceCount 

 inventoryStatusDetail 

 cisco_dnac.inventoryStatusDetail 

 — 

 InventoryStatusDetail 

 location 

 cisco_dnac.Location 

 — 

 Location 

 managementState 

 cisco_dnac.managementState 

 — 

 ManagementState 

 memorySize 

 cisco_dnac.memorySize 

 — 

 MemorySize 

 reachabilityStatus 

 cisco_dnac.reachabilityStatus 

 — 

 ReachabilityStatus 

 role 

 cisco_dnac.role 

 — 

 Role of the device 

 series 

 cisco_dnac.series 

 — 

 Series 

 softwareVersion 

 cisco_dnac.softwareVersion 

 — 

 SoftwareVersion 

 type 

 cisco_dnac.type 

 — 

 Type 

 upTime 

 cisco_dnac.upTime 

 — 

 UpTime 

 uptimeSeconds 

 cisco_dnac.uptimeSeconds 

 — 

 UptimeSeconds 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 BlueCat Attribute Reference 

 Next 

 Cisco ISE Attribute Reference
