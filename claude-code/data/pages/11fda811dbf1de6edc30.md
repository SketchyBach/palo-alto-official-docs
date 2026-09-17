---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/vendor-specific-data-sources/kubernetes/supported-kubernetes-distributions
fetched_at: 2026-09-16T08:41:33Z
source: cortex-platform
---

# Supported Kubernetes distributions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Cortex XDR Data Sources and Connectors 

 Vendor-specific data sources and connectors 

 Kubernetes 

 Supported Kubernetes distributions 

 The following are the Kubernetes platforms that are supported with Cortex XDR agents (Real-time protection). 

 This table shows the Kubernetes platform versions that have been compatibility tested. The table shows the latest version that has been tested. All versions that are not EOL, up to the latest version, are supported. 

 Linux Kubernetes Platform 

 Version 

 Unmanaged Kubernetes (k8s) 

 1.30 

 Amazon Elastic Kubernetes Service (EKS) 

 1.33 

 BottleRocket OS x86_64 

 User mode agent only 

 BottleRocket OS aarch64 

 User mode agent only 

 Microsoft Azure Kubernetes Service (AKS) 

 1.33 

 CBL-mariner 2 x86_64 

 Google Kubernetes Engine (GKE) 

 1.33 

 Google Container-Optimized OS (COS)^(*) x86_64 

 User mode agent only 

 Google Kubernetes Engine (GKE) Autopilot 

 Oracle Kubernetes Engine (OKE) 

 1.33 

 Red Hat Openshift Container Platform (OCP) 

 4.16 

 RHCOS^(*) x86_64 

 User mode agent only 

 SUSE Rancher Kubernetes Engine 2 (RKE2) 

 1.28 

 Talos 

 1.8.3 

 Note 

 In Google Container-Optimized OS release 100 and earlier, where the FANOTIFY EXEC flag is not supported, the Kernel configuration may be partial for the user mode agent to properly function. In such cases, the agent will fallback to asynchronous mode. 

 In RHCOS version 4.12 and earlier, the Kernel configuration may be partial for the user mode agent to properly function. In such cases, the agent will fallback to asynchronous mode. 

 Previous Kubernetes 

 Next LOLBAS 

 Last updated 2 days ago 

 Was this helpful?
