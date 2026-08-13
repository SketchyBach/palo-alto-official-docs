---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-cisco-meraki
fetched_at: 2026-08-13T16:37:00Z
source: palo-alto-main
---

# Cisco Meraki Attribute Reference Clear

Cisco Meraki Attribute Reference 

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

 Cisco Meraki Attribute Reference 

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

 adaptivePolicyGroup 

 cisco_meraki.adaptivePolicyGroup 

 — 

 Adaptive policy group 

 ap_mac 

 — 

 ap_mac 

 Access point MAC address 

 ap_name 

 — 

 Access Point Name 

 Access point name 

 description 

 cisco_meraki.description 

 Description 

 Description 

 firstSeen 

 cisco_meraki.firstSeen 

 First Seen 

 First seen 

 groupPolicy8021x 

 cisco_meraki.groupPolicy8021x 

 — 

 Group policy 802.1x 

 id 

 cisco_meraki.id 

 — 

 Record ID 

 ip 

 cisco_meraki.ip 

 ipv4_address 

 IP address 

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

 lastSeen 

 cisco_meraki.lastSeen 

 Last Activity 

 Last seen 

 mac 

 cisco_meraki.mac 

 MAC; id 

 MAC address 

 manufacturer 

 cisco_meraki.manufacturer 

 Vendor 

 Manufacturer 

 namedVlan 

 cisco_meraki.namedVlan 

 — 

 Named VLAN 

 notes 

 cisco_meraki.notes 

 — 

 Notes 

 os 

 cisco_meraki.os 

 raw_os 

 Operating system 

 pskGroup 

 cisco_meraki.pskGroup 

 — 

 PSK group 

 recentDeviceConnection 

 cisco_meraki.recentDeviceConnection 

 Wired - Wireless 

 Recent device connection 

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

 ssid 

 — 

 SSID 

 SSID 

 status 

 cisco_meraki.status 

 connection_state 

 Status 

 switch_mac 

 — 

 Switch MAC 

 Switch MAC address 

 switch_name 

 — 

 switch_name 

 Switch name 

 switchport 

 cisco_meraki.switchport 

 Switch Port 

 Switch port 

 usage 

 cisco_meraki.usage 

 — 

 Usage 

 user 

 cisco_meraki.user 

 — 

 User 

 vlan 

 cisco_meraki.vlan 

 VLAN ID 

 VLAN 

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

 details.[1].value 

 — 

 OS Version 

 Details value 

 firmware 

 cisco_meraki.firmware 

 latest_firmware_version 

 Firmware version 

 lanIp 

 cisco_meraki.lanIp 

 ipv4_address 

 LAN IP address 

 lat 

 cisco_meraki.lat 

 — 

 Latitude 

 lng 

 cisco_meraki.lng 

 — 

 Longitude 

 mac 

 cisco_meraki.mac 

 id; MAC 

 MAC address 

 model 

 cisco_meraki.model 

 Model 

 Model 

 name 

 cisco_meraki.name 

 Hostname 

 Name 

 networkId 

 cisco_meraki.networkId 

 — 

 Network ID 

 notes 

 cisco_meraki.notes 

 — 

 Notes 

 productType 

 cisco_meraki.productType 

 Wired - Wireless 

 Product type 

 serial 

 — 

 Serial Number 

 Serial number 

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

 ip 

 cisco_meraki.ip 

 ipv4_address 

 IP address 

 mac 

 — 

 is_ip_address_static; MAC; id 

 MAC address 

 name 

 cisco_meraki.name 

 Hostname 

 Name 

 networkId 

 cisco_meraki.networkId 

 — 

 Network ID 

 network_name 

 cisco_meraki.network_name 

 — 

 Network name 

 subnet 

 cisco_meraki.subnet 

 — 

 Subnet 

 vlan_id 

 cisco_meraki.vlan_id 

 VLAN ID 

 VLAN ID 

 VLAN Subnet Attributes 

 Device Security collects VLAN subnet attributes from the Cisco Meraki organization network VLANs API. Each record describes a VLAN configured within a Meraki network.
 The following table lists each Cisco Meraki attribute, its name as stored
 in Device Security , and the Device Security field it maps to (if applicable).

 Cisco Meraki Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 id 

 — 

 VLAN ID 

 VLAN ID 

 name 

 — 

 Device Name 

 VLAN name 

 network_name 

 — 

 Site 

 Network name 

 subnet 

 — 

 prefix; id 

 Subnet 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Cisco ISE Attribute Reference 

 Next 

 Cisco Prime Attribute Reference 

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
