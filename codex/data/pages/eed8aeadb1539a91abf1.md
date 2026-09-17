---
url: https://docs.prismacloud.io/content-collections/administration/network-security/container-network-exposure/deploy-satellite
fetched_at: 2026-09-16T13:35:09Z
source: prisma-cloud
---

# Satellite Deployment | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Administration 

 Network Security 

 Container Network Exposure 

 Satellite Deployment 

 You can deploy Satellite manually or automated using the UI or the API. 

 The deployment of the Satellite operator across multiple namespaces within the same cluster is not supported. If you remove the Satellite operator from the Kubernetes cluster, the Kubernetes data that is ingested through that operator is immediately deleted. 

 Select Settings > Providers 

 Click Connect Provider and select K8s Satellite . 

 Enter the Cluster Name or Resource ID in the K8s Cluster ID dropdown. 

 (Optional) Enter Username and Password . 

 Click Next . 

 You can search the cluster by its name or the unique cluster asset ID by referencing the Cluster Asset ID field on the Asset Inventory page. 

 Review the Cluster details and click Next . 

 Copy the Helm upgrade/install command and run it in your selected cluster. 

 A unique identifier is created each time a Helm chart is generated and it acts as a cluster identifier. Therefore, you cannot reuse the Helm chart across different clusters. 

 As soon as the Helm chart is generated, the cluster will be in Pending state, until the Satellite gets deployed and starts reporting to Prisma Cloud. It can take a few minutes for the Satellite to get successfully deployed. 

 Once the deployment is complete, the cluster state will change to Active . 

 Once a cluster is in the Active state, it sends keep-alives to Prisma Cloud every 30 minutes. If there is a communication issue or if the Satellite gets removed from the cluster, the object will move into an Offline state until the communication is re-established or the object is deleted on the Prisma Cloud console. 

 Uninstall Satellite 

 To uninstall the Satellite operator: 

 Use the following command to uninstall Helm: 

 prismacloud-satellite -n pc-satellite 

 Delete the cluster from the Satellite UI: 

 On Settings > K8s Satellite select Delete under Actions for the corresponding cluster entry. 

 Previous Permissions Required by Satellite 

 Next Investigate Container Network Exposure on Prisma Cloud 

 Last updated 1 month ago 

 Was this helpful?
