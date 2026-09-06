---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/code-to-cloud/code-to-cloud
fetched_at: 2026-09-06T10:06:45Z
source: cortex-platform
---

# Code-to Cloud | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 code-to-cloud 

 Cortex Cloud Posture 

 Code-to Cloud 

 Trace software assets from source code to cloud runtime resources. 

 Code to Cloud (C2C) traceability is the core correlation engine in Cortex Cloud that maps your complete path to production, establishing deterministic, bidirectional lineage across your entire Software Development Life Cycle (SDLC). By connecting source code, build pipelines, artifacts, and runtime infrastructure, C2C transforms fragmented asset data into a unified, traversable graph. 

 Resolving your lineage chain transitions your organization from a fragmented view to a governed posture by providing the following capabilities. 

 Code-to-Cloud (forward traceability) 

 Follows assets from source code through build pipelines and artifacts to their deployed runtime destinations, enabling you to: 

 Understand deployment exposure : Determine if, where, and how code is deployed in cloud environments 

 Precision prioritization : Prioritize code findings using runtime context, such as deployment status, internet exposure, and exploitability, instead of relying only on static severity 

 Support compensating controls : Identify the affected runtime resources so temporary mitigations or compensating controls can be applied while a permanent code fix is being developed 

 Validate deployment lineage : Verify that artifacts and infrastructure originated from the expected source and pipeline, providing end-to-end deployment visibility 

 Cloud-to-Code (backward traceability) 

 Traverses from runtime workloads back to the originating artifacts, pipelines, and source code, enabling you to: 

 Attribution : Identify the owning repository, pipeline, and development team responsible for a runtime workload 

 Fix at the source (shift left) : Trace runtime findings back to the originating code so vulnerabilities and misconfigurations can be remediated where they were introduced, preventing future deployments of the same issue 

 Accelerated remediation : Route issues directly to the responsible owners without manual investigation, reducing mean time to remediation (MTTR) 

 Cross-lineage capabilities 

 By correlating both directions of the lineage graph, Cortex Cloud also enables: 

 Contextual application grouping : Resolve a complete lineage chain and create business applications from related repositories, pipelines, artifacts, and cloud resources using user-defined criteria. This exposes fragmented lineage and allows you to prioritize risk based on business impact rather than isolated asset severity. 

 Drift detection : Compare the intended state in your Version Control System (VCS) with the observed runtime state. Runtime changes are flagged as drift only when they introduce a security policy violation that does not exist in the source code, reducing operational noise. 

 Previous About Cortex Cloud Application Security 

 Next How the C2C engine works 

 Last updated 7 days ago 

 Was this helpful?
