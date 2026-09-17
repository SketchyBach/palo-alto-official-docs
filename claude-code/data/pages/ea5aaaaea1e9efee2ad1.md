---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/hyperscale-security-fabric/cluster-configuration
fetched_at: 2026-09-16T07:54:42Z
source: ai-security
---

# Cluster Configuration Clear

Updated on 

 Mon Aug 24 04:41:52 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Administration 

 Prisma AIRS as a Firewall - Hyperscale Security Fabric 

 Cluster Configuration 

 Download PDF 

 Prisma AIRS 

 Cluster Configuration 

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

 Cluster Management 

 Next 

 Cluster Monitoring & Visibility in Panorama 

 Cluster Configuration 

 Configuration is pushed to cluster nodes from Panorama by enqueueing a commit job on
 the respective cluster node. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS 

 Software NGFW Credits 

 HSF subscription license 

 All cluster nodes must have identical configuration of firewall policies. A discrepancy
 in policy configuration between nodes will lead to different security policies being
 applied to various sessions, depending on the node that is processing the session.
 Configuration is pushed to cluster nodes from Panorama by enqueueing a commit job on the
 respective cluster node. The Panorama maintains a version number for template,
 device-group, and cluster configurations propagated to the cluster nodes. Each cluster
 node is cognizant of the configuration versions pushed to other nodes. 

 Cluster Creation and Node Addition 

 Cluster orchestration will facilitate the creation of device groups,
 templates, template stacks, and firewall clusters, subsequently committing these
 changes to the local Panorama. The template stacks must be configured with
 Automatically push content when a software device registers to Panorama 
 enabled. 

 When a new cluster node is connected, it will be bootstrapped to Panorama.
 This process involves: 

 Pushing content to the new node if its existing content version is
 older than the latest download content from Device Deployment. 

 Pushing antivirus definitions to the new node if its existing
 antivirus version is older than the latest download antivirus from Device
 Deployment. 

 Pushing the configuration (Device Group, Template, and Cluster) to
 the new node through a single commit-all job. 

 If the cluster node's configuration status is out-of-sync following
 the configuration push, the cluster node will fail to come online. 

 Subsequently, the system verifies if the new node's configuration (Device
 Group/Template/Cluster) versions are synchronized with those of the other nodes. If
 discrepancies are found, the autopush workflow will be initiated to distribute
 content, antivirus definitions, and configuration to existing nodes within the same
 cluster. 

 Cluster Node Deletion 

 Cluster orchestration will facilitate the deletion of cluster nodes from the device
 group, template, and cluster, followed by committing the changes to the local
 Panorama. Upon successful completion of the commit job, Panorama will automatically
 schedule a commit-all job to push the configuration (Device Group, Template, or
 Cluster) to all other nodes. 

 Previous 

 Cluster Management 

 Next 

 Cluster Monitoring & Visibility in Panorama
