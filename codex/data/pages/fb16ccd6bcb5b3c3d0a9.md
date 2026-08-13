---
url: https://docs.paloaltonetworks.com/prisma/prisma-access/3-2/prisma-access-panorama-release-notes/prisma-access-about/features-introduced-in-previous-releases/features-introduced-in-prisma-access-1-8
fetched_at: 2026-08-13T17:31:59Z
source: palo-alto-main
---

# Features Introduced in Prisma Access 1.8 Clear

Features Introduced in Prisma Access 1.8 

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

 Features Introduced in Prisma Access 1.8 

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

 Features Introduced in Prisma Access 1.8 

 Download PDF 

 Features Introduced in Prisma Access 1.8 

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

 Features Introduced in Prisma Access 2.0 Preferred 

 Next 

 Features Introduced in Prisma Access 1.7 

 Features Introduced in Prisma Access 1.8 

 The following table describes the new features introduced
in Prisma Access version 1.8. 

 The 1.8 Cloud Services plugin is currently available for
new customers only. If you are currently using the Cloud Services
plugin version 1.7, you can continue with it and are not required
to upgrade to the 1.8 plugin. If you want to upgrade to the Cloud
Services plugin version 1.8, contact your authorized Palo Alto Networks
representative or partner to schedule an upgrade. 

 The following
features are available if you are using the 1.7 plugin without upgrading
to 1.8: 

 Pre-Allocate IP Addresses for Mobile User
Locations —These API enhancements are available to 1.7 customers. 

 Compute Location Changes —If you add locations with
compute location changes after Prisma Access 1.8 is released, Prisma
Access associates the new compute locations automatically. If you
have already onboarded these locations, complete the steps described
in the following table to change the compute location. 

 Feature 

 Description 

 Prisma Access Licensing Changes 

 Prisma Access introduces changes to licensing.
The new licensing model allows you to implement and use the capabilities
of Prisma Access aligned to your business needs in a way that delivers
the fastest return on investment. Whether your applications are
migrating to the cloud, your users are working from anywhere, or
if you are looking to gain operational efficiencies, Prisma Access
offers the relevant type of license for your deployment. 

 There
are no changes to licensing for existing Prisma Access deployments. 

 Choose
from the following license editions: 

 Business 

 Business Premium 

 Zero Trust Network Access (ZTNA) Secure Internet Gateway
(SIG) 

 Enterprise 

 ZTNA SIG is available for
Prisma Access for Mobile Users only; you can use all other editions
with Mobile Users, Remote Networks, or both mobile users and remote networks. 

 All
license editions are available for Local and Worldwide Prisma Access
locations. When you purchase a license with Worldwide locations,
you can deploy Prisma Access in all Prisma Access locations. When
you purchase a license with Local locations, you can select up to
5 Prisma Access locations. For more details about what is available with
the new licenses, see the Prisma Access Licensing Guide . 

 Bandwidth Allocation by Compute
Location for Remote Networks 

 You allocate bandwidth for remote networks at an aggregate level per compute
location . 

 The aggregate bandwidth model is available
for all new Prisma Access 1.8 deployments and for existing deployments
that have not had any remote networks onboarded before upgrading
to 1.8. If you have an existing Prisma Access deployment that has
onboarded remote networks and you then upgrade to Prisma Access
1.8, this model does not apply and you still apply bandwidth per location . 

 Secure inbound access for remote
network sites and Quality of Service (QoS) for
remote networks is not supported in Prisma Access 1.8 when
you use the aggregate bandwidth model for remote network bandwidth
allocation. 

 Each location has a corresponding compute
location for which bandwidth is allocated, and all sites you onboard
in a compute location share that allocated bandwidth. For example,
you want to onboard four branch offices using remote networks in
the Singapore, Hong Kong, Thailand, and Vietnam locations. All these
locations map to the Asia Southeast compute location. If you allocate
200 Mbps bandwidth to the Asia Southeast compute location, all four branch
offices will share the 200 Mbps of bandwidth. 

 If one or more
sites are not using a large amount of bandwidth, Prisma Access makes
the remaining bandwidth available to other sites in that compute
location. 

 Pre-Allocate IP Addresses for
Mobile User Locations 

 Prisma Access introduces an enhancement
to the API you use to retrieve
IP addresses that allows you to reserve gateway and portal IP addresses
for mobile user locations ahead of time, before you enable them.
This ability lets you add the mobile user egress IP addresses to
your organization’s allow lists before you onboard the locations,
which in turn gives mobile users access to external SaaS apps immediately
after you onboard the locations. 

 The API response also includes
the public IP pool subnets that are the source for the egress IP
addresses for the requested locations.The gateway and portal addresses
of any locations you add will be a part of this subnet. Adding the
subnets to your allow lists provides for future location additions
without allow list modification and is beneficial if your organization’s
allow list size is limited. 

 The IP addresses and subnets are
valid for 90 days after you retrieve them and expire after the validity
period if you do not use them. 

 This enhancement works
for existing customers who are using the Cloud Services plugin 1.7
with no additional configuration changes required. 

 Traffic Steering Enhancements 

 Prisma Access offers the following enhancements
to traffic steering : 

 Multi-tenancy is supported
with traffic steering. 

 You can enable and disable Source NAT (SNAT) for dedicated
service connections. 

 Support for 500 Mbps Remote Network
Bandwidth 

 Prisma Access increases its maximum fully-supported remote
network bandwidth from 300 Mbps to 500 Mbps, and 500 Mbps is now
supported with SSL decryption. 

 GlobalProtect App Log Collection
for Troubleshooting Support 
 If you have a Prisma Access for Users license,
you can quickly resolve mobile user connection, performance, and access
issues by having GlobalProtect users generate and send an easy to
read, comprehensive report from the end user’s endpoint to Strata Logging Service for further
analysis. 

 You are required to use CLI to set up a client certificate
to be used between the GlobalProtect app and Strata Logging Service. See Set Up GlobalProtect Connectivity
to Strata Logging Service for details. 

 Support for Scheduled and Custom
Reports 

 Prisma Access supports custom and scheduled reports from
the Panorama that manages Prisma Access. 

 The ability to run
custom and scheduled reports requires the Cloud Services plugin
1.8 and a minimum Panorama version of 10.0.2. 

 Compute Location Changes 

 To optimize performance and improve latency,
Prisma Access adds a new compute location in Japan and also changes
the mapping of the following locations: 

 Colombia —Moved
from the South America East compute location to the US Southeast
compute location. 

 Mexico West —Moved from the US Southeast compute location
to the US West compute location. 

 Japan South —Moved from the Asia Northeast 1 compute
location to the new Asia Northeast 2 compute location. 

 If
you add the locations after your organization installs the 1.8 plugin,
Prisma Access associates the new compute locations automatically. 

 This
enhancement works for existing customers who are using the Cloud
Services plugin 1.7; however, if you have already onboarded these
locations, complete the following steps to take advantage of the
new compute location: 

 To reduce
down time for mobile user deployments, you can use the new API to
pre-allocate the new gateway and portal IP addresses before you
perform these steps. 

 Delete the location associated
with the new compute location. 

 Commit and push your changes. 

 Re-add the locations you just deleted. 

 Commit and push your changes. 

 Retrieve the new gateway and portal IP addresses (for mobile
users) or the new egress IP addresses (for remote networks) using the API script . 

 Make a note of the new IP addresses and add them to your
allow lists. 

 Since you need to allow time to delete
and add the existing location and change your allow lists, Palo
Alto Networks recommends that you schedule a compute location change
during a maintenance window or during off-peak hours. 

 IKE Peer Host Routes for Remote
Networks and Service Connections 

 Prisma Access will offer the following enhancements
to assist you when sharing public address space externally and internally
with private apps: 

 Enable automatic IKE peer host
routes for Remote Networks and Service Connections —This option
allows Prisma Access to automatically add a host-specific static
route to the static IKE gateway peer for the IPSec tunnel on the
Remote Network security processing node (SPN) and Service Connection
corporate access node (CAN). 

 Specify Outbound Routes —This enhancement allows you
to add up to 10 prefixes for which static routes are added on all
SPNs and CANs, and Prisma Access routes traffic to these prefixes
over the internet. 

 WildFire UK Cloud Support 
 Prisma Access supports the use of the WildFire
UK cloud for Prisma Access ( uk.wildfire.paloaltonetworks.com ),
which is designed to adhere to data sovereignty and residency laws as
well as established data protection and privacy regulations. 

 Previous 

 Features Introduced in Prisma Access 2.0 Preferred 

 Next 

 Features Introduced in Prisma Access 1.7 

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
