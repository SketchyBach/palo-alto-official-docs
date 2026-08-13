---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-user-based-policy/retrieve-user-id-information/retrieve-group-mapping-using-the-cloud-identity-engine
fetched_at: 2026-08-13T17:25:27Z
source: palo-alto-main
---

# Cloud Identity Engine Clear

Cloud Identity Engine 

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

 Cloud Identity Engine 

 Updated on 

 Aug 10, 2026 

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

 Aug 10, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access User-Based Policy 

 Retrieve User-ID Group Mappings for Prisma Access 

 Cloud Identity Engine 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Cloud Identity Engine 

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

 Cloud Identity Engine 

 In addition to using the Cloud Identity Engine to retrieve user and group information , you can
 use the Cloud Identity Engine to populate user group names in security policy rules.
 This integration eliminates the need to configure an on-premises or VM-series
 next-generation firewall as a Master Device for this purpose; however,
 Master Devices are still supported. 

 You
can also use Cloud Identity Engine to populate group names in Panorama
Managed multi-tenant deployments ,
which is not possible when using a Master Device. 

 To enable
the Cloud Identity Engine to populate group names in security policy
rules, complete the following steps. 

 In the Cloud Identity Engine, activate the Cloud Identity Engine
and add an on-premises or cloud-based directory,
if you have not already done so. 

 Configure the Cloud Identity Engine as a mapping source. 

 From the Panorama that manages Prisma Access ,
select Panorama User
Identification Cloud Identity Engine and Add a
profile. 

 For the Instance , specify the
following parameters: 

 Region —Select the regional
endpoint for your tenant. 

 The region you select must
match the region you select when you activated your Cloud Identity
Engine tenant. 

 Cloud Identity Engine Instance —Select
the Cloud Identity Engine instance to associate with the profile. 

 Domain —Select the domain that contains
the directories you want to use. 

 Update Interval (min) —Enter the number
of minutes that you want Panorama to wait between updates from the
Cloud Identity Engine app to Panorama (also known as a refresh interval).
The default is 60 minutes and the range is 5—1440. 

 Verify that the profile is Enabled . 

 For the User Attributes , select
the format for the Primary Username . You
can optionally select the formats for the E-Mail and an Alternate
Username. You can configure up to three alternate username formats
if your users log in using multiple username formats. 

 When you view users in security policy rules, the username
displays in the primary username format you select here. 

 For the Group Attributes , select
the format for the Group Name . 

 Leave the Device Attributes as None . 

 Click OK then Commit
and Push your changes. 

 Attach your profile to your Prisma Access configuration. 

 Go to the Settings for the deployment you
are adding. 

 For a Mobile Users—GlobalProtect deployment, select Panorama Cloud Services Configuration Mobile Users—GlobalProtect and
click the gear to edit the Settings . 

 For a Mobile Users—Explicit Proxy deployment, select Panorama Cloud Services Configuration Mobile Users—Explicit
Proxy and click the gear to edit the Settings . 

 For a Mobile Users—Remote Networks deployment, select Panorama Cloud Services Configuration Mobile Users—Remote
Networks and click the gear to edit the Settings . 

 Select Cloud Identity Engine . 

 Select the Cloud Identity Engine profile you created. 

 Select Commit Commit
to Panorama and Commit your
changes. 

 Verify that Prisma Access has the mapping information
from the Cloud Identity Engine. 

 Select Panorama Device Groups <template-name> ,
where <template-name> is the template for
the deployment you are configuring, and verify that the Cloud Identity
Engine profile is attached to the device group. 

 The following example shows that the device group is successfully
attached to the Explicit_Proxy_Device_Group. 

 Select Objects Security Pre Rules , Add a
security policy rule, and verify that the groups are populated in
the user area. 

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
