---
url: https://docs.paloaltonetworks.com/ngfw/help/11-2/network/network-routing-routing-profiles/network-routing-routing-profiles-bfd
fetched_at: 2026-08-13T16:48:09Z
source: palo-alto-main
---

# Network > Routing > Routing Profiles > BFD Clear

Network > Routing > Routing Profiles > BFD 

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

 Network > Routing > Routing Profiles > BFD 

 Updated on 

 Thu Jun 25 17:41:47 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Thu Jun 25 17:41:47 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Network 

 Network > Routing > Routing Profiles 

 Network > Routing > Routing Profiles > BFD 

 Download PDF 

 Next-Generation Firewall 

 Network > Routing > Routing Profiles > BFD 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Network > Routing > Routing Profiles > BGP 

 Next 

 Network > Routing > Routing Profiles > OSPF 

 Network > Routing > Routing Profiles > BFD 

 Create a BFD profile. 

 Create a Bidirectional Forwarding Detection
profile . 

 BFD Routing Profiles 

 Description 

 Name 

 Enter a name for the BFD profile (maximum
of 63 characters). The name must start with an alphanumeric character,
underscore (_), or hyphen (-), and contain zero or more alphanumeric
characters, underscore (_) or hyphen(-). No dot (.) or space is
allowed. 

 Mode 

 Select mode: 

 Active —(default)
BFD initiates sending control packets to peer. At least one of the BFD
peers must be Active; both can be Active. 

 Passive —BFD waits for peer to send control packets and
responds as required. 

 Desired Minimum Tx Interval (ms) 

 Minimum interval, in milliseconds, at which
you want the BFD protocol to send BFD control packets; you are thus
negotiating the transmit interval with the peer. Range for PA-7000 Series,
PA-5200 Series, PA-5400 Series, and PA-3400 Series is 50 to 10,000;
range for PA-3200 Series is 100 to 10,000; range for PA-400 Series
is 150 to 10,000; range for VM-Series is 200 to 10,000; default
is 1,000. 

 Desired Minimum Rx Interval (ms) 

 Minimum interval, in milliseconds, at which
BFD can receive BFD control packets. Range for PA-7000 Series, PA-5200
Series, PA-5400 Series, and PA-3400 Series is 50 to 10,000; range
for PA-3200 Series is 100 to 10,000; range for PA-400 Series is
150 to 10,000; range for VM-Series is 200 to 10,000; default is 1,000. 

 Detection Time Multiplier 

 Range is 2 to 255; default is 3. 

 The
local system calculates the detection time as the Detection
Time Multiplier received from the remote system multiplied
by the agreed transmit interval of the remote system (the greater
of the Required Minimum Rx Interval and the
last received Desired Minimum Tx Interval ).
If BFD does not receive a BFD control packet from its peer before
the detection time expires, a failure has occurred. 

 Hold Time (ms) 

 Delay, in milliseconds, after a link comes
up before BFD transmits BFD control packets. Hold Time applies
to BFD Active mode only. If BFD receives
BFD control packets during the Hold Time, it ignores them. Range
is 0 to 120,000; default is 0, which means no transmit Hold Time
is used; BFD sends and receives BFD control packets immediately
after the link is established. 

 Enable Multihop 

 Enable BFD over BGP multihop. 

 Minimum Rx TTL 

 Enter the minimum Time-to-Live (number of hops)
BFD will accept (receive) in a BFD control packet when BGP supports
multihop BFD. Range is 1 to 254; there is no default. 

 Previous 

 Network > Routing > Routing Profiles > BGP 

 Next 

 Network > Routing > Routing Profiles > OSPF 

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

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 11.2 

 Help 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
