---
url: https://docs.paloaltonetworks.com/prisma-access/administration/manage-multiple-tenants-in-prisma-access/enable-multitenancy-and-migrate-the-first-tenant
fetched_at: 2026-08-13T17:24:25Z
source: palo-alto-main
---

# Enable Multitenancy and Migrate the First Tenant Clear

Enable Multitenancy and Migrate the First Tenant 

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

 Enable Multitenancy and Migrate the First Tenant 

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

 Prisma Access Multi-Tenancy 

 Enable Multitenancy and Migrate the First Tenant 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Enable Multitenancy and Migrate the First Tenant 

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

 Create an All-New Multitenant Deployment 

 Next 

 Add Tenants to Prisma Access 

 Enable Multitenancy and Migrate the First Tenant 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager) , see Prisma
 SASE . 

 Prisma Access 
 license 

 Use the following workflow to enable multitenancy and migrate your existing configuration to the
 first tenant you create. If you don’t have any existing configuration, you can
 enable multitenancy and add your tenants; then configure them. 

 When you enable multitenancy,
 Prisma Access migrates the following components of your configuration: 

 All service connection and remote network tunnel onboarding information,
including tunnel configuration. 

 Existing mobile users onboarding information. 

 Strata Logging Service information. 

 Existing Autonomous DEM (ADEM) configuration 

 The templates, template stacks, and device groups for service connections,
remote networks, and mobile users. 

 You need to specify the number of users (for a mobile user deployment), bandwidth (for a remote
 networks deployment), and Autonomous DEM (ADEM) to allocate for each
 deployment (if you have purchased an ADEM license). 

 Because
of these device group changes, you create an access domain and add
the migrated device groups, templates, and template stacks, as shown
in the following workflow. 

 If you don’t have an existing
 Prisma Access configuration, and you are creating an all-new multitenant
deployment, do not use this workflow; instead, complete the steps
in Add Tenants to Prisma Access to create the
first tenant. 

 Determine the number of licensed units you want to allocate to this
 deployment. 

 While Prisma Access migrates your configuration to the first tenant, you need
 to specify: 

 The Bandwidth to allocate for the tenant’s
 remote users deployment (if applicable). 

 The Users to allocate for the tenant’s mobile
 users deployment (if applicable). 

 The number of ADEM units to allocate for mobile uses and remote
 networks (if applicable). 

 Select Panorama Cloud Services Configuration . 

 Select Enable Multitenancy (located
on the upper right of the page). 

 After you enable multitenancy, Panorama displays a notification informing you that the existing
 Prisma Access configuration move to the first tenant. 

 After you enable
multitenancy, your deployment permanently changes to a multitenant
deployment, and you cannot revert to single tenant mode. 

 Click OK to migrate the existing
configuration to the first tenant. 

 The Tenants page displays, and pie
charts in the center of the window display. 

 If you
have a remote networks or mobile users license, the available amount
of licensed remote network bandwidth and mobile users display. 

 ( Remote Networks and Mobile User Deployments Only )
If you have purchased an Autonomous DEM license, the available number
of units for ADEM uses displays. 

 If you have a Clean Pipe deployment, the amount of bandwidth
for the tenant displays. 

 Choose the type of deployment you want to use for the tenant. 

 For a remote network, mobile user deployment, or
to configure both deployment types for a tenant, select Remote Networks/Mobile
Users . 

 For a clean pipe deployment, select Clean Pipe . 

 This
section only describes how to configure tenants for remote network, mobile
user, or both remote network and mobile user deployment types. To configure
the clean pipe service, see Prisma Access for Clean Pipe . 

 Migrate the existing configuration to the first tenant. 

 The first migrated sub-tenant's name is auto-populated from the tenant you
 are migrating and cannot be edited. 

 Create a new Access Domain by clicking
the down arrow selecting New Access Domain . 

 Enter a Name for the access
domain and click OK . 

 Prisma Access adds the Mobile_User_Device_Group , Remote_Network_Device_Group ,
and Service_Conn_Device_Group Device Groups to
the new access domain. 

 Do not associate the default Device Groups and Templates to other
 sub-tenants other than the first migrated sub-tenant. 

 ( Optional ) Click Templates to
verify that Prisma Access added the following templates and template stacks: 

 Explicit_Proxy_Template 

 Explicit_Proxy_Template_Stack 

 Mobile_User_Template 

 Mobile_User_Template_Stack 

 Remote_Network_Template 

 Remote_Network_Template_Stack 

 Service_Conn_Template 

 Service_Conn_Template_Stack 

 These
are the default template stacks and templates for a standard Prisma
Access deployment; if you added other templates, be sure that Prisma Access 
added them. 

 ( Optional ) If you have other templates associated with
this configuration, select them. 

 Click OK to close the Access
Domain page and return to the Tenants page. 

 Enter the values in Bandwidth (Mbps) for remote
 networks, Users for mobile users, and the number of
 Autonomous DEM Users you want to allocate for each
 deployment type. 

 Use the following guidelines when allocating ADEM units for a tenant: 

 The number of ADEM units you can allocate for mobile users and remote
 networks can be only equal to or less than base license. 

 The minimum number of units you can allocate is 200. 

 After you allocate the ADEM units for a tenant, you can edit or
 remove those units. 

 If you did not purchase an ADEM license for your deployment type
 (Mobile Users or Remote Networks), that choice is grayed out. 

 Click OK . 

 The Panorama Cloud
Services Configuration page
shows the first tenant successfully migrated, and a Tenants drop-down
is added above the Tenants area. 

 Make sure that all the templates and device groups were populated to the
 tenant. 

 Select the tenant from the drop-down list. 

 Go to Panorama Cloud Services Configuration . 

 Select Service Setup . 

 Click the gear to edit the Settings . 

 Make sure that the correct template stack, template, and device group
 (Service_Conn_Template_Stack, Service_Conn_Template, and
 Service_Conn_Device_Group, respectively) were populated to the
 settings. 

 Go to oither tabs for which you have existing configuration (for
 example, Mobile Users—GlobalProtect ,
 Mobile Users—Explicit Proxy ,
 Remote Networks , or Service
 Connection ), click the gear to edit the
 Settings , and make sure that the correct
 template stack, template, and device group were populated to the
 settings. 

 Commit your changes locally to Panorama ( Commit Commit to Panorama . 

 Select Commit Commit to Panorama to save your changes locally on the Panorama that manages Prisma
 Access. 

 If you do not perform a local commit, Prisma Access components do not display
 in the Push Scope when you Commit and Push your changes. 

 Commit and push your changes to make them active in Prisma Access . 

 Select Commit Commit and Push and Edit
Selections in the Push Scope. 

 Select Prisma Access , then
select the tenant you created, Service Setup , Remote Networks ,
and Mobile Users . 

 Click OK to save your changes
to the Push Scope. 

 Commit and Push your
changes. 

 Select Panorama Cloud Services Status . 

 The status page shows the status of all tenants. Because you have created only one tenant, that
 tenant is the only one that displays. If you select that tenant from the
 drop-down, you show a detailed status of that tenant. 

 Selecting a tenant from the drop-down returns you to the Status page for that tenant. 

 Continue to add more tenants to
 Prisma Access . 

 Previous 

 Create an All-New Multitenant Deployment 

 Next 

 Add Tenants to Prisma Access 

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
