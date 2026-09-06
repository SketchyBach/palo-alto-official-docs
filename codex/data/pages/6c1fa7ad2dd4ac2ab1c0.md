---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/generic-on-premise-data-collectors/broker-vm-data-collector-applets/activate-cortex-network-scanner
fetched_at: 2026-09-06T09:41:20Z
source: cortex-platform
---

# Activate Cortex Network Scanner | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Cortex XDR Data Sources and Connectors 

 Generic on-premise data collectors 

 Broker VM data collector applets 

 Activate Cortex Network Scanner 

 Configure on-premises data collection for Cortex XDR. 

 The Cortex Network Scanner identifies and analyzes devices, services, and vulnerabilities in your internal network. It discovers responsive hosts within specified IP ranges, including on-premises and cloud environments. The scanner supports both non-authenticated and authenticated vulnerability scanning, with authenticated scans providing deeper insights through credential-based access. Scan results are seamlessly integrated into the inventory and vulnerability management views in Cortex XDR, providing a centralized view of all discovered assets, vulnerabilities, and issues. 

 Cortex Network Scanner is installed as an applet on a Broker VM. 

 License 

 Requires the Exposure Management add-on. 

 Important 

 The Cortex Network Scanner applet is not supported for FedRAMP customers. 

 Cortex Network Scanner does not support high availability (HA) Broker VM configuration. 

 Prerequisites 

 Review the Cortex Network Scanner deployment recommendations and complete any prerequisites. 

 Set up and configure Broker VM 

 How to activate Cortex Network Scanner 

 Navigate to Settings → Configurations → Data Broker → Broker VMs. 

 Right click the Broker VM, and select Add App → Network Scanner. 

 After the applet has installed, the scanner should automatically connect to the tenant. If the connection is successful, you’ll see a green dot next to Network Scanner in the Apps column of the Broker VMs table.
A red dot indicates that an error occurred and the scanner is not connected. 

 (Optional) Click on the network scanner in the table to display details about the scanner or to deactivate it. 

 Validate the installation. Navigate to Modules → Vulnerability & Exposure Management → Network Scanners → Network Scanners and find your new scanner in the list. The Network Scanners page displays all your deployed and configured scanners, along with additional details about each of them. After setting up a Broker VM and activating Cortex Network Scanner, refer to Get started with Cortex Network Scanner for information about adding networks, adding credentials for authenticated scans, and configuring scans. 

 Previous Activate Apache Kafka Collector 

 Next Activate CSV Collector 

 Last updated 29 days ago 

 Was this helpful?
