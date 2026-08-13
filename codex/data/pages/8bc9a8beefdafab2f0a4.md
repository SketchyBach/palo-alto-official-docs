---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-advanced-deployments/service-connection-advanced-deployments/service-connection-multi-cloud-redundancy/configure-and-activate-service-connection-cloud-provider-redundancy-for-panorama-managed-prisma-access
fetched_at: 2026-08-13T17:24:46Z
source: palo-alto-main
---

# Configure and Activate Service Connection Cloud Provider Redundancy Clear

Configure and Activate Service Connection Cloud Provider Redundancy 

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

 Configure and Activate Service Connection Cloud Provider Redundancy 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

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

 New Features 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Advanced Deployments 

 Prisma Access Service Connection Advanced Deployments 

 Service Connection Multi-Cloud Redundancy 

 Configure and Activate Service Connection Cloud Provider Redundancy 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Configure and Activate Service Connection Cloud Provider Redundancy 

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

 New Features 

 Previous 

 Service Connection Multi-Cloud Redundancy 

 Next 

 Supported In-Country Active and Backup Cloud Provider Redundancy Locations 

 Configure and Activate Service Connection Cloud Provider Redundancy 

 Configure and activate using sites with service connections
to provide cloud provider and regional redundancy for Panorama Managed
 Prisma Access deployments. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Prisma Access 
 license 

 To configure multiple service connections for cloud
providers, complete the following steps. 

 ( Existing Prisma Access Deployments Only )
If you have upgraded your plugin to a version that supports cloud
provider redundancy, perform a Commit and Push operation
after you upgrade to the supported plugin. 

 Service connection multi-cloud redundancy is supported
starting with Prisma Access 3.1 Preferred and Innovation. After
you upgrade the Cloud Services plugin, you must perform a Commit
and Push to have the cloud redundancy changes appear
in the UI. 

 If you have a new deployment (not an upgrade),
skip this step. 

 Create the service
connections to be used as active and backup service connections
in a site. 

 After you create Preferred and Alternate locations
 and Commit and Push your changes, you cannot change these locations. For
 example, you cannot change the Preferred location from Canada East to Canada
 East PA-A and you cannot change the Alternate location from Canada East PA-A
 to Canada East. 

 Select Panorama Cloud Services Configuration Service Connection . 

 Add a service connection that
you will designate as an active service connection in a site. 

 Select from either the list of Preferred or Alternate
Locations . 

 To search for a location,
start typing the Location name. 

 Add a service connection that
you will designate as a backup service connection in a site. 

 ( Optional ) Continue to onboard service connections
to be designated as active and backup sites, as required. 

 Create a site; then, designate the service connections
you added as active or backup service connections in the site. 

 In Manage Sites , Add a
new site. 

 Add the service connections
you onboarded. 

 Designate the service locations you added as active and backup in the
site. 

 You can create multiple active and backup sites. Specify
at least one site to be an active site. 

 Click OK . 

 ( Optional ) Continue to add sites for your
active and backup service connections, as required. 

 Commit and Push your changes. 

 Check the status of your sites. 

 Select Panorama Cloud Services Status Network Details Service Connection Redundancy Status . 

 Check the information in the Redundancy
Status and Redundancy Assessment fields.
The redundancy status provides you with the status of the sites
you deploy and the redundancy assessment provides you with more
detail about the deployed service connections in the site. 

 Redundancy Status Redundancy Assessment 

 Info 

 Your service connections might experience
 congestion in the event of a regional failure. 

 Warning 

 All Service Connections are deployed in a single
 region. Please consider deploying in nearby
 locations. 

 This message informs you that all your service
 connections are deployed in a single region. 

 Caution 

 All Service Connections connecting to the site
 are deployed in a single region. Please consider
 deploying in nearby locations. 

 This message informs you that all service
 connections connecting to a site are deployed in a
 single region. 

 Previous 

 Service Connection Multi-Cloud Redundancy 

 Next 

 Supported In-Country Active and Backup Cloud Provider Redundancy Locations 

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

 4.1 Preferred 

 5.0 Preferred and Innovation 

 Administration 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 SASE 

 4.2 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 Prisma Access 

 4.0 Preferred 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
