---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/vendor-specific-data-sources-and-connectors/elastic/windows-dhcp-via-elasticsearch-filebeat/ingest-logs-from-windows-dhcp-using-elasticsearch-filebeat
fetched_at: 2026-09-06T09:23:42Z
source: cortex-platform
---

# Ingest logs from Windows DHCP using Elasticsearch Filebeat | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Vendor-specific data sources and connectors 

 Elastic 

 Windows DHCP via Elasticsearch Filebeat 

 Ingest logs from Windows DHCP using Elasticsearch Filebeat 

 Collect Windows DHCP data using Elasticsearch Filebeat with Cortex XSIAM. 

 You can configure Cortex XSIAM to receive Windows DHCP logs using Elasticsearch Filebeat with the following data collectors. 

 Ingest Windows DHCP logs with an XDR Collector profile 

 Extend Cortex XSIAM visibility into logs from Windows DHCP using an XDR Collector Windows Filebeat profile. 

 You can enrich network logs with Windows DHCP data when defining data collection in an XDR Collector Windows Filebeat profile. When you add a XDR Collector Windows Filebeat profile using the Elasticsearch Filebeat default configuration file called filebeat.yml , you can define whether the collected data undergoes follow-up processing in the backend for Windows DHCP data. Cortex XSIAM uses Windows DHCP logs to enrich your network logs with hostnames and MAC addresses that are searchable in XQL Search using the Windows DHCP Cortex Query Language (XQL) dataset ( microsoft_dhcp_raw ). 

 While this enrichment is also available when configuring a Windows DHCP Collector for a cloud data collection integration, we recommend configuring Cortex XSIAM to receive Windows DHCP logs with an XDR Collector Windows Filebeat profile because it’s the ideal setup configuration. 

 Configure Cortex XSIAM to receive logs from Windows DHCP using an XDR Collector Windows Filebeat profile. 

 Add an XDR Collector Profile for Windows . 

 Follow the steps for creating a Windows Filebeat profile as described in Add an XDR Collector Profile for Windows , and in the Filebeat Configuration File area, ensure that you select and Add the DHCP template. The template's content will be displayed here, and is editable.Add an XDR Collector Profile for Windows 

 To configure collection of Windows DHCP data, edit the template text as necessary for your system. 

 You can enrich network logs with Windows DHCP data when defining data collection by setting the vendor to “microsoft” , and product to “dhcp” in the filebeat.yml file, which you can then query in the microsoft_dhcp_raw dataset. 

 Note 

 To avoid formatting issues in filebeat.yml , edit the text file in the user interface. Do not copy it elsewhere. Validate the YAML syntax before creating the profile. 

 Ingest Windows DHCP logs with the Windows DHCP Collector 

 Extend Cortex XSIAM visibility into logs from Windows DHCP using Elasticsearch Filebeat with the Windows DHCP data collector. 

 To receive Windows DHCP logs, you must configure data collection from Windows DHCP via Elasticsearch Filebeat. This is configured by setting up a Windows DHCP Collector in Cortex XSIAM and installing and configuring an Elasticsearch Filebeat agent on your Windows DHCP Server. Cortex XSIAM supports using Filebeat up to version 8.0.1 with the Windows DHCP Collector. 

 Certain settings in the Elasticsearch Filebeat default configuration file called filebeat.yml must be populated with values provided when you configure the Data Sources & Integrations settings in Cortex XSIAM for the Windows DHCP Collector. To help you configure the filebeat.yml correctly, Cortex XSIAM provides an example file that you can download and customize. After you set up collection integration, Cortex XSIAM begins receiving new logs and data from the source. 

 Note 

 For more information on configuring the filebeat.yml file, see the Elastic Filebeat Documentation. 

 Windows DHCP logs are stored as CSV (comma-separated values) log files. The logs rotate by days ( DhcpSrvLog-<day>.log ), and each file contains two sections: Event ID Meaning and the events list. 

 As soon as Cortex XSIAM begins receiving logs, the app automatically creates a Windows DHCP XQL dataset ( microsoft_dhcp_raw ). Cortex XSIAM uses Windows DHCP logs to enrich your network logs with hostnames and MAC addresses that are searchable in XQL Search using the Windows DHCP Cortex Query Language (XQL) dataset. 

 Configure Cortex XSIAM to receive logs from Windows DHCP via Elasticsearch Filebeat with the Windows DHCP collector. 

 Configure the Windows DHCP Collector in Cortex XSIAM. 

 Navigate to Settings → Data Sources & Integrations. 

 On the Data Sources & Integrations page, click + Add New, search for Windows DHCP, then hover over it and click Add. 

 (Optional) Download example filebeat.yml file. To help you configure your filebeat.yml file correctly, Cortex XSIAM provides an example filebeat.yml file that you can download and customize. To download this file, use the link provided in this dialog box. 

 Note 

 To avoid formatting issues in your filebeat.yml , we recommend that you use the download example file to make your customizations. Do not copy and paste the code syntax examples provided later in this procedure into your file. 

 Specify a descriptive Name for your log collection configuration. 

 Save & Generate Token. The token is displayed in a blue box, which is blurred out in the image below. Click the copy icon next to the key and record it somewhere safe. You will need to provide this key when you set the api_key value in the Elasticsearch Output section in the filebeat.yml file as explained in Step #2 . If you forget to record the key and close the window you will need to generate a new key and repeat this process. 

 Select Done to close the window. 

 In the Integrations page for the Windows DHCP Collector that you created, select Copy api url and record it somewhere safe. You will need to provide this URL when you set the hosts value in the Elasticsearch Output section in the filebeat.yml file as explained in Step #2 . 

 Configure an Elasticsearch Filebeat agent on your Windows DHCP Server. 

 Navigate to the Elasticsearch Filebeat installation directory, and open the filebeat.yml file to configure data collection with Cortex XSIAM. We recommend that you use the download example file provided by Cortex XSIAM. 

 Update the following sections and tags in the filebeat.yml file. The example code below details the specific sections to make these changes in the file. 

 Filebeat inputs : Define the paths to crawl and fetch. The code below provides an example of how to configure the Filebeat inputs section in the filebeat.yml file with these paths configured. 

 Elasticsearch Output : Set the hosts and api_key , where both of these values are obtained when you configured the Windows DHCP Collector in Cortex XSIAM as explained in Step #1 . The code below provides an example of how to configure the Elasticsearch Output section in the filebeat.yml file and indicates which settings need to be obtained from Cortex XSIAM. 

 Processors : Set the tokenizer and add a drop_event processor to drop all events that do not start with an event ID. The code below provides an example of how to configure the Processors section in the filebeat.yml file and indicates which settings need to be obtained from Cortex XSIAM. 

 Note 

 The tokenizer definition is dependent on the Windows server version that you are using as the log format differs. 

 For platforms earlier than Windows Server 2008, use "%{id},%{date},%{time},%{description},%{ipAddress},%{hostName},%{macAddress}" 

 For Windows Server 2008 and 2008 R2, use "%{id},%{date},%{time},%{description},%{ipAddress},%{hostName},%{macAddress},%{userName},%{transactionID},%{qResult},%{probationTime},%{correlationID}" 

 For Windows Server 2012 and above, use "%{id},%{date},%{time},%{description},%{ipAddress},%{hostName},%{macAddress},%{userName},%{transactionID},%{qResult},%{probationTime},%{correlationID},%{dhcid},%{vendorClassHex},%{vendorClassASCII},%{userClassHex},%{userClassASCII},%{relayAgentInformation},%{dnsRegError}" 

 Verify the status of the integration. 

 Return to the Integrations page and view the statistics for the log collection configuration. 

 After Cortex XSIAM begins receiving logs from Windows DHCP via Elasticsearch Filebeat, you can use the XQL Search to search for logs in the new dataset ( microsoft_dhcp_raw ). 

 Previous Windows DHCP via Elasticsearch Filebeat 

 Next ElasticSearch 

 Last updated 1 month ago 

 Was this helpful?
