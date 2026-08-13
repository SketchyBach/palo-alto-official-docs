---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-upgrade/cli-commands-for-upgrade/use-cli-commands-for-upgrade-tasks
fetched_at: 2026-08-13T17:07:28Z
source: palo-alto-main
---

# Use CLI Commands for Upgrade Tasks Clear

Use CLI Commands for Upgrade Tasks 

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
 Use CLI Commands for Upgrade Tasks 

 Updated on 

 Mon Feb 10 20:35:14 PST 2025 

 Focus 

 Download PDF 

 Filter

 Version 

 10.2 

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

 Install a PAN-OS Software Patch 

 Install 

 Revert 

 Migrate Panorama Logs to the New Log Format 

 Upgrade Panorama for Increased Device Management Capacity 

 Upgrade Panorama and Managed Devices in FIPS-CC Mode 

 Downgrade from Panorama 10.2 

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

 Install a PAN-OS Software Patch 

 Install 

 Revert 

 Revert Content Updates from Panorama 

 Upgrade PAN-OS 

 PAN-OS Upgrade Checklist 

 Upgrade/Downgrade Considerations 

 Upgrade the Firewall to PAN-OS 10.2 

 Determine the Upgrade Path to PAN-OS 10.2 

 Upgrade Firewalls Using Panorama 

 Upgrade a Standalone Firewall 

 Upgrade an HA Firewall Pair 

 Upgrade the Firewall to PAN-OS 10.2 from Panorama 

 Upgrade Firewalls When Panorama Is Internet-Connected 

 Upgrade Firewalls When Panorama Is Not Internet-Connected 

 Upgrade a ZTP Firewall 

 Install a PAN-OS Software Patch 

 Install 

 Revert 

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

 Mon Feb 10 20:35:14 PST 2025 

 Focus 

 Home 

 PAN-OS 

 PAN-OS Upgrade Guide 

 CLI Commands for Upgrade 

 Use CLI Commands for Upgrade Tasks 

 Download PDF 

 PAN-OS Upgrade Guide 

 Use CLI Commands for Upgrade Tasks 

 Table of Contents 

 Filter

 Version 

 10.2 

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

 Install a PAN-OS Software Patch 

 Install 

 Revert 

 Migrate Panorama Logs to the New Log Format 

 Upgrade Panorama for Increased Device Management Capacity 

 Upgrade Panorama and Managed Devices in FIPS-CC Mode 

 Downgrade from Panorama 10.2 

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

 Install a PAN-OS Software Patch 

 Install 

 Revert 

 Revert Content Updates from Panorama 

 Upgrade PAN-OS 

 PAN-OS Upgrade Checklist 

 Upgrade/Downgrade Considerations 

 Upgrade the Firewall to PAN-OS 10.2 

 Determine the Upgrade Path to PAN-OS 10.2 

 Upgrade Firewalls Using Panorama 

 Upgrade a Standalone Firewall 

 Upgrade an HA Firewall Pair 

 Upgrade the Firewall to PAN-OS 10.2 from Panorama 

 Upgrade Firewalls When Panorama Is Internet-Connected 

 Upgrade Firewalls When Panorama Is Not Internet-Connected 

 Upgrade a ZTP Firewall 

 Install a PAN-OS Software Patch 

 Install 

 Revert 

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

 Use CLI Commands for Upgrade Tasks 

 CLI commands for upgrading PAN-OS. 

 Use the following CLI commands to carry out
upgrade tasks. 

 If you want to... 

 Use... 

 Check the current versions
of the firewall 

 Check the current version of
the firewall software and content. 

 show system info 

 Access the available dynamic
updates and upgrade the content version of the firewall 

 Check available content versions
of dynamic updates directly from the Palo Alto Networks servers. 

 request content upgrade check 

 Check available content versions
of dynamic updates directly from the firewall. 

 request content upgrade info 

 Download content version directly
to the firewall. 

 request content upgrade download <content version> 

 Install content version. 

 request content upgrade install <content version> 

 Access the available software
versions and upgrade the firewall 

 Check the available
software versions available for download. 

 request system software info 

 Check the preferred releases of a software. 

 ( PAN-OS 10.2.10 and later 10.2 releases ) 

 request system software info preferred 

 Check the base releases of a software. 

 ( PAN-OS 10.2.10 and later 10.2 releases ) 

 request system software info base 

 Check both preferred and base releases of a software. 

 ( PAN-OS 10.2.10 and later 10.2 releases ) 

 request system software info preferred base 

 Check the available versions
loaded on the firewall. 

 request system software check 

 Download a specific version
of the software. 

 request system software download version <version> 

 Check the status of
a specific download job. 

 Show job id <jobid> 

 Install the downloaded software. 

 request system software install version 10.1.0 

 Restart the firewall. 

 request restart system 

 Access the available software patches
for the firewall: 

 The
patch feature is currently offered in preview mode. Full support
is not available with this functionality. 

 If you want to... 

 Use... 

 Check
the available software patches available for download. 

 request system patch check 

 Check
the available patches for the currently installed firewall version. 

 request system patch info 

 Download
a specific patch version. 

 request system patch download version <version> 

 Check
more detailed information for a specific patch version. 

 request system patch info version <version> 

 Install
the downloaded patch. 

 request system patch install version <version> 

 Apply the
installed patch. 

 request system patch apply 

 Previous 

 CLI Commands for Upgrade 

 Next 

 APIs for Upgrade 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
