---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/csm-introduction/csm-setup-overview/csm-certificate-authority
fetched_at: 2026-09-16T07:25:08Z
source: palo-alto-main
---

# Configure a Certificate Authority (Optional) Clear

Updated on 

 Sep 4, 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Introduction to the Code Signing Capability 

 Configuring the Code Signing Capability 

 Configure a Certificate Authority (Optional) 

 Next‑Gen Trust Security 

 Configure a Certificate Authority (Optional) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Onboard Users 

 Next 

 Create a Signing Key 

 Configure a Certificate Authority (Optional) 

 If you want Next-Gen Trust Security to issue a code signing certificate along with the key, you will need to select a certificate authority (CA) when creating the Signing Key. Some CAs require no setup, while others require configuration before they can be used: 

 None -- creates only a key pair with no certificate 

 Built-in CA -- requires no configuration and is suitable for internal trust use cases, such as development builds. Certificates issued by the Built-in CA are not implicitly trusted by browsers or operating systems. 

 Microsoft AD CS, DigiCert, and Zero Touch PKI -- require certificate authority connectors to be configured before use 

 Notes : 

 If you plan to obtain a certificate from a public certificate authority, you must select AWS KMS as the key storage type when creating the Signing Key. Public CAs will not sign a CSR for a key that is not stored on a hardware HSM. 

 Certificate authority connectors must be configured under Tenant , because the Certificate Authorities page is available only when Tenant is selected in the workspace switcher. Once configured, the CA is available for selection when creating a Signing Key in any workspace. 

 While Next-Gen Trust Security supports additional certificate authorities for issuing TLS certificates, only the CAs listed above are supported for issuing code signing certificates through the code signing capability. 

 For details about setting up certificate authority connectors, see the CA configuration documentation . 

 What's Next 

 After configuring a certificate authority (if needed), continue with Create a Signing Key . 

 Related Links 

 CA configuration 

 Built-in CA 

 Microsoft AD CS 

 DigiCert 

 Zero Touch PKI 

 Previous 

 Onboard Users 

 Next 

 Create a Signing Key
