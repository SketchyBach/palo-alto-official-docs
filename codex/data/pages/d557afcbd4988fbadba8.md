---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-remote-networks/enable-routing-for-your-remote-network
fetched_at: 2026-08-13T17:25:16Z
source: palo-alto-main
---

# Enable Routing for Your Remote Network Clear

Enable Routing for Your Remote Network 

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

 Enable Routing for Your Remote Network 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

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

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Remote Networks 

 Enable Routing for Your Remote Network 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Enable Routing for Your Remote Network 

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

 Set up IPSec Tunnels Prisma Access 

 Next 

 Onboard Multiple Remote Networks 

 Enable Routing for Your Remote Network 

 Configure routing settings for your remote network. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access 
 license 

 In order for Prisma Access to route traffic to your remote networks, you must provide
 routing information for the subnetworks that you want to secure using Prisma Access .
 You can do this in several ways. You can either define a static route to each
 subnetwork at the remote network site, or configure BGP between your service
 connection locations and Prisma Access , or use a combination of both methods. 

 If you configure both static routes and enable BGP, the static routes take
 precedence. While it might be convenient to use static routes if you have just a few
 subnetworks at your remote network locations, in a large deployment with many remote
 networks with overlapping subnets, BGP will enable you to scale more easily. 

 Static Routes —To enable static routes to and from your remote site to
 Prisma Access , identify the subnetworks or individual IP addresses at the
 remote site that you want Prisma Access to secure (for both inbound and
 outbound traffic). The subnetworks at each site must not overlap with each
 other, with the IP pools that you designated for Prisma Access for Users, or
 with the infrastructure subnet. 

 BGP —If you want to enable BGP to dynamically route traffic to and from
 your remote network, you will need to provide the BGP information for the
 eBGP router at your branch: 

 Branch Router Autonomous System (AS) Number —The AS to which
 the eBGP router at the remote network belongs. This is called the
 Peer AS . 

 Router ID —The IP address assigned as the Router ID of the eBGP
 router on the remote network. This is called the Peer
 Address . 

 If you configure both static routes and BGP routing, the static routes take
 precedence. 

 Here’s how to configure routing settings for your remote network site. 

 To add or adjust routing settings, go to 
 Configuration NGFW and Prisma Access Configuration Scope Prisma Access Remote Networks and add or edit a remote network site. 

 Configure static routes. 

 If you are using static routes to route traffic to and from your branch,
 Add the IP subnets or IP addresses that you want
 to secure at the branch. Note that if you make any changes to the IP subnets
 on your branch, you must manually update the static routes. 

 Configure dynamic routing. 

 To use dynamic routing to advertise your branch subnets, Enable
 BGP for Dynamic Routing and then configure the following
 settings: 

 Do Not Export Routes —Prevent Prisma Access 
 from forwarding routes into your remote network. 

 By default, Prisma Access advertises all BGP routing information,
 including local routes and all prefixes it receives from other
 service connections, remote networks, and mobile user subnets.
 Select this check box to prevent Prisma Access from sending any BGP
 advertisements, but still use the BGP information it receives to
 learn routes from other BGP neighbors. 

 Because Prisma Access does not send BGP advertisements, if you
 select this option you must configure static routes on your
 on-premises equipment to establish routes back to Prisma
 Access. 

 Peer IP Address —Enter the Peer IP Address
 assigned as the Router ID of the eBGP router on the remote
 network. 

 Peer AS —Enter the Peer AS, which is the
 autonomous system (AS) for your network. 

 You must use an RFC 6996-compliant BGP Private AS number. 

 Local IP Address —Enter the IP address that
 Prisma Access uses as its Local IP Address for BGP. 

 A local address is only required if your remote site device requires
 it for BGP peering to be successful. Make sure the address you
 specify does not conflict or overlap with IP addresses in the
 infrastructure subnet or subnets in the remote network. 

 Secret —Enter a Secret password to authenticate
 BGP peer communications and then Confirm
 Secret . 

 Troubleshoot Site Connections 

 To troubleshoot your remote network, go to the remote network setup ( Configuration NGFW and Prisma Access Configuration Scope Prisma Access Remote Networks ), select the remote network for which you want to troubleshoot,
 and Edit the routing preferences. 

 Previous 

 Set up IPSec Tunnels Prisma Access 

 Next 

 Onboard Multiple Remote Networks 

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

 4.1 Preferred 

 5.0 Preferred and Innovation 

 Administration 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 SASE 

 4.2 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 Prisma Access 

 4.0 Preferred 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
