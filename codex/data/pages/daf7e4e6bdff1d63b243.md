---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.3/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows
fetched_at: 2026-09-06T10:20:09Z
source: cortex-platform
---

# Troubleshooting resources for Windows | 9.3 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 9.3 

 Cortex XDR agent for Windows 

 Cortex XDR agent 9.3 

 Troubleshooting resources for Windows 

 Refer to the following troubleshooting resources for the Cortex XDR agent for Windows. 

 Resource 

 Description 

 Services, Drivers, and Processes 

 Services: 

 C:\Program Files\Palo Alto Networks\Traps\cyserver.exe 

 C:\Program Files\Palo Alto Networks\Cortex XDR Health Helper\xdrhealth.exe 

 Drivers: 

 C:\Program Files\Palo Alto Networks\Traps\cyverak.sys 

 C:\Program Files\Palo Alto Networks\Traps\cyvrmtgn.sys 

 C:\Program Files\Palo Alto Networks\Traps\cyvrfsfd.sys 

 C:\Program Files\Palo Alto Networks\Traps\tedrdrv.sys 

 C:\Program Files\Palo Alto Networks\Traps\tdevflt.sys 

 C:\Program Files\Palo Alto Networks\Traps\tedrpers-<version>.sys 

 C:\Windows\System32\drivers\telam.sys 

 Processes: 

 C:\Program Files\Palo Alto Networks\Traps\CyveraConsole.exe 

 C:\Program Files\Palo Alto Networks\Traps\tlaworker.exe (background process that is always running) 

 C:\Program Files\Palo Alto Networks\Traps\cytray.exe (background process that is always running) 

 C:\Program Files\Palo Alto Networks\Traps\cytool.exe 

 C:\Program Files\Palo Alto Networks\Traps\cydump.exe 

 C:\Program Files\Palo Alto Networks\Traps\cyreport.exe 

 C:\Program Files\Palo Alto Networks\Traps\cyrprtui.exe 

 C:\Program Files\Palo Alto Networks\Traps\cysandbox.exe 

 C:\Program Files\Palo Alto Networks\Traps\cyuserserver.exe 

 C:\Program Files\Palo Alto Networks\Traps\cywscsvc.exe 

 C:\Program Files (x86)\Palo Alto Networks\Traps\cyreport.exe 

 C:\Program Files (x86)\Palo Alto Networks\Traps\cyrprtui.exe 

 C:\ProgramData\Cyvera\LocalSystem\Python\payload\cortex-xdr-payload.exe 

 Cortex XDR installation log 

 Specifies any errors encountered during installation of agent components. Use this log file when you need to troubleshoot installation issues. On Windows endpoints, the installer stores the log files in the temp or C:\Users\<user_name>\AppData\Local\Temp folder. 

 Cortex XDR agent service log 

 Indicates information, warnings, and errors related to the Cortex XDR. The Service log is located in the following folder on the endpoint: 

 Windows Vista or a later Windows OS — ProgramData\Cyvera\Logs 

 Windows XP — C:\Document and Settings\All Users\Application Data\Cyvera\Logs 

 Cortex XDR agent console log 

 Indicates information, warnings, and errors related to the agent console. The Console log is located in the following folder on the endpoint: 

 Windows Vista or a later Windows OS — C:\Users\<username>\AppData\Roaming\Cyvera 

 Windows XP — C:\Document and Settings\<username>\Application Data\Cyvera\Logs 

 Supervisor Command Line Tool (cytool.exe) 

 Allows you to manage agent features and perform advanced troubleshooting on the local endpoint from a command line interface. For more information, see Cytool for Windows. 

 Unknown files for analysis 

 The agent stores unknown files to send to Cortex XDR in the C:\ProgramData\Cyvera\Temp folder. After Cortex XDR submits a file to WildFire, the agent deletes the file from the Temp folder. 

 In some cases, third-party Antivirus (AV) applications raise an alert for this folder. If this occurs, we recommend that you whitelist this folder in the third-party AV application. 

 Cortex XDR Health Helper 

 Improves the upgrade process of the Cortex XDR agent, which monitors the machine at startup and initiates an upgrade rollback in case of a failed upgrade. As upgrades have multiple re-tries, the next try works on the agent of its original version with no interference. The service only runs at startup and remains in pause mode during other times. To ensure this service is not removed, a periodic task would re-instate the process in case it was removed. 

 Previous Uninstall the Cortex XDR agent for Windows 

 Next Cytool for Windows 

 Last updated 10 days ago 

 Was this helpful?
