---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-cisco-dnac
fetched_at: 2026-08-13T16:37:00Z
source: palo-alto-main
---

# Cisco DNA Center Attribute Reference Clear

Cisco DNA Center Attribute Reference 

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

 Cisco DNA Center Attribute Reference 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Attribute Reference 

 Cisco DNA Center Attribute Reference 

 Download PDF 

 Device Security 

 Cisco DNA Center Attribute Reference 

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

 BlueCat IPAM Attribute Reference 

 Next 

 Cisco ISE Attribute Reference 

 Cisco DNA Center Attribute Reference 

 This reference lists the attributes that Device Security collects from Cisco DNA Center,
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

 Wired Client Attributes 

 Device Security collects wired client attributes from the Cisco DNA Center wired clients API. Each record describes a client device connected to the network via a wired interface.
 The following table lists each Cisco DNA Center attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNA Center Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 collectionStatus 

 cisco_dnac.collectionStatus 

 collection_state 

 Collection status 

 connectedNetworkDevice.connectedNetworkDeviceId 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceId 

 — 

 Connected network device unique identifier 

 connectedNetworkDevice.connectedNetworkDeviceMac 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceMac 

 Switch MAC 

 Connected network device MAC address 

 connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 Switch IP 

 Connected network device management IP address 

 connectedNetworkDevice.connectedNetworkDeviceName 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceName 

 switch_name 

 Connected network device name 

 connectedNetworkDevice.connectedNetworkDeviceType 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceType 

 — 

 Connected network device type 

 connectedNetworkDevice.interfaceName 

 cisco_dnac.connectedNetworkDevice.interfaceName 

 Switch Port 

 Interface name 

 connection.apEthernetMac 

 cisco_dnac.connection.apEthernetMac 

 — 

 Access point Ethernet MAC address 

 connection.apMac 

 cisco_dnac.connection.apMac 

 — 

 Access point MAC address 

 connection.apMode 

 cisco_dnac.connection.apMode 

 — 

 Access point mode 

 connection.authType 

 cisco_dnac.connection.authType 

 network_authentication_method 

 Authentication type 

 connection.band 

 cisco_dnac.connection.band 

 wifi_frequency 

 Wireless band 

 connection.channel 

 cisco_dnac.connection.channel 

 — 

 Connection channel 

 connection.channelWidth 

 cisco_dnac.connection.channelWidth 

 — 

 Connection channel width 

 connection.dataRate 

 cisco_dnac.connection.dataRate 

 — 

 Connection data rate 

 connection.isFabricClient 

 cisco_dnac.connection.isFabricClient 

 — 

 Indicates if device is a fabric client 

 connection.isIosAnalyticsCapable 

 cisco_dnac.connection.isIosAnalyticsCapable 

 — 

 Indicates if device is capable of iOS analytics 

 connection.protocol 

 cisco_dnac.connection.protocol 

 network_connection_protocol 

 Connection protocol 

 connection.protocolCapability 

 cisco_dnac.connection.protocolCapability 

 — 

 Protocol capability 

 connection.radioId 

 cisco_dnac.connection.radioId 

 — 

 Connection radio identifier 

 connection.rssi 

 cisco_dnac.connection.rssi 

 RSSI 

 Received Signal Strength Indicator 

 connection.securityGroupTag 

 cisco_dnac.connection.securityGroupTag 

 — 

 Security group tag 

 connection.sessionDuration 

 cisco_dnac.connection.sessionDuration 

 — 

 Connection session duration 

 connection.snr 

 cisco_dnac.connection.snr 

 SNR 

 Signal-to-Noise Ratio 

 connection.ssid 

 cisco_dnac.connection.ssid 

 SSID 

 Service Set Identifier 

 connection.vlanId 

 cisco_dnac.connection.vlanId 

 VLAN ID 

 VLAN identifier 

 connection.vnId 

 cisco_dnac.connection.vnId 

 — 

 Virtual Network identifier 

 connection.wlcId 

 cisco_dnac.connection.wlcId 

 — 

 Wireless LAN Controller identifier 

 connection.wlcName 

 cisco_dnac.connection.wlcName 

 wlc_name 

 Wireless LAN Controller name 

 connectionStatus 

 cisco_dnac.connectionStatus 

 connection_state 

 Connection status 

 deviceType 

 cisco_dnac.deviceType 

 — 

 Device type 

 formFactor 

 cisco_dnac.formFactor 

 — 

 Device form factor 

 health.connectedScore 

 cisco_dnac.health.connectedScore 

 — 

 Connected health score 

 health.onboardingScore 

 cisco_dnac.health.onboardingScore 

 — 

 Onboarding health score 

 health.overallScore 

 cisco_dnac.health.overallScore 

 — 

 Overall health score 

 health.rssiThreshold 

 cisco_dnac.health.rssiThreshold 

 — 

 RSSI threshold 

 health.snrThreshold 

 cisco_dnac.health.snrThreshold 

 — 

 SNR threshold 

 id 

 cisco_dnac.id 

 — 

 Device identifier 

 ipv4Address 

 cisco_dnac.ipv4Address 

 ipv4_address 

 IPv4 address 

 ipv6Addresses 

 cisco_dnac.ipv6Addresses 

 ipv6_addresses 

 IPv6 addresses 

 lastUpdatedTime 

 cisco_dnac.lastUpdatedTime 

 Last Activity 

 Last updated time 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MAC address 

 name 

 cisco_dnac.name 

 Hostname 

 Device name 

 onboarding.aaaFailureReason 

 cisco_dnac.onboarding.aaaFailureReason 

 — 

 AAA failure reason 

 onboarding.aaaServerIp 

 cisco_dnac.onboarding.aaaServerIp 

 — 

 AAA server IP address 

 onboarding.assocDoneTime 

 cisco_dnac.onboarding.assocDoneTime 

 — 

 Association completion time 

 onboarding.assocFailureReason 

 cisco_dnac.onboarding.assocFailureReason 

 — 

 Association failure reason 

 onboarding.authDoneTime 

 cisco_dnac.onboarding.authDoneTime 

 — 

 Authentication completion time 

 onboarding.dhcpDoneTime 

 cisco_dnac.onboarding.dhcpDoneTime 

 — 

 DHCP completion time 

 onboarding.dhcpFailureReason 

 cisco_dnac.onboarding.dhcpFailureReason 

 — 

 DHCP failure reason 

 onboarding.dhcpServerIp 

 cisco_dnac.onboarding.dhcpServerIp 

 — 

 DHCP server IP address 

 onboarding.onboardingTime 

 cisco_dnac.onboarding.onboardingTime 

 — 

 Onboarding time 

 onboarding.otherFailureReason 

 cisco_dnac.onboarding.otherFailureReason 

 — 

 Other failure reason 

 onboarding.roamingTime 

 cisco_dnac.onboarding.roamingTime 

 — 

 Roaming time 

 osType 

 cisco_dnac.osType 

 raw_os 

 Operating system type 

 osVersion 

 cisco_dnac.osVersion 

 OS Version 

 Operating system version 

 siteHierarchy 

 cisco_dnac.siteHierarchy 

 Location 

 Site hierarchy 

 siteHierarchyId 

 cisco_dnac.siteHierarchyId 

 — 

 Site hierarchy identifier 

 siteId 

 cisco_dnac.siteId 

 — 

 Site identifier 

 tracked 

 cisco_dnac.tracked 

 — 

 Tracking status 

 type 

 — 

 Wired - Wireless 

 Client connection type 

 username 

 — 

 AD Username; last_ad_username 

 Username of the connected client 

 vendor 

 cisco_dnac.vendor 

 Vendor 

 Device vendor 

 Wireless Client Attributes 

 Device Security collects wireless client attributes from the Cisco DNA Center wireless clients API. Each record describes a client device connected to the network via a wireless interface, including the access point it associates with.
 The following table lists each Cisco DNA Center attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNA Center Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 collectionStatus 

 cisco_dnac.collectionStatus 

 collection_state 

 Collection status 

 connectedNetworkDevice.connectedNetworkDeviceId 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceId 

 — 

 Connected network device unique identifier 

 connectedNetworkDevice.connectedNetworkDeviceMac 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceMac 

 ap_mac 

 Connected network device MAC address 

 connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceManagementIp 

 ap_ip 

 Connected network device management IP address 

 connectedNetworkDevice.connectedNetworkDeviceName 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceName 

 Access Point Name 

 Connected network device name 

 connectedNetworkDevice.connectedNetworkDeviceType 

 cisco_dnac.connectedNetworkDevice.connectedNetworkDeviceType 

 — 

 Connected network device type 

 connectedNetworkDevice.interfaceName 

 cisco_dnac.connectedNetworkDevice.interfaceName 

 — 

 Interface name 

 connection.apEthernetMac 

 cisco_dnac.connection.apEthernetMac 

 — 

 Access point Ethernet MAC address 

 connection.apMac 

 cisco_dnac.connection.apMac 

 — 

 Access point MAC address 

 connection.apMode 

 cisco_dnac.connection.apMode 

 — 

 Access point mode 

 connection.authType 

 cisco_dnac.connection.authType 

 network_authentication_method 

 Authentication type 

 connection.band 

 cisco_dnac.connection.band 

 wifi_frequency 

 Wireless band 

 connection.channel 

 cisco_dnac.connection.channel 

 wifi_channel 

 Connection channel 

 connection.channelWidth 

 cisco_dnac.connection.channelWidth 

 — 

 Connection channel width 

 connection.dataRate 

 cisco_dnac.connection.dataRate 

 — 

 Connection data rate 

 connection.isFabricClient 

 cisco_dnac.connection.isFabricClient 

 — 

 Indicates if device is a fabric client 

 connection.isIosAnalyticsCapable 

 cisco_dnac.connection.isIosAnalyticsCapable 

 — 

 Indicates if device is capable of iOS analytics 

 connection.protocol 

 cisco_dnac.connection.protocol 

 Radio; network_connection_protocol 

 Connection protocol 

 connection.protocolCapability 

 cisco_dnac.connection.protocolCapability 

 — 

 Protocol capability 

 connection.radioId 

 cisco_dnac.connection.radioId 

 — 

 Connection radio identifier 

 connection.rssi 

 cisco_dnac.connection.rssi 

 RSSI 

 Received Signal Strength Indicator 

 connection.securityGroupTag 

 cisco_dnac.connection.securityGroupTag 

 — 

 Security group tag 

 connection.sessionDuration 

 cisco_dnac.connection.sessionDuration 

 — 

 Connection session duration 

 connection.snr 

 cisco_dnac.connection.snr 

 SNR 

 Signal-to-Noise Ratio 

 connection.ssid 

 cisco_dnac.connection.ssid 

 SSID 

 Service Set Identifier 

 connection.vlanId 

 cisco_dnac.connection.vlanId 

 VLAN ID 

 VLAN identifier 

 connection.vnId 

 cisco_dnac.connection.vnId 

 — 

 Virtual Network identifier 

 connection.wlcId 

 cisco_dnac.connection.wlcId 

 — 

 Wireless LAN Controller identifier 

 connection.wlcName 

 cisco_dnac.connection.wlcName 

 wireles_lan_controller_name; wlc_name 

 Wireless LAN Controller name 

 connectionStatus 

 — 

 connection_state 

 Connection status 

 deviceType 

 — 

 — 

 Device type 

 formFactor 

 cisco_dnac.formFactor 

 — 

 Device form factor 

 health.connectedScore 

 cisco_dnac.health.connectedScore 

 — 

 Connected health score 

 health.onboardingScore 

 cisco_dnac.health.onboardingScore 

 — 

 Onboarding health score 

 health.overallScore 

 cisco_dnac.health.overallScore 

 — 

 Overall health score 

 health.rssiThreshold 

 cisco_dnac.health.rssiThreshold 

 — 

 RSSI threshold 

 health.snrThreshold 

 cisco_dnac.health.snrThreshold 

 — 

 SNR threshold 

 id 

 cisco_dnac.id 

 — 

 Device identifier 

 ipv4Address 

 cisco_dnac.ipv4Address 

 ipv4_address 

 IPv4 address 

 ipv6Addresses 

 cisco_dnac.ipv6Addresses 

 ipv6_addresses 

 IPv6 addresses 

 lastUpdatedTime 

 cisco_dnac.lastUpdatedTime 

 Last Activity 

 Last updated time 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MAC address 

 name 

 cisco_dnac.name 

 Hostname 

 Device name 

 onboarding.aaaFailureReason 

 cisco_dnac.onboarding.aaaFailureReason 

 — 

 AAA failure reason 

 onboarding.aaaServerIp 

 cisco_dnac.onboarding.aaaServerIp 

 — 

 AAA server IP address 

 onboarding.assocDoneTime 

 cisco_dnac.onboarding.assocDoneTime 

 — 

 Association completion time 

 onboarding.assocFailureReason 

 cisco_dnac.onboarding.assocFailureReason 

 — 

 Association failure reason 

 onboarding.authDoneTime 

 cisco_dnac.onboarding.authDoneTime 

 — 

 Authentication completion time 

 onboarding.dhcpDoneTime 

 cisco_dnac.onboarding.dhcpDoneTime 

 — 

 DHCP completion time 

 onboarding.dhcpFailureReason 

 cisco_dnac.onboarding.dhcpFailureReason 

 — 

 DHCP failure reason 

 onboarding.dhcpServerIp 

 cisco_dnac.onboarding.dhcpServerIp 

 — 

 DHCP server IP address 

 onboarding.onboardingTime 

 cisco_dnac.onboarding.onboardingTime 

 — 

 Onboarding time 

 onboarding.otherFailureReason 

 cisco_dnac.onboarding.otherFailureReason 

 — 

 Other failure reason 

 onboarding.roamingTime 

 cisco_dnac.onboarding.roamingTime 

 — 

 Roaming time 

 osType 

 cisco_dnac.osType 

 raw_os 

 Operating system type 

 osVersion 

 cisco_dnac.osVersion 

 OS Version 

 Operating system version 

 siteHierarchy 

 cisco_dnac.siteHierarchy 

 Location 

 Site hierarchy 

 siteHierarchyId 

 cisco_dnac.siteHierarchyId 

 — 

 Site hierarchy identifier 

 siteId 

 cisco_dnac.siteId 

 — 

 Site identifier 

 tracked 

 cisco_dnac.tracked 

 — 

 Tracking status 

 type 

 — 

 Wired - Wireless 

 Client connection type 

 username 

 — 

 AD Username; last_ad_username 

 Username of the connected client 

 vendor 

 cisco_dnac.vendor 

 Vendor 

 Device vendor 

 Network Device Health Attributes 

 Device Security collects health and status attributes from the Cisco DNA Center device health API. Each record describes the operational health of a managed network device.
 The following table lists each Cisco DNA Center attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNA Center Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 cpuHealth 

 cisco_dnac.cpuHealth 

 — 

 CPU health score 

 cpuUtilization 

 cisco_dnac.cpuUtilization 

 — 

 CPU utilization percentage 

 deviceFamily 

 cisco_dnac.deviceFamily 

 — 

 Device family 

 deviceType 

 cisco_dnac.deviceType 

 — 

 Device type 

 interDeviceLinkAvailHealth 

 cisco_dnac.interDeviceLinkAvailHealth 

 — 

 Inter-device link availability health score 

 ipAddress 

 cisco_dnac.ipAddress 

 ipv4_address 

 IP address 

 location 

 cisco_dnac.Location 

 Location 

 Device location 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MAC address 

 memoryUtilization 

 cisco_dnac.memoryUtilization 

 — 

 Memory utilization percentage 

 memoryUtilizationHealth 

 cisco_dnac.memoryUtilizationHealth 

 — 

 Memory utilization health score 

 model 

 cisco_dnac.model 

 Model 

 Device model 

 name 

 cisco_dnac.name 

 Hostname 

 Device name 

 osVersion 

 cisco_dnac.osVersion 

 OS Version 

 Operating system version 

 overallHealth 

 cisco_dnac.overallHealth 

 — 

 Overall health score 

 reachabilityHealth 

 cisco_dnac.reachabilityHealth 

 — 

 Reachability health score 

 utilizationHealth 

 cisco_dnac.utilizationHealth 

 — 

 Utilization health score 

 uuid 

 cisco_dnac.uuid 

 — 

 Universally unique identifier 

 Network Device Attributes 

 Device Security collects network device inventory attributes from the Cisco DNA Center network device API. Each record describes a network infrastructure device such as a switch, router, or access point managed by DNA Center.
 The following table lists each Cisco DNA Center attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco DNA Center Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 apEthernetMacAddress 

 cisco_dnac.apEthernetMacAddress 

 ap_mac 

 Access point Ethernet MAC address 

 apManagerInterfaceIp 

 cisco_dnac.apManagerInterfaceIp 

 ap_ip 

 Access point manager interface IP 

 associatedWlcIp 

 cisco_dnac.associatedWlcIp 

 wireles_lan_controller_name; wlc_ip 

 Associated WLC IP address 

 bootDateTime 

 cisco_dnac.bootDateTime 

 — 

 Boot date and time 

 collectionStatus 

 cisco_dnac.collectionStatus 

 — 

 Collection status 

 description 

 cisco_dnac.description 

 Description 

 Device description 

 deviceSupportLevel 

 cisco_dnac.deviceSupportLevel 

 — 

 Device support level 

 errorCode 

 cisco_dnac.errorCode 

 — 

 Error code 

 errorDescription 

 cisco_dnac.errorDescription 

 — 

 Error description 

 family 

 cisco_dnac.family 

 — 

 Device family 

 hostname 

 cisco_dnac.hostname 

 Hostname 

 Hostname 

 id 

 cisco_dnac.id 

 — 

 Device identifier 

 instanceTenantId 

 cisco_dnac.instanceTenantId 

 — 

 Instance tenant identifier 

 instanceUuid 

 cisco_dnac.instanceUuid 

 — 

 Instance UUID 

 interfaceCount 

 cisco_dnac.interfaceCount 

 — 

 Total number of network interfaces 

 inventoryStatusDetail 

 cisco_dnac.inventoryStatusDetail 

 — 

 Inventory status detail 

 lastUpdated 

 — 

 Last Activity 

 Last updated timestamp 

 location 

 cisco_dnac.Location 

 — 

 Device location 

 locationName 

 cisco_dnac.locationName 

 Location 

 Location name 

 macAddress 

 cisco_dnac.macAddress 

 MAC; id 

 MAC address 

 managementIpAddress 

 cisco_dnac.managementIpAddress 

 ipv4_address 

 Management IP address 

 managementState 

 cisco_dnac.managementState 

 — 

 Management state 

 memorySize 

 cisco_dnac.memorySize 

 — 

 Memory size 

 platformId 

 cisco_dnac.platformId 

 Model 

 Platform identifier 

 reachabilityStatus 

 cisco_dnac.reachabilityStatus 

 — 

 Reachability status 

 role 

 cisco_dnac.role 

 — 

 Device role 

 serialNumber 

 cisco_dnac.serialNumber 

 Serial Number 

 Serial number 

 series 

 cisco_dnac.series 

 — 

 Device series 

 softwareVersion 

 cisco_dnac.softwareVersion 

 — 

 Software version 

 type 

 cisco_dnac.type 

 — 

 Device type 

 upTime 

 cisco_dnac.upTime 

 — 

 Device uptime 

 uptimeSeconds 

 cisco_dnac.uptimeSeconds 

 — 

 Device uptime in seconds 

 vendor 

 cisco_dnac.vendor 

 Vendor 

 Device vendor 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 BlueCat IPAM Attribute Reference 

 Next 

 Cisco ISE Attribute Reference 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Reference 

 Cloud-Delivered Security Services 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
