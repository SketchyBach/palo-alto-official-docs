---
url: https://docs.paloaltonetworks.com/remote-browser-isolation/administration/remote-isolated-browsing-experience/in-browser-translation
fetched_at: 2026-08-13T17:32:14Z
source: palo-alto-main
---

# In-Browser Translation Clear

In-Browser Translation 

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

 In-Browser Translation 

 Updated on 

 Thu Apr 09 09:06:48 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 Português (Portuguese) 

 Filter

 Expand All 
 | 
 Collapse All 

 Remote Browser Isolation Docs 

 Administration 

 Release Notes 

 New Features 

 Updated on 

 Thu Apr 09 09:06:48 PDT 2026 

 Focus 

 Home 

 Remote Browser Isolation 

 Isolated Browsing Experience 

 In-Browser Translation 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 Português (Portuguese) 

 Remote Browser Isolation 

 In-Browser Translation 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Remote Browser Isolation Docs 

 Administration 

 Release Notes 

 New Features 

 Previous 

 Print in Isolation 

 Next 

 Monitor Remote Browser Isolation 

 In-Browser Translation 

 Understand how RBI in-browser translation uses integrated
 translation services in remote browsing sessions. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Minimum required Prisma Access version: 5.2.1 Innovation
 and Preferred 

 Prisma Access 
 license with the
 Mobile User or Remote Networks license subscription 

 Remote Browser Isolation
 license 

 Remote Browser Isolation (RBI) in-browser translation enables users to translate web content
 within their RBI sessions using integrated translation services.
 This feature preserves the native browser translation experience while maintaining the
 security boundaries of the remote browsing environment. 

 How RBI In-Browser Translation Works 

 To provide the functionality
 for webpage translation, remote web browsers running in the RBI 
 infrastructure in Prisma Access deployments use integrated cloud translation
 services. The translation process occurs entirely within the remote browser
 container, ensuring that the end-user device remains completely isolated and never
 communicates with the translation service's API. End-user information is never
 exposed to the external API, and no code from that service is executed on the
 end-user device. 

 The feature automatically detects each user's browser preferred language from their
 local browser settings and uses the preferred language as the default translation
 target language. When users encounter web content in a different language, they can
 translate either entire pages or selected text portions without switching between
 applications or compromising the secure browsing session. 

 For
 RBI users accessing isolated websites through Prisma Access China deployments , users can translate only
 entire webpages to their preferred language, not selected text portions. 

 User Language Detection 

 RBI automatically identifies each user's preferred language from
 their local browser. This becomes the default translation target language displayed
 in context menus and translation widgets. Users have the option to translate to a
 language other than the preferred language within the translation widget. 

 The system respects the browser's preferred language list order when determining
 translation defaults, but does not use the local browser's Translate into
 this language setting from translation preferences. Only the primary
 language preference influences RBI translation behavior. 

 Use In-Browser Translation 

 Before using in-browser translation in isolated browsing sessions, your users should
 configure their local browser's language preferences to establish the preferred
 translation target language. Users should navigate to their browser's language
 settings and ensure their preferred language appears first in the language list, as
 RBI automatically detects this setting to determine default
 translation options. 

 Users can use RBI in-browser translation to: 

 Translate entire webpages 
 When users access websites through an RBI
 session and navigate to content written in a foreign language, they can
 right-click anywhere on the webpage to open the context menu and select
 Translate to [language] , where the language
 displayed matches the browser's preferred language setting. The translation
 widget appears at the top of the page showing the detected source language
 and the selected target language. 

 After selecting Translate to [language] , the
 webpage content will be translated and the translation widget will appear,
 showing the original and target language options: 

 For RBI China, the
 translation widget does not appear. Users will see a progress indicator
 during the initial translation process, and once translation is complete,
 the context menu option changes to allow them to revert to the original
 content 

 Users can use the translation widget to modify translation
 settings for the current page. They can click the three-dot menu to select
 different target languages from the drop-down if they prefer translating to
 a language other than the browser default. If the user visits a page
 multiple times and translates the page each time, the widget provides the
 option to always convert the page to the target language in future
 visits. 

 The positioning of the language drop-down might appear offset
 from the expected location, particularly in scaled or zoomed
 browser sessions. On mobile devices, some widget elements might
 appear clipped due to space constraints when rendering without
 proper scaling context. 

 RBI in-browser translation is invoked only
 from the context menu. If the user uses the option to translate
 from the browser menu, translation only occurs for RBI interface elements like download
 dialogs or floating action buttons, the actual webpage content
 won't be translated. Users must rely exclusively on right-click
 context menu options to translate webpage content within RBI sessions. 

 Translate selected text 
 Users can highlight specific text portions on
 any webpage that they want to translate without translating the entire page.
 Right-click on the selected text to access the context menu and select
 Translate selection to [language] . The
 translation widget displays the original selected text alongside the
 translated version, enabling you to compare the content directly. 

 Translating selected
 text is not available for RBI China. Users can translate the entire webpage,
 not portions of the page. 

 After selecting Translate
 selection to [language] , the translated text will appear in
 the translation widget as follows: 

 When translating selected text, only the
 widget with the selected translation is shown. Users can’t use advanced
 options like selecting another target language or accessing the three-dot
 menu in the translation widget. 

 Close the translation widget by
 clicking the X or navigating away from the page to
 return to the original language content. The system maintains the user's
 translation preferences and will apply automatic translation settings to
 subsequent pages based on their previous selections. 

 Previous 

 Print in Isolation 

 Next 

 Monitor Remote Browser Isolation 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Remote Browser Isolation 

 Administration 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
