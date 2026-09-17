---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security
fetched_at: 2026-09-16T08:48:41Z
source: cortex-platform
---

# Cortex CLI for Code Security | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cortex CLI 

 Cortex Cloud Posture 

 Cortex CLI for Code Security 

 Use Cortex CLI with Cortex Cloud Posture Management to scan code for security risks. 

 Cortex CLI for Code Security scans allow developers and security teams to integrate security checks directly into their application development workflows. 

 The Code Security CLI supports the following scan types: 

 Secrets : Identifies exposed sensitive secrets within your codebase 

 Infrastructure-as-Code (IaC): Analyzes infrastructure configuration files to detect potential security misconfigurations 

 Software Composition Analysis (SCA): Performs vulnerability detection in third-party dependencies, detects malicious packages, assesses their license compliance and their package operational risk 

 In addition, the Code Security CLI serves as the integration mechanism for security scanning within supported CI tools such as Jenkins, GitHub Actions, and others. This is achieved by adding a code snippet containing the CLI command into the configuration files of your CI tool when integrating the CI tool with Cortex Cloud. It acts as a wrapper, enabling security scanning within your pipelines, and direct upload of results to the platform. 

 Code Security CLI scan behavior and output 

 Scans generate assets (see Code and CI/CD assets , issues , and findings ) 

 If one scanner (such as Secrets) fails, the other scanners will continue to run and produce results 

 Scan failures trigger an error message indicating the scanner that failed 

 The Code Security CLI provides these output modes for management and viewing of scan results: 

 Upload to platform : --upload-mode = upload (default). Uploads scan results directly to the platform for centralized analysis and management 

 Upload findings only . --upload-mode = no-code . Upload findings, but without including the actual source code content. This prevents raw source code from leaving your local environment or being stored on the platform 

 CLI output only : --upload-mode=no-upload . View scan results directly in your command-line interface without being uploaded to the platform 

 For more information about the output flags, refer to Cortex CLI Cortex Cloud Application Security command line reference . 

 Supported outputs 

 The CLI supports the following outputs: 

 json 

 spdx 

 cli 

 junitxml 

 sarif 

 cyclonedx 

 cyclonedx_json 

 Authentication 

 To authenticate the Code Security CLI, choose one of the following methods: 

 Local developer workflows : Run manual, ad-hoc scans on your local machine to catch vulnerabilities and misconfigurations before committing code to your version control system 

 The following flags are required to authenticate the Code Security CLI: 

 --api-base-url [ $CORTEX_API_BASE_URL ] 

 --api-key [ $CORTEX_API_KEY ] 

 --api-key-id [ $CORTEX_API_KEY_ID ] 

 For more information about these flags, refer to Cortex CLI common command line reference guide . 

 Using a cortex.env file : Place your authentication details in a cortex.env file. You can download this file from the UI 

 CI/CD pipeline automation : The Application Security CLI serves as the core integration mechanism for security scanning within your automated pipelines. By inserting simple code snippets into CI tools like Jenkins, GitHub Actions, CircleCI, or GitLab Runner, the CLI acts as a wrapper to enforce security guardrails dynamically and block risky deployments 

 Requirements 

 For the Cortex CLI binary : 

 Install Node.js v22 on the host machine before running scans. The Cortex CLI requires Node.js for JavaScript analysis 

 Check the installed version with node -v 

 Download Node.js from the official Node.js site. 

 On Linux systems, install GLIBC (GNU C Library) version 2.35 or later. This does not apply when using the CLI container image 

 Permissions : Ensure you have the required user permissions. Refer to About Cortex CLI 

 Onboard and install the Cortex CLI : Refer to Connect Cortex CLI 

 Configure proxy for the Code Security CLI 

 When operating the Code Security CLI within environments requiring internet access via a proxy server, you can configure the tool to route its traffic through your proxy using standard environment variables. For proxies that perform TLS inspection, you must also specify a CA certificate 

 Environment variables : Set HTTP_PROXY and HTTPS_PROXY (or http_proxy and https_proxy ) to your proxy address 

 CA Certificate : Use the --ca-certificate flag or the $CORTEX_CA_CERTIFICATE environment variable to provide your CA certificate for proxies that perform TLS inspection. The flag is now global and must appear before code scan . It is currently limited to the Application Security CLI. You can either: 

 Previous Cortex CLI common command line reference guide 

 Next Cortex CLI usage for Cortex Cloud Application Security 

 Last updated 21 days ago 

 Was this helpful?
