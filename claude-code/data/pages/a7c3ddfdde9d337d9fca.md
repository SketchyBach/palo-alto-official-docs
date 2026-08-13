---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/high-availability/ha-concepts/ha-links-and-backup-links/ha-ports-on-the-pa-7000-series-firewall
fetched_at: 2026-08-13T17:00:11Z
source: palo-alto-main
---

# HA Ports on Palo Alto Networks Firewalls Clear

HA Ports on Palo Alto Networks Firewalls 

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

 HA Ports on Palo Alto Networks Firewalls 

 Updated on 

 Aug 3, 2026 

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

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 High Availability 

 HA Ports on Palo Alto Networks Firewalls 

 Download PDF 

 Next-Generation Firewall 

 HA Ports on Palo Alto Networks Firewalls 

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

 HA Links and Backup Links 

 Next 

 Device Priority and Preemption 

 HA Ports on Palo Alto Networks Firewalls 

 Learn about HA ports available on Palo Alto Networks® firewalls. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 For Strata Cloud Manager managed NGFWs: 

 Strata Cloud Manager Pro 

 When connecting two Palo Alto Networks® firewalls in a high availability (HA)
 configuration, we recommend that you use the dedicated HA ports for HA Links and Backup
 Links . These dedicated ports include: the HA1 ports labeled HA1, HA1-A, and
 HA1-B used for HA control and synchronization traffic; and HA2 and the High Speed
 Chassis Interconnect (HSCI) ports used for HA session setup traffic. The PA-5200 Series
 firewalls have multipurpose auxiliary ports labeled AUX-1 and AUX-2 that you can
 configure for HA1 traffic. 

 You can also configure the HSCI port for HA3, which is used for packet forwarding to the
 peer firewall during session setup and asymmetric traffic flow (active/active HA only).
 The HSCI port can be used for HA2 traffic, HA3 traffic, or both. 

 The HA1 and AUX links provide synchronization for functions that reside on the
 management plane. Using the dedicated HA interfaces on the management plane is more
 efficient than using the in-band ports as this eliminates the need to pass the
 synchronization packets over the dataplane. 

 You can configure data ports as both dedicated HA interfaces and as dedicated backup
 HA interfaces. For firewalls without dedicated HA interfaces, such as the PA-200 and
 PA-400 Series, it is required to configure a data port as a HA interface. 

 Data ports configured as HA1, HA2, or HA3 interfaces can be connected directly to
 each HA interface on the firewall or connected through a Layer2 switch. For data
 ports configured as an HA3 interface, you must enable jumbo frames as HA3 messages
 exceed 1,500 bytes. 

 Whenever possible, connect HA ports directly between the two firewalls in an HA pair
 (not through a switch or router) to avoid HA link and communications problems that
 could occur if there is a network issue. 

 Use the following table to learn about dedicated HA ports and how to connect the HA Links and Backup
 Links : 

 Model 

 Front-Panel Dedicated Port(s) 

 PA-800 Series Firewalls 

 HA1 and HA2 —Ethernet 10Mbps/100Mbps/1000Mbps ports
 used for HA1 and HA2 in both HA Modes . 

 For HA1 traffic —Connect the HA1 port on the
 first firewall directly to the HA1 port on the
 second firewall in the pair or connect these ports
 together through a switch or router. 

 For HA2 traffic —Connect the HA2 port on the
 first firewall directly to the HA2 port on the
 second firewall in the pair or connect these ports
 together through a switch or router. 

 PA-1400 Series Firewalls 

 HA1-A and HA1-B —Ethernet 10Mbps/100Mbps/1000Mbps ports
 used for HA1 traffic in both HA Modes . 

 For HA1 traffic —Connect the HA1-A port on the
 first firewall directly to the HA1-A port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the HA1-A connection —Connect
 the HA1-B port on the first firewall directly to the
 HA1-B port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 If the firewall dataplane restarts due to a
 failure or manual restart, the HA1-B link will
 also restart. If this occurs and the HA1-A link is
 not connected and configured, then a split brain
 condition occurs. Therefore, we recommend that you
 connect and configure the HA1-A ports and the
 HA1-B ports to provide redundancy and to avoid
 split brain issues. 

 HSCI —The HSCI port is a Layer 1 SFP+ interface that
 connects two PA-1400 Series firewalls in an HA
 configuration. Use this port for an HA2 connection, HA3
 connection, or both. 

 The traffic carried on the HSCI port is raw Layer 1 traffic,
 which is not routable or switchable. Therefore, you must
 connect the HSCI ports directly to each other (from the HSCI
 port on the first firewall to the HSCI port on the second
 firewall). 

 PA-3200 Series Firewalls 

 HA1-A and HA1-B —Ethernet 10Mbps/100Mbps/1000Mbps ports
 used for HA1 traffic in both HA Modes . 

 For HA1 traffic —Connect the HA1-A port on the
 first firewall directly to the HA1-A port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the HA1-A connection —Connect
 the HA1-B port on the first firewall directly to the
 HA1-B port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 If the firewall dataplane restarts due to a
 failure or manual restart, the HA1-B link will
 also restart. If this occurs and the HA1-A link is
 not connected and configured, then a split brain
 condition occurs. Therefore, we recommend that you
 connect and configure the HA1-A ports and the
 HA1-B ports to provide redundancy and to avoid
 split brain issues. 

 You can remap the firewall’s SFP ports as HA1-A
 and HA1-B ports via PAN-OS or Panorama. 

 HSCI —The HSCI port is a Layer 1 SFP+ interface that
 connects two PA-3200 Series firewalls in an HA
 configuration. Use this port for an HA2 connection, HA3
 connection, or both. 

 The traffic carried on the HSCI ports is raw Layer 1 traffic,
 which is not routable or switchable. Therefore, you must
 connect the HSCI ports directly to each other (from the HSCI
 port on the first firewall to the HSCI port on the second
 firewall). 

 PA-3400 Series Firewalls 

 HA1-A and HA1-B —Ethernet 10Mbps/100Mbps/1000Mbps ports
 used for HA1 traffic in both HA Modes . 

 For HA1 traffic —Connect the HA1-A port on the
 first firewall directly to the HA1-A port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the HA1-A connection —Connect
 the HA1-B port on the first firewall directly to the
 HA1-B port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 If the firewall dataplane restarts due to a
 failure or manual restart, the HA1-B link will
 also restart. If this occurs and the HA1-A link is
 not connected and configured, then a split brain
 condition occurs. Therefore, we recommend that you
 connect and configure the HA1-A ports and the
 HA1-B ports to provide redundancy and to avoid
 split brain issues. 

 HSCI —The HSCI port is a Layer 1 SFP+ interface that
 connects two PA-3400 Series firewalls in an HA
 configuration. Use this port for an HA2 connection, HA3
 connection, or both. 

 The traffic carried on the HSCI port is raw Layer 1 traffic,
 which is not routable or switchable. Therefore, you must
 connect the HSCI ports directly to each other (from the HSCI
 port on the first firewall to the HSCI port on the second
 firewall). 

 The management interface cannot be configured as a HA port. 

 PA-5200 Series Firewalls 

 HA1-A and HA1-B —Ethernet 10Mbps/100Mbps/1000Mbps ports
 used for HA1 traffic in both HA Modes . 

 For HA1 traffic —Connect the HA1-A port on the
 first firewall directly to the HA1-A port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the HA1-A connection —Connect
 the HA1-B port on the first firewall directly to the
 HA1-B port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 HSCI —The HSCI port is a Layer 1 interface that
 connects two PA-5200 Series firewalls in an HA
 configuration. Use this port for an HA2 connection, HA3
 connection, or both. 

 The HSCI port on the PA-5220 firewall is a QSFP+ port and
 the HSCI port on the PA-5250, PA-5260, and PA-5280
 firewalls is a QSFP28 port. 

 The traffic carried on the HSCI port is raw Layer 1 traffic,
 which is not routable or switchable. Therefore, you must
 connect the HSCI ports directly to each other (from the HSCI
 port on the first firewall to the HSCI port on the second
 firewall). 

 PA-5200 Series Firewalls (continued) 

 AUX-1 and AUX-2 —The auxiliary SFP+ ports are
 multipurpose ports that you can configure for HA1,
 management functions, or log forwarding to
 Panorama . Use these ports when you need a fiber
 connection for one of these functions. 

 For HA1 traffic —Connect the AUX-1 port on the
 first firewall directly to the AUX-1 port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the AUX-1 connection —Connect
 the AUX-2 port on the first firewall directly to the
 AUX-2 port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 PA-5400 Series Firewalls (PA-5410, PA-5420, PA-5430, and PA-5440) 

 HA1-A and HA1-B —SFP/SFP+ 1Gbps/10Gbps ports used for
 HA1 traffic in both HA Modes . 

 For HA1 traffic —Connect the HA1-A port on the
 first firewall directly to the HA1-A port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the HA1-A connection —Connect
 the HA1-B port on the first firewall directly to the
 HA1-B port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 HSCI —The HSCI port is a Layer 1 QSFP+ interface that
 connects two PA-5400 Series firewalls in an HA
 configuration. Use this port for an HA2 connection, HA3
 connection, or both. 

 The traffic carried on the HSCI port is raw Layer 1 traffic,
 which is not routable or switchable. Therefore, you must
 connect the HSCI ports directly to each other (from the HSCI
 port on the first firewall to the HSCI port on the second
 firewall). 

 For HA2 and HA3 traffic —Connect the HSCI-A
 port on the first firewall directly to the HSCI-A
 port on the second firewall. 

 You can use the firewall data ports for HA2 or
 HA3 traffic as well; however, the same data port
 cannot be used for both HA2 and HA3 at the same
 time. To have both HA2 and HA3 connections, you
 must use separate data ports. 

 PA-5450 Firewall 

 HA1-A and HA1-B —SFP/SFP+ 1Gbps/10Gbps ports used for
 HA1 traffic in both HA Modes . 

 For HA1 traffic —Connect the HA1-A port on the
 first firewall directly to the HA1-A port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the HA1-A connection —Connect
 the HA1-B port on the first firewall directly to the
 HA1-B port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 HSCI-A and HSCI-B —The HSCI ports are Quad-SFP+
 (QSFP+/QSFP28) interfaces that connect two PA-5450 firewalls
 in an HA configuration. Use these ports for an HA2
 connection, HA3 connection, or both. 

 The traffic carried on the HSCI ports is raw Layer 1 traffic,
 which is not routable or switchable. Therefore, you must
 connect these ports as follows: 

 For HA2 and HA3 traffic —Connect the HSCI-A
 port on the first firewall directly to the HSCI-A
 port on the second firewall. 

 You can configure HA2 (data
 link) on the HSCI ports or on NC data ports. When
 configuring on dataplane ports, you must ensure that
 both the HA2 and HA2-Backup links are configured on
 dataplane interfaces. A mix of a dataplane port and
 an HSCI port for either HA2 or HA2-Backup will
 result in a commit failure. 

 For a backup to the HSCI-A connection —Connect
 the HSCI-B port on the first firewall directly to
 the HSCI-B port on the second firewall. 

 PA-7000 Series Firewalls 

 HA1-A and HA1-B —Ethernet 10Mbps/100Mbps/1000Mbps ports
 used for HA1 traffic in both HA Modes . 

 For HA1 traffic —Connect the HA1-A port on the
 first firewall directly to the HA1-A port on the
 second firewall in the pair or connect them together
 through a switch or router. 

 For a backup to the HA1-A connection —Connect
 the HA1-B port on the first firewall directly to the
 HA1-B port on the second firewall in the pair or
 connect them together through a switch or
 router. 

 You cannot configure an HA1 connection on the NPC
 data ports or the management (MGT) port. 

 HSCI-A and HSCI-B —The HSCI ports are Layer 1 QSFP+
 interfaces that connect two PA-7000 Series firewalls in an
 HA configuration. Use these ports for an HA2 connection, HA3
 connection, or both. 

 The traffic carried on the HSCI ports is raw Layer 1 traffic,
 which is not routable or switchable. Therefore, you must
 connect these ports as follows: 

 For HA2 and HA3 traffic —Connect the HSCI-A
 port on the first firewall directly to the HSCI-A
 port on the second firewall. 

 For HA2 or HA2/HA3 traffic, the PA-7000 Series
 firewalls synchronize sessions across the NPCs
 one-for-one. 

 For a backup to the HSCI-A connection —Connect
 the HSCI-B port on the first firewall directly to
 the HSCI-B port on the second firewall. 

 HA2 and HA2-Backup links can be configured to use a dataplane
 interface instead of the HSCI ports. However, if configured this
 way, both the HA2 and HA2-Backup links need to use dataplane
 interfaces. A mix of a dataplane port and an HSCI port for
 either HA2 or HA2-Backup will result in a commit failure. This
 applies to the PA-7050-SMC, PA-7080-SMC, PA-7050-SMC-B, and
 PA-7080-SMC-B. 

 Previous 

 HA Links and Backup Links 

 Next 

 Device Priority and Preemption 

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
