---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/incidents-and-alerts/api-changes-for-network-secure-fabric-link-event-codes
fetched_at: 2026-08-13T17:29:30Z
source: palo-alto-main
---

# API Changes for Network Secure Fabric Link Event Codes Clear

API Changes for Network Secure Fabric Link Event Codes 

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

 API Changes for Network Secure Fabric Link Event Codes 

 Updated on 

 Wed Feb 25 07:20:45 PST 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Wed Feb 25 07:20:45 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 API Changes for Network Secure Fabric Link Event Codes 

 Download PDF 

 Prisma SD-WAN 

 API Changes for Network Secure Fabric Link Event Codes 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Event Category-User ID 

 Next 

 Setup Incident Policies 

 API Changes for Network Secure Fabric Link Event Codes 

 API Changes for Network Secure Fabric Link Event Codes in Prima SD-WAN. You must use
 the two new filters for Include Suppressed and Show Only Suppressed in the incident
 management. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 The new Secure Fabric Link incident category in 5.4.1 summarizes VPN
 incidents between a branch and a data center or between two branches into two groups:
 NETWORK_SECUREFABRICLINK_DEGRADED and NETWORK_SECUREFABRICLINK_DOWN. 

 With this change, the following VPN incidents that identify link connectivity issues are
 now grouped into one of the two Secure Fabric Link incidents: 

 NETWORK_VPNLINK_DOWN 

 NETWORK_VPNPEER_UNAVAILABLE 

 NETWORK_VPNSS_UNAVAILABLE 

 NETWORK_VPNPEER_UNREACHABLE 

 NETWORK_VPNSS_MISMATCH 

 And if the root cause for the links connectivity issues is one of the following incident
 codes, the Secure Fabric Link incident is suppressed: 

 DEVICEHW_INTERFACE_DOWN 

 NETWORK_DIRECTINTERNET_DOWN 

 NETWORK_DIRECTPRIVATE_DOWN 

 To view the suppressed incidents, you must use the two new filters for Include Suppressed
 and Show Only Suppressed in the incident management window. 

 The following is a sample API response. 

 Before Version 5.4.1 Starting Version 5.4.1 

 {"_created_on_utc": "2020-07-21T19:09:13.454000Z",
 "_etag": 1, "_updated_on_utc": "2020-07-21T19:09:13.454000Z",
 "acknowledged": False, "acknowledgement_info": None, "cleared": False,
 "code": "NETWORK_VPNLINK_DOWN", "correlation_id": "NW6JYud4",
 "element_id": "14999711939070152", "entity_ref":
 "tenants/1092/sites/14994575835930104", "id":
 "5f173d59d7b0fa339626dc98", "info":{ "al_id": "15809335672920128",
 "vpn_link_id": "15953585219130188" }, "severity": "major", "site_id":
 "14994575835930104", "time": "2020-07-21T19:09:12.346000Z", "type":
 "alarm" { "info": { "vpnlinks": [ "15821811883320202" ] },
 "acknowledgement_info": None, "type": "alarm", "severity": "major",
 "_updated_on_utc": "2020-06-02T20:27:16.855000Z", "site_id":
 "14764819359580119", "notes": "Test Notes", "acknowledged": False,
 "cleared": False, "id": "5ed593d2a09dee5049286694", "entity_ref":
 "tenants/1092/anynetlinks/15507065212560023", "correlation_id":
 "h76a6B6X", "code": "NETWORK_ANYNETLINK_DOWN", "suppressed_info": {
 "event_ids": [ "5ed593d1a09dee5049286689", "5ed593d2a09dee5049286692",
 "5ed6b624a09dee58c781256b" ], "other_reason": None, "suppressed_time":
 "2020-06-02T20:27:16.855000Z", "rule_id": None }, "time":
 "2020-06-01T23:48:34.353000Z", "element_id": None, "_created_on_utc":
 "2020-06-01T23:48:34.379000Z", "suppressed": True, "_etag": 4} 

 The API response highlights the new attributes in the 5.4.1 event structure: 

 entity_ref for NETWORK_ANYNETLINK_DOWN incidents will now point to anynetlinks
 instead of pointing to the site. 

 info attribute for NETWORK_ANYNETLINK_DOWN will contain a list of VPN IDs. 

 suppressed_info includes event IDs only if suppressed is True. With the list of
 relevant event IDs that are suppressed, the suppressed_time timestamp is added.
 (Note: other_reason and rule_id are intended for future use). 

 notes to add remarks/comments to events. You can edit notes for active incidents
 only. 

 When querying for events using the API, replace the code for: 

 NETWORK_SECUREFABRICLINK_DOWN with NETWORK_ANYNETLINK_DOWN 

 NETWORK_SECUREFABRICLINK_DEGRADED with NETWORK_ANYNETLINK_DEGRADED 

 For example: { "limit":{ "count":100, "sort_on":"time",
 "sort_order":"descending" }, "severity":[], "acknowledged":False, "start_time":None,
 "query":{ "site":[], "category":[], "code":["NETWORK_ANYNETLINK_DOWN"],
 "correlation_id":[], "type":["alarm"] }} 

 Previous 

 Event Category-User ID 

 Next 

 Setup Incident Policies 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 Incidents & Alerts 

 Prisma SASE 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
