---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-new-features/networking-features/ha-clustering.html
fetched_at: 2026-09-16T10:53:11Z
source: palo-alto-main
---

# HA Clustering Clear

Updated on 

 Aug 28, 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 Networking Features 

 HA Clustering 

 Download PDF 

 PAN-OS ® New Features Guide 

 HA Clustering 

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

 HA Clustering 

 Configure HA clustering on up to 16 firewalls to protect
against failure of data center communications or to achieve horizontal
scaling. 

 A number of Palo Alto Networks ® firewall
models now support session state synchronization among firewalls
in a high availability (HA) cluster of up to 16 firewalls. The HA
cluster peers synchronize sessions to protect against failure of
the data center or a large security inspection point with horizontally
scaled firewalls. In the case of a network outage or a firewall
going down, the sessions fail over to a different firewall in the
cluster. 

 HA clusters support a Layer 3 or virtual wire deployment.
HA peers in the cluster can be a combination of HA pairs and standalone
cluster members. All cluster members share session state. When a
new firewall joins an HA cluster, that triggers all firewalls in
the cluster to synchronize all existing sessions. The new, required
HA4 and HA4 backup connections are the dedicated cluster links that
synchronize session state among all cluster members having the same
cluster ID. The HA4 link between cluster members detects connectivity
failures between cluster members. 

 The firewall models that
support HA clustering and the maximum number of members supported
per cluster are as follows: 

 Firewall Model Number of Members Supported Per Cluster 

 PA-3200 Series 

 6 

 PA-5200 Series 

 16 

 PA-7000 Series firewalls that have at least
one of the following cards: PA-7000-100G-NPC, PA-7000-20GQXM-NPC, PA-7000-20GXM-NPC 

 PA-7080: 4 

 PA-7050: 6 

 VM-300 

 6 

 VM-500 

 6 

 VM-700 

 16 

 Follow the HA Clustering Best Practices
and Provisioning requirements to ensure compatibility and
consistent security enforcement, for example. 

 Configure two HA interfaces (to assign as the
HA4 and HA4 backup links). 

 Enable HA clustering. 

 Select Device High Availability General and
edit the Clustering Settings. 

 Enable Cluster Participation . 

 Enter the Cluster ID and configure the Clustering Settings . 

 Configure the HA4 link. 

 Select HA Communications and
in the Clustering Links section, edit the HA4 section. 

 Select the interface you configured as an HA interface
to be the Port for the HA4 link; for example,
ethernet1/1. 

 Enter the IPv4/IPv6 Address of
the local HA4 interface. 

 Enter the Netmask . 

 ( Optional ) Configure the HA4 Keep-alive
Threshold . 

 Configure the HA4 Backup link by editing the HA4 Backup
section in a similar manner. 

 Specify all members of the HA cluster, including the
local member and both HA peers in any HA pair. 

 Select Cluster Config . 

 Add a peer member’s Device
Serial Number . 

 Enter the remaining device information . 

 Select the device and Enable it. 

 Define HA failover conditions with
link and path monitoring. 

 Commit . 

 Select Dashboard to view HA cluster
information in the web interface. 

 Previous 

 Networking Features 

 Next 

 HA Additional Path Monitoring Groups
