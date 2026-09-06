---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-classification/cortex-cloud-data-classification
fetched_at: 2026-09-06T10:06:57Z
source: cortex-platform
---

# About Cortex Cloud Data Classification | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cortex Cloud Data Classification 

 Cortex Cloud Posture 

 About Cortex Cloud Data Classification 

 Learn how Cortex Cloud Data Classification discovers and classifies sensitive data. 

 What is Cortex Cloud Data Classification? 

 To access Data Classification management, click Settings → Configurations → Data Classification . 

 The main screens of Data Classification management are: 

 Data Patterns: Types of data that are discoverable on a data object, such as credit card numbers, social security numbers (SSNs), and email addresses. Cortex Cloud Data Classification provides a complete list of hundreds of out-of-the-box patterns. Scroll to the right to see more information about each pattern (description, region and state location, whether enabled). You can disable the data patterns that are not relevant for you. For more information, see How to disable and enable data patterns in Data Classification . 

 Data Profiles: A data profile defines a data-related business case and is applied to a data object such as a file or field. Six major data profiles are included out-of-the-box: 

 Developer Secrets : Sensitive pieces of information, such as API keys, passwords, tokens, and other credentials, that are used to authenticate and access various resources, services, and APIs. These secrets play a crucial role in securing applications and systems by validating the identity and permissions of users or applications. 

 Financial : A collection of information and data related to an individual or an organization's financial status, transactions, investments, assets, liabilities, income, expenses, and other financial activities. This profile includes details such as bank account information, credit card details, investment portfolios, income statements, tax returns, and any other financial records that provide a comprehensive view of a person or entity's financial health and behavior. 

 PCI : A set of information and data related to Payment Card Industry (PCI) compliance requirements and standards. This profile includes details such as credit card numbers, expiration dates, security codes (CVV/CVC), and any other data associated with processing payment transactions securely and in accordance with PCI Data Security Standards (PCI DSS). 

 PHI : A collection of information and data related to Protected Health Information (PHI), which includes sensitive and confidential health-related data about individuals. This profile may contain details such as health insurance information, patient identifiers, HIPAA related identifiers, ICD identifiers, and any other data that can be used to identify or link to an individual's health condition. 

 PII : Personally Identifiable Information (PII), which includes any data that can be used to identify or distinguish an individual uniquely. This profile may contain information such as full names, home addresses, email addresses, phone numbers, social security numbers, driver's license numbers, passport numbers, and other personal identifiers that can be linked to a specific person. 

 Sensitive : A broad range of information that is considered confidential, proprietary, or personally sensitive. This profile may include various types of data that we did not use to classify any other profile, such as internal IP addresses, internal classless inter-domain routing (CIDR), IP addresses, license plate numbers, MAC addresses, passwords, political views, religious beliefs, or SIM card numbers (ICCID). 

 Global Settings: By default, both the OCR scan and Collect Masked Patterns are relevant for all modules that are using data classification. In other words, these two settings are global and define the behavior of OCR and sample collection for all modules using data classification. 

 OCR (Optical Character Recognition): Enabled by default. When enabled, OCR extracts text from images. Disabling this option reduces scanning time but does not cover image classification. 

 Collect Masked Patterns : Collects three samples for each data pattern that was classified in each object (file or table) and is masked by the Data Classification engine in your environment. Data does not leave your environment before it is masked, therefore the full data is always protected. 

 Previous Page Reference F: Call-to-action routing by asset type1 

 Next How to create and validate a custom data pattern 

 Last updated 1 month ago 

 Was this helpful?
