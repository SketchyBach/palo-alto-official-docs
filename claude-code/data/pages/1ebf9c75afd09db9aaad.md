---
url: https://docs.paloaltonetworks.com/sd-wan/administration/sd-wan-traffic-steering-using-policies/define-your-application-based-traffic-steering-policies/define-your-application-based-traffic-steering-policies-pan-os
fetched_at: 2026-08-13T17:35:22Z
source: palo-alto-main
---

# PAN-OS & Panorama Clear

PAN-OS & Panorama 

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

 PAN-OS & Panorama 

 Updated on 

 Thu Jul 30 22:19:20 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 Updated on 

 Thu Jul 30 22:19:20 PDT 2026 

 Focus 

 Home 

 SD-WAN 

 SD-WAN Traffic Steering Using Policy Rules 

 Define Your Application-based Traffic Steering Policies 

 PAN-OS & Panorama 

 Download PDF 

 SD-WAN 

 PAN-OS & Panorama 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 PAN-OS & Panorama 

 Configure an SD-WAN policy rule in PAN-OS . 

 Log in to the Panorama Web
 Interface . 

 Select Policies SD-WAN and select the appropriate device group from the
 Device Group context drop-down. 

 Add an SD-WAN policy rule. 

 On the General tab, enter a descriptive
 Name for the rule. 

 On the Source tab, configure the source parameters of
 the policy rule. 

 Add the Source Zone or select
 Any source zone 

 Add one or more source addresses, set an external dynamic list (EDL),
 or select Any Source Address. 

 Add one or more source users or select
 any Source User. 

 On the Destination tab, configure the destination
 parameters of the policy rule. 

 Add the Destination Zone 
 or select Any destination zone. 

 Add one or more destination addresses, set an
 EDL, or select Any Destination Address. 

 On the Application/Service tab, attach your SD-WAN Link Management profiles and specify your applications and
 services. 

 ( SD-WAN 
 plugin 2.0 and later
 versions )
 PAN-OS 10.0.2 supports associating only a SaaS Quality
 Profile or an Error Correction but not both. If you associate one of
 these profiles with an SD-WAN policy rule, you cannot
 associate the other. 

 For example, if you associate a SaaS Quality profile with an SD-WAN policy rule, you are unable to associate an Error
 Correction profile with the same SD-WAN policy rule. 

 Select the Path Quality or define your custom SD-WAN
 application thresholds (using path quality profiles). 

 ( SD-WAN plugin 2.0 and later
 versions )
 Select the SaaS Quality Profile 
 or create a SaaS quality
 profile if the branch firewall has a Direct Internet Access
 (DIA) link to a SaaS application. The default is None
 (disabled) . 

 ( SD-WAN 
 plugin 2.0 and later
 versions )
 Select the Error Correction
 Profile or create an error correction
 profile to apply forward error correction (FEC) or packet
 duplication to the applications that match the SD-WAN 
 policy rule. The default is None
 (disabled) . 

 Add Applications and select one or more
 applications from the list or select Any 
 applications. All applications you select are subject to the health
 thresholds specified in the Path Quality profile you selected. If a
 packet matches one of these applications and that application exceeds
 one of the health thresholds in the Path Quality profile (and the packet
 matches the remaining rule criteria), the firewall selects a new
 preferred path. 

 Add only business-critical applications and applications that are
 sensitive to path conditions for their usability. 

 ( SD-WAN 
 plugin 2.0 and later
 versions )
 If you associate a SaaS Quality
 Profile in Adaptive mode with
 the SD-WAN policy, add the specific SaaS
 applications you want to monitor. Using adaptive monitoring for
 all applications that match the SD-WAN policy
 rule may impact the performance of the SD-WAN 
 firewall. 

 ( SD-WAN 
 plugin 2.0 and later
 versions )
 If you associate a SaaS Quality
 Profile with a specified SaaS application, add the
 SaaS application to the SD-WAN rule to ensure the
 SaaS monitoring settings are applied only to the desired SaaS
 application. 

 Add Services and select one or more services
 from the list or select Any services. All
 services you select are subject to the health thresholds specified in
 the Path Quality profile you selected. If a packet matches one of these
 services and that service exceeds one of the health thresholds in the
 Path Quality profile (and the packet matches the remaining rule
 criteria), the firewall selects a new preferred path. 

 Add only business-critical services and services that are
 sensitive to path conditions for their usability. 

 On the Path Selection tab, select a Traffic
 Distribution profile or create a traffic distribution profile .
 When an incoming packet (unassociated with a session) matches all the match
 criteria in the rule, the firewall uses this Traffic Distribution profile to
 select a new preferred path. 

 On the Target tab, use one of the following methods to
 specify the target firewalls in the device group to which Panorama pushes the
 SD-WAN policy rule: 

 Select Any (target to all devices) (the default)
 to push the rule to all devices. Alternatively, select
 Devices or Tags to
 specify the devices to which Panorama pushes the SD-WAN 
 policy rule. 

 On the Devices tab, select one or more filters to
 restrict the selections that appear in the Name field; then select one
 or more devices to which Panorama pushes the rule, as in this
 example: 

 On the Tags tab, Add one
 or more Tags and select the tag(s) to specify
 that Panorama push the rule to devices that are tagged with the selected
 tags, as in this example: 

 If you specified Devices or Tags, you can select Target to
 all but these specified devices and tags to have
 Panorama push the SD-WAN policy rule to all devices
 except for the specified devices or tagged devices. 

 Click OK . 

 Commit and Commit and Push your
 configuration changes. 

 In an SD-WAN policy rule, you also specify the devices to
 which you want Panorama to push the rule. 

 ( Best Practice ) Create a catch-all SD-WAN policy rule
 to distribute unmatched sessions 
 so that you can control which links any unmatched sessions use and view
 unmatched sessions in logging and reports in the SD-WAN 
 plugin. 

 If you don’t create a catch-all rule to distribute unmatched sessions,
 the firewall distributes them in round-robin order among all available
 links because there is no traffic distribution profile for unmatched
 sessions. Round-robin distribution of unmatched sessions can increase
 your costs unexpectedly and result in loss of application visibility.

 After configuring your SD-WAN policy rules, Create a Security Policy Rule to allow
 traffic (for example, bgp as an
 Application ) from branches to the internet, from
 branches to hubs, and from hubs to branches. 

 ( Optional ) Configure QoS for critical
 applications. 

 If the SD-WAN applications need guaranteed bandwidth
 capacities or if you do not want other applications taking bandwidth
 from critical business applications, create QoS rules to control the
 bandwidth properly. 

 To automatically set up BGP routing between VPN cluster members, in the SD-WAN plugin, Configure BGP routing between branches
 and hubs to dynamically route traffic that will be subject to the SD-WAN failover and load sharing. 

 Alternatively, if you want to manually configure BGP routing on each firewall
 or use a separate Panorama template to configure BGP routing (for more
 control), leave the BGP information in the plugin blank. Instead, configure
 BGP routing. 

 Configure NAT for public-facing
 virtual SD-WAN interfaces. 

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

 IoT Security 

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

 Next-Generation Firewall 

 Administration 

 SD-WAN 

 English 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
