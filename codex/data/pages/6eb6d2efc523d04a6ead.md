---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-6-multi-tenant-guides/6.13/configure-multi-tenant/configure-the-multi-tenant-deployment/run-a-command-on-multiple-tenants
fetched_at: 2026-09-06T10:50:12Z
source: cortex-platform
---

# Run a Command on Multiple Tenants | 6.13  | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Multi-Tenant Guides 

 6.13 

 Configure Multi-Tenant 

 Configure the Multi-Tenant Deployment 

 XSOAR 6.13 Multi-Tenant 

 Run a Command on Multiple Tenants 

 In Cortex XSOAR 6.13, run commands on incidents across multiple tenants. 

 In some cases, you might need to run a command across multiple tenants. For example, you might want to enrich certain IOCs across all tenant accounts. 

 From the main account, you can batch run a command on incidents from different tenant accounts. Running a command at the main account runs it locally on each tenant account. 

 If the command doesn’t exist on a particular tenant or if the user running the command from the main account doesn’t have the correct permissions, the command execution will fail and the output will be written to the incident’s war room. You will not see the error in the main account. 

 In some cases, tenants may have different versions of the same command. The local version of the command runs on the tenant. 

 On the Main Account → Account Management - Incidents page , select one or more incidents. 

 Click Run Command . 

 Enter ! and the command and press enter. 

 Previous Forward Server Configurations to Tenant Accounts 

 Next Move a Tenant to a Different Host 

 Last updated 1 month ago 

 Was this helpful?
