---
url: https://docs.paloaltonetworks.com/prisma-access-agent/release-notes/prisma-access-agent-release-information/prisma-access-agent-known-issues/prisma-access-agent-25-1-known-issues
fetched_at: 2026-08-13T17:22:31Z
source: palo-alto-main
---

# Prisma Access Agent 25.1 Known Issues Clear

Prisma Access Agent 25.1 Known Issues 

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

 Prisma Access Agent 25.1 Known Issues 

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

 Prisma Access Agent 25.1 Known Issues 

 Download PDF 

 Prisma Access Agent 

 Prisma Access Agent 25.1 Known Issues 

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

 Prisma Access Agent 25.3 Known Issues 

 Next 

 Prisma Access Agent Addressed Issues 

 Prisma Access Agent 25.1 Known Issues 

 Review the known issues in Prisma Access Agent 25.1. 

 Prisma Access Agent version 25.1 has the following known issues: 

 Issue ID Description 

 PANG-7947 
 Resolved in Prisma Access Agent 25.4 

 An issue exists where the Dynamic Privilege Access enabled Prisma Access Agent is unable to connect to a gateway after upgrading an
 endpoint to Windows 11 24H2. After the Windows upgrade, the Prisma Access Agent loses the ability to establish gateway connections,
 even though the Prisma Access Agent manager (EPM) connection remains
 functional. This occurs consistently across systems that have
 undergone the Windows 11 24H2 upgrade, affecting the agent's ability
 to connect to any configured gateways while maintaining normal EPM
 connectivity. 

 PANG-6738 
 Resolved in Prisma Access Agent 25.3 

 An issue exists where certificate authentication fails on Windows
 devices when certificates are stored in the machine certificate
 store. This impacts Prisma Access Agent functionality for Windows
 users attempting to authenticate using machine-level
 certificates. 

 Workaround : Import the client certificate from the machine
 store to the user's personal certificate store. The Prisma Access Agent is able to recognize and use client certificate credentials
 when they are located in the user store, even if it can’t access
 them in the machine store. 

 EPM-4848 

 As ring mappings for Prisma Access Agents are calculated during
 configuration time, the ring mappings might not always be accurate.
 Some potential causes are new agent enrollments, changes in
 directory binding, or host operating system updates. 

 Workaround : Before initiating a staged upgrade rollout of the
 agent, perform a commit push. This action ensures all agents are
 correctly mapped to their designated upgrade rings. If new agents
 are enrolled after you run the commit push, the new agents are
 always mapped to the default ring until the next commit push. 

 EPM-4821 

 The Connect Pre-logon option is present in the Prisma Access Agent Settings
 page for Panorama Managed Prisma Access and NGFW deployments, even
 though it's not functional. 

 Workaround : Ignore this option as it won’t work. 

 EPM-4616 
 Resolved in Prisma Access Agent 25.3 

 An issue exists where newly added internal gateways are not visible
 in existing Prisma Access Agent settings. This affects the ability
 to update agent configurations with recently added internal
 gateways. 

 This occurs when you select Configuration Prisma Access Agent Settings Prisma Access Agent and create an agent setting with external and internal gateways.
 Then, if you add additional internal gateways from the
 Infrastructure page, the added internal gateways don't appear in the
 previous agent setting. 

 Workaround : Create a new agent setting to see and utilize the
 newly added internal gateways. 

 Previous 

 Prisma Access Agent 25.3 Known Issues 

 Next 

 Prisma Access Agent Addressed Issues 

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
