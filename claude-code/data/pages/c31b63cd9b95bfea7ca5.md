---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/the-prisma-access-browser-extension/prisma-browser-extension-bulk-extension-id-import
fetched_at: 2026-08-13T17:23:29Z
source: palo-alto-main
---

# Prisma Browser Extension Bulk Extension ID Import Clear

Prisma Browser Extension Bulk Extension ID Import 

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

 Prisma Browser Extension Bulk Extension ID Import 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 The Prisma Browser Extension 

 Prisma Browser Extension Bulk Extension ID Import 

 Download PDF 

 Prisma Browser 

 Prisma Browser Extension Bulk Extension ID Import 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Prisma Browser Extension History Collection 

 Next 

 Prisma Browser Extension - Best Practices 

 Prisma Browser Extension Bulk Extension ID Import 

 Bulk Extension ID import 

 You can import multiple browser extension IDs at the same time to configure Allow and
 Block rules in Allowed or Blocked Extensions control. 

 In large-scale environments with hundreds or thousands of extensions, adding IDs manually
 is inefficient and error-prone. This enhancement streamlines bulk configuration and
 policy management by enabling CSV or plain-text uploads. 

 This feature provides a simple and scalable way for you to upload and manage
 lists of browser extension IDs used in Block Specific Extensions or Allow
 Specific Extensions policies. 

 The feature supports file uploads, validation, deduplication, and real-time
 feedback to enhance policy accuracy and usability. 

 Requirements and Implementation Details 

 Input methods 

 You can add multiple extension IDs in eirher .csv or .txt formats. You can also add
 extensions manually.. 
 .csv file - One extension ID per cell, one cell per row. 
 No header row 

 .txt file - One extension per line, OR separated by commas or
 semicolons. 

 Manual input - You can paste a list of extensions directly into the
 control field. 

 File Uploader Behavior 
 Accepts files in .csv or .txt only. 

 Automatically parses and displays valid entries. 

 Displays validation feedback for errors, duplicates, or formatting
 issues 

 Validation Rules 

 Each extension ID needs to meet the standard Chrome ID format. 

 Validation Type Rule 

 Format Check 32- character, lowercase alphanumeric string. 

 Duplicates Duplicate IDs are flagged with a warning and automatically
 deduplicated. 

 Multiple Errors IDs can trigger multiple validation errors (e.g., invalid +
 duplicate). 

 File Errors Invalid file type or parse failure. 

 Actions 

 The following actions are supported, as part of the Add List of Serial
 Numbers feature: 
 Clear all - Remove all entered or parsed extension IDs. 

 Clear Individual Row - Delete a single entry from the list. 

 Extension search 

 Search for an extension ID before adding it to confirm validity
 or view details. 

 Display results including: 
 Extension name 

 Icon (if available) 

 Audit Logging 

 All bulk updates using this feature generate entries in the Audit Logs page. 

 Log Type Description 

 Rule Created/Updated Lists all extension IDs added or modified in the policy rule
 for blocking or allowing extensions. 

 Downloadable Sample Files 

 You can download sample files to understand the required format for uploads. 

 Available Sample Files 
 Sample csv file - sample_extensions.csv 

 Sample txt file - sample_extensions.txt 

 Included Example Data 

 Extension ID Description 

 aapbdbdomjkkjkaonfhkkikfgjllcleb Google Translate 

 kgjfgplpablkjnlkjmjdecgdpfankdle Zoom 

 Previous 

 Prisma Browser Extension History Collection 

 Next 

 Prisma Browser Extension - Best Practices 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Remote Browser Isolation 

 Prisma Browser 

 Administration 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
