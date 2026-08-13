---
url: https://docs.paloaltonetworks.com/prisma-access/administration/manage-multiple-tenants-in-prisma-access/sort-logs-by-device-group-id-for-external-logging
fetched_at: 2026-08-13T17:24:26Z
source: palo-alto-main
---

# Sort Logs by Device Group ID in a Multitenant Deployment Clear

Sort Logs by Device Group ID in a Multitenant Deployment 

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

 Sort Logs by Device Group ID in a Multitenant Deployment 

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

 Sort Logs by Device Group ID in a Multitenant Deployment 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Sort Logs by Device Group ID in a Multitenant Deployment 

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

 Remove Plugin Access for a Tenant-Level Administrative User 

 Next 

 Prisma Access in a FedRAMP Environment 

 Sort Logs by Device Group ID in a Multitenant Deployment 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 For information about managing multiple tenants in Prisma Access (Managed by Strata Cloud Manager) , see Prisma SASE . 

 Prisma Access license 

 To sort the logs manually by tenant in Panorama,
select Monitor Logs and
choose the Device Group associated with that
tenant to display the logs for that device group. However, if you are
forwarding your logs to an external device, you might have a need
to sort those logs at the tenant level. To do so, find the device
group ID in the logs that is associated with the device group and
use that group ID-to-device group mapping to associate the logs
with a tenant. 

 There are four fields associated with the device
group in the logs: DG Hierarchy Level 1 , DG
Hierarchy Level 2 , DG Hierarchy Level 3 ,
and DG Hierarchy Level 4 . These fields show
the device group IDs in its hierarchy. The shared device group (level
0) is not included in this structure. 

 DG Hierarchy
Level 1 refers to the first device group level in the
hierarchy. If you added children or grandchildren device groups,
the DG Hierarchy Level 2 through DG
Hierarchy Level 4 fields show the hierarchy from the
child group to the great-grandchild group, respectively. 
 To find
logs by tenant, complete the following task. 

 Find
the device group IDs associated with the device group. 

 To find this information using a CLI command, log
into Panorama as a superuser (admin-level user), enter the show readonly command
in configuration mode, and view the values in the device-group heading.
The IDs for the device groups display under the device group name.
The following example shows that the device ID for the acme-sc device
group is 20 . 

 Note that these device
groups are at the first level in the hierarchy ( DG Hierarchy
Level 1 ); you use that information in the query in the
next step. 

 admin# show readonly
...
 device-group {
 acme-sc {
 id 20;
 }
 acme-rn {
 id 39;
 }
 acme-mu {
 id 40;
 }
 hooli-rn {
 id 56;
 }
 hooli-sc {
 id 57;
 }
 hooli-mu {

 To use an API query, enter the following API command: 

 /api/?type=op&cmd=<show><dg-hierarchy></dg-hierarchy></show> 

 For
more information about using APIs with logs, see Retrieve Logs (API) . 

 Use the device group ID-to-device group name mapping
to associate the logs with a tenant. 

 Add the Forwarding parameters
that select the logs you want to forward. 

 Previous 

 Remove Plugin Access for a Tenant-Level Administrative User 

 Next 

 Prisma Access in a FedRAMP Environment 

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
