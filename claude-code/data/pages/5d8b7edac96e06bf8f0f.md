---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/user-id/deploy-user-id-in-a-large-scale-network/redistribute-user-mappings-and-authentication-timestamps/configure-user-id-redistribution
fetched_at: 2026-08-13T17:01:38Z
source: palo-alto-main
---

# Configure Data Redistribution Clear

Configure Data Redistribution 

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

 Configure Data Redistribution 

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

 User-ID 

 Deploy User-ID in a Large-Scale Network 

 Redistribute Data and Authentication Timestamps 

 Configure Data Redistribution 

 Download PDF 

 Next-Generation Firewall 

 Configure Data Redistribution 

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

 Firewall Deployment for Data Redistribution 

 Next 

 Share User-ID Mappings Across Virtual Systems 

 Configure Data Redistribution 

 Before you configure data
redistribution: 

 Plan the
redistribution architecture. Some factors to consider are: 

 Which
firewalls will enforce policies for all data types and which firewalls
will enforce region- or function-specific policies for a subset of
data? 

 How many hops does the redistribution sequence require to
aggregate all data? The maximum allowed number of hops for user
mappings is ten and the maximum allowed number of hops for IP address-to-username
mappings and IP address-to-tag mappings is one. 

 How can you minimize the number of firewalls that query the
user mapping information sources? The fewer the number of querying
firewalls, the lower the processing load is on both the firewalls
and sources. 

 Configure the data sources from which your redistribution agents
obtain the data to redistribute to their clients: 

 user
mappings from PAN-OS Integrated User-ID agents or Windows-based User-ID agents 

 IP address-to-tag mappings for dynamic address groups 

 username-to-tag mappings for dynamic user groups 

 GlobalProtect for HIP-based Policy Enforcement 

 data for device quarantine ( Panorama
only ) 

 Configure
Authentication Policy . 

 Data redistribution consists
of: 

 The redistribution agent that provides information 

 The redistribution client that receives information 

 Perform
the following steps on the firewalls in the data redistribution
sequence. 

 On a redistribution client firewall, configure
a firewall, Panorama, or Windows User-ID agent as a data redistribution
agent. 

 Select Device Data Redistribution Agents . 

 Add a redistribution agent
and enter a Name . 

 Confirm that the agent is Enabled . 

 Add the agent using its Serial Number or
its Host and Port . 

 To add an agent using a serial number, select the Serial
Number of the firewall you want to use as a redistribution agent. 

 To add an agent using its host and port information: 
 Enter
the information for the Host . 

 Select whether the host is an LDAP Proxy . 

 Enter the Port (default is 5007, range
is 1—65535). 

 ( Multiple virtual systems only ) Enter the Collector
Name to identify which virtual system you want to use
as a redistribution agent. 

 ( Multiple virtual systems only ) Enter and confirm the Collector
Pre-Shared Key for the virtual system you want to use as
a redistribution agent. 

 Select one or more Data Type for
the agent to redistribute. 

 IP User Mappings —IP address-to-username
mappings for User-ID. 

 IP Tags —IP address-to-tag mappings for
dynamic address groups. 

 User Tags —Username-to-tag mappings for
dynamic user groups. 

 HIP —Host information profile (HIP) data
from GlobalProtect, which includes HIP objects and profiles. 

 Quarantine List —Devices that GlobalProtect
identifies as quarantined. 

 ( Multiple virtual systems only ) Configure a
virtual system as a collector that can redistribute data. 

 Skip this step if the firewall receives but does not redistribute
data. 

 You can redistribute information
among virtual systems on different firewalls or on the same firewall.
In both cases, each virtual system counts as one hop in the redistribution
sequence. 

 Select Device Data Redistribution Collector Settings . 

 Edit the Data Redistribution Agent Setup . 

 Enter a Collector Name and Pre-Shared
Key to identify this firewall or virtual system as a User-ID
agent. 

 Click OK to save your changes. 

 ( Optional but recommended ) Configure which networks
you want to include in data redistribution and which networks you
want to exclude from data redistribution. 
 You can include or exclude networks and subnetworks when redistributing
either IP address-to-tag mappings or IP address-to-username mappings. 

 As a best practice, always specify which networks
to include and exclude to ensure that the agent is only communicating
with internal resources. 

 Select Device Data Redistribution Include/Exclude
Networks . 

 Add an entry and enter a Name . 

 Confirm that the entry is Enabled . 

 Select whether you want to Include or Exclude the
entry. 

 Enter the Network Address for
the entry. 

 Click OK . 

 Configure the service route that the firewall uses to
query other firewalls for User-ID information. 

 Skip this step if the firewall only receives user mapping
information from Windows-based User-ID agents or directly from the
information sources (such as directory servers) instead of from
other firewalls. 

 Select Device Setup Services . 

 ( Firewalls with multiple virtual systems only )
Select Global (for a firewall-wide service
route) or Virtual Systems (for a virtual
system-specific service route), and then configure the service route . 

 Click Service Route Configuration ,
select Customize , and select IPv4 or IPv6 based
on your network protocols. Configure the service route for both
protocols if your network uses both. 

 Select UID Agent and then select
the Source Interface and Source Address . 

 Click OK twice to save the
service route. 

 Enable the firewall to respond when other firewalls query
it for data to redistribute. 

 Skip this step if the firewall receives but does not redistribute
data. 

 Configure an Interface Management
Profile with the User-ID service enabled
and assign the profile to a firewall interface. 

 ( Optional but recommended ) Use a custom certificate
from your enterprise PKI to establish a unique chain of trust from
the redistribution client to the redistribution agent. 

 On the redistribution client firewall, create
a custom SSL certificate profile to
use for outgoing connections. 

 Select Device Setup Management Secure Communication Settings . 

 Edit the settings. 

 Select the Customize Secure Server Communication option. 

 Select the custom Certificate you want to
 use. 

 Select the Certificate Profile you
created in Substep 1. 

 Click OK . 

 Customize Communication for Data
Redistribution . 

 Commit your changes. 

 Enter the following CLI command to confirm the certificate
profile ( SSL config) uses Custom certificates : show redistribution agent state <agent-name> (where <agent-name> is
the name of the redistribution agent or User-ID agent. 

 ( Optional but recommended ) Use a custom certificate
from your enterprise PKI to establish a unique chain of trust from
the redistribution agent to the redistribution client. 

 On the redistribution agent firewall, create
a custom SSL/TLS service profile for
the firewall to use for incoming connections. 

 Select Device Setup Management Secure Communication Settings . 

 Edit the settings. 

 Select the Customize Secure Server Communication option. 

 Select the SSL/TLS Service Profile you
created in Step 1. 

 Click OK . 

 Commit your changes. 

 Enter the following CLI command to confirm the certificate
profile ( SSL config) uses Custom certificates : show redistribution service status . 

 Verify the agents correctly redistribute data to the
clients. 

 View the agent statistics ( Device Data Redistribution Agents ) and select Status to
view a summary of the activity for the redistribution agent, such
as the number of mappings that the client firewall has received. 

 Confirm that the Connected status
is yes . 

 On the agent, access the CLI and enter
the following CLI command to check the status of the redistribution: show redistribution service status . 

 On the agent, enter the following CLI command to view
the redistribution clients: show redistribution service client all . 

 On the client, enter the following CLI command to
check the status of the redistribution: show redistribution service client all . 

 Confirm the Source Name in
the User-ID logs ( Monitor Logs User-ID )
to verify that the firewall receives the mappings from the redistribution
agents. 

 On the client, view the IP-Tag log ( Monitor Logs IP-Tag )
to confirm that the client firewall receives data. 

 On the client, enter the following CLI command and
verify that the source the firewall receives the mappings From is REDIST : show user ip-user-mapping all . 

 ( Optional ) To troubleshoot data redistribution,
enable the traceroute option. 
 When you enable the traceroute option, the firewall that receives
the data appends its IP address to the <route> field,
which is a list of all firewall IP addresses that the data has traversed.
This option requires that all PAN-OS devices in the redistribution
route use PAN-OS version 10.0. If a PAN-OS device in the redistribution
route uses PAN-OS 9.1.x or earlier versions, the traceroute information
terminates at that device. 

 On the redistribution agent where the source
originates, enter the following CLI command: debug user-id test cp-login traceroute yes ip-address <ip-address> user <username> (where <ip-address> is
the IP address of the IP address-to-username mapping you want to
verify and <username> is
the username of the IP address-to-username mapping you want to verify. 

 On a client of the firewall where you configured the
traceroute, verify the firewall redistributes the data by entering
the following CLI command: show user ip-user-mapping all . 

 The firewall displays the timestamp for the creation of
the mapping ( SeqNumber ) and whether
the user has GlobalProtect ( GP User ). 

 admin > show user ip-user-mapping-mp ip 192.0.2.0

IP address: 192.0.2.0 (vsys1)
User: jimdoe
From: REDIST
Timeout: 889s
Created: 11s ago
Origin: 198.51.100.0
SeqNumber: 15895329682-67831262
GP User: No
Local HIP: No
Route Node 0: 198.51.100.0 (vsys1)
Route Node 1: 198.51.100.1 (vsys1) 

 Previous 

 Firewall Deployment for Data Redistribution 

 Next 

 Share User-ID Mappings Across Virtual Systems 

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
