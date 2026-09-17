---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-cisco-meraki
fetched_at: 2026-09-15T15:14:39Z
source: palo-alto-main
---

# Cisco Meraki Attribute Reference Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Attribute Reference 

 Cisco Meraki Attribute Reference 

 Download PDF 

 Device Security 

 Cisco Meraki Attribute Reference 

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

 Cisco ISE Attribute Reference 

 Next 

 Cisco Prime Attribute Reference 

 Cisco Meraki Attribute Reference 

 This reference lists the attributes that Device Security collects from Cisco Meraki,
 their names as stored in Device Security , and the Device Security fields they map to.

 When Device Security integrates with Cisco Meraki Cloud , it imports
 network visibility data to enrich the device inventory. The attributes in this reference
 cover network clients, organization-managed devices, and VLAN static IP and subnet
 assignments. 

 The third-party attribute name in Device Security refers to the attribute name
 as it appears in the Assets Inventory table and in Query Engine. This follows the format
 of third-party-name . attribute-name .
 When viewing the attribute name in the Assets Inventory table column selector or on a
 Device Details page, where the third-party name can be found as a header for the
 attributes section, then the third-party name is removed from the attribute name.

 For example, micrsoft_defender_xdr.macAddress would appear in the
 Query Builder and in the Assets Inventory table, but under Device Details Attributes Integration Specific Attributes Microsoft Defender , the attribute would appear as macAddress .

 Network Client Attributes 

 Device Security collects client attributes from the Cisco Meraki network clients API. Each record describes a client device that has connected to a Meraki network.
 The following table lists each Cisco Meraki attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco Meraki Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 ap_mac 

 — 

 ap_mac 

 Access point MAC address 

 ap_name 

 — 

 Access Point Name 

 Access point name 

 status 

 cisco_meraki.status 

 connection_state 

 Status 

 description 

 cisco_meraki.description 

 Description 

 Description 

 firstSeen 

 cisco_meraki.firstSeen 

 First Seen 

 First seen 

 ip 

 cisco_meraki.ip 

 ipv4_address 

 IP address 

 lastSeen 

 cisco_meraki.lastSeen 

 Last Activity 

 Last seen 

 mac 

 cisco_meraki.mac 

 MAC; id 

 MAC address 

 os 

 cisco_meraki.os 

 raw_os 

 Operating system 

 ssid 

 — 

 SSID 

 SSID 

 switch_mac 

 — 

 Switch MAC 

 Switch MAC address 

 switchport 

 cisco_meraki.switchport 

 Switch Port 

 Switch port 

 switch_name 

 — 

 switch_name 

 Switch name 

 manufacturer 

 cisco_meraki.manufacturer 

 Vendor 

 Manufacturer 

 vlan 

 cisco_meraki.vlan 

 VLAN ID 

 VLAN 

 recentDeviceConnection 

 cisco_meraki.recentDeviceConnection 

 Wired - Wireless 

 Recent device connection 

 adaptivePolicyGroup 

 cisco_meraki.adaptivePolicyGroup 

 — 

 Adaptive policy group 

 groupPolicy8021x 

 cisco_meraki.groupPolicy8021x 

 — 

 Group policy 802.1x 

 id 

 cisco_meraki.id 

 — 

 Record ID 

 ip6 

 cisco_meraki.ip6 

 — 

 IPv6 address 

 ip6Local 

 cisco_meraki.ip6Local 

 — 

 Local IPv6 address 

 is11beCapable 

 cisco_meraki.is11beCapable 

 — 

 802.11be capability indicator 

 namedVlan 

 cisco_meraki.namedVlan 

 — 

 Named VLAN 

 notes 

 cisco_meraki.notes 

 — 

 Notes 

 pskGroup 

 cisco_meraki.pskGroup 

 — 

 PSK group 

 recentDeviceMac 

 cisco_meraki.recentDeviceMac 

 — 

 Recent device MAC address 

 recentDeviceName 

 cisco_meraki.recentDeviceName 

 — 

 Recent device name 

 recentDeviceSerial 

 cisco_meraki.recentDeviceSerial 

 — 

 Recent device serial number 

 smInstalled 

 cisco_meraki.smInstalled 

 — 

 SM installed 

 usage 

 cisco_meraki.usage 

 — 

 Usage 

 user 

 cisco_meraki.user 

 — 

 User 

 wirelessCapabilities 

 cisco_meraki.wirelessCapabilities 

 — 

 Wireless capabilities 

 Organization Device Attributes 

 Device Security collects device attributes from the Cisco Meraki organization devices API. Each record describes a Meraki network device such as a switch, access point, or security appliance.
 The following table lists each Cisco Meraki attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco Meraki Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 name 

 cisco_meraki.name 

 Hostname 

 Name 

 mac 

 cisco_meraki.mac 

 id; MAC 

 MAC address 

 lanIp 

 cisco_meraki.lanIp 

 ipv4_address 

 LAN IP address 

 firmware 

 cisco_meraki.firmware 

 latest_firmware_version 

 Firmware version 

 model 

 cisco_meraki.model 

 Model 

 Model 

 details.value 

 — 

 OS Version 

 Value 

 serial 

 — 

 Serial Number 

 Serial number 

 productType 

 cisco_meraki.productType 

 Wired - Wireless 

 Product type 

 address 

 cisco_meraki.address 

 — 

 Address 

 configurationUpdatedAt 

 cisco_meraki.configurationUpdatedAt 

 — 

 Configuration updated at 

 details 

 cisco_meraki.details 

 — 

 Details 

 lat 

 cisco_meraki.lat 

 — 

 Latitude 

 lng 

 cisco_meraki.lng 

 — 

 Longitude 

 networkId 

 cisco_meraki.networkId 

 — 

 Network ID 

 notes 

 cisco_meraki.notes 

 — 

 Notes 

 tags 

 cisco_meraki.tags 

 — 

 Tags 

 url 

 cisco_meraki.url 

 — 

 URL 

 VLAN Static IP Attributes 

 Device Security collects VLAN static IP reservation attributes from the Cisco Meraki organization network VLAN API. Each record describes a device with a statically assigned IP address within a VLAN.
 The following table lists each Cisco Meraki attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco Meraki Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 name 

 cisco_meraki.name 

 Hostname 

 Name 

 ip 

 cisco_meraki.ip 

 ipv4_address 

 IP address 

 mac 

 cisco_meraki.is_ip_address_static 

 is_ip_address_static; MAC; id 

 Mac 

 mac 

 cisco_meraki.mac 

 is_ip_address_static; MAC; id 

 Mac 

 vlan_id 

 cisco_meraki.vlan_id 

 VLAN ID 

 VLAN ID 

 applianceIp 

 cisco_meraki.applianceIp 

 — 

 Appliance IP address 

 dhcpRelayServerIps 

 cisco_meraki.dhcpRelayServerIps 

 — 

 DHCP relay server IP addresses 

 dnsNameservers 

 cisco_meraki.dnsNameservers 

 — 

 DNS name servers 

 network_name 

 cisco_meraki.network_name 

 — 

 Network name 

 networkId 

 cisco_meraki.networkId 

 — 

 Network ID 

 subnet 

 cisco_meraki.subnet 

 — 

 Subnet 

 VLAN Subnet Attributes 

 Device Security collects VLAN subnet attributes from the Cisco Meraki organization network VLANs API. Each record describes a VLAN configured within a Meraki network.
 The following table lists each Cisco Meraki attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco Meraki Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 name 

 — 

 Device Name 

 VLAN name 

 subnet 

 — 

 prefix; id 

 Subnet 

 network_name 

 — 

 Site 

 Network name 

 id 

 — 

 VLAN ID 

 VLAN ID 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Cisco ISE Attribute Reference 

 Next 

 Cisco Prime Attribute Reference
