---
url: https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-upgrade/upgrade-panorama/deploy-updates-to-firewalls-log-collectors-and-wildfire-appliances-using-panorama/panorama-log-collector-firewall-and-wildfire-version-compatibility
fetched_at: 2026-08-13T17:08:13Z
source: palo-alto-main
---

# Panorama, Log Collector, Firewall, and WildFire Version Compatibility Clear

Panorama, Log Collector, Firewall, and WildFire Version Compatibility 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PAN-OS Upgrade Guide 

 : 
 Panorama, Log Collector, Firewall, and WildFire Version Compatibility 

 Updated on 

 Tue Dec 03 08:21:27 PST 2024 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 End-of-Life (EoL)

 Filter

 Version 

 11.0 (EoL) 

 11.1 & Later 

 11.0 (EoL) 

 10.2 

 10.1 (EoL) 

 Expand all | Collapse all 

 Software and Content Updates 

 PAN-OS Software Updates 

 Dynamic Content Updates 

 Install Content Updates 

 Applications and Threats Content Updates 

 Deploy Applications and Threats Content Updates 

 Tips for Content Updates 

 Best Practices for Applications and Threats Content Updates 

 Best Practices for Content Updates—Mission-Critical 

 Best Practices for Content Updates—Security-First 

 Content Delivery Network Infrastructure 

 Upgrade Panorama 

 Install Content Updates and Software Upgrades for Panorama 

 Upgrade Panorama with an Internet Connection 

 Upgrade Panorama Without an Internet Connection 

 Install Content Updates Automatically for Panorama without an Internet Connection 

 Upgrade Panorama in an HA Configuration 

 Migrate Panorama Logs to the New Log Format 

 Upgrade Panorama for Increased Device Management Capacity 

 Upgrade Panorama and Managed Devices in FIPS-CC Mode 

 Downgrade from Panorama 11.0 

 Troubleshoot Your Panorama Upgrade 

 Deploy Upgrades to Firewalls, Log Collectors, and WildFire Appliances Using Panorama 

 What Updates Can Panorama Push to Other Devices? 

 Schedule a Content Update Using Panorama 

 Panorama, Log Collector, Firewall, and WildFire Version Compatibility 

 Upgrade Log Collectors When Panorama Is Internet-Connected 

 Upgrade Log Collectors When Panorama Is Not Internet-Connected 

 Upgrade a WildFire Cluster from Panorama with an Internet Connection 

 Upgrade a WildFire Cluster from Panorama without an Internet Connection 

 Upgrade Firewalls When Panorama Is Internet-Connected 

 Upgrade Firewalls When Panorama Is Not Internet-Connected 

 Upgrade a ZTP Firewall 

 Revert Content Updates from Panorama 

 Upgrade PAN-OS 

 PAN-OS Upgrade Checklist 

 Upgrade/Downgrade Considerations 

 Upgrade the Firewall to PAN-OS 11.0 

 Determine the Upgrade Path to PAN-OS 11.0 

 Upgrade a Standalone Firewall 

 Upgrade an HA Firewall Pair 

 Upgrade the Firewall to PAN-OS 11.0 from Panorama 

 Upgrade Firewalls When Panorama Is Internet-Connected 

 Upgrade Firewalls When Panorama Is Not Internet-Connected 

 Upgrade a ZTP Firewall 

 Downgrade PAN-OS 

 Downgrade a Firewall to a Previous Maintenance Release 

 Downgrade a Firewall to a Previous Feature Release 

 Downgrade a Windows Agent 

 Troubleshoot Your PAN-OS Upgrade 

 Upgrade the VM-Series Firewall 

 Upgrade the VM-Series PAN-OS Software (Standalone) 

 Upgrade the VM-Series PAN-OS Software (HA Pair) 

 Upgrade the VM-Series PAN-OS Software Using Panorama 

 Upgrade the PAN-OS Software Version (VM-Series for NSX) 

 Upgrade the VM-Series for NSX During a Maintenance Window 

 Upgrade the VM-Series for NSX Without Disrupting Traffic 

 Upgrade the VM-Series Model 

 Upgrade the VM-Series Model in an HA Pair 

 Downgrade a VM-Series Firewall to a Previous Release 

 Upgrade Panorama Plugins 

 Panorama Plugins Upgrade/Downgrade Considerations 

 Upgrade a Panorama Plugin 

 Upgrade the Enterprise DLP Plugin 

 Upgrade the Panorama Interconnect Plugin 

 Install/Upgrade SD-WAN Plugin with Compatible PAN-OS Release 

 Upgrade and Downgrade Paths for SD-WAN Plugin 

 Install the SD-WAN Plugin 

 Upgrade Panorama High Availability Pair (Active/Passive) Leveraging SD-WAN Plugin 

 Upgrade Standalone Panorama Leveraging SD-WAN Plugin 

 Changes to Note After Upgrade 

 CLI Commands for Upgrade 

 Use CLI Commands for Upgrade Tasks 

 APIs for Upgrade 

 Use the API for Upgrade Tasks 

 Updated on 

 Tue Dec 03 08:21:27 PST 2024 

 Focus 

 Home 

 PAN-OS 

 PAN-OS Upgrade Guide 

 Upgrade Panorama 

 Deploy Upgrades to Firewalls, Log Collectors, and WildFire
Appliances Using Panorama 

 Panorama, Log Collector, Firewall, and WildFire Version Compatibility 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 PAN-OS Upgrade Guide 

 Panorama, Log Collector, Firewall, and WildFire Version Compatibility 

 Table of Contents 

 Filter

 Version 

 11.0 (EoL) 

 11.1 & Later 

 11.0 (EoL) 

 10.2 

 10.1 (EoL) 

 Expand all | Collapse all 

 Software and Content Updates 

 PAN-OS Software Updates 

 Dynamic Content Updates 

 Install Content Updates 

 Applications and Threats Content Updates 

 Deploy Applications and Threats Content Updates 

 Tips for Content Updates 

 Best Practices for Applications and Threats Content Updates 

 Best Practices for Content Updates—Mission-Critical 

 Best Practices for Content Updates—Security-First 

 Content Delivery Network Infrastructure 

 Upgrade Panorama 

 Install Content Updates and Software Upgrades for Panorama 

 Upgrade Panorama with an Internet Connection 

 Upgrade Panorama Without an Internet Connection 

 Install Content Updates Automatically for Panorama without an Internet Connection 

 Upgrade Panorama in an HA Configuration 

 Migrate Panorama Logs to the New Log Format 

 Upgrade Panorama for Increased Device Management Capacity 

 Upgrade Panorama and Managed Devices in FIPS-CC Mode 

 Downgrade from Panorama 11.0 

 Troubleshoot Your Panorama Upgrade 

 Deploy Upgrades to Firewalls, Log Collectors, and WildFire Appliances Using Panorama 

 What Updates Can Panorama Push to Other Devices? 

 Schedule a Content Update Using Panorama 

 Panorama, Log Collector, Firewall, and WildFire Version Compatibility 

 Upgrade Log Collectors When Panorama Is Internet-Connected 

 Upgrade Log Collectors When Panorama Is Not Internet-Connected 

 Upgrade a WildFire Cluster from Panorama with an Internet Connection 

 Upgrade a WildFire Cluster from Panorama without an Internet Connection 

 Upgrade Firewalls When Panorama Is Internet-Connected 

 Upgrade Firewalls When Panorama Is Not Internet-Connected 

 Upgrade a ZTP Firewall 

 Revert Content Updates from Panorama 

 Upgrade PAN-OS 

 PAN-OS Upgrade Checklist 

 Upgrade/Downgrade Considerations 

 Upgrade the Firewall to PAN-OS 11.0 

 Determine the Upgrade Path to PAN-OS 11.0 

 Upgrade a Standalone Firewall 

 Upgrade an HA Firewall Pair 

 Upgrade the Firewall to PAN-OS 11.0 from Panorama 

 Upgrade Firewalls When Panorama Is Internet-Connected 

 Upgrade Firewalls When Panorama Is Not Internet-Connected 

 Upgrade a ZTP Firewall 

 Downgrade PAN-OS 

 Downgrade a Firewall to a Previous Maintenance Release 

 Downgrade a Firewall to a Previous Feature Release 

 Downgrade a Windows Agent 

 Troubleshoot Your PAN-OS Upgrade 

 Upgrade the VM-Series Firewall 

 Upgrade the VM-Series PAN-OS Software (Standalone) 

 Upgrade the VM-Series PAN-OS Software (HA Pair) 

 Upgrade the VM-Series PAN-OS Software Using Panorama 

 Upgrade the PAN-OS Software Version (VM-Series for NSX) 

 Upgrade the VM-Series for NSX During a Maintenance Window 

 Upgrade the VM-Series for NSX Without Disrupting Traffic 

 Upgrade the VM-Series Model 

 Upgrade the VM-Series Model in an HA Pair 

 Downgrade a VM-Series Firewall to a Previous Release 

 Upgrade Panorama Plugins 

 Panorama Plugins Upgrade/Downgrade Considerations 

 Upgrade a Panorama Plugin 

 Upgrade the Enterprise DLP Plugin 

 Upgrade the Panorama Interconnect Plugin 

 Install/Upgrade SD-WAN Plugin with Compatible PAN-OS Release 

 Upgrade and Downgrade Paths for SD-WAN Plugin 

 Install the SD-WAN Plugin 

 Upgrade Panorama High Availability Pair (Active/Passive) Leveraging SD-WAN Plugin 

 Upgrade Standalone Panorama Leveraging SD-WAN Plugin 

 Changes to Note After Upgrade 

 CLI Commands for Upgrade 

 Use CLI Commands for Upgrade Tasks 

 APIs for Upgrade 

 Use the API for Upgrade Tasks 

 End-of-Life (EoL)

 Panorama, Log Collector, Firewall, and WildFire Version Compatibility 

 PAN-OS® 11.0 version compatibility for Panorama™, Log
Collectors, firewalls, and WildFire®. 

 For best results, adhere to the following Panorama™
compatibility guidelines: 

 Install the same Panorama release on both the Panorama management server and the
 Dedicated Log Collectors. 

 Panorama must be running the same or a later PAN-OS version than the firewall it
 manages. See Panorama Management Compatibility for
 more information. 

 Before upgrading firewalls to PAN-OS 11.0, you must first upgrade Panorama to
 11.0. 

 Dedicated Log Collectors must be running the same or later PAN-OS version than
 the managed firewalls forwarding logs. 

 Panorama running PAN-OS 11.0 can manage WildFire® appliances and WildFire
 appliance clusters that are running the same or an earlier PAN-OS release.
 See Panorama Management Compatibility for
 more information. 

 It is recommended that the Panorama management server, Wildfire appliances, and
 Wildfire appliance clusters run the same PAN-OS release. 

 The content release version on the Panorama management server must be the same
 (or earlier) version as the content release version on any Dedicated Log
 Collectors or managed firewalls. See Panorama Management Compatibility for
 more information. 

 Palo Alto Networks® recommends installing the same Applications database
 version on Panorama as on the Dedicated Log Collectors and firewalls. 

 Regardless whether your subscriptions include the Applications database or
 Applications and Threats database, Panorama installs only the Applications
 database. Panorama and Dedicated Log Collectors do not enforce policy rules so
 they do not need the threat signatures from the Threats database. The
 Applications database contains threat metadata (such as threat IDs and names)
 that you use on Panorama and Dedicated Log Collectors when defining policy rules
 to push to managed firewalls and when interpreting threat information in logs
 and reports. However, firewalls require the full Applications and Threats
 database to match the identifiers recorded in logs with the corresponding
 threat, URL, or application names. Refer to the Release Notes for the minimum content
 release version required for a Panorama release. 

 Previous 

 Schedule a Content Update Using Panorama 

 Next 

 Upgrade Log Collectors When Panorama Is Internet-Connected 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
