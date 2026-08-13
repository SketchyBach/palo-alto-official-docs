---
url: https://docs.paloaltonetworks.com/identity/release-notes/cloud-identity-engine/cloud-identity-engine-release-notes-welcome/new-features-introduced-in-june-2024
fetched_at: 2026-08-12T14:07:12Z
source: idira-and-identity
---

# New Features Introduced in June 2024 Clear

New Features Introduced in June 2024 

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

 New Features Introduced in June 2024 

 Updated on 

 Tue Apr 28 14:43:41 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Identity Docs 

 Activation & Onboarding 

 Cloud Identity Engine 

 Help 

 Release Notes 

 New Features 

 Updated on 

 Tue Apr 28 14:43:41 PDT 2026 

 Focus 

 Home 

 Identity 

 Welcome to the Cloud Identity Engine 

 New Features Introduced in June 2024 

 Download PDF 

 Identity 

 New Features Introduced in June 2024 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Identity Docs 

 Activation & Onboarding 

 Cloud Identity Engine 

 Help 

 Release Notes 

 New Features 

 Previous 

 New Features Introduced in August 2024 

 Next 

 New Features Introduced in May 2024 

 New Features Introduced in June 2024 

 Learn more about the new features introduced for the Cloud Identity Engine in June
 2024. 

 The following table provides a snapshot of new features introduced for the Cloud Identity
 Engine app in June 2024. Refer to the Cloud Identity Engine documentation for more
 information on how to use the Cloud Identity Engine. 

 Feature Description 

 Simplified configuration for Azure Active Directory 

 The configuration process for setting up an Azure Active
 Directory for user identification with the Cloud Identity
 Engine has been updated so that it is now simpler and more
 streamlined. Instead of needing to manually complete all the steps
 required to configure a SAML-based app for the Azure directory,
 copying and pasting multiple types of information, or trying to
 decide between the client configuration flow and the auth code flow,
 now all you need to do is copy your directory ID, grant the
 necessary permissions for the Cloud Identity Engine to access your
 directory, and Azure automatically installs the gallery app for your
 directory. 

 All that’s needed from you is to select any additional information
 types (such as user risk information) that you want to collect from
 your Azure directory and whether you want to limit data collection
 to specific groups, then test the connection to ensure that the
 Cloud Identity Engine can successfully connect to your Azure
 directory to collect attributes for user identification. 

 With this new simplified process, the Cloud Identity Engine makes it
 even easier to configure an Azure directory for user identification,
 streamlining the deployment process for your Azure directories. This
 easier method minimizes the chance of misconfiguration, makes the
 process of deployment more efficient, and reduces the time to
 deployment. 

 This change deprecates both the auth code
 flow and the previous version of the client configuration flow. Palo
 Alto Networks recommends that you reconnect your Azure directory
 using the new client credential flow (CIE gallery app) method.

 Dynamic Privilege Access Support for the Cloud Identity
 Engine 

 For networks that manage traffic for IT and IT Enabled Services
 (ITES), ensuring that users have consistent access to the network
 resources that they need while still maintaining a security policy
 based on “least privilege access” can be challenging to deploy and
 time-consuming to maintain, especially as the number of users
 increases. To allow users access to resources on a per-project
 basis, the Cloud Identity Engine now supports Dynamic Privilege
 Access, a seamless, secure, and compartmentalized method to ensure
 users can access only the resources necessary for their assigned
 project. 

 When you enable Dynamic Privilege
 Access for the Cloud Identity Engine, the user obtains access
 through project-specific settings that isolate network resources
 after selecting a profile and a project and successfully completing
 authentication. This ensures that the user cannot gain lateral
 access to other resources or attempt other access-based malicious
 activity as well as helping companies to remain in compliance with
 contracts and regulations. 

 Dynamic Privilege Access also helps users by increasing visibility
 for what resources they can access. When a user logs in, all
 assigned profiles and projects display, allowing the user to choose
 which profile to use and which project to access. Users can have
 multiple customer project assignments but access is restricted to
 one project at a time. 

 Enabling Dynamic Privilege Access helps secure critical network
 resources from unauthorized access while maintaining productivity by
 ensuring that users are not prevented from accessing the resources
 they need to complete their work. 

 Previous 

 New Features Introduced in August 2024 

 Next 

 New Features Introduced in May 2024 

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

 Prisma Access Monitoring & Visibility 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 Release Notes 

 Network Security 

 Cloud Identity Engine 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
