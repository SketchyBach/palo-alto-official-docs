---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-saas-security/connect-a-saas-application/onboard-harness
fetched_at: 2026-09-16T08:36:47Z
source: cortex-platform
---

# Onboard Harness | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Onboard Harness 

 Connect a Harness instance in Cortex XSIAM to detect posture risks and compliance violations. 

 For SaaS Security to detect posture risks in your Harness instance, you must onboard your Harness instance to SaaS Security. Through the onboarding process, SaaS Security connects to a Harness API and, through the API, scans your Harness instance for misconfigured settings. If there are misconfigured settings, SaaS Security suggests a remediation action based on best practices. 

 SaaS Security gets access to your Harness instance through an API key. During the onboarding process, SaaS Security prompts you for the API key. 

 To onboard your Harness instance, complete the following actions: 

 Generate an API access key and personal access token 

 Connect SaaS Security to your Harness instance 

 Step 1: Generate an API Access Key and Personal Access Token 

 To access a Harness API, SaaS Security requires an API key that contains a personal access token of an administrator assigned to the Account Admin role. The API key inherits the permissions of the administrator who generates the key and token. 

 Open a web browser to the Harness site at www.harness.io and log in as an administrator assigned to the Account Admin role. 

 Required Permissions: You must log in as an administrator assigned to the Account Admin role. The account must also have permission to View and to Create/Edit authentication settings. 

 To open your profile, click the profile icon in the lower-left corner of the window. 

 On your profile, click + API Key. The New API Key dialog is displayed. 

 Enter a name for your key and click Save. The key appears in the My API Keys area. 

 For the new API key, click + Token. The New Token dialog is displayed. 

 Enter a name and expiration date for the token and click Generate Token. 

 Harness generates and displays the personal access token. Copy and paste the token into a text file so you can provide it to SaaS Security during onboarding. 

 Note : Do not continue to the next step unless you have copied the token. When SaaS Security prompts you for an API key during the onboarding process, enter this personal access token. 

 Step 2: Connect SaaS Security to Your Harness Instance 

 By adding a Harness app in Cortex, you enable SaaS Security to connect to your Harness instance. 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the app you want to connect to. 

 Click the Harness tile. 

 Under Capabilities , enter a name for your application. 

 Select Security Posture under Default Capabilities and click Next. 

 Under Connections , enter the API key (personal access token) for accessing your Harness instance. 

 Under Configurations , select a Sync Interval . Choose a meaningful Tag to distinguish between various applications in different environments. 

 Click Next to complete the onboarding validation process. 

 Previous Onboard Grammarly 

 Next Onboard Intercom 

 Last updated 2 days ago 

 Was this helpful?
