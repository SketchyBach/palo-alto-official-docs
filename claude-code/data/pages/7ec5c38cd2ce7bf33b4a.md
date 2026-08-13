---
url: https://docs.paloaltonetworks.com/prisma-access/administration/manage-multiple-tenants-in-prisma-access/plan-your-multitenant-deployment
fetched_at: 2026-08-13T17:24:26Z
source: palo-alto-main
---

# Plan Your Multitenant Deployment Clear

Plan Your Multitenant Deployment 

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

 Plan Your Multitenant Deployment 

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

 Plan Your Multitenant Deployment 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Plan Your Multitenant Deployment 

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

 Multitenancy Configuration Overview 

 Next 

 Create an All-New Multitenant Deployment 

 Plan Your Multitenant Deployment 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager) , see Prisma SASE . 

 Prisma Access 
 license 

 Before you enable multitenancy, migrate the first tenant, and
create additional tenants, make sure that you have all required
information and resources to do so by completing the following tasks: 

 If you are migrating an existing
single-tenant deployment to a multitenant deployment ,
make a note of the following Prisma Access features that are not
supported. See the Palo Alto Networks Compatibility
Matrix for the list of unsupported features. 

 If don’t have an existing Prisma Access configuration, you Enable
Multitenancy and add your tenants; then, then configure
the tenants after you create them. See Create an All-New Multitenant Deployment for more
information. 

 Make a note of your license allocation for remote networks
and mobile users. 

 Open your license ( Panorama Licenses ) and find the Prisma
Access Total Mbps (remote networks bandwidth
pool) for remote networks and User Limit (total
number of licensed users) for mobile users. 

 When you create
tenants, you assign resources for remote networks and mobile users
from this license allocation. If you run out of the minimum required licensed
Mbps for remote networks or mobile users, you cannot create additional
tenants. 

 You should also make a note of the bandwidth
and mobile users allocation for your existing configuration. After
you migrate your configuration to the first tenant, check these
values to verify that the first tenant migrated correctly. 

 Make a list of the names you will use to identify each tenant. 

 When you create tenant names, avoid using names
like Tenant-1 , Tenant-2 , Tenant-3 , and
so on. The system logs reserve a small number of characters for
the tenant name in the log output and, if tenants have similar names,
it can be difficult to associate the tenant with the logs. We recommend
using a unique and short name for tenants (for example, Acme or Hooli ). 

 Make a list of the administrative users you will create and
assign for each tenant, and note the maximum number of administrative
users that can be logged in concurrently. 

 When administrative
users are performing normal multitenant operations such as configuration
changes and commit operations, we recommend having a maximum of
12 administrative users logged in to Panorama concurrently. 

 An
administrative user who can manage multiple tenants can provision
up to 200 tenants at the same time with a single commit operation. 

 Be sure that you have sufficient license resources to enable
multiple tenants. 

 The minimum license allocation for each
tenant is 200 Mbps for each remote network or 200 mobile users.
You can also create a tenant with only remote networks or mobile
users, and can configure tenants in differing configurations on
the same Panorama. For example, you could create a tenant with remote
networks only, a tenant with mobile users only, or a tenant with
both mobile users and remote networks, as long as each tenant meets
the minimum license allocation and the relevant licenses are activated
and associated with the Panorama where you configure the tenants. 

 When configuring a tenant in multitenancy mode, create a
unique name for each IPSec tunnel and IKE gateway for service connections
and remote network connections, and try to use a name that will
not be duplicated by another tenant. While there is no effect to
functionality, you cannot delete an IPSec tunnel or IKE gateway
if another tenant is using a tunnel or gateway with the same name. 

 This caveat applies to all objects, including QoS profiles (you cannot delete
 objects with duplicate names in a multi-tenant deployment if one of the objects
 is being referenced by another tenant). 

 Single-tenant users cannot view system logs; only superusers
can. You can, however, sort logs by tenant . 

 When a mobile user logs into a single Prisma Access tenant, the user consumes one
 license unit. If a user logs into additional tenants under a single multitenant
 deployment, the user consumes one license unit for each tenant they are logged
 in. For example, if a single user is logged into five tenants, the user consumes
 five mobile user license units in total. 

 When using the multitenancy feature and logged in as a tenant-level administrative
user, opening the Panorama Task Manager (clicking Tasks at
the bottom of the Panorama web interface) shows all tasks for all
tenants, including any tasks done at the superuser (Admin) level. 

 Some Prisma Access features are not supported for use with
multitenancy. See Multitenancy Unsupported Features in
the Palo Alto Networks Compatibility
Matrix for details. 

 If you back up a Panorama configuration,
then revert it to an earlier
saved configuration, Panorama cannot revert to the configuration
you saved if you perform the following actions in the following
order: 

 Backup a Panorama configuration. 

 Delete a tenant. 

 Restore the configuration. 

 If you delete
a tenant, you cannot use any of the previous backups you saved before
you deleted the tenant. However, you can use any backups you make
after you delete the tenant. 

 Previous 

 Multitenancy Configuration Overview 

 Next 

 Create an All-New Multitenant Deployment 

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
