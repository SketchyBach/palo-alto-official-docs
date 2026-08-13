---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/integrate-prisma-access-with-on-premises-globalprotect-gateways-panorama/setting-priority-for-prisma-access-and-on-premises-gateways
fetched_at: 2026-08-13T17:25:07Z
source: palo-alto-main
---

# Setting Priority for Prisma Access and On-Premises Gateways Clear

Setting Priority for Prisma Access and On-Premises Gateways 

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

 Setting Priority for Prisma Access and On-Premises Gateways 

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

 Prisma Access Mobile Users 

 Mobile Users: GlobalProtect 

 Integrate Prisma Access with On-Premises GlobalProtect Gateways 

 Setting Priority for Prisma Access and On-Premises Gateways 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Setting Priority for Prisma Access and On-Premises Gateways 

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

 Integrate Prisma Access with On-Premises GlobalProtect Gateways 

 Next 

 Mobile Users: Explicit Proxy 

 Setting Priority for Prisma Access and On-Premises Gateways 

 Learn how to set priorities in a Prisma Access (Managed by Panorama)
 deployment. 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 You
can select an on-premises gateway that is physically closest to
your mobile users and allow users to connect to a different gateway
(either on-premises or cloud) to ensure secure access for mobile
users if they change locations. You can also specify priority for
gateways that are in the same country or same linguistic area as
your mobile users. 

 If you
require users to connect to a specific Prisma Access gateway, you
can allow mobile users to manually select specific Prisma Access 
gateways. Mobile users choose one of the Prisma Access gateways
using the GlobalProtect app that is installed on their endpoint. 

 Complete
the following workflow to configure gateway priorities in Prisma
Access. 

 Set Equal Gateway Priorities for On-Premises and Prisma Access Gateways 

 Set a Higher Gateway Priority for an On-Premises Gateway 

 Set Higher Priorities for Multiple On-Premises Gateways 

 Configure Priorities for Prisma Access and On-Premises Gateways 

 Set Equal Gateway Priorities for On-Premises and Prisma Access 
Gateways 

 To enable secure access for your mobile workforce
no matter where they are located, you can set equal priorities for
the on-premises GlobalProtect gateways and the Prisma Access gateways.
 The GlobalProtect app uses Gateway Priority in a Multiple
Gateway Configuration to determine the preferred gateway. 

 You
can use this configuration if your mobile users are most often closer
to an on-premises gateway. When users change locations, the GlobalProtect
app chooses another gateway (either on-premises or Prisma Access 
gateway) based on the highest priority and lowest response time. 

 The
following figure shows a sample configuration with two mobile users
in North America. You set the gateway priority to Highest for
both the Prisma Access gateways and the on-premises gateways. 

 In
this example, User 1’s GlobalProtect app determines that the Prisma
Access gateway has a lower response time than the on-premises gateway,
and user 2’s GlobalProtect app determines that the on-premises gateway
has a lower response time. Since all gateways have the same priority,
User 1 connects to the Prisma Access gateway and User 2 connects
to the on-premises gateway, based on the lower response time. 

 Set a Higher Gateway Priority for an On-Premises Gateway 

 In situations where you want to direct mobile
users to use an on-premises gateway instead of the Prisma Access 
gateways, specify the on-premises gateways with a source region
and a higher priority than the Prisma Access gateway. 

 The
following figure shows a sample configuration for mobile users in
Indonesia. To avoid the possibility of mobile users being connected
to the nearest Prisma Access gateway in Singapore, you set the gateway
priority to Highest for the on-premises gateway
in Indonesia and set the priority to Medium for
the Prisma Access gateways. 

 This example also specifies a
source region of Indonesia for the on-premises gateway. We recommend
specifying a source region for the following reasons: 

 Specifying
a source region for an on-premises gateway allows users in a region
to access that gateway and prevents users outside of that region
from connecting to that gateway. In this example, only mobile users
in Indonesia can connect to the on-premises gateway with the source
region of Indonesia, and the higher priority means that the on-premise
gateway has priority over the Prisma Access gateways. 

 If you set a source region of Any for
the on-premises gateway in Indonesia, every mobile user in your
organization would prefer the on-premises gateway in Indonesia,
because of its higher priority and worldwide accessibility. This
configuration means that mobile users might never connect to the
 Prisma Access gateways. 

 Set Higher Priorities for Multiple On-Premises Gateways 

 To ensure that traffic to the internet stays
in language-specific regions, you can configure multiple gateways
in multiple source regions, setting the priority of the on-premise
gateways to Highest and the priority of the
 Prisma Access gateways to Medium . 

 The
following figure shows a sample configuration for mobile users in
Scandinavia. Using this configuration, when the mobile users access
internet websites, the websites use the character encoding set that
is specific to their languages. 

 In this example, you configure
on-premises gateways with source regions in Denmark, Norway, and
Sweden. You set the priority of those gateways to Highest and
set the priority of the Prisma Access gateways to Medium .
Specifying a source region for the on-premises gateways allows users
in those regions to access those gateways, and prevents users outside
of those regions from connecting to those gateways. 

 In this
example, the GlobalProtect app for mobile users in Sweden selects
the on-premises gateway in Sweden because of the source region and
higher gateway priority. 

 Configure Priorities for Prisma Access and On-Premises Gateways 

 Use this workflow to configure priorities for a deployment that uses on-premises
 gateways with Prisma Access . 

 Log in to Prisma Access . 

 Select Network GlobalProtect Portals in the Mobile_User_Template 
 template. 

 Click the portal name in the Name field. 

 Click the Agent tab. 

 Click the name of the agent to configure. 

 The default agent is named DEFAULT . 

 Click the External tab. 

 Set the priority of the Prisma Access gateways. 

 Click GP cloud service or Prisma
 Access . 
 The name is dependent on when your gateway was set up;
 GP cloud service is the deprecated name.

 Set the priority for your preferred configuration. 

 To Set Equal
 Gateway Priorities for On-Premises and , change the priority from
 None to
 Highest . 

 To Set a Higher
 Gateway Priority for an On-Premises Gateway 
 or Set Higher
 Priorities for Multiple On-Premises Gateways ,
 change the priority from None to
 Medium . 

 Be sure that the Manual check box is
 selected. 

 Checking the Manual check box ensures that
 mobile users can select a specific Prisma Access gateway if it
 is required. 

 Do not add a source region for the Prisma Access gateways;
 any region you specify is not applied to the
 configuration. 

 Click OK . 

 Add one or more on-premises
 external gateways to your configuration. 

 Enter a descriptive Name for the
 gateway. 

 The name you enter should match the name you defined when you
 configured the gateway, and it should be descriptive enough for
 users to know the location of the gateway to which they
 connect. 

 Enter the FQDN or IP address of the interface where the gateway is
 configured in the Address field. 

 You can configure an IPv4 address. The address you specify must
 exactly match the Common Name (CN) in the gateway server
 certificate. 

 Add one or more Source Regions for the
 on-premises gateway, or select Any to make
 the gateway available to all regions. 

 If you set the priority of on-premises external gateways
 higher than Prisma Access gateways, we recommend that you
 specify source regions for the external gateways. If you
 specify Any for the region, the
 GlobalProtect app might never select Prisma Access gateways
 over on-premises gateways because of the higher priority for
 the on-premises gateways. 

 Select the Manual check box to allow users
 to manually switch to the gateway. 

 Set the Priority of the on-premises gateway
 to Highest (the default). 

 Click OK . 

 ( Optional ) Set the priority for additional gateways by repeating
 Step 8 . 

 Be sure to specify the correct source regions. 

 The following figure shows a sample configuration with multiple gateways
 that have source regions in Norway, Sweden, and Denmark. Note that the
 Manual check box is selected, which indicates
 that a mobile user can manually select any of these gateways. 

 Previous 

 Integrate Prisma Access with On-Premises GlobalProtect Gateways 

 Next 

 Mobile Users: Explicit Proxy 

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

 GlobalProtect 

 4.0 Preferred 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
