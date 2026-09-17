---
url: https://docs.paloaltonetworks.com/globalprotect/user-guide/6-0/globalprotect-app-for-linux/uninstall-the-globalprotect-app-for-linux
fetched_at: 2026-09-15T15:14:13Z
source: palo-alto-main
---

# Uninstall the GlobalProtect App for Linux Clear

Updated on 

 Fri Nov 07 16:16:53 PST 2025 

 Focus 

 Home 

 GlobalProtect 

 GlobalProtect App for Linux 

 Uninstall the GlobalProtect App for Linux 

 Download PDF 

 English 

 한국어 (Korean) 

 GlobalProtect 

 Uninstall the GlobalProtect App for Linux 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Previous 

 Disconnect the GlobalProtect App for Linux 

 Next 

 GlobalProtect for IoT Devices 

 Uninstall the GlobalProtect App for Linux 

 Where Can I Use This? What Do I Need? 

 Linux endpoints only 

 GlobalProtect app version 6.0 or later 

 You can uninstall the GlobalProtect app for
Linux using either the dpkg and the apt-get utility. To uninstall
the GlobalProtect app, you must run the command with root permissions: 

 Begin the uninstallation process by
entering the sudo dpkg -P globalprotect command. 

 user@linuxhost:~$ sudo dpkg -P globalprotect 
(Reading database ... 209181 files and directories currently installed.)
Removing globalprotect (4.1.0-12) ...
gp service is running and we need to stop it...
Disable service...
Removing gp service...
gp service has been removed successfully
Removing configuration...

 Uninstall the GlobalProtect app for Linux by entering
the sudo apt-get remove globalprotect command. 

 Previous 

 Disconnect the GlobalProtect App for Linux 

 Next 

 GlobalProtect for IoT Devices
