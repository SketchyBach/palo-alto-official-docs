---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/ip-optimization
fetched_at: 2026-08-13T17:25:07Z
source: palo-alto-main
---

# IP Optimization Clear

IP Optimization 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 IP Optimization 

 Updated on 

 Aug 10, 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Aug 10, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Mobile Users 

 Mobile Users: GlobalProtect 

 IP Optimization 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 IP Optimization 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 Allow Listing GlobalProtect Mobile Users 

 Next 

 IP Capacity Planning 

 IP Optimization 

 IP Optimization provides a simpler, deterministic public IP address allow listing
 experience, improved resiliency, and faster onboarding of Prisma Access 
 tenants. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access license 

 Prisma Access version 5.0 or later 

 GlobalProtect app recommended versions: 

 6.2.6 client version for Windows and macOS 

 6.2.9 for Linux 

 6.1.9 for Android and IOS 

 IP Optimization is a set of architectural enhancements that reduce the overall number
 of IP addresses in your deployment, simplifying your allow listing workflows while
 improving resiliency and enabling faster onboarding of Prisma Access 
 tenants. 

 IP Optimization simplifies the management of IP addresses in a Mobile
 Users—GlobalProtect™ deployment. In deployments that don't use IP Optimization, you
 receive a single Mobile Users Security Processing Node (MU-SPN) for each Prisma Access location you allocate, and each node provides you with two egress
 IP addresses. Prisma Access uses the egress IP addresses to egress traffic to
 the internet, and you must also add these addresses to an allow list to give Prisma Access access to internet resources. 

 Experiencing a scaling event (for example, a
 large number of users accessing an existing Prisma Access location at the same
 time) could lead to autoscaling of MU-SPNs. This action can result in a situation
 where each MU-SPN receives additional Egress IP addresses, which means you will have
 to manage a large number of IPv4 addresses. IP Optimization reduces the number of
 IPv4 addresses you have to manage by adding a network load balancer (NLB) in front
 of the MU-SPNs and a NAT layer behind the MU-SPNs. 

 In IP optimization architecture, Prisma Access applies
 Source NAT (SNAT) to user traffic destined for the internet at the MU-SPN to a
 non-routable IP address from the 240.248.0.0/14 subnet. Prisma Access uses this
 subnet exclusively for internal communication between the MU-SPN and its associated
 NAT layer component. 

 IP Optimization does not reduce the number of IPv6 addresses in your
 deployment. The NAT layer applies to IPv4 addresses only. If you have IPv6 enabled
 in your environment, Prisma Access provides you with an IPv6 prefix per Prisma Access location. 

 The following functionality isn’t supported with IP Optimization: 
 Dynamic Privilege Access 

 Static IP Address Allocation 

 Traffic Steering (supported in IPv4 deployments, not supported
 in IPv6 deployments) 

 Be sure to review the allow listing considerations for IP Optimization . 

 Allow Listing Scenarios and Considerations 

 The following graphic shows the IP addresses you would have to add to your
 organization's allow lists in an IP Optimization deployment, including the ingress
 and egress IP addresses. 

 Here are the addresses you need to add to your allow lists: 

 IP Allow Lists in SaaS applications —If you have enabled IP allow lists
 for your SaaS applications then add the egress IP addresses to your IP allow
 lists to provide users access to the SaaS apps. 

 Source IP Address-Based Allow Lists in Remote Sites or Data Centers —If
 your branch office's perimeter firewall (such as an NGFW or Prisma SD-WAN) uses
 an outbound allow list, you must add the network_load_balancer IP addresses to the
 firewall's allow list. This is essential because the firewall will block mobile
 user traffic that is behind it unless you explicitly allow the Prisma Access 
 entry points (the load balancer IP addresses). 

 Endpoint Device Firewall Allow Listing for Prisma Access —If your endpoint
 devices have enforced policies on their local firewalls (such as Windows
 Defender Firewall), it is essential to allow list the following IP addresses:

 Mobile Users IP Address
 Pool : This refers to the IP addresses used by mobile users
 connecting to Prisma Access . 

 Prisma Access
 Infrastructure Subnet : This includes the IP addresses of the
 underlying Prisma Access infrastructure. 

 Allow listing these IP addresses ensures seamless connectivity and proper
 functioning of Prisma Access for your users. 

 Retrieve the Ingress and Egress IP Addresses for IP Optimization Deployments 

 It's a best practice to retrieve the ingress and egress IP
 addresses that Prisma Access assigns your network to avoid SaaS
 application or corporate firewall disruption. This can result in a situation where
 you're managing a large number of IPv4 addresses. IP Optimization reduces the number
 of IPv4 addresses you have to manage. 

 When you use the API to retrieve Prisma Access IP addresses 
 for IP Optimization, there are two sets of IP addresses you need to add: 

 serviceType of gp_gateway —The
 egress IP addresses the Prisma Access service uses for the cloud gateways.
 Add these addresses to your network allow lists to provide access to internet or
 SaaS apps. 

 addrType of
 network_load_balancer —The ingress IP addresses that you
 need to add to your NGFW allow list or client endpoint policy rules. Internet or
 SaaS apps don’t see these IP addresses; however, you need to add them to your
 network in the following scenarios: 

 Alternatively, you can use the Prisma Access UI to retrieve these addresses. 

 Make sure that you add all these addresses to your allow
 lists. IP addresses can change as the result of a dataplane upgrade and the
 addresses don't always revert to the previous addresses. 

 Best Practices for IP Address Allow Listing in IP Optimization Deployments 

 Palo Alto Networks recommends that you follow these best practices for IP address
 allow listing: 

 Add all ingress and egress IP addresses to your allow lists to
 minimize SaaS and corporate firewall disruption. 

 If you have IPv6 deployments, each Prisma Access location will
 receive an entire IPv6 subnet instead of IPv6 addresses. Add the entire
 subnet to your allow lists. 

 If you expect a large number of users to connect to a Prisma Access
 location, it's advisable to pre-allocate IP
 addresses. 

 Considerations for IP address pre-allocation: 

 When you enable a new location and expect a large number of
 users to connect from that location (more than 400), the MU-SPN
 might autoscale, resulting in allocation of additional IP addresses
 (ingress and egress). If you don't add these IP addresses to your
 allow lists, a service disruption might occur. 

 To avoid any disruption, perform capacity planning with the
 help of your Palo Alto Networks account team; then, use the API to pre-allocate IP
 addresses to retrieve the ingress and egress IP
 addresses. 

 After you run the pre-allocation script, the IP addresses
 have a validity period of 90 days. The public IP addresses are
 unique and not shared with any other Prisma Access deployment. If an
 IP address allocated to you by Palo Alto Networks remains unused for
 six months, it will be reclaimed. This includes IP addresses that
 were activated and then deactivated, and have remained deactivated
 for six months. For instance, if public IP addresses were allocated
 to your tenant for a specific location and that location wasn’t
 enabled for six months, Prisma Access might reclaim those IP
 addresses. Similarly, if you onboarded and then deboarded a mobile
 user location, Palo Alto Networks can reclaim the IP address used
 for that location six months after deboarding. 

 Previous 

 Allow Listing GlobalProtect Mobile Users 

 Next 

 IP Capacity Planning 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SASE 

 4.1 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 5.0 Preferred and Innovation 

 Administration 

 Prisma Access 

 Prisma Access 

 Prisma SASE 

 4.0 Preferred 

 Strata Cloud Manager 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
