---
url: https://docs.paloaltonetworks.com/strata-cloud-manager/release-notes/changes-to-default-behavior
fetched_at: 2026-08-13T17:39:33Z
source: palo-alto-main
---

# Changes to Default Behavior in Strata Cloud Manager Clear

Changes to Default Behavior in Strata Cloud Manager 

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

 Changes to Default Behavior in Strata Cloud Manager 

 Updated on 

 Wed Aug 05 09:15:02 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Updated on 

 Wed Aug 05 09:15:02 PDT 2026 

 Focus 

 Home 

 Strata Cloud Manager 

 Changes to Default Behavior in Strata Cloud Manager 

 Download PDF 

 Strata Cloud Manager 

 Changes to Default Behavior in Strata Cloud Manager 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Previous 

 New Features in Strata Cloud Manager 

 Next 

 Known Issues 

 Changes to Default Behavior in Strata Cloud Manager 

 Changes to the default behavior, in Strata Cloud Manager . 

 The following table details the changes in default behavior in Strata Cloud Manager . 

 Feature Change 

 Object Cloning 

 In Strata Cloud Manager , configuration objects are organized in a
 folder hierarchy. Objects defined at higher levels are automatically
 inherited by all folders below them. When you clone an object to a
 child folder, you create a copy that can be customized for that
 level. 

 When you clone a configuration object from a parent folder or snippet
 to a child folder in Strata Cloud Manager Release 2.0, the system
 now automatically appends a -1 suffix to the cloned
 copy. For example, cloning an address object named
 blocked-ips creates
 blocked-ips-1 in the child folder instead of
 blocked-ips . 

 In previous releases, cloning an object with the same name as the
 parent object would silently override the inherited object, breaking
 inheritance and preventing security updates from flowing down to
 child folders. The new behavior preserves inheritance by default. If
 you intentionally want to override an inherited object, you must
 explicitly rename the cloned copy to match the parent object name.
 This ensures that overrides are always deliberate, not
 accidental. 

 Previous 

 New Features in Strata Cloud Manager 

 Next 

 Known Issues 

 On This Page 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

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

 Shared Policy for NGFWs and Prisma Access 

 Endpoints 

 GlobalProtect 

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

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
