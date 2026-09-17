---
url: https://docs.paloaltonetworks.com/prisma-access-agent/administration/deploy-prisma-access-agents/prisma-access-agent-processes-to-be-allowlisted-on-edr-deployments
fetched_at: 2026-09-16T07:45:20Z
source: strata-and-sase
---

# Prisma Agent Processes To Be Allow Listed on EDR Deployments Clear

Updated on 

 Thu Aug 27 20:22:38 PDT 2026 

 Focus 

 Home 

 Prisma Agent 

 Deploy the Prisma Agent 

 Prisma Agent Processes To Be Allow Listed on EDR Deployments 

 Download PDF 

 Prisma Agent 

 Prisma Agent Processes To Be Allow Listed on EDR Deployments 

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

 Deploy the Prisma Agent 

 Next 

 Download the Prisma Agent Package 

 Prisma Agent Processes To Be Allow Listed on EDR Deployments 

 To prevent false positives in antivirus, Endpoint Detection and Response (EDR), or
 firewall applications, you need to allow list key Prisma Agent processes on EDR
 deployments. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to activate the Prisma Agent feature 

 To ensure the uninterrupted operation of Prisma Agents on endpoints,
 configure antivirus, Endpoint Detection and Response (EDR), or firewall applications to
 recognize Prisma Agent processes as safe. These security applications can
 sometimes mistakenly identify Prisma Agent processes as malicious. To
 prevent these security applications from interfering with Prisma Agent 
 operations, allow list or create security exceptions for the following Prisma Agent processes before installation. 

 The following tables list the Prisma Agent processes that you must allow
 list on your EDR deployments. 

 macOS Processes to Allow List 

 /Applications/ Prisma Agent .app/Contents/MacOS/ Prisma Agent 

 /Applications/ Prisma Agent .app/Contents/Helpers/uninstaller 

 /Applications/ Prisma Agent .app/Contents/Helpers/pacli 

 /Applications/ Prisma Agent .app/Contents/Helpers/Enforcer.app/Contents/MacOS/pangdlp 

 /Applications/ Prisma Agent .app/Contents/Helpers/PAInsightsEngine 

 /Applications/ Prisma Agent .app/Contents/Helpers/PAHipCompliance 

 /Applications/ Prisma Agent .app/Contents/Helpers/downgrader 

 /Applications/ Prisma Agent .app/Contents/Helpers/PASrv.app/Contents/MacOS/PASrv 

 /Library/SystemExtensions/[UUID]/com.paloaltonetworks.pangdlp.enforcer.systemextension/Contents/MacOS/com.paloaltonetworks.pangdlp.enforcer 

 /Library/SystemExtensions/[UUID]/com.paloaltonetworks.pang.securityextension.systemextension/Contents/MacOS/com.paloaltonetworks.pang.securityextension 

 /Library/SystemExtensions/[UUID]/com.paloaltonetworks.pang.networkextension.systemextension/Contents/MacOS/com.paloaltonetworks.pang.networkextension 

 Windows Processes to Allow List 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \downgrader.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \PABrowser.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \PAchecker.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \PACli.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \PAHipCompliance.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \PAInsightsEngine.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \PASrv.exe 

 C:\Program Files\Palo Alto Networks\ Prisma Agent \PAUI.exe 

 C:\Program Files\Palo Alto Networks\DLP\bin\PADlp.exe 

 Previous 

 Deploy the Prisma Agent 

 Next 

 Download the Prisma Agent Package
