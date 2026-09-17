---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-posture-and-runtime-security-data-sources/container-registry-scanning/how-container-registry-scanning-works
fetched_at: 2026-09-16T08:33:31Z
source: cortex-platform
---

# How Container Registry Scanning Works | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Cloud Security 

 Registry scanning 

 Cortex XSIAM 

 How Container Registry Scanning Works 

 Learn how Cortex XSIAM discovers, scans, and evaluates container images in onboarded registries to identify and continuously monitor security risks. 

 Container Registry Scanning continuously monitors container images in your onboarded registries for security risks. After you onboard a registry, Cortex XSIAM automatically discovers new and updated images, scans them, and evaluates the results against the latest threat intelligence. 

 The process of container registry scanning consists of three key phases: 

 Discovery : The connector automatically discovers registries, repositories, and image tags across the onboarded account. 

 Scanning : The connector scans newly discovered or updated images and extracts software bills of materials (SBOMs), secrets, and malware indicators. To reduce bandwidth and compute usage, the connector scans immutable container images only once. The connector rescans an image if the scanning engines are updated or if the previous scan failed. 

 Evaluation : Extracted artifact metadata is evaluated against current threat intelligence to identify vulnerabilities, secrets, and malware. Findings and risk scores are re-evaluated dynamically whenever new CVE data is published, without needing to re-download or rescan the container image. 

 Previous Supported container registry integrations 

 Next Scan re-evaluation process 

 Last updated 7 days ago 

 Was this helpful?
