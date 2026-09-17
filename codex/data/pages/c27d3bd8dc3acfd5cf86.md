---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-m-series-appliance/m-series-setup-overview/set-up-an-m-series-appliance-in-management-only-mode
fetched_at: 2026-09-16T07:42:01Z
source: palo-alto-main
---

# Set Up an M-Series Appliance in Management Only Mode Clear

Updated on 

 Jul 16, 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Set Up the M-Series Appliance 

 M-Series Setup Overview 

 Set Up an M-Series Appliance in Management Only Mode 

 Download PDF 

 Panorama 

 Set Up an M-Series Appliance in Management Only Mode 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Set Up an M-Series Appliance in Management Only Mode 

 How to set up an M-Series appliance in Management Only
mode. 

 Set up the Panorama management server in Management
Only mode to dedicate Panorama to managing firewalls and Dedicated
Log Collectors. Panorama in Management Only mode have no log collection
capabilities, except for config and system logs, and requires a
Dedicated Log Collector to store logs. 

 If you configured a local Log Collector, the local Log Collector still exists on Panorama when
 you change to Management Only mode despite having no log collection
 capabilities. Deleting the local Log Collector ( Panorama Managed Collectors ) deletes the Eth1/1 interface configuration the local Log
 Collector uses by default. If you decide to delete the local Log Collector, you
 must reconfigure the Eth1/1
 interface . 

 Rack mount the M-Series appliance. Refer to the M-Series
Appliance Hardware Reference Guide for instructions. 

 Perform
Initial Configuration of the M-Series Appliance . 

 Register
Panorama and Install Licenses . 

 Install content and software
updates on Panorama . 

 Change to Management Only mode. 

 Log in to the Panorama CLI . 

 Switch from Panorama mode to Management Only mode: 
 request system system-mode management-only 

 Enter Y to confirm the mode
change. The Panorama management server reboots. If the reboot process
terminates your terminal emulation software session, reconnect to
the Panorama management server to see the Panorama login prompt. 

 If you see a CMS Login prompt,
this means the Panorama management server has not finished rebooting.
Press Enter at the prompt without typing a username or password. 

 Log back in to the CLI. 

 Verify that the switch to Management Only mode succeeded: 
 show system info | match system-mode 
 If
the mode change succeeded, the output displays: 
 system mode:management-only 

 Configure Administrative Access to
 Panorama 

 Manage Firewalls 

 Manage Log Collection
