---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/release-notes/new-features/prisma-sd-wan-release-information/prisma-sd-wan-features-introduced-in-2020/features-introduced-in-march-2020
fetched_at: 2026-08-13T17:31:38Z
source: palo-alto-main
---

# Prisma SD-WAN Features Introduced in March 2020 Clear

Prisma SD-WAN Features Introduced in March 2020 

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

 Prisma SD-WAN Features Introduced in March 2020 

 Updated on 

 Tue Aug 11 22:44:50 PDT 2026 

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

 Tue Aug 11 22:44:50 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN New Features 

 Prisma SD-WAN Release Information 

 Prisma SD-WAN Features Introduced in 2020 

 Prisma SD-WAN Features Introduced in March 2020 

 Download PDF 

 Prisma SD-WAN 

 Prisma SD-WAN Features Introduced in March 2020 

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

 Prisma SD-WAN Features Introduced in April 2020 

 Next 

 Prisma SD-WAN Features Introduced in February 2020 

 Prisma SD-WAN Features Introduced in March 2020 

 Learn what’s new in Prisma SD-WAN in March 2020. 

 New Feature/Enhancement Description 

 Detailed View of Secure Fabric and Third-Party
Connections The Connectivity option in the Site Summary
window can now display all overlay connections in one place, including
the following information: 

 Site Connectivity Status:
The site connectivity status of Branch-DC, Branch-3rdParty, and
Branch-Branch sites are graphically displayed. The drop-down next
to each site lets you view the Secure Fabric Links or 3rd Party links
for the selected site. The color legend indicates the status of
the connectivity and is interpreted as follows: 

 Red:
No connectivity established 

 Green: Full connectivity established 

 Yellow: Partial connectivity 

 Grey: Admin down 

 Nascent: Initial (no connectivity) 

 Connectivity Window: On clicking the Secure Fabric Link or 3rd
Party VPN link, the Connectivity window is displayed from where
you can select one or all VPNs, choose a chart, view ingress and
egress traffic, and view link analytics. 

 Connected Site List Filtering: The list of connected sites can
be filtered by the site or endpoint name, site tags, or site connectivity. 

 Setting Administrative State: Check the checkbox to set the
Admin Up option at the Secure Fabric Link level or Site level. By
default, the Admin Up option is checked, unchecking the option means
that connections have been administratively brought down. 

 Enhanced Site Details: Use the icons in the header section to
delete a site, edit the name, description, and tags of a site, and
change the address of a site. 

 Branch-Branch Connectivity: In full-mesh architecture, where
you have site-to-site connectivity, you can view both active and
backup links. 
 Active link is indicated by a solid green line. 

 Backup link is indicated by a dotted green line. 

 Add Link to a Site: Use the Add Link button to directly add
a new Secure Fabric Link to a site. Select the circuit, fill in
the name, description, and tags for the chosen site and save the
link. 

 Additional Sorting and Filtering Capabilities
for Improved Stacked Policy Management Stacked Policies under Policies tab has improved
filtering and sorting capabilities. The Path Policy Rules and QoS
Policy Rules can now be filtered using these additional parameters. 

 Path Policy: You can filter path policy rules based on Rule
Name or Circuit Category Name, Network Context, or Path. You can
sort path policy rules based on rules that are enabled, order of
the rules, name, network context, and source and destination prefixes. 

 QoS Policy: You can filter QoS policy rules based on Rule Name,
Network Context, or Priority. You can sort QoS policy rules based
on rules that are enabled, order of the rules, name, network context,
source and destination prefixes, priority of the application, and
the DSCP value. 

 Ability to Bulk Download Multiple WAN Clarity
Report Packages Reports can be downloaded in bulk individually
or for a week. The date range is in the folder name. The description
of the Reports can be viewed by clicking the 'i' icon next to the
reports. 

 Ability to View Past and Active Remote Access
Device Toolkit Sessions A list view of active remote sessions and the
history of previously accessed remote sessions for claimed devices
is now available. Click the gear icon on the Claimed Devices page
and select Remote Sessions. The Remote Sessions screen will display both
the Active Sessions and History tabs. You can filter to view your
lists by Session ID, Element ID or Operator. 

 Enhanced Filtering in Map View The Prisma SD-WAN portal MAP tab has been enhanced
to include the following changes: 
 Map View Filtering Options:
The Map view includes two new filtering options, Domain and Tag
to improve filtering by domains or tags. 

 Site List Filtering Options: 

 The Site List view includes
two new filtering options, All Domains and All Statuses to filter
by domains or status. 

 The filter icon drop-down on the sites screen can be used to
filter a site by Type, Mode, or Tag. A blue dot indicates that a
filter criterion has been set. 

 Enhanced RMA Wizard When using the RMA Wizard to replace a device,
there will be an option to upload a previously-downloaded JSON configuration
file that you may apply to the replacement device. 

 Enhanced Syslog Export Syslog messages will be generated on initial
flow-rule classification and end-of-flow for all flows handled by
the ION device. The Syslog messages are in RFC 5424 format. An administrator
can configure to export flow logs from an ION device to one or more Syslog
Servers. Device Software Version Required: 5.1.17 or 5.2.3 

 Previous 

 Prisma SD-WAN Features Introduced in April 2020 

 Next 

 Prisma SD-WAN Features Introduced in February 2020 

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

 Release Notes 

 Prisma SASE 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
