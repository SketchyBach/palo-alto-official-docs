---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-networking-admin/configure-interfaces/layer-2-interfaces/configure-a-layer-2-interface
fetched_at: 2026-08-13T17:10:46Z
source: palo-alto-main
---

# Configure a Layer 2 Interface Clear

Configure a Layer 2 Interface 

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

 Configure a Layer 2 Interface 

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

 Layer 2 Interfaces 

 Configure a Layer 2 Interface 

 Download PDF 

 Next-Generation Firewall 

 Configure a Layer 2 Interface 

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

 Layer 2 Interfaces 

 Next 

 Configure a Layer 2 Interface, Subinterface, and VLAN 

 Configure a Layer 2 Interface 

 Configure a Layer2 interface for switching; this task is for when you aren't using
 VLANs. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 One of these licenses when using Strata Cloud Manager: 

 Strata Cloud Manager Essentials 

 Strata Cloud Manager Pro 

 Configure a Layer 2 interface on the firewall so it can act as a switch in your layer
 2 network (not at the edge of the network). The Layer 2 hosts are probably
 geographically close to each other and belong to a single broadcast domain. The
 firewall provides security between the Layer 2 hosts when you assign the interfaces
 to security zones and apply security rules to the zones. 

 The hosts communicate with the firewall and each other at Layer 2 of the OSI model by
 exchanging frames. A frame contains an Ethernet header that includes a source and
 destination Media Access Control (MAC) address, which is a physical hardware
 address. MAC addresses are 48-bit hexadecimal numbers formatted as six octets
 separated by a colon or hyphen (for example, 00-85-7E-46-F1-B2). 

 The following figure has a firewall with three Layer 2 interfaces that each connect
 to a Layer 2 host in a one-to-one mapping. 

 The firewall begins with an empty MAC table. When the host with source address
 0A-76-F2-60-EA-83 sends a frame to the firewall, the firewall doesn’t have
 destination address 0B-68-2D-05-12-76 in its MAC table, so it doesn’t know which
 interface to forward the frame to; it broadcasts the frame to all of its Layer 2
 interfaces. The firewall puts source address 0A-76-F2-60-EA-83 and associated Eth1/1
 into its MAC table. 

 The host at 0C-71-D4-E6-13-44 receives the broadcast, but the destination MAC address
 is not its own MAC address, so it drops the frame. 

 The receiving interface Ethernet 1/2 forwards the frame to its host. When host
 0B-68-2D-05-12-76 responds, it uses the destination address 0A-76-F2-60-EA-83, and
 the firewall adds to its MAC table Ethernet 1/2 as the interface to reach
 0B-68-2D-05-12-76. 

 Configure a Layer 2 interface with no VLANs when you want Layer 2 switching and you
 don’t need to separate traffic among VLANs. 

 PAN-OS & Panorama 

 Strata Cloud Manager 

 Configure a Layer 2 Interface (PAN-OS) 

 Procedure for configuring a Layer 2 interface in PAN-OS and Panorama. 

 Configure a Layer 2 interface. 

 Select Network Interfaces Ethernet and select an interface. The Interface
 Name is fixed, such as ethernet1/1. 

 For Interface Type , select
 Layer2 . 

 Select the Config tab and assign the interface
 to a Security Zone or create a New
 Zone . 

 Configure additional Layer 2 interfaces on the firewall that connect to
 other Layer 2 hosts. 

 ( Optional ) ( PAN-OS 12.2.2 and later versions ) To
 apply port-level STP parameters, in the STP tab,
 select the STP port profile you created. If no port profile is selected,
 default STP parameters are applied to the port. Optionally, specify the
 STP Port Priority and Path
 Cost to override the default values applied to the port.
 See Configure Spanning Tree
 Protocol . 

 Commit. 

 Click OK and Commit . 

 Configure a Layer 2 Interface (SCM) 

 Procedure for creating a Layer 2 interface in Strata Cloud Manager. 

 Log in to Strata Cloud Manager . 

 Select Manage Configuration NGFW and Prisma Access Device Settings Interfaces Ethernet Configuration NGFW and Prisma Access Device Settings Interfaces Ethernet and select the Configuration Scope where you want to create the
 Layer 2 interface. 

 Select a firewall from your Folders or select
 Snippets to configure the Layer 2 interface in a
 snippet. 

 If you select a folder or select a snippet, you create a Layer 2 interface
 variable that must be assigned at the device level. 

 Add the interface. 

 If you’re configuring a Layer 2 interface for a specific firewall, select
 the interface you want to configure instead. 

 Folders and Snippets — Add Interface and
 select Interface . 

 Firewalls — Add and Add
 Interface . 

 Configure the interface. 

 If you’re configuring an interface in the folder or snippet scope, the
 interface configuration is pushed only to firewalls that have the
 corresponding interface slot available. For example, if you configure
 Ethernet 1/5 in the folder scope and the firewall associated with the folder
 has only four interface slots, then the configuration isn’t pushed to the
 firewall. 

 Select the interface Slot . 

 Select the Interface Name . 

 When you configure an interface for a specific firewall, the
 Interface Name is fixed, such as
 ethernet1/1 if you select Slot
 1. The fixed interface names are dependent on the slot that you
 selected in the previous step. 

 ( Folders and Snippets only ) Select the Default
 Interface Assignment . 

 ( Optional ) Enter a Description . 

 For Interface Type , select
 Layer2 . 

 ( Folders and Snippets only, Optional ) Assign
 Interface to VLAN Tag to add the interface to a VLAN.

 ( Folders and Snippets only; Recommended ) Assign the interface
 to a Zone . 

 Create New to create a new zone. See Zone Protection and DoS
 Protection for more information. 

 Selecting an inherited zone overrides the previous settings and
 removes any inherited objects. Any changes made to the global folder
 are no longer inherited in a top-down manner. A message appears,
 indicating that the interface settings will be overridden and the
 inherited objects from the parent folder will be removed on all
 firewalls. When you save your changes, a confirmation message
 appears. If you confirm, the zone is overridden. 

 ( Optional ) Configure the interface link settings. 

 Select the interface Link Speed . 

 Auto is selected by default and allows the
 firewall to determine the speed. 

 Select the interface Link Duplex transmission
 mode. 

 Auto is selected by default to allow the
 firewall to negotiate the transmission mode automatically. 

 Select the interface Link State . 

 Auto detect is selected by default to allow
 the firewall to determine the link state. 

 Save . 

 Create a Security policy rule to allow the traffic through the tap
 interface. 
 When creating a Security policy rule for a tap interface, both the source zone
 and destination zone must be the same. 

 Select Manage Configuration Security Services Security Policy Configuration NGFW and Prisma Access Security Services Security Policy and Add Rule . 

 For the Source, Add Zones and select the zone
 you created in the previous step. 

 For the Destination, Add Zones and select the
 zone you created in the previous step. 

 Set all of the Security policy rule match criteria (Applications, User,
 Service, Address) to any . 

 For the Action and Advanced Inspection, set the Action to
 Allow . 

 Expand the Advanced Settings and for the Log
 Settings, set Log at Session End . 

 Save . 

 Push Config to push your configuration changes. 

 Previous 

 Layer 2 Interfaces 

 Next 

 Configure a Layer 2 Interface, Subinterface, and VLAN 

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

 Networking 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
