---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/identity-access-management/appsec-cicd-185
fetched_at: 2026-09-16T09:11:10Z
source: cortex-platform
---

# Any organization member can create private repositories | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Identity Access Management 

 Any organization member can create private repositories 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_185 

 Category 

 IAM 

 Severity 

 LOW 

 Impact 

 All members of an organization have privileges to create private repositories. If a member's account or access token is compromised, a malicious actor could create such a repository and access all of the organization's secrets scoped to private and internal repositories. For example, if the scope of a GitHub organization secret is not limited to specific repositories, any member of the organization can create an private repository and configure a GitHub Actions workflow to retrieve the secret. 

 Recommended Solution - Buildtime 

 Disable the excessive permissions granted to all organization members to create private repositories. 

 To disable internal repository creation refer to https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/restricting-repository-creation-in-your-organization. 

 If the above mitigation is not possible, or in addition to it, it’s important to scope organization secrets to specific repositories and grant permission on a need-to-access basis only, following the principle of least privileges. 

 To change the scope of a GitHub organization secret: 

 Browse to the Settings tab of your GitHub organization’s repository where the secret is located. 

 Click on the Secrets menu located in the left-hand side of the page. 

 Select the required secret and click on its name to open the details page. 

 Click on the Edit button on the top right-hand corner of the page. 

 Under Repository access , select the repositories that should have access to the secret. 

 Click on the Update secret button to save the changes. 

 Ask Copy 

 For more information refer to https://docs.github.com/en/enterprise-cloud@latest/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-an-organization. 

 Previous Any organization member can create internal repositories 

 Next Default branch does not require signed commits 

 Last updated 1 month ago 

 Was this helpful?
