---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/ip-address-pools-for-a-globalprotect-mobile-users-deployment/static-ip-address-allocation
fetched_at: 2026-08-13T17:25:08Z
source: palo-alto-main
---

# Static IP Address Allocation for Mobile Users—GlobalProtect Deployments Clear

Static IP Address Allocation for Mobile Users—GlobalProtect Deployments 

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

 Static IP Address Allocation for Mobile Users—GlobalProtect Deployments 

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

 Prisma Access Mobile Users 

 Mobile Users: GlobalProtect 

 IP Address Pools for a GlobalProtect Mobile Users Deployment 

 Static IP Address Allocation for Mobile Users—GlobalProtect Deployments 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Static IP Address Allocation for Mobile Users—GlobalProtect Deployments 

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

 IP Address Pools for a GlobalProtect Mobile Users Deployment 

 Next 

 Context-Driven IP Address Manager 

 Static IP Address Allocation for Mobile Users—GlobalProtect Deployments 

 Learn about the benefits of using a static IP address for mobile users in a Mobile
 Users—GlobalProtect deployment. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 This feature is available for new Prisma Access deployments only. 

 Prisma Access version 5.2.1 

 PAN-OS dataplane version 11.2.4 includes Activity Insights ,
 User Group, and Location Group support. 

 GlobalProtect™ version 6.1.4 

 This is a Limited Availability release.
 To activate this functionality, reach out to your Palo Alto
 Networks account representative after activating the
 tenant. 

 Some legacy networks use IP address-based authorization to restrict users’ access to
 internal or external resources. A Prisma Access Mobile Users—GlobalProtect
 deployment assigns users an IP address from the mobile users IP address pool you
 assign during onboarding, and this user-to-IP address mapping can change in
 subsequent logins. To retain user-to-IP address mapping, Prisma Access lets you
 assign static IP addresses to users. With this feature, Prisma Access allows you
 to allocate IP addresses to users based on the User or User-group, along with
 Theatre and Location groups. 

 You can only enable the Static IP address Allocation feature
 immediately after the activation of a new Prisma Access tenant. After you enable
 this feature and activate the tenant, the feature is set for the life of the tenant,
 and you can't disable it. 

 To create an IP Pool Profile, use one or more of these criteria: 

 A Theater —Allocate IP addresses based on the theater your users are
 in. For example, you can create a /30 subnet for a specific theater. These
 IP addresses are static for that theater. You can apply access to resources
 based on theater by creating Security policy rules using the IP addresses
 you specify for that theater. 

 A User —Allocate IP addresses based on a User-ID by configuring a /30
 or /32 address in the mobile user IP address
 pool , and using match criteria to associate that user with an IP
 address. In this way, you assign a static IP address that Prisma Access 
 retains for a specific user, enabling you to keep your current IP
 address-based Security policy rules to control a user's access to resources. 

 A User Group —Allocate IP addresses based on the user group. The user
 will get the IP address from the defined IP Pool subnet if they are part of
 the configured user group. 

 A Location Group —Allocate IP addresses based on the location group
 defined in the IP Pool profile. 

 Use the following guidelines when allocating static IP addresses: 

 If you specify multiple IP pools, Prisma Access evaluates the rules from top
 to bottom and assigns IP addresses based on the first match in the list of
 rules. 

 Integrate your Prisma Access deployment with the Cloud Identity Engine if you want to
 use User-ID or User-Group as criteria to match IP pools. 

 The following maximum allocations are supported per tenant: 
 20,000 users 

 5,000 user groups with 50,000 users per user group 

 10,000 IP address pool profiles 

 10,000 IP address pools 

 Enter a prefix length between /23 and /32. 

 For each Mobile User Client IP Pool profile you
 create: 
 Up To 10 IP prefixes are supported. 

 Up to 256 users are supported. 

 Static IP addressing uses a Lease Period and a
 Grace Period to specify how long Prisma Access 
 keeps a user-to-IP address association. 
 The Lease Period is the amount of time the
 user-to-IP address mapping is valid after you allocate it. 
 The
 default lease period is 86400 seconds (24 hours). 

 The minimum
 lease period is 3600 seconds (1 hour). 

 The maximum lease
 period is 7776000 seconds (90 days). 

 The Grace Period is the amount of time that,
 after a lease period expires, Prisma Access retains that user-to-IP
 address mapping without assigning it to another user. 
 The default
 grace period is 14400 seconds (4 hours). 

 The minimum grace
 period is 60 seconds. 

 The maximum grace period is 7776000
 seconds (90 days). 

 Configure Static IP Address Allocation 

 To configure a static IP address allocation in a deployment, complete these steps. 

 Go to Configuration NGFW and Prisma Access Configuration Scope Prisma Access GlobalProtect and click the gear to highlight the Infrastructure
 Settings . 

 In the Client IP Pool area, Add IP Pool for the
 static IP addresses. 

 Define the criteria to assign the IP address to mobile users. 

 Give the IP address pool a unique
 Name . 

 Select one or more of the
 Theatres to allow the pool to be used in
 those theaters, or select Any to allow the
 pool to be used in all theaters. 

 Select one or more of the Prisma
 Access Location Groups to allow the pool to be used
 in that location group, or select Any to
 allow the pool to be used in all location groups. 

 Select a user or user group to assign an IP
 address based on the User-ID or user group, or select
 Any to allow IP address assignment to be
 based on other criteria. 

 To assign one or more users or user groups to an IP address pool,
 select the user or user groups in the
 Users or User
 Groups tab. 

 In the IP Pools area, enter an IP address
 pool. 

 To limit a user to a single
 IP address, specify a /30 or /32 IP address; Prisma Access 
 assigns the user to that address. Since a /32 would provide only
 one IP address, we recommend a minimum subnet of /30 and
 restricting the user to that subnet. 

 ( Optional ) Enter a Lease Period and
 a Grace Period for the user-to-IP address
 mapping. 

 Save your changes. 

 Verify your changes by going to GlobalProtect Settings on the client machine, viewing the Tunnel
 Statistics , and verifying the Assigned IP
 Address(es) . 

 Previous 

 IP Address Pools for a GlobalProtect Mobile Users Deployment 

 Next 

 Context-Driven IP Address Manager 

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
