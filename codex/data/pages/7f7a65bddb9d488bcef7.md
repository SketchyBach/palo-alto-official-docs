---
url: https://docs.prismacloud.io/content-collections/runtime-security/alerts/jira
fetched_at: 2026-09-16T13:35:29Z
source: prisma-cloud
---

# JIRA | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Runtime Security 

 Alerts 

 JIRA 

 Prisma Cloud continually scans your environment for vulnerabilities using the threat data in the Intelligence Stream. Prisma Cloud can open JIRA issues when new vulnerabilities are detected in your environment. This mechanism lets you implement continuous vulnerability assessment and remediation by hooking directly into the developer’s workflow. 

 New JIRA issues are opened when new vulnerabilities are found. A new issue is created for each discovery. Each JIRA issue lists the new vulnerabilities discovered, and a list of vulnerabilities that have already been reported but were still detected. 

 JIRA issues are opened based on policy. For example, an issue would be created when all of the following conditions are met: 

 You have a rule that alerts on critical vulnerabilities, 

 The rule is associated with your JIRA alert profile, 

 The Prisma Cloud scanner finds a critical vulnerability in an image in your environment. 

 Intelligent issue routing 

 You can leverage image labels to intelligently route alerts to the right team, and eliminate manual ticket triage. For example, if team-a is responsible for image-a, and a vulnerability is found in image-a, you could set up the alert to flow directly to team-a’s JIRA queue. 

 Intelligent routing depends on a Prisma Cloud feature called alert labels , where you define labels that Prisma Cloud should watch. When rules trigger, Prisma Cloud extracts the value of the label from the resource, and applies it to the next phase of alert processing. For JIRA alerts, you can use labels to specify the JIRA project key, JIRA labels, and JIRA issue assignee. 

 For example, if you have an image with the following labels: 

 Ask Copy 

 group=front-end-group 
 team=client-team 
 business-app=my-business-app 

 You could configure Prisma Cloud to open issues about this specific image in the JIRA project defined by the group label. 

 Configuring alert frequency 

 You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period. 

 Open Console, and go to Manage > Alerts . 

 In General settings , select the default frequency for all alerts. 

 You can specify Second , Minute , Hour , Day . 

 Integrating Prisma Cloud with JIRA 

 Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles. 

 Alert profiles consist of two parts: 

 (1) Alert settings — Who should get the alerts, and on what channel? Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on. 

 (2) Alert triggers — Which events should trigger an alert to be sent? Specify which of the rules that make up your overall policy should trigger alerts. 

 If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service. 

 Create new alert profile 

 Create a new alert profile. 

 In Manage > Alerts , click Add profile . 

 Enter a name for your alert profile. 

 In Provider , select JIRA . 

 Configure the channel 

 Configure the channel. 

 In Base URL , specify the location of your JIRA service. 

 In Credential , select the API Token that you added in the Manage > Authentication > Credentials Store page. 

 For more information, see Managing Jira Authentication in Prisma Cloud . 

 In CA certificate , enter a copy of the CA certificate in PEM format. 

 In Project key , enter a project key. 

 Alternatively, you can dynamically specify the project key based on a label. When an alert fires, the project key is taken from the label of the resource that triggered the action. To do so, click Select labels…​ , and choose a label that you know will contain the project key. If there are no labels in the drop-down list, go to Manage > Alerts > Alert Labels , and define them. 

 Enter an issue type. 

 Enter a priority. 

 Enter a comma delimited list of JIRA labels to apply to the issue. 

 You can dynamically define the list from a label. Click Select labels…​ , and select one or more labels. 

 Enter an assignee for the new issue. 

 You can dynamically define the assignee from a label. Click Select labels…​ , and select one or more labels. 

 Click Send Test Alert to test the connection. 

 Configure the triggers 

 In Select triggers , select the events that should trigger an alert to be sent. 

 To specify specific rules that should trigger an alert, deselect All rules , and then select any individual rules. 

 Click Next . 

 Managing Jira Authentication in Prisma Cloud 

 To integrate Jira with Prisma Cloud, you must configure authentication using API tokens. Jira Cloud and Jira Data Center (DC) no longer support password-based authentication for REST API access. Instead: 

 Jira Cloud requires an API token generated from your Atlassian account. 

 Jira DC supports authentication using Personal Access Tokens. 

 This section provides procedures for adding API tokens to the Credentials Store, updating existing credentials, and replacing credentials in Jira alert profiles. 

 Adding API Tokens in Credentials Store for Jira DC Authentication 

 To integrate Jira DC with Prisma Cloud, generate a Personal Access Token in Jira, store it in the Credentials Store in Prisma Cloud, and use it when adding a Jira profile. 

 Jira Data Center (DC) supports authentication with Personal Access Tokens instead of traditional passwords. For more information, see Using Personal Access Tokens . 

 To add an API token for Jira DC authentication, do the following: 

 Navigate to Manage > Authentication > Credentials Store . 

 Click Add Credential . 

 In the Create Credential window, complete the following fields: 

 Name – Enter a name for the credential. 

 Description – Add a description. 

 Type – Select API token . 

 Access Token – Enter the API token (use the Personal Access Token created in Jira DC) 

 Click Save to store the credential. 

 Adding API Tokens in Credentials Store for Jira Cloud Authentication 

 Jira Cloud requires an API token for authentication instead of traditional passwords. To integrate Jira Cloud with Prisma Cloud, generate an API token in Jira Cloud, store it in the Credentials Store in Prisma Cloud, and use it when adding a Jira profile. 

 For more information on creating cloud token from your Jira Cloud account, see Manage API tokens for your Atlassian account 

 To add an API token for Jira Cloud authentication, do the following: 

 Navigate to Manage > Authentication > Credentials Store . 

 Click Add Credential . 

 In the Create Credential window, complete the following fields: 

 Name – Enter a name for the credential. 

 Description – Add a description. 

 Type – Select Basic authentication . 

 Username – Add the email address used for the Jira Cloud account. 

 Password : Enter the API token (use the API token created in Jira Cloud) 

 Click Save to store the credential. 

 Updating Jira Cloud Credentials to Use an API Token 

 Jira Cloud no longer supports basic authentication with passwords. If you previously stored Jira Cloud credentials using a password, you must update the credential by replacing the password with an API token. 

 To update Jira Cloud credentials, do the following: 

 Navigate to Manage > Authentication > Credentials Store . 

 Select the Jira Cloud credential in the table, and click the Edit icon. 

 In the Edit Credential window, update the following fields: 

 Password – Replace the existing password with the API token generated in Jira Cloud. 

 Click Save to update the credential. 

 Replacing Credentials in an Existing Jira DC Alert Profile 

 When updating Jira DC authentication, you must replace the old credential with a new API token in the existing Jira alert profile. 

 To update the Jira DC alert profile with a new credential: 

 Navigate to Manage > Alerts > Alert Profiles . 

 Select the Jira alert profile you want to update and click the Edit icon. 

 In the Settings section, under Credential , select the API token that you added in the Manage > Authentication > Credentials Store page. 

 Click Next and then click Save . 

 Troubleshooting 

 Issue 1 

 Unable to Send Test Alert in JIRA due to the Error 'Failed to send JIRA test alert, error: request failed with status 400: Specify an issue type' despite configuring the Issue Type 

 Symptom 

 Unable to send test alert in JIRA due to the following error despite configuring the issue type: 

 Failed to send JIRA test alert, error: request failed with status 400: Specify an issue type 

 Reason The Issue Type configured in Prisma Cloud does not match the one set up in your JIRA environment. 

 Resolution 

 Log into your JIRA account 

 Navigate to the Project and check the available Issue Type 

 Update the Issue type in Prisma Cloud to match the one in JIRA (In the above example, the issue type is 'Email request') 

 Issue 2 

 Unable to Send Test Alert in JIRA due to the Error 'Failed to send jira test alert, error: request failed with status 400: Priority name '<name>' is not valid' despite configuring the Priority 

 Symptom 

 Unable to send test alert in JIRA due to the following error despite configuring the priority: 

 Failed to send jira test alert, error: request failed with status 400: Priority name '<name>' is not valid 

 Reason The Priority configured in Prisma Cloud does not match the one set up in your JIRA environment 

 Resolution 

 Log into your JIRA account 

 Navigate to the Project and check the configured Priority . 

 Update the Priority in Prisma Cloud to match the one in JIRA (In the above example, the Priority configured in JIRA is P1) 

 Previous Alert mechanism 

 Next Cortex XDR 

 Last updated 1 month ago 

 Was this helpful?
