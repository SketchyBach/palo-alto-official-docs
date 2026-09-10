---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/onboard-and-configure-cortex-xdr/deployment-steps/step-4-configure-and-deploy-cortex-xdr/cortex-xdr-analytics/configure-cortex-xdr-network-parameters
fetched_at: 2026-09-06T09:47:48Z
source: cortex-platform
---

# Configure Cortex XDR network parameters | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Onboard and configure Cortex XDR 

 Deployment steps 

 Step 4: Configure and deploy Cortex XDR 

 Cortex XDR - Analytics 

 Cortex XDR 3.x 

 Configure Cortex XDR network parameters 

 Define your internal IP address ranges and domain names to enable Cortex XDR to identify, track, and analyze network assets. 

 Define internal IP address ranges 

 The IP Address Ranges page displays the address ranges that Cortex XDR - Analytics monitors. Addresses are pre-populated with the default IPv4 and IPv6 address spaces. The names you define will appear when investigating the network-related events in Cortex XDR. 

 You can add a new IP address range manually or upload IP address ranges from a CSV file. 

 How to define internal IP address ranges 

 Select Assets → Network Configuration → Internal IP Address Ranges . 

 Do one of the following: 

 To 

 Do this 

 Add a new IP address manually 

 1. Click Add New Range → Create New , and then enter the IP address name and IP address range or CIDR values. 

 By default, Cortex XDR creates Private Network ranges that specify reserved industry-approved ranges. Private Network ranges are marked with a icon and you can only edit the name. 

 Note 

 You can add a range that is fully contained in an existing range, however, you cannot add a new range that partially intersects with another range. 

 2. Click Save . 

 Upload IP address ranges from a CSV file 

 1. Select Assets → Network Configuration → Internal IP Address Ranges . 

 2. Click Add New Range → Upload from File . 

 3. Locate the CSV file you want to upload, and then click Add . 

 Define internal domain names 

 Select Assets → Network Configuration → Internal Domain Suffixes . 

 Type the domain suffix you want to include as part of your internal network, for example, acme.com . 

 Select to add the suffix to the Domains List . 

 Previous Cortex XDR - Analytics 

 Next Enable the Analytics Engine and Identity Analytics 

 Last updated 10 days ago 

 Was this helpful?
