---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/advanced-url-filtering/administration/url-filtering-features/url-filtering-response-pages/predefined-url-filtering-response-pages.html
fetched_at: 2026-09-16T12:58:21Z
source: palo-alto-main
---

# Predefined URL Filtering Response Pages Clear

Updated on 

 Jul 30, 2026 

 Focus 

 Home 

 Advanced URL Filtering 

 URL Filtering Features 

 URL Filtering Response Pages 

 Predefined URL Filtering Response Pages 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced URL Filtering 

 Predefined URL Filtering Response Pages 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Previous 

 URL Filtering Response Pages 

 Next 

 URL Filtering Response Page Objects 

 Predefined URL Filtering Response Pages 

 Review images and descriptions of the URL filtering response pages provided by
 default. 

 Where can I use
this? What do I need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 Advanced URL Filtering
 license (or a legacy URL filtering license) 

 Notes: 

 Legacy URL filtering licenses are discontinued, but
 active legacy licenses are still supported. 

 Prisma Access licenses include Advanced URL Filtering capabilities. 

 URL filtering response pages display on web
 browsers when access to a requested URL has been restricted. Each response page explains
 why the page cannot be accessed, and most pages list information about the user, the
 requested URL, and the URL category that triggered the blocking action. 

 You may observe variations in the appearance of the response pages across different
 PAN-OS software releases. However, the functionality remains the same. 

 Remember that you can customize the response pages to meet your
 specific needs. 

 URL Filtering and Category Match Block Page 

 Access to a URL category is blocked either in the URL Filtering profile associated with the
 matching Security policy rule or because the URL category is a match condition
 in a Security policy rule that denies access. 

 URL Filtering Continue and Override Page 

 Page with an initial block policy rule that allows users to bypass the restriction by clicking
 Continue . With URL Admin Override enabled ( Allow Password Access to Certain
 Sites ), after clicking Continue , users must enter
 the URL Admin Override password to access the requested URL. 

 This response page displays over HTTP on port 6080 with
 an encrypted URL parameter. 

 URL Filtering
Safe Search Block Page 

 Access blocked by a Security policy rule with a URL Filtering profile with the Safe Search
 Enforcement option enabled (see Safe Search Enforcement ). Users see
 this page if a search is performed using Google, Bing, Yahoo, or Yandex and
 their browser or search engine account setting for Safe Search is not set to
 strict. 

 Anti Phishing
Block Page 

 This page displays to users when they attempt to enter corporate credentials (usernames or
 passwords) on a web page in a category for which credential submissions are
 blocked. The user can continue to access the site but remains unable to submit
 valid corporate credentials to any associated web forms. To control the sites to
 which users can submit corporate credentials, you must configure User-ID and
 enable credential phishing
 prevention based on URL category. 

 Anti Phishing
Continue Page 

 This page warns users against submitting
credentials (usernames and passwords) to a web site. Warning users
against submitting credentials can help to discourage them from
reusing corporate credentials and to educate them about possible
phishing attempts. They must select Continue to proceed to credentials
on the site. To control the sites to which users can submit corporate credentials,
you must configure User-ID and enable credential phishing
prevention based on URL category. 

 Previous 

 URL Filtering Response Pages 

 Next 

 URL Filtering Response Page Objects
