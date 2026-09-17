---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/8.7/cortex-xdr-agent-for-macos/troubleshooting-resources-for-mac/cytool-for-mac
fetched_at: 2026-09-16T08:51:39Z
source: cortex-platform
---

# Cytool for Mac | 8.7 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 8.7 

 Cortex XDR Agent for MacOS 

 Troubleshooting Resources for Mac 

 Cortex XDR agent 8.7 

 Cytool for Mac 

 In addition to being available for Windows and Linux endpoints, Cytool is also available for Mac endpoints. 

 Cytool is a command-line interface that is integrated into the Cortex XDR agent that enables you to query and manage both basic and advanced functions of the agent. Any changes that you make using Cytool are active until the agent receives the next heartbeat communication (every five minutes) from Cortex XDR. 

 On Mac endpoints, access Cytool as a super user using a terminal. Cytool is located in the /Library/Application Support/PaloAltoNetworks/Traps/bin directory on the endpoint. 

 The following table displays the Cytool options available on Mac endpoints. For the Cytool admin commands that require a password, the password is the same as is defined as the Uninstall password. 

 Note 

 Since Cortex XDR agent 7.6, the pmd process includes and replaces the trapsd process. 

 Command Option 

 Description 

 cert_enforcement 

 Perform Certificate enforcement related operations. 

 Usage: cytool cert_enforcement <operation> 

 Where <operation> is one of the following: 

 query Display current enforcement status 

 disable Forcibly disable enforcement 

 policy Set enforcement by policy 

 import <certificate file path> Import a proprietary certificate in PEM format as root CA 

 import clear Clear all custom root CA certificates. 

 checkin 

 Initiate check-in to the server. 

 Usage: sudo ./cytool checkin 

 To verify the checkin, view the check-in time on the Cortex XDR agent console. 

 dump 

 Enable or disable dump generation or restore policy settings. 

 Traps-Mac:bin Traps$ sudo ./cytool dump enable Traps-Mac:bin Traps$ sudo ./cytool dump disable Traps-Mac:bin Traps$ sudo ./cytool dump restore 

 endpoint_tags 

 Usage: sudo ./cytool endpoint_tags <action> 

 where <action> can be: 

 add —To add tags to the endpoint tags. 

 remove —Remove the given tags from the list of endpoint tags. 

 list —Displays the available endpoint tags. 

 Note 

 Tags should be passed as one string separated by comas. 

 For example: 

 Traps-Mac:bin Traps$ 

 sudo ./cytool endpoint_tags add "tag1 [,tag2, ...,tagN]" 

 Traps-Mac:bin Traps$ 

 sudo ./cytool endpoint_tags remove "tag1 [,tag2, ...,tagN]" 

 Traps-Mac:bin Traps$ 

 sudo ./cytool endpoint_tags list 

 enum 

 Enumerate protected processes. 

 Usage: sudo ./cytool enum 

 For example: 

 Traps-Mac:bin Traps$ sudo ./cytool enum List of protected processes: Process name Process ID User Photos 2047 User1 Mail 2099 User2 

 Note 

 If you change the action mode for protected processes in the Exploit Security Profile in Cortex XDR, you must restart the protected processes for the security policy to be enforced on the processes and its forked processes, and only then you will see them on this list. 

 -h --help 

 Traps-Mac:bin Traps$`` sudo ./cytool ` Usage: cytool cytool - Support tool Options: -h --help Display help information. enum List processes protected by Cortex XDR. startup query List startup status for Cortex XDR agent and daemons. startup <enable 

 import suex 

 Import pre-downloaded content or local support exceptions. Used for solving specific problems with a support representative. 

 isolate 

 Usage: cytool isolate stop 

 Release endpoint from network isolation. 

 log 

 Log set_level - Set the log level for the desired process. 

 Usage: sudo ./cytool log set_level <log_level> <components> 

 where: 

 <log_level> is an integer value corresponding to the log level: 

 0—Disable logging 

 1—Fatal 

 2—Critical 

 3—Error 

 4—Warning 

 5—Notice 

 6—Information 

 7—Debug 

 8—Trace 

 <components> is all or one or more of the following agent component: authorized , pmd , cortex xdr , kproc-ctrl . 

 For example: 

 Traps-Mac:bin Traps$ sudo ./cytool log set_level 2 all 

 log collect 

 Use the sudo ./cytool log collect command to generate a support file archive of all logs in a TGZ file. On Mac endpoints running OS X 10.10 and OSX 10.11, Cytool outputs the logs to the /var/log/traps directory. On Mac endpoints running macOS 10.12 and later, you can view logs from the Console application. 

 opswat 

 Check the Cortex XDR agent status and version. 

 Usage: sudo ./cytool opswat <parameter> 

 where <parameter> is: 

 version —Displays the version of the agent. 

 installed —Displays the agent installation status: 

 true if the com.paloaltonetworks.pkg.cortx xdr package is installed 

 or false if the package is not installed. 

 You must also supply the agent supervisor password to view the status. 

 running —Displays the running status of agent daemons: true if running or false if not running. 

 protected —Displays the applied policy status: true if applied or false if not applied. 

 Traps-Mac:bin Traps$ sudo ./cytool opswat version 8.1.0.1042 Traps-Mac:bin Traps$ sudo ./cytool opswat installed Password: true Traps-Mac:bin Traps$ sudo ./cytool opswat running true Traps-Mac:bin Traps$ sudo ./cytool opswat protected true 

 persist 

 The Cortex XDR agent stores policy and security event information such as the list of trusted signers, local verdicts, and one-time actions in local databases on the endpoint. To troubleshoot policy issues and security events, you can use cytool persist operations to import, export, and view information stored in the local database. 

 Usage: sudo ./cytool persist <action> 

 where <action> : 

 list —List the local databases on the endpoint. 

 ** export [<database name> ` 

 queryall 

 The cytool queryall command displays a list of imported certificates, for troubleshooting purposes. 

 Reconnect 

 Try reconnecting if communication with server has been disabled, or force registration with a new Distribution ID. 

 Usage: 

 cytool reconnect —Reconnects the Cortex XDR agent to the management application on the server. 

 cytool reconnect [force <distribution_id]> 

 runtime 

 Stop or start product components. 

 Usage: sudo ./cytool runtime <action> <component> 

 where: 

 <action> —Change startup runtime action for an agent component. 

 Options are: start , stop , query . The query option displays the startup status for each component. 

 <component> —Target component for which to set the runtime action, or all components if no components are specified. 

 To change the runtime action for multiple components, list them with spaces separating each component. 

 Options are: cortex xdr , authorized , pmd , kproc-ctrl 

 For example: 

 Traps-Mac:bin Traps$ sudo ./cytool runtime query Name PID User Status Command cortex xdr 1055 User1 Running /Library/Application Support/PaloAltoNetworks/Traps/bin/cortex xdr.app/Contents/MacOS/cortex xdr authorized 927 _traps_panw Running /Library/Application Support/PaloAltoNetworks/Traps/bin/authorized pmd 909 root Running /Library/Application Support/PaloAltoNetworks/Traps/bin/pmd kproc-ctrl 159 root Loaded com.paloaltonetworks.driver.kproc-ctrl Traps-Mac:bin Traps$ sudo ./cytool runtime stop all Name PID User Status Command authorized N/A N/A STOPPED N/A pmd N/A N/A STOPPED N/A cortex xdr N/A N/A STOPPED N/A kproc-ctrl N/A N/A Unloaded N/A Traps-Mac:bin Traps$ sudo ./cytool runtime start all Name PID User Status Command system call failed for command='/usr/bin/su -l Traps -c "/bin/launchctl start cortex xdr.plist"', returned status code=768 authorized 1883 _traps_panw Running /Library/Application Support/PaloAltoNetworks/Traps/bin/authorized pmd 1889 root Running /Library/Application Support/PaloAltoNetworks/Traps/bin/pmd cortex xdr N/A N/A FAILED TO START N/A kproc-ctrl 160 root Loaded com.paloaltonetworks.driver.kproc-ctrl 

 security_modules 

 Query, enable, disable or return to policy the Cortex XDR agent anti-tampering protection. 

 Usage: cytool security_modules operation module 

 Where: 

 Operation is one of the following: 

 query — Queries Security Module activity status 

 enable — Enables Security Module 

 disable — Disables Security Module 

 policy — Syncs the Security Module according to cloud-defined policy 

 Module options self_prot 

 startup 

 Enable, disable, or query the startup state of Cortex XDR agent components. 

 Usage: sudo ./cytool startup <action> <component> 

 where: 

 <action> —Change startup action for an agent component. 

 Options are: enable , disable , query . 

 The query option displays the startup status for each component. 

 <component> —Target component for which to set the startup action. To change the startup action for multiple components, list them with spaces separating each component. Options are: cortex xdr , authorized , pmd , kproc-ctrl 

 For example: 

 Traps-Mac:bin Traps$ sudo ./cytool startup disable cortex xdr pmd Process name Startup status cortex xdr Disabled authorized Enabled pmd Disabled kproc-ctrl Loaded Traps-Mac:bin Traps$ sudo ./cytool startup enable all Process name Startup status cortex xdr Enabled authorized Enabled pmd Enabled kproc-ctrl Loaded 

 wakeup 

 Wake up the endpoint from an OS incompatibility state. 

 Traps-Mac:bin Traps$ sudo ./cytool wakeup SIGTERM caught 

 Previous Troubleshooting Resources for Mac 

 Next Cortex XDR Agent for Linux 

 Last updated 14 days ago 

 Was this helpful?
