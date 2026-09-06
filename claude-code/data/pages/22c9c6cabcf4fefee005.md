---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/saas-security/saas-security/onboard-a-supported-saas-application/onboard-youtrack
fetched_at: 2026-09-06T09:58:19Z
source: cortex-platform
---

# Onboard YouTrack | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Onboard YouTrack 

 Connect a YouTrack instance to detect posture risks and compliance violations. 

 SaaS Security connects to the YouTrack API using a permanent token that you generate from a YouTrack administrator account. After connecting, SaaS Security scans your YouTrack instance for misconfigured settings. 

 Onboarding consists of two tasks: 

 Collect the instance name and generate a permanent token 

 Connect SaaS Security to YouTrack 

 The onboarding process requires the following credentials: 

 Item 

 Description 

 Instance Name 

 The unique subdomain that identifies your organization's YouTrack instance, as shown in your YouTrack URL: <instance-name>.youtrack.cloud. 

 Permanent Token 

 A token generated from a YouTrack administrator account assigned to the System Admin role. The token must be scoped to YouTrack and YouTrack Administration. 

 Task 1 — Collect Information for Accessing Your YouTrack Instance 

 Step 1 — Identify your YouTrack instance name 

 Open a browser and go to your YouTrack login page. Your instance name is the subdomain shown in the URL: <instance-name>.youtrack.cloud. 

 Note : Record your instance name before proceeding. You must provide it during onboarding. 

 Step 2 — Generate a permanent token 

 Log in to YouTrack as an administrator assigned to the System Admin role. 

 Click your account avatar in the upper-right corner and select <your-avatar> > Profile. 

 On your profile page, go to Account Security. 

 In the Tokens section, click New token. 

 In the New Permanent Token dialog: 

 Enter a name for the token. 

 Select the following scopes: 

 YouTrack 

 YouTrack Administration 

 Click Create. YouTrack displays the new permanent token. 

 Click Copy token and save it to a text file. 

 Note: Do not proceed until you have copied the token. You must provide it during onboarding. 

 Task 2 — Connect SaaS Security to YouTrack 

 Log in to Cortex . 

 Select Settings > Data Sources and Integrations > Add New and click the YouTrack tile. 

 On the Capabilities tab, enter a name for this instance. 

 Under Default Capabilities, confirm Security Posture is selected. 

 Click Next. 

 On the Connections tab, enter your Instance Name and Permanent Token. 

 Click Next. 

 On the Configurations tab: 

 Set the Sync Interval. 

 (Optional) Add a Tag. 

 Click Next to complete onboarding. 

 Previous Onboard Wrike 

 Next SaaS Security Overview 

 Last updated 10 days ago 

 Was this helpful?
