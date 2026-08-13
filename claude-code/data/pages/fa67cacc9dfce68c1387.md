---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/plan-your-migration-to-the-new-model
fetched_at: 2026-08-13T17:25:18Z
source: palo-alto-main
---

# Plan Your Migration to the New Model Clear

Plan Your Migration to the New Model 

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

 Plan Your Migration to the New Model 

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

 Prisma Access Remote Networks 

 Plan Your Migration to the New Model 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Plan Your Migration to the New Model 

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

 Allocate Remote Network Bandwidth 

 Next 

 Migrate Your Bandwidth Management Settings 

 Plan Your Migration to the New Model 

 Learn how to plan from a deployment that allocates bandwidth by Prisma Access location to
 one that aggregates bandwidth by compute location. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Prisma Access 
 license 

 Bandwidth for new Prisma Access remote network deployments are allocated at
 an aggregate level per compute location, also known as the aggregate bandwidth
 model . Allocating bandwidth at a compute location level offers you more
 flexibility in allocating your licensed remote network bandwidth, because Prisma Access 
 dynamically allocates the bandwidth for each location based on load or demand. 

 If you have an existing deployment that allocates bandwidth by Prisma Access location,
 you can migrate to the aggregate bandwidth model. You can also migrate your remote
 network QoS deployment. When you migrate, all remote networks use the aggregate
 bandwidth model. 

 Use the following checklist to plan for the migration to the aggregate bandwidth
 model: 

 Note the following remote network components that remain unchanged after
 migration: 

 There are no changes to the dataplane. Traffic continues to flow through
 the Prisma Access dataplane without any change to the existing
 configuration. 

 The migration does not impact existing tunnels. 

 No reconfiguration of your IPSec tunnel parameters are required. IKE
 gateways, IKE and IPSec crypto profiles, and IPSec tunnel configurations
 remain unchanged. 

 The remote network Service Endpoint
 Address (the FQDN or public IP addresses used on the Prisma Access side
 of the IPSec tunnel for the remote network connection) does not change
 for each remote network when you migrate your deployment to the
 aggregate bandwidth model. 

 Prisma Access assigns IPSec termination nodes and allocates bandwidth to remote
 networks during a migration to the aggregate bandwidth model. You should
 understand how this model works before you migrate. 

 If you want to reassign an existing remote network to another IPSec
 termination node after migration, Prisma Access assigns another Service Endpoint Address to the remote
 network after you commit and push your changes. In this case, you will need
 to reconfigure your CPE to point to the new IP address for the remote
 network tunnel. 

 If you have an unsupported configuration, you will not see the Bandwidth
 Allocation tab or view the banner to migrate. The following configurations are
 not supported for migration to the aggregate bandwidth model: 

 A remote network with a bandwidth of 1000
 Mbps . 

 A Prisma SD-WAN CloudBlade integration with
 Prisma Access that has a version earlier than 3.0. 

 A remote network configuration that provides secure inbound access 
 to applications at a remote network site earlier than 2.1
 Innovation. 

 If you have an use QoS with your remote networks, be sure to follow the QoS
 migration guidleines before you migrate. 

 If you’re not sure which model your deployment is using, Select Panorama Cloud Services Configuration Remote Networks . 

 If you see a Bandwidth field in the Remote
 Networks area, you are allocating bandwidth by Prisma Access location,
 and you can migrate to the aggregate bandwidth model. 

 If you see an IPSec Termination Node , you have
 already migrated to the aggregate bandwidth model. 

 After you migrate to the aggregate bandwidth model, the change is permanent and
 you cannot revert to having a deployment that allocates bandwidth by Prisma
 Access location. 

 You must have a minimum of 50 Mbps of available bandwidth to migrate to the
 aggregate bandwidth model. 

 If you want to implement QoS after migration, learn the differences about
 configuring QoS for an aggregate bandwidth deployment. 

 Be sure to use a Class Bandwidth Type of
 Percentage instead of
 Mbps in your QoS profiles. Prisma Access does
 not support bandwidth types of Mbps in QoS
 profiles for deployments that allocate bandwidth by compute
 location. 

 Understand how to specify a guaranteed bandwidth ratio and how to
 customize bandwidth per site. 

 Using a guaranteed bandwidth ratio, you can allocate a percentage of the
 total allocated bandwidth in the compute location. Prisma Access divides
 the guaranteed bandwidth equally by the number of IPSec termination
 nodes in the compute location. 

 By customizing the bandwidth per site, you can apply an allocation ratio
 for the sites an a single IPSec termination node and specify QoS
 profiles per site in the remote network Settings .
 Alternatively, you can specify a QoS profile during remote network
 configuration by selecting the remote network and specifying a QoS
 profile in the QoS tab. 

 If you have configured your remote networks to provide secure inbound access to
 your remote network locations , all existing inbound access features
 are supported, such as enabling a secondary WAN link ( Enable
 Secondary WAN ), BGP, QoS and source NAT options. There is also
 no change to the bandwidth that is consumed 
 by the public IP addresses that Prisma Access allocates (5 IP addresses take 150
 Mbps from your remote network license allocation, and 10 IP addresses take 300
 Mbps). 

 If you need to configure inbound access after you migrate, use the inbound access
 procedure that is specific to the aggregate bandwidth
 model . 

 Palo Alto Networks recommends that you take a note of your existing bandwidth
 settings and total licensed bandwidth before you migrate. 

 Although Prisma Access migrates your bandwidth during migration; you should
 note your current settings as a best practice and make any adjustments to
 the compute location bandwidth after you migrate. 

 Check your existing bandwidth settings by selecting Panorama Cloud Services Configuration Remote Networks and make a note of the existing
 Bandwidth that is available for each remote
 network connection. 

 Navigate to Panorama Licenses and check your total licensed bandwidth in Mbps for
 remote networks. This information is included under Prisma
 Access 
 Net Capacity or GlobalProtect Cloud
 Service for Mobile Users , depending on your license
 type. 

 After you migrate, make a note of the following differences to your deployment: 

 You onboard all new remote networks using the aggregate bandwidth remote network
 onboarding procedure. 

 When you view Bandwidth Usage Statistics, you view them at a per-IPSec
 termination node level. 

 Bandwidth Allocation for a Migrated Aggregate Bandwidth Deployment 

 If you have a deployment that allocates bandwidth by Prisma Access location, Prisma
 Access makes the following changes when you migrate to the aggregate bandwidth
 model: 

 Prisma Access sums the bandwidth for all locations in a given compute
 location and allocates the summed bandwidth to that compute location. 

 For example, you have three locations ( Location 1 , Location 2 ,
 and Location 3 ) in the Mexico West, US Southwest, and US West
 locations, and each existing location has 50 Mbps of bandwidth. Since each
 location is in the US Southwest compute location, Prisma Access sums the
 bandwidth of the three locations and allocates 150 Mbps of bandwidth to the
 US Southwest location. 

 If all the location or locations in a compute location have a total bandwidth
 of less than 50 Mbps, Prisma Access will increase the bandwidth to 50 Mbps
 for that compute location. Prisma Access provides you with the locations
 that require the bandwidth increase during the migration process. 

 Prisma Access uses IPSec termination nodes in aggregate bandwidth
 deployments. During migration, Prisma Access provides one IPSec termination
 node per compute location for every 1,000 Mbps of allocated bandwidth. For
 example, if you allocate 1500 Mbps of bandwidth in a compute location,
 Prisma Access provides that location with two IPSec termination nodes. 

 You assign IPSec termination nodes to a remote network during remote network
 onboarding. In an aggregate bandwidth migration, Prisma Access associates
 the IPSec termination nodes to the remote networks during migration. The
 following list provides some examples of IPSec termination node association
 for a migration: 

 If you have four remote networks that are in the same compute
 location, and those locations has 50 Mbps each of bandwidth each,
 Prisma Access allocates 200 Mbps of bandwidth to that compute
 location, provides a single IPSec termination node to that compute
 location, and associates that IPSec termination node to all four
 remote networks. 

 If you have three remote networks in the same compute location with
 100 Mbps each, Prisma Access allocates 300 Mbps of bandwidth to that
 compute location, provides a single IPSec termination node to that
 compute location, and associates that IPSec termination node to all
 three remote networks. 

 If you have seven remote networks in the same compute location, with
 two remote networks having 500 Mbps and five remote networks having
 100 Mbps each, Prisma Access allocates 1500 Mbps of bandwidth to
 that compute location. Because the total allocated bandwidth in that
 compute location is greater than 1,000 Mbps, Prisma Access allocates
 two IPSec termination nodes and makes the following
 associations: 

 The two 500 Mbps remote networks are assigned one IPSec
 termination node (one node for each 1,000 Mbps remote
 network). 

 The five 100 Mbps remote networks are assigned one IPSec
 termination node. 

 After you migrate, you can change the IPSec termination node association to
 increase bandwidth for a location. For example, given a compute location
 with two IPSec termination nodes, you could reassign a single IPSec
 termination node to a single location and reassign the other IPSec
 termination node to the remaining locations, which effectively provides the
 location that does not share an IPSec termination node with more
 bandwidth. 

 If you reduce bandwidth sufficiently, you might have to release an IPSec
 termination node. For example, if you reduce the bandwidth in a compute
 location from 1500 Mbps to 800 Mbps, you would need to remove one of the
 existing IPSec termination nodes. If any of those nodes are being used by
 existing locations, you must reassign the IPSec termination node before you
 delete the IPSec termination node. 

 QoS Migration Guidelines 

 If you use QoS with your current Prisma Access remote network deployment and you
 allocate bandwidth by location, you can migrate to an aggregate bandwidth deployment
 while still retaining your existing QoS policies and profiles . 

 Using the aggregate bandwidth model, you allocate bandwidth at an aggregate level per
 compute location, and Prisma Access dynamically allocates the bandwidth based on
 load or demand per location. 

 After migration, the QoS tab displays the QoS configuration in
 the remote network settings ( Panorama Cloud Services Configuration Remote Networks Settings ). Any compute locations that map to locations that have QoS enabled
 have Enable QoS selected; any compute locations that map to
 locations that do not have QoS enabled have Enable QoS 
 deselected. 

 The following screenshot shows a sample QoS tab after migration. A remote network in
 the US West location has QoS enabled, and no other locations have QoS enabled. Since
 the US West location maps to the US Southwest compute location, the
 QoS tab shows QoS enabled for the US Southwest compute
 location. 

 Palo Alto Networks makes the following recommendations and requirements for QoS in an
 aggregate bandwidth deployment. 

 Because bandwidth is shared for all locations in a single compute location,
 you should change the Class Bandwidth Type of
 Mbps to Percentage . The
 only time that a bandwidth type of Mbps is supported
 is when you have an existing deployment that allocates bandwidth by location
 and you then migrate to an aggregate bandwidth deployment. 

 You cannot adjust QoS bandwidth allocation based on Mbps in the profile; for
 profiles that use a Percentage bandwidth type, you
 can change the QoS bandwidth per location by adjusting the Guaranteed
 Bandwidth Ratio and customizing the QoS profile per site. 

 You cannot mix bandwidth types in a compute location; if you do, you receive
 an error message during commit. 

 If you add new locations and those locations belong to a new compute
 location, you will only be able to create profiles that have a
 Class Bandwidth Type of
 Percentage in the new compute location. 

 If you retain QoS profiles that have a Class Bandwidth
 Type of Mbps , any changes you make to
 the Guaranteed Bandwidth Ratio or customize the QoS profile per site are
 ignored. 

 After migration, any locations who use QoS profiles with a Class
 Bandwidth Type of Mbps show a
 QoS Class Type For Sites of
 Mbps for their corresponding compute location in
 the QoS tab. QoS Profiles with a Class
 Bandwidth Type of Percentage show a
 QoS Class Type For Sites of
 Percentage . 

 In addition, you cannot select any QoS profiles that have a Class
 Bandwidth Type of Mbps . The following
 screenshot shows the US Southwest compute location using a QoS profile with
 a Class Bandwidth Type of
 Mbps . That choice is not selectable in the drop-down
 in the QoS Profile area. 

 However, you can select a QoS Profile that uses a Class Bandwidth
 Type of Percentage (QoS-2 in this
 example). 

 If you change the QoS profile for a compute location from a Class
 Bandwidth Type of Mbps to
 Percentage , you should make the change during a
 maintenance window or during off peak hours. Changing the QoS profile might
 change the traffic prioritization. 

 You can only select QoS profiles with a Class Bandwidth
 Type of Percentage when you customize
 the QoS profile per site. 

 Previous 

 Allocate Remote Network Bandwidth 

 Next 

 Migrate Your Bandwidth Management Settings 

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
