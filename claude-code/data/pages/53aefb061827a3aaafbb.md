---
url: https://docs.paloaltonetworks.com/prisma-access-agent/release-notes/prisma-access-agent-release-information/prisma-access-agent-known-issues/prisma-access-agent-25-7-linux-known-issues
fetched_at: 2026-08-13T17:22:33Z
source: palo-alto-main
---

# Prisma Access Agent 25.7 (Linux) Known Issues Clear

Prisma Access Agent 25.7 (Linux) Known Issues 

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

 Prisma Access Agent 25.7 (Linux) Known Issues 

 Updated on 

 Wed Jul 29 16:38:38 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Jul 29 16:38:38 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent Release Notes 

 Prisma Access Agent Release Information 

 Prisma Access Agent Known Issues 

 Prisma Access Agent 25.7 (Linux) Known Issues 

 Download PDF 

 Prisma Access Agent 

 Prisma Access Agent 25.7 (Linux) Known Issues 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Prisma Access Agent 25.7 (macOS and Windows) Known Issues 

 Next 

 Prisma Access Agent 25.6.2 Known Issues 

 Prisma Access Agent 25.7 (Linux) Known Issues 

 Review the known issues in Prisma Access Agent Linux 25.7. 

 Prisma Access Agent Linux version 25.7 has the following known issues: 

 Issue ID Description 

 PANG-10159 

 On a Linux device, when Prisma Access Agent 25.7.0.10 establishes a
 tunnel connection to a gateway, SSH connections initiated from a
 different subnet to a remote host are lost or cannot be
 established. 

 PANG-10022 

 An issue exists with Prisma Access Agent on Arch Linux ARM where HIP
 reports are not sent to gateways after successful Prisma Access Agent Manager (endpoint manager) authentication and gateway
 connection. The agent shows empty HIP status despite active gateway
 and websocket connections. This occurs because outbound TCP SYN
 packets are blocked due to missing source application configuration
 in firewall rules on Arch Linux. The issue can block users if
 previous HIP reports don't match policy requirements. 

 Workaround: Add the destination domain (e.g.,
 gpcloudservice.com ) to the firewall allow list
 to resolve the SYN packet blockage and enable proper HIP report
 transmission. 

 PANG-10020 

 An issue exists with Prisma Access Agent for Linux on Arch Linux ARM
 where the websocket connection to the Prisma Access Agent Manager
 (or endpoint manager) goes down after authentication, causing HIP
 and keepalive failures. The agent cannot obtain source application
 information on this platform, resulting in endpoint manager traffic
 being incorrectly routed through the tunnel instead of direct
 connection. 

 Workaround : For single Prisma Access tenant deployments
 without enforcer mode, administrators must add Prisma Access Agent 
 endpoint manager FQDN rules for both DATA and DNS traffic to go via
 DIRECT in the forwarding profiles. In enforcer scenarios where users
 switch between tenants, administrators need to configure DATA and
 DNS destination rules for all essential domains to go via DIRECT: 
 *.epm.gpcloudservice.com (endpoint manager
 domain) 

 *.gw.gpcloudservice.com (gateway
 domain) 

 PANG-9990 

 An issue exists with Prisma Access Agent for Linux where SSH incoming
 connections do not work. When attempting to SSH into an endpoint
 that has the Prisma Access Agent installed, the connection fails.
 This prevents remote SSH access to devices running the agent,
 blocking workflows that rely on SSH connectivity. 

 PANG-9870 

 An issue exists with Prisma Access Agent for Linux where application
 filtering does not work on Arch Linux ARM due to eBPF failing to
 load. Traffic steering according to forwarding profiles fails when
 the tunnel is disconnected, causing traffic to hit default rules
 instead of configured policies. 

 PANG-9351 

 An issue exists with Prisma Access Agent for Linux where root users
 can delete nftable rules, resulting in all traffic bypassing the
 network filtering module. 

 PANG-9349 

 PANG-9331 

 Prisma Access Agent for Linux does not currently support Docker
 traffic for system updates or package installations within
 containers. When you run Docker containers on a Linux device with
 Prisma Access Agent active, all outgoing traffic from Docker is
 routed through the secure tunnel by default, which causes system
 updates and package installations to fail within the container
 environment. 

 Workaround : For agents running in on-demand mode, temporarily
 disconnect the Prisma Access Agent tunnel to perform container
 updates or install packages, then reconnect the tunnel after
 completing these operations. 

 Previous 

 Prisma Access Agent 25.7 (macOS and Windows) Known Issues 

 Next 

 Prisma Access Agent 25.6.2 Known Issues 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Release Notes 

 Prisma Access Agent 

 Next-Generation Firewall 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
