---
url: https://cortex-docs.paloaltonetworks.com/cortex-xpanse/integrations/ingest-cloud-resources-from-prisma-cloud/configure-the-prisma-cloud-integration-in-cortex-xpanse
fetched_at: 2026-09-16T08:59:15Z
source: cortex-platform
---

# Configure the Prisma Cloud Integration in Cortex Xpanse | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Xpanse 

 Xpanse Expander Documentation 

 Integrations 

 Ingest Cloud Resources from Prisma Cloud 

 Configure the Prisma Cloud Integration in Cortex Xpanse 

 Enable Cortex Xpanse to ingest Prisma Cloud data. 

 Before you begin this task, you must generate an API access key and secret key in Prisma Cloud. See Generate an API Access Key in Prisma Cloud . 

 Navigate to Settings → Configurations → Data Collection → Collection Integrations. 

 Click + Add Instance for Prisma Cloud . 

 In the Collection Integration window, complete the information as follows: 

 Enter a descriptive Name of your choice. 

 In the Access Key ID field, enter your Prisma Cloud API access key ID. 

 In the Secret Key field, enter your Prisma Cloud secret key. 

 In the Service URL field, enter the URL for your Prisma Cloud instance. 

 The Prisma Cloud URL is different between the UI and APIs. Customers that log into https://app3.prismacloud.io should input https://api3.prismacloud.io as the Service URL. 

 In the Business Unit field, select the business unit you’d like to assign these assets to in Xpanse. 

 prisma-cloud-integration-configuration.png 

 Click Add Integration . 

 Prisma Cloud data may take up to 48 hours to be ingested into your Cortex Xpanse Expander instance. 

 Once you've configured the Prisma Cloud collection integration it may take up to 48 hours for new asset records, services, websites, alerts, and incidents to appear. This is because the collection process must run multiple times to ensure that data is only loaded for high confidence resources and can be properly combined with Xpanse global scan findings. 

 If after 48 hours you don't see new assets, services, websites, alerts, or incidents, check for errors on the collection integration configuration page in Settings . You should also confirm that you've properly configured access to all of the desired account groups in Prisma Cloud. 

 Previous Generate an API Access Key in Prisma Cloud 

 Next Prisma Cloud resource types 

 Last updated 2 months ago 

 Was this helpful?
