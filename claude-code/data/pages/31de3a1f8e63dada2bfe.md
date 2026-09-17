---
url: https://cortex-docs.paloaltonetworks.com/kubernetes-security/cloud-workload-policies-and-rules/cloud-workload-policies/cloud-workload-preventive-action
fetched_at: 2026-09-16T08:48:52Z
source: cortex-platform
---

# Cloud workload preventive action | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Kubernetes Security 

 Cloud workload policies and rules 

 Cloud workload policies 

 Cloud workload preventive action 

 Some Cloud Workload policies provide a Prevent and Create an Issue action that enforces compliance during deployments. 

 Prevention action for Runtime stage Policies 

 The Prevent action at Runtime applies only to Kubernetes Workload Images assets. 

 When a Kubernetes Workload image violates a policy, the Kubernetes Admission Controller (on clusters where the KSPM Connector is deployed and Admission Control is enabled) can block it from being admitted to the cluster. 

 For all other asset types within the policy scope, no runtime prevention will occur. Instead, the violation will result in an Issue being created. 

 Prerequisites 

 Deploy your cluster via the Kubernetes connect wizard. After your clusters are connected, you can manage and monitor your Kubernetes clusters for posture management and real-time protection. 

 To access the Kubernetes connect page, navigate to the following URL in your tenant environment: https://[TENANT-ADDRESS]/cwp/k8s-management. 

 Admission controller 

 This option is enabled via the Kubernetes connect wizard in the Posture management solution option. Policy enforcement by the admission controller must be enabled for the admission controller to evaluate requests that help you set the right policy scope and avoid unexpected blocks. 

 The admission controller manages the following: 

 Kubernetes object-level enforcement based on workload specs, including Deployments, StatefulSets, DaemonSets, ReplicaSets, Jobs, and CronJobs. 

 Create and update operations, re-evaluating the entire object for policy violations on every change, including simple scaling or replica updates. 

 Visibility for already-running workloads, surfacing existing policy violations as issues without disrupting or deleting the active resources. 

 Image-based blocking, relying on pre-existing scan results in the backend (such as CI, registry, or Agentless Disk Scanner results) to enforce policies without adding latency at admission time. 

 Trusted Images validation, blocking a workload that lacks a valid, up-to-date scan result in the backend when the policy uses the Prevent action on a cluster where the admission controller is enabled. 

 Important considerations 

 Recommended Approach : Begin with the Create an Issue action to validate results before selecting Prevent and Create an Issue . This helps prevent potential disruptions to your applications or development workflows. 

 Impact on New Deployments : The Prevent and Create an Issue action affects only new or future deployments that meet the prevention criteria. It does not impact cloud workload assets that are already deployed. 

 Prevention action for CI stage Policies 

 Prevention actions in the CI stage triggers a pipeline failure by returning an exit code of 2 in the CI tool. 

 Previous Manage cloud workload policies 

 Next Cloud workload rules 

 Last updated 1 month ago 

 Was this helpful?
