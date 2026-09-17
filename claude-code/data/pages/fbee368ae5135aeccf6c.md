---
url: https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/vm-image-scanning
fetched_at: 2026-09-16T13:35:22Z
source: prisma-cloud
---

# VM Image Scanning | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Runtime Security 

 Compliance 

 Enforce Compliance Checks 

 VM Image Scanning 

 Prisma Cloud can scan the virtual machine (VM) images in your cloud environment for the following types of vulnerabilities: 

 Host configuration : Vulnerabilities in the VM image setup. 

 Docker daemon configuration : Vulnerabilities that stem from misconfiguring your Docker daemon. The Docker daemon derives its configuration from various files, including /etc/sysconfig/docker or /etc/default/docker . 

 Docker daemon configuration files : Vulnerabilities that arise from setting incorrect permissions on critical configuration files. 

 Docker security operations : Recommendations and reminders for extending your current security best practices to include containers. 

 Linux configuration : Compliance of Linux hosts. For example, ensure mounting of the hfs filesystem is disabled. 

 Reviewing VM image scan reports 

 To view the health of the VM images in your environment: 

 Open Console, then go to Monitor > Compliance > Hosts > VM images . 

 Select CSV or PDF to export all the compliance issues identified in the latest VM image scan to a CSV or a PDF file respectively. 

 Click on a VM image on the list. 

 A report for the compliance issues on the VM image is shown. 

 Previous Host Scanning 

 Next App-Embedded Scanning 

 Last updated 3 months ago 

 Was this helpful?
