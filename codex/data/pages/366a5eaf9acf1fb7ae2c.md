---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/9-1/pan-os-new-features/upgrade-to-pan-os-91/upgrade-the-firewall-to-pan-os-91/determine-the-upgrade-path.html
fetched_at: 2026-09-16T10:53:16Z
source: palo-alto-main
---

# Determine the Upgrade Path to PAN-OS 9.1 Clear

Updated on 

 Aug 21, 2024 

 Focus 

 Home 

 PAN-OS 

 PAN-OS® New Features Guide 

 Upgrade to PAN-OS 9.1 

 Upgrade the Firewall to PAN-OS 9.1 

 Determine the Upgrade Path to PAN-OS 9.1 

 Download PDF 

 PAN-OS® New Features Guide 

 Determine the Upgrade Path to PAN-OS 9.1 

 Table of Contents 

 Filter

 Version 

 9.1 (EoL) 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 Upgrade to PAN-OS 9.1 

 Upgrade/Downgrade Considerations 

 Upgrade the Firewall to PAN-OS 9.1 

 Determine the Upgrade Path to PAN-OS 9.1 

 Upgrade Firewalls Using Panorama 

 Upgrade a Standalone Firewall to PAN-OS 9.1 

 Upgrade an HA Firewall Pair to PAN-OS 9.1 

 Downgrade from PAN-OS 9.1 

 Downgrade a Firewall to a Previous Maintenance Release 

 Downgrade a Firewall to a Previous Feature Release 

 Downgrade a Windows Agent from PAN-OS 9.1 

 SD-WAN Features 

 Secure SD-WAN 

 App-ID Features 

 Streamlined Application-Based Policy 

 Simplified Application Dependency Workflow 

 Panorama Features 

 Automatic Panorama Connection Recovery 

 Next-Generation Firewalls for Zero Touch Provisioning 

 User-ID Features 

 Include Username in HTTP Header Insertion Entries 

 Dynamic User Groups 

 GlobalProtect Features 

 Enhanced Logging for GlobalProtect 

 Virtualization Features 

 VM-Series Firewall on VMware NSX-T (East-West) 

 End-of-Life (EoL)

 Determine the Upgrade Path to PAN-OS 9.1 

 Upgrade path planning for PAN-OS 9.1. 

 When you upgrade from one PAN-OS feature release version to a later feature release, you cannot
 skip the installation of any feature release versions in the path to your target
 release. In addition, the recommended upgrade path includes installing the latest
 maintenance release in each release version before you download the base image for
 the next feature release version. To minimize downtime for your users, perform
 upgrades during non-business hours. 

 For manual upgrades, Palo Alto Networks recommends installing and upgrading from
 the latest maintenance release for each PAN-OS release along your upgrade path.
 Do not install the PAN-OS base image for a feature release unless it is the
 target release you want to upgrade to. 

 Determine
the upgrade path as follows: 

 Identify
which version is currently installed. 

 From Panorama, select Panorama Managed Devices and check the
Software Version on the firewalls you plan to upgrade. 

 From the firewall, select Device Software and check which version
has a check mark in the Currently Installed column. 

 Identify the upgrade path: 

 Review the known issues and changes
to default behavior in the Release Notes and upgrade/downgrade
considerations in the New Features Guide for
each release through which you pass as part of your upgrade path. 

 Installed PAN-OS Version Recommended Upgrade Path to PAN-OS 9.1 

 9.0.x 
 If you are already running
a PAN-OS 9.0 release, download and install the preferred PAN-OS 9.0 maintenance
release and reboot. You can then proceed to Upgrade the Firewall to PAN-OS 9.1 . 

 Review
the upgrade/downgrade considerations before upgrading
any Log Collectors to the latest PAN-OS 9.0 maintenance release. 

 8.1.x 

 Download
and install the latest preferred PAN-OS 8.1 maintenance
release and reboot. 

 Download PAN-OS 9.0.0 

 Download and install the latest preferred PAN-OS 9.0 maintenance
release and reboot. 

 Review the upgrade/downgrade considerations before
upgrading any Log Collectors to the latest PAN-OS 9.0 maintenance
release. 

 Proceed to Upgrade the Firewall to PAN-OS 9.1 . 

 8.0.x 
 Download
and install PAN-OS 8.0.20 and reboot. 

 Download PAN-OS 8.1.0 . 

 Download and install the latest preferred PAN-OS 8.1 maintenance
release and reboot. 

 Download PAN-OS 9.0.0 

 Download and install the latest preferred PAN-OS 9.0 maintenance
release and reboot. 

 Review the upgrade/downgrade considerations before
upgrading any Log Collectors to the latest PAN-OS 9.0 maintenance
release. 

 Proceed to Upgrade the Firewall to PAN-OS 9.1 . 

 7.1.x 
 Download and
install the PAN-OS 7.1.26 maintenance release and reboot. 

 Download PAN-OS 8.0.0 . 

 Download and install PAN-OS 8.0.20 and reboot. 

 Download PAN-OS 8.1.0 . 

 Download and install the latest preferred PAN-OS 8.1 maintenance
release and reboot. 

 Download PAN-OS 9.0.0 

 Download and install the latest preferred PAN-OS 9.0 maintenance
release and reboot. 

 Review the upgrade/downgrade considerations before
upgrading any Log Collectors to the latest PAN-OS 9.0 maintenance
release. 

 Proceed to Upgrade the Firewall to PAN-OS 9.1 . 

 Previous 

 Upgrade the Firewall to PAN-OS 9.1 

 Next 

 Upgrade Firewalls Using Panorama
