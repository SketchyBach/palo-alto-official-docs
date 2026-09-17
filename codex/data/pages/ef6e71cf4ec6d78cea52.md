---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/co-overview-issuing-certs/distributed-issuer-overview/add-configurations
fetched_at: 2026-09-16T07:25:04Z
source: palo-alto-main
---

# Add Configurations Clear

Updated on 

 Fri Sep 04 10:31:48 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Overview: Certificate Issuance 

 Distributed Issuer Overview 

 Add Configurations 

 Next‑Gen Trust Security 

 Add Configurations 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Save Installation Credentials 

 Next 

 Network Clients with JWT 

 Add Configurations 

 Configurations are runtime settings that define how Distributed Issuer operates through a bootstrap performed at startup. They link a sub CA provider, policies, and client configurations that define which clients can interact with Distributed Issuer and how they authenticate. 

 Prerequisites 

 In Next-Gen Trust Security, a Superuser user role. 

 A subordinate CA provider . 

 At least one policy . 

 At least one Built-in Account . 

 Your IdP type (OIDC or JWKS) and its discovery URL or JWKS URI. 

 Note : You can create configurations in any workspace, and each configuration belongs to the workspace it was created in. Inside a workspace, however, the only subordinate CA providers and policies you can choose from are the ones shared with that workspace under Tenant . Under Tenant , the Issuer Configurations page adds a Workspace column naming the owner of each configuration. 

 Step 1: Add General Settings 

 Add general configuration properties and optionally, enable logging. 

 Sign in to Next-Gen Trust Security. 

 Click Configuration > Certificate Configuration > Issuer Configurations . 

 On the Issuer Configurations page, click New . 

 Enter a configuration Name . 

 Select a Sub CA Provider . 

 Select one or more Built-in Accounts . A Built-in Account can only connect to one configuration, but a single configuration can have multiple Built-in Accounts. 

 (Optional) Under Advanced Security & Logging Settings , select Log certificate issuance information and Include raw certificate data . 

 (Optional) If you'll install Distributed Issuer using a FIPS image, select Require Issuer instances to be FIPS compliant . 

 Click Continue . 

 Step 2: Configure Client Access 

 The Client Configuration section controls how clients connect to Distributed Issuer. Select one or both network client options, or skip both for local-only access. 

 Network Clients (REST, gRPC, Remote cert-manager) 

 Select this option to allow clients to connect using JSON Web Token (JWT) authentication. See Network Clients with JWT to finish the configuration. 

 Network Clients Authenticated with Instance Metadata 

 Select this option to allow cloud VM instances to authenticate with signed identity documents. See Network Clients with Instance Metadata to finish the configuration. 

 Local-only Access 

 If you select neither network client option, local access via Unix Domain Sockets (UDS) is always available. With this setup, cert-manager must be installed in the same environment. 

 Do the following to finish the configuration. 

 Under Policies , select the Allowed Policies that clients can use. 

 Click Create to save the configuration. 

 What's Next? 

 Once the configuration is complete, it's time to install Distributed Issuer. Installation is CLI-based and requires access to your Kubernetes cluster or Linux host. 

 For more information, see Installation Overview on the NGTS developer documentation site. 

 Previous 

 Save Installation Credentials 

 Next 

 Network Clients with JWT
