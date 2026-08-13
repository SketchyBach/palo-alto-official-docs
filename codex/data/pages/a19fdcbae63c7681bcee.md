---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/csm-introduction/csm-getting-started-introduction/csm-tutorial
fetched_at: 2026-08-13T16:39:00Z
source: palo-alto-main
---

# Tutorial: Setting Up the Code Signing Capability Clear

Tutorial: Setting Up the Code Signing Capability 

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

 Tutorial: Setting Up the Code Signing Capability 

 Updated on 

 Tue Jul 28 08:20:33 PDT 2026 

 Focus 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Updated on 

 Tue Jul 28 08:20:33 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Introduction to the Code Signing Capability 

 Getting Started with the Code Signing Capability 

 Tutorial: Setting Up the Code Signing Capability 

 Next‑Gen Trust Security 

 Tutorial: Setting Up the Code Signing Capability 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Getting Started with the Code Signing Capability 

 Next 

 Configuring the Code Signing Capability 

 Tutorial: Setting Up the Code Signing Capability 

 This tutorial walks you through an end-to-end code signing workflow using the self-service scenario . In this scenario, an administrator creates a Signing Key and configures access, and a signer creates their own built-in account, authenticates the Code Sign Client, and signs a file. 

 This tutorial does not cover all available configuration options. Instead, it provides a focused workflow that demonstrates how the pieces fit together. 

 What You'll Do 

 This tutorial involves two roles: 

 Administrator — creates a custom role for signers, assigns it to a user, and creates a Signing Key. The administrator needs a role with write access to the Signing Keys page. 

 Signer — downloads the Code Sign Client, creates a built-in account, authenticates, and performs a signing operation. The signer needs a role with read access to the Signing Keys page and write access to the Built-in Accounts page. 

 You will complete the following tasks: 

 As the administrator: 

 Create a custom role for signers and assign it to a user on the TSG. 

 Create a Signing Key. 

 As the signer: 

 Download and install the Code Sign Client. 

 Create a built-in account and authenticate the Code Sign Client. 

 Sign a file and verify the signature. 

 View signing statistics and event logs. 

 Before You Begin 

 To complete this tutorial, you will need the following: 

 A user account with a role that has write access to the Signing Keys page on the TSG. 

 A second user account (or the ability to create one) to act as the signer. 

 A signing workstation where you can install the Code Sign Client. This can be a Windows, Linux, or macOS workstation. See system requirements . 

 Step 1: Create a Custom Role for Signers (Administrator) 

 Create a custom role that grants signers read access to the Signing Keys page and write access to the Built-in Accounts page. Then assign this role to the signer's user account on the TSG. 

 When creating the role, set the following permissions under Next-Gen Trust Security : 

 Permission Access level 

 Signing Keys Page View access 

 Built-in Accounts Page Write access 

 Assign this role to the user who will act as the signer in this tutorial. 

 Step 2: Create a Signing Key (Administrator) 

 Next, create a Signing Key within the TSG. The signer will use this key later in the tutorial. 

 Sign in to Next-Gen Trust Security. 

 Click Insights > Certificate Inventory > Signing Keys . 

 Click New . 

 In Basic information , do the following: 

 In Signing Key Name , enter Tutorial key . 

 In Description , enter This is my tutorial signing key . 

 Click Continue . 

 In Key pair properties , do the following: 

 For Key storage type , select your preferred storage type. 

 Key storage location is pre-selected based on your key storage type selection. 

 Set the validity period to 24 hours. 

 Select any Key algorithm . 

 Click Continue . 

 In Certificate properties , do the following: 

 Leave Certificate authority set to Built-in CA . 

 Leave Product option set to Default product . 

 For Common name , enter Tutorial, Inc . 

 All other fields are optional. 

 Click Continue . 

 In Cryptographic object creation , select Create cryptographic objects now , and then click Finish . 

 After the key and certificate are created, the details drawer for the Signing Key opens automatically. 

 Step 3: Download and Install the Code Sign Client (Signer) 

 The remaining steps are performed by the signer. 

 Start by downloading and installing the Code Sign Client from the Next-Gen Trust Security UI. 

 Sign in to Next-Gen Trust Security as the signer. 

 Click Insights > Certificate Inventory > Signing Keys . 

 Select Tutorial key to open its details drawer. 

 Note : For the purposes of downloading the client, you can select any Signing Key. We specify Tutorial key in this tutorial just to draw connection to the previous step. 

 Select the Client installation tab. 

 Select the appropriate platform for the signing machine, and then either download and install the client or follow the on-screen installation instructions. 

 Step 4: Create a Built-in Account and Authenticate the Code Sign Client (Signer) 

 Next, create a built-in account and use it to authenticate the Code Sign Client on the signing machine. 

 Click System Settings > Certificate Settings > Built-in Accounts . 

 Click New . 

 In the Use Case section, select Code Sign Manager . Click Continue . 

 In the Details section, do the following: 

 For Name , enter Tutorial account . 

 For Validity , enter 1 day. 

 For the authentication method, select Auto-generate a keypair and download the private key . 

 Note : This method generates the key pair in the UI. You will copy the private key to the signing machine and use it to authenticate the Code Sign Client. This method allows you to log the Code Sign Client out and then log it back in without generating a new key pair. 

 The alternative method, Generate your own keypair and upload the public key , generates the key pair on the signing machine instead, and you upload the public key to the UI. See Create a built-in account for details on both methods. 

 Click Create . 

 Copy the Private Key . 

 On the signing machine, create a PEM file (such as key.pem ) and paste the private key into that file. Save the file. 

 Return to the UI. Click Finish . The Built-in Accounts inventory page opens. 

 From the Built-in Accounts inventory page, copy the Client ID for this account. 

 On the signing machine, run the following command: 

 pkcs11config login --host <tsg-id>.ngts.paloaltonetworks.com --clientid <clientID> --keyfile <keyfile-name> 

 Note : The command examples in this tutorial use the pkcs11config utility. If you are using a different utility, adjust the commands accordingly. 

 (Optional) Verify your configuration: 

 pkcs11config option show 

 Your result should look similar to the following: 

 INFO: User configuration holds 9 values:
Name │ Value
───────────────────────────────┼───────────────────────────────────────────────────────
ACCESS EXPIRES │ 1776374034
AUTHENTICATION PRIVATE KEY PEM │ <365 characters redacted>
HSM SERVER URL │ https://xxxxxxxxxx.ngts.paloaltonetworks.com/vedhsm/
SUPPORTS API KEY │ true
ACCESS TOKEN │ <24 characters redacted>
AUTH SERVER URL │ https://xxxxxxxxxx.ngts.paloaltonetworks.com/
CREDENTIAL EXPIRES │ 1807908272
CSC SERVER URL │ https://dl.ngts.paloaltonetworks.com/code-sign-client/
CLIENT ID │ xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 

 Step 5: Sign a File and Verify the Signature (Signer) 

 With the Code Sign Client authenticated, perform a signing operation and verification on the signing machine. 

 On the signing machine, list your available Signing Keys: 

 pkcs11config list 

 If you have followed this tutorial, the output should look similar to the following: 

 Certificate 1:
Label: Tutorial key
Subject: CN=Tutorial\, Inc
ID: 64346264333165662D326333662D346539662D393665322D663461396561643138386331
Environment: Certificate

Public Key 1:
Label: Tutorial key
Key-Type: RSA 2048
ID: 64346264333165662D326333662D346539662D393665322D663461396561643138386331
Environment: Certificate 

 In a temporary directory, create a file called signme.txt : 

 echo "This is my test file" > signme.txt 

 Sign the file: 

 pkcs11config sign --filename signme.txt --label "Tutorial key" --output signme.txt.sig 

 If the signing succeeds, you will see a message similar to: 

 SUCCESS: Signed file 'signme.txt', signature written to 'signme.txt.sig'. 

 Note : 

 If the signing fails, try running pkcs11config sign without arguments to use the interactive signing wizard. 

 Verify the signature: 

 pkcs11config verify --filename signme.txt --label "Tutorial key" --output signme.txt.sig 

 Step 6: View Signing Statistics and Event Logs 

 After the Signing Key is used, its activity appears in both the usage counts and the event logs. 

 In the Next-Gen Trust Security UI, return to Insights > Signing Keys to confirm that the key now shows signing activity. 

 To view detailed events, open the event log at System Settings > Event Logs and filter for Signing succeeded events. 

 Conclusion 

 You have successfully set up the code signing capability using the self-service model. The administrator created a Signing Key and configured a role for the signer. The signer then created their own built-in account, authenticated the Code Sign Client, and signed a file — all without needing access to create or manage Signing Keys. 

 The private key used for signing was generated and stored securely in your selected key storage location and was never present on the signing machine. 

 What's Next 

 Review Setting up access for code signing to explore other access patterns for your environment. 

 Continue creating Signing Keys as needed for your use cases. 

 Review the CLI documentation to learn more about all available options. 

 Explore sample integrations for common code signing applications. 

 Previous 

 Getting Started with the Code Signing Capability 

 Next 

 Configuring the Code Signing Capability 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on Dell PowerEdge 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 Next-Gen Trust Security 

 Getting Started 

 Certificate Management 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
