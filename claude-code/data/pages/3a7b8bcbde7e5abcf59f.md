---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-new-features/sd-wan-features/sd-wan-full-mesh-vpn-cluster-with-ddns-service.html
fetched_at: 2026-09-16T10:53:07Z
source: palo-alto-main
---

# SD-WAN Full Mesh VPN Cluster with DDNS Service Clear

Updated on 

 Aug 28, 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 SD-WAN Features 

 SD-WAN Full Mesh VPN Cluster with DDNS Service 

 Download PDF 

 PAN-OS ® New Features Guide 

 SD-WAN Full Mesh VPN Cluster with DDNS Service 

 Table of Contents 

 Filter

 Version 

 10.0 (EoL) 

 10.0 (EoL) 

 Expand all | Collapse all 

 Upgrade PAN-OS 

 Upgrade/Downgrade Considerations 

 Upgrade the Firewall to PAN-OS 10.0 

 Determine the Upgrade Path to PAN-OS 10.0 

 Upgrade Firewalls Using Panorama 

 Upgrade a Standalone Firewall 

 Upgrade an HA Firewall Pair 

 Downgrade PAN-OS 

 Downgrade a Firewall to a Previous Maintenance Release 

 Downgrade a Firewall to a Previous Feature Release 

 Downgrade a Windows Agent 

 Enterprise Data Loss Prevention Features 

 Enterprise Data Loss Prevention 

 SD-WAN Features 

 SD-WAN Remove Private AS 

 SD-WAN Full Mesh VPN Cluster with DDNS Service 

 SD-WAN DIA AnyPath 

 SaaS Application Path Monitoring 

 SD-WAN Forward Error Correction 

 SD-WAN Packet Duplication 

 IoT Security Features 

 IoT Security 

 Device-ID 

 Content Inspection Features 

 DNS Security Signature Categories 

 Enhanced Pattern-Matching Engine for Custom Signatures 

 IPS Signature Converter Plugin for Panorama 

 Expanded Data Collection for DNS Security Improvements 

 Decryption Features 

 Decryption for TLSv1.3 

 Block Export of Private Keys 

 Enhanced Decryption Troubleshooting 

 GlobalProtect Features 

 Identification and Quarantine of Compromised Devices 

 Enhanced Logging for the Selected GlobalProtect Gateway 

 Management Features 

 Millisecond Granularity for PAN-OS Log Forwarding 

 Visibility on Custom Threat Names 

 Proxy Support for Cortex Data Lake 

 External Dynamic List Log Fields 

 Additional Predefined Time Filters for the ACC, Monitoring, and Reports 

 Rule Usage Filtering Actions 

 Device Telemetry 

 Certificate Management Features 

 Master Key Encryption Enhancement 

 Panorama Features 

 Automatic Content Updates Through Offline Panorama 

 Enhanced Authentication for Dedicated Log Collectors and WildFire Appliances 

 Syslog Forwarding Using Ethernet Interfaces 

 Increased Configuration Size for Panorama 

 Access Domain Enhancements for Multi-Tenancy 

 Enhanced Performance for Panorama Query and Reporting 

 Log Query Debugging 

 Configurable Key Limits in Scheduled Reports 

 Multiple Plugin Support for Panorama 

 Networking Features 

 HA Clustering 

 HA Additional Path Monitoring Groups 

 Packet Buffer Protection Based on Latency 

 Ethernet SGT Protection 

 ECMP Strict Source Path 

 Tunnel Acceleration for GRE, VXLAN, and GTP-U Tunnels 

 Advanced Route Engine 

 Bonjour Reflector for Network Segmentation 

 Authentication Features 

 TLS Encryption for Email Server Profiles 

 Authentication Portal Exclusion for Predefined Domains 

 User-ID Features 

 Streamlined and Resilient Redistribution 

 Authentication with Custom Certificates for Redistribution 

 Policy Features 

 IP Range and Subnet Support in Dynamic Address Groups 

 X-Forwarded-For HTTP Header Data Support in Policy 

 URL Filtering Features 

 URL Filtering Inline ML 

 WildFire Features 

 WildFire Real-Time Signature Updates 

 IPv6 Address Support for the WildFire Appliance 

 Windows 10 Analysis Environment for the WildFire Appliance 

 WildFire Inline ML 

 Virtualization Features 

 Automatic Site License Activation on the PAYG VM-Series Firewalls 

 CN-Series Firewalls for Securing Kubernetes Deployments 

 Panorama Support for Multiple IP-Tag Sources 

 VMotion Support for the VM-Series Firewall on NSX-T and ESXi 

 Mobile Infrastructure Security Features 

 Network Slice Security in a 5G Network 

 Equipment ID Security in a 5G Network 

 Subscriber ID Security in a 5G Network 

 Equipment ID Security in a 4G Network 

 Subscriber ID Security in a 4G Network 

 End-of-Life (EoL)

 SD-WAN Full Mesh VPN Cluster with DDNS Service 

 High-level steps to create an SD-WAN VPN cluster that
is full mesh with DDNS Service. 

 SD-WAN supports a full mesh topology, in addition
to the hub-spoke topology. The mesh can consist of branches with
or without hubs. Use full mesh when the branches need to communicate
with each other directly. 

 If the branch firewall receives
a dynamic IP address, the firewall requires Dynamic DNS (DDNS) so
that a DDNS service can detect the public-facing IP address of the
firewall interface that is running SD-WAN. When you push the DDNS
setting to all firewalls, that notifies each firewall to register
its external interface IP address with the Palo Alto Networks DDNS
cloud service so that the IP address is converted to an FQDN. 

 DDNS
is also required because the CPE device from the ISP may be performing source
NAT. The DDNS service allows the firewall to register the public-facing
IP address with the DDNS server. When you have devices connect for
branch-to-branch mesh, Auto VPN contacts the DDNS service for those
firewalls to pull their public IP addresses that are registered
in the DDNS cloud and uses those public IP addresses to create the
IKE peering and the VPN tunnels. If the CPE device is performing
source NAT, when you add an SD-WAN branch device to
be managed by Panorama, you will enable Upstream NAT and
the NAT IP Address Type will be DDNS . 

 SD-WAN
full mesh with DDNS service requires the following: 

 PAN-OS
10.0.3 or a later 10.0 release 

 SD-WAN Plugin 2.0.1 or a later 2.0 release 

 ZTP Plugin 1.0.1 or a later 1.0 release that is downloaded,
installed, and configured in order to leverage the DDNS that is
associated with ZTP. Panorama must be ZTP-registered and communicating
with the ZTP Service. 

 All firewalls participating in full mesh DDNS must be registered
under the same Customer Support Portal account. 

 All firewalls participating in full mesh DDNS must have the
latest device certificate installed. 

 If you have a firewall or other network device that controls
outgoing traffic positioned in front of the Palo Alto Networks firewall,
you must change the configuration on that device to allow traffic
from the DDNS-enabled interfaces to the following FQDNs: 
 https://myip.ngfw-ztp.paloaltonetworks.com/      (to
reach whatsmyIP service) 

 https://ngfw-ztp.paloaltonetworks.com/              (to
reach DDNS registration service) 

 Install the latest device certificate for Panorama
and for all managed firewalls that are hubs or branches. 

 Install ZTP Plugin 1.0.1 to
set up Zero Touch Provisioning. 

 Install SD-WAN Plugin 2.0.1. 

 Commit on Panorama. 

 Log in to the Panorama Web Interface . 

 Create the VPN Address Pool as shown in Create a VPN Cluster . 

 Create the full mesh VPN cluster . 

 Commit and Commit to Panorama .
If your firewalls have static IP addresses, you are done. If your
branch or hub firewalls in a VPN mesh have DHCP or PPPoE interfaces, you
must use DDNS, so continue this procedure as follows. 

 Select Network Interfaces Ethernet and
in the Template field, select the Template-stack
for a particular branch. 

 Select the interface whose IP address indicates Dynamic-DHCP Client or PPPOE ,
click Override on the bottom of the screen,
and click OK to close. 

 Verify on Panorama that the DDNS
settings were configured . 

 If the VPN cluster includes any hubs that have a DHCP
or PPPoE interface, repeat Steps 9 through 11, but in the Template field,
select the Template-stack for a particular hub. 

 Commit to Panorama and Push to
Devices . 

 Verify on the branch firewall that the branch is configured
with DDNS. 

 Previous 

 SD-WAN Remove Private AS 

 Next 

 SD-WAN DIA AnyPath
