---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/5.0/traps-agent-5.0-for-linux/use-the-traps-agent-for-linux
fetched_at: 2026-09-16T08:51:42Z
source: cortex-platform
---

# Use the Traps Agent for Linux | 5.0 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 5.0 

 Traps Agent 5.0 for Linux 

 Use the Traps Agent for Linux 

 After you install Traps for Linux, Traps operates transparently in the background as a system process. Typically, it is not necessary to interact with the Traps agent; however, to perform common actions, such as initiating a manual check in with the Traps management service, you can use the command-line utility (also available for Mac and Windows) named Cytool. Cytool is available in the /opt/traps/bin/cytool directory and must be run as root or with root permissions. 

 Display the Cytool help. 

 From the Linux server, run the cytool command without any arguments or with -h or --help options. 

 Ask Copy 

 root@ubuntu:~$ /opt/traps/bin/cytool 

 Usage: cytool<options> 
 cytool - Support tool 

 Options: 
 -h --help Display help information. 
 enum List processes protected by Traps. 
 startup query List startup status for traps endpoint agent(s) and daemon(s). 
 startup <enable | disable> <process_name | all> Enable/Disable agent(s) and daemon(s) after reboot. 
 runtime query List runtime status for agent(s), daemon(s) and kernel extensions. 
 runtime <start | stop> <process_name | all> Start/Stop agent(s), daemon(s) and kernel extensions immediately. 
 persist list Display list of persistent databases. 
 persist export <db_name | db_path> Export database(s) to the file(s) in JSON format. 
 persist import <db_name | db_path> <file_name> Import data into the database from the given JSON file. 
 persist print <db_name | db_path> [csv] Print database to the command prompt. 
 log <log_level> <process_name | all> Set log level for the desired process. 
 log collect Generate support file archive. 
 dump <enable | disable | restore> Enable/Disable dump generation or restore policy settings. 
 checkin Initiate Check In Now (send heartbeat to ESM). 

 Follow the usage guidelines to run additional Cytool commands. 

 List processes protected by Traps. 

 Enter the cytool enum command. 

 Ask Copy 

 root@ubuntu:~$ cytool 
 enum 
 ----------------------------------- 
 Traps list of protected processes: 
 ----------------------------------- 
 PID CMD UID 
 1098 /usr/sbin/cron -f 0 
 1131 /usr/sbin/rsyslogd -n 104 

 To view processes for all users including those initiated by the operating system, specify the /a option. 

 Start or stop Traps daemons. 

 The Traps agent comprises the trapsd, authorized, and pmd daemons. To start or stop one or all daemons, enter either the cytool runtime [start | stop] [ <process_name> | all] command or the cytool startup [enable | disable] [ <process_name> | all] command. The behavior of both commands changes both the current running state and the startup registration status of the daemons when the server boots. 

 For example: 

 Ask Copy 

 root@ubuntu:~$ /opt/traps/bin/cytool 
 runtime stop trapsd 
 Name PID User Status Command 
 trapsd N/A N/A STOPPED N/A 
 authorized 2179 root Running /opt/traps/bin/authorized 
 pmd 2164 root Running /opt/traps/bin/pmd 
 root@ubuntu:~$ /opt/traps/bin/cytool runtime start all 
 Name PID User Status Command 
 trapsd 26427 root Running /opt/traps/bin/trapsd 
 authorized 2179 root Running /opt/traps/bin/authorized 
 pmd 2164 root Running /opt/traps/bin/pmd 

 View the Traps security policy. 

 Traps stores policy and security event information such as the list of trusted signers, local verdicts, and one-time actions in local databases in the /opt/traps/persist/ directory. To troubleshoot policy issues and security events, you can use Cytool to import, export, and view information stored in the local database. 

 To view a list of all local databases, use the cytool persist list command. 

 Ask Copy 

 root@ubuntu:~$ /opt/traps/bin/cytool 
 persist list 
 Persistent database list: 
 post_detection.db Database of post-detection candidates 
 agent_actions.db Database of one time actions 
 cloud_frontend.db Database of Cloud frontend settings 
 hashes_lru.db Least recently used verdicts database 
 cloud_reports.db Database of Cloud reports 
 hashes.db Database of the verdicts received from WildFire 
 esm_frontend.db Database of ESM frontend settings 
 policy.db Policy database 
 fvhash.db Database of blacklisted fvhashes 
 trusted_signers.db Database of trusted signers 
 hash_paths.db Database of file paths 
 hash_override.db Database of hashes override (Admin exeptions) 
 esm_reports.db Database of ESM reports 
 security_events.db Database of security events (preventions) 
 file_upload.db Database of files being uploaded to ESM 
 hashes_retransmit.db Database of hashes to be retransmitted 
 agent_settings.db Database of agent settings 

 To view the records of a database, use the cytool persist print [ <database_name> | <database_path> ] command where you specify either the name of database (see the cytool persist list command) or the path to the database. Or, to export the records of a database to a JSON file, use the cytool persist export [ <database_name> | <database_path> ] command. For example: 

 Ask Copy 

 root@ubuntu:~$ /opt/traps/bin/cytool 
 persist print security_events.db 
 Database security_events: 
 persistence::DB: /opt/traps/persist/security_events.db: Open 
 persistence::DB: /opt/traps/persist/security_events.db: Open: IO error: lock /opt/traps/persist/security_events.db/LOCK: Resource temporarily unavailable 
 3c34dcc1-bc37-ffef-ed55-f5512df05884, 
 Prevention ID: 3c34dcc1-bc37-ffef-ed55-f5512df05884 
 Time: 2018-05-02T10:31:51Z 
 Timezone offset (min): 240 
 Module ID (CyveraComponent): 277 
 Module status (CyStatus): 0xC0400015 
 Blocked: false 
 Source process ID: 14818 
 Source process terminated: true 
 Source process command line: /root/Desktop/Linux_testers/ROP/lighttpd system 0 
 Source process file index: 0 
 Target process ID: 0 
 Target process terminated: false 
 Target process command line: 
 Target process file index: 0 
 User ID: 0 
 User name: 
 Traps version: 5.0.0.601 
 OS name: Linux 
 OS version: Red Hat Enterprise Linux Server release 6.9 (Santiago) 

 Machine name: Saar_redhat64x64 
 Dump path: /opt/traps/forensics/3c34dcc1-bc37-ffef-ed55-f5512df05884/ 
 Content version: 17-2805 
 IP Address: 10.200.0.55 
 Verdict (WildFire/Hash Control): 0 
 1 Files: 
 Name: lighttpd 
 Path: /root/Desktop/Linux_testers/ROP 
 Size: 0 
 Hash: 8630c9e57ca58fb7966c80525c36f572416e0a8db617b8a43c946d4fa966a71c 
 Version: 
 Publisher: 
 Quarantine ID: 
 Signers: '' 
 ------------------------------------------------ 
 ---------- END Security Event Files ---------- 

 root@ubuntu:~$ /opt/traps/bin/cytool persist export security_events.db 
 persistence::DB: /opt/traps/persist/security_events.db: Open 
 -rw-r--r-- 1 ubuntu root 25824 Jan 2 18:10 /home/ubuntu/traps/cytool/security_events.db_18.10.04.427_02.01.2018.json 

 To add records to the database, use the cytool persist import [ <database_name> | <database_path> ] <input_filename> command where <input_filename> is a JSON file. 

 Collect logs. 

 Use the cytool log <log_level> [ <process_name> | all] command to change the log level of a Traps component where: 

 <log_level> is an integer value corresponding to the log level: 

 1—Fatal 

 2—Critical 

 3—Error 

 4—Warning 

 5—Notice 

 6—Information 

 7—Debug 

 8—Trace 

 <process_name> is the traps component: trapsd , authorized , or pmd . 

 Then use the cytool log collect command to collect all logs in a TGZ file. 

 Ask Copy 

 root@ubuntu:~$ /opt/traps/bin/cytool log 
 1 trapsd 
 root@ubuntu:~$ /opt/traps/bin/cytool log collect 
 -rw-r--r-- 1 root root 1651939 Dec 30 20:33 /tmp/Traps_log_2017-12-30_20-33-22/Traps_log_2017-12-30_20-33-22.tgz 

 Manually initiate a check in with the server. 

 Use the cytool checkin command to initiate the manual check-in. To verify the status of the check-in on the Traps management service, view the LAST SEEN date from the additional details view of an endpoint on the Endpoints page. 

 Configure proxy communication. 

 If defined, the Traps agent uses the proxy settings defined in the system environment in /etc/environment . If proxy settings are not defined, you can add the proxy server to the system environment by specifying the following setting in the environment file: 

 https_proxy=”https:// <proxyserver> : <port> " 

 where: 

 <proxyserver> is the IP address of the proxy server 

 <port> is the port number used for proxy communication. 

 For example: https_proxy="https://10.196.20.244:8080" 

 View the version of Traps. 

 To view the version of Traps on the Linux server, open or read the version.txt file in the /opt/traps/ directory. For example: 

 Ask Copy 

 root@ubuntu:~$ cat /opt/traps/version.txt 
 traps_linux-5.0.0.1040 
 ce1707dadbbb67effb7bf08cd4edee60d9508377 

 Previous Install the Traps Agent for Linux 

 Next Uninstall the Traps Agent for Linux 

 Last updated 2 months ago 

 Was this helpful?
