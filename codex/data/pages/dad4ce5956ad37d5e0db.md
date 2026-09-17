---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/about-built-in-accounts/t-built-in-accounts-create-scanafi
fetched_at: 2026-09-16T07:24:21Z
source: palo-alto-main
---

# Create a Scanafi Built-in Account Clear

Updated on 

 Fri Sep 04 10:31:48 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Built-in Accounts Overview 

 Create a Scanafi Built-in Account 

 Next‑Gen Trust Security 

 Create a Scanafi Built-in Account 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Scopes and Built-in Account Permissions 

 Next 

 Toggling a Built-in Account On or Off 

 Create a Scanafi Built-in Account 

 Scanafi built-in accounts use a private key and Client ID for authentication. 

 For more information about downloading and installing the Scanafi utility, refer to Downloading and Installing Scanafi . 

 Before You Begin 

 Before creating a Scanafi built-in account, you must complete the following tasks: 

 By completing these prerequisites, you ensure that your built-in accounts are configured correctly and ready to handle authentication requests using modern security protocols. 

 To Create a Scanafi Built-in Account 

 Sign in to Next-Gen Trust Security. 

 Click System Settings > Certificate Settings > Built-in Accounts . 

 Click New . 

 Choose the desired use case from the Use case list, and click Continue . The use cases available for you to choose depend on which Next-Gen Trust Security components you have licenses for. 

 Enter a Name for your new built-in account. 

 (Conditional) Enter the number of days for which you want the account to remain valid in the Validity (days) field. You can select any number from 1 to 365 days. This step doesn't apply when creating a Custom API Integration built-in account. 

 Select a Key pair authentication method. 

 Note: 

 Selecting Key pair - Auto-generate a keypair and download the private key requires you to copy the public and private key values used for authentication. 

 Selecting Key pair - Generate your own keypair and upload the public key requires you to provide your own the public key in PEM format for authentication. 

 Select the desired Scope , making sure it matches the permissions and access requirements of your built-in account, and then click Continue . Learn more 

 (Conditional) After selecting a key pair authentication method and scope options, click Create or Continue . 

 (Conditional) If you previously selected Key pair - Auto-generate a keypair and download the private key , copy the public and private key values used for authentication. 

 (Conditional) If you previously selected Key pair - Generate your own keypair and upload the public key enter your public key in PEM format for authentication. 

 After entering all the details, review the information to ensure it's correct and then click Finish to create the new built-in account. 

 Related Links 

 Toggling Built-in Accounts on or Off 

 Editing Built-in Account Settings 

 Deleting Built-in Accounts 

 Overview of Built-in Accounts 

 Downloading and Installing Scanafi 

 API Reference 

 Reference: Service Account API endpoint 

 Reference: creating built-in accounts 

 Previous 

 Scopes and Built-in Account Permissions 

 Next 

 Toggling a Built-in Account On or Off
