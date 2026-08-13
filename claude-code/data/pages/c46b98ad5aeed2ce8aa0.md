---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/high-availability/set-up-activepassive-ha
fetched_at: 2026-08-13T17:09:20Z
source: palo-alto-main
---

# Set
Up Active/Passive HA Clear

Set
Up Active/Passive HA 

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

 Set
Up Active/Passive HA 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

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

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 High Availability 

 Set
Up Active/Passive HA 

 Download PDF 

 Next-Generation Firewall 

 Set
Up Active/Passive HA 

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

 Session Setup 

 Next 

 Configuration Guidelines for Active/Passive HA 

 Set
Up Active/Passive HA 

 Ensure both firewalls have the same model, PAN-OS version, multi virtual system
 capability, and type of interfaces. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 For Strata Cloud Manager managed NGFWs: 

 Strata Cloud Manager Pro 

 Strata Cloud Manager Essentials 

 To set up high availability on your Palo Alto Networks firewalls, you need a pair of
 firewalls that meet the following requirements: 

 The same model —Both the firewalls in the pair must be of the same hardware
 model or virtual machine model. (Verify that by viewing Dashboard, General
 Information, Model.) 

 The same PAN-OS version —Both the firewalls should be running the same
 PAN-OS version and must each be up-to-date on the application, URL, and threat
 databases. (Verify that by viewing Dashboard, General Information, Software
 Version.) 

 The same multi virtual system capability—Both firewalls must have
 Multi Virtual System Capability either enabled or not
 enabled. When enabled, each firewall requires its own multiple virtual systems
 licenses. (Verify that by viewing Device > Setup > Management, General Settings,
 Multi Virtual System Capability enabled or disabled.) 

 ( Cloud Managed NGFWs Only ) —Both firewalls must have the
 multi-vsys capability disabled. 

 The same type of interfaces —Dedicated HA links, or a combination of the
 management port and in-band ports that are set to interface type 
 HA. (Verify the following on Device > High Availability > HA
 Communications.) 

 ( Cloud Managed NGFWs Only ) —Strata Cloud Manager supports
 IPv4 addresses only. 

 Determine the IP address for the HA1 (control) connection between the HA
 peers. The HA1 IP address for both peers must be on the same subnet if
 they are directly connected or are connected to the same switch. 

 For firewalls without dedicated HA ports, you can use the management port
 for the control connection. Using the management port provides a direct
 communication link between the management planes on both firewalls.
 However, because the management ports will not be directly cabled
 between the peers, make sure that you have a route that connects these
 two interfaces across your network. 

 If you use Layer 3 as the transport method for the HA2 (data) connection,
 determine the IP address for the HA2 link. Use Layer 3 only if the HA2
 connection must communicate over a routed network. The IP subnet for the
 HA2 links must not overlap with that of the HA1 links or with any other
 subnet assigned to the data ports on the firewall. 

 The same set of licenses —Licenses are unique to each firewall and cannot
 be shared between the firewalls. Therefore, you must license both firewalls
 identically. If both firewalls do not have an identical set of licenses, they
 cannot synchronize configuration information and maintain parity for a seamless
 failover. (Verify that the licenses match by comparing Device > Licenses.) 

 As a best practice, if you have an existing firewall and you want to add a
 new firewall for HA purposes and the new firewall has an existing
 configuration Reset the Firewall to Factory Default Settings on the new
 firewall. This ensures that the new firewall has a clean configuration.
 After HA is configured, you will then sync the configuration on the primary
 firewall to the newly introduced firewall with the clean configuration. 

 ( Cloud Managed NGFWs Only ) —Both firewalls in the HA pair must be
 added to the same folder. 

 Firewalls in an HA pair cannot be moved to a new folder. To move them, you must
 first break the HA configuration, move both firewalls to the new folder, and
 then reconfigure HA 

 LACP and LLDP Pre-Negotiation for Active/Passive HA 

 If a firewall uses LACP or LLDP, negotiation of those protocols upon failover
 prevents sub-second failover. However, you can enable an interface on a passive
 firewall to negotiate LACP and LLDP prior to failover. Thus, a firewall in Passive or Non-functional HA
 state can communicate with neighboring devices using LACP or LLDP. Such
 pre-negotiation speeds up failover. 

 All firewall models except VM-Series firewalls support a pre-negotiation
 configuration, which depends on whether the Ethernet or AE interface is in a Layer
 2, Layer 3, or virtual wire deployment. An HA passive firewall handles LACP and LLDP
 packets in one of two ways: 

 Active —The firewall has LACP or LLDP configured on the interface and
 actively participates in LACP or LLDP pre-negotiation, respectively. 

 Passive —LACP or LLDP is not configured on the interface and the
 firewall does not participate in the protocol, but allows the peers on
 either side of the firewall to pre-negotiate LACP or LLDP, respectively. 

 The following table displays which deployments are supported on Aggregate Ethernet
 (AE) and Ethernet interfaces. 

 Interface Deployment AE Interface Ethernet Interface 

 LACP in Layer 2 

 Active 

 Not supported 

 LACP in Layer 3 

 Active 

 Not supported 

 LACP in Virtual Wire 

 Not supported 

 Passive 

 LLDP in Layer 2 

 Active 

 Active 

 LLDP in Layer 3 

 Active 

 Active 

 LLDP in Virtual Wire 

 Active 

 Active if LLDP itself is configured. 

 Passive if LLDP itself is not configured. 

 Pre-negotiation is not supported on subinterfaces or tunnel interfaces. 

 To configure LACP or LLDP pre-negotiation, see the step (Optional) Enable LACP and LLDP
 Pre-Negotiation for Active/Passive HA for faster failover in your network uses
 LACP or LLAP . 

 Previous 

 Session Setup 

 Next 

 Configuration Guidelines for Active/Passive HA 

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

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
