---
url: https://docs.paloaltonetworks.com/prisma-access-agent/user-guide/configure-global-app-settings-for-the-agent
fetched_at: 2026-08-13T17:22:38Z
source: palo-alto-main
---

# Configure General Global Settings for the Prisma Access Agent Clear

Configure General Global Settings for the Prisma Access Agent 

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

 Configure General Global Settings for the Prisma Access Agent 

 Updated on 

 Wed Jul 01 22:45:41 PDT 2026 

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

 Wed Jul 01 22:45:41 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent User Guide 

 Configure General Global Settings for the Prisma Access Agent 

 Download PDF 

 Prisma Access Agent 

 Configure General Global Settings for the Prisma Access Agent 

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

 Configure General Global Settings for the Prisma Access Agent 

 Configure general global agent settings for Prisma Access Agent , such as
 configuring the anti-tamper protection settings, authentication override settings, and
 inactivity timeout settings. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 You can customize global agent settings that apply to Prisma Access Agents across all
 endpoints. 

 Navigate to the Prisma Access Agent setup. 

 From Strata Cloud Manager : 
 Log in to Strata Cloud Manager 
 as the administrator. 

 Select Configuration NGFW and Prisma Access Configuration Scope Access Agent Setup Prisma Access Agent . 

 From Panorama : 
 From the Cloud Services plugin in Panorama, select Panorama Cloud Services Prisma Access Agent Launch Prisma Access Agent . 

 Select Configuration Prisma Access Agent Settings Prisma Access Agent . 

 Edit the Global Agent Settings . 

 ( Strata Cloud Manager only) Select
 General . 

 Configure Authentication Override settings to allow
 Prisma Access to generate and accept secure, encrypted cookies for user
 authentication. Authentication override allows the user to provide login
 credentials only once during the specified Cookie
 Lifetime . 

 Generate cookie for authentication
 override —Enables Prisma Access to generate encrypted
 endpoint-specific cookies and issue authentication cookies to the
 endpoint. (Default: Enabled) 

 Accept cookie for authentication override —Enables
 Prisma Access to authenticate users with a valid, encrypted cookie. When
 the app presents a valid cookie, Prisma Access verifies that the cookie
 was encrypted by Prisma Access originally, decrypts the cookie, and then
 authenticates the user. (Default:
 Enabled) 

 Certificate to Encrypt/Decrypt Cookie —Select a
 certificate to use to encrypt and decrypt the cookie. For NGFW
 deployments, this certificate is the same one that you imported in the
 Infrastructure 
 settings. 

 ( Panorama Managed
Prisma Access 
 and Panorama Managed NGFW deployments ) If you updated the
 Certificate to Encrypt/Decrypt Cookie 
 field in Panorama and pushed the configuration, you must select the
 same certificate in the Certificate to Encrypt/Decrypt
 Cookie in Strata Cloud Manager and perform a push
 config. Otherwise, the Prisma Access Agent will not be able to
 establish a tunnel to the gateway. 
 For example, in Panorama, you
 selected Authentication Cookie
 Cert : 

 In Strata Cloud Manager , you need to select the same
 certificate: 

 Cookie Lifetime —Specifies the hours, days, or
 weeks for which the cookie is valid (default is 24 hours). The range for
 hours is 1-72; the range for weeks is 1-52; and the range for days is
 1-365. After the cookie expires, the user must reenter their login
 credentials. Prisma Access then encrypts a new cookie to send to the
 agent. This value can be the same as or different from the cookie
 lifetime that you configure. 

 Configure authentication
 timers that enable you to control when and how frequently users must
 re-authenticate when accessing resources through the agent. 

 Re-authentication Frequency —Define the frequency
 that determines how often users must provide their credentials. This
 frequency applies globally across your deployment and directly controls
 the user refresh token lifetime. You can enter a value 10 hours and 30
 days. (Default: 7 days) 

 Notify Before Re-authentication —Specify a
 notification timer that alert users before their authentication expires.
 You specify how many minutes in advance users receive warnings, with a
 range of 5 to 120 minutes. (Default: 60 minutes) 

 Re-authentication Notification Message —Customize
 the notification message that displays to users. If you leave the
 re-authentication notification message empty, the agent displays a
 default message. You can enter custom text with a maximum of 127
 characters. 

 If Endpoint Insights 
 is enabled in the Agent Settings , configure the diagnostic
 Data Retention period. 

 Prisma Access Agent collects the diagnostic data, stores it securely on the
 endpoint, and retains it for the number of days specified by the data
 retention period. Prisma Access Agent automatically purges any diagnostic
 data that exceeds the data retention period. 

 The default is 45 days. The range is 7 to 730 days (2 years). 

 ( Strata Cloud Manager ) ( Not supported on Prisma Access Agent
 Linux ) Block Login for Quarantined
 Devices to prevent Prisma Access Agent users from logging in
 from quarantined devices. 

 If a user attempts to log in from a quarantined device when this setting is
 enabled, the Prisma Access Agent notifies the user that the device is
 quarantined and the user cannot log in from that device. If this setting is
 not enabled, the user receives the notification but is able to log in from
 that device. 

 The Block Login for Quarantined
 Devices setting applies to both Prisma Access Agent and
 GlobalProtect. Any changes you make will be reflected and used for
 GlobalProtect, and vice versa. 

 Save your settings. 

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
