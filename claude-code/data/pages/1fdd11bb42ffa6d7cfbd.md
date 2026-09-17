---
url: https://cortex-docs.paloaltonetworks.com/kubernetes-security/kubernetes-resources-inventory/kubernetes-pods
fetched_at: 2026-09-16T08:48:50Z
source: cortex-platform
---

# Kubernetes pods | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Kubernetes Security 

 Kubernetes Resources Inventory 

 Kubernetes pods 

 Kubernetes security provides comprehensive support for pods, including inventory tracking, detailed asset visibility, compliance scanning, and container inspection. This enhances protection across your workloads, whether they are managed by a controller (such as a deployment or job), deployed directly as standalone pods, or modified during admission before they run. Kubernetes security models the actual running pod, showing you the workload exactly as it operates in the cluster, including any changes applied after its definition. 

 Support for pods is available through the Posture Management solution of the Kubernetes Security offering. To collect pods, install either the agent-based Kubernetes Connector or Agentless KSPM. 

 Pods are where your workloads actually run. By modeling both directly, Kubernetes security gives you a complete, instance-level view of your clusters: 

 See the real running state of every workload, not only its desired state as defined by the controller. 

 Extend security coverage to workloads deployed directly as pods, for example, with kubectl apply -f pod.yaml , so standalone workloads are fully represented alongside managed ones. 

 Assess and prioritize risk at the container-instance level, providing your teams with precise context for investigation and remediation. 

 Key benefits include: 

 Complete visibility : A dedicated Kubernetes Pod Group in the inventory includes a relationship graph that shows how a pod connects to related Kubernetes resources. Kubernetes Pod Groups are also available in Search Graph for discovery and investigation. 

 Container inspection: A Containers tab on each Kubernetes Pod Group asset provides complete visibility into pod composition and container details, including each container's name, image, exposed ports, command, arguments, and Container type : Main (your application's primary container), Init (runs to completion before the main container starts), or Sidecar (a helper container that runs alongside the main container). You can filter the Containers tab to focus on specific containers and export the container data for reporting or offline analysis. Use the Kubernetes Pod Group to investigate the security posture of individual pods and their containers. 

 Compliance and rules : Run compliance checks on pods alongside workload controllers, including system-rule validation for pod-scoped Rego rules. Custom compliance rules also support pods. 

 Scalable by design : Identical replicas are automatically aggregated into a single Kubernetes Pod Group asset, so you gain full visibility without inventory clutter in large clusters. Kubernetes Pod Group aggregation is available for both the Kubernetes connector (agent) and Kubernetes agentless deployments. Standalone pods and pods owned by unsupported kinds (for example, Node-owned static pods) each produce their own single-replica Kubernetes Pod Group with Is Standalone = true. Agentless deployments collect pods that are linked to a controlling workload. 

 Kubernetes Pod Group 

 Kubernetes clusters can run thousands of pods, most of which are identical replicas of the same workload. To keep your inventory clear and eliminate clutter, Kubernetes security automatically aggregates identical pods into a single Kubernetes Pod Group asset. When you access Kubernetes Resources in the Kubernetes Resources page, you can filter by the Kubernetes Pod Group type to view these assets. 

 Each Kubernetes Pod Group reports the following properties: 

 Replicas : The number of identical pods aggregated into the group. 

 Is Standalone : Indicates whether the pod was created directly (with no controlling owner) or is managed by a controller. 

 Containers : Details on the containers running in the pod, including name, image, exposed ports, commands, arguments, and container type ( Main , Init , or Sidecar ). 

 With the Kubernetes connector, standalone pods and pods owned by unsupported resource types are represented individually so nothing is hidden from the inventory. 

 A Kubernetes Pod Group asset represents all identical Pod replicas of a workload as a single, unique inventory asset based on the workload owner's unique identifier. 

 Relationships graph for Kubernetes Pod Groups in Search Graph 

 Kubernetes Pod Groups participate in the Search Graph asset relationship graph like other workloads. In addition to standard workload relationships, they include the following: 

 Owned by : Links a Kubernetes Pod Group to its controlling workload (ReplicaSet, StatefulSet, DaemonSet, or Job). 

 Runs : Links the Kubernetes Pod Group to the container images it runs. 

 Routes traffic to/selected by : Services and NetworkPolicies that target the workload also resolve to the corresponding Kubernetes Pod Group . 

 Note : 

 These relationships are available in Search Graph only. 

 Selecting a Kubernetes Pod Group in the Kubernetes Resources inventory opens its asset card, where you can review its overview, configuration, containers, security findings, and relationships within the cluster. 

 Previous Kubernetes Resources Inventory 

 Next Manage Kubernetes Connector instances 

 Last updated 1 month ago 

 Was this helpful?
