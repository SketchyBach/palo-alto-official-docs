---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/ai-access-security/administration/discover-risks-posed-by-genai-apps/discover-risks-posed-by-genai-apps-by-use-case.html
fetched_at: 2026-09-16T12:45:56Z
source: palo-alto-main
---

# Discover Risks Posed by GenAI Apps by Use Case Clear

Updated on 

 Wed Sep 09 11:26:17 PDT 2026 

 Focus 

 Home 

 AI Access Security 

 Administration 

 Discover Risks Posed by GenAI Apps 

 Discover Risks Posed by GenAI Apps by Use Case 

 Download PDF 

 AI Access Security 

 Discover Risks Posed by GenAI Apps by Use Case 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 AI Access Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Discover Risks Posed by GenAI Apps by Use Case 

 Discover risks posed by generative AI (GenAI) apps based on the GenAI app use
 case. 

 Review the Supported Use Cases for full descriptions of all use
 case categories that a GenAI app falls into. 

 Log in to 
 Strata Cloud Manager . 

 Select Insights AI Access to view the AI Access Security Insights
 dashboard. 

 The AI Access Security Insights dashboard displays GenAI app usage
 on your network by use case by default as well as the following high-level
 information about your top GenAI use cases: 

 Time Filter 

 Filter your GenAI use case breakdown for the time period you want to
 investigate. You can select Past 1 Hour ,
 Past 3 Hours , Past 24
 Hours , Past 7 Days , or
 Past 30 Days . 

 Threats Detected 

 Threats are detected by the Vulnerability Protection
 profile attached to the Web Security policy rule. This
 profile detects threats such as malicious and phishing URLs,
 malicious files, or malware. The Threats
 Detected summarizes all threats across all GenAI
 apps and enforcement points. 

 Alerted —Total number of threats
 detected that generated an alert. 

 Blocked —Total number of threats
 detected that were blocked by your NGFW or
 Prisma Access tenants. 

 Sensitive Data Assets 

 Sensitive data assets displays the number of incidents of sensitive
 data detected when traffic matches the match criteria in your Enterprise Data Loss Prevention (E-DLP) 
 data profile for data at rest ( Data Security ) and data in motion ( SaaS Security Inline ). 

 Data at Rest —Total number of DLP Incidents that
 either generated an alert or were blocked through the SaaS
 API ( Data Security ) enforcement channel. 

 Data in Motion —Total number of DLP Incidents that
 either generated an alert or were blocked through the SaaS Security Inline enforcement channel. 

 Alerted —Total number of DLP Incidents that
 generated an alert for both data at rest and data in motion.

 Blocked —Total number of DLP incidents 
 blocked by your NGFW s or Prisma Access 
 tenants for both data at rest and data in motion. 

 Top Use Cases 

 The AI Access Security Insights dashboard dynamically
 displays the top four GenAI app use cases based on activity on your
 network, along with the total number of GenAI apps and users who
 accessed any GenAI in the selected time period. This allows you to
 quickly investigate security incidents related to your most widely
 used GenAI apps and implement access control policy rules. 

 GenAI Apps —Total number of GenAI apps
 that fall into the particular use case. The total number of
 GenAI apps are categorized into three groups—Sanctioned,
 Tolerated, and Unsanctioned GenAI apps. 

 Unique GenAI Users —Total number of
 users who accessed any GenAI app that falls into the
 particular use case. Click the Unique GenAI
 Users count to view a list of each unique
 user who was blocked from accessing the GenAI app 

 AI Access Security automatically aggregates
 the total Unique GenAI Users 
 count on a set interval and generates the user list
 immediately when you click on the Unique
 GenAI Users count. This might cause the
 Unique GenAI Users count to
 slightly differ from the list count. 

 All Other Use Cases 

 Applications —Total number of GenAI
 apps that fall into any other GenAI app use case. The total
 number of GenAI apps are categorized into three
 groups—Sanctioned, Tolerated, and Unsanctioned GenAI
 apps. 

 Users —Total number of users who have
 accessed any GenAI app that falls into any other GenAI app
 use case. 

 Hover your mouse over each of the use cases to see summary
 information about GenAI app usage associated with the use case. 

 Review use case to see a detailed breakdown of all
 Sanctioned, Tolerated, and Unsanctioned GenAI apps in the use case you're
 interested in. 

 Review the use case details page to understand GenAI app usage. 

 The use case details page provides granular data about the GenAI app usage.
 You can use this information to understand GenAI app usage to help inform
 you of what policy rules your security administrators need to write to
 strengthen your security posture. This ensures that your organization is
 safely adopting GenAI apps and to prevent exfiltration of sensitive
 data. 

 Use Case Summary 

 The use case summary aggregates all important GenAI app usage
 information for the use case you're investigating. 

 Most Used Applications —The most used GenAI app for the
 use case. This also includes the app tag
 ( Sanctioned ,
 Tolerated , or
 Unsanctioned ) currently assigned
 to the GenAI app. 

 Application Breakdown —Summary of the
 total number of GenAI apps associated with the use case as
 well as a summary of the app tags 
 across all detected GenAI apps. 

 User Breakdown —Summary of the total
 number of users who accessed any of the GenAI apps
 associated with the use case. A summary of how many users
 accessed Sanctioned ,
 Tolerated , or
 Unsanctioned GenAI apps is also
 provided. 

 Applications 

 A list of all GenAI apps associated with the use case accessed by
 your users. You can apply a Sort By filter to
 the use case GenAI apps to sort them by User
 Count , Threats Count ,
 Transferred Count . AI Access Security sorts GenAI apps from highest to
 lowest count. 

 The apps list displays the following information about each GenAI app
 detected. 

 Application Name —Name of the detected
 GenAI app. Click the app name to view detailed usage
 information . You're redirected to the Activity
 Insights Applications 

 Tag —Current GenAI app tag . You can apply a new tag by
 clicking the tag you want to apply. 

 Palo Alto Networks groups the child App-IDs for app
 functionality in a container App-ID. However, tagging an
 App-ID container isn’t supported. You must individually
 tag the specific child App-ID that are sanctioned,
 unsanctioned, or tolerated within your organization. 

 Allowed Users —Total number of unique users who
 accessed the GenAI app based on the access privileges
 configured in your Security policy rules. Click the
 Allowed Users count to view a
 list of each unique user who successfully accessed the GenAI
 app. 

 Blocked Users —Total number of unique users blocked
 from accessing the GenAI app based on the access privileges
 configured in your Security policy rules. Click the
 Blockers Users count to view a
 list of each unique user blocked from accessing the GenAI
 app. 

 Threats —Total number of detected threat
 activity . 

 Transferred —Total amount of data in
 gigabyte (GB) uploaded to or downloaded from the GenAI
 app. 

 Sensitive Asset —Number of DLP incidents 
 generated due to sensitive data detected and blocked by Enterprise DLP . 

 Enterprise Available —Indicates whether
 the GenAI app offers an enterprise plan or license
 schema. 

 Data Used in ML —Indicates whether the
 GenAI app uses user-uploaded data for training purposes. 

 Risk Score — Risk score of the
 GenAI app. 

 Use Case Highlights 

 Applications —Total number of GenAI
 apps that fall into any other GenAI app use case. The total
 number of GenAI apps are categorized into three
 groups—Sanctioned, Tolerated, and Unsanctioned GenAI
 apps. 

 Users —Total number of users who have
 accessed any GenAI app that falls into any other GenAI app
 use case. 

 Create a custom Security policy rule 
 to control access to a GenAI app. 

 In the example above, Openai-Base is the most
 used GenAI app in the Code Assistant &
 Generator use case. Additionally, this is an
 Unsanctioned app and indicates this an app not
 approved for use on your corporate network. 

 In this case, you can modify the default GenAI app access policy
 rule to explicitly block all access to
 OpenAI if this is an app your organization
 should not access.
