---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/prisma-access-integrations/prisma-access-for-networks-aggregate-bandwidth-licensing/qos-cir-support-for-aggregate-bandwidth
fetched_at: 2026-08-13T17:29:21Z
source: palo-alto-main
---

# QoS CIR Support For Aggregate Bandwidth Clear

QoS CIR Support For Aggregate Bandwidth 

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

 QoS CIR Support For Aggregate Bandwidth 

 Updated on 

 Wed Feb 25 08:09:54 PST 2026 

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

 Wed Feb 25 08:09:54 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN CloudBlades Integration with Prisma Access 

 Prisma Access for Networks Aggregate Bandwidth Licensing 

 QoS CIR Support For Aggregate Bandwidth 

 Download PDF 

 Prisma SD-WAN 

 QoS CIR Support For Aggregate Bandwidth 

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

 Prisma Access for Networks Aggregate Bandwidth Licensing 

 Next 

 IPSec Termination Nodes Within Prisma 

 QoS CIR Support For Aggregate Bandwidth 

 Use QoS CIR support for bandwidth allocation for a compute location in Prisma
 Access. 

 Where Can I Use This? What Do I Need? 

 Supported CloudBlades: 

 Prisma Access for Networks (Managed by Panorama) 

 Prisma Access for Networks (Cloud Managed) 

 Prisma SD-WAN 

 Prisma Access 

 Supported Cloud Plugin Versions 

 Prisma Access for Networks (Managed by Panorama) CloudBlade versions 3.x.x and
 later 

 Prisma Access for Networks (Cloud Managed) CloudBlade versions 3.x.x and
 4.x.x 

 In Aggregate Bandwidth licensing mode, the bandwidth allocation is done for a
 compute location on Prisma Access. To use QoS with remote networks, you enable or
 disable QoS and specify the guaranteed bandwidth at the compute location level. The
 number of tunnels terminating within a compute location and SPN share the aggregate
 bandwidth allocated. You must configure the CIR for specific tunnels terminating on an
 SPN within a compute location to guarantee the Quality of Service (QoS). 

 Panorama Managed CloudBlade 

 Cloud Managed CloudBlade 

 QoS CIR Support for Aggregate Bandwidth (Panorama Managed CloudBlade) 

 Create or use an existing QoS CIR to define QoS support for aggregate bandwidth
 (Panorama Managed CloudBlade). 

 You use QoS Profiles to shape the traffic at egress point by defining QoS classes and
 assigning a bandwidth to them. Select either an existing QoS profile or create a new
 QoS Profile when you enable QoS for Prisma Access. 

 Add a QoS Profile . 

 You can edit any existing QoS profile, including the default, by clicking the
 QoS Profile name. 

 In Panorama, select Network Network Profiles QoS Profile and Add a new profile. 

 Enter a descriptive Profile Name . 

 Set the overall bandwidth limits for the QoS profile rule. 

 Enter an Egress Max value to set the
 overall bandwidth allocation for the QoS Profile rule. 

 Enter an Egress Guaranteed value
 (bandwidth that is the guaranteed bandwidth for this profile
 (in Mbps). 

 Any traffic that exceeds the Egress Guaranteed value is best
 effort and not guaranteed. Unused guaranteed bandwidth continues
 to remain available for all traffic. 

 In the Classes section, Add one or more classes
 and specify how to mark up to eight individual QoS classes. 

 Select the Priority for the class
 (either real-time ,
 high ,
 medium , or
 low ). 

 Enter the Egress Max and the
 Egress Guaranteed for traffic
 assigned to each QoS class. 

 The guaranteed bandwidth assigned
 to a class isn't reserved for that class; any unused
 bandwidth remains available for all traffic. If a class of
 traffic exceeds the egress-guaranteed bandwidth, Prisma
 Access handles that traffic on a best-effort basis. 

 Enter a Class Bandwidth Type for the
 profile. 

 Click OK . 

 Click OK to save the changes. 

 For Default QoS Profiles , enable QoS for your remote
 network locations that allocate bandwidth by compute location. 

 Determine the Prisma Access locations where you want to deploy QoS;
 then find the compute location that corresponds to each location. 

 Each location is allocated bandwidth from its compute location, and
 you must know the name of the compute location for the locations
 where you want to allocate QoS. For a list of compute
 location-to-location mapping, see Prisma Access , or select Panorama Cloud Services Configuration Remote Networks Aggregate Bandwidth and click the gear icon; the mappings display in the
 Compute Location and Prisma
 Access Location columns. 

 Select Panorama Cloud Services Configuration Remote Networks Settings , click the gear to edit the settings, and select
 QoS . 

 Enable QoS at a compute location level. 

 Whatever settings you enter apply to all locations that correspond to
 this compute location. 

 In the case of default QoS Profiles, you must enter the QoS
 Profile , and the Guaranteed Bandwidth
 Ratio . 

 Select Save and Commit 
 your changes. 

 The default QoS Profile does not require any configuration changes in
 Prisma SD-WAN . 

 Customize QoS per Site. 

 In Panorama, go to Settings QoS and select the site that you wish to customize. 

 If you don't wish to use the default profile on the sites, the
 profile can be customized by using Interface or Circuit level tags
 in Prisma SD-WAN . 

 Check the Customize Per Site check box and click
 OK . 

 Select Commit and Push to
 save the changes. 

 In Prisma SD-WAN , navigate to the Site Interfaces/Circuits and assign interface level tags in the following format. 
 prisma_qos:<profile_name>:[0-100] 

 The profile name for QoS will be the same name as the profile created in step
 1. 

 Interface/Circuit level tagging can be done for both ECMP and Non-ECMP
 enabled sites in Prisma SD-WAN . 

 Non-ECMP : Go to the site on Prisma SD-WAN where you wish to customize QoS and tag
 the interface or circuit. In the example shown below, the allocated
 bandwidth is 20%. 

 After you tag the Interface or Circuit, the CloudBlade integration
 applies these changes on Panorama. 

 ECMP : enabled sites allow customizations per
 ECMP link. You must tag the ECMP links where you want to apply the
 QoS customization. 

 After applying the tags, the CloudBlade integration applies these
 changes on Panorama. 

 QoS CIR Support for Aggregate Bandwidth (Cloud Managed CloudBlade) 

 Create or use an existing QoS CIR to define QoS support for aggregate bandwidth
 (Cloud Managed CloudBlade). 

 Use QoS to prioritize the critical traffic in your remote networks, and to set
 maximum and guaranteed bandwidths for remote network sites in a compute
 location. 

 Enable QoS for your remote network locations. 

 Select Configuration NGFW and Prisma Access Remote Networks Bandwidth Management . 

 Determine the Prisma Access locations where you want to deploy QoS;
 then find the compute location that corresponds to each Prisma Access location. 

 Each Prisma Access location is allocated bandwidth from its
 compute location, and you must know the name of the compute location
 for the locations where you want to allocate QoS. 

 Enable QoS at a compute location level in the QoS column. 

 Any changes in settings apply to all locations corresponding to this
 compute location. 

 Edit the QoS settings for the compute location. 

 Select the guaranteed bandwidth ratio, which is a ratio based on the
 entire allocated bandwidth for the compute location. 

 For example, if you have allocated bandwidth of 1,001 Mbps for the US
 Southwest compute location, and you enter a guaranteed bandwidth
 ratio of 82%, the guaranteed bandwidth for that compute location is
 820.82 Mbps. 

 By default, each remote network is given a percentage equal to the
 number of connections. For example, given four connections in a
 compute location and a total guaranteed bandwidth of 820.82 Mbps,
 each location receives 25% of that bandwidth, which is 205.2
 Mbps. 

 Create New QoS Profile or
 Manage to edit an existing QoS profile. 

 Customize QoS settings for remote network sites in a compute location.
 If you have multiple remote networks per compute location and want to
 change either the bandwidth ratio or QoS Profile for each remote
 network, select Customize and change the
 bandwidth allocation ratio, QoS Profile, or both. 

 Select Save and Push your
 changes. 

 In Prisma SD-WAN , navigate to the Site Interfaces/Circuits and assign interface or circuit level tags in the following
 format. 
 Format:

 <profile_name>:<qos_bandwidth> 

 Example:

 prisma_qos:qos_test:20 

 The tags can be both ECMP and Non-ECMP. For Non-ECMP ,
 go to the site on Prisma SD-WAN , where you wish to customize QoS
 and tag the interface or circuit. In the example shown below, the allocated
 bandwidth is 40%. 

 In ECMP , enabled sites allow customizations per ECMP
 link. You must tag the ECMP links where you want to apply the QoS
 customization. 

 After applying the tags, the CloudBlade integration applies these changes on
 the Prisma Access Cloud Management interface. 

 Previous 

 Prisma Access for Networks Aggregate Bandwidth Licensing 

 Next 

 IPSec Termination Nodes Within Prisma 

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

 Prisma SD-WAN 

 Strata Cloud Manager 

 CloudBlades 

 Prisma SASE 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
