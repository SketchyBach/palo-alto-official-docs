---
url: https://docs.paloaltonetworks.com/prisma-access-agent/user-guide/prisma-access-agent-for-desktop-devices/log-in-to-the-agent
fetched_at: 2026-08-13T17:22:50Z
source: palo-alto-main
---

# Log in to the Prisma Access Agent Clear

Log in to the Prisma Access Agent 

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

 Log in to the Prisma Access Agent 

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

 Prisma Access Agent for Desktop Devices 

 Log in to the Prisma Access Agent 

 Download PDF 

 Prisma Access Agent 

 Log in to the Prisma Access Agent 

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

 Use Single Sign-On with Prisma Access Agent 

 Next 

 Change Prisma Access Agent App Settings 

 Log in to the Prisma Access Agent 

 To securely access applications and resources in your organization's
 network, you must log in to the Prisma Access Agent . 

 Where Can I Use This? What Do I Need? 

 Prisma Access Agent 

 Minimum Prisma Access Agent version: 

 25.1 (macOS and Windows) 

 25.7 (Linux) 

 macOS, Windows, or Linux
 desktop devices 

 Check the prerequisites for the
 supported OS versions 

 Internet access 

 To access your organization's network, resources, SaaS applications,
 or the internet, log in to the Prisma Access Agent using your login credentials. 

 After you log in to the Prisma Access Agent , you’re automatically
 connected to your network using the best location (sometimes called a gateway). The
 agent automatically selects the best location to provide you with the best
 performance to provide a better experience, such as viewing websites in your local
 language. When your device is outside your organization's network, the agent finds
 the best location to give you the best performance when connecting to the network. 

 Before you begin, the Prisma Access Agent must be installed on your
 device. Typically, your administrator will deploy the Prisma Access Agent to the
 device that you use to access your organization's network, resources, and
 applications. Your administrator configures the agent according to your
 organization's policy rules and deploys it to your device.
 However,
 if your administrator did not deploy the Prisma Access Agent to your device, you
 will need to manually install the Prisma Access Agent . 

 Depending on how Prisma Access is set up in your organization, your
 administrator should provide you with the name of the server that manages your
 Prisma Access Agent . 

 If your administrator configured
 the macOS or Windows Prisma Access Agent to use single sign-on (SSO), refer to Use Single Sign-On with Prisma Access Agent . 

 The app icons and app interface can appear in dark mode or light mode depending
 on your operating system settings. 

 Log in to the Prisma Access Agent by completing the
 following steps: 

 If your administrator configured the Prisma Access Agent in Always On mode, the
 Prisma Access Agent starts automatically after the installation and whenever you
 log in to your device. 

 If your administrator configured the Prisma Access Agent in On-Demand mode, you need to start the Prisma Access Agent by
 clicking the Prisma Access Agent icon 

 from the macOS menu bar, Windows
 taskbar, or Linux panel. 

 Select the Server Name of the Prisma Access server that
 your administrator provided and click Connect . 

 The format of the server name is
 <xxx>.epm.gpcloudservice.com (without the
 https:// protocol). The maximum length of the
 server name is 256 characters. 

 ( Not supported on
 Prisma Access Agent Linux ) ( Prisma Access Agent 25.3.0.43 ) If your organization uses LDAP
 authentication, enter your login credentials for your organization: 

 In the Login field, enter the username or email
 address you use for LDAP authentication. 

 Type the Password and press
 Enter . 

 On the macOS agent, click Login after entering
 the password to begin the authentication. 

 On the Windows agent, after typing in the password and pressing
 Enter , the authentication begins. 

 In the login page that appears in your default web browser, sign in to your
 organization's single sign-on (SSO) app, such as Okta or Azure Active
 Directory (AD), by entering your login credentials for your
 organization. 

 ( Prisma Access Agent 25.3.0.43 ) Depending on your agent's configuration, the
 login page can appear in your default system web browser (such as Chrome
 or Firefox) or in the Prisma Access Agent internal browser. 
 (The internal embedded browser is not
 supported on Prisma Access Agent Linux.) 

 If your administrator enabled multi-factor authentication (MFA), you’ll need
 to complete additional verification in the browser when you log in. 

 When the browser prompts you, click Open Prisma Access Agent . ( Prisma Access Agent 25.3.0.43 ) If the Prisma Access Agent is
 using the default system web browser, click Open Prisma Access Agent when prompted. 

 ( Optional ) If you don’t want the browser to prompt you the next time
 you log in, select Always allow <site> to open these types of
 links in the associated app , then click Open
 Prisma Access Agent (if supported by your default web
 browser). 

 ( Not supported on
 Prisma Access Agent Linux ) ( Prisma Access Agent 25.3.0.43 ) If you're connecting from
 networks with captive portals, such as hotels, cafes, and airports, the captive
 portal login page will appear in the browser. Enter your credentials or accept
 the terms of service as required by the network provider. 

 Wait while Prisma Access Agent connects to Prisma Access. 

 After successfully logging in, you’re connected automatically to the best
 available location. 

 You can now access your organization's resources and SaaS apps, along with
 secure access to the internet. 

 If your administrator enabled Always On mode for
 the Prisma Access Agent , you can’t disconnect from Prisma Access due to
 your organization's policy. However, you can still change locations. 

 If your administrator enabled On Demand mode for
 the Prisma Access Agent , you must click the lock icon to connect to
 Prisma Access. 

 If you're using the Prisma Browser to securely access
 your organization's network and resources and to browse the internet, the
 Prisma Browser might prompt you to open the Prisma Access Agent 
 again. This can happen if you leave the Prisma Access Agent authentication
 tab open in the Prisma Browser and then restart the browser and restore
 all open tabs. This action refreshes the Open Prisma Access Agent browser
 tab even though your login credentials are still valid and active. Clicking
 Open won’t affect the state of the agent and you
 won't have to authenticate to the agent again. 

 Previous 

 Use Single Sign-On with Prisma Access Agent 

 Next 

 Change Prisma Access Agent App Settings 

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

 User Guide 

 Prisma Access Agent 

 Next-Generation Firewall 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
