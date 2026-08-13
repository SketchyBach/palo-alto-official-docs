---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/monitor-enterprise-dlp/save-evidence-for-investigative-analysis-with-enterprise-data-loss-prevention/set-up-sftp-storage-to-save-evidence
fetched_at: 2026-08-13T15:32:22Z
source: palo-alto-main
---

# Set Up SFTP Storage to Save Evidence Clear

Set Up SFTP Storage to Save Evidence 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Set Up SFTP Storage to Save Evidence 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 Save Evidence for Investigative Analysis with Enterprise DLP 

 Set Up SFTP Storage to Save Evidence 

 Download PDF 

 Enterprise DLP 

 Set Up SFTP Storage to Save Evidence 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Save Evidence for Investigative Analysis with Enterprise DLP 

 Next 

 Set Up Cloud Storage on AWS to Save Evidence 

 Set Up SFTP Storage to Save Evidence 

 Connect your SFTP server to store files that match your Enterprise Data Loss Prevention (E-DLP) data
 profiles. 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Prisma Browser 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Or any of the following licenses that include the Enterprise DLP license 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 To store files scanned by Enterprise Data Loss Prevention (E-DLP) , you must specify the SFTP server
 connectivity information to upload and write files to a target location on the SFTP
 server. Enterprise DLP creates a reportId folder
 on first upload to your SFTP server and uploads all subsequent files to the
 reportId folder within your folder path. Enterprise DLP automatically names files using the SFTP target folder location,
 default reportId folder, and filename. 

 The following special characters in a file name are not supported and prevent Enterprise DLP from saving files to SFTP storage: '/ \ * ?
 <>' . If you have a file name that includes one of these special
 characters, you must change the special character to an underscore
 ( _ ) so Enterprise DLP can save a copy of the
 file. 

 Enterprise DLP automatically sends email alerts to the data security
 administrator who originally connected Enterprise DLP to the SFTP storage
 bucket and to the data security admin who last modified the storage bucket settings
 in case of connection issues. Enterprise DLP sends the email alert every 48
 hours until you restore the connection between Enterprise DLP and the storage
 bucket. 

 Files not scanned while Enterprise DLP is disconnected from your storage
 bucket can't be stored and are lost. This means that all impacted files are not
 available for download. However, your data security administrator can still view
 all snippet data associated with the DLP incident . 

 Enterprise DLP automatically resumes forwarding files to your storage bucket
 after you restore the connection. 

 This procedure assumes you have already set up an SFTP server to save evidence for
 investigative analysis. 

 Review the setup prerequisites for Enterprise DLP and enable the required ports, fully qualified domain names
 (FQDN), and IP addresses on your network. 

 Allow all IP addresses for Evidence Storage in the region where you
 deployed the SFTP server so Enterprise DLP can write to your
 SFTP server. 

 Allow the IP or FQDN of the SFTP server on your network so Enterprise DLP can reach it. 

 Log in to 
 Strata Cloud Manager . 

 Access to evidence storage settings and files on Strata Cloud Manager is
 allowed only for an account administrator or app
 administrator role with Enterprise DLP read and write
 privileges. 

 Select Configuration Data Loss Prevention Settings Sensitive Data and navigate to Evidence
 Storage . 

 Select the enforcement points for which you want to enable Evidence Storage
 for. 

 You can enable evidence storage for Prisma Browser , Prisma Access , and Endpoint
 DLP. 

 Select Configure Regional Bucket SFTP . 

 Select the Region(s) from which you want to forward
 evidence files to the SFTP server. 

 You can associate SFTP servers in different regions with your DLP regions.
 When DLP incidents are generated in the regions you select here, Enterprise DLP forwards the incident evidence to the SFTP server. 

 Review the Instructions - SFTP and click
 Next . 

 In Input Bucket Details , configure the SFTP server
 connection settings. 

 Enter the Username of the SFTP server user used
 for secure file uploads. 

 The user must have read and write access to the SFTP server. 

 Enter the Private Key for the SFTP server. 

 This is required to authenticate the SSH connection to the SFTP
 server. The Private Key must include both the
 BEGIN RSA PRIVATE KEY and
 END RSA PRIVATE KEY prompts. 

 ( Optional ) Enter the public PGP Key to
 sign and encrypt files uploaded to the SFTP server. 

 Pretty Good Privacy (PGP) is an encryption program providing privacy
 and authentication for data communication, and used for signing,
 encrypting, and decrypting files. The PGP Key 
 must include both the BEGIN RSA PRIVATE
 KEY and END RSA PRIVATE
 KEY prompts. 

 Enter the Hostname of the SFTP server. 

 The Hostname can be a fully qualified domain
 name (FQDN) or an IPv4 address. 

 If you enter a FQDN, the FQDN must be publicly resolvable. If you
 enter an IPv4 address, the IP address must be public. Enterprise DLP can't connect to a private FQDN or IPv4
 address. 

 ( Optional ) Enter the Folder Path to
 specify the target location where files are uploaded on the SFTP
 server. 

 If no Folder Path is specified, Enterprise DLP creates the default
 reportId folder at the top-most
 folder the Username has read and write access
 to. The folder path for uploaded files depends on whether a
 Folder Path is specified. 

 Folder Path Specified —< folder
 path > /reportId/ < file
 name > 

 Folder Path Not
 Specified — /reportId/ < file
 name > 

 Enter the Port number through which files are
 uploaded to the SFTP server. 

 Palo Alto Networks recommends using Port 22 for file uploads to your
 SFTP server. For uncommon ports, Enterprise DLP needs to open
 the egress port for connection and upload. 

 Click Connect to connect Enterprise DLP 
 to your SFTP server. 

 Review the Connection Status to verify Enterprise DLP successfully connected to your SFTP server. 

 As part of the setup process, Enterprise DLP uploads a
 Palo_Alto_Networks_DLP_Connection_Test.txt 
 file to the target Folder Path on your SFTP server to
 test and verify connectivity. 

 Save the SFTP server settings if Enterprise DLP 
 successfully connected. 

 Select Previous and edit the connection settings if
 Enterprise DLP can't connect to your SFTP server. 

 ( Email DLP only ) Select Configuration SaaS Security Settings Email DLP Settings and enable Evidence Storage for Email DLP. 

 Enterprise DLP won't forward evidence files for Email DLP traffic
 matches unless you enable this setting. 

 Enable Sensitive Files for your enforcement
 points. 

 You can enable evidence storage of sensitive files for Prisma Access , NGFW , and Endpoint DLP. Enable 
 evidence storage when prompted to confirm. 

 Download Files for Evidence Analysis . 

 Previous 

 Save Evidence for Investigative Analysis with Enterprise DLP 

 Next 

 Set Up Cloud Storage on AWS to Save Evidence 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Administration 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Task 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
