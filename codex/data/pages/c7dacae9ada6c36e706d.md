---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/manage-prisma-access-agents/view-details-about-devices
fetched_at: 2026-08-13T17:22:24Z
source: palo-alto-main
---

# View Detailed Information About a Device Clear

View Detailed Information About a Device 

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

 View Detailed Information About a Device 

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

 Manage Prisma Access Agents 

 View Detailed Information About a Device 

 Download PDF 

 Prisma Access Agent 

 View Detailed Information About a Device 

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

 Search for Devices 

 Next 

 Endpoint Insights for Prisma Access Agent 

 View Detailed Information About a Device 

 Learn how to see detailed information about a device on which the Prisma Access Agent is installed. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 While the Devices table shows you at a glance the overall status of the deployed Prisma Access Agents , you can select an individual device to view detailed
 information about the device and how the Prisma Access Agent is performing on
 the device. 

 Select Configuration Endpoint Management . 

 ( Optional ) Set the Time Range for which you
 want to view the data. You can select a preset time range or customize the time
 range. 

 In the Devices table, scroll through the list to find
 the device or search for a device . 

 Select the hostname of the device for which you want to get detailed
 information. Be sure to select the hostname itself and not the check box. 

 In the window that slides open, review the information about the selected
 device: 

 You can view the following information: 

 Field Description 

 Experience Score (<Time
 Range>) 

 ( macOS and Windows agents only ) Shows a weighted average of application performance
 metrics for the selected endpoint across all monitored
 apps if Autonomous DEM (ADEM) has been enabled. The
 experience
 score gives an indication of how the Prisma Access Agent is performing on the end
 user's device. 

 You can select MOBILE USER
 EXPERIENCE to view application
 experience details about the associated user ID. 

 If ADEM has not been set up, select Here is how
 to set up for more information. 

 Device Information 

 Host Name The hostname of the endpoint 

 Private IP The IP address assigned to the endpoint by the gateway 

 Public IP The IP address assigned to the endpoint by the
 ISP 

 OS Version The version of the operating system on the
 endpoint 

 Host ID The physical address (or MAC address) of the main network
 adapter on the endpoint 

 Platform The operating system that’s running on the
 endpoint 

 User Information 

 User Id The user ID associated with the Prisma Access Agent . 

 Last Seen The last time a keep-alive was sent to Prisma Access . 

 Agent Information 

 Agent Status The status of
 the Prisma Access Agent running on the
 endpoint 

 Agent Version The version of the Prisma Access Agent that’s
 running on the endpoint 

 Ring ( macOS and Windows agents only ) The upgrade ring that the agent belongs to 

 Previous Agent Version The previous version of the Prisma Access Agent 
 that was installed on the endpoint 

 ADEM Information ( macOS and Windows agents only ) 

 Agent Status If installed, the status of the Access Experience app
 that is running on the endpoint 

 Agent Version If installed, the version of the Access Experience app
 hat is installed on the endpoint 

 Endpoint DLP Information ( macOS and Windows agents only ) 

 DLP Status If enabled, the status of Endpoint DLP that
 is running on the endpoint 

 DLP Version If enabled, the version of Endpoint DLP that
 is running on the endpoint 

 Anti-Tamper ( macOS and Windows agents only ) 

 Privileged Access
 Protection Shows the status (Enabled or Disabled) of the privileged
 access protection (or anti-tamper protection) ,
 for the device. 

 Disable Agent with OTP Shows the status (Allow or Disallow) of the disable agent
 with one-time password (OTP) function. 

 One-Time Passwords (OTPs) ( macOS and Windows agents only ) 

 Privileged Access OTP 

 Contains the Privileged Access OTP when
 Privileged Access Protection 
 is enabled. If Privileged Access
 Protection is disabled, no Privileged
 Access OTP appears. 

 The OTP is masked. Click the eye icon to show the OTP.
 Click the clipboard icon to copy the OTP to the
 clipboard. 

 Disable OTP 

 Contains the Disable Agent OTP if Disable
 Agent with OTP is set to
 Allow . When
 Disable Agent with OTP 
 disabled, no Disable Agent OTP appears. 

 The OTP is masked. Click the eye icon to show the OTP.
 Click the clipboard icon to copy the OTP to the
 clipboard. 

 Uninstall OTP 

 Contains the Uninstall OTP when Privileged
 Access Protection is enabled. If
 Privileged Access Protection 
 is disabled, no Uninstall OTP appears. 

 The OTP is masked. Click the eye icon to show the OTP.
 Click the clipboard icon to copy the OTP to the
 clipboard. 

 ( Optional ) You can take the following Actions 
 on this agent for troubleshooting purposes: 

 Run a remote shell 
 (macOS and Windows agents only) 

 Upgrade the
 agent 
 (macOS and Windows agents only) 

 Downgrade the
 agent 
 (macOS and Windows agents only) 

 Download the latest HIP reports 

 Generate Prisma Access Agent
 logs 

 These actions are not visible to administrators with the View Only
 Administrator role . 

 Previous 

 Search for Devices 

 Next 

 Endpoint Insights for Prisma Access Agent 

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
