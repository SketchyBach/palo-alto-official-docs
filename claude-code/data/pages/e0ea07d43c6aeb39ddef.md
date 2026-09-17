---
url: https://cortex-docs.paloaltonetworks.com/cortex-xpanse/inventory/asset-types/services
fetched_at: 2026-09-16T08:59:16Z
source: cortex-platform
---

# Services | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Xpanse 

 Xpanse Expander Documentation 

 Inventory 

 Asset Types 

 Services 

 Cortex Xpanse provides a complete inventory of all of the public internet-facing services attributed to your organization. 

 Cortex Xpanse provides a complete inventory of all of the public internet-facing services attributed to your organization. An external service can be any internet-facing device or software that communicates on a domain:port or IP:port pair. 

 Services include classifications which are fingerprint-based identifiers of software, technologies, and behaviors observed on the service. Classifications can be either active or inactive based on the most recent observations of a service. In addition to classifications, services will also include banner, response, and header information from Cortex Xpanse data collection. 

 Navigate to Asset Inventory → Services to view the complete list of services discovered by Cortex Xpanse. The fields are described in the table below. 

 Field 

 Description 

 Active Classifications 

 Facts that have been inferred a service by examining a response for fingerprints. Classifications cover a variety of details including: 

 Identifying specific software and versions 

 Configuration details of note 

 Identifying when the services do not implement best practices like web security headers or certificate security standards 

 Some Classifications merely note that a fact is true or false, like Missing Cache Control Header. Other Classifications provide additional information, such as a version number for “nginx Server”. 

 Discovery Type 

 Services are identified with one of the following two discovery types, depending on the level of confidence Cortex Xpanse has in attributing it to your organization. 

 Directly Discovered —Services that are definitively associated with an asset that belongs to your organization. Examples include: 

 It is hosted on one of your on-prem IP ranges 

 The service advertises one of your organization's certificates 

 It is on a managed cloud resource that is known to be yours 

 Colocated with your Services —Service is running on the same IP as a different directly-discovered service. In a multi-tenant hosting environment, these co-located services may belong to other organizations but can sometimes pose adjacency risks to your services hosted on that IP. If your organization has “single-tenant environment only” policies with 3rd party hosting providers, you can use this functionality to identify possible violations of that policy. 

 Domain 

 The most recent domain on which the service is running. 

 Externally Detected Providers 

 The provider of the asset is determined by an external assessment. 

 Externally Inferred CVEs 

 Externally Inferred CVEs are identified by comparing the product name and version of active service, if identifiable, with CVES for those products in the National Vulnerability Database. Additional investigation may be required to confirm if the CVE is present. 

 Click on the service to view the service details, which include the complete list of all the externally inferred CVEs. 

 Externally Inferred Vulnerability Score 

 This score is based on the highest CVSSv3 score for Externally Inferred CVEs on this service. If there is no CVSSv3 score for the CVE, then the CVSSv2 score is used. 

 First Observed 

 When the asset was first observed via any of the sources. 

 Inactive Classifications 

 Previously observed classifications that are no longer observed. See Active Classifications for a description of classifications. 

 Is Active 

 Yes— indicates the service is active, which means that the service has been observed recently. No— indicates the service is inactive, which means Cortex Xpanse no longer sees it on the internet 

 IPv4 Addresses 

 Array column listing the IPv4 addresses associated with this asset. 

 IPv6 Addresses 

 Array column listing the IPv6 addresses associated with this asset. 

 Last Observed 

 When the asset was last observed via any of the sources. 

 Port 

 The most recent port for the service. 

 Protocol 

 The application-level protocol on the public internet over which Cortex Xpanse validated the service. 

 Service ID 

 Unique ID associated with the service. 

 Service Classification Version 

 Version information detected for an active classification. 

 Service Classification Version information is displayed when it is available. Version information may not be available if: 

 The service doesn't have a version number. 

 The version was not detected in ASM scans. 

 Service Name 

 The service type along with the specific domain:port or IP:port pair for the service. 

 Service Type 

 The type of server or software for the service. 

 Tags 

 The following types of tags can be applied to assets: 

 BU : Business Unit is a designation to classify assets by the organization that owns the asset. The BU tag cannot be changed for individual assets in the Asset Inventory. 

 IR : IP range tag . Can be applied to external IP ranges. 

 AT : Asset Tag. Can be applied to domains, certificates, cloud compute instances, and unassociated responsive IPs. 

 Services vs. Alerts 

 Both Services and the Alerts enable you to review items that are attributed to your organization and that are exposed to the public internet. 

 Alerts identify specific security problems and violations of your organization’s policies and help you track progress on efforts to remediate those problems. 

 Services provides you with a complete inventory of all services that Cortex Xpansehas observed without security judgments. You can use the Services page to search for items for which there are not currently Attack Surface Rules or to conduct technology usage audits. 

 Cortex Xpanse can convert any service classifications that are relevant to your organization’s security policies into Attack Surface Rules that will automatically flag new instances that appear on your network as alerts. We are also continuously developing new service classifications to support inventory and security use cases. Contact your Customer Success representative to discuss your needs or ideas. 

 Inferred CVEs 

 Common Vulnerabilities and Exposures (CVE) is a system for referencing publicly disclosed software security vulnerabilities. Individual vulnerabilities are commonly referred to as CVEs, and each one is uniquely identified by a CVE ID, such as CVE-2020-1234. 

 Cortex Xpanse attempts to match each service with CVEs that might be present on that service. We refer to any potential matches as Inferred CVEs. We perform this matching using the service name and version information that is available to our scanners. 

 We categorize Inferred CVE matches as High or Medium Confidence based on the version information that is available on the service and from the National Vulnerability Database (NVD). 

 High Confidence —Precise version information is available both from the service and from NVD. 

 Medium Confidence —Part of the version information from the service matches the NVD entry for the CVE, but the version information from the service has additional characters 

 The table below provides examples of Inferred CVE matches. 

 Service information available from Xpanse Scan 

 CVE information available from NVD 

 Match Result 

 Details 

 Apache v 2.4.50 

 CVE-2021-41773 

 Affects cpe:2.3 🅰️ apache:http_server:2.4.49: : : : : : :* 

 No Match 

 Because the CPE information from NVD indicates a version of Apache that is different than the one we saw in the scan, this does not match. 

 Apache v 2.4.49 

 CVE-2021-41773 

 Affects cpe:2.3 🅰️ apache:http_server:2.4.49: : : : : : :* 

 High Confidence Match 

 Because the CPE information from NVD matches the version of Apache indicated from the scan, this is a high confidence match. 

 Apache v 2.4.49c 

 CVE-2021-41773 

 Affects cpe:2.3 🅰️ apache:http_server:2.4.49: : : : : : :* 

 Medium Confidence Match 

 Because the version numbers from the service and the NVD information match, except for the additional character in the version from the service, this is a medium confidence match. 

 Apache v 2.4.50 

 CVE-2022-22719 

 Affects cpe:2.3 🅰️ apache:http_server: : : : : : : : (up to and including 2.4.52) 

 High Confidence Match 

 Because the CPE information from NVD matches the version of Apache indicated from the scan, this is a high confidence match. 

 Apache v 2.4.50 (Running on Red Hat Enterprise Linux 6 (RHEL6), which is not affected by this CVE) 

 CVE-2022-22719 

 Affects cpe:2.3 🅰️ apache:http_server: : : : : : : : (up to and including 2.4.52) 

 High Confidence Match 

 Because the CPE information from NVD matches the version of apache indicated from the scan, this is a high confidence match.Xpanse cannot determine if mitigating controls are in place or the underlying OS, so this pairing will still generate a high confidence match. 

 In general, an Inferred CVE might impact your service, but additional investigation is required to confirm that the CVE is actually present. 

 Cortex Xpanse is making ongoing improvements to CVE version matching. In general, we aim to err on the side of overmatching, so you don’t miss a vulnerable service in need of patching. If you notice a version that is incorrectly matched or not matched, please contact your CSM and let them know. 

 Search for Instances of a Specific CVE 

 To search for instances of a specific CVE in your attack surface, go to the Inventory → Services page and filter on Externally Inferred CVEs . This will show you any services in your attack surface that match the inferred CVE. This does not confirm the presence or absence of a specific CVE. 

 For more detailed information about the risks of an externally inferred CVE, review the the Risk tab of an incident with that CVE. Here you will find exploit information, risk factors, and other details. 

 Previous Owned Responsive IPs 

 Next Owned IPv4 Ranges 

 Last updated 1 month ago 

 Was this helpful?
