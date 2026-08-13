---
url: https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-upgrade/upgrade-the-vm-series-firewall/upgrade-the-vm-series-nsx-pan-os-software/upgrade-the-vm-series-for-nsx-during-a-maintenance-window
fetched_at: 2026-08-13T17:08:18Z
source: palo-alto-main
---

# Upgrade the VM-Series for NSX During a Maintenance Window Clear

Upgrade the VM-Series for NSX During a Maintenance Window 

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
 Upgrade the VM-Series for NSX During a Maintenance Window 

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

 Upgrade the VM-Series Firewall 

 Upgrade the PAN-OS Software Version (VM-Series for NSX) 

 Upgrade the VM-Series for NSX During a Maintenance Window 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 PAN-OS Upgrade Guide 

 Upgrade the VM-Series for NSX During a Maintenance Window 

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

 Upgrade the VM-Series for NSX During a Maintenance Window 

 Use Panorama to upgrade the VM-Series firewall NSX edition
during a maintenance window. 

 For
the VM-Series Firewall NSX edition, use Panorama to upgrade the
software version on the firewalls. 

 Review the VM-Series for VMware NSX upgrade paths . 

 Allocate additional hardware resources to your VM-Series
firewall. 

 Verify that enough hardware resources are available to
the VM-Series firewall. Refer to the VM-Series System Requirements to
see the new resource requirements for each VM-Series model. Allocate
additional hardware resources before continuing the upgrade process.
The process for assigning additional hardware resources differs
on each hypervisor. 

 Save a backup of the current configuration file on each
managed firewall that you plan to upgrade. 

 Although the firewall will automatically
create a backup of the configuration, it is a best practice to create
a backup prior to upgrade and store it externally. 

 Select Device Setup Operations and
click Export Panorama and devices config bundle .
This option is used to manually generate and export the latest version
of the configuration backup of Panorama and of each managed device. 

 Save the exported file to a location external to the
firewall. You can use this backup to restore the configuration if
you have problems with the upgrade. 

 Check the Release Notes to verify the Content Release
version required for the PAN-OS version. 

 The firewalls you plan to upgrade must be running the Content
Release version required for the PAN-OS version. 

 Select Panorama Device Deployment Dynamic Updates . 

 Check for the latest updates. Click Check Now (located
in the lower left-hand corner of the window) to check for the latest updates.
The link in the Action column indicates whether an update is available.
If a version is available, the Download link displays. 

 Click Download to download
a selected version. After successful download, the link in the Action column
changes from Download to Install . 

 Click Install and select the
devices on which you want to install the update. When the installation completes,
a check mark displays in the Currently Installed column. 

 Deploy software updates to selected firewalls. 

 If your firewalls are configured in HA, make sure
to clear the Group HA Peers check box and
upgrade one HA peer at a time. 

 Select Panorama Device Deployment Software . 

 Check for the latest updates. Click Check
Now (located in the lower left-hand corner of the window)
to check for the latest updates. The link in the Action column
indicates whether an update is available. 

 ( PAN-OS 11.0.5 and later 11.0 releases ) By default, the
 preferred releases and the corresponding base releases are
 displayed. To view the preferred releases only, disable (clear) the
 Base Releases checkbox. Similarly, to
 view the base releases only, disable (clear) the
 Preferred Releases checkbox. 

 Review the File Name and click Download .
Verify that the software versions that you download match the firewall
models deployed on your network. After successful download, the
link in the Action column changes from Download to Install . 

 Click Install and select the
devices on which you want to install the software version. 

 Select Reboot device after install ,
and click OK . 

 If you have devices configured in HA, clear the Group
HA Peers check box and upgrade one HA peer at a time. 

 Verify the software and Content Release version running
on each managed device. 

 Select Panorama Managed Devices . 

 Locate the device(s) and review the content and software
versions on the table. 

 Previous 

 Upgrade the PAN-OS Software Version (VM-Series for NSX) 

 Next 

 Upgrade the VM-Series for NSX Without Disrupting Traffic 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
