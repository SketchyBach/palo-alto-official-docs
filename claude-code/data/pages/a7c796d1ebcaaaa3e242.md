---
url: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-release-notes/pan-os-9-1-addressed-issues/pan-os-9-1-16-addressed-issues
fetched_at: 2026-08-13T17:14:13Z
source: palo-alto-main
---

# PAN-OS 9.1.16 Addressed Issues Clear

PAN-OS 9.1.16 Addressed Issues 

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

 PAN-OS 9.1.16 Addressed Issues 

 Updated on 

 Tue Jul 22 10:17:59 PDT 2025 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 Updated on 

 Tue Jul 22 10:17:59 PDT 2025 

 Focus 

 Home 

 PAN-OS 

 PAN-OS 9.1 Addressed Issues 

 PAN-OS 9.1.16 Addressed Issues 

 Download PDF 

 PAN-OS 9.1.16 Addressed Issues 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 End-of-Life (EoL)

 Previous 

 PAN-OS 9-1-16-h3 Addressed Issues 

 Next 

 PAN-OS 9.1.15-h1 Addressed Issues 

 PAN-OS 9.1.16 Addressed Issues 

 PAN-OS® 9.1.16 addressed issues. 

 Issue ID 

 Description 

 PAN-235168 

 Fixed an issue where disk space became full even after clearing old
 logs and content images. 

 PAN-216656 

 Fixed an issue where the firewall was unable to fully process the user list from a child group when the child group contained more than 1,500 users. 

 PAN-215911 

 Fixed an issue that resulted in a race condition, which caused the configd process to stop responding. 

 PAN-215488 

 Fixed an issue where an expired Trusted Root CA was used to sign the forward proxy leaf certificate during SSL Decryption. 

 PAN-211997 

 Fixed an issue where large OSPF control packets were fragmented, which caused the neighborship to fail. 

 PAN-211602 

 Fixed an issue where, when viewing a WildFire Analysis Report via the web interface, the detailed log view was not accessible if the browser window was resized. 

 PAN-209696 

 Fixed an issue where link-local address communication for IPv6, BFD, and OSPFv3 neighbors was dropped when IP address spoofing check was enabled in a Zone Protection profile. 

 PAN-207740 

 Fixed an issue that resulted in a race condition, which caused the configd process to stop responding. 

 PAN-205453 

 Fixed an issue where running reports or queries under a user group caused the reportd process to stop responding. 

 PAN-203563 

 Fixed an issue with Content and Threat Detection allocation storage space where performing a commit failed with a CUSTOM_UPDATE_BLOCK error message. 

 PAN-203402 

 Fixed an intermittent issue where forward session installs were delayed, which resulted in latencies. 

 PAN-203147 

 ( Firewalls in FIPS-CC mode only ) Fixed an issue where the firewall unexpectedly rebooted when downloading a new PAN-OS software image. 

 PAN-201910 

 PAN-OS security profiles might consume a large amount of memory depending on the profile configuration and quantity. In some cases, this might reduce the number of supported security profiles below the stated maximum for a given platform. 

 PAN-201639 

 Fixed an issue with Saas Application Usage reports where Applications with Risky Characteristics displayed only two applications per section. 

 PAN-199612 

 Fixed a sync issue with firewalls in active/active HA configurations. 

 PAN-198871 

 Fixed an issue when both URL and Advanced URL licenses were installed, the expiry date was not correctly checked. 

 PAN-198693 

 Fixed an issue where decrypted SSH sessions were interrupted with a decryption error. 

 PAN-198038 

 A CLI command was added to address an issue where long-lived sessions were aging out even when there was ongoing traffic. 

 PAN-197919 

 Fixed an issue where, when path monitoring for a static route was configured with a new Ping Interval value, the value was not used as intended. 

 PAN-197847 

 Fixed an issue where disabling the enc-algo-aes-128-gcm cipher did not work when using an SSL/TLS profile. 

 PAN-197729 

 Fixed an issue where repeated configuration pushes from Panorama resulted in a management server memory leak. 

 PAN-197576 

 Fixed an issue where commits pushed from Panorama caused a memory leak related to the mgmtsrvr process. 

 PAN-197219 

 Fixed an issue where the following error message was not sent from multi-factor authentication
 PingID and did not display in the browser: Your
 company has enhanced its VPN authentication with PingID. Please
 install the PingID app for iOS or Android, and use pairing
 key:<key>. To connect, type
 "ok" . 

 PAN-195790 

 Fixed an issue where syslog traffic that was sent from the management interface to the syslog server even when a destination IP address service route was configured. 

 PAN-195583 

 Fixed an issue where, after renaming an object, configuration pushes from Panorama failed with the commit error object name is not an allowed keyword . 

 PAN-194175 

 Fixed an issue on Panorama where a commit push to managed firewalls failed when objects were added as source address exclusions in a Security policy and Share Unused Address and Service Objects with Devices was unchecked. 

 PAN-193808 

 Fixed a memory leak issue in the mgmtsrvr process that resulted in an OOM condition. 

 PAN-193763 

 Fixed an issue on the firewall where the dataplane CPU spiked, which caused traffic to be affected during commits or content updates. 

 PAN-192681 

 Fixed an issue where HIP database storage on the firewall reached full capacity due to the firewall not purging older HIP reports. 

 PAN-190950 

 Fixed an issue where creating or modifying a GlobalProtect portal configuration failed in FIPS mode with the following error message: clientless-vpn enc-algo-rc4 unexpected here . 

 PAN-189518 

 Fixed an issue where incoming DNS packets with looped compression pointers caused the dnsproxyd process to stop responding. 

 PAN-189379 

 Fixed an issue where FQDN based Security policy rules did not match correctly. 

 PAN-187829 

 Fixed an issue where the web_backend and httpd processes leaked descriptors, which caused activities that depended on the processes, such as logging in to the web interface, to fail. 

 PAN-187761 

 Fixed an issue where, during HA failover, the newly passive firewall continued to pass traffic after the active firewall had already taken over. 

 PAN-184537 

 Fixed an issue where GlobalProtect requested for passwords that contained non ASCII characters (ö) to be reentered when refreshing the connection. 

 PAN-183319 

 Fixed an issue on Panorama where commits remained at 99% due to multiple firewalls sending out CSR singing requests every 10 minutes. 

 PAN-183297 

 Fixed an issue where, when the firewall received a large amount of
 user information, the firewall was unable to output IP-address to
 username mapping information via XML API. 

 PAN-183126 

 Fixed an issue on Panorama where you were able to attempt to push a number of active schedules to the firewall that was greater than the firewall's maximum capacity. 

 PAN-182845 

 Fixed an issue that caused devices to be removed from Panorama when one device was added by one user, but a Commit and Push operation was completed by a second user before the first user completed a Commit of the added device change. 

 PAN-181839 

 Fixed an issue where Panorama Global Search reported No Matches found while still returning results for matching entries on large configurations. 

 PAN-181759 

 ( Firewalls in active/active HA configurations only ) Fixed an issue where firewall configuration files were not synced. 

 PAN-181295 

 Fixed an issue where clicking on a rule in the App Dependency tab after a commit or commit all did not display the rule correctly. 

 PAN-179624 

 Fixed an issue where setting the password complexity to Require Password Change on First Login caused the user to be prompted with certificate authentication. 

 PAN-177942 

 Fixed an issue where, when grouping HA peers, access domains that were configured using multi-vsys firewalls deselected devices or virtual systems that were in other configured access domains. 

 PAN-177054 

 Fixed an issue where, when you disabled a NAT rule, the Destination Translation value none displayed in blue and was still able to be modified to a different value. 

 PAN-175176 

 Fixed an issue in which CBC ciphers for TLS traffic to port 28443 on Panorama were enabled. 

 PAN-174680 

 Fixed an issue where, when adding new configurations, Panorama didn't display a list of suggested template variables when typing in a relevant field. 

 PAN-173179 

 Fixed an issue where the rem_addr field in Terminal Access Controller Access-Control System (TACACS+) authentication displayed the management or service route IP address of the firewall instead of the source IP address of the user. 

 PAN-161958 

 Fixed an issue where the FQDN refresh timer was pushed from Panorama appliances on PAN-OS 9.0 and later releases to firewalls running a PAN-OS 8.1 release. 

 PAN-158511 

 Fixed an issue where configurations loaded and committed to Panorama changed external dynamic list references on Security policy rules to NONE when Antivirus Protection was not installed. 

 PAN-143930 

 Fixed an issue where a process ( routed ) restarted due to the number of BGP peers exceeding the supported configuration. 

 PAN-78762 

 Fixed an issue where you were unable to reset a VPN tunnel via the firewall web interface ( Network > IPSec Tunnels > Tunnel Info > Restart ). 

 Previous 

 PAN-OS 9-1-16-h3 Addressed Issues 

 Next 

 PAN-OS 9.1.15-h1 Addressed Issues 

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

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

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

 Shared Policy for NGFWs and Prisma Access 

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

 PAN-OS 

 Next-Generation Firewall 

 9.1 (EoL) 

 Panorama 

 Network Security 

 VM-Series 

 Advanced Wildfire 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
