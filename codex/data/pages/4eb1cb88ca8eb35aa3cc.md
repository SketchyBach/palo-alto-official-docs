---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-stacked-policies/service-and-data-center-groups/add-third-party-endpoints
fetched_at: 2026-09-16T07:47:58Z
source: strata-and-sase
---

# Add a Standard VPN Endpoint Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Stacked Policies 

 Service and Data Center Groups 

 Add a Standard VPN Endpoint 

 Download PDF 

 Prisma SD-WAN 

 Add a Standard VPN Endpoint 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Service and Data Center Groups 

 Next 

 Add Groups and Domains 

 Add a Standard VPN Endpoint 

 Lets learn about the addition of third-party or standard VPN endpoints in Prisma SD-WAN.
 A service endpoint is a label representing a specific location or network
 service. 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 A service endpoint is a label representing
a specific location or network service. It can be Prisma SD-WAN 
data centers for transit services or third-party data centers. 

 Add a Standard VPN Endpoint 

 Select Configuration Prisma SD-WAN Resources Service & DC Groups . 

 Select Manage Endpoints to an endpoint. 

 Select Standard VPN from the drop-down and click
 Add Endpoint . 

 All Palo Alto Networks data center sites are automatically added when
 Admin Up is selected, which means that it can
 accept traffic per network policy. These endpoints cannot be deleted
 from the list. You can clear the Admin Up 
 selection to remove the endpoints from consideration when the system
 performs path selection per the defined network policy rules. 

 Enter a Name , and optionally, a
 Description for the service endpoint. 

 Select Admin Up to bring it up. 

 If you do not select Admin Up , the endpoint is not
 used in path selection for forwarding traffic. 

 (Optional) Select Allow Enterprise Traffic 
 to explicitly allow enterprise traffic to transit through the Cloud Security
 Service. 

 By default, the Prisma Access check box is selected
 for endpoints created through Easy Onboarding . This
 check box informs the Site Configuration and
 Overlay Connections page on the Prisma SD-WAN web
 interface that VPNs with this endpoint connect to Prisma Access. For
 manually created endpoints, ensure you select the check box for Prisma
 Access. 

 (Optional) Click on each of the options in the ellipses to add
 values for Address , IPs &
 Hostnames , and Liveliness Probes . 

 Select Address to enter the address of the
 endpoint location. 

 Select IPs & Hostnames and add their
 values. By default, the Disable Tunnel
 Reoptimization option is off, allowing tunnel
 reoptimization for latency changes. 

 When
 multiple IP addresses or URLs are configured under a Standard
 VPN endpoint, the ION device probes each endpoint IP address (it
 will resolve the URLs if configured) to determine the lowest
 latency endpoint. After the lowest latency endpoint is
 determined, the ION device builds the Standard VPN tunnel to
 that IP address. If the configuration liveliness 
 check fails, then it uses the next lowest latency endpoint IP
 address in the list. Additionally, the ION device tracks the
 current latency to each endpoint IP address, and, if there is a
 significant change in the latency to the closest endpoint from
 the current endpoint, the tunnel is moved. 

 Select Liveliness Probe and configure the
 following: 
 ICMP PING : Set the probing interval,
 failure count, and IP address (up to four
 configurations). 

 HTTP : Define the probing interval,
 failure count, HTTP status codes, and URL (up to four
 configurations). 

 Enable DNS Liveliness in Tunnel to
 resolve DNS for HTTP probes over the service tunnel instead
 of using WAN interface DNS servers. 

 The Enable DNS
 Liveliness in Tunnel option enhances
 HTTP probe reliability in the ION devices by performing
 DNS lookups directly over the Standard VPN tunnel
 instead of relying on WAN interface DNS servers.
 Previously, ION devices sent DNS requests to all
 interfaces, using the first response received, which
 could lead to incorrect probe targeting or failures due
 to misconfigured or unreachable DNS servers. 

 Save & Exit the endpoints dialog. 

 Previous 

 Service and Data Center Groups 

 Next 

 Add Groups and Domains
