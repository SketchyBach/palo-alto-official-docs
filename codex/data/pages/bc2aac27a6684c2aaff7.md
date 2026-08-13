---
url: https://docs.paloaltonetworks.com/prisma-access-browser/activation-and-onboarding/prisma-browser-for-msps-activation-and-onboarding/prisma-browser-msp-dashboard/add-child-tenants-for-msp
fetched_at: 2026-08-13T17:23:06Z
source: palo-alto-main
---

# Add Child Tenants for Managed Service Providers Clear

Add Child Tenants for Managed Service Providers 

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

 Add Child Tenants for Managed Service Providers 

 Updated on 

 Sun Aug 02 02:16:49 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Sun Aug 02 02:16:49 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Browser for Managed Service Providers - Activation and Onboarding 

 Prisma Browser MSP Dashboard 

 Add Child Tenants for Managed Service Providers 

 Download PDF 

 Prisma Browser 

 Add Child Tenants for Managed Service Providers 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Prisma Browser MSP Dashboard 

 Next 

 Assign Prisma Browser Roles 

 Add Child Tenants for Managed Service Providers 

 Add child tenants for Prisma Browser MSP 

 Where Can I Use This? What Do I Need? 

 Strata Multitenant Cloud Manager 

 Prisma Browser Standalone License 

 Strata Cloud Manager Pro License 

 Cloud Identity Engine is included and spun up during activation. 

 Identity & Access
 role : Multitenant Superuser or Superuser 

 The Prisma Browser for Managed Service Providers (MSP) allows you to add
 additional child tenants beneath the root level. This means that you need one standalone
 license that will be activated on the root tenant, which is shared across multiple child
 tenants. This article describes the detailed step-by-step instructions needed to add and
 onboard the child tenants. 

 Before You begin 

 Before you configure the CIE, decide on the Identity Provider type that best
 meets your requirements: 

 MSP IdP: Required when an MSP customer does not have their own
 IDP. In that case, MSP need to setup users and groups within their IDP and integrate this IdP with our CIE 
 at the root tenant which can authenticate users in their
 tenant. 

 Tenant-Specific IdP: Uses an MSP customer’s own IdP connected to
 a tenant-level CIE. 

 If you plan to use the tenant-specific IdP type, ensure that the
 customer’s IdP is ready and can interface with the tenant-specific CIE. 

 To add child tenants to the MSSP root tenant, perform the following: 

 Access the Strata Multitenant Cloud
 Manager . 

 Select the tenant where you have activated the Prisma Browser 
 Standalone license and want to add the child tenants. 

 Select Summary > Prisma Browser . 

 Click Add Tenant to create and onboard child tenants on the root
 tenant where you activated the Prisma Browser license. You can add and
 onboard the tenants using the step-by-step guided wizard. 

 Step 1 - Tenant Configuration 

 Specify a Name for the child tenant. 

 Select the Region, the SLS location where you want to deploy
 this tenant. 

 If you plan to use the MSP
 IdP, then ensure that this region is the CIE region of the root
 tenant. 

 Subscription is auto-populated based on the activated license. 

 the User Quantity, the number of Prisma Browser Standalone
 licenses to allocate to this child tenant. 

 Step 2 - Identity Provider Configuration You can
 configure two types of Identity Providers(IdP): 
 Tenant Specific IDP 
 Select the type as Tenant
 Specific IdP and ensure that the customer's IdP is
 ready and can interface with the tenant-specific CIE. 

 MSP IdP 
 Ensure that the CIE is configured at the root
 tenant. Select the appropriate Root Directory,
 Authentication Profile, and User Groups
 configured in the root tenant. 

 Review the summary and click Create Tenant. 

 If you are using a tenant IdP, perform a manual group sync
 in the Prisma Browser portal to synchronize the identities. 

 You can repeat the Add Tenant procedure to add the required number of
 tenants. You can view the list of tenants added and also the status of the tenant
 onboarding at Summary > Prisma Summary . 

 Previous 

 Prisma Browser MSP Dashboard 

 Next 

 Assign Prisma Browser Roles 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Prisma Browser 

 Activation & Onboarding 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
