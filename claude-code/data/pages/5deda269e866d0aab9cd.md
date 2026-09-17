---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/build-xql-queries/how-to-build-xql-queries
fetched_at: 2026-09-16T08:44:19Z
source: cortex-platform
---

# How to build XQL queries | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Cortex XDR XQL 

 Build XQL queries 

 Cortex XDR 3.x 

 How to build XQL queries 

 Learn more about how to build XQL queries in the Query Builder. 

 Notice 

 Building Cortex Query Language (XQL) queries in the Query Builder requires a Cortex XDR Pro license. 

 The Cortex Query Language (XQL) enables you to query data ingested into Cortex XDR for rigorous endpoint and network event analysis returning up to 1M results. To help you create an eﬀective XQL query with the proper syntax, the query ﬁeld in the user interface provides suggestions and deﬁnitions as you type. 

 XQL forms queries in stages. Each stage performs a specific query operation and is separated by a pipe character (|). Queries require a dataset, or data source, to run against. Unless otherwise specified, the query runs against the xdr_data dataset, which contains all log information that Cortex XDR collects from all Cortex product agents, including EDR data, and PAN NGFW data. In XDM queries, you must specify the dataset mapped to the XDM that you want to run your query against. 

 Important 

 Forensic datasets are not inlcuded by default in XQL query results, unless the dataset query is explicitly defined to use a forensic dataset. 

 Dataset query syntax 

 In a dataset query, unless otherwise specified, the query runs against the xdr_data dataset, which contains all log information that Cortex XDR collects from all Cortex product agents, including EDR data, and PAN NGFW data. In a dataset query, if you are running your query against a dataset that has been set as default, there is no need to specify a dataset. Otherwise, specify a dataset in your query. The Dataset Queries lists the available datasets, depending on system configuration. 

 Note 

 Users with different dataset permissions can receive different results for the same XQL query. 

 An administrator or a user with a predefined user role can create and view queries built with an unknown dataset that currently does not exist in Cortex XDR. All other users can only create and view queries built with an existing dataset. 

 When you have more than one dataset or lookup, you can change your default dataset by navigating to Settings → Configurations → Data Management → Dataset Management , right-click on the appropriate dataset, and select Set as default . For more information about setting default datasets, see Dataset management . 

 The basic syntax structure for querying datasets that are not mapped to the XDM is: 

 Ask Copy 

 dataset = <dataset name> 
 | <stage1> ... 
 | <stage2> ... 
 | <stage3> ... 

 or 

 Ask Copy 

 dataset in (<dataset name>) 
 | <stage1> ... 
 | <stage2> ... 
 | <stage3> ... 

 You can specify a dataset using one of the following formats, which is based on the data retention offerings available in Cortex XDR. 

 Hot Storage queries use the format dataset = <dataset name> . This is the default option. 

 Example: 

 Ask Copy 

 dataset = xdr_data 

 Cold Storage queries use the format cold_dataset = <dataset name> . 

 Example: 

 Ask Copy 

 cold_dataset = xdr_data 

 Note 

 You can build a query that investigates data in both a cold dataset and a hot dataset in the same query. In addition, as the hot storage dataset format is the default option and represents the fully searchable storage, this format is used throughout this guide for investigation and threat hunting. For more information on hot and cold storage, see Dataset management . 

 When using the hot storage default format, this returns every xdr_data record contained in your Cortex XDR instance over the time range that you provide to the Query Builder user interface. This can be a large amount of data, which may take a long time to retrieve. You can use a limit stage to specify how many records you want to retrieve. 

 There is no practical limit to the number of stages that you can specify. See Stages for information on all the supported stages. 

 In the xdr_data dataset, every user ﬁeld included in the raw data for network, authentication, and login events has an equivalent normalized user ﬁeld associated with it that displays the user information in the following standardized format: 

 <company domain>\<username> 

 For example, the login_data ﬁeld has the login_data_dst_normalized_user ﬁeld to display the content in the standardized format. To ensure the most accurate results, we recommend that you use these normalized_user ﬁelds when building your queries. 

 Additional components 

 XQL queries can contain different components, such as functions and stages, depending on the type of query you want to build. 

 Previous About the Query Builder 

 Next Get started with XQL queries 

 Last updated 1 month ago 

 Was this helpful?
