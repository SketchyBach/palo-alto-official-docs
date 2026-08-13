---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/manage-prisma-access-browser-policy-profiles/configure-prisma-access-browser-data-controls/configure-data-leak-prevention
fetched_at: 2026-08-13T17:23:21Z
source: palo-alto-main
---

# Configure Data Leak Prevention Clear

Configure Data Leak Prevention 

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

 Configure Data Leak Prevention 

 Updated on 

 Jul 28, 2026 

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

 Jul 28, 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 Manage Prisma Browser Policy Profiles 

 Configure Prisma Browser Data Controls 

 Configure Data Leak Prevention 

 Download PDF 

 Prisma Browser 

 Configure Data Leak Prevention 

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

 Configure Prisma Browser Data Controls 

 Next 

 Configure Threat Protection 

 Configure Data Leak Prevention 

 The Data Leak Prevention Controls 

 File Download 

 Mobile Browser -
 Partial support 

 For detailed information in File Downloads using
 the Prisma Browser for Mobile, refer to the Prisma Access Mobile Browser
 information 

 File Download control provides multiple
 capabilities related to downloading files from websites that match a specified URL,
 application, or website classification. To set the File Download control: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select File Download . 

 Select one of the following options: 

 Allow - the Prisma Browser 
 will allow all downloads. 

 Allow (Protected ) – the Prisma Browser 
 will allow downloads that can open only in the browser. 

 Allow to open outside of the
 browser - users will be able to
 unprotect the file, allowing viewing and editing of the
 file using external applications. This includes any
 browser and any Desktop application. 

 To unprotect a file: 

 Click the Download History folder link
 in the Browser bar. 

 Select the file to open. It will be
 indicated by a folder with a slash. 

 Click on the icon to unprotect the file. 

 Save to organizational storage - Users won't be able to
 download the files directly. Files will be uploaded to the cloud
 storage that you selected. 
 Select provider - Select the cloud provider from the
 list. For more information on configuring cloud storage
 items refer to Configuration→ Prisma Browser 
 →Integrations→Services→Cloud storage 

 Be sure to configure the
 organizational storage before it becomes available to
 the users. If you did not configure organizational
 storage, the option is not available. 

 Block - the Prisma Browser will block all
 downloads. 

 Apply on:- select between one of the following options: 

 Any file - the
 download restrictions will apply to all files.

 Specific files -
 the download restrictions will apply to files that
 meet the selected specifications (the rule can
 contain as many of these specifications as
 needed): 

 File size - set
 the size of the file. 

 File types - set
 the file
 types that need to match this rule. 

 File hash - set
 the SHA-256 hash to be matched for this rule. 

 MIP label - set the level of
 the MIP label 
 that can be used to protect contents with sensitive
 content. 

 Prompt - when there is a restriction, select
 between one of the following options: 

 None - there will be no
 prompts. 

 Before download - inform
 the user that there is a restriction and how to bypass
 it. 

 Warn and allow to proceed
 anyway - informs users about the risk
 or sensitivity of downloading files but allowing
 them to continue. 

 Warn and allow to proceed
 anyway with a reason - informs users
 about the risk or sensitivity of downloading files
 and require them to select a reason to continue.

 Permission request - allows
 users to send a permission request to the admin. The
 user will be informed once the request is approved
 or denied. 

 Require MFA - Require users to complete an
 additional authentication (PIN code, passkey, or IdP authentication)
 before downloading files. Configure the authentication factor used
 under Browser Security >
 Browser Hardening > Authentication Factor 

 When you use this control, you can use your own dialog text to replace the
 default. To set the text, click Set dialog text .

 Set . 

 When downloading PDF files - On
 Android devices, the PDF may briefly appear in the browser viewer before
 the system blocks the download. On iOS, the download is blocked
 immediately, and the viewer does not open. 

 File Upload 

 Mobile Browser - Partial support 

 For detailed information in File Upload using the Prisma
 Browser for Mobile, refer to the Prisma Access Mobile Browser
 information 

 The File Upload policy controls whether users can upload files that come from
 websites that match the URL or from a selected application or category. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select File Upload . 

 Select one of the following options: 

 Allow - the Prisma Browser 
 will allow all uploads. 

 Allow protected files only between the
 rule’s web applications - Protected files
 sourced from the Web application of this
 rule. Only previously downloaded protected files from the Web
 application of this rule can be uploaded. 

 Requires setting the File Download control
 to “Allow (Protected)” . 

 Allow only nonprotected files –
 only nonprotected files from any source can be uploaded. 

 Block - the Prisma Browser will block
 all uploads. You can block uploads from specific file
 extensions. Other extensions will be blocked. 

 Apply on: - select between one of the
 following options: 

 Any file - the download
 restrictions will apply to all files. 

 Specific files - the
 upload restrictions will apply to files that meet the
 selected specifications (the rule can contain as many of
 these specifications as needed): 

 File size - set
 the size of the file. 

 File types - set
 the file
 types that need to match this rule. 

 File hash - set
 the SHA-256 hash to be matched for this rule. 

 MIP label - set the level of
 the MIP label 
 that can be used to protect contents with sensitive
 content. Install the Microsoft Information
 Protection integration to use this feature. 

 Prompt - when there is a restriction, select
 between one of the following options: 

 None - there will be no
 prompts. 

 Before upload - inform
 the user that there is a restriction and how to bypass
 it. 

 Warn and allow to proceed
 anyway - informs users about the risk
 or sensitivity of uploading or downloading files,
 but allowing them to continue. 

 Warn and allow to proceed
 anyway with a reason - informs users
 about the risk or sensitivity of uploading files,
 and require them to select a reason to continue.

 Permission request - allows
 users to send a permission request to the admin. The
 user will be informed once the request is approved
 or denied. 

 Require MFA - Require users to complete an
 additional authentication (PIN code, passkey, or IdP authentication)
 before uploading files. Configure the authentication factor used
 under Browser Security >
 Browser Hardening > Authentication Factor . 

 When you use this control, you can use your own dialog text to replace the
 default. To set the text, click Set dialog text .

 Click Set . 

 Clipboard 

 Mobile Browser - Partial support 

 The Clipboard Policy manages copy and paste functions when using the Prisma Browser . This tool allows you to manage Copy & Paste functions.
 To configure the Clipboard control: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Clipboard . 

 Select the control that you need to configure (both controls can be
 configured): 

 Copy & Paste data out -
 Configure whether users are allowed to copy & paste
 information from the browser to other applications. 

 Allow (anywhere) - Allow
 the copied data to be pasted to any web application or
 external process. 

 Block (permit only within the rule's
 web applications) - Block copy and paste
 data out of the rule's web application. 

 Exclude URL address
 bar – The URL address bar won't be
 considered as part of the webpage. 

 Prompt - Select whether you want to
 display a prompt. 

 None - Don't
 require a prompt. 

 Before pasting dat1a out to
 other web applications (Inform the user
 of the restriction and allow bypassing it). 

 Pop-up
 Notifications 

 Warn and allow to proceed anyway. 

 Warn and allow to proceed anyway with
 a reason. 

 Permission request - select a Bypass
 time frame as well. 

 Copy & Paste data in -
 configure whether or not users are allowed to copy & paste
 information from other web applications or external processes. 

 Allow - allow the copied
 data to be pasted from any web application or external
 process. 

 Block - don't allow the
 copied data to be pasted from any web application or
 external process. 

 Prompt - select whether
 you want to display a prompt before pasting data in. 

 None - don't
 require a prompt. 

 Before pasting data in
 (Inform the user of the restriction
 and allow bypassing it) 

 Pop-up notification - 

 Warn and allow to proceed anyway. 

 Warn and allow to proceed anyway with
 a reason. 

 Permission request - select a Bypass
 time frame as well. 

 When you use this control, you can use your own dialog text to replace the
 default. To set the text, click Set dialog text .

 Click Set . 

 Webpage Data Masking 

 Mobile Browser - No support 

 This control allows you to mask textual content within webpages. The
 masking is set according to either predefined information types (PII or PCI) or
 a custom regex. 

 When this is enabled, the browser will inspect and mask any webpage or
 frame within the webpage. This will be done only in situations where the URL in
 the browser tab or the URL in the frame is matched. To enable Webpage Data
 Masking: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Webpage Data Masking . 

 Select one of the following options: 

 Enable - the Prisma Browser 
 will mask URLs in tabs or frames that match the conditions.
 Select the masking pattern: 

 Mask all characters. 

 Leave the last characters unmasked. 

 Leave the first characters unmasked. 

 You can choose to unmask up to 4
 characters. 

 Disable - the Prisma Browser won't
 mask URLs in tabs or frames that match the conditions. 

 Prompt - Optionally select one of the following
 prompt options: 

 None - Do not use pop-up notifications. 

 Pop-up notifications 
 Warn and allow to proceed anyway -
 the prompt will freeze the sensitive information until the
 user acknowledges the message. 

 Warn and allow to proceed anyway with a
 reason - the prompt will freeze the
 sensitive information until the user acknowledges the
 message and selects a reason. 

 Permission request - the prompt will
 freeze and mask the sensitive information until permission
 is granted. 

 Click Set . 

 Typing Guard 

 Mobile Browser - No support 

 Linux/IGEL Browser - No support 

 Scans manual input made by users in real-time within the browser. It operates
 based on defined rules that can be customized based on specific organizational
 requirements. To set the Typing Guard control: 

 Typing guard is only compatible with basic HTML form
 fields. It may not function on websites that use complex or JavaScript-based
 input methods. For complete copy-paste protection, please use the clipboard
 control. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Typing Guard . 

 Select one of the following options: 

 Enable - the Prisma Browser 
 will enable the Typing Guard, blocking the users from entering
 potentially sensitive data to the policy rule's application. 

 Disable - the Prisma Browser 
 will disable the Typing Guard, and won't block potentially
 sensitive data. 

 Prompt - Optionally select one of the following
 pop-up options: 

 Warn and allow to proceed anyway 
 - the prompt will freeze the sensitive information until the
 user acknowledges the message. 

 Warn and allow to proceed anyway with a
 reason - the prompt will freeze the sensitive
 information until the user acknowledges the message and selects
 a reason. 

 Permission request - the prompt will freeze
 and mask the sensitive information until permission is granted.

 When you use this control, you can use your own dialog text to replace the
 default. To set the text, click Set dialog text .

 Click Set . 

 The new control enables you to control users typing activities within the context
 of an Access & Data Control rule. This is designed to
 restrict the specific content definitions of the rule. 

 In an Access & Data Control rule, go to the
 When contains section. 

 Select Specific content and select the appropriate
 sensitive information for the rules. 

 Additionally, you can set custom content types to add content that might not
 be included in the predefined types. 

 When users try to type in the sensitive information, the sensitive
 information will be sanitized. 

 Webpage Watermarking 

 Mobile Browser - Partial support 

 Webpage watermarking enhances Data Loss Prevention (DLP) coverage by providing an
 additional layer of security. While screenshot restrictions can prevent users
 from capturing on-screen content, they do not prevent the use of external
 devices, such as smartphones, to take photos of the screen. This feature applies
 a visible overlay to webpages, serving as a deterrent against unauthorized
 information sharing. For optimal protection, it is recommended to use webpage
 watermarking in conjunction with screenshot control. 

 Webpage Watermark control intelligently applies watermarks exclusively to
 pages identified as containing sensitive content , minimizing user
 friction. This control is active only when you configure the ‘When Contains’
 parameter. 

 The watermark places information on the page, including: 

 Company Logo (if it's configured in the browser customization)

 Company Name (if it's configured in the browser customization)

 User's Email 

 Date and Timestamp 

 You can also specify the opacity of the watermark. 

 To set the Webpage Watermarking control: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Webpage Watermarking . 

 Select one of the following options: 

 Enable - The Prisma Browser 
 will display the watermark information to deter users from
 taking screenshots. 

 Select the Opacity level using the
 slider 

 Select the Watermark Rotation from the
 drop-down list. The options are -45, 0, or 45 degrees. 

 Select the Density of the watermark from
 the drop-down. The options are: 

 Low 

 Standard 

 High 

 For Color , select White to display the logo in a
 single color, or Standard, to display the logo in using its
 original color when uploaded. 

 Watermark Components - Watermarks enhance security by
 allowing teams to trace leaked screenshots without exposing
 sensitive information (PII) to bystanders. These QR codes
 provide a secure, machine-readable audit trail for sensitive
 pages. 
 Company logo - Uses the Company Logo as the
 watermark. 

 Text details - Uses various text components
 as the watermark. 

 QR code - When this component is enabled, the
 QR code contains The user's email address, page URL,
 exact timestamp of page load. The QR code is
 regenerated each time the page loads so as to
 maintain an audit trail using the information. 

 You can create a watermark
 using any combination of the components. You need to
 consider the following: 
 High Opacity: Improves scan success rates
 but may obscure underlying page content,
 potentially impacting user productivity. 

 Low Opacity: Enhances user productivity
 by keeping pages clearer, though it may reduce
 scan reliability if the QR code pixels overlap
 with complex page content. 

 Click Set . 

 Print 

 Mobile Browser - Partial support 

 This feature controls whether or not users can print from websites that match the
 URL, application, or category in the rule. To set the Print control: 

 The Print control can also be used to manage File
 Downloads by printing to a PDF. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Print . 

 Select one of the following options: 

 Allow - the Prisma Browser 
 will permit printing of webpages and files opened in the Prisma
 Access Browser. 

 Block - the Prisma Browser 
 will block all printing of webpages and files opened in the
 Prisma Access Browser. 

 If you want to enable Prompting notifications when you allow printing,
 click the down arrow next to Prompt: Pop-up
 notifications. 

 The Prompting notifications are not applicable
 for the Prisma Browser for Mobile. 

 Configure the following options: 

 Warn and allow to proceed anyway - Informs users
 about the risk or sensitivity of printing files, but
 allowing them to continue. 

 Warn and allow to proceed anyway with a reason -
 Informs users about the risk or sensitivity of printing
 files, and requires them to provide a reason to continue. 

 Permission request - Allows users to send a
 permission request to the admin. The user will be informed
 once the request is approved or denied. 
 Choose the timeframe for the permission. You can
 configure the permission to be used once, or for a
 timeframe ranging from 10 minutes to 90 days. 

 When you use this control, you can use your own dialog text to replace the
 default. To set the text, click Set dialog text .

 Click Set . 

 Screenshot 

 Prisma Browser Desktop Prisma Browser Extension Prisma Browser for Mobile 

 Full support Partial support Partial support 

 Content blur on screenshot attempt detection. Does not block screen
 sharing or video conferencing. Allow (Specific) setting allows you the following options 
 Allow screenshots using the browser's snipping tool. 

 Allow screen sharing using specific applications that you can
 select. 

 Linux/IGEL Browser - No support 

 Prisma Browser Extension —
 Screenshot protection on the extension uses content blur on capture attempt. The following
 limitations apply:

 The blur may trigger during certain user actions that are not actual screenshot
 attempts, including browser menu activation, mouse right-click events, switching
 away from the tab (Alt-Tab or Cmd-Tab), and returning to the tab from another
 window. 

 Screen sharing and video conferencing tools bypass the blur. Screenshot
 protection does not prevent screen content from being captured during screen
 sharing or video calls. 

 Prompting notifications (JIT messages) are not available for Screenshot controls
 on the Prisma Browser Extension. 

 This feature controls whether or not users can take screenshots (using
 snipping tools or Print Screen), record the screen, or share the screen with
 video conferencing tools from websites that match the URL, application, or
 category in the rule. To set the Screenshot control: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Screenshot . 

 Select one of the following options: 

 Allow - The Prisma Browser 
 allows you to select the tools that you permit your users to
 use. 

 Allow (Specific) – The Prisma Browser allows captures only from specific tools and
 under specific circumstances. Any other tool is blocked. 
 Allow screenshot by the browser’s snipping tool -
 You will be able to use the browser’s snipping tool; all
 other screenshot tools will be blocked. 
 This tool
 works with the Secured Screenshot feature and is the
 only available option for taking screenshots when
 the policy is set to Allow (Specific) , as
 other screenshot, screen share, or recording tools
 are blocked. 
 To enable the Snipping Tool, you must enable
 and display the Sidebar, which will show the
 Snipping Tool icon. 

 The control for the tool is located at the
 bottom of the sidebar or at the top of the browser
 page in the Tools and Actions section. 

 When a screen capture is taken, the image is
 sent to the clipboard. 

 The file is saved
 as an encrypted file in the Clipboard. If the File
 Download control is set as protected, then the
 screenshot file will be saved as a protected file.

 If the
 Clipboard control is set to block between
 applications, you won't be able to paste the
 screenshot to any unapproved
 applications. 

 Allow screen sharing by specific web apps - This
 option allows you to select which web apps can initiate
 screen sharing from a curated list of conferencing web
 apps, or by browsing all available apps. 

 To activate the feature, users need to share
 the tab that was specifically allowed, sharing the
 entire screen will remain blocked .

 Only web versions of apps can be allowed to
 initiate screen sharing - native desktop
 applications will remain blocked . 

 Custom and private applications cannot be
 chosen from the list at this time - reach out if
 there is a concrete need to specifically allow
 sharing to such an app. 

 Prisma Browser Extension and Prisma Browser for Mobile do not support selective
 screen sharing. 

 Block - Prisma Browser will block
 screen capture, screen recording, and screen sharing using video
 conference tools. This is the default behavior. 

 This will also block sharing when
 using remote session tools. 

 If you want to enable Prompting notifications when you allow screenshots,
 click the down arrow next to Prompt: Pop-up
 notifications. 

 The Prompting notifications are not applicable
 for the Prisma Browser for Mobile. Prompting is only available when you
 select Allow , and not Allow (Specific) . 

 Configure the following options: 

 Warn and allow to proceed anyway - Informs users
 about the risk or sensitivity of the action, but allows them
 to continue. 

 Warn and allow to proceed anyway with a reason -
 Informs users about the risk or sensitivity of the action,
 and requires them to provide a reason to continue. 

 Permission request - Allows users to send a
 permission request to the admin. The user will be informed
 once the request is approved or denied. 
 Choose the timeframe for the permission. You can
 configure the permission to be used once, or for a
 timeframe ranging from 10 minutes to 90 days. 

 Click Set . 

 GenAI Prompt 

 Prisma Browser Desktop Prisma Browser Extension Prisma Browser for Mobile 

 Full support Partial support No support 

 Content-aware prompt scanning is not supported. Allow and
 block enforcement only. 

 GenAI Prompt Control enables administrators to monitor and
 control data submitted to Generative AI applications and embedded AI
 widgets. The control applies to standalone applications such as ChatGPT,
 Microsoft Copilot, Gemini, Claude, and Perplexity , as well as AI
 widgets embedded within standard business tools — for example, Gemini in
 Google Workspace applications such as Docs, Drive, and Gmail, or Microsoft
 Copilot embedded in Microsoft Word and other Microsoft 365 web
 applications. 

 The control operates across multiple enforcement layers, leveraging
 last-mile analysis on the browser side to make it resilient against attempts
 to bypass policy enforcement. 

 For selective enforcement, configure the
 Block action together with the rule's
 When Contains section to restrict blocking to
 prompts that match specific DLP profiles — for example, blocking only
 prompts that contain PII, PHI, or proprietary content, while allowing all
 other prompts through. 

 Comparison with Typing Guard 

 The GenAI Prompt control and the Typing Guard control both address
 data entry in web applications, but they operate differently: 

 Typing Guard (Block mode) - Masks sensitive data
 while still allowing the prompt to be submitted with the sensitive
 content replaced. The original prompt reaches the AI provider, minus
 the redacted portions. 

 GenAI Prompt (Block) - Prevents the prompt from
 being submitted entirely. No part of the prompt reaches the AI
 provider. 

 Typing Guard operates at the DOM level only and may not reliably
 intercept input in all AI application implementations. The GenAI Prompt
 control enforces at multiple layers on the browser side, making it more
 suitable when complete prevention of data submission is required. 

 Tenancy Enforcement 

 To restrict rule enforcement to specific enterprise tenants,
 configure the Application Tenants step of the rule.
 This allows, for example, blocking prompts only when the user is logged into
 the organization's approved Claude organization, while allowing the same
 application when accessed with a personal account. 

 Tenancy enforcement is available for the following providers: 

 Provider Identifier 

 Claude Organization ID (UUID) or domain 

 ChatGPT (OpenAI) Domain, tenant ID, plan type, or account
 structure 

 Microsoft (Copilot / M365) Domain and resource host 

 Google (Workspace) Domain 

 Tenancy enforcement is configured in the
 Application Tenants step of the Access and Data
 Control rule, not in the GenAI Prompt control step itself. 

 Content Inspection 

 When set to Block , the Prisma Browser 
 can evaluate prompt text against configured DLP profiles before applying the
 enforcement action. Two types of data profiles are supported: 

 Local data profiles - Perform on-device pattern
 matching without sending prompt content to external services. 

 Cloud-assisted data profiles - Send prompt text to
 Palo Alto Networks cloud scanning services, enabling advanced
 classifiers including Advanced Machine Learning, LLM-based
 classifiers, Exact Data Matching (EDM), and Indexed Data Matching
 (IDM). 

 Content inspection is configured using the When
 Contains section of the rule. 

 Compliance Relevance 

 The GenAI Prompt control supports the following regulatory
 frameworks that require visibility and governance over AI interactions: 

 EU AI Act — Mandates tracking and auditing of AI
 system interactions for covered providers and deployers. 

 GDPR / CCPA — Requires organizations to verify that
 PII is not transmitted to third-party AI vendors without appropriate
 controls. 

 NIST AI RMF (AI 600-1) — Focuses on tracking harmful
 content, data provenance, and AI transparency. 

 HIPAA — Requires controls to prevent PHI from being
 shared with AI vendors that are not covered entities or business
 associates. 

 To set the GenAI Prompt control: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select GenAI Prompt . 

 Select one of the following options: 

 Allow - the Prisma Browser permits prompt submission. Prompt collection can be
 configured for allowed prompts in the rule's
 Tracking section. 

 Block - the Prisma Browser prevents the prompt from being submitted entirely. To
 selectively block based on prompt content, configure the
 rule's When Contains section with DLP
 profiles. Optionally, configure a custom dialog message to
 display to the user when a prompt is blocked. 

 Click Set . 

 Read-only Webpage 

 Mobile Browser - No support 

 You can now configure read-only mode for webpages that are contained
 within the Rule's scope. 

 This allows users to browse the information on web applications. Users
 can read the information, download files, but can't input data to any editable
 element in the page. This control isn't affected by specific content inspection
 - the settings in the When contains schedule. To
 configure the read-only webpage: 

 Read-only applies to HTML elements that are not
 editable. It does not prevent a web application from listening in to
 keyboard strokes, paste operations, mouse clicks, and so on. 
 This means that
 apps written in JavaScript, may still be fully editable if they are not
 built from standard HTML components such as HTML Forms. 

 An example
 for an app that is not working with Read-only control is Google
 Docs. 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Read-Only webpage . 

 Select one of the following options: 

 Enable - the Prisma Browser 
 will allow users to read and download the information on web
 applications but won't allow users to input information to any
 editable part of the page. Developer tools will be disabled on
 any webpage affected by this control. 

 Exclude Login Elements - Exclude username and
 password elements so that the user will be able to log on.

 Disable - the Prisma Browser does not
 block any user interaction with the web applications, subject to
 other rules. 

 When you use this control, you can use your own dialog text to replace the
 default. To set the text, click Set dialog text .

 Click Set . 

 Camera 

 Mobile Browser - No support 

 This feature controls whether or not websites that match the URL, application, or
 category in the rule have access to the device camera. This control isn't
 affected by specific content inspection - the settings in the When contains
 schedule. To set the Camera control: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Camera . 

 Select one of the following options: 

 Allow - the Prisma Browser 
 will allow using the camera in specific webpages. 

 Block - the Prisma Browser 
 will block using the camera in specific webpages. 

 Click Set . 

 Microphone 

 Mobile Browser - No support 

 This feature controls whether or not websites that match the URL, application, or
 category in the rule have access to the device microphone. this control isn't
 affected by specific content inspection - the settings in the When
 contains schedule. To set the Microphone control: 

 From Strata Cloud Manager , select Configuration Prisma Browser 
 Policy Controls Data Controls 

 Select Microphone . 

 Select one of the following options: 

 Allow - the Prisma Browser 
 will allow using the microphone in specific webpages. 

 Block - the Prisma Browser 
 will block using the microphone in specific webpages. 

 Click Set . 

 Previous 

 Configure Prisma Browser Data Controls 

 Next 

 Configure Threat Protection 

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
