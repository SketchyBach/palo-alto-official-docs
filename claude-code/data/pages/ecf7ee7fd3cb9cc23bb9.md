---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/deploy-prisma-access-agents/deploy-prisma-access-agents-using-jamf-pro/deploy-agents-to-macos-endpoints-using-jamf/create-a-prisma-access-agent-configuration-profile-in-jamf-pro
fetched_at: 2026-08-13T17:22:13Z
source: palo-alto-main
---

# Manually Create Configuration Profiles (V3) for Prisma Access Agent Clear

Manually Create Configuration Profiles (V3) for Prisma Access Agent 

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

 Manually Create Configuration Profiles (V3) for Prisma Access Agent 

 Updated on 

 Wed Jul 29 16:23:07 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Jul 29 16:23:07 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent Administration 

 Deploy the Prisma Access Agent 

 Deploy Prisma Access Agents Using Jamf Pro 

 Deploy Prisma Access Agents to macOS Endpoints Using Jamf Pro 

 Manually Create Configuration Profiles (V3) for Prisma Access Agent 

 Download PDF 

 Prisma Access Agent 

 Manually Create Configuration Profiles (V3) for Prisma Access Agent 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Deploy the Prisma Access Agent Using a Unified Configuration Profile (V2_1) 

 Next 

 Manually Create a Configuration Profile (V2_1) for Prisma Access Agent 

 Manually Create Configuration Profiles (V3) for Prisma Access Agent 

 Learn how to create and deploy a configuration profile that defines how the Prisma Access Agent is configured and run on macOS devices. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 macOS 14 and later desktop devices 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 Create and deploy configuration profiles for Prisma Access Agents that define
 how the Prisma Access Agent is configured on managed macOS devices. For
 example, you can set up the configuration profile to automatically load system
 extensions to provide a seamless experience for users running the Prisma Access Agent to access the internet, SaaS applications, and private
 applications and resources in your organization. 

 ( Recommended ) As an alternative to manually creating a configuration
 profile, use the unified configuration profiles provided by Palo
 Alto Networks . 

 You will need to create two
 configuration profiles: one for Prisma Access Agent , and the other for Endpoint DLP . Both configuration files
 must be installed for Prisma Access Agent . When the agent installer runs, it
 automatically installs Endpoint DLP—the extensions must already be authorized or
 macOS will prompt users to approve them. 

 The Endpoint DLP agent requires a separate license and remains inactive
 until you activate the license. 

 This configuration profiles will automatically load the following extensions on a
 managed endpoint: 
 PAA Network Extension (com.paloaltonetworks.pang.networkextension) 

 PAA Security Extension (com.paloaltonetworks.pang.securityextension) 

 Endpoint DLP enforcer extension (com.paloaltonetworks.pangdlp.enforcer) 

 Endpoint DLP network filter extension
 (com.paloaltonetworks.pangdlp.netfilterdlp) 

 After you deploy the agent, you can run the systemextensionsctl
 list command on an endpoint to verify that the extensions have been
 loaded. For example: 

 If you previously deployed other Palo Alto Networks apps such as GlobalProtect™
 and Cortex® XDR® to your endpoints, when deploying the system extensions via
 mobile device management (MDM) software, the configuration profiles for Prisma Access Agent and the other Palo Alto Networks apps must include the
 Allowed System Extension and Removable
 System Extension settings. If only one of the profiles has the
 removable system extension, the uninstallation of Prisma Access Agent 
 won’t complete. 

 The following procedure is based on the Prisma Access Agent unified
 configuration profiles (V3). 

 Create a Jamf Smart Computer Group to
 target specific managed macOS devices for the installation of the Prisma Access Agent . 

 Create the configuration profile for Prisma Access Agent . 

 In Jamf Pro, select Computers Configuration Profiles New . 

 Configure the General tab as follows. You can
 use any meaningful display name for the profile. 

 Configure the Content Filter . The Prisma Access Agent content filter suppresses the following
 prompts on the endpoints: 

 Configure the content filter settings as shown: 
 Filter Name = A meaningful name such
 as PAA Content Filter 

 Identifier =
 com.paloaltonetworks.pang 

 Password = Enter the password for
 authenticating to the service 

 Filter Order =
 Firewall 

 Socket Filter =
 Enabled 

 Socket Filter Bundle Identifier =
 com.paloaltonetworks.pang.networkextension 

 Socket Filter Designated Requirement 
 =

 identifier "com.paloaltonetworks.pang.networkextension" and anchor apple generic and certificate leaf[subject.OU] = PXPZ95SK77 

 Configure the Notifications tab to set up how
 Prisma Access Agent notifications are displayed on your end
 users' devices. 

 App Name = Prisma Access Agent 

 Bundle ID =
 com.paloaltonetworks.PrismaAccessAgent 

 Notifications =
 Enabled 

 Configure the Privacy Preferences Policy Control 
 tab to specify access settings for Prisma Access Agent . This will
 provide Full Disk Access permissions for Prisma Access Agent 
 processes. 

 Identifier =
 com.paloaltonetworks.pang.securityextension 

 Identifier Type = Bundle
 ID 

 Code Requirement =

 identifier "com.paloaltonetworks.pang.securityextension" and anchor apple generic and certificate leaf[subject.OU] = PXPZ95SK77 

 APP OR SERVICE =
 SystemPolicyAllFiles 

 ACCESS =
 Allow 

 Configure the System Extensions tab to
 automatically load Prisma Access Agent system extensions on the
 end users' devices and suppress notifications such as the
 following: 

 Configure the system extensions as follows: 

 Display name = A meaningful name such as
 PAA Allowed System Extensions 

 System Extension Types =
 Allowed system extensions 

 Team Identifier =
 PXPZ95SK77 

 In Allowed System Extensions = 
 com.paloaltonetworks.pang.networkextension 

 com.paloaltonetworks.pang.securityextension 

 To avoid potential conflict between nonremovable and removable system
 extensions, configure removable system extensions for Prisma Access Agent by adding a second Allowed System Extensions and
 Team IDs section. 

 Display name = A meaningful name such as
 PAA Removable System Extensions 

 System Extension Types =
 Removable system extensions 

 Team Identifier =
 PXPZ95SK77 

 Removable System Extensions = 
 com.paloaltonetworks.pang.networkextension 

 com.paloaltonetworks.pang.securityextension 

 Configure the VPN tab to specify how the device
 connects to your wireless network via the tunnel. 

 Connection Name = Enter the display name
 of the connection 

 VPN Type =
 VPN 

 Connection Type = Custom
 SSL 

 Identifier =
 com.paloaltonetworks.pang . 

 Server = A placeholder IP address such as
 8.8.8.8 

 Provider Bundle Identifier =
 com.paloaltonetworks.pang.networkextension 

 Custom Data : 
 Key =
 ztna-spdo-dyn-uuid 

 Value =
 339E19CD-B2EF-4DB4-8E7F-D6E72BDFA7CB 

 Provider Type =
 App-proxy 

 Exclude Local Networks = Selected 

 Provider Designated Requirement =

 identifier "com.paloaltonetworks.pang.networkextension" and anchor apple generic and certificate leaf[subject.OU] = PXPZ95SK77 

 Enable VPN on Demand = Selected 

 On Demand Rules Configuration XML 
 = 

 <array>
<dict>
<key>Action</key>
<string>Connect</string>
</dict>
</array> 

 Save the Prisma Access Agent configuration
 profile. 

 Set the scope for the Prisma Access Agent configuration profile. 

 Edit the configuration profile. 

 Select Scope and
 Add the Smart Computer Group that you
 created to target the specific managed macOS devices for the
 installation of the Prisma Access Agent configuration
 profile. You can also select specific computers as deployment
 targets. For example: 

 Save the scope of the profile. Jamf will
 target the selected computers and computer groups for the
 distribution of the Prisma Access Agent configuration
 profile. 

 Create the configuration profile with Endpoint DLP settings. 

 You must configure and
 install this profile for Prisma Access Agent . When the installer runs,
 it installs Endpoint DLP automatically—the extensions must already be
 authorized or macOS will prompt users to approve them. 

 In Jamf Pro, select Computers Configuration Profiles New . 

 Configure the General tab as follows. You can
 use any meaningful display name for the profile. 

 Configure the Content Filter tab for Endpoint
 DLP: 

 Filter Name = A meaningful name such as
 PAA DLP Content Filter 

 Identifier =
 com.paloaltonetworks.pangdlp 

 Password = Enter the password for
 authenticating to the service 

 Filter Order =
 Firewall 

 Socket Filter =
 Enabled 

 Socket Filter Bundle Identifier =
 com.paloaltonetworks.pangdlp.netfilterdlp 

 Socket Filter Designated Requirement =

 identifier "com.paloaltonetworks.pangdlp.netfilterdlp" and anchor apple generic and certificate leaf[subject.OU] = PXPZ95SK77 

 Configure the Privacy Preferences Policy Control 
 tab for Endpoint DLP: 

 Configure the App Access section for the
 com.paloaltonetworks.pangdlp.enforcer extension. 

 Identifier =
 com.paloaltonetworks.pangdlp.enforcer 

 Identifier Type = Bundle
 ID 

 Code Requirement =

 identifier "com.paloaltonetworks.pangdlp.enforcer" and anchor apple generic and certificate leaf[subject.OU] = PXPZ95SK77 

 APP OR SERVICE =
 SystemPolicyAllFiles 

 ACCESS =
 Allow 

 Add a second App Access section for the
 com.paloaltonetworks.pangdlp extension. 

 Identifier =
 com.paloaltonetworks.pangdlp 

 Identifier Type = Bundle
 ID 

 Code Requirement =

 identifier "com.paloaltonetworks.pangdlp" and anchor apple generic and certificate leaf[subject.OU] = PXPZ95SK77 

 APP OR SERVICE =
 SystemPolicyAllFiles 

 ACCESS =
 Allow 

 Configure the System Extensions tab for Endpoint
 DLP. 

 Display name = A meaningful name such as
 PAA DLP Allowable System Extensions 

 System Extension Types =
 Allowed system extensions 

 Team Identifier =
 PXPZ95SK77 

 In Allowed System Extensions = 
 com.paloaltonetworks.pangdlp.enforcer 

 com.paloaltonetworks.pangdlp.netfilterdlp 

 To avoid potential conflict between nonremovable and removable system
 extensions, configure removable system extensions for Endpoint DLP
 by adding a second Allowed System Extensions and Team
 IDs section. 

 Display name = A meaningful name such as
 PAA DLP Removable System Extensions 

 System Extension Types =
 Removable system extensions 

 Team Identifier =
 PXPZ95SK77 

 Removable System Extensions = 
 com.paloaltonetworks.pangdlp.enforcer 

 com.paloaltonetworks.pangdlp.netfilterdlp 

 Save the configuration profile for Endpoint
 DLP. 

 Set the scope for the Endpoint DLP configuration profile. 

 Edit the configuration profile. 

 Select Scope and
 Add the Smart Computer Group that you
 created to target the specific managed macOS devices for the
 installation of the Endpoint DLP configuration profile. You can
 also select specific computers as deployment targets. 

 Save the scope of the profile. Jamf will
 target the selected computers and computer groups for the
 distribution of the Endpoint DLP configuration profile. 

 To verify the status of the configuration profile installation: 

 In Jamf Pro, select Computers Configuration Profiles . 

 Find the configuration profile that you set up and select
 View . 

 Select the log that you want to view: 

 After the profiles have been deployed, verify the status of the profile
 installation on a macOS endpoint: 

 In System Settings, search for Profiles and
 select Device Management . 

 Double-click the Prisma Access Agent and Endpoint DLP profiles
 that you deployed. 

 Review the profile settings to ensure that the correct settings have
 been deployed. For example: 

 For Prisma Access Agent : 

 For Endpoint DLP: 

 Click OK when you have finished reviewing the
 profile. 

 Previous 

 Deploy the Prisma Access Agent Using a Unified Configuration Profile (V2_1) 

 Next 

 Manually Create a Configuration Profile (V2_1) for Prisma Access Agent 

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

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Prisma Access Agent 

 Next-Generation Firewall 

 Administration 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
