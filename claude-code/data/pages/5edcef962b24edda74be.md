---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/vendor-specific-data-sources-and-connectors/docker/connect-docker-hub-registry/manage-a-docker-hub-connector
fetched_at: 2026-09-06T09:31:48Z
source: cortex-platform
---

# Manage a Docker Hub connector | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Vendor-specific data sources and connectors 

 Docker 

 Connect Docker Hub registry 

 Cortex XSIAM 

 Manage a Docker Hub connector 

 Manage the Docker Hub registry connector in Cortex XSIAM. 

 After you add a Docker Hub connector, you can modify the connector settings and configure the scanning scope to control which images are scanned in the connected registry. 

 To manage the connector, follow these steps: 

 Navigate to Settings → Data Sources & Integrations . 

 Find the Docker Hub data source from the list of data sources, or use the filter to search. 

 Select the Docker Hub row. A pane opens with a list of integration instances and their details. 

 You can create a new instance by selecting Add Instance and following the onboarding wizard to define the settings. 

 Right click an instance to perform actions on it as follows: 

 Action 

 Instructions 

 Edit 

 Edit the Docker integration instance. 

 If you selected Scan with Broker VM mode, you can't change to a different scan mode (such as Cloud Discovery or Scan with Outpost ) when you edit the instance. 

 When editing an instance configured for Scan with Broker VM , you must re-enter your authentication credentials, including Username , Password , and CA certificate . 

 Exclude/Include images 

 Define conditions to automatically exclude or include specific images while scanning. Conditions can be based on Repository or Tags . These conditions apply automatically to newly discovered images in the account. 

 Disable 

 Stops image scanning for the connector without deleting it. 

 Delete 

 Removes the connector. 

 Previous Connect Docker Hub registry 

 Next Connect Docker V2 compliant container registry 

 Last updated 9 days ago 

 Was this helpful?
