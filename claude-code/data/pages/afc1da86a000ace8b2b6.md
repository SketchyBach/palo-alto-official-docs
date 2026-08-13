---
url: https://docs.paloaltonetworks.com/panorama/administration/configure-administrative-access-to-panorama/configure-administrative-accounts-and-authentication/configure-radius-authentication-for-panorama-administrators
fetched_at: 2026-08-13T17:17:32Z
source: palo-alto-main
---

# Configure RADIUS Authentication for Panorama Administrators Clear

Configure RADIUS Authentication for Panorama Administrators 

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

 Configure RADIUS Authentication for Panorama Administrators 

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

 Configure Administrative Access to Panorama 

 Configure
Administrative Accounts and Authentication 

 Configure RADIUS Authentication for Panorama Administrators 

 Download PDF 

 Panorama 

 Configure RADIUS Authentication for Panorama Administrators 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Configure an Administrator with SSH Key-Based Authentication for the CLI 

 Next 

 Configure TACACS+ Authentication for Panorama Administrators 

 Configure RADIUS Authentication for Panorama Administrators 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Panorama superuser role 

 You can use a RADIUS server to authenticate administrative
access to the Panorama web interface. You can also define Vendor-Specific Attributes (VSAs) on the
RADIUS server to manage administrator authorization. Using VSAs
enables you to quickly change the roles, access domains, and user
groups of administrators through your directory service, which is
often easier than reconfiguring settings on Panorama. 

 You can use a RADIUS server to authenticate administrative
access to the Panorama web interface. You can also define Vendor-Specific Attributes (VSAs) on the
RADIUS server to manage administrator authorization. Using VSAs
enables you to quickly change the roles, access domains, and user
groups of administrators through your directory service, which is
often easier than reconfiguring settings on Panorama. 

 You
can Import the Palo Alto Networks RADIUS dictionary into
RADIUS server to define the authentication attributes needed for
communication between Panorama and the RADIUS server. 

 You
can also use a RADIUS server to implement multi-factor authentication (MFA) for
administrators. 

 Add
a RADIUS server profile. 

 The profile defines how Panorama connects to the RADIUS
server. 

 Select Panorama Server Profiles RADIUS and Add a
profile. 

 Enter a Profile Name to identify
the server profile. 

 Enter a Timeout interval in
seconds after which an authentication request times out (default
is 3; range is 1–20). 

 If you use the server profile to integrate Panorama
with an MFA service, enter an interval that gives administrators
enough time to respond to the authentication challenge. For example,
if the MFA service prompts for a one-time password (OTP), administrators
need time to see the OTP on their endpoint device and then enter
the OTP in the MFA login page. 

 Select the Authentication Protocol (default
is CHAP ) that Panorama uses to authenticate
to the RADIUS server. 

 Select CHAP if
the RADIUS server supports that protocol; it is more secure than PAP . 

 Add each RADIUS server and
enter the following: 

 Name to identify the server 

 RADIUS Server IP address or FQDN 

 Secret / Confirm Secret (a
key to encrypt usernames and passwords) 

 Server Port for authentication requests
(default is 1812) 

 Click OK to save the server
profile. 

 Assign the RADIUS server profile to an authentication
profile. 

 The authentication profile defines authentication settings
that are common to a set of administrators. 

 Select Panorama Authentication Profile and Add a
profile. 

 Enter a Name to identify the
authentication profile. 

 Set the Type to RADIUS . 

 Select the Server Profile you
configured. 

 Select Retrieve user group from RADIUS to
collect user group information from VSAs defined on the RADIUS server. 

 Panorama matches the group information against the groups
you specify in the Allow List of the authentication profile. 

 Select Advanced and, in the
Allow List, Add the administrators that are
allowed to authenticate with this authentication profile. 

 Click OK to save the authentication
profile. 

 Configure Panorama to use the authentication profile
for all administrators. 

 Select Panorama Setup Management and
edit the Authentication Settings. 

 Select the Authentication Profile you
configured and click OK . 

 Configure the roles and access domains that define authorization
settings for administrators. 

 Configure
an Admin Role Profile if the administrator uses a custom
role instead of a predefined (dynamic) role. 

 Configure
an Access Domain if the administrator uses a Device Group
and Template role. 

 Commit your changes. 

 Select Commit Commit
to Panorama and Commit your
changes. 

 Configure the RADIUS server. 

 Refer to your RADIUS server documentation for the specific
instructions to perform these steps: 

 Add the Panorama IP address or hostname
as the RADIUS client. 

 Add the administrator accounts. 

 If the RADIUS server profile specifies CHAP as
the Authentication Protocol , you must define
accounts with reversibly encrypted passwords .
Otherwise, CHAP authentication will fail. 

 Define the vendor code for Panorama (25461) and define
the RADIUS VSAs for the role, access domain,
and user group of each administrator. 

 When you predefine dynamic administrator roles for users,
use lower-case to specify the role (for example, enter superuser ,
not SuperUser ). 

 Verify that the RADIUS server performs authentication
and authorization for administrators. 

 Log in the Panorama web interface using
an administrator account that you added to the RADIUS server. 

 Verify that you can access only the web interface
pages that are allowed for the role you associated with the administrator. 

 In the Monitor , Policies ,
and Objects tabs, verify that you can access
only the device groups that are allowed for the access domain you
associated with the administrator. 

 Previous 

 Configure an Administrator with SSH Key-Based Authentication for the CLI 

 Next 

 Configure TACACS+ Authentication for Panorama Administrators 

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
