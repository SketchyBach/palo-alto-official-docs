---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/hyperscale-security-fabric/offline-licensing-for-esxi-hsf-cluster/delicense-delete-offline-licensed-hsf-node
fetched_at: 2026-09-16T07:54:43Z
source: ai-security
---

# Delicense and Delete the Offline-Licensed HSF Node Clear

Updated on 

 Mon Aug 24 04:41:52 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Administration 

 Prisma AIRS as a Firewall - Hyperscale Security Fabric 

 Offline Licensing for an ESXi HSF Cluster 

 Delicense and Delete the Offline-Licensed HSF Node 

 Download PDF 

 Prisma AIRS 

 Delicense and Delete the Offline-Licensed HSF Node 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Supply Chain Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Update the HSF Offline License Profile 

 Next 

 Deploy and Manage Prisma AIRS HSF Clusters on KVM 

 Delicense and Delete the Offline-Licensed HSF Node 

 Delicense offline-licensed HSF nodes before deleting them to release their allocated
 status and make the licenses available for reassignment. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS 

 Software NGFW Credits 

 HSF subscription license 

 Software Firewall License plugin installed on Panorama 

 Software Firewall Orchestration plugin installed on Panorama 

 Before you delete an offline-licensed HSF node, you must ensure that the required HSF
 cluster is undeployed through the Software Firewall Orchestration plugin. Delicensing
 changes the node's status from Allocated to Available , making the license
 available for assignment to another node. 

 Delicensing does not release the associated credits. The credits remain reserved
 until you deactivate the license in the Customer Support Portal and upload a new
 Air-Gap License JSON file to Panorama. 

 If an HSF cluster is deployed and the nodes are not connected to Panorama, the
 allocated serial numbers are not successfully released following a cluster
 undeployment. Devices continue to be displayed as allocated despite being
 removed from the HSF. While no active deployments exist and prior deployments
 have been terminated, subsequent deployment attempts fail due to the
 unavailability of required credits. 
 Use the following op command to manually
 delicense a device serial
 number: 

 request plugins sw_fw_license offline-license delicense-device
serial-number <serial> 

 Undeploy an HSF Cluster 

 To undeploy the cluster, initiate the undeployment workflow within the Software
 Firewall Orchestration plugin. 

 Delete a Node 

 To delete a node, remove the node from the cluster in the Software Firewall
 Orchestration plugin and commit the change. 

 To remove an individual HSF cluster node, adjust the firewall count within the
 Software Firewall Orchestration plugin and initiate the update deployment
 workflow. 

 Reclaim Credits in Customer Support Portal 

 ( Optional ) If you want to reclaim credits in Customer Support Portal for use
 in other deployments, perform the following steps: 

 In the Customer Support Portal, locate the license entry for the deleted node
 and deactivate it. 

 Download the updated Panorama Air-Gap License JSON file. 

 In Panorama, select Panorama Plugins SW FW License Offline License . 

 Select the offline license profile and click Edit . 

 Upload the new JSON file and click OK . 

 Commit the change to Panorama. 

 Previous 

 Update the HSF Offline License Profile 

 Next 

 Deploy and Manage Prisma AIRS HSF Clusters on KVM
