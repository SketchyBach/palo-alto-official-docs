---
url: https://docs.paloaltonetworks.com/panorama/administration/manage-wildfire-appliances/configure-basic-wildfire-appliance-settings-on-panorama/configure-authentication-for-a-wildfire-appliance/configure-an-administrative-account-for-a-wildfire-appliance
fetched_at: 2026-08-13T17:17:58Z
source: palo-alto-main
---

# Configure An Administrative Account for a WildFire Appliance Clear

Configure An Administrative Account for a WildFire Appliance 

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

 Configure An Administrative Account for a WildFire Appliance 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Home 

 Panorama 

 Manage WildFire Appliances 

 Configure Basic WildFire Appliance Settings on Panorama 

 Configure Authentication for a WildFire Appliance 

 Configure An Administrative Account for a WildFire Appliance 

 Download PDF 

 Panorama 

 Configure An Administrative Account for a WildFire Appliance 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Configure An Administrative Account for a WildFire Appliance 

 Create and configure admin user with granular authentication
parameters for the WildFire appliance. 

 Create one or more administrators with granular
authentication parameters for your WildFire appliance to manage
from the Panorama™ management server. Additionally, you can configure
local administrators from Panorama that can be configured directly
on the CLI of the WildFire appliance. However, pushing new configuration changes
to the WildFire appliance will overwrites local administrators with
the administrators configured for the WildFire appliance. 

 Log in to the Panorama web
 interface . 

 Add Standalone WildFire Appliances to Manage with Panorama . 

 ( Optional ) Configure an authentication profile to
define the authentication service that validates the login credentials
of the administrators who access the WildFire appliance CLI. 

 Configure one or more
administrator accounts as needed. 

 The administrator accounts created on Panorama are later
imported to the WildFire appliance and managed from Panorama. 

 You
must configure the administrative account with Superuser admin role privileges
to successfully configure authentication for the WildFire appliance. 

 Configure the authentication for the WildFire appliance. 

 Select Panorama Managed WildFire Appliance and
select the WildFire appliance you previously added. 

 ( Optional ) Select the Authentication
Profile you configured in the previous step. 

 Configure the authentication Timeout Configuration for
the WildFire appliance. 

 Enter the number of Failed Attempt s
before a user is locked out of the WildFire appliance CLI. 

 Enter the Lockout Time , in minutes,
for which the WildFire appliance locks out a user account after
that user reaches the configured number of Failed Attempts . 

 Enter the Idle Timeout , in minutes,
before the user account is automatically logged out due to inactivity. 

 Enter the Max Session Count to set
how many user accounts can simultaneously access the WildFire appliance. 

 Enter the Max Session Time the administrator
can be logged in before being automatically logged out. 

 Add the WildFire appliance administrators. 

 Administrators may either be added as a local administrator
or as an imported Panorama administrator—but not both. Adding the
same administrator as both a local administrator and as an imported
Panorama administrator is not supported and causes the Panorama
commit to fail. For example, the commit to Panorama fails if you
add admin1 as both a local and Panorama administrator. 

 Add and configure new administrators
unique to the WildFire appliancer. These administrators are specific
to the WildFire appliance for which they are created and you manage
these administrators from this table. 

 Add any administrators configured on
Panorama. These administrators are created on Panorama and imported
to the WildFire appliance. 

 Click OK to save the WildFire
appliance authentication configuration. 

 Commit and then Commit
and Push your configuration changes. 

 Access the WildFire appliance
CLI to verify you can successfully access the WildFire appliance
using the local admin user. 

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

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Administration 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
