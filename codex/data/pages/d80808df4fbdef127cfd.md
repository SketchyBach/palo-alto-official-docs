---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/tenant-console-workflow
fetched_at: 2026-09-16T08:49:01Z
source: cortex-platform
---

# Configure the Generic 3rd Party AppSec Collector | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 Onboard data sources 

 Ingest third-party data sources 

 Generic 3rd Party AppSec Collector 

 Configure the Generic 3rd Party AppSec Collector 

 The Collector can be managed through the tenant for the full collector lifecycle, creation, credential generation, SARIF validation, editing, and deletion. Finding upload is performed exclusively through the API workflow. 

 Prerequisites 

 Fulfill the prerequisites stated in Generic 3rd Party AppSec Collector . 

 Onboarding steps 

 Step 1: Navigate to data sources 

 Navigate to Settings → Data Sources & Integrations . 

 Filter by Name = 3rd Party AppSec Collector . 

 The Collector instances page displays all existing 3rd Party AppSec Collector instances. 

 Step 2: Create a collector 

 The collector creation wizard has three sequential steps. 

 Step 2a: Configure a collector 

 Define the collector identity and configuration. 

 Select + Add New or select Add Another Instance if a collector is displayed. 

 Enter a Collector Name (required). Set the collector name to match the tool.driver.name field from the SARIF file for consistent identification across the platform. 

 Note: The collector name is the primary identifier for the collector instance. Use a descriptive name that identifies the third-party tool. 

 Select Generate API key . 

 Step 2b: Generate an API key 

 Copy the generated API credentials for use in the upload workflow. 

 Review the success message confirming the collector was created. 

 Copy the Token ID (first credential value), used as the x-crtx-auth-id header. 

 Copy the API Token (second credential value), used as the Authorization header. 

 Select Copy API URL to copy the collector-specific upload endpoint. 

 Optionally select View Examples to display cURL and Python upload examples. 

 Select Next . 

 Important 

 The Token ID and API Token are displayed only once. Copy and store the credentials securely before proceeding. If the credentials are lost, edit the collector to regenerate the credentials. 

 Step 2c: Validate the file format (optional) 

 Validate a SARIF file to verify the format before production use. 

 Upload a SARIF file using the file input. 

 Review the validation result. Values : Valid, Partially Valid, and Invalid. For definitions of each status, see Reference E: Validation statuses . 

 Select Done to complete the collector creation. 

 Validate a SARIF file (post-creation) 

 Validate a SARIF file against an existing collector instance without uploading findings. 

 Navigate to Settings → Data Sources → 3rd Party AppSec Collector . 

 Select the Test action for the collector instance. 

 Upload a SARIF file using the file input. 

 Review the validation result ( VALID , PARTIALLY VALID , or INVALID ). The validation panel displays the status and any issues detected. 

 Previous Generic 3rd Party AppSec Collector 

 Next Upload findings from CI/CD pipelines 

 Last updated 19 days ago 

 Was this helpful?
