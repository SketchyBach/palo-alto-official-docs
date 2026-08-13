---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-release-notes/features-introduced-in-pan-os/iot-security-features
fetched_at: 2026-08-13T17:12:04Z
source: palo-alto-main
---

# IoT Security Features Clear

IoT Security Features 

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

 IoT Security Features 

 Updated on 

 Tue Aug 11 16:14:24 PDT 2026 

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

 Updated on 

 Tue Aug 11 16:14:24 PDT 2026 

 Focus 

 Home 

 PAN-OS 

 Features Introduced in PAN-OS 11.1 

 IoT Security Features 

 Download PDF 

 IoT Security Features 

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

 Previous 

 GlobalProtect Features 

 Next 

 Virtualization Features 

 IoT Security Features 

 Learn about new IoT Security capabilities in PAN-OS 11.1. 

 The following section describes new IoT Security features introduced in PAN-OS 
 11.1. 

 Inbound Policy Rule Recommendations for Device Security 

 September 2025 

 Introduced in PAN-OS 11.1.11 

 ( September 2025 ) Introduced in PAN-OS 11.1.11.

 Device Security enables you to secure your connected device
 environments with both inbound and outbound policy recommendations . While
 PAN-OS and Panorama initially supported only outbound
 policy recommendations, the addition of inbound policy recommendations lets you
 create a more comprehensive security posture for your IT and IoT devices. Creating
 policy rule recommendations based on both outbound and inbound profile behaviors
 helps prevent vulnerability exploitation, lateral movement, and other security risks
 that outbound policies alone cannot address. 

 You can now view both inbound and outbound behaviors for device profiles in the UI
 and create security policies accordingly. For outbound behaviors, the source is the
 IT/IoT device profile, while the destination can be any .
 For inbound behaviors, you can now set the source as any ,
 and the destination is the IT/IoT device profile. This symmetrical approach
 lets you control both what your IT/IoT devices can access, as well as what
 other enterprise sources can access your IT/IoT devices, implementing a true
 Zero Trust security model.

 The policy recommendation workflow supports both per-device and per-profile levels,
 giving you flexibility in how you implement security policies. When creating
 policies, you can specify source and destination attributes including
 device profiles, IP addresses, and FQDNs. The naming convention for policies
 intelligently selects the appropriate profile name (whether in source or
 destination) to ensure clarity in your policy set. For policy rule recommendations
 based on inbound profile behaviors, the name has "-inbound" appended.

 By leveraging both inbound and outbound policy recommendations, you can
 significantly reduce your attack surface by allowing only trusted behaviors for
 your IT/IoT devices. This is particularly valuable for securing critical
 infrastructure and sensitive device deployments where you need to control both
 inbound and outbound traffic.

 Device-ID Visibility and Policy Rule Recommendations in PAN-OS 

 November 2023 

 Introduced in PAN-OS 11.1.0 

 When next-generation firewalls subscribe to Device Security services, they
 send the Device Security instance that’s in the same tenant service group (TSG) Traffic
 logs for analysis. Device Security uses AI and machine learning to automatically
 discover and identify network-connected devices and then construct a data-rich,
 dynamically updating inventory. From PAN-OS® 11.1, administrators can see this
 inventory directly in the PAN-OS web interface without having to open the
 Device Security portal, which is the only place this information appears when Device Security 
 integrates with firewalls running earlier PAN-OS releases. For further 
 Device-ID visibility ,
 the PAN-OS 11.1 web interface also shows a summary of the 10 most common
 device categories, profiles, and operating systems on the network learned from
 Device Security .

 In addition to identifying devices, Device Security analyzes network behaviors
 to determine a baseline of normal, acceptable behaviors. It then generates policy
 rule recommendations that would allow devices to continue their normal network
 behaviors while denying behaviors that deviate from the norm. PAN-OS administrators
 can view these recommendations in the PAN-OS 11.1 web interface, select the ones
 they want their firewalls to apply, and import them into the Security policy
 rulebase. When using a PAN-OS release prior to PAN-OS 11.1, it was necessary to
 create policy rule sets in the Device Security portal and activate them before they
 appeared in the PAN-OS interface. To simplify the workflow, these steps have been
 eliminated in PAN-OS 11.1.

 See and manage the device inventory and top 10 common device categories, profiles,
 and operating systems directly in the PAN-OS interface. You no longer need
 to create and activate policy rule sets in Device Security , resulting in more
 convenient IoT device visibility and simplified policy rule creation.

 SNMP Network Discovery for IoT Security 

 November 2023 

 Introduced in PAN-OS 11.1.0 

 Depending on where you place the firewalls in your network, they may not see
 enough network traffic for Device Security to comprehensively identify
 devices in your environment. To identify devices on the network, Device Security 
 requires network traffic metadata for analysis. Palo Alto Networks firewalls
 extract and log this metadata when they apply Security policy rules that have
 logging enabled. The firewalls send the logs to the logging service. The
 logging service then streams the metadata to Device Security , which uses
 AI and machine learning to automatically discover and identify
 network-connected devices, dynamically construct an asset inventory, detect
 device vulnerabilities, and determine a baseline of acceptable network behaviors
 that Device Security recommends next-generation firewalls allow in
 Device-ID policy rules.

 When firewalls don't have visibility into all network traffic, this results in
 device discovery gaps and lower efficacy in identifying devices,
 monitoring behaviors, and enforcing Device-ID rules. When firewalls don’t
 receive traffic from all devices, they can still gather
 IP address-to-MAC address bindings and additional network data by using
 SNMP to query switches 
 and other forwarding devices throughout the network.

 When using SNMP to query network switches, firewalls first develop a
 network topography by requesting the Link Layer Discovery Protocol (LLDP) neighbors
 and Cisco Discovery Protocol (CDP) neighbors of one switch (the entry point switch)
 and then repeating the request with neighboring switches and child switches one by
 one throughout the network. After obtaining a list of switches throughout the
 network, or within a limited area of the network, the firewalls next query each one
 for its ARP table as well as other information. The ARP table contains the IP
 address-to-MAC address binding information for the devices connected through the
 switch to the network. Other device details for which firewalls query include the
 physical interfaces or ports on the switch to which devices connect, their VLANs and
 subnets, and DHCP and DNS server IP addresses. After the firewalls receive this
 information, they create logs and send them through the logging service to
 Device Security for analysis. By using SNMP to collect more data from switches and
 forwarding devices in parts of the network that firewalls don’t have visibility
 into, you enable Device Security to form a greater view of the devices on the
 network and expand its services to even more devices.

 Previous 

 GlobalProtect Features 

 Next 

 Virtualization Features 

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

 Release Notes 

 Network Security 

 PAN-OS 

 11.1 

 Next-Generation Firewall 

 GlobalProtect 

 IoT Security 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
