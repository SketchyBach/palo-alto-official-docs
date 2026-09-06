---
url: https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/governance-and-enforcement/cicd-policies/create-cicd-configuration-policies
fetched_at: 2026-09-06T10:12:49Z
source: cortex-platform
---

# Create CI/CD configuration policies | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Software supply chain security 

 Governance and enforcement 

 CI/CD Policies 

 Create CI/CD configuration policies 

 CI/CD configuration policies scan your CI/CD and Version Control System (VCS) environments to detect and enforce standards against misconfigurations and risky settings in pipelines, workflows and VCS systems (such as GitHub). 

 Prioritize risk with application context 

 By leveraging application context, you can create Scope-Based Access Control (SBAC) policies that align security enforcement with each application's purpose, business sensitivity, and lifecycle, ensuring targeted and effective risk management that allows you to focus efforts on high-impact issues and reduces noise. For more information about creating application-scoped policies, refer to Scope user access to applications (Application SBAC) . 

 Steps 

 Under Modules , select Application Security → AppSec Policies → + Add Policy . 

 On the General step of the policy creation wizard. 

 Select CI/CD Configuration Scanners as the policy type. 

 Provide a policy name (required) and description. 

 Click Next . 

 On the Conditions step of the wizard, define the conditions that apply to the policy. 

 By default, CI/CD Risk is selected as the Finding Type. 

 Click + to define CI/CD condition attributes. 

 Adding attributes allows you to narrow and refine findings, creating a tailored policy that targets the specific risk patterns you want to address. 

 You can also use the AND/OR options to build more precise logic: each AND bracket defines a set of conditions that must all be met, and multiple brackets can be combined with OR to evaluate different sets of conditions independently. 

 Refer to Reference A: CI/CD policy Condition attributes for more information about condition attributes. 

 Select Next . 

 On the Scope step of the wizard. Limit policy evaluation to relevant assets: 

 Asset types 

 Asset groups 

 Use Asset Types to limit policy evaluation to relevant assets. Select Asset Types → Add Filters → select an asset type → select or provide a value from the matching Value field. 

 For supported asset types and values, refer to Reference B:Scope Asset Types . 

 Select Asset Groups : 

 Select the asset groups on which this policy and its chosen detection rules will be evaluated. You can only select asset groups that are assigned to you as part of your scope. 

 The policy is evaluated only on the relevant assets within the selected group, based on the asset types defined in the category filter. 

 For more information about Cortex Cloud Application Security Asset Groups , refer to Scope user access to applications (Application SBAC) . 

 Click Next . 

 On the Triggers & Action step of the wizard. 

 Verify that Periodic Scan (required) is selected by default. 

 Note 

 Periodic scan is the only trigger that is supported for CI/CD policies. 

 Verify that Create an Issue (required) is selected by default) 

 (Optional): Select Override Severity to apply a severity level other than the default. 

 Click Next. 

 On the Summary step of the wizard: Review the policy settings and click Done. 

 This step provides an overview of the configured policy, including its name and description, the configured scope, and a table of conditions, triggers, and actions. It also displays the user who created the policy and the creation date. 

 You can view the custom policy that you created in the general policies table on the AppSec Policies page. 

 Next step: Investigate and remediate repository and pipeline 

 Investigate and remediate issues detected in your VCS configurations and CI/CD infrastructure to mitigate risks across your development lifecycle and delivery process. For more information, refer to CI/CD Risks . 

 Previous CI/CD policies inventory 

 Next Manage CI/CD policies 

 Last updated 25 days ago 

 Was this helpful?
