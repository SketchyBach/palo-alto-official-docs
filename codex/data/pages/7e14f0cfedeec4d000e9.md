---
url: https://docs.paloaltonetworks.com/prisma-access/administration/configure-dynamic-privilege-access-settings
fetched_at: 2026-08-13T17:24:13Z
source: palo-alto-main
---

# Configure Dynamic Privilege Access Settings Clear

Configure Dynamic Privilege Access Settings 

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

 Configure Dynamic Privilege Access Settings 

 Updated on 

 Aug 10, 2026 

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

 Aug 10, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Configure Dynamic Privilege Access Settings 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Configure Dynamic Privilege Access Settings 

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

 De-board an NGFW Connector 

 Next 

 Enable Dynamic Privilege Access for Prisma Access Through Common Services 

 Configure Dynamic Privilege Access Settings 

 Learn about the Dynamic Privilege Access functionality in this section. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access
 license 

 Prisma Access 5.1 

 Role: Superuser 

 For IT Enterprise and IT Enabled Services (ITES) companies that need to control which
 users have access to their customer projects, Dynamic Privilege Access 
 provides a seamless, secure, and compartmentalized way for your users to access only
 those projects that they are assigned to. These companies typically assign several
 customer projects to employees and provide siloed access to these projects so that
 so that an authorized user can access only one customer project at a time. 

 What Is Dynamic Privilege Access? 

 Dynamic Privilege Access is a feature in Prisma Access that provides dynamic
 privileges for your users based on the workflow or project that your users select in
 the Prisma Agent . Your users can have dynamic privileges based on the
 combination of the user group and IP pool that is assigned to a project. This unique
 combination defines a project. With Dynamic Privilege Access, you can isolate
 resources in your network so that they are only accessible to your users according
 to the projects they are assigned to. 

 A new predefined role called the Project Admin is available on
 Prisma Access 
 to allow project administrators to
 create and manage project definitions. Project administrators have the ability to
 map projects to select Prisma Access location groups, and create IP address
 assignments using DHCP based on the project and location group. Project
 administrators can manage only the projects that they are assigned to in Strata
 Cloud Manager. 

 When your end users log in to a Prisma Agent that is enabled for Dynamic
 Privilege Access on their managed devices, the following workflow takes place: 
 Your end user selects a project that they are assigned to (for example,
 Project 1). 

 Their identity is authenticated in Cloud Identity Engine, which maps the
 user's user group to the project. 

 Upon successful authentication, and their user group matches the project
 criteria set up by the project admin, the user has access to resources in
 the network through project-specific settings for Project 1 and security
 rules that provide security posture and access control on a per-project
 basis. The security infrastructure applies security rules to restrict user
 access to only the resources and applications belonging to that project.
 Access to resources and applications from other projects isn't allowed. 

 When the user switches to a different project (for example, Project 2), they
 are signed out of the previous project (Project 1). They can then access the
 resources for the second project based on the project-specific settings and
 security rules for that project. 

 You can gain visibility into your Prisma Agent deployment by using Strata Cloud Manager to monitor your users' project activity, and view the service
 consumption and security posture in your network. 

 Previous 

 De-board an NGFW Connector 

 Next 

 Enable Dynamic Privilege Access for Prisma Access Through Common Services 

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

 4.1 Preferred 

 5.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 5.0 Preferred and Innovation 

 Administration 

 Prisma Access 

 Prisma Access 

 Prisma SASE 

 4.0 Preferred 

 Strata Cloud Manager 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
