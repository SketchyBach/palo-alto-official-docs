---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/customize-cases-and-issues/external-integrations
fetched_at: 2026-09-16T08:42:44Z
source: cortex-platform
---

# External integrations | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Customize cases and issues 

 Cortex XDR 5.x 

 External integrations 

 Integrate external threat intelligence and case management services with Cortex XDR. 

 You can integrate external threat intelligence services with Cortex XDR that provide additional verification sources for each key artifact in a case. Cortex XDR supports the following integrations: 

 Threat intelligence 

 Integration 

 Description 

 WildFire 

 Cortex XSIAM automatically includes WildFire threat intelligence in the case and issue investigation. 

 WildFire detects known and unknown threats, such as malware. The WildFire verdict contains detailed insights into the behavior of identified threats. The WildFire verdict is displayed next to relevant Key Artifacts in the Cases page. See Review WildFire analysis details for more information. 

 VirusTotal 

 VirusTotal provides aggregated results from over 70 antivirus scanners, domain services included in the block list, and user contributions. The VirusTotal score is represented as a fraction. For example, a score of 34/52 means out of 52 queried services, 34 services determined the artifact to be malicious. 

 To view VirusTotal threat intelligence in cases, you must obtain the license key for the service and add it to the Cortex XDR Configuration . When you add the service, the relevant VirusTotal (VT) score is displayed in the Cases page under Key Artifacts . 

 Case management 

 Integration 

 Description 

 Third-party ticketing systems 

 To manage cases from the application of your choice, you can use the Cortex XDR API Reference to send issues and issue details to an external receiver. After you generate your API key and set up the API to query Cortex XDR, external apps can receive case updates, request additional data about cases, and make changes such as setting the status and changing the severity or assigning an owner. To get started, see the Cortex XDR API Reference guide. 

 Previous Customize cases and issues 

 Next Set up case scoring 

 Last updated 20 days ago 

 Was this helpful?
