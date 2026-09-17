---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/harden-endpoint-security/disk-encryption
fetched_at: 2026-09-16T08:44:03Z
source: cortex-platform
---

# Disk encryption | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Endpoint security 

 Install and manage endpoints 

 Set up endpoint protection 

 Harden endpoint security 

 Disk encryption 

 For enhanced security, you can configure and apply disk encryption profiles to the disks of your Windows and Mac endpoints. 

 Cortex XDR provides full visibility into encrypted Windows and Mac endpoints that were encrypted using BitLocker and FileVault, respectively. Additionally, you can apply Cortex XDR Disk Encryption rule on the endpoints by creating disk encryption rules and policies that leverage BitLocker and FileVault capabilities. 

 Before you start applying disk encryption policy rules, ensure you meet the following requirements and refer to these known limitations: 

 Requirement / Limitation 

 Windows 

 Mac 

 Endpoint Prerequisites 

 The endpoint must be running a Microsoft Windows version that supports BitLocker. 

 The endpoint must be within the organization's network domain. 

 The endpoint must be running a Cortex XDR agent 7.1 or later. 

 To allow the agent to encrypt the endpoint, Trusted Platform Module (TPM) must be supported and enabled on the endpoint. 

 Active Directory Domain Services is required for recovery key backup. 

 The endpoint must be running a macOS version that supports FileVault. 

 The endpoint must be running a Cortex XDR agent 7.2 or later. 

 Disk Encryption Scope 

 You can enforce XDR disk encryption policy rules only on the Operating System volume. 

 You can enforce XDR disk encryption policy rules only on the Operating System volume. 

 The Cortex XDR Disk Encryption profile for Mac can encrypt the endpoint disk, however, it cannot decrypt it. After you disable the Cortex XDR policy rule on the endpoint, you can decrypt the endpoint manually. 

 Other 

 Group Policy configuration: 

 Make sure the GPO configuration applying to the endpoint enables Save BitLocker recovery information to AD DS for operating system drives . 

 Make sure your Cortex XDR disk encryption policy does not conflict with the GPO configuration to Choose drive encryption method and cipher strength . 

 Provide a FileVaultMaster certificate / institutional recovery key (IRK) that is signed by a valid authority. 

 It can take the agent up to 5 minutes to report the disk encryption status to Cortex XDR if the endpoint was encrypted through Cortex XDR, and up to one hour if it was encrypted through another MDM. 

 In line with the operating system requirements, the Cortex XDR encryption profile will take place on the endpoint after the user logs off and back on, and approves the prompt to enable the endpoint encryption. 

 Palo Alto Networksrecommends that you do not apply an encryption enforcement from another MDM on the endpoint together with the Cortex XDR encryption profile. 

 Follow this high-level workflow to deploy the Cortex XDR disk encryption in your network: 

 Monitor the endpoint encryption status 

 You can monitor the Encryption Status of an endpoint in the Endpoints → Disk Encryption Visibility table. For each endpoint, the table lists both system and custom drives that were encrypted. 

 The following table describes both the default and additional optional fields that you can view in the Disk Encryption Visibility table per endpoint. The fields are in alphabetical order. 

 Field 

 Description 

 Encryption Status 

 The endpoint encryption status can be: 

 Applying Policy: Indicates that the Cortex XDR disk encryption policy is in the process of being applied on the endpoint. 

 Compliant: Indicates that the Cortex XDR agent encryption status on the endpoint is compliant with the Cortex XDR disk encryption policy. 

 Not Compliant: Indicates that the Cortex XDR agent encryption status on the endpoint is not compliant with the Cortex XDR disk encryption policy. 

 Not Configured: Indicates that no disk encryption rules are configured on the endpoint. 

 Not Supported: Indicates that the operating system running on the endpoint is not supported by Cortex XDR. 

 Unmanaged: Indicates that the endpoint encryption is not managed by Cortex XDR. 

 Endpoint ID 

 Unique ID assigned by Cortex XDR that identifies the endpoint. 

 Endpoint Name 

 Hostname of the endpoint. 

 Endpoint Status 

 Status of the endpoint, for more information, see Manage endpoints . 

 IP Address 

 Last known IPv4 or IPv6 address of the endpoint. 

 Last Reported 

 Date and time of the last change in the agent’s status, for more information, see Manage endpoints . 

 MAC Address 

 MAC address of the endpoint. 

 Operating System 

 Platform running on the endpoint. 

 OS Version 

 Name of the operating system version running on the endpoint. 

 Volume Status 

 Lists all the disks on the endpoint along with the status per volume, Decrypted or Encrypted . For Windows endpoints, Cortex XDR includes the encryption method. 

 You can also monitor the endpoint Encryption Status in your Endpoint Administration table. 

 Configure a disk encryption profile 

 Under Endpoints → Policy Management → Extensions → Profiles , select + New Profile or Import from File . Choose the Platform and select Disk Encryption . Click Next . 

 Fill-in the general information for the new profile. 

 Assign a name and an optional description to the profile. 

 Enable disk encryption. 

 To enable the Cortex XDR agent to apply disk encryption rules using the operating system disk encryption capabilities, Enable the Use disk encryption option. 

 Configure Encryption details . 

 For Windows: 

 Encrypt or decrypt the system drives. 

 Encrypt the entire disk or only the used disk space. 

 For Mac: 

 Inline with the operating system requirements, when the Cortex XDR agent attempts to enforce an encryption profile on an endpoint, the endpoint user is required to enter the login password. Limit the number of login attempts to one or three. Otherwise, if you do not force log in attempts, the user can continuously dismiss the operating system pop-up and the Cortex XDR agent will never encrypt the endpoint. 

 (Windows only) Specify the Encryption methods per operating system. 

 For each operating system (Windows 7, Windows 8-10, Windows 10 (1511), and above), select the encryption method from the corresponding list. 

 Note 

 You must select the same encryption method configured by the Microsoft Windows Group Policy in your organization for the target endpoints. Otherwise, if you select a different encryption method than the one already applied through the Windows Group Policy, Cortex XDR displays errors. 

 (Mac only) Upload the FileVaultMaster certificate. 

 To enable the Cortex XDR agent to encrypt your endpoint, or to help users who forgot their password to decrypt the endpoint, you must upload to Cortex XDR the FileVaultMaster certificate / institutional recovery key (IRK). You must ensure the key is signed by a valid authority and upload a CER file only. 

 Save your profile. 

 When you’re done, Create your disk encryption profile. 

 Apply disk encryption profile to your endpoints . 

 Apply disk encryption profile to your endpoints 

 After you define the required disk encryption profiles, configure Protection Policies and enforce them on your endpoints. Cortex XDR applies Protection policies on endpoints from top to bottom, as you’ve ordered them on the page. The first policy that matches the endpoint is applied. If no policies match, the default policy that enables all communication to and from the endpoint is applied. 

 Under Endpoints → Policy Management → Extensions → Policy Rules , select +New policy or Import from File . 

 Note 

 When importing a policy, select whether to enable the associated policy targets. Rules within the imported policy are managed as follows: 

 New rules are added to the top of the list. 

 Default rules override the default rule in the target tenant. 

 Rules without a defined target are disabled until the target is specified. 

 Configure settings for the disk encryption policy. 

 Assign a policy name and optional description. 

 The platform will automatically be assigned to Windows. 

 Assign the disk encryption profile you want to use in this rule. 

 Click Next . 

 Select the target endpoints on which to enforce the policy. 

 Use filters or manual endpoint selection to define the exact target endpoints of the policy rules. If exists, the Group Name is filtered according to the groups within your defined user scope. 

 Click Done . 

 Alternatively, you can associate the disk encryption profile with an existing policy. Right-click the policy and select Edit . Select the Disk Encryption profile and click Next . If needed, you can edit other settings in the rule, such as target endpoints and description. When you’re done, click Done . 

 Configure policy hierarchy. 

 Drag and drop the policies in the desired order of execution. 

 Save the policy hierarchy. 

 After the policy is saved and applied to the agents, Cortex XDR enforces the disk encryption policies on your environment. 

 Select one or more policies, right-click and select Export Policies . You can choose to include the associated Policy Targets , Global Exceptions , and endpoint groups. 

 Monitor the endpoint encryption status . 

 Previous Host firewall for macOS 

 Next Host Inventory 

 Last updated 1 month ago 

 Was this helpful?
