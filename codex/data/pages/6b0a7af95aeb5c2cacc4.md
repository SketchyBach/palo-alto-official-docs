---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-new-features/mobile-infrastructure-security-features/equipment-id-security-in-4g-network.html
fetched_at: 2026-09-16T10:53:14Z
source: palo-alto-main
---

# Equipment ID Security in a 4G Network Clear

Updated on 

 Aug 28, 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 Mobile Infrastructure Security Features 

 Equipment ID Security in a 4G Network 

 Download PDF 

 PAN-OS ® New Features Guide 

 Equipment ID Security in a 4G Network 

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

 Equipment ID Security in a 4G Network 

 Secure your 4G/LTE traffic with Security policy rules
that specify source equipment identifiers. 

 4G/LTE mobile networks are used by billions
of subscribers worldwide, increasingly to connect the Internet of
Things. This evolution needs context-aware security in the network
to prevent financial and operational risks for service providers
and enterprise customers using private 4G networks. Malware that infects
User Equipment (UE), including smart phones, tablets, laptops connected
via a dongle, and cellular IoT devices, can prevent the UE from
accessing the mobile network and can be part of a botnet launching
an attack against the mobile network infrastructure. 

 The impact
of such malware to the customer includes battery exhaustion damage
to the device, degraded service, excessive billing, and more. The
impact to the service provider can include customer churn, help
desk calls, billing issues, excessive use of network resources by
compromised subscribers and devices, and more. Detection of these
threats in 4G/LTE mobile networks requires identification of compromised
equipment; prevention requires the ability to apply network security based
on equipment ID, which is an International Mobile Equipment Identity (IMEI). 

 You
can now apply network security based on the equipment identity of
any device or equipment that is trying to access your 4G network.
You can secure such things as: 

 Internet of small/sensing
things 

 An area of Massive IoT (smart metering, smart waste management, anti-theft,
and asset management) 

 Critical IoT (such as health care), wireless payments, home
control, vehicle communication, phone, and tablet 

 Security
policy rules and correlation based on 4G IMEI are supported on: 

 PA-7000 Series firewalls 

 PA-5200 Series firewalls 

 VM-700, VM-500, VM-300, and VM-100 firewalls 

 Enable GTP Security , commit,
and reboot the firewall. 

 Enable inspection of 4G GTPv2-C control
packets and content inspection of GTP-U packets; create a Mobile
Network Protection profile. 

 Create address objects for the IP addresses assigned
to the network elements in your topology, such as in deployment
option 1: the MME on the S11 interface, the eNB on the S1-U interface,
and the SGW on the S1-U and S11 interface; or deployment option
2: the SGW on the S5/S8 interface and PGW on the S5/S8 interface. 

 ( Optional ) Create an External Dynamic List (EDL)
of Type Equipment Identity List ; the Source of
the list provides access to a server that provides identifiers of
devices connected to the 4G network, for which you want to allow traffic. 

 Create a Security policy rule that applies your Mobile Network Protection profile to
application traffic. 

 Select Policies Security and Add a
Security policy rule. 

 For Source Address , Add the
address objects for the 4G network elements that you want to allow. 

 Add Destination Addresses for
the 4G network element you want to allow. 

 Add the Applications to
allow, such as gtp-u for user plane and gtpv2-c for
control plane traffic. 

 Select Action to Allow ;
select the Mobile Network Protection profile
you created. 

 Create another Security policy rule based on Equipment
ID. Most notably: 

 Add one or more Source
Equipment IDs in any of the following formats (if you
configured an EDL, specify that EDL in this step): 

 IMEI (15 or 16 digits) 

 IMEI prefix of eight digits for Type Allocation Code (TAC) 

 External dynamic list (EDL)
that specifies IMEIs 

 Add the Applications to
allow, such as ssh , ssl , radmin ,
and telnet . 

 Commit your changes. 

 Previous 

 Subscriber ID Security in a 5G Network 

 Next 

 Subscriber ID Security in a 4G Network
