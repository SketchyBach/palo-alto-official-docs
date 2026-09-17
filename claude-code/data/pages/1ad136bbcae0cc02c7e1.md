---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-new-features/policy-features/ip-range-and-subnet-support-in-dynamic-address-groups.html
fetched_at: 2026-09-16T10:53:13Z
source: palo-alto-main
---

# IP Range and Subnet Support in Dynamic Address Groups Clear

Updated on 

 Aug 28, 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 Policy Features 

 IP Range and Subnet Support in Dynamic Address Groups 

 Download PDF 

 PAN-OS ® New Features Guide 

 IP Range and Subnet Support in Dynamic Address Groups 

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

 IP Range and Subnet Support in Dynamic Address Groups 

 Learn how to use IP ranges or subnets in dynamic address
groups in addition to individual IP addresses. 

 PAN-OS 10.0 introduces enhancements to dynamic address
groups—you can now use IP sets, including IP address ranges and
IP subnets, in dynamic address group membership and you can view
source and destination dynamic address groups in some logs. 

 PAN-OS can now populate dynamic address groups with
IPv4 address sets, such as subnets and ranges, in addition to individual
IP addresses. When a new device joins your network as part of a
tagged IP set, the firewall applies the appropriate security policy
dynamically. Additionally, you can leverage security policy based
on dynamic address groups to dynamically quarantine infected or
vulnerable hosts. You can now use this functionality to dynamically
quarantine entire subnets or IP ranges instead of individual devices.
And an IP set is considered as a single registered IP address when
counted towards the maximum number of registered IP addresses supported
by each firewall model. 

 For example, the VM-Series firewall for VMware NSX collects IP
address information from NSX Manager and assigns those IP address
to dynamic address groups. NSX administrators can create security
groups that include static VM membership and dynamic VM membership. Static
membership is based upon IP sets that include subnets and ranges.
When an NSX administrator creates independent IP sets or security
groups with IP sets as members in NSX Manager, the Panorama administrator
can create corresponding dynamic address groups. And any changes
made to the IP set, range, or subnet are reflected in Panorama and
the firewall. 

 IPv6 IP subnets and ranges are not supported in dynamic
address groups. 

 To improve visibility and troubleshooting, source and destination
dynamic address groups are now recorded in some logs—Traffic, Threat, URL
Filtering, Wildfire Submissions, and Data Filtering—if the rule
the traffic matches includes a dynamic address group. If an IP address appears
in more than one dynamic address group, the firewall displays up
to five dynamic address groups in logs along with the source IP address. 

 Additionally, the IP-Tag log now displays how and when an IP
subnet or range is registered or unregistered on the firewall which
tag is applied. 

 Previous 

 Policy Features 

 Next 

 X-Forwarded-For HTTP Header Data Support in Policy
