---
url: https://docs.paloaltonetworks.com/prisma-browser/administration/manage-prisma-browser-policy-profiles/configure-prisma-browser-data-controls/configure-data-leak-prevention/webpage-data-masking
fetched_at: 2026-09-16T08:21:51Z
source: palo-alto-main
---

# WebPage Data Masking Clear

Updated on 

 Thu Sep 10 09:47:19 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Manage Prisma Browser Control Sets 

 Configure Prisma Browser Data Controls 

 Configure Data Leak Prevention 

 WebPage Data Masking 

 Download PDF 

 Prisma Browser 

 WebPage Data Masking 

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

 Clipboard 

 Next 

 Typing Guard 

 WebPage Data Masking 

 Webpage Data Masking Controls 

 Prisma Browser Desktop Prisma Browser Extension Prisma Browser for Mobile 

 Full support No support No support 

 This control allows you to mask textual content within webpages. The
 masking is set according to either predefined information types (PII or PCI) or a
 custom regex. 

 When this is enabled, the browser will inspect and mask any webpage or
 frame within the webpage. This will be done only in situations where the URL in the
 browser tab or the URL in the frame is matched. To enable Webpage Data Masking: 

 From Strata Cloud Manager , select Configuration Policy Control Sets Data Control Data Leak Prevention 

 Select Webpage Data Masking . 

 Select one of the following options: 

 Enable - the Prisma Browser will
 mask URLs in tabs or frames that match the conditions. Select the
 masking pattern: 

 Mask all characters. 

 Leave the last characters unmasked. 

 Leave the first characters unmasked. 

 You can choose to unmask up to 4
 characters. 

 Disable - the Prisma Browser won't mask
 URLs in tabs or frames that match the conditions. 

 Prompt - Optionally select one of the following prompt
 options: 

 None - Do not use pop-up notifications. 

 Pop-up notifications 
 Warn and allow to proceed anyway - the
 prompt will freeze the sensitive information until the user
 acknowledges the message. 

 Warn and allow to proceed anyway with a
 reason - the prompt will freeze the sensitive
 information until the user acknowledges the message and selects
 a reason. 

 Permission request - the prompt will
 freeze and mask the sensitive information until permission is
 granted. 

 Click Set . 

 Previous 

 Clipboard 

 Next 

 Typing Guard
