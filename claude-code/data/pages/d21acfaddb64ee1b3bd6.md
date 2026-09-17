---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/endpoint-dlp/create-an-endpoint-dlp-policy-rule/create-an-endpoint-dlp-policy-rule-data-at-rest
fetched_at: 2026-09-15T15:10:22Z
source: palo-alto-main
---

# Create an Endpoint DLP Data at Rest Policy Rule Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Endpoint DLP 

 Create an Endpoint DLP Policy Rule 

 Create an Endpoint DLP Data at Rest Policy Rule 

 Download PDF 

 Enterprise DLP 

 Create an Endpoint DLP Data at Rest Policy Rule 

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

 Create an Endpoint DLP Data at Rest Policy Rule 

 Create a data at rest Endpoint DLP policy rule to scan managed endpoints for
 sensitive data stored locally. 

 Log in to 
 Strata Cloud Manager . 

 ( Optional ) Create one or more custom data profiles that support Local
 Detection. 

 Select Configuration Data Loss Prevention Endpoint DLP and click Create Scan . 

 Enterprise DLP supports only one data at rest policy rule per
 tenant. To detect multiple types of sensitive data, add multiple data
 profiles to the single data at rest policy rule. 

 Add an Endpoint Compatible data profile to the Data at
 Rest policy rule. 

 Click Add Local Data Profile to search for and select
 an Endpoint Compatible data profile. 

 Data at rest scanning supports predefined regex data
 profiles and custom data profiles that support Local
 Detection only. Endpoint DLP also supports Optical Character
 Recognition (OCR) detections. 

 Enable Trigger an Incident if you want inspected
 files on the endpoint that contain sensitive data to generate an
 incident. 

 This setting applies per data profile. 

 Enabled — Prisma Agent generates a DLP
 incident when it detects sensitive data when a
 file that matches a data profile. Scan results also appear
 in the Data Asset
 Explorer . 

 Disabled —No DLP incident is generated. Scan results
 appear in the Data Asset
 Explorer only. 

 Choose the Severity for files that match the
 data at rest policy rule. 

 The severity applies to all DLP incidents and assets displayed in the
 Data Asset Explorer for all files that match this data profile. You
 can select Critical, High, Medium, Low, or Informational. 

 Repeat this step to add additional Endpoint
 Compatible data profiles. 

 Select the File Types to include or exclude in the
 scan. 

 Any File Types (default)—Scan all supported file types . 

 ( Optional ) Exclude specific file
 types from the scan. 

 Select File Types —Scan only the file types you
 select. 

 Data at rest scanning supports files up to 100 MB. 

 ( Optional ) Configure the User scope to define
 which users the data at rest policy rule applies to. 

 Enable Apply Users match criteria to all enabled data
 profiles . 

 Select the Users 
 added using Cloud Identity Engine 
 whose endpoints you want to scan. 

 Any User (default)—Scan endpoints for
 all users. 

 ( Optional ) Exclude specific
 users or groups from inspection. 

 Select Users —Scan endpoints only for
 the users and groups you select. 

 ( Optional ) Exclude specific
 users or groups from inspection. 

 Configure the Folder Paths to define which directories
 on the endpoint the scan targets. 

 Enter the folder paths for each operating system separately. You can specify
 paths for macOS, Windows, or both. 

 Click Add Folder Path to include directories in the scan. 

 Prisma Agent inspects only actual files and directories within
 the specified paths, not symbolic links (shortcuts that point to files or
 directories in other locations). 

 Some examples of commonly configured folder paths include: 

 macOS Windows 

 /Users/*/Desktop C:\Users\*\Desktop 

 /Users/*/Documents C:\Users\*\Documents 

 /Users/*/Downloads C:\Users\*\Downloads 

 /Users/*/Library/CloudStorage/GoogleDrive-* C:\Users\*\AppData\Local\Google\Drive 

 /Users/*/Library/CloudStorage/OneDrive-* C:\Users\*\OneDrive - Company Name 

 Click Next to continue. 

 Review the policy rule Summary to verify the
 configuration is correct and click Save . 

 Push your Endpoint DLP policy rule. 

 Select Push Policies and click
 Push Policies . 

 ( Optional ) Enter a Description for the
 Endpoint DLP policy push. 

 Review the Push Policies scope to understand which Endpoint DLP policy
 rules and configuration changes are included in the push. 

 Click Push . 

 Review your Endpoint DLP Audit and Push
 Logs . 

 Review the Data Asset Explorer or your DLP incidents . 

 The Data Asset Explorer displays assets that match your data at rest policy
 rule regardless of whether a DLP incident was generated. 

 Prisma Agent generates a DLP incident when the data at rest scan
 detects sensitive data on an endpoint that matches the configured data
 profiles and you enabled Trigger an Incident for the
 matched data profile.
