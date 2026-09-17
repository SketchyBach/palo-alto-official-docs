---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/asset-managment/asset-classes/external-surface-assets/domain-assets
fetched_at: 2026-09-16T08:44:39Z
source: cortex-platform
---

# Domain assets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Asset Managment 

 Asset classes 

 External Surface assets 

 Cortex Cloud Runtime 

 Domain assets 

 View domains and subdomains attributed to your organization. 

 The External Surface inventory includes all domains that Cortex Cloud has attributed to your organization and whether each domain has a recent resolution. Root domains and subdomains are displayed as separate entries in the inventory. However, if an organization owns a wildcard DNS entry, all subdomains of that wildcard that resolve to the same IP address are grouped under that one wildcard domain asset entry. If there are more than 1,000 subdomains, subdomains are collapsed under the parent domain. 

 Cortex Cloud collects domains and DNS data from a combination of active and passive global collection techniques. For DNS scanning, Cortex Cloud sends a BIND version query as the payload. This approach still identifies DNS servers that are not BIND compliant as their response informs us of a DNS server’s existence. 

 Click a row in the Domains table to open the details page for that domain. The information on this page is organized into the following tabs: 

 Overview: Summarizes key information about the domain, including Highlights like internet exposure, Properties like Asset ID, Provider, Asset Category, Account ID, and Tags, along with Attribution Evidence explaining why the asset belongs to your organization 

 Vulnerabilities: Displays Vulnerability Findings and Packages associated with the domain, including CVE IDs, CVSS scores, and EPSS scores 

 Compliance: Displays the Overall Compliance Score and Controls by Status for the domain 

 Recently Observed: Lists recently observed IPs associated with the domain, including the IP Address, Last Seen date, and Cloud Type 

 Services & Websites: Lists the services and websites running on the domain, including their Type, Status, Discovery Type, and Host 

 Previous Service assets 

 Next Certificate assets 

 Last updated 1 month ago 

 Was this helpful?
