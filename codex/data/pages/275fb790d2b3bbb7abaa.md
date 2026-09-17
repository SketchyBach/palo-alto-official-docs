---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-service-provider-csp-onboarding/outpost-onboarding
fetched_at: 2026-09-16T08:26:10Z
source: cortex-platform
---

# Outpost onboarding | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Cloud service provider (CSP) onboarding 

 Cortex XSIAM Data Ingestion Onboarding 

 Outpost onboarding 

 Learn about outposts, which are a dedicated set of infrastructure resources that extends the reach of Cortex XSIAM into your environment. 

 License type : This feature is included with a Cortex XSIAM Premium license. It is also included with any other Cortex XSIAM product that has the Cloud Runtime Security add-on. 

 An outpost is a dedicated set of infrastructure resources that extends the reach of Cortex XSIAM into your environment. It serves as a secure, localized point for scanning assets across cloud providers and on-premises workloads. 

 By establishing a trusted relationship between Palo Alto Networks and your environment, the outpost allows for deep security analysis, such as identifying vulnerabilities or classifying sensitive data, while ensuring that your live workloads remain unaffected. This architecture helps you maintain strict data residency and compliance by performing scans locally within a demarcated area of your network. 

 Important : Outpost scan is an alternative to the recommended standard cloud scan. Cloud scan is recommended because it is fully managed by Palo Alto Networks and incurs minimal compute costs for your organization. Outpost scan is an advanced deployment model reserved for specific data residency or architectural requirements. 

 Basic, standard outposts are the recommended deployment path for most organizations. Cortex XSIAM generates a Terraform template tailored to the values you enter in the outpost creation wizard, and you run that template in your CSP account to provision every resource the outpost needs, such as VPC or VNet, subnets, storage, secret vault, IAM roles or service accounts, scanner managed identities, and the trust relationship back to Cortex XSIAM. 

 This approach gives you the fastest, most consistent path to coverage while keeping the number of manual steps low. Cortex owns the resource definitions, naming conventions, and network topology, and you own the CSP account they run in. 

 What outposts include 

 A standard outpost deployment covers the full outpost lifecycle end to end: 

 Provisioning. Cortex-generated Terraform creates all outpost infrastructure in your CSP account, including networking, storage, secret vault, IAM roles, scanner managed identities, and optionally, for Azure, the Entra ID app registration and its federated identity credentials. 

 Trust establishment. The template configures the trust relationship between your CSP account and Cortex XSIAM automatically, using federated identity credentials rather than long-lived secrets. 

 Registration. Once the Terraform apply completes for both the outpost and the CSP onboarding overall, your cloud environment sends a registration callback to Cortex XSIAM, and the outpost transitions from Pending to Connected . 

 Ongoing scanning. After the outpost reaches Connected , Cortex schedules scans against the resources you onboard. 

 What's Next? 

 Review outpost fundamentals 

 Plan your outpost 

 Create your outpost 

 Previous Alibaba Cloud post-deployment verification 

 Next Outpost fundamentals and planning 

 Last updated 1 month ago 

 Was this helpful?
