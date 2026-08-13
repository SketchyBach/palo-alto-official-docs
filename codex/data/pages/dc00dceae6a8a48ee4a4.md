---
url: https://docs.paloaltonetworks.com/ngfw/help/12-1/objects/objects-security-profiles-wildfire-analysis
fetched_at: 2026-08-13T16:50:37Z
source: palo-alto-main
---

# Objects > Security Profiles > WildFire Analysis Clear

Objects > Security Profiles > WildFire Analysis 

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

 Objects > Security Profiles > WildFire Analysis 

 Updated on 

 Thu Jun 25 18:50:04 PDT 2026 

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

 Thu Jun 25 18:50:04 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Objects 

 Objects > Security Profiles > WildFire Analysis 

 Download PDF 

 Next-Generation Firewall 

 Objects > Security Profiles > WildFire Analysis 

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

 Objects > Security Profiles > File Blocking 

 Next 

 Objects > Security Profiles > Data Filtering 

 Objects > Security Profiles > WildFire Analysis 

 Use a WildFire Analysis profile to specify for WildFire
file analysis to be performed locally on the WildFire appliance
or in the WildFire cloud. You can specify traffic to be forwarded
to the public cloud or private cloud based on file type, application,
or the transmission direction of the file (upload or download).
After creating a WildFire analysis profile ,
adding the profile to a policy ( Policies Security ) further allows you
apply the profile settings to any traffic matched to that policy
(for example, a URL category defined in the policy). 

 Use the predefined default profile to forward all unknown files to WildFire for
 analysis. In addition, set up WildFire appliance content updates to
 download and install every minute so you always have the most recent support. 

 WildFire
Analysis Profile Settings 

 Name 

 Enter a descriptive name for the WildFire
analysis profile (up to 31 characters). This name appears in the
list of WildFire Analysis profiles that you can choose from when
defining a Security policy rule. The name is case-sensitive and
must be unique. Use only letters, numbers, spaces, hyphens, and
underscores. 

 Description 

 Optionally describe the profile rules or
the intended use for the profile (up to 255 characters). 

 Shared ( Panorama only ) 

 Select this option if you want the profile
to be available to: 

 Every virtual system (vsys) on
a multi-vsys firewall. If you clear this selection, the profile
will be available only to the Virtual System selected
in the Objects tab. 

 Every device group on Panorama. If you clear this selection,
the profile will be available only to the Device Group selected
in the Objects tab. 

 Disable override ( Panorama only ) 

 Select this option to prevent administrators
from overriding the settings of this Vulnerability Protection profile
in device groups that inherit the profile. This selection is cleared
by default, which means administrators can override the settings
for any device group that inherits the profile. 

 Rules 

 Rules 

 Define one or more rules to specify traffic
to forward to either the WildFire public cloud or the WildFire appliance
(private cloud) for analysis. 

 Enter a descriptive Name for
any rules you add to the profile (up to 31 characters). 

 Add an Application so that any application
traffic will be matched to the rule and forwarded to the specified
analysis destination. 

 Select a File Type to be analyzed
at the defined analysis destination for the rule. 

 A
WildFire private cloud (hosted by a WildFire appliance) does not
support analysis of APK, Mac OS X, archive, and linux files. 

 Apply the rule to traffic depending on the transmission Direction .
You can apply the rule to upload traffic, download traffic, or both. 

 Select the destination for traffic to be forwarded for Analysis : 

 In
a hybrid cloud deployment, files that match to both private-cloud
and public-cloud rules are forwarded only to the private cloud as
a cautionary measure. 

 Select public-cloud so
that all traffic matched to the rule is forwarded to the WildFire
public cloud for analysis. 

 Select private-cloud so that all traffic matched to the rule
is forwarded to the WildFire appliance for analysis. 

 Inline Cloud Analysis 

 Enable Inline Cloud Analysis 

 Select this option to enable Advanced WildFire Inline Cloud
 Analysis. 

 Rules 

 Define one or more rules to specify traffic to forward to Advanced
 WildFire Inline Cloud Analysis. 

 Enter a descriptive Name for any rules
 you add to the profile (up to 31 characters). 

 Add an Application so that any
 application traffic will be matched to the rule and
 forwarded to the specified analysis destination. 

 Select a File Type to be analyzed at
 the defined analysis destination for the rule. 

 Apply the rule to traffic depending on the transmission
 Direction . You can apply the rule
 to download traffic. 

 When downloading multiple files simultaneously from some
 online services, the files are archived in a format that
 is not currently supported by PAN-OS. These files are
 not unarchived and analyzed. 

 Specify an Action to take when
 Advanced WildFire Inline Cloud Analysis detects malware. 

 Previous 

 Objects > Security Profiles > File Blocking 

 Next 

 Objects > Security Profiles > Data Filtering 

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

 12.1 

 Help 

 Web Interface 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
