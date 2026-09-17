---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/integrations/troubleshoot-integrations
fetched_at: 2026-09-16T08:46:23Z
source: cortex-platform
---

# Troubleshoot Integrations | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cortex Cloud Data Sources and Connectors 

 Administration and troubleshooting 

 Integrations 

 Troubleshoot Integrations 

 The Troubleshooting Instances dashboard provides you with insight into command execution errors. When troubleshooting integrations, we recommend the following steps: 

 Use the Test button in the integration instance. 

 Verify the integration settings. Check settings such as usernames, URLs, and passwords. 

 Download the debug log file and review its contents. 

 In the following example, you receive a 401 unauthorized error code after testing the integration. 

 integration-error.png 

 Click Run Test & Download Debug Log , to download the debug file locally. You can verify what server the URL request is being forwarded to and any other reasons as to why you received this error code. The 401 unauthorized error code usually relates to invalid error credentials, expired tokens, or incorrect API settings. 

 Enable verbose or debug-level logging on the integration. 

 Note 

 If an integration instance consistently encounters API rate limits when running on the tenant, consider configuring the instance to run on an engine to change the source of the outbound traffic. 

 If you are unable to fix the integration, contact Customer Support for further assistance. 

 Previous Configure integration permissions 

 Next Verify collector connectivity 

 Last updated 1 month ago 

 Was this helpful?
