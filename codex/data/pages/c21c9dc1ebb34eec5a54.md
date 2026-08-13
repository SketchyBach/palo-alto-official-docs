---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/set-up-and-manage-a-wildfire-appliance/enable-wildfire-appliance-analysis-features/set-up-wildfire-appliance-content-updates/install-wildfire-content-updates-directly-from-the-update-server
fetched_at: 2026-08-13T15:19:44Z
source: palo-alto-main
---

# Install WildFire Content Updates Directly from the Update
Server Clear

Install WildFire Content Updates Directly from the Update
Server 

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

 Install WildFire Content Updates Directly from the Update
Server 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 Set Up and Manage a WildFire Appliance 

 Enable WildFire Appliance Analysis Features 

 Set Up WildFire Appliance Content Updates 

 Install WildFire Content Updates Directly from the Update
Server 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 Install WildFire Content Updates Directly from the Update
Server 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 Set Up WildFire Appliance Content Updates 

 Next 

 Install WildFire Content Updates from an SCP-Enabled Server 

 Install WildFire Content Updates Directly from the Update
Server 

 Where Can I Use
This? What Do I Need? 

 WildFire Appliance 

 WildFire License 

 Verify connectivity from the appliance to the
update server and identify the content update to install. 

 Log in to the WildFire appliance and run
the following command to display the current content version: 

 admin@WF-500> show system info | match wf-content-version 

 Confirm that the appliance can communicate with the
Palo Alto Networks Update Server and view available updates: 

 admin@WF-500> request wf-content upgrade check 

 The
command queries the Palo Alto Networks Update Server and provides
information about available updates and identifies the version that
is currently installed on the appliance. 

 Version Size  Released on      Downloaded Installed 
--------------------------------------------------- 
2-253   57MB 2014/09/20 20:00:08 PDT no         no 
2-39    44MB 2014/02/12 14:04:27 PST yes     current 

 If
the appliance cannot connect to the update server, you will need
to allow connectivity from the appliance to the Palo Alto Networks
Update Server (updates.paloaltonetworks.com), or download and install
the update using SCP as described in Install
WildFire Content Updates from an SCP-Enabled Server . 

 Download and install the latest content update. 

 Download the latest content update: 

 admin@WF-500> request wf-content upgrade download latest 

 View the status of the download: 

 admin@WF-500> show jobs all 

 You
can run show jobs pending to view pending
jobs. The following output shows that the download (job id 5) has
finished downloading (Status FIN): 

 Enqueued          ID  Type Status Result Completed 
--------------------------------------------------- 
2014/04/22 03:42:20  5  Downld  FIN   OK   03:42:23 

 After the download is complete, install the update: 

 admin@WF-500> request wf-content upgrade install version latest 

 Run
the show jobs all command again to monitor
the status of the install. 

 Verify the content update. 

 Run the following command and refer to the wf-content-version field: 

 admin@WF-500> show system info 

 The
following shows an example output with content update version 2-253
installed: 

 admin@WF-500> show system info 
hostname: WildFire 
ip-address: 10.5.164.245 
netmask: 255.255.255.0 
default-gateway: 10.5.164.1 
mac-address: 00:25:90:c3:ed:56 
vm-interface-ip-address: 192.168.2.2 
vm-interface-netmask: 255.255.255.0 
vm-interface-default-gateway: 192.168.2.1 
vm-interface-dns-server: 192.168.2.1 
time: Mon Apr 21 09:59:07 2014 
uptime: 17 days, 23:19:16 
family: m 
model: WildFire 
serial: abcd3333 
sw-version: 6.1.0 
 wf-content-version: 2-253 
wfm-release-date: 2014/08/20 20:00:08 
logdb-version: 6.1.2 
platform-family: m 

 Confirm that all services are running. 

 admin@WF-500> show system software status 

 ( Optional ) Schedule content updates to be installed
on a daily or weekly basis. 

 When setting a schedule for content updates on WildFire appliances
 enrolled in a cluster, it is advisable to schedule WildFire content
 updates at different times on all nodes to ensure efficient availability
 of the cluster for sample processing. 

 Schedule the appliance to download and install
content updates: 

 admin@WF-500# set deviceconfig system update-schedule wf-content recurring [daily | weekly] action [download-and-install | download-only] 

 For
example, to download and install updates daily at 8:00 am: 

 admin@WF-500# set deviceconfig system update-schedule wf-content recurring daily action download-and-install at 08:00 

 Commit the configuration 

 admin@WF-500# commit 

 Previous 

 Set Up WildFire Appliance Content Updates 

 Next 

 Install WildFire Content Updates from an SCP-Enabled Server 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 Panorama 

 VM-Series 

 SASE 

 Prisma Access 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Security Policy 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 10.1 

 11.0 

 Network Security 

 PAN-OS 

 10.2 

 WF-500-B Appliance 

 Advanced Wildfire 

 WF-500 Appliance 

 Appliance 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
