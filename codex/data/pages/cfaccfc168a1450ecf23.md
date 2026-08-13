---
url: https://docs.paloaltonetworks.com/ngfw/help/11-2/network/network-network-profiles/network-network-profiles-bfd-profile/building-blocks-of-a-bfd-profile
fetched_at: 2026-08-13T16:48:00Z
source: palo-alto-main
---

# Building Blocks of a BFD Profile Clear

Building Blocks of a BFD Profile 

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

 Building Blocks of a BFD Profile 

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

 Network > Network Profiles 

 Network > Network Profiles > BFD Profile 

 Building Blocks of a BFD Profile 

 Download PDF 

 Next-Generation Firewall 

 Building Blocks of a BFD Profile 

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

 BFD Overview 

 Next 

 View BFD Summary and Details 

 Building Blocks of a BFD Profile 

 Network > Network Profiles
> BFD Profile 

 You can enable BFD for a static route or dynamic routing protocol
by applying the default BFD profile or a BFD profile that you create.
The default profile uses the default BFD settings and cannot be
changed. You can Add a new BFD profile and specify
the following information. 

 BFD Profile Settings 

 Description 

 Name 

 Name of the BFD profile (up to 31 characters).
The name is case-sensitive and must be unique on the firewall. Use
only letters, numbers, spaces, hyphens, and underscores. 

 Mode 

 Mode in which BFD operates: 

 Active —BFD
initiates sending control packets (default). At least one of the BFD
peers must be active; they can both be active. 

 Passive —BFD waits for the peer to
send control packets and responds as required. 

 Desired Minimum Tx Interval (ms) 

 Minimum interval (in milliseconds) at which
you want the BFD protocol to send BFD control packets. Minimum value
on PA-7000 Series, PA-5450, PA-5430, PA-5420, PA-5410, and PA-3400
Series is 50; minimum on PA‑3200 Series is 100; minimum on the PA-400
is 150; minimum on VM-Series is 200 (maximum value is 10,000; default
is 1000). 

 If you have multiple protocols
that use different BFD profiles on the same interface, configure
the BFD profiles with the same Desired Minimum Tx Interval . 

 Required Minimum Rx Interval (ms) 

 Minimum interval (in milliseconds) at which
BFD can receive BFD control packets. Minimum value on PA-7000 Series,
PA-5450, PA-5430, PA-5420, PA-5410, and PA-3400 Series is 50; minimum
on PA-3200 Series is 100; minimum on the PA-400 is 150; minimum
on VM-Series is 200 (maximum value is 10,000; default is 1000). 

 Detection Time Multiplier 

 The local system calculates the detection
time as the Detection Time Multiplier received
from the remote system multiplied by the agreed transmit interval
of the remote system (the greater of the Required Minimum
Rx Interval and the last received Desired
Minimum Tx Interval ). If BFD does not receive a BFD
control packet from its peer before the detection time expires,
a failure has occurred (range is 2 to 50; default is 3). 

 Hold Time (ms) 

 Delay (in milliseconds) after a link comes
up before the firewall transmits BFD control packets. Hold
Time applies to BFD Active mode only. If the firewall receives
BFD control packets during the Hold Time ,
it ignores them (range is 0-120000; default is 0). The default setting
of 0 means no transmit Hold Time is used;
the firewall sends and receives BFD control packets immediately
after the link is established. 

 Enable Multihop 

 Enables BFD over multiple hops. Applies
to BGP implementation only. 

 Minimum Rx TTL 

 Minimum Time-to-Live value (number of hops)
BFD will accept (receive) when it supports multihop BFD. Applies
to BGP implementation only (range is 1-254; there is no default). 

 Previous 

 BFD Overview 

 Next 

 View BFD Summary and Details 

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
