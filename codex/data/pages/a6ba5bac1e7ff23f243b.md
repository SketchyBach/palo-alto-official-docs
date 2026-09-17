---
url: https://docs.prismacloud.io/admin-guide/32/vulnerability-management/registry-scanning/scan-coreos-quay
fetched_at: 2026-09-16T13:37:29Z
source: prisma-cloud
---

# Scan CoreOS Quay Registry | 32 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 32 

 Vulnerability Management 

 Registry Scans 

 Scan CoreOS Quay Registry 

 To scan a repository in CoreOS Quay , configure the registry. 

 Prerequisites 

 You have installed a Defender somewhere in your environment. 

 Configure a CoreOS Quay Registry Scan 

 Log in to Console, and select Defend > Vulnerabilities > Images > Registry settings . 

 Select Add registry and enter the details: 

 In Version , select CoreOS Quay . 

 In Registry (Optional) enter the Fully Qualified Domain Name (FQDN) for the CoreOS Quay registry server. 

 To configure a self-hosted registry, enter an IP address, while for the SaaS version, provide the registry URL. 

 In Repository , enter the name of the repository to scan. 

 Optionally enter the Repositories to exclude them from being scanned. 

 Enter Tag numbers to scan, leave blank, or enter a wildcard (*) to scan all the tags. 

 Optionally, enter Tags to exclude , to avoid scanning images with specified tags. 

 In Credential , configure how Prisma Cloud authenticates with CoreOS Quay. 

 Select the credential for CoreOS Quay from the drop-down list. 

 If there are no credentials in the list, click Add new to create new credentials under Manage > Authentication > Credentials Store . 

 In OS type , specify whether the repo holds Linux or Windows images. 

 In Scanners scope , specify the collections of defenders to use for the scan. 

 In Number of scanners , enter the number of Defenders across which scan jobs can be distributed. 

 In Cap , limit the number of images to scan. 

 Set Cap to 5 to scan the five most recent images, or enter a different value to increase or decrease the limit. Set Cap to 0 to scan all images. 

 Select Add and scan . 

 Verify that the images in the repository are being scanned under Monitor > Vulnerabilities > Images > Registries . 

 Previous OpenShift integrated Docker registry 

 Next Trigger Registry Scan with Webhooks 

 Last updated 2 months ago 

 Was this helpful?
