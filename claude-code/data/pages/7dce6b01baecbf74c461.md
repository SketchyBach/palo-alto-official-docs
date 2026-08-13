---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/prisma-access-agent-administration-overview/agent-lifecycle-management
fetched_at: 2026-08-13T17:22:24Z
source: palo-alto-main
---

# Prisma Access Agent Lifecycle Management Clear

Prisma Access Agent Lifecycle Management 

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

 Prisma Access Agent Lifecycle Management 

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

 Prisma Access Agent Administration Overview 

 Prisma Access Agent Lifecycle Management 

 Download PDF 

 Prisma Access Agent 

 Prisma Access Agent Lifecycle Management 

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

 Prisma Access Agent Administration Overview 

 Next 

 Automatic Tunnel Restoration in Prisma Access Agents 

 Prisma Access Agent Lifecycle Management 

 After you deploy Prisma Access Agents to mobile user endpoints in your
 organization, you can use Strata Cloud Manager to manage the lifecycle of the
 agents. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 To simplify the day-to-day management of the fleet of Prisma Access Agents that
 have been deployed to mobile users, Prisma Access Agent provides a single point of
 control to help you maintain the agents in your fleet, troubleshoot agent connectivity
 issues, and gain visibility into the agents as a part of the troubleshooting
 process. 

 Installation and Configuration of Prisma Access Agents 

 To help you easily install Prisma Access Agents on mobile user endpoints
 without user intervention, you can onboard your users to configure the cloud infrastructure and agent settings that will be pushed to Prisma Access or NGFW. Then, you can download the Prisma Access Agent package from the Prisma Access Agent Endpoint Management
 page ( Configuration Endpoint Management ) for deployment to endpoints using third-party mobile device management
 (MDM) software such as Jamf Pro and Microsoft
 Intune.. 

 If you configured the agent to run in Always On mode, the
 agents are automatically launched when your users sign on to their devices, and will
 automatically connect to Prisma Access whenever they access their mobile
 devices. If you configured the agent to run in On Demand 
 mode, the user needs to launch the Prisma Access Agent and manually connect to
 Prisma Access . 

 Maintenance of Prisma Access Agents 

 ( macOS and Windows agents only ) To facilitate the upgrade of the deployed Prisma Access Agents , a
 maintenance routine called a staged rollout is used to easily upgrade
 the Prisma Access Agents on your end users' devices. Using staged rollouts , you can plan the upgrade of the Prisma Access Agent by staggering the upgrade based on user group and device
 operating system with minimal interruption to your end users. 

 You can set up upgrade rings with user or user group
 and OS attributes. Endpoints that match the criteria will be upgraded, while
 endpoints that are configured in another upgrade ring will wait for the successful
 completion of the first ring before beginning its upgrade. You can configure up to
 five upgrade rings. Any devices that are not part of the configured rings are placed
 in a default ring that will be upgraded after rings 0 to 4 have completed.

 When an upgrade is available, you’re notified of the upcoming rollout in the Endpoint Management
 page , and users or devices are upgraded in the order of the upgrade rings. 

 Selectively Upgrade or Downgrade Prisma Access Agents 

 ( macOS and Windows agents only ) To keep your managed devices secure, the Prisma Access Agent software is
 upgraded automatically on your endpoints during staged upgrade rollouts. If an
 endpoint was not reachable during a ring upgrade, an attempt will be made to upgrade
 the device during the next agent check-in. 

 If, for whatever reason, an endpoint still cannot be upgraded during a ring upgrade
 cycle, you can manually upgrade an agent in Endpoint Management
 page . You can also downgrade an agent to the previous version to help isolate any
 problems with the current version of the agent. 

 During an agent upgrade or downgrade, logs are created on the endpoints that include
 the following information: 

 The entities that triggered the upgrade, such as the administrator ID 

 Endpoint details such as the operating system version and the existing agent
 version 

 The user for whom the upgrade was attempted 

 Troubleshooting and Remediation 

 The Prisma Access Agent provides information that allows administrators to
 analyze, troubleshoot, and remediate agent problems remotely without requiring an
 active tunnel to Prisma Access or NGFW. 

 The Prisma Access Agent communicates with Prisma Access or NGFW in the
 following manner: 

 Receives commands from Prisma Access or NGFW to perform specific operations
 without requiring a tunnel or an active connection to Prisma Access or
 NGFW 

 Provides status on tasks that were performed, and sufficient information for
 administrators to determine whether the tasks were successfully performed 

 Receives commands from for performing routine operations, such as resetting user
 or machine credentials, reissuing user or machine credentials, reinstalling,
 upgrading, or downgrading the agent 

 Restarts the tunnel or data connection to Prisma Access or NGFW 

 Collects and sends data about the endpoint and agent for troubleshooting and
 remediation 

 The Prisma Access Agent provides audit trails in the form of logs regarding the
 status of all operations that it attempts, including successful and unsuccessful
 attempts, such as: 

 Attempts to authenticate to various components in Prisma Access or
 NGFW 

 Attempts to create, renew, or tear down tunnels or datapaths into Prisma Access or NGFW 

 Attempts to start, stop, or restart any component in the agent
 infrastructure 

 Attempts to upgrade or downgrade any component in the agent infrastructure 

 Attempts to gather host information for the purposes of security posture or
 integrity 

 Attempts to remediate or change certain components on the host to bring the
 host inline with the required posture or integrity 

 All agent activity and activity by the administrator using Configuration Endpoint Management are automatically logged and sent to the Strata Logging Service . The logs
 will reside on the Strata Logging Service . You can view Audit Prisma Access Agent Logs and Management Logs using the log viewer or Strata Logging Service . 

 Visibility into Prisma Access Agents 

 Using data sent from the agent, the Endpoint Management
 page provides complete visibility and management
 capabilities of Prisma Access Agents to IT administrators. 

 You can view information about all Prisma Access Agents that interacted with Prisma Access or NGFW
 (established connectivity within a time range that you specify), including the
 following data: 

 Hostname 

 User 

 Operating system name 

 Operating version 

 Agent status 

 Connected location 

 Agent version 

 Public IP address 

 Private IP address 

 Ring membership (macOS and Windows agents only) 

 Last seen (the last time a keep-alive was sent to Prisma Access ) 

 Mobile experience score (if the Access Experience app is installed and enabled
 on an endpoint) (macOS and Windows agents only) 

 To give you the flexibility and speed to locate the data that you need, you can
 filter agent data or search for specific agents based on the following ring
 attributes: 

 Hostname 

 Operating system version 

 Operating system name 

 Agent version 

 Agent status 

 Public IP address 

 Private IP address 

 Ring (macOS and Windows agents only) 

 User 

 When a user encounters an issue, you can remotely download all agent logs without intervention from the user
 to examine Prisma Access Agent processes and diagnose the issue. You can also
 download the host information profile
 report to review information about the security status of the endpoints
 and which host attributes are monitored for policy enforcement. With permission from
 the user, you can also run a remote shell to access the end user's
 device, run shell commands to diagnose the problem, and potentially remediate the
 problem in a single session. (Remote shell is only available on macOS and Windows
 agents.) 

 Previous 

 Prisma Access Agent Administration Overview 

 Next 

 Automatic Tunnel Restoration in Prisma Access Agents 

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
