---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-browser-customization/configure-customization
fetched_at: 2026-08-13T17:23:17Z
source: palo-alto-main
---

# Configure Customization Clear

Configure Customization 

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

 Configure Customization 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 Manage Prisma Browser Policy Profiles 

 Configure Prisma Browser Customization Controls 

 Configure Customization 

 Download PDF 

 Prisma Browser 

 Configure Customization 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Configure Autonomous Digital Experience Management (ADEM) 

 Next 

 Configure Routing 

 Configure Customization 

 PAB Customization controls and policies 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Prisma Browser standalone 

 Prisma Access with Prisma Browser bundle
 license or Prisma Browser standalone license 

 Superuser or Prisma Browser 
 role 

 Incognito 

 Mobile Browser - Full support 

 This feature allows you to control whether or not the Prisma Browser can be
 opened in Incognito mode. A user in Incognito mode is anonymized from the Web
 only. Admin visibility and Browser Policies are not affected by this feature.
 You can set Access & Data Control rules to allow access to personal websites
 without logging. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Incognito . 

 Select one of the following options: 

 Allow - Permit use of Incognito mode in Prisma Browser . 

 Block - Block use of Incognito mode in The Prisma Browser . 

 Force - Force use of Incognito mode in the Prisma Browser . 

 Click Set . 

 Extension Force Install 

 Mobile Browser - No support 

 This feature allows you to configure specific extensions that are to be installed
 automatically in the Prisma Browser . 

 If there
 are multiple rules that have the Extension Force Install control applied,
 all the applicable extensions will be installed. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Extension Force Install . 

 Click Add Extension . 

 Select the Store that is the source of the extension. The options are: 

 Chrome Web Store . 

 Custom URL . Enter the URL. 

 Select whether the extension will be pinned to the toolbar for the
 end users. 

 Select whether the extension will be automatically installed in
 Incognito mode . 

 If applicable, enter the Custom Configuration . 

 The system supports JSON format. Custom
 configuration depends on your extension vendor; contact your vendor or
 support partner for assistance. 

 Click Add . 

 User-Agent 

 Mobile Browser - Full support 

 The User-Agent feature allows you to add additional Agent components to the
 default User-Agent string to identify the Prisma Browser HTTP/S requests.

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select User-Agent . 

 Select one of the following options: 

 Use default User-Agent - Use the default
 User-Agent string when identifying requests from the Prisma Browser . This is the same as the Chrome User-Agent 

 Set an additional User-Agent component - Configure an
 additional User-Agent for the Prisma Browser by entering the
 component name in the appropriate field. 

 User-Agent desktop mode - Allows you to ensure that
 applications that do not function properly in mobile browsers
 open in desktop mode. 

 Click Set . 

 Custom HTTP Header 

 Mobile Browser - No support 

 Custom HTTP headers let the browser pass additional information along with HTTP/S
 requests. An HTTP header consists of its case-insensitive name followed by a
 colon (:), then by its value. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Custom HTTP Header . 

 Select one of the following options: 

 Keep default header - Use the default setting,
 without any custom HTTP headers. 

 Add a custom header - Configure a custom HTTP header that
 will identify the Prisma Browser HTTP/S requests. 

 Custom Header Name - Add a name to identify the
 custom header. 

 Custom Header Value - Add a custom value for the
 header. 

 Click Set . 

 Profile Sync 

 Mobile Browser - Full support 

 Linux/IGEL Browser - No support 

 In some organizations, employees use the Prisma Browser on multiple
 devices. This feature enables you to synchronize profiles across all Prisma Browser installations on different devices. 

 You have the option of customizing the browser settings to sync
 everything - all information that is associated with the user - or selecting
 specific information that will be included in the sync. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Profile Sync . 

 Select one of the following options: 

 Enable - Allow a Profile Sync. You can select the
 following sync options: 

 Sync everything - Select all the
 information that can be synchronized. 

 Customize sync - Select the components
 that will be synchronized across multiple devices. 

 Disable - Don't perform profile sync. 

 Click Set . 

 Default Browser 

 Mobile Browser - Full support 

 Linux/IGEL Browser - No support 

 This feature allows you to control whether Prisma Browser will be the default
 browser. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Default Browser . 

 Select one of the following options: 

 Suggest user - Suggest that users select the Prisma Browser . 

 Don't suggest user - don't suggest using the Prisma Browser . 

 Click Set . 

 Onboarding Wizard 

 Mobile Browser - No support 

 This feature allows you to configure the Onboarding Wizard that is displayed to
 all new Prisma Browser users when they install the browser. The wizard
 assists end users in installing and configuring the Prisma Access Browser, and
 at the same time - displays a brief tutorial of some of the more popular
 features. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Onboarding Wizard . 

 Select one of the following options: 

 Enabled - the Onboarding Wizard will be enabled
 for use. You will be able to select the steps that will be made
 available to the users. 

 By default, all steps are enabled. 

 Step 1: Welcome and language selection
 (Editable) allows you to select either the
 default welcome message or create a custom message for
 your users. The custom content allows 160 characters for
 a title and 320 characters as the message. 

 In Step 2: Customize , users can add
 their picture. If you did not configure the Brand
 Color , users will be able to configure their
 own preferred color. If the Brand Color was configured,
 the color option won't be displayed. 

 Step 3: Import allows users to import
 their existing resources including: 

 Browsing History 

 Favorites / Bookmarks 

 Saved Passwords 

 Cookies 

 Extensions 

 Extension Data 

 Tabs and Tab Groups 

 Step 4: Labels & Policy indicator 
 provides a brief description on how users can benefit
 from the displayed labels. 

 Step 5: Popup extensions &
 Notifications encourages users to use the Prisma Browser icon to help manage their account.

 Step 6: Restrictions describes to users
 the way that Prisma Browser uses the restrictions in
 the browser. 

 Step 7: Mobile & Sync informs users
 that the mobile application is a seamless extension of
 the desktop browser. 

 Step 8: Feedback invites users to send
 their comments and suggestions. 

 Disabled - the Onboarding Wizard won't be enabled. 

 Click Set . 

 Search Engine Content Filtering 

 Mobile Browser - Full support 

 When you enable the Safe Search feature, you extend the URL filtering to include
 the selected search engines. . 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Search Engine Content Filtering . 

 Select one of the following options: 

 Enable -Enable the feature. You also need to select
 at least one of the available search engines to be used for safe
 search. 

 Disable - Disable the feature. 

 Click Set . 

 Microsoft Auto-SSO (Windows only) 

 Mobile Browser - No support 

 This feature enables automatic web-application user sign-in for Microsoft Entra
 ID accounts, based on the device signed-in account. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Microsoft Auto-SSO . 

 Select one of the following options: 

 Enable - Enable the automatic user sign-in for Microsoft
 Entra accounts. 

 Disable - Disable the Microsoft auto-sso feature. 

 It is strongly recommended that this feature be
 limited to managed devices only. 

 Click Set . 

 Automatic Client Certificate Selection 

 Mobile Browser - No support 

 This control allows you to configure matching client certificates for specified
 URLs to facilitate seamless authentication. When you configure this control, it
 acts as an override to any lower priority rule definitions. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Automatic Client Certificate Selection . 

 Select one of the following options: 

 Enable: Allows you to bypass manual certificate selection.
 Specified URLs will operate seamlessly. Enter the following
 information in the Certificate criteria for specific URLs section

 Enter A URL pattern that will use the certificate. Click
 here for more information about the URL pattern
 syntax . 

 From the drop-down list, select a criteria for the
 certificate. 

 Enter the name of the certificate's issuer
 organization . 
 You can add multiple criteria and issuer
 organization for each URL. 

 Additionally, you can add as many URLs as needed.

 Disable: Users will be required to manually choose the
 certificate they need when browsing the URL 

 Click Set . 

 If you enable Google Workspace
 Integration, Automatic Client Certificate Selection for Google URLs may
 not function properly. 

 History Collection 

 This Policy only supports Prisma Browser 
 Extension. 

 This feature allows you to create a History Collection that allows you to
 identify browsing trends and behavior patterns of your users. 

 You need to be aware of the following limitations
 regarding this feature: 
 The information is collected from Prisma Access Browser Extension
 users only . 

 The historical information will be collected beginning up to 30 days
 before the installation. 

 The Scope of a rule containing History Collection is 50 
 users. 

 For more information, refer to Prisma Browser Extension History Collection 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select History Collection . 

 If you do not see the History Collection, make
 sure that the Browser Extension controls are visible. 

 Select one of the following options: 

 Enable - Enable the History Collection. 

 Disable - Disable the History Collection. 

 Click Set. 

 On Browser Startup 

 Mobile Browser - No support 

 This feature allows you to control the Prisma Browser 's "On-Startup"
 routine. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select On Browser Startup . 

 Select one of the following options: 

 Configured by the user - Users will be able to determine
 exactly how the browser will open. 

 Restore the Last Session (Continue where the user left
 off - Restore the last set of browser tabs, allowing the
 users to continue working. 

 Restore the last session and open a list of URLs - Allows
 the user to reopen the last set of browser tabs. This option
 will also open an additional list of (predefined) apps. When you
 select this field, you will be able to add additional web pages
 to open. 

 Open a New Tab Page - Opens a generic new tab page. 

 Web pages to open on startup - Enter a list of web pages
 that will open on startup. 

 Click Set . 

 Default Search Provider 

 Mobile Browser - Full support 

 This feature allows you to set up the way the browser search engine works.
 This feature allows you to either configure a search engine, allow your
 users to select their preferred browser, or disable searching entirely on
 the Prisma Browser . 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Default Search Provider . 

 Select one of the following options: 

 Enable - You can select the search provider that will
 serve as the default for all users. To configure default search
 engine, provide the following information: 
 Search Provider - Select a search provider from
 the list. You can also select a customized provider. If
 you use a custom provider, enter a Search Provider
 Name , and the url for the engine. 

 Disable - Do not allow searching. 

 User Choice - Allow users t select their own search
 provider . 

 Click Set . 

 Auto-Launch External Applications 

 Support for Prisma Browser Extension only. 

 The Prisma Browser Extension
 provides an auto-login feature that offers users a seamless and automatic
 sign-in experience, eliminating the need for manual authentication. The feature
 is available only when you integrate it with the following Identity Providers
 (IdP): 
 Okta 

 Azure Active Directory 

 Google Workspace 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Auto-Launch External Applications . 

 Select one of the following options: 

 Allow - Permit the use of Auto-Launch External
 Applications. 
 Protocol - Enter the protocol in the proper
 format. The format is displayed on the control. 

 Add Origin - Enter the Origin patterns for the
 protocol. The format is displayed on the top of the
 page. 

 Block - Do not allow Auto-Launching External
 Applications. 

 Click Set . 

 Desktop Sharing 

 Mobile Browser - No
 support 

 When this feature is enabled, users will be granted
 the ability to share their screens when they are using the sharing tools from
 within a browser. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Desktop Sharing . 

 Select one of the following options: 

 Allow - Allows you to enable end-users to share their
 desktop screens or desktop applications. 

 Block - Block end-users from sharing their desktop
 screens or desktop applications. 

 Click Set . 

 Built-in DNS Client 

 Mobile Browser - No
 support 

 Choose whether DNS is resolved in the Prisma Browser built-in client, or by the operating system. 
 For more information, refer
 to BuiltInDnsClientEnabled on the Chrome
 Enterprise site. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Built-in DNS Client . 

 Select one of the following options: 

 Always use the built-in DNS client. 

 Never use the built-in DNS client. 

 Click Set . 

 Page Translation (Google Translate) 

 Mobile Browser - No
 support 

 This control allows you to manage the Google
 Translation banner on foreign-language pages. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Page Translation (Google
 Translate) . 

 Select one of the following options: 

 Always offer translation. 

 Never offer translation. 

 Allow the user to decide. 

 Click Set . 

 Search Suggestions 

 Mobile Browser - No support 

 Implement a dynamic real-time prediction feature within the address bar,
 displaying relevant search suggestions and direct navigation links as the
 user inputs their query. This functionality is designed to significantly
 enhance the user experience by reducing the number of keystrokes required,
 accelerating search and navigation, and proactively guiding the user to the
 most pertinent results or destinations as quickly and efficiently as
 possible. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Browser Customization 

 Select Search Suggestions . 

 Select one of the following options: 

 Enabled - The browser will always offer search
 suggestions. 

 Disabled - The browser will not offer search suggestions. 

 Allow the user to decide - Users will decide whether or
 not to enable this feature. This is the default. 

 Click Set . 

 Previous 

 Configure Autonomous Digital Experience Management (ADEM) 

 Next 

 Configure Routing 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Prisma Browser 

 Administration 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
