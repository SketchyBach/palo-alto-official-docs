---
url: https://cortex-docs.paloaltonetworks.com/data-security-documentation/get-started-with-cortex-data-security/understand-cortex-data-security-licenses/data-storage-lifecycle
fetched_at: 2026-09-16T08:58:39Z
source: cortex-platform
---

# Data storage lifecycle | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Data Security 

 Cortex Data Security Documentation 

 Get started with Cortex Data Security 

 Understand Cortex Data Security Licenses 

 Data storage lifecycle 

 Cortex Data Security data storage is managed in the Cortex Data Layer. You receive data storage based on the amount associated with your license, determined by daily ingestion needs. The license provides default retention periods, which can be extended for hot and cold storage. 

 To determine your requirements, you must understand the differences between the available storage options. The following describes these differences: 

 Data Ingestion Pipeline 

 Data enters via a data stream called the Data Ingestion Pipeline, where manipulation, such as normalization, enrichment, and analytics, occurs. Once ready, it is transferred to the following locations based on your license: 

 Hot storage 

 With the Cortex Data Security license, data is automatically sent to hot storage for the default retention period (30 days). 

 Extensions : You can add retention in monthly increments via Period-Based Retention (all ingested data) or Additional Hot Storage (specific datasets). 

 Retroactive application : If you purchase additional hot storage, the new retention time can be applied retroactively to any data still available in your hot datasets that hasn't been purged yet. 

 Image example : The Cortex Data Security license and additional storage licenses ensure that all the data is accessible from hot storage for two months. After this, data begins purging except for Dataset 2 (accessible for one additional month) and Dataset 3 (accessible for two additional months) before being gradually purged. 

 Cold storage 

 The Cortex Data Security license provides no default cold storage. 

 Independence : There is no connection between hot and cold storage; you cannot move missing data from hot to cold storage later. Data must be sent to cold storage from the pipeline starting from the purchase date. 

 Tip: If cold storage data must align with hot storage data, purchase the cold storage license at the same time as the base Cortex Data Security license. 

 Accessibility : Cold storage data is collected upon ingestion but is only accessible after the hot storage retention period has expired. The cold storage retention period only begins once the hot storage period ends. 

 Retroactive application : If you purchase additional cold storage, the extra retention time may be applied retroactively to any data still residing in your cold datasets that hasn't been purged yet, provided the existing data is covered under the renewal/purchase. 

 Requirements : Requires a minimum of six months of retention and Compute Units (CU) to run cold storage queries. Cold-storage queries consume 1 CU per 35 GB of data scanned. For more information on CU, see Manage compute units. For information on the CU add-on license, see Understand Cortex Data Security license plans. 

 Image example : Cold storage is aligned with hot storage. The pipeline sends data to both for the first two months, but it is not accessible in cold storage during the hot storage retention period. After two months, the data becomes accessible in cold storage for six months (except for Datasets 2 and 3, which are still in their extended hot storage periods). Once those datasets finish their hot retention, they also become accessible in cold storage for six months before purging. 

 Export 

 The Cortex Data Security license does not provide default export capabilities. 

 Event Forwarding : Only after purchasing this add-on is data sent to an intermediate storage location from the pipeline. 

 Retention : This data is accessible for seven days before being gradually purged. 

 Image example : Export data is aligned with hot and cold storage. The pipeline sends data to intermediate storage for Event Forwarding, which is accessible for seven days before purging. For more information on Event Forwarding, see Manage Event Forwarding. 

 Recommendations 

 To optimize your data strategy and prevent data loss, consider the following best practices: 

 Synchronize license purchases : To align cold storage data with hot storage data, purchase the cold storage license at the same time as the base Cortex Data Security license. This ensures the Data Ingestion Pipeline begins feeding both streams simultaneously from day one. 

 Manage retention proactively : To ensure no data is lost and that extensions can be retroactively applied to hot and cold datasets, always make changes to the data retention licenses while your current license is still active. If a license expires or the data retention period passes, the data is purged and cannot be recovered or extended retroactively. 

 Tip: You can view details about your Cortex Data Security license by selecting Settings → Cortex Data Security License . 

 Previous Data retention in Cortex Data Security 

 Next License allocation 

 Last updated 2 months ago 

 Was this helpful?
