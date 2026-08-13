---
url: https://docs.paloaltonetworks.com/fedramp/autonomous-dem/get-started-with-adem/enable-adem-for-remote-networks/enable-adem-in-panorama-managed-pa-rn
fetched_at: 2026-08-13T16:32:36Z
source: palo-alto-main
---

# Enable ADEM in Panorama Managed Prisma Access for Remote
Sites Clear

Enable ADEM in Panorama Managed Prisma Access for Remote
Sites 

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

 Enable ADEM in Panorama Managed Prisma Access for Remote
Sites 

 Updated on 

 Wed Sep 04 15:52:49 PDT 2024 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 FedRAMP Docs 

 Reference 

 Autonomous DEM 

 Updated on 

 Wed Sep 04 15:52:49 PDT 2024 

 Focus 

 Home 

 FedRAMP 

 Get Started with Autonomous DEM 

 Enable ADEM for Your Remote Sites 

 Enable ADEM in Panorama Managed Prisma Access for Remote
Sites 

 Download PDF 

 FedRAMP 

 Enable ADEM in Panorama Managed Prisma Access for Remote
Sites 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 FedRAMP Docs 

 Reference 

 Autonomous DEM 

 Previous 

 Enable ADEM for Your Remote Sites 

 Next 

 Enable ADEM in Cloud Managed Prisma Access for Remote Sites 

 Enable ADEM in Panorama Managed Prisma Access for Remote
Sites 

 Based on your capacity planning, you allocate
your Remote Networks bandwidth licenses on Prisma Access for each
compute location. The unit of measure for bandwidth licenses is
Mbps. 

 Below
are some points to consider when allocating bandwidth for ADEM: 

 When enabling ADEM on a compute location, the amount of ADEM
bandwidth allocated on a compute location will mandatorily be equal
to the bandwidth that you had already allocated for Remote Networks
(see Bandwidth Allocation (Mbps) column)
on Prisma Access for that compute location. 

 As soon as you
enable ADEM on a compute location, the same amount of bandwidth
allocated for Remote Network is automatically deducted from the
overall ADEM pool of bandwidth licenses (shown by Autonomous
DEM Allocated Total ). 

 The Autonomous DEM Allocated Total shows
you how much bandwidth has already been consumed by ADEM and how
much is remaining. 

 For any compute location, you can Enable ADEM
only if you have enough ADEM bandwidth license available in the
overall ADEM bandwidth pool (shown in Autonomous DEM
Allocated Total ) matching the allocated Remote Networks
bandwidth. For example, if you are trying to Enable ADEM
on a compute location where 100 Mbps of Remote Networks bandwidth
is allocated, if your ADEM pool of licenses does not have at least 100
Mbps bandwidth available, you won't be able to enable ADEM on that
compute location unless you add more ADEM bandwidth license to overall
pool. 

 Also, when ADEM is enabled on a particular compute location,
if you increase or decrease the amount of Remote Networks Bandwidth
Allocation (Mbps) on that compute location, it will
correspondingly increase or decrease the overall bandwidth in the
ADEM pool of licenses ( Autonomous DEM Allocated Total ). 

 When you Enable ADEM on a compute
location, all the sites that connect to the compute location get
ADEM enabled and those Prima SD-WAN sites can connect to the ADEM
portal. Hence all those sites can be monitored. 

 After you have enabled ADEM on a compute location, if you
would like to free up some ADEM bandwidth to allocate to some other
compute location, you can deselect the Enable check
box. Doing so will release that bandwidth back to the ADEM pool
of licenses, but it will also disable ADEM on the compute location
which results in synthetic test monitoring to be stopped on all
sites connected to that compute location. 

 To enable
Autonomous DEM for the compute location, follow these steps: 

 Open Panorama. 

 In the left panel, expand Cloud Services and
select Configuration Remote Networks . 

 Edit the Aggregate Bandwidth and Autonomous
DEM Settings . 

 Enable the compute locations for
which to allocate the bandwidth for ADEM. 

 The Autonomous
DEM Allocation column will be visible only if you have
purchased the ADEM for Remote Networks license. 

 Click OK . 

 Add the following URLs to make the SD-WAN site register
to the ADEM portal: 

 In Panorama, go to Objects addresses . Click on Add and add
 the following ADEM Service Destination FQDNs. 

 FedRAMP High:

 updates.dem.prismasasegov.com 

 agents.dem.prismasasegov.com 

 features.dem.prismasasegov.com 

 agents-il4-prod-us-central1.dem.prismasasegov.com 

 FedRAMP Moderate:

 agents-fed-mod-prod-1-us-central1.dem.prismaaccess.com 

 updates-fed-mod-prod-1-us-central1.dem.prismaaccess.com 

 features-fed-mod-prod-1-us-central1.dem.prismaaccess.com 

 Create an address group to contain the addresses above by
going to Objects Address Groups ,
clicking Add and providing a name for the
address group. 

 Add the address group you just created into the security
policy. Go to Policies Security PreRules . Click Add and
add the address group to the policy. 

 Previous 

 Enable ADEM for Your Remote Sites 

 Next 

 Enable ADEM in Cloud Managed Prisma Access for Remote Sites 

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

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

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

 Autonomous DEM 

 Autonomous DEM 

 SASE 

 Prisma SASE 

 FedRAMP 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
