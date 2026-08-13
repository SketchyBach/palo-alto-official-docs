---
url: https://docs.paloaltonetworks.com/ngfw/networking/configure-interfaces/cellular-interfaces/configure-multiple-apn-dnn-sessions
fetched_at: 2026-08-13T16:53:47Z
source: palo-alto-main
---

# Configure Multiple APN and DNN Sessions Clear

Configure Multiple APN and DNN Sessions 

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

 Configure Multiple APN and DNN Sessions 

 Updated on 

 Tue Aug 04 17:04:37 PDT 2026 

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

 Tue Aug 04 17:04:37 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Configure Interfaces 

 Cellular Interfaces 

 Configure Multiple APN and DNN Sessions 

 Download PDF 

 Next-Generation Firewall 

 Configure Multiple APN and DNN Sessions 

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

 Configure DHCP Relay over a Cellular Interface 

 Next 

 Upgrade 5G Firmware 

 Configure Multiple APN and DNN Sessions 

 Configure APN and DNN cellular subinterfaces on a 5G-integrated firewall to run
 independent data sessions on separate security zones and routing domains. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 PAN-OS 12.2.2 or later 

 One of the supported 5G-integrated firewalls listed in
 the Mobile Network
 Infrastructure Feature Support compatibility
 matrix 

 The Multiple APN/DNN feature enables the establishment and maintenance of
 parallel, concurrent sessions across 4G LTE and 5G cellular networks, allowing for
 granular traffic segmentation, custom QoS definitions, and differentiated security
 policies. Beginning with PAN-OS® 12.2.2, you can run up to eight concurrent access
 point name (APN) sessions on 4G LTE networks or up to eight concurrent data network
 name (DNN) sessions on 5G standalone (SA) networks, or a combination of APN and DNN
 up to eight. Each session maps to a dedicated cellular subinterface with its own IP
 address, default gateway, routing domain, and security zone, letting you isolate
 workloads, apply distinct security policies per traffic type, and route different
 applications to different carrier connections—all on a single firewall. 

 Each additional APN or DNN session is provisioned as a cellular
 subinterface. The unit number assigned to a subinterface determines which SIM slot
 carries the session: units 1 through 7 use SIM slot 1, and units 8 through 14 use
 SIM slot 2. For example, on a single-modem firewall, Cellular1/1.1 through
 Cellular1/1.7 carry SIM 1 sessions and Cellular1/1.8 through Cellular1/1.14 carry
 SIM 2 sessions. On dual-modem platforms, each modem has its own parent cellular
 interface and follows the same unit-numbering scheme. The parent cellular interface
 (without a unit suffix) continues to carry the primary APN session and behaves the
 same way it did in earlier releases, so single-APN deployments require no changes.
 DNN sessions are handled in the same way as APN sessions, along with the network
 slicing. 

 APN and DNN both define how the firewall establishes a carrier data
 session, but they apply to different network generations. An APN identifies the
 packet data network that the firewall connects to through an Evolved Packet Core
 (EPC) in 4G LTE deployments. A DNN serves the same purpose in 5G SA networks, where
 the firewall establishes protocol data unit (PDU) sessions through a 5G Core (5GC).
 DNN profiles additionally support S-NSSAI (Single Network Slice Selection Assistance
 Information): you specify a Slice/Service Type (SST) value in the range 0–255 and an
 optional 24-bit Slice Differentiator (SD) to map the DNN session to a specific 5G
 network slice. The subinterface paradigm is the same for both APN and DNN
 configurations. 

 APN and DNN profiles are centrally managed under Network Network Profiles Cellular APN/DNN Profile . You create a profile there and then assign it to the parent cellular
 interface or to individual subinterfaces. Subinterfaces inherit advanced cellular
 settings from the parent interface (exceptions are radio band preferences, GPS, DHCP
 relay, and SIM configuration). You configure each subinterface's security zone,
 virtual or logical router, and other configuration parameters independently. For
 example, you can use policy-based forwarding (PBF) to steer traffic to the
 appropriate subinterface based on source address, destination address, port, or
 application. In Panorama, APN/DNN profiles are available under Templates Network Network Profiles Cellular APN/DNN Profile and push to managed firewalls through the standard template
 mechanism. Committing a multiple APN or DNN configuration does not require a
 firewall reboot. 

 Configure Multiple APNs 

 Create APN profiles and assign them to cellular subinterfaces to run multiple
 4G LTE data sessions simultaneously on the same firewall. Each subinterface
 carries a separate APN connection with independent IP addressing and
 routing. 

 Create one or more APN profiles. 

 Select Network Network Profiles Cellular APN/DNN Profile and click Add . 

 For Type , choose
 APN . 

 Enter a Profile Name and the APN
 Name as provided by your carrier. 

 ( Optional ) Select a PDP Type and
 configure Authentication Type with
 credentials if your carrier requires authentication. 

 Click OK and repeat for each additional
 APN. 

 Select Network Interfaces Cellular and select the cellular interface you want to
 configure. 

 On the parent interface, assign the primary APN profile to the appropriate
 SIM slot and click OK . 

 Add cellular subinterfaces for each additional APN session. 

 On the Subinterfaces tab, click
 Add . 

 Enter a unit number: 1–7 for SIM slot 1 sessions, or 8–14 for SIM
 slot 2 sessions. 

 Choose the SIM Slot that corresponds to the
 unit number range. 

 For APN/DNN Profile , choose the APN profile
 to assign to this subinterface. 

 Click OK and repeat for each additional
 subinterface. 

 For each subinterface, configure the Security Zone 
 and Virtual Router settings on the
 IPv4 tab. 

 Configure policy-based forwarding (PBF) rules to steer traffic to the
 appropriate APN subinterface based on source address, destination address,
 port, or application. 

 Commit . 

 A reboot is not required after committing APN subinterface
 configurations. 

 Configure Multiple DNNs 

 Create DNN profiles and assign them to cellular subinterfaces to run multiple
 5G SA data sessions simultaneously. For network slicing deployments, configure
 S-NSSAI values on each DNN profile to map sessions to specific 5G network
 slices before assigning the profiles to subinterfaces. 

 Create one or more DNN profiles. 

 Select Network Network Profiles Cellular APN/DNN Profile and click Add . 

 For Type , choose
 DNN . 

 Enter a Profile Name and the DNN
 Name as provided by your carrier. 

 ( Optional ) Select a PDP Type and
 configure Authentication Type with
 credentials if your carrier requires authentication. 

 ( Optional ) For network slicing, enter the
 Slice/Service Type (SST) value in the
 range 0–255, and enter the Slice
 Differentiator (SD) if your carrier requires
 it. 

 Click OK and repeat for each additional
 DNN. 

 Select Network Interfaces Cellular and select the cellular interface you want to
 configure. 

 On the parent interface, assign the primary DNN profile to the appropriate
 SIM slot and click OK . 

 Add cellular subinterfaces for each additional DNN session. 

 On the Subinterfaces tab, click
 Add . 

 Enter a unit number: 1–7 for SIM slot 1 sessions, or 8–14 for SIM
 slot 2 sessions. 

 Choose the SIM Slot that corresponds to the
 unit number range. 

 For APN/DNN Profile , choose the DNN profile
 to assign to this subinterface. 

 Click OK and repeat for each additional
 subinterface. 

 For each subinterface, configure the Security Zone 
 and Virtual Router settings on the
 IPv4 tab. 

 Configure policy-based forwarding (PBF) rules to steer traffic to the
 appropriate DNN subinterface. 

 Commit . 

 A reboot is not required after committing DNN subinterface
 configurations. 

 Verify the DNN sessions are active. 

 show cellular dnn 

 show cellular session detail 

 Previous 

 Configure DHCP Relay over a Cellular Interface 

 Next 

 Upgrade 5G Firmware 

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

 Interfaces 

 Mobile Network Infrastructure 

 12.2 

 PAN-OS 

 Next-Generation Firewall 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
