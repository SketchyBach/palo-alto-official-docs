---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-6-installation-guides/6.12/cortex-xsoar-installation-guide/multi-tenant-installation/install-multi-tenant-with-bolt-database
fetched_at: 2026-09-06T10:50:45Z
source: cortex-platform
---

# Install Multi-Tenant with Bolt Database | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Installation Guides 

 6.12 (EoL) 

 Cortex XSOAR Installation Guide 

 Multi-Tenant Installation 

 XSOAR 6.12 Installation EoL 

 Install Multi-Tenant with Bolt Database 

 Install a multi-tenant Bolt or Bleve deployment in Cortex XSOAR 6.12. 

 Ensure the following: 

 Run all commands as the root user. 

 If you are installing on an Oracle Linux operating system, manually Install Docker . 

 Caution 

 Multi-tenant deployments are only intended for MSSPs. If you are not an MSSP and want to deploy a multi-tenant environment, you must first consult with the Cortex XSOAR product management team. If you deploy a multi-tenant environment without approval from the product management team, Cortex XSOAR will not support the deployment. 

 Installation File Structure 

 For information about the default installation file structure, see Installation File Structure . 

 Installer Flags 

 For the list of supported installer flags, see Installer Flags . 

 Download the server package you received from Cortex XSOAR support. 

 Note 

 When you receive a link to download, ensure that the downloadLink link refers to https://download.demisto.com and not https://download.demisto.works . 

 For example, wget -O demisto.sh “https://download.demisto.com/download-params?token=xabcedef&email=user@paloaltonetworks.com&eula=accept” 

 To download the latest vendor affirmed FIPS version, append &downloadName=fips . For example, wget -O demisto.sh “https://download.demisto.com/download-params?token=xabcedef&email=user@paloaltonetworks.com&eula=accept&downloadName=fips” 

 Run the chmod +x demisto.sh to make the server package executable. 

 Run the ./demisto.sh -- -multi-tenant command as root user. 

 Previous Multi-Tenant Installation 

 Next Installer Flags 

 Last updated 27 days ago 

 Was this helpful?
