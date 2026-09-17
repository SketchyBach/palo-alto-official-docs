---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/notification-center-cco/t-notification-branding
fetched_at: 2026-09-16T07:25:25Z
source: palo-alto-main
---

# Configure Notification Branding Settings Clear

Updated on 

 Fri Sep 04 10:31:48 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Notification Rules Overview 

 Configure Notification Branding Settings 

 Next‑Gen Trust Security 

 Configure Notification Branding Settings 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Advanced Filter Criteria 

 Next 

 Create Notification Templates 

 Configure Notification Branding Settings 

 Use the notification branding page to customize the branding that appears in emails sent by Reports and Notification Rules. Apply your organization's logo, header, footer, and call-to-action (CTA) text consistently across those messages. 

 You can configure any combination of logo, header, footer, and call-to-action. CTA Text requires a CTA Link. If you provide a CTA Link without CTA Text, the link appears as a full URL. 

 To Configure Branding Settings 

 Sign in to Next-Gen Trust Security. 

 Click Configuration > Certificate Notifications > Notification Branding . 

 In the Upload Logo field, enter the URL of the branding image you want to include in notifications. 

 This image isn't stored on CyberArk servers, so ensure the URL is publicly accessible. Images should be at least 75 px tall, with a recommended 2:1 aspect ratio (twice as wide as tall). 

 If you don't specify a value, the CyberArk logo will be used. 

 In Header Text , enter the text you want to appear before the notification content. 

 In Footer Text ,enter the text you want to appear after the notification content. 

 In Footer Call To Action (CTA) Text , enter the display text for a link displayed after the Footer Text. 

 If you specify a CTA Text value, the CTA Link field becomes required. 

 In Footer Call To Action (CTA) Link , enter the URL destination for the link displayed below the footer. 

 If you provide a CTA link without CTA text, the bare URL is shown in the notification. 

 Click Save . 

 To Test Notification Branding 

 Click Send Test Email . 

 A test email is sent to the email address associated with your account. The message is from notification@venafi.cloud . 

 Fields at a Glance 

 Use the table below to review the available Notification Branding fields. 

 Field Description Notes 

 Logo Link URL of the branding image shown at the top of emails. - Must be publicly accessible (not stored on CyberArk servers).- Recommended size: ≥75 px tall, 2:1 aspect ratio.- If not set, the CyberArk logo is used. 

 Header Text Text shown above the notification content. Optional. Keep it short (org name, tagline, etc.). 

 Footer Text Text shown below the notification content. Optional. Often used for disclaimers or copyright. 

 Footer Call To Action (CTA) Text Display text for a clickable link under the footer. Optional. Requires a CTA Link . 

 Footer Call To Action (CTA) Link URL opened when the CTA is clicked. - Required if CTA Text is set.- If provided without CTA Text, the bare URL is displayed. 

 Previous 

 Advanced Filter Criteria 

 Next 

 Create Notification Templates
