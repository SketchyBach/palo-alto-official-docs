---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/saas-security/saas-security/onboard-a-supported-saas-application/onboard-businessmap
fetched_at: 2026-09-06T10:07:19Z
source: cortex-platform
---

# Onboard Businessmap | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 SAAS SECURITY 

 SaaS Security 

 Onboard a Supported SaaS Application 

 Cortex Cloud Posture 

 Onboard Businessmap 

 Connect a Businessmap instance in Cortex Cloud Posture Management to detect posture risks and compliance violations. 

 For SaaS Security to detect posture risks in your Businessmap (formerly Kanbanize) instance, you must onboard your Businessmap instance to SaaS Security. Through the onboarding process, SaaS Security connects to a Businessmap API by using an API key that you generate from a Businessmap account. After connecting to the Businessmap API, SaaS Security scans your Businessmap instance for misconfigured settings and account risks. 

 To access your Businessmap instance, SaaS Security requires the following information, which you specify during the onboarding process. 

 API Key 

 A generated character string that identifies a Businessmap administrator to the Businessmap API. SaaS Security requires this API key to authenticate to the API. The key inherits the permissions of the administrator who creates it. Required permissions: The user who generates the API key must have the following Admin privileges: Manage Integrations, Access Audit Logs. 

 Host name 

 A unique subdomain for your Businessmap instance, which appears as part of your Businessmap URL. 

 To onboard your Businessmap instance, complete the following actions. 

 Step 1: Identify the Businessmap Account for API Key Generation 

 Identify the Businessmap account that you will use to generate the API key. 

 Required permissions: The account that generates the API key must have the following Admin privileges: 

 Manage Integrations 

 Access Audit Logs 

 Step 2: Log In to Businessmap 

 Open a web browser to the Businessmap login page or your unique company subdomain URL, and log in to the account you identified. 

 Step 3: Identify Your Host Name 

 After you log in to Businessmap, your host name appears as a unique subdomain in the URL. For example, <subdomain>.kanbanize.com. 

 Note: Make note of your host name before you continue to the next step. You will provide this host name to SaaS Security during the onboarding process. 

 Step 4: Generate and Copy an API Key 

 Click your profile icon in the top-right corner of the page and select API. Businessmap opens your My Account settings to the API tab. 

 If an API key was already generated for the account, it is shown on the API tab. If not, click Generate API key. 

 Copy your API key and paste it into a text file. 

 Note: Do not continue to the next step unless you have copied your API key. You will provide this key to SaaS Security during the onboarding process. 

 Step 5: Connect SaaS Security to Your Businessmap Instance 

 By adding a Businessmap app in Cortex, you enable SaaS Security to connect to your Businessmap instance. 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the app you want to connect to. 

 Click the Businessmap tile. 

 Under Capabilities , Enter a Name for your application. 

 Select Security Posture under Default Capabilities and click Next. 

 Under Connections , provide the API key and Host ID. 

 Under Configurations , select a Sync Interval . Choose a meaningful Tag to distinguish between various applications in different environments. 

 Click Next to complete the onboarding validation process. 

 Previous Onboard Automox 

 Next Onboard Celonis 

 Last updated 5 days ago 

 Was this helpful?
