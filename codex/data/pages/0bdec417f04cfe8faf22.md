---
url: https://docs.paloaltonetworks.com/iot/integration/attribute-reference/attribute-reference-aruba-clearpass
fetched_at: 2026-09-15T15:14:39Z
source: palo-alto-main
---

# Aruba ClearPass Attribute Reference Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

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

 Aruba WLAN Attribute Reference 

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

 Insight Endpoint Attributes 

 Device Security collects insight endpoint attributes from Aruba ClearPass. The following table lists each Aruba ClearPass attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Aruba ClearPass Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 user 

 aruba_clearpass.user 

 AD Username 

 User 

 domain 

 aruba_clearpass.domain 

 domain 

 Domain 

 device_name 

 aruba_clearpass.device_name 

 hostname 

 Device name 

 mac 

 aruba_clearpass.mac 

 id; MAC 

 Mac 

 mac 

 aruba_clearpass.mac_address 

 id; MAC 

 Mac 

 ip 

 aruba_clearpass.ip 

 IP Address 

 Ip 

 updated_at 

 aruba_clearpass.updated_at 

 Last Activity 

 Updated at 

 aruba_user_vlan 

 aruba_clearpass.aruba_user_vlan 

 VLAN ID 

 Aruba user vlan 

 aruba_user_role 

 aruba_clearpass.aruba_user_role 

 — 

 Aruba user role 

 device_category 

 aruba_clearpass.device_category 

 — 

 Device category 

 device_family 

 aruba_clearpass.device_family 

 — 

 Device family 

 ipv6 

 aruba_clearpass.ipv6 

 — 

 Ipv6 

 is_conflict 

 aruba_clearpass.is_conflict 

 — 

 Is conflict 

 is_online 

 aruba_clearpass.is_online 

 — 

 Is online 

 other_category 

 aruba_clearpass.other_category 

 — 

 Other category 

 other_family 

 aruba_clearpass.other_family 

 — 

 Other family 

 other_name 

 aruba_clearpass.other_name 

 — 

 Other name 

 roles 

 aruba_clearpass.roles 

 — 

 Roles 

 spt 

 aruba_clearpass.spt 

 — 

 Spt 

 Insight Session Attributes 

 Device Security collects insight session attributes from Aruba ClearPass. The following table lists each Aruba ClearPass attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Aruba ClearPass Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 username 

 aruba_clearpass.username 

 last_ad_username 

 Username associated with the device 

 ap_name 

 aruba_clearpass.ap_name 

 ap_name 

 Ap name 

 mac_address 

 aruba_clearpass.mac_address 

 id; MAC 

 Mac address 

 framedipaddress 

 aruba_clearpass.framedipaddress 

 IP Address 

 Framedipaddress 

 ssid 

 aruba_clearpass.ssid 

 SSID 

 Ssid 

 arubauservlan 

 aruba_clearpass.arubauservlan 

 VLAN ID 

 Arubauservlan 

 acct_id 

 aruba_clearpass.acct_id 

 — 

 Acct ID 

 acctinputoctets 

 aruba_clearpass.acctinputoctets 

 — 

 Acctinputoctets 

 acctoutputoctets 

 aruba_clearpass.acctoutputoctets 

 — 

 Acctoutputoctets 

 acctsessionid 

 aruba_clearpass.acctsessionid 

 — 

 Acctsessionid 

 acctsessiontime 

 aruba_clearpass.acctsessiontime 

 — 

 Acctsessiontime 

 acctstarttime 

 aruba_clearpass.acctstarttime 

 — 

 Acctstarttime 

 acctstoptime 

 aruba_clearpass.acctstoptime 

 — 

 Acctstoptime 

 acctterminatecause 

 aruba_clearpass.acctterminatecause 

 — 

 Acctterminatecause 

 arubauserrole 

 aruba_clearpass.arubauserrole 

 — 

 Arubauserrole 

 calledstationid 

 aruba_clearpass.calledstationid 

 — 

 Calledstationid 

 callingstationid 

 aruba_clearpass.callingstationid 

 — 

 Callingstationid 

 cppm_uuid 

 aruba_clearpass.cppm_uuid 

 — 

 Cppm uuid 

 id 

 aruba_clearpass.id 

 — 

 Id 

 nas_name 

 aruba_clearpass.nas_name 

 — 

 Nas name 

 nasipaddress 

 aruba_clearpass.nasipaddress 

 — 

 Nasipaddress 

 nasportid 

 aruba_clearpass.nasportid 

 — 

 Nasportid 

 nasporttype 

 aruba_clearpass.nasporttype 

 — 

 Nasporttype 

 role_name 

 aruba_clearpass.role_name 

 — 

 Role name 

 servicetype 

 aruba_clearpass.servicetype 

 — 

 Servicetype 

 state 

 aruba_clearpass.session.state 

 — 

 State 

 sponsor_email 

 aruba_clearpass.sponsor_email 

 — 

 Sponsor email 

 sponsor_name 

 aruba_clearpass.sponsor_name 

 — 

 Sponsor name 

 sponsor_profile_name 

 aruba_clearpass.sponsor_profile_name 

 — 

 Sponsor profile name 

 state 

 aruba_clearpass.state 

 — 

 State 

 total_traffic 

 aruba_clearpass.total_traffic 

 — 

 Total traffic 

 updated_at 

 aruba_clearpass.updated_at 

 — 

 Updated at 

 visitor_carrier 

 aruba_clearpass.visitor_carrier 

 — 

 Visitor carrier 

 visitor_company 

 aruba_clearpass.visitor_company 

 — 

 Visitor company 

 visitor_name 

 aruba_clearpass.visitor_name 

 — 

 Visitor name 

 visitor_phone 

 aruba_clearpass.visitor_phone 

 — 

 Visitor phone 

 Insight Wired Session Attributes 

 Device Security collects insight wired session attributes from Aruba ClearPass. The following table lists each Aruba ClearPass attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Aruba ClearPass Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 username 

 aruba_clearpass.username 

 AD Username 

 Username associated with the device 

 mac_address 

 aruba_clearpass.mac_address 

 id; MAC 

 Mac address 

 framedipaddress 

 aruba_clearpass.framedipaddress 

 IP Address 

 Framedipaddress 

 nasipaddress 

 aruba_clearpass.nasipaddress 

 Switch IP 

 Nasipaddress 

 calledstationid 

 aruba_clearpass.calledstationid 

 Switch MAC 

 Calledstationid 

 nas_name 

 aruba_clearpass.nas_name 

 switch_name 

 Nas name 

 arubauservlan 

 aruba_clearpass.arubauservlan 

 VLAN ID 

 Arubauservlan 

 acct_id 

 aruba_clearpass.acct_id 

 — 

 Acct ID 

 acctinputoctets 

 aruba_clearpass.acctinputoctets 

 — 

 Acctinputoctets 

 acctoutputoctets 

 aruba_clearpass.acctoutputoctets 

 — 

 Acctoutputoctets 

 acctsessionid 

 aruba_clearpass.acctsessionid 

 — 

 Acctsessionid 

 acctsessiontime 

 aruba_clearpass.acctsessiontime 

 — 

 Acctsessiontime 

 acctstarttime 

 aruba_clearpass.acctstarttime 

 — 

 Acctstarttime 

 acctstoptime 

 aruba_clearpass.acctstoptime 

 — 

 Acctstoptime 

 acctterminatecause 

 aruba_clearpass.acctterminatecause 

 — 

 Acctterminatecause 

 ap_name 

 aruba_clearpass.ap_name 

 — 

 Ap name 

 arubauserrole 

 aruba_clearpass.arubauserrole 

 — 

 Arubauserrole 

 callingstationid 

 aruba_clearpass.callingstationid 

 — 

 Callingstationid 

 cppm_uuid 

 aruba_clearpass.cppm_uuid 

 — 

 Cppm uuid 

 id 

 aruba_clearpass.id 

 — 

 Id 

 nasportid 

 aruba_clearpass.nasportid 

 — 

 Nasportid 

 nasporttype 

 aruba_clearpass.nasporttype 

 — 

 Nasporttype 

 role_name 

 aruba_clearpass.role_name 

 — 

 Role name 

 servicetype 

 aruba_clearpass.servicetype 

 — 

 Servicetype 

 state 

 aruba_clearpass.session.state 

 — 

 State 

 sponsor_email 

 aruba_clearpass.sponsor_email 

 — 

 Sponsor email 

 sponsor_name 

 aruba_clearpass.sponsor_name 

 — 

 Sponsor name 

 sponsor_profile_name 

 aruba_clearpass.sponsor_profile_name 

 — 

 Sponsor profile name 

 ssid 

 aruba_clearpass.ssid 

 — 

 Ssid 

 state 

 aruba_clearpass.state 

 — 

 State 

 total_traffic 

 aruba_clearpass.total_traffic 

 — 

 Total traffic 

 updated_at 

 aruba_clearpass.updated_at 

 — 

 Updated at 

 visitor_carrier 

 aruba_clearpass.visitor_carrier 

 — 

 Visitor carrier 

 visitor_company 

 aruba_clearpass.visitor_company 

 — 

 Visitor company 

 visitor_name 

 aruba_clearpass.visitor_name 

 — 

 Visitor name 

 visitor_phone 

 aruba_clearpass.visitor_phone 

 — 

 Visitor phone 

 Endpoint Attributes 

 Device Security collects endpoint attributes from Aruba ClearPass. The following table lists each Aruba ClearPass attribute, its name as stored in Device Security , and the Device Security field it maps to (if applicable).

 Aruba ClearPass Attribute 

 Device Security Attribute Name 

 Device Security Common Attribute* 

 Description 

 mac_address 

 aruba_clearpass.mac_address 

 MAC; id 

 Mac address 

 added_at 

 aruba_clearpass.added_at 

 — 

 Added at 

 attributes 

 aruba_clearpass.attributes 

 — 

 Attributes 

 id 

 aruba_clearpass.id 

 — 

 Id 

 randomized_mac 

 aruba_clearpass.randomized_mac 

 — 

 MAC address of the randomized 

 status 

 aruba_clearpass.status 

 — 

 Status of the device 

 updated_at 

 aruba_clearpass.updated_at 

 — 

 Updated at 

 * Only some attributes map to a Device Security Common Attribute. 

 Previous 

 Aruba Central Attribute Reference 

 Next 

 Aruba WLAN Attribute Reference
