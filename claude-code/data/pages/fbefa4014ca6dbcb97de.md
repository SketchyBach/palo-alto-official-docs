---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-saas-security/connect-a-saas-application/onboard-gainsight-px
fetched_at: 2026-09-16T08:36:47Z
source: cortex-platform
---

# Onboard Gainsight PX | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Cloud Security 

 Cortex Cloud SaaS Security 

 Connect a SaaS application 

 Cortex XSIAM 

 Onboard Gainsight PX 

 Connect a Gainsight PX instance in Cortex XSIAM to detect posture risks and compliance violations. 

 For SaaS Security to detect posture risks in your Gainsight PX instance, you must onboard your Gainsight PX instance to SaaS Security. Through the onboarding process, SaaS Security logs in to Gainsight PX using administrator account credentials. SaaS Security uses this account to scan your Gainsight PX instance for misconfigured settings. If there are misconfigured settings, SaaS Security suggests a remediation action based on best practices. 

 To onboard your Gainsight PX instance, complete the following actions: 

 Collect information for connecting to your Gainsight PX instance 

 Connect SaaS Security to your Gainsight PX instance 

 Step 1: Collect Information for Connecting to Your Gainsight PX Instance 

 To access your Gainsight PX instance, SaaS Security requires the following information, which you specify during the onboarding process. 

 Item 

 Description 

 Email ID 

 The login email address of a Gainsight PX administrator account. 

 Password 

 The password of the Gainsight PX administrator account. 

 Subscription ID 

 A unique identifier for your Gainsight PX subscription. 

 As you complete the following steps, make note of the values of the items described in the preceding table. You will need to enter these values during onboarding to access your Gainsight PX instance from SaaS Security. 

 Identify the Gainsight PX administrator account that SaaS Security will use to access your Gainsight PX instance. 

 Required Permissions: To enable SaaS Security to scan your Gainsight PX instance, the account must have administrator access. 

 Identify your Gainsight PX subscription ID. 

 Open a web browser to the Gainsight PX login page at app.aptrinsic.com/authentication/login and log in as an administrator. 

 In the left navigation pane, select Administration > SET UP > Company & Timezone. 

 Copy the subscription ID and paste it into a text file. 

 Note : Do not continue to the next step unless you have copied the subscription ID. You must provide this identifier to SaaS Security during the onboarding process. 

 Step 2: Connect SaaS Security to Your Gainsight PX Instance 

 By adding a Gainsight PX app in Cortex, you enable SaaS Security to connect to your Gainsight PX instance. 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the app you want to connect to. 

 Click the Gainsight PX tile. 

 Under Capabilities , Enter a Name for your application. 

 Select Security Posture under Default Capabilities and click Next. 

 Under Connections , enter the administrator login credentials and the subscription ID. 

 Under Configurations , select a Sync Interval . Choose a meaningful Tag to distinguish between various applications in different environments. 

 Click Next to complete the onboarding validation process. 

 Previous Onboard Datadog 

 Next Onboard Grammarly 

 Last updated 2 days ago 

 Was this helpful?
