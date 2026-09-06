---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/attack-surface-management/asm-enrichment-of-cloud-assets
fetched_at: 2026-09-06T09:45:44Z
source: cortex-platform
---

# ASM enrichment of cloud assets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Detect, investigate, and respond to threats 

 Attack surface management 

 ASM enrichment of cloud assets 

 ASM enrichment of cloud assets provides visibility into all the assets in your cloud infrastructure that are exposed to the internet. 

 Attack Surface Management (ASM) enrichment of cloud assets brings ASM capabilities to cloud security posture management, providing visibility into all the assets in your cloud infrastructure that are exposed to the internet. 

 ASM enrichment of cloud assets includes the following capabilities: 

 Discovery of unmanaged cloud services : Identify internet-exposed cloud services that are unmanaged, so you can onboard them into Cortex XSIAM for comprehensive cloud security and policy enforcement. 

 Confirmation of internet exposure: ASM internet scan data is used to reinforce CNA detections to provide high-confidence detections of inadvertent internet exposure. This joint approach combines inside-out and outside-in assessments to reduce false-positives. 

 Monitoring of managed and unmanaged cloud services : Gain ongoing visibility into the risks on cloud services through regular ASM scans and issues and findings for cloud-related attack surface detections. 

 What is unmanaged cloud? 

 Managed cloud —Cloud services that were discovered in an ASM scan and can be correlated with preexisting cloud assets that have been onboarded into your asset inventory. For example, if an ASM scan finds a service on AWS that is also in your cloud inventory, the asset is considered a managed cloud asset. 

 Unmanaged cloud —Cloud services that were discovered by an ASM scan, were attributed to you based on domain, subdomain, or TLS certificate, but cannot be correlated to the IPs or FQDNs of any onboarded cloud assets. For example, if a scan detects a service on an Azure asset that has not been onboarded into your cloud inventory, it is considered an unmanaged cloud asset. 

 If an ASM scan finds a service on HiNet or some other unsupported cloud provider, it is considered "not applicable" because it cannot be onboarded and converted to a managed asset. 

 Review your unmanaged cloud services 

 Review your unmanaged cloud services in your External Surface inventory. Unmanaged cloud services are cloud services that were discovered in an ASM scan and cannot be correlated with cloud assets that were previously onboarded into your inventory. 

 Navigate to Inventory → Assets → All Assets → External Surface → Services . 

 On the Service Inventory page, filter the list of services using the filter Partially Onboarded = Yes . 

 Review unmanaged cloud issues 

 The attack surface rule Unmanaged Cloud Service creates findings when ASM scans detect unmanaged cloud services. This rule is enabled by default, which means it will also create issues. Perform these steps to view your unmanaged cloud issues: 

 Navigate to Cases & Issues → Issues . 

 Filter the Issues table using the filter Attack Surface Rule ID = UnmanagedCloudService . 

 Click on an issue to display the issue details, including the unmanaged cloud service information. 

 Previous Deploy ASM and Exposure Management enrichment and remediation automation 

 Next Emerging Vulnerabilities 

 Last updated 1 month ago 

 Was this helpful?
