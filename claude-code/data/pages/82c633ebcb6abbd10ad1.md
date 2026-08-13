---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/high-availability/ha-clustering-best-practices-and-provisioning
fetched_at: 2026-08-13T17:04:39Z
source: palo-alto-main
---

# HA Clustering Best Practices and Provisioning Clear

HA Clustering Best Practices and Provisioning 

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

 HA Clustering Best Practices and Provisioning 

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

 HA Clustering Best Practices and Provisioning 

 Download PDF 

 Next-Generation Firewall 

 HA Clustering Best Practices and Provisioning 

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

 HA Clustering Overview 

 Next 

 Configure HA Clustering 

 HA Clustering Best Practices and Provisioning 

 Follow provisioning requirements and best practices for
HA clustering. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 For Strata Cloud Manager managed NGFWs: 

 Strata Cloud Manager Pro 

 These are the provisioning requirements
and best practices for HA clustering. 

 Provisioning Requirements and Best Practices 
 HA cluster
members must be the same firewall model and run the same PAN-OS ® version. 

 When
upgrading, firewall members will continue to synchronize sessions
with one member at a different version. 

 It is highly recommended and a best practice to use Panorama
to provision HA cluster members to keep all configuration and policies
synchronized among all cluster members. 

 HA cluster members must be licensed for the same components
to ensure consistent policy enforcement and content inspection capabilities. 

 The licenses must expire at the same time to prevent mismatched
licenses and loss of functionality. 

 All cluster members should be running with the same version
of dynamic Content Updates for consistent security enforcement. 

 HA cluster members must share the same zone names in order for
sessions to successfully fail over to another cluster member. For
example, suppose sessions going to an ingress zone named internal are
dropped because the link is down. For those sessions to fail over
to an HA firewall peer in the cluster, that peer must also have
a zone named internal . 

 Client-to-server and server-to-client flows must go back to
the same firewall under normal (non-failure) conditions in order
for security content scanning to occur. Asymmetric traffic won’t
be dropped, but it cannot be scanned for security purposes. 

 Session Synchronization Best Practices 
 Dedicated HA communication
interfaces should be used over dataplane interfaces. HSCI interfaces
aren’t used for HA4. This allows separation of HA pair and cluster
session synchronization to ensure maximum bandwidth and reliability
for session syncing. 

 HA4 should be adequately sized if you use dataplane interfaces.
This ensures best effort session state synchronizing between cluster
members. 

 Best practice is to have a dedicated cluster network for the
HA4 communications link to ensure adequate bandwidth and non-congested,
low-latency connections between cluster members. 

 Architect your networks and perform traffic engineering to avoid
possible race conditions, in which a network steers traffic from the
session owner to a cluster member before the session is successfully
synced between the firewalls. Layer2 HA4 connections must have sufficient
bandwidth and low latency to allow timely synchronization between
HA members. The HA4 latency must be lower than the latency incurred
when the peering devices switch traffic between cluster members. 

 Architect your networks to minimize asymmetric flows. Session
setup requires one cluster member to see the complete TCP three-way
handshake. 

 Health Check Best Practices 
 On HA pairs in a cluster,
configure an Active/Passive pair with HA backup communication links
for HA1, HA2, and HA4. Configure an Active/Active pair with HA backup
communications links for HA1, HA2, HA3, and HA4. 

 Configure HA4 backup links on all cluster members. 

 Previous 

 HA Clustering Overview 

 Next 

 Configure HA Clustering 

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
