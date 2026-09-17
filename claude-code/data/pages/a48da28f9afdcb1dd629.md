---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-saas-security/connect-a-saas-application/onboard-redis-labs
fetched_at: 2026-09-16T08:36:49Z
source: cortex-platform
---

# Onboard Redis Labs | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Cloud Security 

 Cortex Cloud SaaS Security 

 Connect a SaaS application 

 Cortex XSIAM 

 Onboard Redis Labs 

 Connect a Redis Labs instance in Cortex XSIAM to detect posture risks and compliance violations. 

 For SaaS Security to detect posture risks in your Redis Labs instance, you must onboard your Redis Labs instance to SaaS Security. Through the onboarding process, SaaS Security connects to the Redis Cloud REST API by using a pair of API keys that you generate within Redis Labs. After connecting to the Redis Cloud REST API, SaaS Security scans your Redis Labs instance for misconfigured settings and account risks. 

 To onboard your Redis Labs instance, SaaS Security requires the following information, which you specify during the onboarding process. 

 Item 

 Description 

 Account key 

 An API account key that Redis Labs generates the first time a Redis Labs account owner enables the REST API. The API account key is an alphanumeric string that uniquely identifies your Redis Labs account. SaaS Security uses this key and the API user key to authenticate to a Redis Labs API. 

 User key 

 An API user key that you create in Redis Labs and associate with a particular user. SaaS Security uses this key to authenticate to a Redis Labs API. Redis Labs authorizes requests from SaaS Security based on the key's role, which it inherits from the user associated with the key. 

 To onboard your Redis Labs instance, complete the following actions. 

 Step 1: Identify the Redis Labs Owner Account 

 Identify the Redis Labs user who will get the API account key and API user key. 

 Required Permissions: The user must be assigned to the Owner role in Redis Labs. The Owner role is required to enable the Redis Cloud REST API and to create an API user key. 

 Step 2: Log In to Redis Labs 

 Open a web browser to the Redis Labs login page and log in as the Owner you identified. 

 Step 3: Locate and Copy Your API Account Key 

 Redis Labs generates a unique API account key the first time a Redis Labs account Owner enables the REST API. This API account key appears on the Access Management page. 

 From the left navigation pane, select Access Management. 

 On the Access Management page, select the API Keys tab. If another Owner previously enabled the API, the API account key appears on this page. Otherwise, the page contains an Enable API button. 

 If necessary, click Enable API. 

 Copy the API account key and paste it into a text file. 

 Note : Do not continue to the next step unless you have copied the API account key. You will provide this key to SaaS Security during the onboarding process. 

 Step 4: Create and Copy an API User Key 

 When you create an API user key, you associate the key with a specific Redis Labs user. The key's permissions are based on the associated user's role. 

 On the Access Management page's API Keys tab, locate the API User Keys section. 

 In the API User Keys section, click the add button (+). Redis Labs displays an empty entry for you to configure your API user key. 

 In the empty entry, complete the following actions: 

 Specify an API key name. For effective logging, auditing, and future maintenance, supply a descriptive name that clearly identifies the purpose of the key. For example, SaaS Security-integration. 

 Select a User name from the list. The user you select must be assigned to the Owner role. 

 Click Create. Redis Labs generates and displays your API user key. 

 Copy the API user key and paste it into a text file. 

 Note : Do not continue to the next step unless you have copied the API user key. You will provide this key to SaaS Security during the onboarding process. 

 Step 5: Connect SaaS Security to Your Redis Labs Instance 

 By adding a Redis Labs app in Cortex, you enable SaaS Security to connect to your Redis Labs instance. 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the app you want to connect to. 

 Click the Redis Labs tile. 

 Under Capabilities , enter a name for your application. 

 Select Security Posture under Default Capabilities and click Next. 

 Under Connections , enter your API account key and API user key. 

 Under Configurations , select a Sync Interval. Choose a meaningful Tag to distinguish between various applications in different environments. 

 Click Next to complete the onboarding validation process. 

 Onboard a Redis Labs App to SaaS Security 

 Connect a Redis Labs instance to SaaS Security to detect posture risks. 

 SaaS Security connects to the Redis Cloud REST API using a pair of API keys that you generate in Redis Labs. After connecting, SaaS Security scans your Redis Labs instance for misconfigured settings and account risks. 

 The onboarding process requires the following credentials: 

 Item 

 Description 

 Account key 

 An API account key that Redis Labs generates the first time an account Owner enables the REST API. This alphanumeric string uniquely identifies your Redis Labs account. 

 User key 

 An API user key that you create in Redis Labs and associate with a specific user. Redis Labs authorizes requests based on the key's role, which it inherits from the associated user. 

 Step 1 — Identify the Owner account 

 Identify the Redis Labs user who will retrieve the API account key and create the API user key. 

 Required permissions: The user must be assigned the Owner role in Redis Labs. The Owner role is required to enable the Redis Cloud REST API and to create an API user key. 

 Step 2 — Log in to Redis Labs 

 Open a browser to app.redislabs.com and log in as the Owner you identified in Step 1. 

 Step 3 — Get the API account key 

 Redis Labs generates a unique API account key the first time an account Owner enables the REST API. The key appears on the Access Management page. 

 From the left navigation pane, select Access Management. 

 Select the API Keys tab. 

 If another Owner previously enabled the API, the account key appears on this page. 

 If not, click Enable API to generate the key. 

 If necessary, click Enable API. 

 Copy the API account key and save it to a text file. 

 Note : Do not proceed to the next step until you have copied the API account key. You will provide this key during the onboarding process. 

 Step 4 — Create an API user key 

 When you create an API user key, you associate it with a specific Redis Labs user. The key's permissions are based on that user's role. 

 On the Access Management page, select the API Keys tab. 

 In the API User Keys section, click the + (add) button. Redis Labs displays an empty entry for you to configure. 

 Complete the following fields: 

 API key name — Enter a descriptive name that identifies the key's purpose. For example, SaaS-Security-integration. 

 User name — Select a user assigned to the Owner role. 

 Click Create. Redis Labs generates and displays the API user key. 

 Copy the API user key and save it to a text file. 

 Note : Do not proceed to the next step until you have copied the API user key. You will provide this key during the onboarding process. 

 Step 5 — Connect SaaS Security to Redis Labs 

 Log in to Cortex . 

 Select Settings > Data Sources and Integrations > Add New and click the Redis Labs tile. 

 On the Capabilities tab, enter a name for this instance. 

 Under Default Capabilities, confirm Security Posture is selected. 

 Click Next. 

 On the Connections tab, enter your API account key and API user key. 

 Click Next. 

 On the Configurations tab: 

 Set the Sync Interval. 

 (Optional) Add a Tag. 

 Click Next to complete onboarding. 

 Previous Onboard PagerDuty 

 Next Onboard Salesforce 

 Last updated 2 days ago 

 Was this helpful?
