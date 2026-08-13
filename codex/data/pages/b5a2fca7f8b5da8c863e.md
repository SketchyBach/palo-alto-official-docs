---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/deploy-prisma-access-agents/prisma-access-agent-processes-to-be-allowlisted-on-edr-deployments
fetched_at: 2026-08-13T17:22:18Z
source: palo-alto-main
---

# Prisma Access Agent Processes To Be Allow Listed on EDR Deployments Clear

Prisma Access Agent Processes To Be Allow Listed on EDR Deployments 

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

 Prisma Access Agent Processes To Be Allow Listed on EDR Deployments 

 Updated on 

 Wed Jul 29 16:23:07 PDT 2026 

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

 Wed Jul 29 16:23:07 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent Administration 

 Deploy the Prisma Access Agent 

 Prisma Access Agent Processes To Be Allow Listed on EDR Deployments 

 Download PDF 

 Prisma Access Agent 

 Prisma Access Agent Processes To Be Allow Listed on EDR Deployments 

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

 Deploy the Prisma Access Agent 

 Next 

 Download the Prisma Access Agent Package 

 Prisma Access Agent Processes To Be Allow Listed on EDR Deployments 

 To prevent false positives in antivirus, Endpoint Detection and Response (EDR), or
 firewall applications, you need to allow list key Prisma Access Agent processes on EDR
 deployments. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 To ensure the uninterrupted operation of Prisma Access Agents on endpoints,
 configure antivirus, Endpoint Detection and Response (EDR), or firewall applications to
 recognize Prisma Access Agent processes as safe. These security applications can
 sometimes mistakenly identify Prisma Access Agent processes as malicious. To
 prevent these security applications from interfering with Prisma Access Agent 
 operations, allow list or create security exceptions for the following Prisma Access Agent processes before installation. 

 The following tables list the Prisma Access Agent processes that you must allow
 list on your EDR deployments. 

 macOS Processes to Allow List 

 /Applications/ Prisma Access Agent .app/Contents/MacOS/ Prisma Access Agent 

 /Applications/ Prisma Access Agent .app/Contents/Helpers/uninstaller 

 /Applications/ Prisma Access Agent .app/Contents/Helpers/pacli 

 /Applications/ Prisma Access Agent .app/Contents/Helpers/Enforcer.app/Contents/MacOS/pangdlp 

 /Applications/ Prisma Access Agent .app/Contents/Helpers/PAInsightsEngine 

 /Applications/ Prisma Access Agent .app/Contents/Helpers/PAHipCompliance 

 /Applications/ Prisma Access Agent .app/Contents/Helpers/downgrader 

 /Applications/ Prisma Access Agent .app/Contents/Helpers/PASrv.app/Contents/MacOS/PASrv 

 /Library/SystemExtensions/[UUID]/com.paloaltonetworks.pangdlp.enforcer.systemextension/Contents/MacOS/com.paloaltonetworks.pangdlp.enforcer 

 /Library/SystemExtensions/[UUID]/com.paloaltonetworks.pang.securityextension.systemextension/Contents/MacOS/com.paloaltonetworks.pang.securityextension 

 /Library/SystemExtensions/[UUID]/com.paloaltonetworks.pang.networkextension.systemextension/Contents/MacOS/com.paloaltonetworks.pang.networkextension 

 Windows Processes to Allow List 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \downgrader.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \PABrowser.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \PAchecker.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \PACli.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \PAHipCompliance.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \PAInsightsEngine.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \PASrv.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Access Agent \PAUI.exe 

 C:\Program Files\Palo Alto Networks\DLP\bin\PADlp.exe 

 Previous 

 Deploy the Prisma Access Agent 

 Next 

 Download the Prisma Access Agent Package 

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

 Prisma Access Agent 

 Next-Generation Firewall 

 Administration 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
