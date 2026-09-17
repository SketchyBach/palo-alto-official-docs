---
url: https://docs.paloaltonetworks.com/prisma-access/administration/manage-multiple-tenants-in-prisma-access/sort-logs-by-device-group-id-for-external-logging
fetched_at: 2026-09-16T07:46:04Z
source: strata-and-sase
---

# Sort Logs by Device Group ID in a Multitenant Deployment Clear

Updated on 

 Thu Sep 03 12:12:03 PDT 2026 

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
