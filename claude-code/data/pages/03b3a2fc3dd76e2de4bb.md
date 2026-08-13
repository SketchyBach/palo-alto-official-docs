---
url: https://docs.paloaltonetworks.com/saas-security/sspm/onboard-saas-apps-supported-by-sspm/onboard-a-servicenow-app-to-sspm
fetched_at: 2026-08-13T17:34:20Z
source: palo-alto-main
---

# Onboard a ServiceNow App to SSPM Clear

Onboard a ServiceNow App to SSPM 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Onboard a ServiceNow App to SSPM 

 Updated on 

 Fri Jul 10 09:31:52 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Updated on 

 Fri Jul 10 09:31:52 PDT 2026 

 Focus 

 Home 

 SaaS Security 

 Onboard SaaS Apps Supported by SSPM 

 Onboard a ServiceNow App to SSPM 

 Download PDF 

 SaaS Security 

 Onboard a ServiceNow App to SSPM 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Previous 

 Onboard a Sentry App to SSPM 

 Next 

 Onboard a Shopify App to SSPM 

 Onboard a ServiceNow App to SSPM 

 Connect a ServiceNow instance to SSPM to detect posture risks. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 SaaS Security Posture Management license 

 Or any of the following licenses that include the Data Security license: 

 CASB-X 

 CASB-PA 

 For SSPM to detect posture risks in your ServiceNow instance, you must onboard your
 ServiceNow instance to SSPM. Through the onboarding process, SSPM connects to a
 ServiceNow API by using OAuth 2.0 authorization. To enable OAuth 2.0 authorization,
 you first register an OAuth 2.0 integration application in ServiceNow before
 onboarding your ServiceNow instance in SSPM. During the onboarding process, you're
 prompted to log in to ServiceNow and to grant SSPM the access it requires. After
 connecting to the ServiceNow API, SSPM scans your ServiceNow instance for
 misconfigured settings, third-party plugins, and account risks. 

 You can also use the OAuth 2.0 application to enable SSPM to create tickets in
 ServiceNow. To enable ServiceNow ticketing, you link SSPM to a ServiceNow instance
 from the Ticketing Settings page. To enable ticketing, SSPM requires the same
 information that it requires for onboarding ServiceNow. However, onboarding
 ServiceNow for scans and linking to ServiceNow for ticketing are two separate
 procedures. When you're creating your OAuth 2.0 application in ServiceNow, be aware
 that SSPM uses different redirect URLs depending on whether you're onboarding
 ServiceNow for scans or linking to ServiceNow for ticketing. Your OAuth 2.0
 integration application can specify both of these redirect URLs. 

 To onboard your ServiceNow instance, SSPM requires the following information, which
 you will specify during the onboarding process. 

 Item Description 

 Client ID SSPM will access a ServiceNow API through an OAuth 2.0
 application that you create. ServiceNow generates the Client ID to
 uniquely identify the application. 

 Client Secret SSPM will access the ServiceNow API through an OAuth 2.0
 application that you create. ServiceNow generates the Client Secret,
 which SSPM uses to authenticate to the application. 

 Instance URL The unique URL for your ServiceNow instance. 

 To onboard your ServiceNow instance, you complete the following actions: 

 From SSPM, get the redirect URLs that you will need when you register your
 OAuth 2.0 application in ServiceNow. 

 For onboarding, you must specify the redirect URL for onboarding for scans.
 If you also want to enable ServiceNow ticketing from SSPM, you must also
 specify the redirect URL for ticketing. To get the redirect URL, you will
 begin the onboarding procedure in SSPM, but you will not complete the
 procedure. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Posture Security Applications Add Application and click the ServiceNow tile. 

 On the Posture Security tab, Add
 New instance. 

 OAuth 2.0 . 

 SSPM displays a configuration page for onboarding a ServiceNow
 instance. The Redirect URL field displays the redirect URL
 value. 

 Copy the redirect URL and paste it into a text file. 

 Don’t continue to the next step unless you
 have copied the redirect URL. You will need to specify this URL
 later when you're configuring your OAuth 2.0 integration
 application. 

 If you also want to link SSPM to the ServiceNow instance for ticketing, get
 the redirect URL for ticketing. To get this redirect URL, you will begin the
 procedure for linking SSPM to ServiceNow for ticketing, but you will not
 complete the procedure. 

 Select Configuration SaaS Security Settings Workflow Ticketing Settings . 

 Add Link for ServiceNow. 

 The login page for linking to a ServiceNow instance is displayed. The
 Redirect URL field displays the redirect URL value. Copy the
 redirect URL and paste it into a text file. 

 Don’t continue to the next step unless you
 have copied the redirect URL. You will need to specify this URL
 later when you're configuring your OAuth 2.0 integration
 application. 

 Create an authentication scope to limit access to ServiceNow REST APIs. 

 During onboarding, you will log in to a ServiceNow account and will grant
 SSPM access to that account. SSPM will get access to your ServiceNow account
 through an OAuth 2.0 integration application that you will create. By
 default, the OAuth token will have full access to the REST APIs that the
 ServiceNow account can access. Although SSPM will access only the Table API,
 the OAuth token will allow more access than SSPM requires. Before you create
 the OAuth 2.0 integration application, create an authentication scope, which
 will limit SSPM's access to only the Table API. You can create a scope that
 allows SSPM read-access only or full read and write access to the Table API.
 Later, you will assign this scope to your OAuth 2.0 application. 

 Log in to ServiceNow as an administrator. 

 Make sure the REST API Auth Scope plugin (com.glide.rest.auth.scope) is
 activated in ServiceNow. To verify that the plugin is activated,
 navigate to System Definition Plugins and use the search field to locate the plugin. If the
 plugin isn’t installed, refer to the ServiceNow documentation to install and activate the REST API
 Auth Scope plugin . 

 Create the authentication scope. 

 Navigate to the Authentication Scopes table
 (sys_auth_scope.list) by using the filter navigator. 

 Click New to define the authentication
 scope. 

 Specify a meaningful Name for your
 authentication scope, such as SSPM Connector . You can
 optionally specify a longer
 Description . 

 Make note of the authentication scope
 name. You will need to specify this name later when you're
 configuring a REST API Auth Scope and your OAuth 2.0
 integration application. 

 Submit . 

 Create a REST API Auth Scope and link it to your authentication
 scope. 

 The REST API Auth Scope is where you will limit SSPM access to the
 Table API only. You can allow SSPM full read and write access to
 perform all HTTP methods, or you can limit SSPM to read-only access
 (GET method only). 

 Navigate to the REST API Auth Scopes list ( System Web Services API Auth Scopes REST API Auth Scope ). 

 Click New to define the REST API Auth
 Scope. 

 In the Name field, specify a name for
 your REST API Auth Scope. 

 From the REST API list, select
 Table API . 

 Configure the REST API Auth Scope to allow SSPM full read and
 write access (all HTTP methods) to the Table API, or read-only
 access (HTTP GET method only). 
 Read-only Access : Configuring the REST API Auth
 Scope for reduced, read-only access will enable SSPM to
 perform configuration scans, account scans, and
 third-party plugin scans. However, SSPM will not be able
 to perform automated remediation of misconfigured
 settings. 
 To configure the REST API Auth Scope for
 read-only access, complete the following steps: 
 Deselect the Apply auth scope to
 all http methods in this API check
 box. 

 From the HTTP Method 
 list, select GET . 

 Read and Write Access : Configuring the REST API
 Auth Scope for full read and write access will enable
 SSPM to perform configuration scans, account scans, and
 third-party plugin scans. It will also enable SSPM to
 perform automated remediation of misconfigured
 settings. 
 To configure the REST API Auth Scope for
 Read and Write access, select the Apply
 auth scope to all http methods in this
 API check box. 

 In the Auth Scope field, specify the name
 of the authentication scope that you created earlier. This
 specification links the REST API Auth Scope to the
 authentication scope. 

 Submit . 

 Create your OAuth 2.0 application in ServiceNow. 

 Log in to ServiceNow as an administrator. 

 Navigate to the Application Registries page ( System OAuth Application Registry ). 

 From the Application Registries page, create a
 New application. 

 ServiceNow prompts you to select the type of OAuth application that you
 want to create. Specify that you want to Create an OAuth API
 endpoint for external clients . 

 ServiceNow displays a dialog for configuring your OAuth 2.0
 application. 

 Fill in your OAuth 2.0 application details using the fields that
 ServiceNow provides. 

 Specify the Redirect URL for onboarding
 ServiceNow, and, optionally, the redirect URL for linking to
 ServiceNow for ticketing. If you're adding both redirect URLs,
 separate the two URLs with a comma. 

 Under Auth Scopes , add the authentication
 scope that you created earlier. 

 If the form includes an Enforce Token
 Restrictions checkbox, make sure it is not
 selected. Depending on your ServiceNow version and installed
 security plugins, the form might not include this checkbox. 

 Submit . 

 ServiceNow registers your new OAuth 2.0 application and displays the
 Application Registries page. The Application Registries page now
 lists your OAuth 2.0 application. 

 Open your OAuth 2.0 application and copy the Client ID and Client
 Secret into a text file. 

 Don’t continue to the next step unless you
 have copied the Client ID and Client Secret. You must provide this
 information to SSPM during the onboarding process. 

 Ensure that SSPM can access ServiceNow tables. 

 For SSPM to complete its scans, SSPM must be able to access the following
 tables in ServiceNow. 

 sys_plugins 

 sys_properties 

 sys_scope 

 sys_user 

 sys_user_has_role 

 sys_user_role 

 oauth_entity 

 oauth_credential 

 v_plugin 

 sys_db_object 

 pwd_reset_request 

 To ensure that SSPM can access these tables, open the table definition record
 for each table and verify that external systems can access the table through
 the ServiceNow REST Table API. 

 Navigate to the Tables page ( System Definition Tables ). 

 For each of the tables that SSPM must be able to access, complete the
 following steps: 

 Locate the table record in the list of tables and click its name
 to open the table record. To quickly locate a table record, you
 can use the Search field to filter the
 list. 

 In the table record, select the Application
 Access tab. 

 In the table record, verify that the Allow access to
 this table via web services checkbox is
 selected. If necessary, select the Allow access to
 this table via web services checkbox and click
 Update to save your changes. 

 Connect SSPM to your ServiceNow instance. 

 In SSPM, complete the following steps to enable SSPM to connect to your
 ServiceNow instance. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Posture Security Applications Add Application and click the ServiceNow tile. 

 On the Posture Security tab, Add
 New instance. 

 OAuth 2.0 . 

 On the configuration page, enter your Instance URL and the application
 credentials (Client ID and Client Secret). 

 Specify whether you're granting SSPM Read
 Permissions only or Read and Write
 Permissions . 

 The option you choose depends on how you configured the
 authentication scope to limit access. If you configured the
 authentication scope to allow only the GET method, select
 Read Permissions . If you configured the
 authentication scope to allow access to all HTTP methods, select
 Read and Write Permissions . 

 The onboarding page lists the API scopes that SSPM will access to
 complete scans and to perform automated remediation. 

 Connect . 
 SSPM redirects you to the ServiceNow login page. 

 Log in using a ServiceNow administrator account. 

 The account you use must be assigned to the
 admin role in ServiceNow. Make sure the account is not
 also assigned to the snc_read_only role, which will restrict
 the account to read-only access. If the account is restricted to
 read-only access, onboarding will fail. 
 After onboarding is
 complete, you can restrict the account to read-only access. Full
 read and write access is required only to during onboarding and
 reauthentication to grant access to the requested
 scopes. 

 ServiceNow displays a consent form. 

 Review the consent form and Allow access to the
 account. 

 If you also want to create ServiceNow tickets from SSPM, link SSPM to
 the ServiceNow instance. You link SSPM to ServiceNow from the Ticketing
 Settings page ( Configuration SaaS Security Settings Workflow Ticketing Settings ). 

 Previous 

 Onboard a Sentry App to SSPM 

 Next 

 Onboard a Shopify App to SSPM 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Prisma Access Monitoring and Visibility 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Enterprise DLP 

 SaaS Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SaaS Security Posture Management 

 SaaS Security 

 SSPM 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
