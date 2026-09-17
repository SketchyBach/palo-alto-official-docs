---
url: https://cortex-docs.paloaltonetworks.com/xpanse-api/
fetched_at: 2026-09-16T09:12:58Z
source: cortex-platform
---

# Get Started with Xpanse APIs | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex Xpanse 

 Xpanse APIs 

 Get Started with Xpanse APIs 

 Using the Cortex Xpanse APIs, you can integrate Cortex Xpanse with third-party apps or services to ingest alerts, services, assets, and IP ranges and leverage investigation capabilities. The APIs allow you to manage incidents in a ticketing or automation system of your choice by reviewing and editing the incident's details, status, and assignee. 

 Before you can begin using Cortex Xpanse APIs, you must generate the following items from the Cortex Xpanse console: 

 Value 

 Description 

 API Key 

 The API Key is your unique identifier used as the Authorization:{key} header required for authenticating API calls. Depending on your desired security level, you can generate two types of API keys, Advanced or Standard, from your Cortex Xpanse app. 

 API Key ID 

 The API Key ID is your unique token used to authenticate the API Key. The header used when running an API call is x-xdr-auth-id:{key_id} . 

 FQDN 

 The FQDN is a unique host and domain name associated with each tenant. When you generate the API Key and Key ID, you are assigned an individual FQDN. 

 Cortex XPanse API URIs are made up of your unique FQDN, the API name, and name of call. For example, https://api-{fqdn}/public_api/v1/{name of api}/{name of call}/. 

 The following steps describe how to generate the necessary key values: 

 Get your Cortex Xpanse API Key. 

 In Cortex Xpanse, navigate to Settings > Configurations > Integrations > API Keys . 

 Select + New Key . 

 Choose the type of API Key you want to generate based on your desired security level: Advanced or Standard . The Advanced API key hashes the key using a nonce, a random string, and a timestamp to prevent replay attacks. cURL does not support this but is suitable with scripts. Use the provided script to create the advanced API authentication token. 

 Note 

 To integrate with Cortex XSOAR you must generate a Standard Key. 

 If you want to define a time limit on the API key authentication, mark Enable Expiration Date and select the expiration date and time. Navigate to Settings > Configurations > Integrations > API Keys to track the Expiration Time field for each API key. In addition, Cortex Xpanse displays a API Key Expiration notification in the Notification Center one week and one day prior to the defined expiration date. 

 Provide a comment that describes the purpose for the API key, if desired. 

 Select the desired level of access for this key. You can select existing Roles , or you can select Custom to set the permissions on a more granular level. 

 Note 

 Be sure to select a role with View/Edit access for the Public API. Use the predefined Instance Administrator role or a create a custom role with Public API permission. Roles are described in the Manage Roles section of the Cortex Xpanse User Guide. 

 Generate the API Key. 

 Copy the API key, and then click Done . This value represents your unique Authorization:{key} . 

 You will not be able to view the API Key again after you complete this step. Ensure that you copy it before closing the notification. 

 Get your Cortex Xpanse API Key ID. 

 In the API Keys table, locate the ID field. 

 Note your corresponding ID number. This value represents the x-xdr-auth-id:{key_id} token. 

 Get your FQDN. 

 Right-click your API key and select View Examples . 

 Copy the CURL Example URL. The example contains your unique FQDN: https://api-{fqdn}/public_api/v1/{name of api}/{name of call}/ 

 You can use the CURL Example URL to run the APIs. 

 Make your first API call. The following examples vary depending on the type of key you select. You can test authentication with Advanced API keys using the provided Python 3 example. With Standard API keys, use either the cURL example or the Python 3 example. Don’t forget to replace the example variables with your unique API key, API key ID, and FQDN tenant ID. After you verify authentication, you can begin making API calls. 

 Next What's new in this release 

 Last updated 1 month ago 

 Was this helpful?
