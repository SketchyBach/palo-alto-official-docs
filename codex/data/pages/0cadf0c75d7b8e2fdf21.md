---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/administration/configure-enterprise-dlp/data-dictionaries/add-a-data-dictionary.html
fetched_at: 2026-09-16T13:01:42Z
source: palo-alto-main
---

# Add a Data Dictionary Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Data Dictionaries 

 Add a Data Dictionary 

 Download PDF 

 Enterprise DLP 

 Add a Data Dictionary 

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

 Add a Data Dictionary 

 Add a new data dictionary to Enterprise Data Loss Prevention (E-DLP) . 

 If you want to upload a data dictionary to a region-specific storage bucket , allow
 the region-specific Public API URL and Storage
 Bucket on your network. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration Data Loss Prevention Detection Methods Data Dictionary and Add Custom Dictionary . 

 Enter a descriptive Name for the data dictionary. 

 The data dictionary must have a unique name. The upload fails if a data
 dictionary with an identical name already exits. 

 Special characters are not supported. 

 ( Optional ) Enter a Description for the data
 dictionary. 

 Enterprise DLP doesn't support special characters in the data dictionary
 description. 

 Select the data dictionary Category . 

 Enterprise DLP uses the data dictionary category to group together
 similar types of data dictionaries for administrative purposes. 

 You can specify one of the following predefined categories—Academia,
 Confidential, Employment, Financial, Government, Healthcare, Legal,
 Marketing, or Source Code. 

 Select the Region where you want to upload and store
 your data dictionary. 

 Specify whether keywords are Case Sensitive . 

 This settings instructs Enterprise DLP to treat uppercase and lowercase
 letters for all keywords in the data dictionary as distinct (case sensitive)
 if enabled or as equivalent (case insensitive) if disabled. 

 In the Keywords section, drag and drop the data
 dictionary file or Browse Files to navigate to and select
 the data dictionary file. 

 Only one data dictionary file can be uploaded at a time. Upload will fail if
 you attempt to upload multiple data dictionaries at one time. 

 Enterprise DLP displays a preview of the keywords
 and the total number of keywords included in the data dictionary you
 uploaded. The Keywords Differences section
 specifies that you're adding new keywords. You can click View
 All to view the full list of keywords. 

 You have the option to Edit and
 modify the keyword list if needed. View the Update 
 procedure for details about editing a data dictionary you uploaded to Enterprise DLP . 

 Create the new data dictionary. 

 Verify that the data dictionary was successfully uploaded. 

 Create or modify a data profile to add your
 data dictionary. 

 Data dictionaries compliment the match criteria in your advanced and nested
 data profiles and increase the likelihood of positive detections.
