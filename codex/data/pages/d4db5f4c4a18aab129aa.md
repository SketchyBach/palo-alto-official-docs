---
url: https://docs.paloaltonetworks.com/globalprotect/release-notes/6-3/known-issues-related-to-gp-app/globalprotect-6-3-3-h2-linux-known-issues
fetched_at: 2026-09-15T15:14:12Z
source: palo-alto-main
---

# GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues Clear

Updated on 

 Sep 1, 2026 

 Focus 

 Home 

 GlobalProtect 

 GlobalProtect™ App Release Notes 

 Known Issues 

 GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

 Download PDF 

 GlobalProtect 

 GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

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

 GlobalProtect 6.3.3-h11 (6.3.3-c1016) Windows and macOS (Preferred) Known Issues 

 Next 

 GlobalProtect 6.3.3-h9 (6.3.3-c999) Windows and macOS Known Issues 

 GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

 The following table lists the issues addressed in GlobalProtect app 6.3.3-h2 (6.3.3-c42)
 Linux. 

 Issue ID 

 Description 

 GPC-25973 

 After uninstalling the GlobalProtect agent from a Red Hat Enterprise
 Linux 9.6 system, the `gpd0` virtual interface remains listed as an
 unmanaged interface when using the `nmcli` command. Additionally,
 configuration files related to the `gpd0` interface are not removed
 from the `/etc/NetworkManager/conf.d` directory. DNS and interface
 configurations previously set by GlobalProtect may also persist in
 `nmcli`, `systemd-resolved` settings, and the `/etc/resolv.conf`
 file. This persistence does not cause any functional impact on
 network operations. 

 GPC-26289 

 After a fresh installation of the GlobalProtect client on Fedora 43
 with GNOME (Wayland), the GlobalProtect icon does not automatically
 appear in the system tray. Users must manually launch the
 GlobalProtect user interface by searching for "GlobalProtect" in the
 Applications menu or by running the `globalprotect launch-ui`
 command. The icon appears correctly in the system tray after a
 system reboot. 

 GPC-26290 

 When Direct Local Subnet Access (DLSA) is disabled, traffic between
 devices on the same local subnet does not route through the VPN
 tunnel as expected. Instead, this traffic attempts to route directly
 via the physical interface, which can lead to connection failures.
 This issue affects all Linux platforms, including RHEL, Ubuntu, and
 Fedora. 

 GPC-26293 

 When installing GlobalProtect on Ubuntu using a custom installation
 path, the installation process does not complete successfully. 

 Previous 

 GlobalProtect 6.3.3-h11 (6.3.3-c1016) Windows and macOS (Preferred) Known Issues 

 Next 

 GlobalProtect 6.3.3-h9 (6.3.3-c999) Windows and macOS Known Issues
