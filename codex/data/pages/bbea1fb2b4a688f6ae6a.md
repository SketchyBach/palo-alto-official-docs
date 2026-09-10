---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/alibaba-cloud-cloud-onboarding/prerequisites-for-onboarding-alibaba-cloud
fetched_at: 2026-09-06T10:03:31Z
source: cortex-platform
---

# Prerequisites for onboarding Alibaba Cloud | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 onboard and configure 

 Deployment steps and checklist 

 Cloud service provider (CSP) onboarding 

 Alibaba Cloud cloud onboarding 

 Cortex Cloud Posture 

 Prerequisites for onboarding Alibaba Cloud 

 Before you begin onboarding Alibaba Cloud, you must review the following prerequisites. 

 Permissions 

 Before you begin to onboard Alibaba Cloud to Cortex Cloud, ensure that you have the necessary permissions: 

 In Cortex Cloud, you must have a Cortex Cloud role with Data Sources - View & Edit permissions (to add/configure cloud accounts in Cortex Cloud). This role is included in the following built-in roles: Instance Administrator, Security Admin, and IT Admin. 

 In Alibaba Cloud, your credentials must have the necessary RAM permissions to deploy templates, manage roles and policies, as well as perform create and update operations for OIDC. 

 Additional prerequisites 

 Before you begin onboarding Alibaba Cloud, ensure that: 

 You have added an OIDC provider for Cortex Cloud in Alibaba Cloud. 

 You have the Alibaba Cloud account ID of the account you want to onboard. 

 You are logged into the Alibaba Cloud account. 

 If you are onboarding your first Alibaba Cloud account, you must first request manual provisioning of the cloud scanning environment. Open a customer support ticket to have the cloud scan environment created and ensure that the environment is ready for you to start onboarding. (Attempting to onboard Alibaba Cloud without first having the cloud scanning environment created will result in the following UI error: "No valid outpost scan env ALIBABA_CLOUD".) 

 Required RAM permissions in Alibaba Cloud 

 Before onboarding Alibaba Cloud to Cortex Cloud, ensure the user or role performing the onboarding has the necessary RAM permissions. 

 Required permissions for onboarding Alibaba Cloud account scope 

 Use the following template to create a custom policy with the permissions required for onboarding an Alibaba Cloud account to Cortex Cloud. The custom policy can be created in Alibaba Cloud RAM Console at Permissions → Policies → Create Policy → Script and attach the policy to the RAM user or role that will run the Terraform apply. 

 Ask Copy 

 { 
 " Version " : " 1 " , 
 " Statement " : [ 
 { 
 " Effect " : " Allow " , 
 " Action " : [ 
 " ram:CreateRole " , 
 " ram:GetRole " , 
 " ram:UpdateRole " , 
 " ram:DeleteRole " , 
 " ram:ListRoles " , 
 " ram:CreatePolicy " , 
 " ram:GetPolicy " , 
 " ram:GetPolicyVersion " , 
 " ram:DeletePolicy " , 
 " ram:ListPolicies " , 
 " ram:ListPolicyVersions " , 
 " ram:CreatePolicyVersion " , 
 " ram:DeletePolicyVersion " , 
 " ram:SetDefaultPolicyVersion " , 
 " ram:AttachPolicyToRole " , 
 " ram:DetachPolicyFromRole " , 
 " ram:ListPoliciesForRole " , 
 " sts:GetCallerIdentity " 
 ], 
 " Resource " : " * " 
 } 
 ] 
 } 

 Add Cortex Cloud as an OIDC provider in Alibaba Cloud 

 In order to establish trust between Cortex Cloud and Alibaba Cloud, you must add an OpenID Connect (OIDC) provider. If you already have an existing OIDC provider for accounts.google.com , you can add Cortex Cloud as an audience to the existing provider. Otherwise, create a new OIDC provider. 

 Add the audience to an existing OIDC provider 

 In Alibaba Cloud Console, navigate to RAM → Integrations → SSO . 

 In SSO , select the OIDC tab. 

 In the list of IdPs, identify the existing entry for GCP ( accounts.google.com ) and click it. 

 Under Client ID , click Add . 

 Enter alibaba-cortex-wif as the audience value for the new client ID and save the changes. 

 Enter alibaba-cortex-wif-<accountID> as the audience value for the new client ID where <accountID> corresponds to the Cortex Cloud Project ID. Save the changes. 

 Create a new OIDC provider 

 Before you begin, obtain the Cortex Cloud Project ID of your tenant by clicking on the User menu and then selecting About. 

 In Alibaba Cloud Console, navigate to RAM → Integrations → SSO . 

 In SSO , select the OIDC tab. 

 Click Create IdP . 

 In Create IdP , enter the IdP Name . For example, CortexGCPProvider . 

 In Issuer URL , enter the GCP IdP URL: https://accounts.google.com . 

 In Client ID , enter: alibaba-cortex-wif-<accountID> where <accountID> corresponds to the Cortex Cloud Project ID. 

 In Fingerprint , click Auto-add to automatically retrieve and add the signing certificate fingerprint for accounts.google.com . 

 (cn-hongkong accounts only) In Fingerprint , click Add and enter the following SHA1 fingerprint: 932bed339aa69212c89375b79304b475490b89a0 . 

 Click Add Fingerprint . 

 Save the changes. 

 Previous Onboard Alibaba Cloud 

 Next How to onboard Alibaba Cloud 

 Last updated 6 days ago 

 Was this helpful?
