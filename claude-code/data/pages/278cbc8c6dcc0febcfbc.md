---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/8.3-ce/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux
fetched_at: 2026-09-06T11:26:55Z
source: cortex-platform
---

# Cytool for Linux | 8.3 CE (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 8.3 CE (EoL) 

 Cortex XDR Agent for Linux 

 Troubleshooting Resources for Linux 

 Cortex XDR agent 8.3 CE EoL 

 Cytool for Linux 

 Cytool is a command-line tool integrated into the Cortex XDR agent that enables you to query and manage both basic and advanced functions of the agent. 

 Cytool is a command-line tool that is integrated into the Cortex XDR agent that enables you to query and manage both basic and advanced functions of the agent. For most commands, changes that you make using Cytool are active until the agent receives the next heartbeat communication from Cortex XDR. 

 The following table displays the Cytool options available on Linux endpoints. 

 Note 

 Since Cortex XDR agent 7.6, the pmd process includes and replaces the trapsd process. 

 Command Option 

 Description 

 adaptive_policy 

 Adaptive policy agent commands. 

 Usage: cytool adaptive_policy [<interval> <collect_stats> <recalc> <query>] 

 where: 

 interval —Sets a recalculation interval override (in seconds), or reset an override. Options are: seconds , policy 

 collect_stats —Initiates a collection of internal statistics. 

 recalc —Triggers a recalculation of the adaptive policy. 

 query —Query the current interval and APEX. 

 anti_malware 

 Perform Anti Malware related operations. 

 [version <query> 

 checkin 

 Initiate check-in to the server. 

 Usage: cytool checkin 

 To verify the check in, view the check-in time on the Cortex XDR agent console. 

 connectivity_test 

 Perform a connectivity test to Cortex XDR servers. 

 Usage: cytool connectivity_test [request_count] 

 dump 

 Enable/disable dump generation or restore policy settings. 

 Usage: 

 cytool dump enable 

 cytool dump disable 

 cytool dump restore 

 endpoint_tags 

 Usage: cytool endpoint_tags <action> 

 where <action> can be: 

 add—To add tags to the endpoint tags. 

 remove—Remove the given tags from the list of endpoint tags. 

 list—Displays the available endpoint tags. 

 Note 

 Tags should be passed as one string separated by comas. 

 Linux does not support tag names with spaces as command line arguments to the shell installer. 

 Instead, tags can be set in the /etc/panw/cortex.conf configuration file, that supports all Linux installers. 

 For example: 

 cytool endpoint_tags add "tag1[,tag2,...,tagN]" 

 cytool endpoint_tags remove "tag1[,tag2,...,tagN]" 

 cytool endpoint_tags list 

 enum 

 Enumerate protected processes. 

 Usage: cytool enum 

 For example: 

 root@ubuntu: cytool enum ----------------------------------- Cortex XDR list of protected processes: ----------------------------------- PID CMD UID 1098 /usr/sbin/cron -f 0 1131 /usr/sbin/rsyslogd -n 104 

 To view processes for all users including those initiated by the operating system, specify the /a option. 

 Note 

 If you change the action mode for protected processes in the Exploit Security Profile in Cortex XDR, you must restart the protected processes for the security policy to be enforced on the processes and its forked processes; only then you will see them on this list. 

 event_collection 

 Stop or start event collection status (EDR/DSE). 

 <query, enable, disable, logstat> 

 -h --help 

 Displays the available help information 

 import suex 

 Import pre-downloaded content or local support exceptions. Used for solving specific problems with a support representative. 

 isolate stop 

 Release machine from network isolation. 

 last_checkin 

 Display last successful check-in time. 

 log 

 Set the log level for the desired process. 

 Usage: cytool log set_level <log_level> <components> 

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

 <components> is all or one or more of the following agent components: authorized , pmd , cortex xdr , kproc-ctrl . 

 For example: 

 cytool log set_level 2 all 

 Then use the cytool log collect command to generate a support file archive. 

 log collect 

 Generate support file archive of all logs in a TGZ file. 

 persist 

 The Cortex XDR agent stores policy and security event information such as the list of trusted signers, local verdicts, and one-time actions in local databases on the endpoint. To troubleshoot policy issues and security events. Use cytool persist operations to import, export, and view information stored in the local database. 

 Usage: cytool persist <action> 

 where <action>: 

 list —List the local databases on the endpoint. 

 **`export [ 

 reconnect 

 Try reconnecting if communication with server has been disabled, or force registration with a new Distribution ID. 

 Usage: cytool reconnect [force <distribution_id]> 

 runtime 

 Stop or start product components. 

 Usage: cytool runtime <action> <component> 

 where: 

 <action> —Change startup runtime action for an agent component. 

 Options are: start , stop , query . The query option displays the startup status for each component. 

 <component> —Target components for which to set the runtime action, or all components. 

 To change the runtime action for multiple components, list them with spaces separating each component. 

 Options: cortex xdr , authorized , pmd , kproc-ctrl 

 For example: 

 cytool runtime query Name PID User Status Command cortex xdr 1055 User1 Running /Library/Application Support/PaloAltoNetworks/Traps/bin/cortex xdr.app/Contents/MacOS/cortex xdr authorized 927 _traps_panw Running /Library/Application Support/PaloAltoNetworks/Traps/bin/authorized pmd 909 root Running /Library/Application Support/PaloAltoNetworks/Traps/bin/pmd kproc-ctrl 159 root Loaded com.paloaltonetworks.driver.kproc-ctrl cytool runtime stop all Name PID User Status Command authorized N/A N/A STOPPED N/A pmd N/A N/A STOPPED N/A cortex xdr N/A N/A STOPPED N/A kproc-ctrl N/A N/A Unloaded N/A cytool runtime start all Name PID User Status Command system call failed for command='/usr/bin/su -l Traps -c "/bin/launchctl start cortex xdr.plist"', returned status code=768 authorized 1883 _traps_panw Running /Library/Application Support/PaloAltoNetworks/Traps/bin/authorized pmd 1889 root Running /Library/Application Support/PaloAltoNetworks/Traps/bin/pmd cortex xdr N/A N/A FAILED TO START N/A kproc-ctrl 160 root Loaded com.paloaltonetworks.driver.kproc-ctrl 

 scan 

 Perform Scan operations on the endpoint. 

 Options: start , stop , query 

 startup 

 Enable, disable, or query the startup state of Cortex XDR agent components. 

 Usage: cytool startup <action> <component> 

 where: 

 <action> —Change startup action for an agent component. 

 Options are: enable , disable , query . 

 The query option displays the startup status for each component. 

 <component> —Target component for which to set the startup action. To change the startup action for multiple components, list them with spaces separating each component. Options are: cortex xdr , authorized , pmd , kproc-ctrl 

 For example: 

 root@ubuntu: sudo ./cytool startup disable cortex xdr pmd Process name Startup status cortex xdr Disabled authorized Enabled pmd Disabled kproc-ctrl Loaded root@ubuntu: sudo ./cytool startup enable all Process name Startup status cortex xdr Enabled authorized Enabled pmd Enabled kproc-ctrl Loaded 

 Previous Troubleshooting Resources for Linux 

 Last updated 4 days ago 

 Was this helpful?
