---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/troubleshoot-prisma-access-agents/resolve-problems-by-running-commands-in-a-remote-shell
fetched_at: 2026-08-13T17:22:29Z
source: palo-alto-main
---

# Resolve Prisma Access Agent Problems by Running Commands in a Remote
        Shell Clear

Resolve Prisma Access Agent Problems by Running Commands in a Remote
 Shell 

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

 Resolve Prisma Access Agent Problems by Running Commands in a Remote
 Shell 

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

 Troubleshoot Prisma Access Agents 

 Resolve Prisma Access Agent Problems by Running Commands in a Remote
 Shell 

 Download PDF 

 Prisma Access Agent 

 Resolve Prisma Access Agent Problems by Running Commands in a Remote
 Shell 

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

 Logs Collected by Prisma Access Agent 

 Next 

 Prisma Access Agent Commands (PACli) 

 Resolve Prisma Access Agent Problems by Running Commands in a Remote
 Shell 

 Learn how to troubleshoot Prisma Access Agent problems by running commands in a
 remote shell. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 macOS 14 and later or Windows 10 version 2024 and later
 desktop devices 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 To investigate and resolve Prisma Access Agent issues effectively on desktop
 agents, such as an end user's inability to access corporate resources, you’ll likely
 need to physically access the end user's device to collect relevant data, diagnose
 the issue, and fix the issue. However, in today's remote-first work environment,
 it’s becoming more difficult to gain physical access to an end user's device for
 troubleshooting. 

 Using the Endpoint Management
 page ( Configuration Endpoint Management ), you can: 
 Conveniently access any end user's device that is running the Prisma Access Agent remotely by starting a terminal session (remote
 shell) on the device, provided that you have permission from the end
 user. 

 Initiate a remote shell from the device details page. 
 When the remote
 shell is initiated, the user is prompted to accept the request to allow
 the administrator to open a remote shell. When the user accepts the
 request, a live terminal window appears for you to enter shell commands
 to diagnose an issue. 

 Because any command that you enter and any output in the remote shell session
 will be logged, ensure that you do not enter any input or produce output that
 contains sensitive information. 

 Select Configuration Endpoint Management . 

 ( Optional ) Set the Time Range for which you
 want to view the data. You can select a preset time range or customize the time
 range. 

 In the Devices table, scroll through the list to find
 the device or search for a device . 

 Select the hostname of the device for which you want to open a remote shell.

 In the device details page, click Remote Shell . 

 The
 Remote Shell is not available to administrators
 with the View Only Administrator role . 

 Wait for the end user to confirm the remote access. 

 On the endpoint, the user is prompted to accept the remote shell request. 

 If the user accepts the remote shell request, a live terminal window
 appears. 

 If the user denies the request or does not respond within 2 minutes, you are
 notified that the terminal session cannot be established due to the lack of
 permission.

 Run any shell commands that are needed to diagnose or resolve an issue. 

 For example, you can run Prisma Access Agent Commands (PACli) in the remote
 shell. 

 When you have finished with your remote session,
 Disconnect the remote shell, which terminates the
 session. 

 You can choose to save the remote session activity to a log file by clicking
 Yes . 

 This action exports all the terminal session activity to a log file,
 including any commands that were run and the command output. Any action,
 from the initiation of the shell to the types of commands, is logged in the
 appropriate Prisma Access Agent log or management log, along with the
 timestamp and administrator identity. 

 The log file in .txt format is saved to the download
 location specified by your web browser. 

 Previous 

 Logs Collected by Prisma Access Agent 

 Next 

 Prisma Access Agent Commands (PACli) 

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
