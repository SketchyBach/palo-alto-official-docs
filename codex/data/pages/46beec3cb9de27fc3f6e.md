---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/managed-ai-runtime-security-for-aws/managed-airs-for-aws-protect/managed-airs-for-aws-secure-ai-traffic
fetched_at: 2026-09-16T07:54:45Z
source: ai-security
---

# Secure AI Traffic on Managed AIRS for AWS Clear

Updated on 

 Mon Aug 24 04:41:52 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Administration 

 Managed AI Runtime Security for AWS 

 Protect 

 Secure AI Traffic on Managed AIRS for AWS 

 Download PDF 

 Prisma AIRS 

 Secure AI Traffic on Managed AIRS for AWS 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Supply Chain Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Secure Amazon EKS Traffic 

 Next 

 Author and Enforce Managed AIRS for AWS Policies in AIRS Profile 

 Secure AI Traffic on Managed AIRS for AWS 

 Configure security rules to protect AI traffic flowing through Managed AIRS for
 AWS. 

 Where Can I Use This? What Do I Need? 

 Managed AIRS for AWS 

 Access to Strata Cloud Manager (SCM) 

 Prerequisites: 

 Ensure the structural configuration snippet includes the baseline default
 AIRS best practices profile for proper classification. 

 Outbound SSL decryption rules must be explicitly configured alongside
 matching decryption certificates. Since prompt data payloads are encrypted under
 standard HTTPS traffic, a lack of decryption configuration prevents the firewall
 from parsing payload contents, rendering threat inspection non-functional. The
 application chatbot or container pod store must be configured to trust this root
 certificate in its CA chain. 

 Following are the steps to secure and configure security rules to protect
 AIT traffic on Managed AIRS for AWS: 

 Deploy Managed AIRS for AWS in
 Strata Cloud Manager . 

 Create Endpoints for Managed AIRS for
 AWS . 

 Author and Enforce Managed AIRS for AWS Policies in AIRS Profile . 

 Previous 

 Secure Amazon EKS Traffic 

 Next 

 Author and Enforce Managed AIRS for AWS Policies in AIRS Profile
