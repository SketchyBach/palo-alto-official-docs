---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-saas-security/saas-ai-agent-security/onboard-saas-ai-agents/onboard-box-ai-agents
fetched_at: 2026-09-16T08:36:54Z
source: cortex-platform
---

# Onboard Box AI Agents | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Cloud Security 

 Cortex Cloud SaaS Security 

 SaaS AI Agent Security 

 Onboard SaaS AI Agents 

 Cortex XSIAM 

 Onboard Box AI Agents 

 Connect Box AI Agents in Cortex XSIAM SaaS Agent Security for visibility and control across your AI ecosystem. 

 Prerequisites 

 Ensure you have the necessary administrative privileges in your Box instance, including the ability to access the Admin and Dev console. 

 To access Box AI Studio and start building custom agents, your organization must have a Box - Enterprise Advanced license. If you would like to explore these capabilities, coordinate with your IT Administrator or Box Sales representative to ensure the proper licensing is in place. 

 Note : Box AI Studio is a Microsoft-native product, not a feature developed or managed by Palo Alto Networks. 

 Ensure you have enabled Box AI. To do this, go to your Box instance > Box AI > Settings and click Enable Box AI . 

 Create and Configure a Custom Box App 

 Sign in to your Box instance. 

 From the left navigation pane, select Dev Console > Create Platform App > Custom App. 

 On the Custom App page, enter the following information: 

 Give a suitable App Name. 

 Give a suitable Description (optional). 

 For Purpose, choose Automation from the drop-down and click Next. 

 Select Server Authentication (Client Credentials Grant) for the authentication method and click Create App. 

 On the newly created app page, select the Configuration tab. 

 In the OAuth 2.0 Credentials section, copy the Client ID and the Client Secret (Fetch Client Secret) and keep it handy for use during onboarding. 

 In the App Access Level section, choose App+Enterprise Access. 

 In the Application Scopes > Content Actions section, ensure you select the following checkbox options: 

 Read all files and folders stored in Box. 

 Write all files and folders stored in Box. 

 Manage AI. 

 Ensure you deselect all other checkbox options under Application Scopes > Administrative Actions and Application Scopes > Developer Actions. 

 Click Save Changes. 

 Back on the newly created app page, select Authorization > Review and Submit and then click Submit. Your new app will move to the Pending Authorization state. 

 Authorize the App in the Admin Console. 

 Click Back to My Account on the left navigation pane and select Admin Console > Integrations > Platform Apps Manager. 

 On the Server Authentication Apps list, find the app you created and select ... > Authorize App > Authorize. 

 Retrieve the Enterprise ID 

 Go Back to My Account > Dev Console and select the app you created. 

 Copy the Enterprise ID (available in the General Settings tab). 

 Note : Ensure you repeat the authorization process again if you modify any settings during configuration. 

 Onboard Box AI Agents to Cortex: 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the Box connector. 

 You may find multiple Box tiles, select the Box titled Box integration for SaaS Data and Posture Security for Box . Click on the tile and select the Add Another Instance. 

 On the Capabilities page, provide an Instance Name and select the Agent Security scanning capability. 

 On the Connections page, provide your Instance URL and select the Recommended authentication method. Provide your Client ID and Client Secret for the authentication flow. 

 Once Cortex validates the credentials and permissions, the onboarding process is complete. 

 Validation and Scanning : Cortex validates the credentials and permissions. After the validation is successful, you will see a confirmation message. Scanning begins immediately after a successful validation. The amount of time Cortex takes to scan varies based on the amount of scan data. At a minimum, it takes at least one hour to scan and display data in the Cortex dashboard. 

 Previous Onboard Atlassian Rovo 

 Next Onboard ChatGPT Enterprise 

 Last updated 2 days ago 

 Was this helpful?
