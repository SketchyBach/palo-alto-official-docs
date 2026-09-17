---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-new-features/panorama-features/syslog-forwarding-using-ethernet-interfaces.html
fetched_at: 2026-09-16T10:53:11Z
source: palo-alto-main
---

# Syslog Forwarding Using Ethernet Interfaces Clear

Updated on 

 Mon Aug 28 18:34:50 PDT 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 Panorama Features 

 Syslog Forwarding Using Ethernet Interfaces 

 Download PDF 

 PAN-OS ® New Features Guide 

 Syslog Forwarding Using Ethernet Interfaces 

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

 Syslog Forwarding Using Ethernet Interfaces 

 Use Ethernet interfaces, rather than the management interface,
to forward syslogs. 

 PAN-OS 10.0 enables syslog forwarding over
an Ethernet interface to optimize management operations. In an environment with
a high rate of log generation, you can forward logs over an Ethernet
interface to prevent loss of logs and to reduce the load on the
management interface. 

 Syslog forwarding uses an Ethernet interface
that is supported only for a Panorama™ management server in Panorama
mode or in Log Collector mode. Additionally, you can enable syslog
forwarding on only a single interface regardless whether the Panorama
management server is in Panorama mode or Log Collector mode. 

 Log in to the Panorama Web Interface . 

 Configure a Managed Collector . 

 Configure an Ethernet interface for forwarding syslogs
over an Ethernet interface. 

 Configure an Ethernet interface on the local Log
Collector. 

 Select Panorama Setup Interfaces and
select an Ethernet interface. 

 Enable Interface . 

 Configure the Ethernet interface as appropriate. 

 In the Device Management Services section, enable Syslog
Forwarding . 

 Select Yes to confirm your syslog
forwarding change. 

 You can only a single Ethernet interface
on the local Log Collector. 

 Click OK to save your changes. 

 Commit and then Commit
and Push your configuration changes. 

 Configure an Ethernet interface on a Dedicated Log Collector. 

 Select Panorama Managed
Collectors and select a Dedicated Log Collector. 

 Enable Interface . 

 Configure the Ethernet interface as appropriate. 

 In the Log Collection Services section, enable Syslog
Forwarding . 

 Select Yes to confirm your syslog
forwarding change. 

 You can only a single Ethernet interface
on the Dedicated Log Collector. 

 Click OK to save your changes. 

 Commit and then Commit
and Push your configuration changes. 

 Configure a Collector Group —On
the M-Series appliance, a default Collector Group is predefined
and already contains the local Log Collector as a member. However,
on the Panorama virtual appliance, you must add the Collector Group and
add the local Log Collector as a member. For both configurations,
you need to assign firewalls to a Log Collector for log forwarding. 

 Configure log forwarding to Panorama . 

 Configure syslog forwarding from
Panorama to a syslog server . 

 Previous 

 Enhanced Authentication for Dedicated Log Collectors and WildFire Appliances 

 Next 

 Increased Configuration Size for Panorama
