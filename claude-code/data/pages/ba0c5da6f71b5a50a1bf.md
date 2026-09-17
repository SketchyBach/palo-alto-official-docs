---
url: https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/consts/kubernetes-pod-container-type
fetched_at: 2026-09-16T09:04:13Z
source: cortex-platform
---

# XDM_CONST.KUBERNETES_POD_CONTAINER_TYPE | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Schemas 

 XSIAM Data Model Schema 

 XDM Consts 

 XDM_CONST.KUBERNETES_POD_CONTAINER_TYPE 

 The Kubernetes pod container type 

 Original 

 Mapped 

 Description 

 MAIN 

 XDM_CONST.KUBERNETES_POD_CONTAINER_TYPE_MAIN 

 A main application container defined in pod.spec.containers. 

 INIT 

 XDM_CONST.KUBERNETES_POD_CONTAINER_TYPE_INIT 

 An init container defined in pod.spec.initContainers that runs to completion before main containers start. 

 SIDECAR 

 XDM_CONST.KUBERNETES_POD_CONTAINER_TYPE_SIDECAR 

 A sidecar container (Kubernetes 1.28+) defined in pod.spec.initContainers with restartPolicy=Always, running alongside main containers for the lifetime of the pod. 

 Previous XDM_CONST.KUBERNETES_PROFILE_CAPABILITY_STATUS 

 Next XDM_CONST.KUBERNETES_DISTRIBUTION 

 Last updated 1 month ago 

 Was this helpful?
