---
url: https://docs.prismacloud.io/admin-guide/32/install/deploy-console/console-on-aks
fetched_at: 2026-09-16T13:37:18Z
source: prisma-cloud
---

# Deploy the Prisma Cloud Console on AKS | 32 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 32 

 Install 

 Deploy the Prisma Cloud Console On-Prem 

 Deploy the Prisma Cloud Console on AKS 

 Use the following procedure to install Prisma Cloud in an AKS cluster. This setup uses dynamic PersistentVolumeClaim provisioning using Premium Azure Disk. When creating your Kubernetes cluster, be sure to specify a VM size that supports premium storage. 

 Prisma Cloud doesn’t support Azure Files as a storage class for persistent volumes. Use Azure Disks instead. 

 Prerequisites 

 You have deployed an Azure Container Service (AKS) cluster . Use the --node-vm-size parameter to specify a VM size that supports Premium Azure Disks. 

 You have installed Azure CLI 2.0.22 or later. 

 You have downloaded the Prisma Cloud command-line utility . 

 Use twistcli to generate the Prisma Cloud Console YAML configuration file, where <PLATFORM> can be linux or osx . Set the storage class to Premium Azure Disk. 

 Ask Copy 

 $ <PLATFORM>/twistcli console export kubernetes \ 
 --storage-class managed-premium \ 
 --service-type LoadBalancer 

 Deploy the Prisma Cloud Console in the Azure Kubernetes Service cluster. 

 Ask Copy 

 $ kubectl create -f ./twistlock_console.yaml 

 Wait for the service to come up completely. 

 Ask Copy 

 $ kubectl get service -w -n twistlock 

 Change the reclaimPolicy of the PersistentVolumeClaim . 

 Ask Copy 

 $ kubectl get pv 
 $ kubectl patch pv < pvc-nam e > -p ' {"spec":{"persistentVolumeReclaimPolicy":"Retain"}} ' 

 Next, configure the Prisma Cloud console . 

 Previous Deploy the Prisma Cloud Console on ACS 

 Next Deploy the Prisma Cloud Console on EKS 

 Last updated 2 months ago 

 Was this helpful?
