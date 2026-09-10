---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x-rn/cortex-xdr-release-information/known-issues-xdr
fetched_at: 2026-09-06T10:53:11Z
source: cortex-platform
---

# Known Issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XDR 

 Cortex XDR 3.x 

 Release Information 

 Known Issues 

 The Cortex XDR release includes the following known issues: 

 Issue ID 

 Description 

 CPATR-25409 

 In some cases, when the XDR Collectors is installed on a Linux platform, the XDR Collectors fails to register due to an incorrect operating system version. As a workaround, remove the agilitytools application and restart XDR Collectors. 

 CPATR-20105 

 When performing a XDR Collectors installation or upgrade in Linux using a shell installer, the /tmp folder cannot be marked as noexec . Otherwise, the installation or upgrade fails. As a workaround, before the installation or upgrade, use the following command: 

 Ask Copy 

 mount -o remount,exec /tmp 

 The deb and rpm installations work fine without any problems. 

 CRTX-57553 

 When setting up the Broker VM on Google Cloud Platform (GCP) and a GCP image is imported using the G Cloud CLI, the following command fails. 

 gcloud compute images import <VMDK image> --os=ubuntu-1804 --source-file="gs://<image path>" --network=<network_name> --subnet=<subnet_name> --zone=<region> --async 

 Until this is resolved as a workaround, use the following command. 

 gcloud compute images import <VMDK image> --data-disk --source-file="gs://<image path>" --network=<network_name> --subnet=<subnet_name> --zone=<region> --async 

 CRTX-41336 

 A Database Collector applet on a broker VM that is deployed in a Cortex XDR FedRAMP environment cannot connect to MySQL and MSSQL. 

 XDR-55313 

 When exporting Restriction type profile with custom indicator rules and then importing those back, the rules are no longer available. 

 CPATR-15036 

 Cortex XDR only supports stitching login Windows Event Logs into stories for a Windows 8.1 or later machine. 

 XDR-30122 

 When your XQL query includes a filter with a result that is an exponential number, the filter can sometimes not work as expected, including not returning any results. 

 XDR-29691 

 Cortex XDR calculates CVEs for applications according to the application version, and not according to application build numbers. 

 XDR-21780 

 Backwards scan is not supported when generating a BIOC from the Native Search. 

 CPATR-10766 

 After a Microsoft Windows patch (KB) is uninstalled from the endpoint, the Cortex XDR agent continues to report this KB to Cortex XDR. As a result, the CVEs list for the endpoint in Vulnerability Management cannot be updated to include the CVEs addressed by the uninstalled KB. 

 Previous Cortex XDR Agent Release Information 

 Next Previous Maintenance Releases 

 Last updated 16 days ago 

 Was this helpful?
