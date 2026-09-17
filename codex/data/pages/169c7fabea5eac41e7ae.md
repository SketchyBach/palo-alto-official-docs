---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/co-overview-issuing-certs/adding-a-certificate-authority/c-custom-ca-overview/r-sectigo-example/c-sectigo-certificate-terms
fetched_at: 2026-09-16T07:25:02Z
source: palo-alto-main
---

# Sectigo Certificate Term Settings and Issuance Validity Clear

Updated on 

 Fri Sep 04 10:31:48 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Overview: Certificate Issuance 

 Adding a Certificate Authority 

 Create a Custom Certificate Authority (CA) 

 Create a Sectigo Certificate Manager (VSatellite) Configuration 

 Sectigo Certificate Term Settings and Issuance Validity 

 Next‑Gen Trust Security 

 Sectigo Certificate Term Settings and Issuance Validity 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Create a Sectigo Certificate Manager (VSatellite) Configuration 

 Next 

 Creating a SwissSign Connector 

 Sectigo Certificate Term Settings and Issuance Validity 

 When creating certificates, Sectigo's certificate profiles use static "terms" instead of an arbitrary number of days to determine certificate validity periods, while Next-Gen Trust Security uses arbitrary numbers. 

 The Sectigo CA Connector accounts for this difference by intelligently matching the number you select to the closest Sectigo term setting. 

 The following table gives an example of how a Next-Gen Trust Security request could match to the Sectigo terms, if these are the terms that apply to the Sectigo account: 

 Next-Gen Trust Security request Sectigo term options Result 

 7 day certificate request Sectigo minimum term length is 30 days Issued certificate will be valid for 30 days. 

 20 day certificate request Sectigo terms allow for 15 day, 45 day, or 90 day terms Issued certificate will be valid for 45 days, since that is the minimum term that covers the requested period. 

 2 year certificate request Sectigo maximum term length is 398 days for your account Issued certificate will be valid for 398 days, since that is the maximum allowed by any available term. This is the only case where the issued certificate will be valid for a shorter term than was requested. 

 When you create a request policy in Next-Gen Trust Security, you specify the maximum validity a user may request, and this is the default validity that is used if the user does not specify a validity in their request. 

 Because of the way Next-Gen Trust Security maps validity to available terms in Sectigo, it is possible for the validity of issued certificates to exceed the maximum validity specified by the request policy. This scenario is possible in situations where the maximum validity specified in the request policy does not exactly match one of the defined Sectigo terms, and only if the Sectigo term is longer than the maximum request policy validity. Consider these two examples: 

 Next-Gen Trust Security request Max validity from request policy Sectigo terms Result 

 150 days 180 days 45 days, 90 days The issued certificate will be valid for 90 days 

 150 days 180 days 100 days, 200 days The issued certificate will be valid for 200 days 

 Previous 

 Create a Sectigo Certificate Manager (VSatellite) Configuration 

 Next 

 Creating a SwissSign Connector
