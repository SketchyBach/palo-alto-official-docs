---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/elasticsearch/elasticsearch-setup/elasticsearch-data-management
fetched_at: 2026-09-16T08:56:38Z
source: cortex-platform
---

# Elasticsearch Data Management | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Elasticsearch 

 Elasticsearch Setup 

 Cortex XSOAR 6.13 

 Elasticsearch Data Management 

 Manage Elasticsearch data in Cortex XSOAR 6.13. 

 Cortex XSOAR uses Elasticsearch to store configurations and content items. Indicator and incident data is saved monthly. 

 When using Elasticsearch, each logical data component is stored in an index for flexibility and archiving purposes. Logical data is divided based on contextual usage and size. Some indices contain only one data type, while other indices contain multiple data types. For example, all content items are stored in the configuration index, while an incident context is stored in a dedicated index. Each index may store multiple document types but each document stores only its own type. 

 A document in a sub-typed index (an index which contains multiple data types) has a prefix of the object type as part of the document ID. This ensures uniqueness of the documents regardless of their type when stored in the same index 

 All sensitive data in Elasticsearch is encrypted and Base64 when stored in Elasticsearch. This includes user passwords, API keys, credentials, instance sensitive parameters, etc. 

 All Elasticsearch indices use a known pattern: {indexPrefix-}dmst-{type}{_MMYYYY} 

 {indexPrefix-} is an optional customer selected index prefix configured in the Elasticsearch section in demisto.conf . 

 {type} is the index type to save, describing the contextual data stored. See lists below. 

 {_MMYYYY} is a suffix used only for partitioned indices. If the index is partitioned, the suffix is a 2 digit month and 4 digit year such as _092021 to indicate the index is storing data for September 2021. Note that some customers may have the following suffix: {_YYYYMM}. 

 For a multi-tenant deployment, the index prefix for accounts is predefined to allow account move functionality without reindexing. The prefix equals "account-{md5}" where {md5} is the account name hashed as md5. This can be calculated using the following bash command echo -n "acc_<name>" | md5sum where <name> is the account display name. 

 The lists below may change in future Cortex XSOAR versions. Objects may shift and indices may be removed or added as needed in future releases. 

 Main Indices - Non-Partitioned 

 Cortex XSOAR creates the following indices for configuration, indicators, relationships etc. 

 Note 

 Perform scheduled backups for the main indices, but DO NOT archive or delete them. 

 common-incidentidtrack - Contains one document containing the current incident ID used to calculate the next incident ID to generate. 

 genericobjectinstances - Contains all generic non-partitioned object instances used for dynamically defined objects such as threat intel reports. 

 common-relationships - Contains all relationship objects describing relationships to indicators in the Cortex XSOAR database or indicators found elsewhere. 

 common-configuration - Contains all content objects such as automations, integrations and instances, mappers and classifications, lists, incident fields, playbooks, etc. Also contains configuration objects such as API keys, UI configurations, users and roles, installed content packs, etc. 

 common-privateincident - Contains private incident mapping, details of the incident role based access including playgrounds. 

 common-indicator-shared - Contains all shared indicators data, including comments, source and expiration data on each indicator. 

 common-audit - Contains all audit logs on sensitive actions done in Cortex XSOAR. 

 common-indicator - Contains all indicators data, comments, enrichment data, source and expiration data on each indicator. 

 Examples of index names: dmst-common-configuration , myprefix-dmst-common-audit , account-807bc0ad51aab492607286c450a8eacb-dmst-common-indicator 

 Monthly Indices - Partitioned 

 Cortex XSOAR creates the following monthly indices. The monthly partitioned indices can be backed up and archived to restore space on the Elasticsearch nodes. Monthly indices can be identified by the {_MMYYYY} suffix. 

 common-invcontext - Contains all incident context keyed by the incident ID. 

 common-incident - Contains all incident related objects including the incident object, canvases, to do tasks, dropped incidents related, and others. 

 common-invplaybook - Contains all investigation playbooks keyed by the incident ID. Multiple investigation playbook runs are stored in the same object. The investigation playbook is viewable under the incident Work Plan. 

 common-investigation - Contains investigation details such as user members, RBAC permissions, and other investigation information associated with the incident. Keyed by the incident ID. 

 common-entry - Contains all investigation entries keyed by the entry ID and the investigation ID. 

 common-commoninvtask - Contains a mapped subset of the common-invplaybook to allow investigation tasks, metrics, and widgets. Only used when investigation task indexing is on. 

 common-metrics - Contains all metrics logs used to quantify and aggregate metrics details on automated Cortex XSOAR executions. Used by widgets and dashboards. 

 Examples of index names: dmst-common-invplaybook_202109 , myprefix-dmst-common-incident_202203 , account-807bc0ad51aab492607286c450a8eacb-dmst-common-commoninvtask_202001 

 Previous Elasticsearch Configurations 

 Next Elasticsearch Security 

 Last updated 1 month ago 

 Was this helpful?
