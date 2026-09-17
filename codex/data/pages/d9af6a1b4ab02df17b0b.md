---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/engines/troubleshoot-cortex-xsoar-engines/troubleshoot-engine-upgrades
fetched_at: 2026-09-16T08:56:53Z
source: cortex-platform
---

# Troubleshoot Engine Upgrades | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Engines 

 Troubleshoot Cortex XSOAR Engines 

 Cortex XSOAR 6.13 

 Troubleshoot Engine Upgrades 

 Troubleshoot engine upgrades in Cortex XSOAR 6.13. 

 During an upgrade, the upgrade file is sent to the engine server. A cron job running on the engine server checks if that file exists. The most common upgrade error is that the job is not running so the new installer does not run. 

 SSH to the machine. 

 Check the d1 service status on the engine server. It is possible that it stopped or doesn't exist. 

 sudo systemctl status d1 

 Access the installer log on the engine server and review the error. 

 sudo vi /tmp/demisto_install.log 

 Rerun the installer on the engine server using one of the following options. You can open a second window and run watch df -h . If the problem seems to be disk space, you should resolve the disk space issue and then rerun the installer. 

 Option 1 

 Download the installer from the user interface and copy it to the engine server. 

 sudo chmod +x installer.sh 

 sudo ./installer.sh -- -y 

 Option 2 

 Verify that /usr/local/demisto/d1_upgrade.sh exists. 

 If the file exists, run the following on the engine server: 

 sudo chmod +x /usr/local/demisto/d1_upgrade.sh 

 sudo /usr/local/demisto/d1_upgrade.sh 

 If d1_upgrade.sh does not exist, check if /usr/local/demisto/archived_d1_upgrade.sh exists and that it was created at the time of the attempted upgrade. 

 If the file exists and was created at the time of the attempted upgrade, run the following on the engine server: 

 sudo chmod +x /usr/local/demisto/archived_d1_upgrade.sh 

 sudo /usr/local/demisto/archived_d1_upgrade.sh 

 Previous Troubleshoot Engine Installation 

 Next Troubleshoot Engine Connectivity 

 Last updated 1 month ago 

 Was this helpful?
