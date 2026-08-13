---
url: https://docs.paloaltonetworks.com/pan-os/11-0/pan-os-new-features/mobile-infrastructure-security-features/user-equipment-ue-to-ip-address-correlation-for-5g-migration
fetched_at: 2026-08-13T17:07:49Z
source: palo-alto-main
---

# User Equipment (UE) to IP Address Correlation with PFCP for
4G Clear

User Equipment (UE) to IP Address Correlation with PFCP for
4G 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PAN-OS ® New Features Guide 

 : 
 User Equipment (UE) to IP Address Correlation with PFCP for
4G 

 Updated on 

 May 6, 2026 

 Focus 

 Download PDF 

 End-of-Life (EoL)

 Filter

 Version 

 11.0 (EoL) 

 11.0 (EoL) 

 Expand all | Collapse all 

 Networking Features 

 PPPoE Client Support on a Subinterface 

 DHCPv6 Client with Prefix Delegation 

 IPSec Transport Mode 

 Multicast Source Discovery Protocol on Advanced Routing Engine 

 Web Proxy 

 Power Over Ethernet (PoE) 

 Panorama Features 

 Admin-Level Commit with Policy Reordering 

 Static Security Group Tag (SGT) for TrustSec Plugin 

 Management Features 

 Skip Software Version Upgrade 

 TLSv1.3 Support for Management Access 

 Policy Rulebase Management Using Tags 

 Certificate Management Features 

 Support for OCSP Verification through HTTP Proxy 

 Cloud Identity Features 

 User Context for the Cloud Identity Engine 

 Content Inspection Features 

 DNS Security Support for DNS Over HTTPS (DoH) 

 Advanced Threat Prevention Support for Zero-day Exploit Prevention 

 Support for Custom Layer 3 and Layer 4 Threat Signatures 

 IoT Security Features 

 IoT Security Policy Rule Recommendation Enhancements 

 Improved DHCP Traffic Visibility for IoT Security 

 Mobile Infrastructure Security Features 

 User Equipment (UE) to IP Address Correlation with PFCP for 4G 

 SD-WAN Features 

 SD-WAN IPv6 Basic Connectivity 

 SD-WAN Plugin Support for Advanced Routing Engine 

 Virtualization Features 

 KMS Support for VM-Series 

 Software Cut-Through Based Offload on Software Firewalls 

 WildFire Features 

 Advanced WildFire Support for Intelligent Run-time Memory Analysis 

 Hold Mode for WildFire Real-Time Signature Lookup 

 Enterprise Data Loss Prevention Features 

 File Type Include or Exclude List for Data filtering Profiles 

 Updated on 

 May 6, 2026 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 Mobile Infrastructure Security Features 

 User Equipment (UE) to IP Address Correlation with PFCP for
4G 

 Download PDF 

 PAN-OS ® New Features Guide 

 User Equipment (UE) to IP Address Correlation with PFCP for
4G 

 Table of Contents 

 Filter

 Version 

 11.0 (EoL) 

 11.0 (EoL) 

 Expand all | Collapse all 

 Networking Features 

 PPPoE Client Support on a Subinterface 

 DHCPv6 Client with Prefix Delegation 

 IPSec Transport Mode 

 Multicast Source Discovery Protocol on Advanced Routing Engine 

 Web Proxy 

 Power Over Ethernet (PoE) 

 Panorama Features 

 Admin-Level Commit with Policy Reordering 

 Static Security Group Tag (SGT) for TrustSec Plugin 

 Management Features 

 Skip Software Version Upgrade 

 TLSv1.3 Support for Management Access 

 Policy Rulebase Management Using Tags 

 Certificate Management Features 

 Support for OCSP Verification through HTTP Proxy 

 Cloud Identity Features 

 User Context for the Cloud Identity Engine 

 Content Inspection Features 

 DNS Security Support for DNS Over HTTPS (DoH) 

 Advanced Threat Prevention Support for Zero-day Exploit Prevention 

 Support for Custom Layer 3 and Layer 4 Threat Signatures 

 IoT Security Features 

 IoT Security Policy Rule Recommendation Enhancements 

 Improved DHCP Traffic Visibility for IoT Security 

 Mobile Infrastructure Security Features 

 User Equipment (UE) to IP Address Correlation with PFCP for 4G 

 SD-WAN Features 

 SD-WAN IPv6 Basic Connectivity 

 SD-WAN Plugin Support for Advanced Routing Engine 

 Virtualization Features 

 KMS Support for VM-Series 

 Software Cut-Through Based Offload on Software Firewalls 

 WildFire Features 

 Advanced WildFire Support for Intelligent Run-time Memory Analysis 

 Hold Mode for WildFire Real-Time Signature Lookup 

 Enterprise Data Loss Prevention Features 

 File Type Include or Exclude List for Data filtering Profiles 

 End-of-Life (EoL)

 User Equipment (UE) to IP Address Correlation with PFCP for
4G 

 As mobile
service providers migrate from 4G/LTE to 5G, control and user plane
separation (CUPS) architecture is a common deployment in 4G networks.
With CUPS architecture, the User Plane Function (UPF) is closer
to the enterprise (either on the edge service or in an on-premises
location) while the control plane remains in a central location,
such as a data center. 

 Subscriber ID (IMSI) and equipment
ID (IMEI) correlation requires inspection of both control plane
and user plane traffic by the same firewall. UEIP Correlation provides
a way to ensure uninterrupted security policy enforcement during
migration to a CUPS architecture through correlation of the subscriber
ID and equipment ID to user equipment (UE) IP-based traffic and
GTP-U content inspection. 

 For a solution for 5G networks,
refer to 5G Multi-access Edge Computing
Security . 

 The firewall monitors traffic for PFCP
control messages at the Sxb interface and extracts the User Equipment
IP Address (UE_IP) and Mobile User Identification (User_ID), which
it uses to map the UE_IP to the IMEI, the IMSI, or both. It adds
the mapping to a database which it distributes to other data planes
and uses the mapping to perform GTP-U content inspection. You can
query the database for the UE_IP to view the correlated Mobile User
information for the UE IP traffic inside the GTP-U tunnels that
comprise the CUPS architecture. 

 The following diagram represents
a possible configuration for correlation for a 4G MEC topology using
CUPS architecture: 

 S1-U
represents a 3GPP interface that connects a 4G Radio Access Network
(RAN) to the serving gateway user plane (SGW-U) and PDN gateway
user plane (PGW-U) combo node using the GTP-U protocol. The control
plane (Sxb) is a 3GPP interface that connects the PGW-U in the MEC
location to the PGW-C in the 4G core at the central location (such
as a public cloud or on-premises data center) using the PFCP protocol. 

 The
SGI is also a 3GPP interface that connects the PGW-U to the external
network (such as the internet or enterprise IT data center) using
traditional IP-based interfaces. 

 In this topology, you can
deploy the firewall as external to the MEC host in a hardware form
factor or deploy the firewall on an MEC host in a virtual or container
form factor. 

 To enforce security policy based on Subscriber
ID or Equipment ID for a 4G MEC-based enterprise, position the firewall
on the user plane (S1-U) and control plane (Sxb) interfaces at the
MEC location. 

 The firewall inspects the control plane to
extract information for correlation with the user plane, providing
subscriber and equipment-level visibility, as well as policy control
for vulnerabilities, malware, viruses, URLs, C2, and applications
at the SP’s MEC location. 

 To support correlation, the
PFCP control message must contain the UE_IP and related User ID
IE (Information Element). 

 The following platforms support
UEIP Correlation: 

 VM Series 

 CN Series 

 PA-3430 and PA-3440 

 PA-5410, PA-5420, PA-5430, and PA-5440 

 If you
enable UEIP Correlation, the following options are not available
in the same Mobile Network Protection Profile: 
 GTP-C 

 5G-C 

 PFCP 

 Select Objects Security Profiles Mobility Network
Protection . 

 Add or Edit a
profile. 

 Select Correlation and enable UEIP
Correlation . 

 Select the handling Mode to define
the action if a query for the correlated information is not successful. 

 Loose —(Default) When the firewall
detects GTP-U inner traffic, it queries the source or destination
address to find the correlated IMEI/IMSI information. If there are
no results, the firewall forwards the traffic. 

 Strict —Drops the GTP-U traffic if the
query fails. 

 Select PFCP as the Source . 

 For deployments using CUPS, select PFCP. 

 (Optional) Select whether you want to log UEIP correlation
events when the firewall allocates an IP address to the UE ( Log
At Ueip Start ), when the firewall releases the allocated
IP address ( Log At Ueip End ), or both. 

 Click OK to save your changes. 

 (Optional but recommended) Enable stateful inspection for
GTP traffic . 

 Confirm that the profile is Enabled ( Policies Security Security Policy Rule Actions Profile Setting Mobile Network
Protection ) and Commit the
changes. 

 Use App-IDs to configure the Mobile Network Protection
Profile in a security policy to decapsulate the GTP-U tunnels and
correlate the IP address with the Subscriber ID and Equipment ID. 

 Using App-ID, configure a security policy
rule for the Sxb interface that allows PFCP traffic between the
Sxb nodes (PGW-C and PGW-U) and select the Mobile Network
Protection Profile you configured as the Profile
Setting (traffic can originate from either endpoint). 

 Using App-ID, configure a security policy rule for
the S1-U interface that allows GTP-U traffic between the S1-U nodes
(eNodeB and SGW-U) and select the Mobile Network Protection Profile
you configured as the Profile Setting   (traffic
can originate from either endpoint). 

 Previous 

 Mobile Infrastructure Security Features 

 Next 

 SD-WAN Features 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
