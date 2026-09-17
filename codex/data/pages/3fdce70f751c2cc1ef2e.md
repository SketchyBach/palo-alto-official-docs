---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/clean-pipe/complete-the-clean-pipe-configuration/enable-multitenancy-and-create-a-tenant.html
fetched_at: 2026-09-17T06:45:43Z
source: palo-alto-main
---

# Enable Multitenancy and Create a Tenant Clear

Updated on 

 Thu Sep 03 12:12:03 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access for Clean Pipe 

 Complete the Clean Pipe Configuration 

 Enable Multitenancy and Create a Tenant 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Enable Multitenancy and Create a Tenant 

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

 Complete the Clean Pipe Configuration 

 Next 

 Authenticate Mobile Users 

 Enable Multitenancy and Create a Tenant 

 Shows the steps you perform to enable multitenancy and
create a tenant in a Clean Pipe deployment. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Prisma Access 
 license 

 To begin the Clean Pipe configuration, you
create a multitenant deployment in Panorama and create one or more
tenants. 

 Install and activate Prisma Access for Clean Pipe. 

 Prisma Access for Clean Pipe requires a separate license,
and activating it creates Clean Pipe-specific tabs in the Cloud
Services plugin. The procedure you use to install Prisma Access 
for Clean Pipe is the same as the procedure you use to activate and
install a Prisma Access license, including installing the Cloud
Services plugin. 

 Enable Multitenancy if you have not done so already. 

 Select Panorama Cloud Services Configuration . 

 Select Enable Multitenancy (located on
the upper right of the page). 

 Click OK . 

 The Tenants page displays. 

 In the Options area, select Clean
Pipe . 

 To configure a tenant for remote networks, mobile users,
or both, see Manage Multiple Tenants in Prisma Access . 

 Enter a Name for the first tenant. 

 Create and configure a new Access Domain for
the first tenant and click OK . 

 In the Clean Pipe area, enter
a Bandwidth (Mbps) for This Tenant . 

 Enter a minimum of 100 Mbps for each tenant you create. 

 Click OK . 

 Create zones for the tenant and map those zones for the tenant. 

 Select Network Zones . 

 Make sure that selected the Clean Pipe Template for
the tenant you created ( cp-tpl- tenant ). 

 Create zones for the tenant (for example, Trust and Untrust ). 

 Select Panorama Cloud Services Configuration and select
the Tenant from the drop-down list. 

 Select the Clean Pipe tab. 

 Click the gear icon next to Zone Mapping to
edit the settings. 

 Add and Remove the
zones you created to map them to trusted and untrusted zones. 

 Onboard
a new Clean Pipe. 

 Select Panorama Cloud Services Configuration Clean Pipe . 

 Add a new Clean Pipe instance
for the tenant, entering the following information: 

 Name —Specify a name for the
clean pipe. 

 Bandwidth —Select the Bandwidth to
allocate for the clean pipe. 

 You can onboard Clean Pipe instances
in increments of 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps,
1000 Mbps, 2000 Mbps, 5000 Mbps, and 10000 Mbps. The amount of bandwidth
you specify must be within the licensed bandwidth allocation, and
it must match the bandwidth of the VLAN attachment you create in
the Partner Interconnect. 

 Edge Availability Domain —Select the availability
domain you want for the clean pipe. You can choose 1 , 2 , ANY ,
or REDUNDANT . 

 Specify ANY for
a non-redundant Clean Pipe deployment. 

 Make sure that your
cloud provider supports this choice; you must also select ANY on
the cloud provider side of the partner interconnect. If that choice
is not available for your cloud provider, make another choice. 

 To specify two VLAN attachments in the same location in an active/backup
configuration in the same location, select REDUNDANT . 

 Prisma
Access creates two pairing keys for a REDUNDANT configuration
(one for each availability zone), and appends the clean pipe name
with zone1 for the first availability zone and zone2 for
the second availability zone. For example, if you specify a Name of San
Francisco , Prisma Access creates two zones named San
Francisco-zone1 and San Francisco-zone2 . 

 Be
sure that you configure the first availability zone (zone1) as the
primary zone on your CPE. 

 You can also build a pair
of clean pipes for a single tenant redundancy in different locations;
to do so, specify 1 for the first clean pipe in one location
and 2 for the second clean pipe in a different location. 

 BGP Peer ASN —Enter the BGP Autonomous
System Number (ASN). 

 You can specify either a private or public
BGP ASN. 

 Make a note of this value; you configure it on the
customer edge (CE) router when you complete the Clean Pipe configuration. 

 Location —Select the location. 

 We
recommend that you use the same location that you use when you create
the VLAN attachment for the partner interconnect. 

 To enable QoS, select QoS , then select
the QoS Profile to use with the clean pipe. Clean Pipe QoS shapes
on ingress. 

 Add more Clean Pipe instances as required by repeating
Step 4. 

 Be sure that each additional Clean Pipe uses a different
location. 

 Commit
and push your changes to make them active in Prisma Access . 

 Select Commit Commit and Push and Edit
Selections in the Push Scope. 

 Select Prisma Access , then
select Clean Pipe . 

 Click OK to save your changes
to the Push Scope. 

 Commit and Push your
changes. 

 Check that
your Clean Pipe has been provisioned. 

 Select Panorama Cloud Services Status . 

 Select the Tenant from the
drop-down list at the top of the page. 

 Click Status . 

 The Clean Pipe status displays. 

 Hover over the Clean Pipe Config Status and
wait until the status changes from Provisioning in Progress to Provisioned . 

 This provisioning can take up to 30 minutes. 

 Click the Network Details tab,
click the Clean Pipe radio button, and make
a note of the Pairing Key . 

 The MSSP CE and Cloud
Router IP fields are blank when you start to configure
the Clean Pipe. These fields populate after you create the VLAN
Attachment when you complete the Clean Pipe configuration. 

 If
you specified a REDUNDANT connection, Prisma
Access creates two pairing keys, one for each availability zone,
and appends the clean pipe name with zone1 for
the first availability zone and zone2 for the
second availability zone. The following screenshot shows the SanFrancisco clean
pipe with a redundant configuration; Prisma Access has created two
pairing keys, one for SanFrancisco-zone1 and
one for SanFrancisco-zone2 . 

 Be
sure that you configure the first availability zone (zone1) as the
primary zone on your CPE. 

 Complete the Clean Pipe Configuration. 

 Previous 

 Complete the Clean Pipe Configuration 

 Next 

 Authenticate Mobile Users
