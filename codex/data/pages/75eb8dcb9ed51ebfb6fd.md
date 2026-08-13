---
url: https://docs.paloaltonetworks.com/prisma-access-agent/release-notes/prisma-access-agent-release-information/prisma-access-agent-known-issues/prisma-access-agent-25-4-known-issues
fetched_at: 2026-08-13T17:22:32Z
source: palo-alto-main
---

# Prisma Access Agent 25.4 Known Issues Clear

Prisma Access Agent 25.4 Known Issues 

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

 Prisma Access Agent 25.4 Known Issues 

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

 Prisma Access Agent 25.4 Known Issues 

 Download PDF 

 Prisma Access Agent 

 Prisma Access Agent 25.4 Known Issues 

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

 Prisma Access Agent 25.6 Known Issues 

 Next 

 Prisma Access Agent 25.3.0 (Mobile) Known Issues 

 Prisma Access Agent 25.4 Known Issues 

 Review the known issues in Prisma Access Agent 25.4. 

 Prisma Access Agent version 25.4 has the following known issues: 

 Issue ID Description 

 PANG-8945 

 Resolved in Prisma Access Agent 25.7 

 When you upgrade to the latest Prisma Access Agent Manager (EPM), the
 default for Block Non-TCP and Non-UDP based traffic when
 connected to tunnel is disabled. An issue exists
 where the pacli traffic show command output
 incorrectly shows Allow non-tunnel outbound ICMP when
 connected to tunnel as true. 

 When the Block Non-TCP and Non-UDP based traffic when
 connected to tunnel option is disabled, the
 Allow ICMP for troubleshooting value
 should be passed as true. Currently, the Allow ICMP for
 troubleshooting value is incorrectly being passed as
 false (disabled), which should block ICMP traffic that goes out of
 the tunnel. However, ICMP traffic is actually being allowed through
 the physical adapter, creating a discrepancy between the
 configuration and actual traffic behavior. 

 This results in inconsistent ICMP traffic handling where the
 configuration indicates ICMP should be blocked, but the traffic is
 actually permitted. 

 PANG-8864 

 Resolved in Prisma Access Agent 25.6 

 An issue exists where the Prisma Access Agent might incorrectly
 remain bound to port 0 when switching between Prisma Access Agent 
 Manager (EPM) configurations with different proxy settings, causing
 endpoint traffic to Explicit Proxy (EP) to fail. 

 When the Prisma Access Agent initially connects to an EPM without
 agent proxy configured, it binds to port 0 after a system restart on
 the endpoint. If the system subsequently switches to a different EPM
 that has a proxy port configured, the agent might fail to update its
 port binding and incorrectly remain bound to port 0. This results in
 endpoint traffic destined for the Explicit Proxy failing to function
 properly. 

 Workaround : To resolve this issue, restart the endpoint, and
 then run the pacli proxy disable command,
 followed by the pacli proxy enable command.
 This forces the agent to properly initialize with the correct proxy
 port configuration from the new EPM. 

 PANG-8863 

 An issue exists where the embedded browser intermittently displays as
 blank or empty after installing Prisma Access Agent version 25.4 on
 Windows 11 systems. The embedded browser window appears but shows no
 content, preventing users from completing authentication or
 accessing websites through the agent's built-in browser
 component. 

 Workaround : Restart the endpoint. 

 PANG-8646 

 An issue exists where the reasoning for blocked non-TCP, non-UDP, and
 ICMP traffic is not logged in the PACli logs or network manager
 logs. When Prisma Access Agent forwarding profiles block this type
 of traffic, administrators cannot view the verdict reasoning or
 decision details through either the PACli command-line interface or
 network manager logs, making it difficult to audit and troubleshoot
 blocked traffic for these protocol types. 

 Previous 

 Prisma Access Agent 25.6 Known Issues 

 Next 

 Prisma Access Agent 25.3.0 (Mobile) Known Issues 

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
