---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-device-and-tenant-management
fetched_at: 2026-08-13T17:27:57Z
source: palo-alto-main
---

# Prisma SD-WAN Device and Tenant Management Clear

Prisma SD-WAN Device and Tenant Management 

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

 Prisma SD-WAN Device and Tenant Management 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Device and Tenant Management 

 Download PDF 

 Prisma SD-WAN 

 Prisma SD-WAN Device and Tenant Management 

 Table of Contents 

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

 Previous 

 Assign Domains to Sites 

 Next 

 Prisma SD-WAN MSP Dashboard 

 Prisma SD-WAN Device and Tenant Management 

 Prisma SD-WAN for MSPs provides a set of operational features for Managed
 Service Providers (MSPs) to manage devices and tenants within their purview. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Prisma SD-WAN provides a set of operational
features for Managed Service Providers (MSPs) to manage devices
and tenants within their purview. 

 Multi-Tenancy 

 MSP Account Roles and Permissions 

 Manage Devices for Client Tenants 

 Multi-Tenancy 

 The Prisma SD-WAN controller has multi-tenancy integrated
 into the solution, allowing service providers, enterprise customers, and managed
 support organizations to provide dedicated services based on their organizational
 structure. Some examples of multi-tenancy are: 

 MSPs operating the Prisma SD-WAN environment for multiple
 customers. 

 Enterprise customers with a central purchasing model, which uses several
 lines of business independently within the enterprise. 

 For detailed information, check the following sections: 

 Prisma SD-WAN MSP Dashboard 

 Monitor Tenant Devices, Branches, and Alarms 

 Access Child Tenants 

 MSP Account Roles and Permissions 

 Role-based access control and
 authentication is supported for all operations performed by the MSPs. The
 MSP tenant, though subservient to the Prisma SD-WAN tenant, acts as a
 super-tenant to all the client tenants under its control. 

 Typically, MSP accounts are regular user accounts with additional set of
 roles, and Single Sign-On (SSO) access through an enterprise Identity Provider
 (IdP). A group name within an IdP system may be mapped to the same name to create a
 custom role. The MSP roles and their responsibilities can be classified as: 

 MSP Role Permissions 

 MSP Superuser (msp_superuser) MSP Superuser has read and write access to manage all
 dashboards, reports, apps, logs, and SD-WAN services and devices
 within the assigned level of nested hierarchy. Includes all
 permissions assigned to all roles, and the ability to activate
 product licenses through email activation link. Assign only to users
 or service accounts that require unrestricted access across multiple
 tenants. 

 MSP Identity and Access Management (IAM)
 Administrator (msp_iam_admin) Multi-tenant Identity IAM Administrator provides read
 and write access to identity and authentication functions for all
 tenants in a multitenant hierarchy. This role also includes
 read-only access for logs. No access to dashboards. 

 In a MSP account, you may view, manage, or administer other client networks and
 accounts, if: 

 The user is added at the root (MSP) tenant IAM and has access to all the
 child (client) tenants in the hierarchy. 

 Specific users of a provider account are assigned to manage specific,
 approved client accounts for that provider. These users need to be added to
 the IAM for the particular child (client) tenants. This is handled by the
 users of a provider account who have msp_superuser or msp_iam_admin
 privileges. 

 Previous 

 Assign Domains to Sites 

 Next 

 Prisma SD-WAN MSP Dashboard 

 On This Page 

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

 SASE 

 Administration 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
