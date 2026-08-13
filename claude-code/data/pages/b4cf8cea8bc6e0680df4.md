---
url: https://docs.paloaltonetworks.com/ngfw/administration/virtual-systems/shared-objects-for-virtual-systems
fetched_at: 2026-08-13T16:40:42Z
source: palo-alto-main
---

# Shared
Objects for Virtual Systems Clear

Shared
Objects for Virtual Systems 

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

 Shared
Objects for Virtual Systems 

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

 Virtual Systems 

 Shared
Objects for Virtual Systems 

 Download PDF 

 Next-Generation Firewall 

 Shared
Objects for Virtual Systems 

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

 Virtual System Components and Segmentation 

 Next 

 Platform Support and Licensing for Virtual Systems 

 Shared
Objects for Virtual Systems 

 Learn which objects can be shared across virtual systems. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 Virtual Systems
 license for any virtual systems beyond the base
 number supported by each NGFW series. 

 One of the following licenses when using Strata Cloud
 Manager: 
 Strata Cloud Manager Pro 

 Strata Cloud Manager Essentials 

 Virtual System support on Strata Cloud
 Manager is available on request. Contact your account team to enable
 the feature. 

 If your administrator account extends to multiple virtual systems, you can choose to configure
 objects (such as an address object) and policy rules for a specific virtual system or as
 shared objects, which apply to all of the virtual systems on the firewall. If you try to
 create a shared object with the same name and type as an existing object in a virtual
 system, the virtual system object is used. 

 Some Shared objects pushed from the Panorama management
 server, such as External Dynamic Lists (EDL), are counted toward the total maximum
 capacity for each object supported by the firewall model . Others, like Address
 objects, are not counted towards the total maximum capacity of the firewall model and
 are specific to the vsys. For example, you configure 51 vsys and have a firewall model
 that supports up to 50,000 IP addresses. You create a
 Shared EDL consisting of 1,000 IP addresses and you
 push the EDL to all vsys. In this example, 1,000 IP addresses are pushed to each of the
 first 50 vsys of your multi-vsys firewall and total 50,000 IP addresses. No IP addresses
 are pushed to the 51st vsys because the total maximum IP addresses supported by firewall
 model is reached. If configured locally, this same EDL counts for only 1,000 IP
 addresses. 

 The following Shared configuration objects are multiplied by
 the number of vsys and count toward the total maximum capacity of your firewall
 model. 

 External Dynamic Lists 

 Security Profile Groups 

 All Security Profiles 

 HIP objects and Profiles 

 Custom Objects (custom data patterns, Spyware, Vulnerability Protection, and URL
 Category) 

 Decryption Profile 

 SD-WAN Link Management Profiles 

 Previous 

 Virtual System Components and Segmentation 

 Next 

 Platform Support and Licensing for Virtual Systems 

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
