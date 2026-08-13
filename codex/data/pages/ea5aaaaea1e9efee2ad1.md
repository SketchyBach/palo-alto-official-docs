---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/hyperscale-security-fabric/cluster-configuration
fetched_at: 2026-08-13T14:04:17Z
source: ai-security
---

# Cluster Configuration Clear

Cluster Configuration 

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

 Cluster Configuration 

 Updated on 

 Mon Aug 10 05:08:54 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Updated on 

 Mon Aug 10 05:08:54 PDT 2026 

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

 AI Model Security 

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

 Next-Generation Firewalls 

 CN-Series 

 Firewalls 

 VM-Series 

 Cloud-Delivered Security Services 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Enterprise DLP 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Administration 

 Prisma AIRS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
