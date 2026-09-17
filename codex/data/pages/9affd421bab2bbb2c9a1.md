---
url: https://docs.paloaltonetworks.com/prisma-agent/administration/deploy-prisma-agents/deploy-prisma-agents-using-microsoft-intune/deploy-prisma-agents-to-android-endpoints-using-microsoft-intune
fetched_at: 2026-09-16T08:21:21Z
source: palo-alto-main
---

# Deploy Prisma Agents to Android Endpoints Using Microsoft Intune Clear

Updated on 

 Thu Aug 27 20:22:38 PDT 2026 

 Focus 

 Home 

 Prisma Agent 

 Deploy the Prisma Agent 

 Deploy Prisma Agents Using Microsoft Intune 

 Deploy Prisma Agents to Android Endpoints Using Microsoft Intune 

 Download PDF 

 Prisma Agent 

 Deploy Prisma Agents to Android Endpoints Using Microsoft Intune 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Verify Prisma Agent Configuration Profiles on macOS 

 Next 

 Add the Prisma Agent App for Android Endpoints to Microsoft Intune 

 Deploy Prisma Agents to Android Endpoints Using Microsoft Intune 

 . By leveraging Microsoft Intune, administrators can efficiently push the Prisma Agent app to all managed Android devices. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Android 10 and later version 

 Microsoft Intune is a cloud-based endpoint management solution that enables you to manage
 mobile endpoints from a central console. Using Microsoft Intune, you can deploy the
 Prisma Agent app to managed endpoints that are enrolled with Microsoft
 Intune. 

 Using Microsoft Intune, you can deploy Prisma Agent to the Android endpoints with
 the following connect methods: 

 Always-On 
 In an Always-On configuration, Prisma Agent automatically connects as soon as end users log in. You can optionally
 enable Lockdown Mode to enforce all network traffic through the Prisma Agent and block traffic that does not go through the Prisma Agent . 

 On-Demand 
 In an on-demand configuration, end users must
 manually connect Prisma Agent through the application. Traffic is routed
 through the Prisma Agent app only after the end users initiate and
 establish the connection. 

 Per-App 
 In a per-app configuration, you can specify the
 managed apps that can route traffic through Prisma Agent when connected.
 If using an allowlist, only the specified apps will be routed through Prisma Agent . If using a blocklist, all traffic will be routed through Prisma Agent except for the specified apps. 

 Prisma Agent works both with Android devices with a work profile and
 fully-managed Android devices. 

 Previous 

 Verify Prisma Agent Configuration Profiles on macOS 

 Next 

 Add the Prisma Agent App for Android Endpoints to Microsoft Intune
