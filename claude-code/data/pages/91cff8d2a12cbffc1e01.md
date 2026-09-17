---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/integrate-ci-tools/circleci-for-code-scans
fetched_at: 2026-09-16T08:48:58Z
source: cortex-platform
---

# CircleCI for code scans | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 Onboard data sources 

 Integrate CI tools 

 CircleCI for code scans 

 Integrate Cortex Cloud Application Security with your CircleCI system to allow dynamic, automated, and context-specific code scans across your codebase. This integration provides continuous scanning of your workflows, triggered by code changes or pipeline events, ensuring security checks are performed and issues are detected as early as possible. 

 Code scans are executed using the Cortex CLI, and include automated shift-left actions based on scan results. 

 Note 

 CircleCI onboarding offers both code and CI/CD scanning. A single integrated instance supports either code or CI scanning, but not both. If you require both code and CI scanning for your CircleCi environment, you must create two separate integrations, selecting the appropriate scanning type for each. To onboard CircleCI for CI/CD scans, refer to CircleCI for CI/CD pipeline scans . 

 Prerequisites 

 Before you begin: 

 User permissions : Ensure the user performing the integration has permissions to edit pipeline configurations (such as YAML files) and manage secrets/credentials within the CI platform to store the Cortex Cloud API key securely 

 Onboarding steps 

 On the Cortex Cloud console: 

 Navigate to Settings → Data Sources & Integrations → + Add New . 

 Enter CircleCI in the search bar → Hover over the displayed search result → Connect .Search for and hover over CircleCI and click Add , or Add Another Instance if an instance is already onboarded. 

 On the Select Integration step of the CircleCI integration wizard, select Code Scan → Next . 

 On the Add Environment Variables step of the wizard. 

 Select Generate API key. 

 The API key secret and API key ID values are generated and populate their respective fields. 

 Select your system architecture. 

 Click Next. 

 Create a context in CircleCI and name it cortex-secrets . 

 Important 

 The cortex-secrets naming convention for the context is mandatory to ensure functionality and must not be changed. 

 Store your Cortex Cloud API Key and API ID within the cortex-secrets context. 

 If you have an API key: 

 Copy the CORTEX_API_KEY and CORTEX_API_KEY_ID variable names from their respective fields in the wizard. 

 Add the CORTEX_API_KEY and CORTEX_API_KEY_ID and their corresponding values as separate environment variables (secrets) to the cortex-secrets context. 

 If you do not have an API key: 

 Click Generate API key → Copy the CORTEX_API_KEY and CORTEX_API_KEY_ID and their corresponding values from their respective fields . 

 Add the CORTEX_API_KEY and CORTEX_API_KEY_ID and their corresponding values as separate environment variables to the cortex-secrets context. 

 Note 

 Do not change the names of the environment variables provided by Cortex Cloud. They are required for proper integration and functionality. 

 For more information on context in CircleCI, refer to Using contexts in CircleCI . 

 Copy and paste the pre-populated code from the Configure Job step of the integration wizard into your .circleci/config.yaml file, and click Done. 

 In your .circleci/config.yaml file: 

 Verify that the YAML file includes a Docker container image 

 Verify that the context is cortex-secrets 

 In the docker run command, replace --repo-id REPO_OWNER/REPO_NAME values with your repository owner and repository name 

 Check that the The integration will be created once CircleCI authorizes message is displayed in the final step of the wizard and click Done . 

 Verify integration 

 Verify integration and confirm that the your integrated CircleCI instance has a status of Connected . 

 On the Data Sources & Integrations page, search for CircleCI in the search bar. 

 Hover over and select the resulting entry. 

 Verify that the status of your CircleCI instance is Connected . 

 Next steps 

 View scan results and mitigate issues. 

 CircleCI code scan workflow template 

 Use the CircleCI code scan workflow template to configure Cortex CLI code scanning in your .circleci/config.yaml file. 

 Manage the integration 

 Instance-level actions 

 Navigate to Settings → Data Sources & Integrations and search for CircleCI . 

 Select the matching result. 

 Locate your instance from the displayed list. Right-click it, then select an option: 

 Edit instance : Opens the onboarding wizard, where you can change the instance configuration. 

 Delete instance : Deletes the instance and previous scan data. 

 Copy entire row : Copies all row values to the clipboard. 

 Repository-level actions 

 Right-click a connected repository to Set Scanned Branches , run a manual scan through Scan Repository , modify the Scan Configuration , or Remove Repository . In Scan Configuration , you can toggle scanners and manage pull request behavior. 

 Locate your instance. See Instance-level actions . 

 Select the instance. A list of connected repositories appears. 

 Right-click a repository, select the required action, then select Save . 

 Previous AWS CodeBuild code scan workflow template 

 Next CircleCI code scan workflow template 

 Last updated 1 month ago 

 Was this helpful?
