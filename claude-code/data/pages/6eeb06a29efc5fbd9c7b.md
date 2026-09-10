---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/serverless-function-posture-security/serverless-function-posture-rules/create-a-configuration-rule-for-serverless-functions
fetched_at: 2026-09-06T10:08:17Z
source: cortex-platform
---

# Create a configuration rule for serverless functions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Serverless function posture security 

 Serverless function posture rules 

 Cortex Cloud Posture 

 Create a configuration rule for serverless functions 

 Create Cortex Cloud Posture Management rules that detect serverless function configuration risks. 

 Config rules for serverless functions identify security misconfigurations within the settings and deployment infrastructure of your individual serverless resources. 

 Under Posture Management , select Rules & Policies → Cloud Security (under Rules) → click Create Rule . 

 Select Config . 

 On the Overview step of the Create Config Rule wizard. 

 Fill in these fields: 

 Rule Name : (required): A user-provided to identify the rule 

 Description (required): A description of the rule 

 Severity (required): Select the severity level. Only findings with this exact severity level will trigger this rule. Findings with different severity levels will be ignored 

 Labels : (optional): Assign labels to categorize and organize the rule based on specific criteria or attributes. Labels help in easily identifying and filtering rules 

 Enable How to Fix : (Default: ON): Enable to take action when the rule is violated 

 Click Next. 

 Define the logic for the configuration rule on the Rule Logic step of the wizard in the query editor. 

 Under the Value menu in the Find field: 

 Select Compute . 

 Select the relevant serverless function from the list that is displayed. Options: Lambda Function , Google Cloud Function , Azure Cloud Function . 

 The JSON configuration file for the selected serverless function is displayed. Note that each type of serverless function has a unique configuration file and unique properties. 

 Select a property or multiple properties of the serverless function configuration file and provide a value. 

 Click Search. 

 All assets matching the search criteria are displayed. This allows you to validate the rule's effectiveness on existing functions and provides valuable context for refining the rule's logic to accurately identify future functions. 

 Click Next if you have enabled a fix in step 1a above, or Done if fix is disabled. 

 Define the fix in the How to Fix step (when enabled in step 1a above), and click Done. 

 Previous Create an attack path rule for serverless functions 

 Next Create a network exposure rule for serverless functions 

 Last updated 2 months ago 

 Was this helpful?
