---
url: https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-upgrade/upgrade-panorama/install-content-and-software-updates-for-panorama/install-updates-for-panorama-with-ha-configuration
fetched_at: 2026-08-13T17:08:15Z
source: palo-alto-main
---

# Upgrade Panorama in an HA Configuration Clear

Upgrade Panorama in an HA Configuration 

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
 Upgrade Panorama in an HA Configuration 

 Updated on 

 Dec 3, 2024 

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

 Dec 3, 2024 

 Focus 

 Home 

 PAN-OS 

 PAN-OS Upgrade Guide 

 Upgrade Panorama 

 Install Content Updates and Software Upgrades for Panorama 

 Upgrade Panorama in an HA Configuration 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 PAN-OS Upgrade Guide 

 Upgrade Panorama in an HA Configuration 

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

 Upgrade Panorama in an HA Configuration 

 To ensure a seamless failover when you update
the Panorama software in a high availability (HA) configuration,
the active and passive Panorama peers must be running the same Panorama
release with the same Applications database version. The following
example describes how to upgrade an HA pair (active peer is Primary_A
and passive peer is Secondary_B). 

 If you are upgrading Panorama
and managed devices in FIPS-CC mode to PAN-OS 11.0 from PAN-OS 10.2
or earlier release, you must take the additional steps of resetting
the secure connection status of the devices in FIPS-CC mode if added
to Panorama management while running a PAN-OS 10.2 release. See Upgrade Panorama and Managed Devices in FIPS-CC Mode for more details
on upgrading Panorama and FIPS-CC devices in FIPS-CC mode. 

 Before
updating Panorama, refer to the Release Notes for the minimum
content release version required for PAN-OS 11.0. 

 Upgrade the Panorama software on the Secondary_B (passive)
peer. 

 Perform one of the following tasks on the Secondary_B peer: 

 Upgrade Panorama with an Internet Connection 

 Upgrade Panorama Without an Internet Connection 

 After
the upgrade, this Panorama transitions to a non-functional state
because the peers are no longer running the same software release. 

 ( Panorama Interconnect plugin only ) Synchronize the Panorama Node with the
 Panorama Controller . 

 Before you begin upgrading a Panorama Node, you must synchronize the Panorama
 Controller and Panorama Node configuration. This is required to successfully
 push the common Panorama Controller
 configuration to your Panorama Node after successful upgrade. 

 ( Best Practices ) If you are leveraging Cortex
Data Lake (CDL), install the Panorama device certificate on
each Panorama HA peer. 

 Panorama automatically switches to using the device certificate
for authentication with CDL ingestion and query endpoints on upgrade
to PAN-OS 11.0. 

 If you do not install the device certificate
prior to upgrade to PAN-OS 11.0, Panorama continues to use the existing
logging service certificates for authentication. 

 Suspend the Primary_A peer to force a failover. 

 Before you suspend the active-primary peer to force a failover,
 verify that both HA peers are fully synchronized across all HA checks
 and all status indicators are green. Resolve any issues highlighted in
 red and ensure that the status turns green before proceeding with the
 suspension. 

 On the Primary_A peer: 

 In the Operational Commands section ( Panorama High Availability ), Suspend
local Panorama . 

 Verify that state is suspended (displayed
on bottom-right corner of the web interface). 

 The resulting failover should cause the Secondary_B peer
to transition to active state. 

 Upgrade the Panorama software on the Primary_A (currently passive)
peer. 

 Perform one of the following tasks on the Primary_A peer: 

 Upgrade Panorama with an Internet Connection 

 Upgrade Panorama Without an Internet Connection 

 After
you reboot, the Primary_A peer is initially still in the passive
state. Then, if preemption is enabled (default), the Primary_A peer
automatically transitions to the active state and the Secondary_B
peer reverts to the passive state. 

 If you disabled preemption,
manually Restore the Primary Panorama
to the Active State . 

 Verify that both peers are now running any newly installed content
release versions and the newly installed Panorama release. 

 On the Dashboard of each Panorama
peer, check the Panorama Software Version and Application Version
and confirm that they are the same on both peers and that the running
configuration is synchronized. 

 ( Local Log Collectors in a Collector Group only )
Upgrade the remaining Log Collectors in the Collector Group. 

 Upgrade Log Collectors When Panorama Is Internet-Connected 

 Upgrade Log Collectors When Panorama Is Not Internet-Connected 

 ( Recommended for Panorama mode ) Increase the memory of the Panorama virtual
 appliance to 64GB. 

 After you successfully upgrade the Panorama virtual appliance in Panorama
 mode to PAN-OS 11.0, Palo Alto Networks recommends increasing the memory of
 the Panorama virtual appliance to 64GB to meet the increased system requirements to
 avoid any logging, management, and operational performance issues related to
 an under-provisioned Panorama virtual appliance. 

 Select Commit Commit and Push and Commit and Push the Panorama managed
 configuration to all managed devices. 

 After you successfully upgrade Panorama and managed devices to PAN-OS 11.0, a
 full commit and push of the Panorama managed configuration is required
 before you can push selective configuration to your
 managed devices and leverage the improved shared configuration
 object management for multi-vsys firewalls managed by Panorama. 

 ( Panorama and managed devices in FIPS-CC mode ) Upgrade Panorama and Managed Devices in FIPS-CC Mode . 

 Upgrading Panorama and managed devices in FIPS-CC mode
requires you to reset the secure connection status of the devices
in FIPS-CC mode if added to Panorama management while running a
PAN-OS 11.0 release. You need to re-onboard the following managed
devices to Panorama management: 

 Managed
devices in FIPS-CC mode added to Panorama using the device registration
authentication key. 

 Managed devices in the normal operational mode added to Panorama
using the device registration authentication key 
 You do
not need to re-onboard managed devices added to Panorama management while
the managed device was running a PAN-OS 10.0 or earlier release. 

 Regenerate or re-import all certificates to adhere to OpenSSL Security Level
 2. 

 This step is required if you upgrade from PAN-OS 10.1 or earlier release to
 PAN-OS 11.0. Skip this step if you upgrade from PAN-OS 10.2 and have already
 regenerated or re-imported your certificates. 

 It is required that all certificates meet the following minimum
 requirements: 

 RSA 2048 bits or greater, or ECDSA 256 bits or greater 

 Digest of SHA256 or greater 

 See the PAN-OS Administrator's Guide or
 Panorama Administrator's Guide for
 more information on regenerating or re-importing your certificates. 

 Previous 

 Install Content Updates Automatically for Panorama without an Internet Connection 

 Next 

 Migrate Panorama Logs to the New Log Format 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
