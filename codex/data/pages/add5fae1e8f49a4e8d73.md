---
url: https://docs.prismacloud.io/admin-guide/32/upgrade/upgrade-defender-single-container
fetched_at: 2026-09-16T13:37:18Z
source: prisma-cloud
---

# Manually upgrade single Container Defenders | 32 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 32 

 Upgrade 

 Manually upgrade single Container Defenders 

 The Console user interface lets you upgrade all Defenders in a single shot. This method minimizes the effort required to upgrade all your deployed Defenders. 

 Alternatively, you can select whisch Defenders to upgrade. Use this method when you have different maintenance windows for different deployments. For example, you might have an open window on Tuesday to upgrade thirty Defenders in your development environment, but no available window until Saturday to upgrade the remaining twenty Defenders in your production environment. In order to give you sufficient time to upgrade your environment, older versions of Defender can coexist with the latest version of Defender and the latest version of Console. 

 Prerequisites: You have already upgraded Console. 

 Open Console. 

 On Manage > Defender > Manage and select Defenders to see a list of all your deployed stand-alone Container Defenders. 

 Upgrade your stand-alone Defenders. You can either: 

 Select Upgrade all to upgrade all Defenders at the same time. 

 On Actions select Upgrade corresponding to individual Defenders to upgrade a subset of your Defenders. 

 The Restart and Decommission buttons are not available for DaemonSet Defenders. They are only available for stand-alone Defenders. 

 Previous Amazon ECS 

 Next Manually upgrade Defender DaemonSets 

 Last updated 2 months ago 

 Was this helpful?
