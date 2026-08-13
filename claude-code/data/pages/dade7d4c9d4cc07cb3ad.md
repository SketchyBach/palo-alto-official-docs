---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/new-features/by-date/prisma-sd-wan/july-2024#c3b14bf677de92ef4891388f51206ed2
fetched_at: 2026-08-13T17:31:14Z
source: palo-alto-main
---

# New Features - Prisma SD-WAN - July 2024 Clear Clear Clear Clear

New Features - Prisma SD-WAN - July 2024 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

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

 Focus 

 Home 

 Prisma SD-WAN 

 New Features - Prisma SD-WAN - July 2024 

 Prisma SD-WAN Support for FedRAMP Moderate Environment 

 Release Date: July 2024 
 | 
 Last Updated: May 2026 

 The Federal Risk and Authorization Management Program (FedRAMP) is a United States government-wide program that provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud products and services for government users. Prisma SD-WAN demonstrates FedRAMP Moderate compliance. 

 Prisma SD-WAN supports new deployments in a FedRAMP Moderate environment, but it does not support upgrades from an existing Prisma SD-WAN deployment to a FedRAMP Moderate deployment. 

 Here are some considerations that you need to follow before deploying Prisma SD-WAN in a FedRAMP Moderate environment. 

 Requirement of specific SKUs. Prisma SD-WAN requires SKUs that are specific to the FedRAMP environment. Work with your authorized Palo Alto Networks representative or partner to make sure that you purchase the correct SKUs. 

 Prisma SD-WAN ION device platforms ION-1200-S-5G, ION 3200, and ION-9200 on device software version 6.1.6 and later, support FedRAMP Moderate deployments. 

 Support for FIPS-validated encryption. Prisma SD-WAN uses FIPS-validated encryption and hardened on-premises ION devices as part of the Prisma SASE FedRAMP service offering. 

 You need to toggle from the non-FIPS to FIPS mode for the supported ION devices from the Prisma SD-WAN web interface (controller). When you enable FIPS mode, all cryptographic security parameters (CSPs), including the CIC certificate, are cleared and the device is rebooted. After reboot, the device comes up in the FIPS approved mode of operation with a new CIC provisioned by the controller and the FIPS functionality enabled on the device. 

 Support for features in FedRAMP Moderate environment. Prisma SD-WAN supports the following features in a FedRAMP Moderate environment. 

 IPv6 on WAN interfaces for branch and data center ION devices 

 IPv4 and IPv6 on WAN interface (dual-stack) 

 VPN tunnels (IPv6 underlay & IPv4 overlay) 

 WAN DHCPv6 clients 

 PPPoE interfaces 

 Static Routing 

 DHCP for both IPv4 and IPv6 (on the same device) 

 IPv6 on LAN interfaces for branch devices 

 Address distribution to LAN hosts — Static configured prefix 

 DHCPv6 server 

 DNS as a service 

 IPv6 QoS 

 IPv6 Path Policy support 

 Zone Based Firewall 

 Route maps, Prefix Lists 

 Statistics 

 Prisma Access CloudBlades (Panorama Managed) 

 Prisma SD-WAN does not currently support the following features in a FedRAMP environment: 

 User-ID based policies 

 Strata Cloud Manager web interface 

 Predictive analytics 

 Native integration with SASE (Easy Onboarding) 

 NOC Dashboard 

 Performance Policy 

 OSPF LAN Routing for DC and Branch 

 Virtual Routing and Forwarding 

 Branch Gateway mode 

 Aggregate Bandwidth Utilization Reports 

 Site Templates 

 WAN Clarity Reports (WCR) and Extended Analytics (DVR) 

 Azure vWAN CloudBlade 

 AWS Transit Gateway CloudBlade 

 Email Notifications for Alarms CloudBlade 

 Third-party Services CloudBlades 

 Prisma SD-WAN

 Core

 July 2024

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.
