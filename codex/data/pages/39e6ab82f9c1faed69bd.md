---
url: https://docs.paloaltonetworks.com/prisma/prisma-access/3-2/prisma-access-panorama-release-notes/prisma-access-about/features-introduced-in-previous-releases/features-introduced-in-prisma-access-1-3-0
fetched_at: 2026-08-13T17:31:57Z
source: palo-alto-main
---

# Features Introduced in Prisma Access 1.3.0 Clear

Features Introduced in Prisma Access 1.3.0 

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

 Features Introduced in Prisma Access 1.3.0 

 Updated on 

 May 29, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 Updated on 

 May 29, 2026 

 Focus 

 Home 

 Prisma 

 Prisma Access 

 Prisma Access Release Notes (Panorama Managed) 

 Prisma Access (Panorama Managed) Release Information 

 Features Introduced in Previous Prisma Access (Panorama Managed)
Releases 

 Features Introduced in Prisma Access 1.3.0 

 Download PDF 

 Features Introduced in Prisma Access 1.3.0 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 Previous 

 Features Introduced in Prisma Access 1.3.1 

 Next 

 Features Introduced in Prisma Access 1.2.0 

 Features Introduced in Prisma Access 1.3.0 

 The following table describes the new features introduced
in the Cloud Services plugin version 1.3.0. For additional information
on how to use the new features in this release, refer to the Prisma Access Administrator’s
Guide (Panorama Managed) . 

 Upgrading to 1.3 causes changes to device groups. 

 Feature 

 Description 

 Quality of Service (QoS) Support 

 You can now enable QoS in Prisma Access to
mark and shape QoS traffic. Prisma Access delivers the same QoS
marking and shaping features available today in Palo Alto Networks next-generation
firewalls. 

 You can create PAN-OS security policies to mark
traffic destined to Prisma Access for mobile users and for remote
network connections. For service connections, Prisma Access honors
traffic marking from your on-premise devices. In addition, you can
optionally use on-premise devices to mark traffic for remote networks. 

 You can create QoS profiles to shape
QoS traffic for service connections and for remote network connections
and apply those profiles to traffic that you marked with PAN-OS
security policies, traffic that you marked with an on-premise device,
or both PAN-OS-marked and on-premise-marked traffic. 

 Support for Additional Service Connections 

 You can now configure up to 100 service connections
in Prisma Access. Previously, a maximum of three service connections
were allowed and you had to use remote network connections for additional
connections to an HQ or data center site, which limited throughput
to the configured bandwidth of the remote connection. 

 You
can configure up to three service connections with no license cost;
however, each additional connection uses 300 Mbps of the remote
network bandwidth allocation from your Prisma Access license. 

 The
license cost for additional service connections does not change
their functionality. Prisma Access does not limit the bandwidth
over service connections, and additional service connections work
the same as other service connections. 

 Additional Bandwidth Choices for Remote
Networks 

 In addition to the existing remote network bandwidth
choices of 2 Mbps, 5 Mbps, 10 Mbps, 25 Mbps, 50 Mbps, 100 Mbps,
or 300 Mbps, you can now select 20 or 150 Mbps, to better match commonly-used
ISP speeds. 

 Expanded Visibility for Mobile Users 

 You now have expanded visibility for mobile
users, including their client OS, their last login time, and their
public IP addresses. You can view a list of currently logged in
users or view historical information of previously-logged in users
for a 90-day time period. 

 To view User ID information, select Panorama Cloud Services Status Status ;
then click either Current Users or Users
(Last 90 days) in the Mobile Users area. 

 Multiple Prisma Access Instances On a
Single Panorama Appliance (Multi-Tenancy) 

 You can now host and manage multiple instances
of Prisma Access (known as tenants ) on a single Panorama appliance.
With multi-tenancy, each single Panorama appliance supports up to
100 tenants, each with their own templates and template stacks , device groups , and access domains.
This enables you to create tenant-level administrative users who
can view and edit the configuration for a single tenant. 

 You
allocate remote network and mobile user license resources for each
tenant based on the license that is associated with the Cloud Services
plugin in Panorama. The minimum license allocation for each tenant
is 500 Mbps for remote networks and 500 mobile users. You can also
configure a tenant with only remote networks (minimum 500 Mbps)
or mobile users (minimum 500 mobile users). 

 Since this
feature is supported starting with PAN-OS version 8.1.6, you must
use the Cloud Services plugin with a Panorama appliance running
a minimum version of 8.1.6. 

 GlobalProtect App Generate Ticket Option 

 Panorama now allows GlobalProtect administrators
and Help Desk support personnel to generate a ticket that end users
must supply to disable the GlobalProtect app
for Windows or for Mac . 

 Since
this enhancement is supported starting with PAN-OS version 8.1.6, you
must use the Cloud Services plugin with a Panorama appliance running
a minimum version of 8.1.6. 

 Persistent Public IP Addresses for Mobile
User Gateways 

 This feature is applicable if you are adding Prisma
Access public IP addresses to an allow list in your network to control
access for SaaS or public applications. 

 With this release,
Prisma Access now assigns two new sets of public IP addresses for
mobile user gateways: 

 One set that is assigned to
gateways that are currently active. 

 Another set to reserve in case of a scaling event, infrastructure
upgrade, or other event that causes an IP address change for
mobile users. 

 These new IP addresses will persist
across future upgrades. 

 Prisma Access provides each customer
with their own unique set of IP addresses. While the currently assigned
IP address will change after you upgrade, this change does not affect
mobile users' ability to connect to Prisma Access. 

 Public
IP addresses for remote networks will not change after you upgrade,
and you do not have to reconfigure your IPSec tunnels. 

 You
can retrieve these new addresses by retrieving your API key and
entering a curl command in the following format: 

 curl -k -H header-api-key: Current-API-Key "https://api.gpcloudservice.com/getAddrList/latest?get_egress_ip_all=yes" 

 Where Current-API-Key is
the Prisma Access API key. 

 For example, given an API key of 123abc ,
use the following curl command to retrieve the public IP address: 

 curl -k -H header-api-key:123abc "https://api.gpcloudservice.com/getAddrList/latest?get_egress_ip_all=yes" 

 If
you have a large number of mobile users from a single region, the
reserved IP addresses might be insufficient to scale; in this case,
Prisma Access adds more public IP addresses to the allocated IP
sets and you will have to retrieve those new IP addresses to add
to your allow lists. These extra sets of IP addresses also persist
after an upgrade. Continue to use the curl command to get notified
when additional sets of IPs are added to the reserved pool. 

 PAN-OS 8.1 Support 

 The Prisma Access infrastructure is upgraded
to PAN-OS version 8.1. You can now implement PAN-OS 8.1 features
in Prisma Access, including but not limited to the following features: 

 Security Features: 

 SaaS Application Hosting Characteristics 

 Simplified App-ID 

 HTTP Header Insertion and Modification 

 Service-Based Session Timeouts 

 Automatic SAN Support for SSL
Decryption 

 WildFire Script Sample Analysis 

 Management Features: 

 Rule Usage Tracking (also
known as Policy Rule Usage Tracking) 

 Configuration Table Export 

 Reporting Engine Enhancements 

 Enhanced Application Logging 

 Mobile Features: 

 Optimized Split Tunneling for
GlobalProtect 

 Extensible Authentication Protocol
(EAP) Support for RADIUS 

 Support for Multiple Username
Formats 

 Upgrading the infrastructure
to 8.1 causes changes to default behavior; for more information,
see the following documentation: 

 Changes to Default Behavior for
PAN-OS and GlobalProtect 8.1 

 Changes to Default Behavior for
the User-ID Agent 

 In particular, please note that previously,
the firewall normalized usernames received from User-ID sources
(such as an LDAP directory) to the domain\username format. In PAN-OS
8.1, when the Primary Username is in UPN format, it will not be normalized
as in previous PAN-OS versions. As a result, usernames are displayed
in their original format (for example, username@domain). 

 Previous 

 Features Introduced in Prisma Access 1.3.1 

 Next 

 Features Introduced in Prisma Access 1.2.0 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

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

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SASE 

 Release Notes 

 3.2 Preferred and Innovation 

 Prisma SASE 

 Prisma Access 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
