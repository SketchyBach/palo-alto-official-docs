---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/saas-security/saas-security/onboard-a-supported-saas-application/onboard-mural
fetched_at: 2026-09-16T08:45:20Z
source: cortex-platform
---

# Onboard Mural | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Saas Security 

 SaaS Security 

 Onboard a Supported SaaS Application 

 Cortex Cloud Runtime 

 Onboard Mural 

 Connect a Mural instance to detect posture risks and compliance violations. 

 For SaaS Security to detect posture risks in your Mural instance, you must onboard your Mural instance to SaaS Security. Through the onboarding process, SaaS Security connects to a Mural API by using an Enterprise API key. You generate this key from the Company Dashboard in Mural. After connecting to the Mural API, SaaS Security scans your Mural instance for misconfigured settings and account risks. 

 The supported Mural account plan for SaaS Security scans is the Enterprise plan. This plan is required for you to create an Enterprise API key. 

 To onboard your Mural instance, SaaS Security requires the following information, which you specify during the onboarding process. 

 Item 

 Description 

 API Key 

 A generated character string that gives SaaS Security access to Mural's Enterprise API. You configure this key to limit SaaS Security' access to only the scopes it requires. Required permissions: You must be a Company Admin to create the Enterprise API key. 

 To onboard your Mural instance, complete the following actions. 

 Step 1: Identify the Mural Account 

 Identify the Mural account that you will use to generate the Enterprise API key. 

 Required permissions: The account that generates the API key must be assigned to the Company Admin role in Mural. 

 Step 2: Log In to Mural 

 Open a web browser to the Mural login page and log in to the account you identified. 

 Step 3: Generate and Copy the Enterprise API Key 

 Navigate to the Company Dashboard in Mural. Locate your avatar in the upper-right corner of the Mural page and select <your-avatar> > Manage company. 

 From the Company Dashboard's left-hand navigation pane, select API keys. The API keys item appears under the Development section. 

 On the API Keys page, click Create API Key. The Create API key dialog prompts you to select the API scopes that the key will authorize SaaS Security to access. 

 In the Create API key dialog, select the following scopes, which SaaS Security requires: 

 Member information 

 User activity logs 

 Reports 

 Click Create API key. Mural generates and displays the Enterprise API key. 

 Copy the API key and paste it into a text file. 

 Note: Do not continue to the next step unless you have copied the API key. This is the only time that Mural displays the API key, and you must provide this key to SaaS Security during the onboarding process. 

 Step 4: Connect SaaS Security to Your Mural Instance 

 By adding a Mural app in Cortex, you enable SaaS Security to connect to your Mural instance. 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the app you want to connect to. 

 Click the Mural tile. 

 Under Capabilities , enter a name for your application. 

 Select Security Posture under Default Capabilities and click Next. 

 Under Connections , enter your API key. 

 Under Configurations , select a Sync Interval . Choose a meaningful Tag to distinguish between various applications in different environments. 

 Click Next to complete the onboarding validation process. 

 Previous Onboard MuleSoft 

 Next Onboard Office 365 

 Last updated 1 day ago 

 Was this helpful?
