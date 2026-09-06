---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security-rn/cortex-cloud-runtime-security-release-information/features-introduced-in-2026-cloud/february-2026/feature-enhancements
fetched_at: 2026-09-06T10:53:26Z
source: cortex-platform
---

# Feature Enhancements | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex CLOUD 

 Cortex Cloud Runtime Security 

 Cortex Cloud Runtime Security Release Information 

 Features introduced in 2026 

 February 2026 

 Feature Enhancements 

 These enhancements provide new and improved capabilities. 

 General 

 FEATURE 

 DESCRIPTION 

 New forwarding integrations for cases and issues 

 Streamline issue and case management workflows by forwarding cases and issues to new destinations such as Splunk, Amazon SQS, Amazon S3, and Webhook, allowing you to manage investigations in external systems or meet strict data retention requirements. 

 FedRamp/Government Cloud support 

 For organizations in regulated industries (such as defense or public sector), you can now onboard and manage your cloud security posture for tenants operating in isolated Government Cloud environments (including AWS GovCloud, Azure Government, and Google Public Sector). This ensures you have full visibility, detection coverage, and compliance monitoring across segregated cloud partitions, allowing you to easily meet strict regulatory requirements. 

 Onboard Microsoft Azure using Terraform 

 You can now automate infrastructure provisioning and save deployment time by using Terraform to onboard Microsoft Azure tenant and management group scope cloud instances. 

 Compliance improvements 

 Asset card compliance tab: Gain a detailed understanding of an asset's alignment with security standards by using the new compliance tab, which displays an asset's overall compliance score and compliance against individual controls. 

 Compliance Assessment CSV report improvements: Compliance Assessment CSV reports now include more actionable data such as remediation guidance for failed rules, tags, and cloud account IDs. 

 Autodetect Palo Alto Networks VM-Series firewalls 

 We now support the automatic detection of VM-Series firewalls deployed using Gateway Load Balancers (GWLBs) in isolated mode in AWS. This provides additional visibility and insights for internet-exposed assets. 

 Improved discovery and scanning for private Azure Container Registries (ACRs) 

 Cortex Cloud now provides complete visibility into all your Azure Container Registries by discovering and scanning the repositories and images in private ACRs. We enabled a new Allow connection to private registries toggle by default so the system can automatically create private links for successful scanning. The system then deletes these links immediately after to manage your resources efficiently and maintain security. 

 Asset-level rule configuration 

 Support for asset-based rules allows Exclusion, Starring, Scoring, and Playbook rules to be configured for specific asset objects, enabling tailored automation and notifications per account or asset group. 

 Previous Release Highlights 

 Next AI Security 

 Last updated 12 minutes ago 

 Was this helpful?
