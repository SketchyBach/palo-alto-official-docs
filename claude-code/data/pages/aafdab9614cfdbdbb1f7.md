---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/integrations-overview/credential-managers-overview/setting-up-hashicorp-integration
fetched_at: 2026-09-16T08:21:39Z
source: palo-alto-main
---

# Setting Up a HashiCorp Integration Clear

Updated on 

 Sep 4, 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Welcome to Integrations 

 Credential Managers Overview 

 Setting Up a HashiCorp Integration 

 Next‑Gen Trust Security 

 Setting Up a HashiCorp Integration 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Setting Up a CyberArk Integration 

 Next 

 Notification Providers Overview 

 Setting Up a HashiCorp Integration 

 Next-Gen Trust Security uses the HashiCorp Vault as a Privileged Access Manager (PAM) to access credentials stored in HashiCorp. Once the connection between HashiCorp and Next-Gen Trust Security is established, you can create credential references from Next-Gen Trust Security to credentials stored in HashiCorp. 

 Credential references can then be assigned to a machine in Next-Gen Trust Security. When you want to provision a certificate to that machine, Next-Gen Trust Security uses the HashiCorp credential to access the machine. 

 Since Next-Gen Trust Security creates a reference to the HashiCorp credential, any update to the credential in HashiCorp will be automatically used by Next-Gen Trust Security when provisioning a certificate to a machine. 

 Note (HashiCorp feature enablement): Creating the HashiCorp connector and importing credentials requires the Superuser role and Tenant selected in the workspace switcher. Credential Managers is visible from any workspace, but with a workspace selected it is read only and the buttons for adding a connector are unavailable. See Workspace-Scoped Resources . 

 If you don't see the menu options mentioned in the steps below, please contact support. 

 Note (Supported HashiCorp versions): Next-Gen Trust Security supports HashiCorp Vault as a Privileged Access Manager (PAM) . 

 Supported versions: 1.16 and later 

 Step 1: Deploy VSatellites in Your Datacenter 

 If you don't already have any VSatellites installed, you'll need to get those up and running first. VSatellite is the connector between Next-Gen Trust Security and HashiCorp. 

 The VSatellites need to be able to access HashiCorp in your datacenter. Before proceeding with the next step, make sure to have the IP addresses of the VSatellites readily available. 

 Follow our documentation to deploy VSatellites . 

 Step 2: Set Up the HashiCorp Integration in Next-Gen Trust Security 

 With VSatellites now in place, you're ready to create an application in HashiCorp and then connect Next-Gen Trust Security to that application. 

 Before You Begin 

 Ensure that your HashiCorp Vault server meets the following requirements before configuring the integration with Next-Gen Trust Security: 

 The Vault server must be reachable from your VSatellite instance . 

 If your Vault instance uses policies to control access, you must configure a policy to grant access to Vault PKI paths. You can create this policy using the HashiCorp Configuration Language (HCL) . For more information, see HashiCorp Vault Policies . 

 If your HashiCorp Vault instance requires certificate-based authentication, ensure that you have the necessary certificate available for Next-Gen Trust Security to authenticate. 

 Performed by : Superuser 

 Sign in to Next-Gen Trust Security. 

 Click Configuration > Certificate Integrations > Credential Managers . 

 Under HashiCorp Vault Configuration , complete the fields according to the following guidelines: 

 Vault Service URL : The URL of the HashiCorp Central Credential Provider web service. 

 Authentication Type : The method you will use to authenticate to HashiCorp. The following options are supported: 

 Certificate Credential : The certificate credential required to authenticate to the HashiCorp service. After you upload the certificate, you'll be prompted to enter the certificate password. 

 Username and Password : The username and password required to authenticate to the HashiCorp service. After you select Username and Password , you'll be prompted to enter the username and password. 

 Note: Too many failed attempts to authenticate with a username and password will result in a user lockout. For more information, refer to the HashiCorp documentation . 

 Token : The token credential required to authenticate to the HashiCorp service. After you select Token , you'll be prompted to enter the token. 

 Choose a VSatellite : The list of VSatellites that are allowed to connect to HashiCorp. These VSatellites must be whitelisted on the HashiCorp application. 

 Click Test Access . 

 Click Save . 

 Step 3: Import Credentials from HashiCorp 

 With the connector now in place, you can import credentials into Next-Gen Trust Security. HashiCorp credentials in Next-Gen Trust Security are just references to the real credentials stored in HashiCorp. 

 Before You Begin 

 Set up a team that will be allowed to use the imported credentials. The team assigned to the credential should be the same team that will be assigned to the machine in Step 4 below. 

 Have the Secret Path and the Secret Key Name for the HashiCorp credential you want to import. 

 Performed by : Superuser 

 Click Insights > Certificate Installations > Credentials . 

 Click New > HashiCorp Credential . Complete the fields on the Add a new credential screen according to the following guidelines: 

 Name : The name for this credential to be displayed in Next-Gen Trust Security. 

 Access Type : The type of credential that Next-Gen Trust Security will receive from HashiCorp. The type you select determines if Next-Gen Trust Security will reference only the password, or both the username and password from an account in HashiCorp. 

 Secret Path : The full path in HashiCorp Vault where the credential is stored.The Secret Path should include "/data/" after the Key-Vault Secret Engine name in the case of KV v2 key paths (as documented here . For example, in the case of KV v2, this value should be "kv/data/test1" . In the case of KV v1, it should be "kv/test1" . 

 Secret Key Name : The name of the key for the stored secret. 

 Example: In the following HashiCorp Vault entry: 

 The key "admin" is the Secret Key Name . 

 Click Save . The Credentials page opens with your new credential listed. 

 Test the credential you just created by clicking the vertical ellipses icon on the row of the new credential, and selecting Test Access . 

 Step 4: Assign the HashiCorp Credential On a Next-Gen Trust Security Machine 

 Performed by : Superuser 

 Now that the credential is in Next-Gen Trust Security, you can assign it to a machine . Pay attention to the following when creating a new machine that you want to use this credential: 

 During machine configuration, when asked for a Credential Type, choose Select Credentials , and then select your HashiCorp credential. 

 Related Links 

 Credential managers overview 

 Integrations overview 

 Previous 

 Setting Up a CyberArk Integration 

 Next 

 Notification Providers Overview
