---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/data-ingestion/external-data-ingestion/ingest-authentication-logs-and-data/ingest-logs-and-data-from-google-workspace
fetched_at: 2026-09-06T09:50:34Z
source: cortex-platform
---

# Ingest Logs and Data from Google Workspace | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Data management 

 Data Ingestion 

 External data ingestion 

 Ingest authentication logs and data 

 Cortex XDR 3.x 

 Ingest Logs and Data from Google Workspace 

 Ingest logs and data from Google Workspace for use in Cortex XDR. 

 Notice 

 Ingestion of logs and data requires a Cortex XDR Pro per GB license. 

 Cortex XDR can ingest the following types of data from Google Workspace, where most of the data is collected as audit events from various Google reports, using the Google Workspace data collector. 

 Google Chrome 

 Admin Console 

 Google Chat 

 Enterprise Groups 

 Login 

 Rules 

 Google drive 

 Token 

 User Accounts 

 SAML 

 Alerts 

 Emails—Requires a compliance mailbox to ingest email data (not email reports). 

 All message details except email headers and email content ( payload.body , payload.parts , and snippet ). 

 The following Google APIs are required to collect the different types of data from Google Workspace. 

 For all data types, except emails: Admin SDK API . 

 For all data types, except alerts and emails: Admin Reports API (part of Admin SDK API). 

 Note 

 For all types of data collected via the Admin Reports API, except alerts and emails, the log events are collected with a preset lag time as reported by Google Workspace. For more information on these lag times for the different types of data, see Google Workspace Data retention and lag times . 

 Alerts require implementing an additional API: Alert Center API (part of Admin SDK API). 

 Emails require implementing the Gmail API . 

 To receive logs from Google Workspace for any of the data types except emails, you must first enable the Google Workspace Admin SDK API with a user with access to the Admin SDK Reports API. For emails, you must set up a compliance email account as explained in the prerequisite steps below and then enable the Google Workspace Gmail API. Once implemented, you can then configure the Collection Integrations settings in Cortex XDR. After you set up data collection, Cortex XDR begins receiving new logs and data from the source. 

 When Cortex XDR begins receiving logs, the app creates a new dataset for the different types of data that you are collecting, which you can use to initiate XQL Search queries. For example queries, refer to the in-app XQL Library. For all logs, Cortex XDR can raise Cortex XDR alerts for Correlation Rules only, when relevant from Google Workspace logs. 

 For the different types of data you can collect using the Google Workspace data collector, the following table lists the different datasets, vendors, and products automatically configured, and whether the data is normalized. 

 Data type 

 Dataset 

 Vendor 

 Product 

 Normalized data 

 Google Chrome 

 google_workspace_chrome_raw 

 Google 

 Workspace Chrome 

 — 

 Admin console 

 google_workspace_admin_console_raw 

 Google 

 Workspace Admin Console 

 When relevant, Cortex XDR normalizes Admin Console audit logs into authentication stories. All SaaS audit logs are collected in a dataset called saas_audit_logs and specific relevant events are collected in the authentication_story preset for the xdr_data dataset. 

 Google Chat 

 google_workspace_chat_raw 

 Google 

 Workspace Chat 

 — 

 Enterprise groups 

 google_workspace_enterprise_groups_raw 

 Google 

 Workspace Enterprise Groups 

 When relevant, Cortex XDR normalizes Enterprise Group audit logs into authentication stories. All SaaS audit logs are collected in a dataset called saas_audit_logs and specific relevant events are collected in the authentication_story preset for the xdr_data dataset. 

 Login 

 google_workspace_login_raw 

 Google 

 Workspace Login 

 When relevant, Cortex XDR normalizes Login audit logs into authentication stories. All SaaS audit logs are collected in a dataset called saas_audit_logs and specific relevant events are collected in the authentication_story preset for the xdr_data dataset. 

 Rules 

 google_workspace_rules_raw 

 Google 

 Workspace Rules 

 When relevant, Cortex XDR normalizes Rules audit logs into authentication stories. All SaaS audit logs are collected in a dataset called saas_audit_logs and specific relevant events are collected in the authentication_story preset for the xdr_data dataset. 

 Google Drive 

 google_workspace_drive_raw 

 Google 

 Workspace Drive 

 When relevant, Cortex XDR normalizes Google drive audit logs into authentication stories. All SaaS audit logs are collected in a dataset called saas_audit_logs and specific relevant events are collected in the authentication_story preset for the xdr_data dataset. 

 Token 

 google_workspace_token_raw 

 Google 

 Workspace Token 

 When relevant, Cortex XDR normalizes Token audit logs into authentication stories. All SaaS audit logs are collected in a dataset called saas_audit_logs and specific relevant events are collected in the authentication_story preset for the xdr_data dataset. 

 User accounts 

 google_workspace_user_accounts_raw 

 Google 

 Workspace User Accounts 

 — 

 SAML 

 google_workspace_saml_raw 

 Google 

 Workspace SAML 

 When relevant, Cortex XDR normalizes SAML audit logs into authentication stories. All SaaS audit logs are collected in a dataset called saas_audit_logs and specific relevant events are collected in the authentication_story preset for the xdr_data dataset. 

 Alerts 

 google_workspace_alerts_raw 

 Google 

 Workspace Alerts 

 — 

 Emails 

 google_gmail_raw 

 Google 

 Gmail 

 — 

 Prerequisite Steps 

 Be sure you do the following tasks before you begin configuring data collection from Google Workspace using the instructions detailed below. 

 When configuring data collection for all data types except emails, you need to complete the Google Workspace Reports API Prerequisites to set up the Google Workspace Admin SDK environment. This entails completing the instructions for Set up the basics and Set up a Google API Console project without activating the Reports API service as this will be explained in greater detail in the task below. For more information on these Google Workspace prerequisite steps, see Reports API Prerequisites . 

 When you only want to collect Google Workspace alerts without configuring any other data types, you need to set up a Cloud Platform project . 

 Before you can collect Google emails, you need to set up the following: 

 A compliance email account. 

 The organization’s Google Workspace account administrator can now set up a BCC to this compliance email account for all incoming and outgoing emails of any user in the organization. 

 Login to the Admin direct routing URL in Google Workspace for the user account that you want to configure. 

 Double-click Routing , and set the following parameters in the Add setting dialog. 

 Routing : Configure the compliance email account that you want to receive a BCC for emails from this user account using the format BCC TO <compliance email> . For example, BCC TO admin@organization.com . 

 Select Inbound and Outbound to ensure all incoming and outgoing emails are sent. 

 (Optional) To configure another email address to receive a BCC for emails from this account, select Add more recipients in the Also deliver to section, and then click Add . 

 Click Show options , and from the list displayed select Account types to affect → Users . 

 Save your changes. 

 This configuration ensures to forward every message sent to a user account to a defined compliance mailbox. After the Google Workspace data collector ingests the emails, they are deleted from the compliance mailbox to prevent email from building up over time (nothing touches the actual users’ mailboxes). 

 Note 

 Spam emails from the compliance email account, and from all other monitored email accounts, are not collected. 

 Any draft emails written in the compliance email account are collected by the Google Workspace data collector, and are then deleted even if the email was never sent. 

 Create a custom role with at least these permissions : 

 To follow the principle of least privilege, you must create a custom role in the Google Admin Console to ensure the user being impersonated has at least the following permissions: 

 In the Google Admin Console, select Account → Admin roles . 

 Click Create new role . 

 Assign at least the following permissions: 

 Reports : View Reports. 

 Services : Alerts (Full Access). 

 Assign this custom role to the user account you intend to use for impersonation. Record this user's email address. 

 To set up the Google Workspace integration: 

 Complete the applicable prerequisite steps for the types of data you want to collect from Google Workspace. 

 Log in to your GCP account . 

 Perform Google Workspace Domain-Wide Delegation of Authority when collecting any type of data from Google Workspace except Google Emails. 

 When collecting any type of data from Google Workspace except emails, you need to set up Google Workspace enterprise applications to access users’ data without any manual authorization. This is performed by following these steps. 

 Note 

 For more information on the entire process, see Perform Google Workspace Domain-Wide Delegation of Authority . 

 Enable the Admin SDK API to create a service account and set credentials for this service account. 

 As you complete this step, you need to gather information related to your service account, including the Client ID, Private key file, and Email address, which you will need to use later on in this task. 

 Select the menu icon → APIs & Services → Library . 

 Search for the Admin SDK API , and select the API from the results list. 

 Enable the Admin SDK API. 

 Select APIs & Services → Credentials . 

 Select + CREATE CREDENTIALS → Service account . 

 Set the following Service account details in the applicable fields. 

 Specify a service account name. This name is automatically used to populate the following field as the service account ID, where the name is changed to lowercase letters and all spaces are changed to hyphens. 

 Specify the service account ID, where you can either leave the default service account ID or add a new one. This service account ID is used to set the service account email using the following format: <id>@<project name>.iam.gserviceaccount.com . 

 (Optional) Specify a service account description. 

 CREATE AND CONTINUE . 

 (Optional) Decide whether you want to Grant this service account access to project or Grant users access to this service account . 

 Click Done . 

 Select your newly created Service Account from the list. 

 Create a service account private key and download the private key file as a JSON file. 

 In the Keys tab, select ADD KEY → Create new key , leave the default Key type set to JSON , and CREATE the private key. Once you’ve downloaded the new private key pair to your machine, ensure that you store it in a secure location, because it’s the only copy of this key. You will need to browse to this JSON file when configuring the Google Workplace data collector in Cortex XDR. 

 Note 

 You don't need to add permissions to the GCP Project-org service account. 

 When collecting alerts, enable the Alert Center API to create a service account and set credentials for this service account. 

 Note 

 When collecting Google Workspace alerts with other types of data, except emails, you need to configure a service account in Google with the applicable permissions to collect events from the Google Reports API and alerts from the Alert Center API. If you prefer to use different service accounts to collect events and alerts separately, you'll need to create two service accounts with different instances of the Google Workspace data collector. One instance to collect events with a certain service account, and another instance to collect alerts using another service account. The instructions below explain how to set up one Google Workspace instance to collect both event and alerts. 

 Select the menu icon → APIs & Services → Library . 

 Search for the Alert Center API , and select the API from the results list. 

 Enable the Alert Center API. 

 Select APIs & Services → Credentials . 

 Select the same service account in the Service Accounts section that you created for the Admin SDK API above. 

 Delegate domain-wide authority to your service account with the Admin Reports API and Alert Center API scopes. 

 Open the Google Admin Console . 

 Select Security → Access and data control → API controls . 

 Scroll down to the Domain wide delegation section, and select MANAGE DOMAIN WIDE DELEGATION . 

 Click Add new . 

 Set the following settings to define permissions for the Admin SDK API. 

 Client ID : Specify the service account’s Unique ID , which you can obtain from the Service accounts page by clicking the email of the service account to view further details. When creating a single Google Workspace data collector instance to collect both events and alert data, provide the same service account ID as the Admin SDK API. 

 In the OAuth scopes (comma-delimited) field, paste in the first of the two Admin Reports API scopes: https://www.googleapis.com/auth/admin.reports.audit.readonly 

 In the following OAuth scopes (comma-delimited) field, paste in the second Admin Reports API scope: https://www.googleapis.com/auth/admin.reports.usage.readonly 

 Note 

 For more information on the Admin Reports API scopes, see OAuth 2.0 Scopes for Google APIs . 

 When collecting alerts, add the following Alert Center API scope: https://www.googleapis.com/auth/apps.alerts 

 Authorize the domain-wide authority to your service account. 

 This ensures that your service account now has domain-wide access to the Google Admin SDK Reports API and Google Workspace Alert Center API, if configured, for all of the users of your domain. 

 Enable the Gmail API to collect Google emails. 

 When you are configuring the Google Workspace data collector to collect Google emails, the instruction differ depending on whether you are configuring the collection along with other types of data with the Admin SDK API already set up or you are configuring the collection to only include emails using only the Gmail API. The steps below explain both scenarios. 

 Select the menu icon → APIs & Services → Library . 

 Search for the Gmail API , and select the API from the results list. 

 Enable the Gmail API. 

 Select APIs & Services → Credentials . 

 The instructions for setting up credentials differ depending on whether you are setting up the Gmail API together with the Admin SDK API as you are collecting other data types, or you are configuring collection for emails only with the Gmail API. 

 When you’ve already set up the Admin SDK API, verify that the same Service Account that you configured for the Admin SDK API is listed, and continue on to the next step. 

 When you’re only collecting Google emails without the Admin SDK API, complete these steps. 

 Select + CREATE CREDENTIALS → Service account . 

 Set the following Service account details in the applicable fields. 

 -Specify a service account name. This name is automatically used to populate the following field as the service account ID, where the name is changed to lowercase letters and all spaces are changed to hyphens. 

 -Specify the service account ID, where you can either leave the default service account ID or add a new one. This service account ID is used to set the service account email using the following format: <id>@<project name>.iam.gserviceaccount.com . 

 -(Optional) Specify a service account description. 

 CREATE AND CONTINUE . 

 (Optional) Decide whether you want to Grant this service account access to project or Grant users access to this service account . 

 Click Done . 

 Select your newly created Service Account from the list. 

 Create a service account private key and download the private key file as a JSON file. 

 In the Keys tab, select ADD KEY → Create new key , leave the default Key type set to JSON , and CREATE the private key. Once you’ve downloaded the new private key pair to your machine, ensure that you store it in a secure location as it’s the only copy of this key. You will need to browse to this JSON file when configuring the Google Workplace data collector in Cortex XDR . 

 Delegate domain-wide authority to your service account with the Gmail API scopes. 

 Open the Google Admin Console . 

 Select Security → Access and data control → API controls . 

 Scroll down to the Domain wide delegation section, and select MANAGE DOMAIN WIDE DELEGATION . 

 This step explains how the following Gmail API scopes are added. 

 https://mail.google.com/ 

 https://www.googleapis.com/auth/gmail.addons.current.action.compose 

 https://www.googleapis.com/auth/gmail.addons.current.message.action 

 https://www.googleapis.com/auth/gmail.addons.current.message.metadata 

 https://www.googleapis.com/auth/gmail.addons.current.message.readonly 

 https://www.googleapis.com/auth/gmail.compose 

 https://www.googleapis.com/auth/gmail.insert 

 https://www.googleapis.com/auth/gmail.labels 

 https://www.googleapis.com/auth/gmail.metadata 

 https://www.googleapis.com/auth/gmail.modify 

 https://www.googleapis.com/auth/gmail.readonly 

 https://www.googleapis.com/auth/gmail.send 

 https://www.googleapis.com/auth/gmail.settings.basic 

 https://www.googleapis.com/auth/gmail.settings.sharing 

 Note 

 For more information on the Gmail API scopes, see OAuth 2.0 Scopes for Google APIs . 

 The instructions differ depending on whether you are setting up the Gmail API together with the Admin SDK API as you are collecting other data types, or you are configuring collection for emails only with the Gmail API. 

 When you’ve already set up the Admin SDK API, Edit the same Service Account that you configured for the Admin SDK API, and add the Gmail API scopes listed above. 

 When you’re only collecting Google emails without the Admin SDK API, click Add New , and set the following settings to define permissions for the Admin SDK API. 

 - Client ID —Specify the service account’s Unique ID , which you can obtain from the Service accounts page by clicking the email of the service account to view further details. 

 In the OAuth scopes (comma-delimited) field, paste in the first of the Gmail API scopes listed above, and continue adding in the rest of the scopes. 

 Authorize the domain-wide authority to your service account. 

 This ensures that your service account now has domain-wide access to the Google Gmail API for all of the users of your domain. 

 Prepare your service account to impersonate a user with access to the Admin SDK Reports API when collecting any type of data from Google Workspace except Google emails. 

 Only users with access to the Admin APIs can access the Admin SDK Reports API. Therefore, your service account needs to be set up to impersonate one of these users to access the Admin SDK Reports API. This means that when collecting any type of data from Google Workspace except Google emails, you need to designate a user whose Roles permissions are set to access reports, where Security → Reports is selected. This user’s email will be required when configuring the Google Workspace data collector in Cortex XDR. 

 In the Google Admin Console , select Directory → Users . 

 From the list of users listed, select the user configured with the necessary permissions in Admin roles and privileges to view reports that you want to set up your service account to impersonate. This is the user you created the custom role for in the Create a custom role with at least these permissions of the prerequisite steps above. 

 Record the email of this user as you will need it in Cortex XDR . 

 In Cortex XDR, select Settings → Configurations → Data Collection → Collection Integrations . 

 In the Google Workspace configuration, click Add Instance to begin a new configuration. 

 Integrate the applicable Google Workspace service with Cortex XDR. 

 Specify a descriptive Name for your log collection integration. 

 Browse to the JSON file containing your service account key Credentials for the Google Workspace Admin SDK API that you enabled. If you’re only collecting Google emails, ensure that you Browse to the JSON file containing your service account private key Credentials for the Gmail API that you enabled. 

 Select the types of data that you want to Collect from Google Workspace. 

 Google Chrome : Chrome browser and Chrome OS events included in the Chrome activity reports. 

 Admin Console : Account information about different types of administrator activity events included in the Admin console application's activity reports. 

 Google Chat : Chat activity events included in the Chat activity reports. 

 Enterprise Groups : Enterprise group activity events included in the Enterprise Groups activity reports. 

 Login : Account information about different types of login activity events included in the Login application's activity reports. 

 Rules : Rules activity events included in the Rules activity report. 

 Google drive : Google Drive activity events included in the Google Drive application's activity reports. 

 Token : Token activity events included in the Token application's activity reports. 

 User Accounts : Account information about different types of User Accounts activity events included in the User Accounts application's activity reports. 

 SAML : SAML activity events included in the SAML activity report. 

 Alerts : Alerts from the Alert Center API beta version , which is still subject to change. 

 Emails : Collects email data (not emails reports). All message details except email headers and email content ( payload.body , payload.parts , and snippet ). 

 Note 

 For more information about the events collected from the various Google Reports, see Google Workspace Reports API Documentation . 

 For all options selected, except Emails , you must specify the Service Account Email . This is the email account of the user with access to the Admin SDK Reports API that you prepared your service account to impersonate . 

 When selecting Emails , configure the following. 

 Audit Email Account : Specify the email address for the compliance mailbox that you set up. 

 Test the connection settings. 

 To test the connection, you must select one or more log types. Cortex XDR then tests the connection settings for the selected log types. 

 If successful, Enable Google Workspace log collection. 

 Previous Ingest Logs and Data from a GCP Pub/Sub 

 Next Ingest Logs from Microsoft Azure Event Hub 

 Last updated 10 days ago 

 Was this helpful?
