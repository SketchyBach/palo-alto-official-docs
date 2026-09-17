---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/prisma-access-agent-administration-overview/agent-lifecycle-management
fetched_at: 2026-09-16T07:45:23Z
source: strata-and-sase
---

# Prisma Agent Lifecycle Management Clear

Updated on 

 Thu Aug 27 20:22:38 PDT 2026 

 Focus 

 Home 

 Prisma Agent 

 Prisma Agent Administration Overview 

 Prisma Agent Lifecycle Management 

 Download PDF 

 Prisma Agent 

 Prisma Agent Lifecycle Management 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Prisma Agent Administration Overview 

 Next 

 Automatic Tunnel Restoration in Prisma Agents 

 Prisma Agent Lifecycle Management 

 After you deploy Prisma Agents to mobile user endpoints in your
 organization, you can use Strata Cloud Manager to manage the lifecycle of the
 agents. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to activate the Prisma Agent feature 

 To simplify the day-to-day management of the fleet of Prisma Agents that
 have been deployed to mobile users, Prisma Agent provides a single point of
 control to help you maintain the agents in your fleet, troubleshoot agent connectivity
 issues, and gain visibility into the agents as a part of the troubleshooting
 process. 

 Installation and Configuration of Prisma Agents 

 To help you easily install Prisma Agents on mobile user endpoints
 without user intervention, you can onboard your users to configure the cloud infrastructure and agent settings that will be pushed to Prisma Access or NGFW. Then, you can download the Prisma Agent package from the Prisma Agent Endpoint Management
 page ( Configuration Endpoint Management ) for deployment to endpoints using third-party mobile device management
 (MDM) software such as Jamf Pro and Microsoft
 Intune.. 

 If you configured the agent to run in Always On mode, the
 agents are automatically launched when your users sign on to their devices, and will
 automatically connect to Prisma Access whenever they access their mobile
 devices. If you configured the agent to run in On Demand 
 mode, the user needs to launch the Prisma Agent and manually connect to
 Prisma Access . 

 After a first-time installation, users must log in to the Prisma Agent to complete their initial enrollment, even when Always On mode is configured.
 The agent does not automatically connect on the first installation. After this
 first login, Always On mode takes effect and the agent connects automatically on
 subsequent device logins. 

 Maintenance of Prisma Agents 

 ( macOS and Windows agents only ) To facilitate the upgrade of the deployed Prisma Agents , a
 maintenance routine called a staged rollout is used to easily upgrade
 the Prisma Agents on your end users' devices. Using staged rollouts , you can plan the upgrade of the Prisma Agent by staggering the upgrade based on user group and device
 operating system with minimal interruption to your end users. 

 You can set up upgrade rings with user or user group
 and OS attributes. Endpoints that match the criteria will be upgraded, while
 endpoints that are configured in another upgrade ring will wait for the successful
 completion of the first ring before beginning its upgrade. You can configure up to
 five upgrade rings. Any devices that are not part of the configured rings are placed
 in a default ring that will be upgraded after rings 0 to 4 have completed.

 When an upgrade is available, you’re notified of the upcoming rollout in the Endpoint Management
 page , and users or devices are upgraded in the order of the upgrade rings. 

 Selectively Upgrade or Downgrade Prisma Agents 

 ( macOS and Windows agents only ) To keep your managed devices secure, the Prisma Agent software is
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

 The Prisma Agent provides information that allows administrators to
 analyze, troubleshoot, and remediate agent problems remotely without requiring an
 active tunnel to Prisma Access or NGFW. 

 The Prisma Agent communicates with Prisma Access or NGFW in the
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

 The Prisma Agent provides audit trails in the form of logs regarding the
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
 will reside on the Strata Logging Service . You can view Audit Prisma Agent Logs and Management Logs using the log viewer or Strata Logging Service . 

 Visibility into Prisma Agents 

 Using data sent from the agent, the Endpoint Management
 page provides complete visibility and management
 capabilities of Prisma Agents to IT administrators. 

 You can view information about all Prisma Agents that interacted with Prisma Access or NGFW
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
 to examine Prisma Agent processes and diagnose the issue. You can also
 download the host information profile
 report to review information about the security status of the endpoints
 and which host attributes are monitored for policy enforcement. With permission from
 the user, you can also run a remote shell to access the end user's
 device, run shell commands to diagnose the problem, and potentially remediate the
 problem in a single session. (Remote shell is only available on macOS and Windows
 agents.) 

 Previous 

 Prisma Agent Administration Overview 

 Next 

 Automatic Tunnel Restoration in Prisma Agents
