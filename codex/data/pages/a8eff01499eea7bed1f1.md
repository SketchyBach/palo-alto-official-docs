---
url: https://cortex-docs.paloaltonetworks.com/cortex-xpanse/onboard-and-configure-cortex-xpanse/step-6-configure-priority-integrations
fetched_at: 2026-09-06T10:52:20Z
source: cortex-platform
---

# Step 6: Configure priority integrations | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Xpanse 

 Xpanse Expander Documentation 

 Onboard and configure Cortex Xpanse 

 Step 6: Configure priority integrations 

 Set up collection, automation, and outbound integrations as part of the Cortex Xpanse onboarding process. 

 Cortex Xpanse integrates with third-party tools and other Palo Alto Networks products, including Cloud Service Providers (CSPs), CMDBs, ticketing systems, SOARs, SIEMs and other systems. Some of the supported use cases include the following: 

 Maintain accurate asset inventory—Integrate Expander with IT and IT security systems that require an accurate source of truth of your organization's public-facing assets. 

 Generate notifications—Set up SIEM-configured notifications so you will be alerted on new assets and exposures quickly. 

 Kick off investigations—Kick off investigations of exposures with IT tickets to drive remediation action and reduce the number of exposures on your network edge. 

 Automate remediations—Cortex Xpanse Active Response uses automation integrations with playbooks to augment alert investigation and remediate risks automatically. 

 The specific integrations you set up will depend on your IT and security ecosystem. We suggest configuring collection integrations first, automation integrations next (requires Active Response add-on license), and then outbound integrations. The following table describes each type of integration and provides links for details and configuration instructions. 

 Type of Integration 

 Description 

 More Information 

 Collection Integrations 

 Cortex Xpanse supports two types of collection integrations: 

 Cloud Inventory integrations that ingest cloud compute instances from the major cloud providers (Amazon Web Services (AWS), Google Cloud Platform (GCP), MS Azure) 

 Prisma Cloud integration that ingests cloud resources from your Prisma Cloud inventory. 

 Both of these collection integrations bring cloud context into Expander where it can be enriched with ASM data, providing a unified, normalized inventory of your cloud assets. 

 Configure Collection Integrations 

 Ingest Cloud Resources from Prisma Cloud 

 Automation Integrations 

 Automation integrations are used by Active Response playbooks to enrich an alert or respond to an alert with an action, such as sending notifications or remediating the alert by directly modifying the configuration of an asset, service, or networking infrastructure. 

 These integrations require the Active Response add-on license. 

 Supported Automation Integrations 

 Configure Automation Integrations 

 Outbound Integrations 

 Outbound integrations push or pull information from Xpanse into a third party security or workflow tool in order to integrate into to an organization’s existing vulnerability or incident response system. 

 Set up Outbound Integrations 

 Previous Step 5: Begin asset validation and asset enrichment 

 Next Post-deployment steps 

 Last updated 1 month ago 

 Was this helpful?
