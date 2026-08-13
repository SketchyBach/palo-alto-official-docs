---
url: https://docs.paloaltonetworks.com/prisma-access-agent/release-notes/prisma-access-agent-release-information/prisma-access-agent-addressed-issues
fetched_at: 2026-08-13T17:22:30Z
source: palo-alto-main
---

# Prisma Access Agent Addressed Issues Clear

Prisma Access Agent Addressed Issues 

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

 Prisma Access Agent Addressed Issues 

 Updated on 

 Wed Jul 29 16:38:38 PDT 2026 

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

 Wed Jul 29 16:38:38 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent Release Notes 

 Prisma Access Agent Release Information 

 Prisma Access Agent Addressed Issues 

 Download PDF 

 Prisma Access Agent 

 Prisma Access Agent Addressed Issues 

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

 Prisma Access Agent 25.1 Known Issues 

 Next 

 Changes to Default Behavior in Prisma Access Agent 

 Prisma Access Agent Addressed Issues 

 Review the issues addressed in the Prisma Access Agent . 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the
 deployment you're using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 Review the issues that have been addressed in Prisma Access Agent . 

 Issues Addressed in Prisma Access Agent 26.2.2 (macOS and Windows) 

 Issues Addressed in Prisma Access Agent 26.2.1 

 Issues Addressed in Prisma Access Agent 26.2 

 Issues Addressed in Prisma Access Agent 26.1.2 

 Issues Addressed in Prisma Access Agent 26.1.1 

 Issues Addressed in Prisma Access Agent 25.7.1 

 Issues Addressed in Prisma Access Agent 25.7 

 Issues Addressed in Prisma Access Agent 25.6.2 

 Issues Addressed in Prisma Access Agent 25.6 

 Issues Addressed in Prisma Access Agent 25.4 

 Issues Addressed in Prisma Access Agent 25.3.1 

 Issues Addressed in Prisma Access Agent 25.3 

 Issues Addressed in Prisma Access Agent 26.2.2 (macOS and Windows) 

 The following table lists the addressed issues in Prisma Access Agent 26.2.2
 for macOS and Windows. 

 Issue ID 

 Description 

 PANG-13419 

 Fixed an issue where the Prisma Access Agent , when configured in
 always-on mode, did not automatically reconnect after a network
 status change, such as when an endpoint resumed from sleep and
 network connectivity became available. The agent remained unable
 to connect, requiring users to manually initiate the connection.
 This occurred because the agent attempted to connect before
 network connectivity was fully established, which prevented
 subsequent automatic connection attempts. The agent now properly
 detects network status changes and automatically reconnects. 

 PANG-13210 

 Fixed an issue where the Prisma Access Agent pre-logon tunnel
 disconnected and did not automatically reconnect when an
 endpoint resumed from an extended suspension in pre-logon mode.
 The tunnel now automatically reconnects after the endpoint
 resumes from suspension. 

 PANG-13116 

 Fixed an issue where the Prisma Access Agent frequently
 disconnected, causing the tunnel to tear down when an access
 token expired and the agent failed to refresh the token for
 re-authentication. The agent now properly handles token
 refreshes to maintain a stable connection. 

 PANG-12959 

 Fixed an issue where the Prisma Access Agent intermittently
 received an "Agent Configuration Not Found" message after an
 endpoint upgrade. The agent now correctly retrieves its
 configuration after an upgrade. 

 PANG-12945 

 Fixed an issue where Endpoint DLP blocked a Prisma Access Agent 
 worker thread in the control manager, which prevented proper
 operation of the agent. Endpoint DLP no longer interferes with
 Prisma Access Agent worker threads, ensuring continuous and
 correct functionality. 

 PANG-12928 

 Fixed an issue where Windows endpoints could not connect to the
 Prisma Access Agent in pre-logon mode and the Prisma Access Agent icon doesn't show up in the
 credentials provider, preventing successful pre-logon
 connections. Endpoints now connect to the agent as expected in
 pre-logon mode. 

 PANG-12884 

 On endpoints running macOS, fixed an issue where the Prisma Access Agent 
 Connected window lacked configuration
 options for its visibility or display duration. Administrators
 can now manage the display of the connection window. 

 PANG-12883 

 For Prisma Access Agents on macOS and Windows devices,
 fixed an issue where when the device was in sleep mode, running
 the pacli status command resulted in an
 invalid JSON string response and a timeout error, preventing the
 retrieval of Endpoint Manager (EPM) status. With this fix, the
 command now provides the correct EPM status. 

 PANG-12882 

 Fixed an issue where the Prisma Access Agent app on macOS
 endpoints remained open after users signed out. This occurred if
 the app lost focus when a user clicked another application or
 window after initiating sign-out from the Settings page. The app
 now closes as expected after sign-out. 

 PANG-12484 

 Fixed an issue where the Prisma Access Agent pre-logon tunnel did
 not connect automatically after users logged off the operating
 system, preventing them from establishing the connection from
 the Prisma Access Agent app in pre-logon mode. The pre-logon
 tunnel now establishes automatically after users log off. 

 PANG-12422 

 Fixed an issue where IPSec tunnels did not use optimized Path
 Maximum Transmission Unit (MTU) settings when enabled. IPSec
 tunnels now correctly apply the optimized Path MTU. 

 Issues Addressed in Prisma Access Agent 26.2.1 

 The Prisma Access Agent 26.2.1 release includes performance and bug fixes. The
 following table lists the security issues addressed in Prisma Access Agent 
 26.2.1. 

 Issue ID 

 Description 

 — 

 A fix was made to address CVE-2026-0271 
 (Linux). 

 — 

 A fix was made to address CVE-2026-0268 
 (Linux). 

 — 

 A fix was made to address CVE-2026-0248 (Android
 and ChromeOS). 

 — 

 A fix was made to address CVE-2026-0247 ( Prisma Access Agent (Endpoint DLP) on macOS and Windows). 

 — 

 A fix was made to address CVE-2026-0246 (Linux,
 macOS, and Windows). 

 — A fix was made to address CVE-2026-0245 (macOS and
 Windows). 

 Issues Addressed in Prisma Access Agent 26.2 

 The following table lists the addressed issues in Prisma Access Agent 26.2. 

 Issue ID 

 Description 

 PANG-11346 

 Fixed an issue where on Ubuntu operating systems, Docker
 containers experienced a "Network is unreachable" error when
 attempting to send curl traffic, despite the host system having
 full connectivity, if the Prisma Access Agent was connected on
 the host. 

 PANG-10947 

 Fixed an issue where the Prisma Access Agent on Linux devices
 (such as ArchLinux and Ubuntu) failed to automatically reconnect
 to the gateway in on-demand mode after the internet connection
 was temporarily lost and then restored. 

 PANG-10668 

 Fixed an issue where the Prisma Access Agent settings page
 appeared half blank on ArchLinux devices running KDE Plasma
 desktop when a Dark OS theme was enabled, preventing relevant
 data from displaying. 

 Issues Addressed in Prisma Access Agent 26.1.2 

 Issue ID 

 Description 

 PANG-11395 

 Fixed an issue where the Prisma Access Agent on Windows 11
 laptops did not reauthenticate with the internal gateway when
 transitioning between network interfaces (for example, from
 Wi-Fi to LAN) and temporarily having more than one active
 network interface. This prevented the IP-user mapping from being
 updated on the NGFW firewall, causing traffic from the user's IP
 to be unrecognized. 

 PANG-11328 

 Fixed an issue where DNS resolution failed for Microsoft 365
 services (MS Teams and Outlook) running Prisma Access Agents on
 dual-stack Windows devices. 

 PANG-11311 

 Fixed an issue where the Prisma Access Agent displayed an
 erroneous "Your connectivity might be affected. Please try again
 or contact your administrator" error notification when a user
 manually disconnected from an on-demand connection. 

 PANG-11293 

 Fixed an issue where Prisma Access Agent version 26.1 was unable
 to retrieve the status of disk encryption for Host Information
 Profile (HIP) reports, causing HIP checks to fail and denying
 access to private applications. 

 PANG-11284 

 Fixed an issue where, after upgrading to Prisma Access Agent 
 version 26.1.1.10 on Windows, users attempting to log in with
 Microsoft Entra SSO experienced login failures and HIP check
 compliance errors (Error 53000) because the embedded browser
 incorrectly prompted for a plugin installation." 

 PANG-11274 

 Fixed an issue on macOS devices where gateway connections would
 fail or experience significant delays after waking from sleep.
 This occurred because the Prisma Access Agent service (daemon)
 attempted to access client certificates in the login keychain
 through the user interface (UI) while the UI was still asleep.
 These requests would queue up and process sequentially once the
 UI woke, causing older requests to time out and preventing
 timely gateway connections. 

 Issues Addressed in Prisma Access Agent 26.1.1 

 The following table lists the issues addressed in Prisma Access Agent version
 26.1.1. 

 Issue ID Description 

 PANG-11201 

 Fixed an issue on Prisma Access Agents for Linux where the Prisma Access Agent connection profile became stuck in an "activating"
 state when NetworkManager was configured not to manage the
 tunnel interface, resulting in a tunnel connect and disconnect
 loop that prevented successful establishment of the tunnel. 

 PANG-11153 

 Fixed an issue where the Prisma Access Agent on Linux experienced
 recurring PASrv process crashes approximately every 20 seconds
 due to abnormal termination during agent upgrade operations,
 causing the agent to become unresponsive and preventing log
 collection. 

 PANG-10723 

 Fixed an issue where the Prisma Access Agent installer script on
 Linux incorrectly modified permissions of the entire
 /opt installation directory. The
 installer script now only modifies
 /opt/paloaltonetworks . 

 Issues Addressed in Prisma Access Agent 25.7.1 

 The following table lists the issues addressed in Prisma Access Agent version
 25.7.1. 

 Issue ID Description 

 PANG-9876 Fixed an issue where the PASrv service would crash and generate
 crash files on a newly installed Prisma Access Agent running in
 Always On mode on Linux systems. The crash occurred after user
 sign-in during the tunnel connection process while the agent was
 operating in Always On mode. This issue affected Linux environments,
 particularly Ubuntu 22 x86 systems. 

 Issues Addressed in Prisma Access Agent 25.7 

 The following table lists the issues addressed in Prisma Access Agent version
 25.7. 

 Issue ID Description 

 PANG-9242 

 Fixed an issue where the Prisma Access Agent on macOS and Windows
 would fail to properly clean up tunnel interface routing table
 entries when executing the pacli epm
 signout command after a gateway shutdown had
 left the agent in a Disconnected state. This problem occurred
 when agents that were previously connected to a tenant became
 disconnected due to gateway shutdowns, and users subsequently
 attempted to sign out using the pacli 
 command. 

 PANG-8945 

 Fixed an issue where the Prisma Access Agent Manager would
 incorrectly handle ICMP traffic configuration after upgrading to
 the latest version. When the Block Non-TCP and
 Non-UDP based traffic when connected to tunnel 
 option was disabled by default following an upgrade, the
 pacli traffic show command would
 inaccurately display Allow non-tunnel outbound ICMP
 when connected to tunnel as true, while the
 underlying Allow ICMP for troubleshooting 
 value was incorrectly being passed as false instead of the
 expected true value. 

 The agent now properly synchronizes the ICMP traffic
 configuration values to ensure consistent behavior between the
 configuration display and actual traffic routing. 

 PANG-8929 

 Fixed an issue where the Prisma Access Agent on Windows would
 incorrectly report "error: 513 - PASrv is unreachable, please
 confirm it's running" when executing the pacli epm
 status command during reinstallation scenarios.

 Issues Addressed in Prisma Access Agent 25.6.2 

 The following table lists the issues addressed in Prisma Access Agent version
 25.6.2. 

 Issue ID Description 

 PANG-9620 

 Fixed an issue where the Prisma Access Agent would automatically
 disconnect and remain disconnected without attempting to
 reconnect, leaving users without network protection. The problem
 occurred when the agent lost its connection to the endpoint
 management server and failed to re-establish the connection
 automatically as expected. 

 This occurred due to a DNS resolution timing conflict in certain
 network environments where the primary DNS server was
 unresponsive while the secondary DNS server was functioning
 properly. The fix adjusts the DNS resolution process to ensure
 proper failover occurs when the primary DNS server is
 unavailable, allowing the agent to maintain connectivity and
 automatically reconnect when network issues are resolved. 

 PANG-9630 

 Fixed an issue where the Prisma Access Agent would become stuck
 in a "Connecting" state after a network switch when attempting
 to connect to an internal gateway. This problem occurred when
 users experienced a network change that caused them to be logged
 out from the tunnel, and while the Prisma Access Agent endpoint
 manager web-socket would successfully reconnect, the Prisma Access Agent app would remain stuck displaying "Connecting"
 indefinitely. 

 PANG-9276 

 Fixed an issue where the Spyder application would display
 "Permission denied" errors and fail to work properly when Prisma Access Agent was installed on the same computer. Users found
 that Spyder would only function normally after completely
 removing the Prisma Access Agent from their system, creating a
 conflict between the two programs. The fix ensures that the
 Prisma Access Agent no longer interferes with Spyder, allowing
 both programs to run simultaneously without conflicts while
 maintaining the agent's security protection for other
 applications on the system. 

 PANG-9220 

 Fixed an issue where users encountered "Server Enrollment
 failure" errors after installing Prisma Access Agent version
 25.4.0.29, preventing them from successfully connecting to their
 organization's network. The problem occurred during the initial
 setup process when the agent attempted to register with the
 endpoint management server but failed with messages indicating
 an invalid enrollment secret. This occurred due to a
 compatibility issue between the agent's security enrollment
 method and certain Windows system security components. When the
 agent tried to use the primary secure enrollment process, some
 Windows systems would reject the connection due to unsupported
 security protocols, causing the entire enrollment to fail. 

 PANG-9092 

 Fixed an issue where the Prisma Access Agent would freeze and
 become stuck in a non-responding state. The problem occurred
 when the application attempted to update multiple settings at
 the same time from different parts of the program, causing
 conflicts that would lock up the entire application. This
 resulted in users being unable to interact with Prisma Access Agent , as the interface would stop responding and the agent
 would appear to hang indefinitely. The fix ensures that all
 setting updates are now processed in a controlled, sequential
 manner to prevent these conflicts and maintain application
 responsiveness. 

 PANG-9067 
 Fixed an issue where the Prisma Access Agent on macOS 15.6.1 failed to connect to external gateways when selecting Best Location and incorrectly switched to internal connectivity. This issue manifested in two specific scenarios: 

 After upgrading the operating system from macOS 15.6 to 15.6.1, Prisma Access Agent would incorrectly connect to an on-premises gateway instead of maintaining its connection to the external Prisma Access gateway that it was using prior to the OS upgrade. 

 When users selected Best Location from the Prisma Access Agent app, the agent would search through all available Prisma Access gateways but then inappropriately switch to Internal mode, even when connected to a home WiFi network where Internal Host Detection should not be triggered. 

 This occurred due to the improper cleanup of the on-premises tunnel routes during the Best Location selection process, which caused the system to incorrectly determine that it was on an internal network and activate the Internal Host Detection functionality. This resulted in users being unable to establish proper external gateway connections through Prisma Access Agent on the updated macOS version, forcing the agent into internal mode when external connectivity was required and available. 

 Issues Addressed in Prisma Access Agent 25.6 

 The following table lists the issues addressed in Prisma Access Agent version
 25.6. 

 Issue ID Description 

 PANG-8845 

 Fixed an issue where the Prisma Access Agent would incorrectly
 remain bound to port 0 when switching between Prisma Access Agent endpoint manager configurations with different proxy
 settings, causing endpoint traffic to Explicit Proxy (EP) to
 fail. This problem occurred when the agent initially connected
 to an endpoint manager without agent proxy configured, then
 switched to a different endpoint manager that had a proxy port
 configured, but failed to update its port binding from port 0 to
 the new proxy port. The agent now correctly updates its port
 binding when switching between endpoint manager configurations
 with different proxy settings, eliminating traffic routing
 disruptions. 

 PANG-8200 

 Fixed an issue where the Prisma Access Agent on Windows devices
 would incorrectly display the previously connected server FQDN in
 the Server Name field after executing the pacli epm
 signout command without the --keep 
 parameter, instead of properly resetting to show Select
 Server Name as expected. This inconsistency between
 Windows and Mac platforms has been resolved, ensuring that both
 operating systems now consistently reset the login view and display
 the default Select Server Name prompt when
 signing out without preserving server information. 

 Issues Addressed in Prisma Access Agent 25.4 

 The following table lists the issues addressed in Prisma Access Agent version
 25.4. 

 Issue ID Description 

 PANG-7949 Fixed an issue where the Dynamic Privilege Access enabled Prisma Access Agent was unable to connect to a gateway after upgrading an
 endpoint to Windows 11 24H2. Following the Windows upgrade, the
 Prisma Access Agent would lose the ability to establish gateway
 connections, even though the Endpoint Manager (EPM) connection
 remained functional. This issue occurred consistently across systems
 that had undergone the Windows 11 24H2 upgrade, affecting the
 agent's ability to connect to any configured gateways while
 maintaining normal endpoint manager connectivity. 

 PANG-7865 Fixed an issue where the Prisma Access Agent on Windows did not
 properly honor updated session timers after a user extended their
 session through the embedded browser. The agent now correctly adopts
 the newly extended session duration when users authenticate through
 the session expiry banner, preventing premature session termination
 and ensuring the Prisma Access Agent icon remains responsive in the
 system tray throughout the extended session period. 

 PANG-7960 

 Fixed an issue where the Prisma Access Agent on Windows blocked
 authentication in the embedded browser due to the
 Best Available - Fail Safe mechanism
 in the forwarding profile triggering during the initial
 connection attempt. The embedded browser now properly bypasses
 the fail-safe mechanism when the agent is configured to run in
 on-demand mode, enabling successful authentication on the first
 attempt without requiring users to cancel and retry the
 authentication process after a reboot. 

 PANG-7309 Fixed an issue where the Prisma Access Agent on Windows failed to
 automatically switch from an external gateway to an internal gateway
 when the user's device woke from sleep mode after being connected to
 different network environments. The agent now properly detects
 network changes upon waking from sleep. It also automatically
 switches to the appropriate internal gateway without requiring
 manual sign-out via the pacli epm signout 
 command and subsequent reauthentication through the Prisma Access Agent app. 

 Issues Addressed in Prisma Access Agent 25.3.1 

 The following table lists the issues addressed in Prisma Access Agent version
 25.3.1. 

 Issue ID Description 

 PANG-7012 Fixed an issue where the embedded browser for Prisma Access Agent 
 did not reuse the Windows Hello token for reauthentication, forcing
 users to manually enter their credentials despite having Windows
 Hello enabled on their devices. The embedded browser now properly
 leverages existing Windows Hello authentication tokens for seamless
 reauthentication without requiring manual credential entry. 

 Issues Addressed in Prisma Access Agent 25.3 

 The following table lists the issues addressed in Prisma Access Agent version
 25.3. 

 Issue ID Description 

 PANG-6738 Fixed an issue where certificate authentication failed on Windows
 devices when certificates were stored in the machine certificate
 store, preventing the Prisma Access Agent from properly
 authenticating users with machine-level certificates. The agent now
 correctly accesses and utilizes client certificates from the machine
 certificate store, eliminating the need to manually import
 certificates to the user's personal certificate store as a
 workaround. 

 EPM-4616 Fixed an issue where newly added internal gateways weren’t
 visible in existing Prisma Access Agent settings, preventing
 administrators from updating agent configurations with recently
 added internal gateways. The agent settings now automatically
 refresh to display all available internal gateways, including those
 added after the initial configuration, eliminating the need to
 create new agent settings to access newly added gateways. 

 Previous 

 Prisma Access Agent 25.1 Known Issues 

 Next 

 Changes to Default Behavior in Prisma Access Agent 

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

 Release Notes 

 Prisma Access Agent 

 Next-Generation Firewall 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
