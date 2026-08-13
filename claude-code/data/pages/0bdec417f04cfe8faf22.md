---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-aruba-clearpass
fetched_at: 2026-08-13T16:36:58Z
source: palo-alto-main
---

# Aruba ClearPass Attribute Reference Clear

Aruba ClearPass Attribute Reference 

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

 Aruba ClearPass Attribute Reference 

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

 Aruba ClearPass Attribute Reference 

 Download PDF 

 Device Security 

 Aruba ClearPass Attribute Reference 

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

 Aruba Central Attribute Reference 

 Next 

 Aruba WLC Attribute Reference 

 Aruba ClearPass Attribute Reference 

 This reference lists the attributes that Device Security collects from Aruba ClearPass,
 their names as stored in Device Security , and the Device Security fields they map to.

 When Device Security integrates with Aruba ClearPass , it imports network
 access control data to enrich the device inventory. The attributes in this reference
 cover endpoint records and session data for both wireless and wired clients. 

 The third-party attribute name in Device Security refers to the attribute name
 as it appears in the Assets Inventory table and in Query Engine. This follows the format
 of third-party-name . attribute-name .
 When viewing the attribute name in the Assets Inventory table column selector or on a
 Device Details page, where the third-party name can be found as a header for the
 attributes section, then the third-party name is removed from the attribute name.

 For example, micrsoft_defender_xdr.macAddress would appear in the
 Query Builder and in the Assets Inventory table, but under Device Details Attributes Integration Specific Attributes Microsoft Defender , the attribute would appear as macAddress .

 Endpoint Attributes 

 Device Security collects endpoint attributes from the Aruba ClearPass Insight endpoint API. Each record describes a network endpoint profiled by ClearPass.

 Aruba ClearPass Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 roles 

 aruba_clearpass.roles 

 — 

 Roles 

 aruba_user_role 

 aruba_clearpass.aruba_user_role 

 — 

 Aruba user role 

 device_name 

 aruba_clearpass.device_name 

 Hostname 

 Device name 

 aruba_user_vlan 

 aruba_clearpass.aruba_user_vlan 

 — 

 Aruba user VLAN 

 is_conflict 

 aruba_clearpass.is_conflict 

 — 

 Indicates whether the session has a conflict 

 user 

 aruba_clearpass.user 

 — 

 User 

 updated_at 

 aruba_clearpass.updated_at 

 — 

 Last updated timestamp 

 is_online 

 aruba_clearpass.is_online 

 — 

 Indicates whether the device is online 

 device_family 

 aruba_clearpass.device_family 

 — 

 Device family 

 device_category 

 aruba_clearpass.device_category 

 — 

 Device category 

 ip 

 aruba_clearpass.ip 

 ipv4_address 

 IP address 

 mac 

 aruba_clearpass.mac 

 id; MAC 

 MAC address 

 domain 

 aruba_clearpass.domain 

 — 

 Domain 

 spt 

 aruba_clearpass.spt 

 — 

 SPT value 

 ipv6 

 aruba_clearpass.ipv6 

 — 

 IPv6 address 

 Wireless Session Attributes 

 Device Security collects wireless session attributes from the Aruba ClearPass Insight session API. Each record describes an active or recent wireless authentication session.

 Aruba ClearPass Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 updated_at 

 aruba_clearpass.updated_at 

 — 

 Last updated timestamp 

 ap_name 

 aruba_clearpass.ap_name 

 Access Point Name 

 AP name 

 framedipaddress 

 aruba_clearpass.framedipaddress 

 ipv4_address 

 Framed IP address 

 ssid 

 aruba_clearpass.ssid 

 SSID 

 SSID 

 mac_address 

 aruba_clearpass.mac_address 

 id; MAC 

 MAC address 

 state 

 aruba_clearpass.session.state 

 — 

 State 

 nas_name 

 aruba_clearpass.nas_name 

 — 

 NAS name 

 nasporttype 

 — 

 aruba_clearp__nasporttype 

 NAS port type 

 nasportid 

 aruba_clearpass.nasportid 

 — 

 NAS port ID 

 calledstationid 

 aruba_clearpass.calledstationid 

 — 

 Called station ID 

 callingstationid 

 aruba_clearpass.callingstationid 

 — 

 Calling station ID 

 arubauservlan 

 aruba_clearpass.arubauservlan 

 VLAN ID 

 Aruba user VLAN ID 

 arubauserrole 

 aruba_clearpass.arubauserrole 

 — 

 Aruba user role 

 nasipaddress 

 aruba_clearpass.nasipaddress 

 — 

 NAS IP address 

 username 

 aruba_clearpass.username 

 last_ad_username 

 Username 

 Wired Session Attributes 

 Device Security collects wired session attributes from the Aruba ClearPass Insight wired session API. Each record describes a wired authentication session.

 Aruba ClearPass Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 calledstationid 

 — 

 Switch MAC 

 Called station ID 

 nasipaddress 

 — 

 Switch IP 

 NAS IP address 

 nas_name 

 — 

 switch_name 

 NAS name 

 framedipaddress 

 — 

 ipv4_address 

 Framed IP address 

 mac_address 

 — 

 id; MAC 

 MAC address 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Aruba Central Attribute Reference 

 Next 

 Aruba WLC Attribute Reference 

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
