---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-service-provider-csp-onboarding/pending-cloud-instances
fetched_at: 2026-09-16T08:26:19Z
source: cortex-platform
---

# Pending cloud instances | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Cloud service provider (CSP) onboarding 

 Cortex XSIAM Data Ingestion 

 Pending cloud instances 

 Review pending cloud instances in Cortex XSIAM. 

 In Cortex XSIAM, a pending cloud instance refers to a cloud instance created after Cortex Cloud generates an authentication template, but before that template has been fully executed within the Cloud Service Provider (CSP) environment. 

 A pending cloud instance is created each time you complete the onboarding wizard for a new CSP and click Save . You can view all cloud instances, including those in a pending state, by navigating to Cloud Instances . Ensure you remove any default filters that might exclude instances with a "pending" status. 

 A single pending instance can be leveraged to create multiple cloud instances, all sharing the same configurations defined during the cloud onboarding process. Pending instances are automatically deleted after 30 days. 

 Manage pending cloud instances 

 There are some actions that can be performed specifically on cloud instances with a status of "pending". 

 Action 

 Instructions 

 Manually connect an instance 

 After the authentication template has been executed in the CSP, you can manually connect the Cortex Cloud cloud instance to the CSP by right-clicking the pending cloud instance and selecting Manually connect an instance . For more about this process, see Manually connect a cloud instance . 

 View Details 

 To review the configuration settings defined in the onboarding wizard for a pending instance, right-click the instance and select View Details . This is helps you distinguish between pending instances when you want to create a new cloud instance from an existing pending instance or when you want to manually connect an instance. 

 Re-download Connection Template 

 The authentication template that you download from the onboarding wizard is valid for seven days from when it was downloaded. If you want to create a new cloud instance from a pending instance after the authentication template has expired, you can right-click the pending instance and select Re-download Connection Template . You must then execute the template in the CSP. 

 Delete 

 To delete a pending instance, right-click the pending instance and select Delete . 

 Previous Manage cloud instances 

 Next Edit your onboarded CSP configuration 

 Last updated 12 days ago 

 Was this helpful?
