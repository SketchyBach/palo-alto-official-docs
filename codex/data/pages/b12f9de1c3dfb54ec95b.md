---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/detect-threats-and-analyze-data/asset-management/asset-inventory/all-assets
fetched_at: 2026-09-16T08:44:11Z
source: cortex-platform
---

# All Assets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Detect threats and analyze data 

 Asset management 

 Asset Inventory 

 Cortex XDR 3.x 

 All Assets 

 Cortex XDR enables you to view all external assets from the various asset categories on the All Assets page. 

 Note 

 Ingesting and Viewing Cloud Compute Instances for Cloud Inventory Assets requires a Cortex XDR Pro per GB license. 

 The All Assets page enables you to view all your assets from various asset categories. Each asset is available in Cortex XDR in different ways depending on the asset category and Cortex XDR license as explained in the following table. 

 Asset Category 

 Availability in Cortex XDR 

 License Required 

 On-prem 

 Automatically available 

 Any license 

 Cloud compute instance 

 Requires configuring either a Cloud Inventory data collector or Agents that are installed on the Cloud Compute Instances. 

 Cortex XDR Pro TB license 

 To view the All Assets page, select Assets → Asset Inventory . 

 By default, the All Assets page displays all assets according to the asset name. To search for specific assets, use the filters above the results table to narrow the results. You can export the tables and respective asset views to a tab-separated values (TSV) file. From the All Assets page, you can also manage the asset's output using the right-click pivot menu. 

 The All Assets table is comprised of a number of common fields that are available when viewing any of the Specific Assets pages. The TYPE field is only available in the All Assets table as this field determines the Specific Assets categories, and can be used to filter the different types of assets from the entire list of assets. 

 When any row in the table is selected, a side panel on the right with greater details is displayed, where you can view additional data divided by sections. The section heading names and data displayed change depending on the source of the assets. 

 The following table describes the fields that are available when viewing All Assets in alphabetical order. 

 Note 

 Certain fields are exposed and hidden by default. An asterisk (*) is beside every field that is exposed by default. 

 Field 

 Description 

 Active external services types* 

 An array column that displays all the active Service types observed for this asset. 

 ASM IDs 

 The ASM identifiers for this asset, indicate it is exposed to the Internet. 

 Business units* 

 A Business Unit is a designation to classify assets. tracks business units as a means to identify owning organizations of these assets. Business units become extremely important when an organization has subsidiaries and groups established through M&A activities. 

 Cloud provider* 

 The cloud provider used to collect these cloud assets is either GCP, AWS, or Azure. 

 Note 

 This field only displays with a Cortex XDR Pro TB license. 

 Cloud ID* 

 Displays the Resource ID as provided by the cloud provider. 

 Note 

 This field only displays with a Cortex XDR Pro TB license. 

 Externally detected providers* 

 The provider of the asset is determined by an external assessment. 

 First observed* 

 When the asset was first observed via any of the sources. 

 Has active external services* 

 A boolean value that displays whether the asset has any active external services. Use this filter to narrow down the asset inventory to internet-facing assets, and get a clear view of the organization's attack surface. 

 Has XDR agent* 

 Boolean value indicating if this asset has a Cortex XDR agent installed on it. 

 IP addresses* 

 Array column specifying a list of IPs associated with this asset. 

 IP range names* 

 Names of the IP address ranges allocated to the IP addresses. 

 Last observed* 

 When the asset was last observed via any of the sources. 

 MAC addresses* 

 MAC addresses associated with this asset. 

 Name* 

 Displays the name that describes the asset as provided by the source, if provided. 

 Operating system* 

 The operating system reported by the source for this asset. 

 Region* 

 Displays the region as provided by the Cloud provider. 

 Note 

 This field only displays with a Cortex XDR Pro TB license. 

 Sources* 

 An array column that displays all the sources that provided observations for this asset. 

 Type* 

 Type of asset, which can be defined as one of the following. 

 Note 

 The options available are dependent on your Cortex XDR license. 

 Cloud Compute Instance 

 On-Prem 

 This field is unique to the All Assets table. 

 XDR agent ID 

 If there is an endpoint installed on this asset, this is the endpoint ID. 

 Previous Asset Inventory 

 Next Specific Assets 

 Last updated 20 days ago 

 Was this helpful?
