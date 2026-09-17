---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.12/onboard-cortex-xsoar/post-deployment/configure-system-settings/configure-security-settings
fetched_at: 2026-09-16T08:53:51Z
source: cortex-platform
---

# Configure security settings | 8.12 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.12 

 Onboard Cortex XSOAR 

 Post deployment 

 Configure system settings 

 Cortex XSOAR 8.12 On-prem 

 Configure security settings 

 In Cortex XSOAR 8.12 On-prem, configure security settings for your deployment. 

 You can configure security settings such as how long users can be logged into Cortex XSOAR, and from which domains and IP ranges users can log in. 

 Go to Settings & Info → Settings → System → Security Settings . 

 Settings 

 Options 

 Description 

 Session Expiration 

 User Login Expiration 

 The number of hours (between 1 and 24) after which the user login session expires. You can also choose to automatically log users out after a specified period of inactivity. 

 Session Expiration 

 Dashboard Expiration 

 Whether the Dashboard page expires at the same time as the user login session or after seven days. This is useful when you view a dashboard on a separate screen. 

 For example, if you select seven days for dashboards and eight hours for login expiration and you are currently viewing the Dashboard page, the dashboard expiration takes priority (seven days). This ensures that the Dashboard page continues to display the widgets for an extended period. 

 Allowed Sessions 

 Approved Domains 

 The domains from which you want to allow user access (login) to Cortex XSOAR. You can add or remove domains as necessary. 

 Allowed Sessions 

 Approved IP Ranges 

 The IP ranges from which you want to allow user access (login) to Cortex XSOAR. You can also choose to limit API access from specific IP addresses. 

 User Expiration 

 Deactivate Inactive User 

 Deactivate an inactive user, and also set the user deactivation trigger period. By default, user expiration is disabled. When enabled, enter the number of days after which inactive users should be deactivated. 

 Allowed Domains 

 Domain Name 

 Enables you to specify one or more domain names that can be used in your distribution list for audit forwarding. 

 Previous Configure server settings 

 Next How to install Cortex XSOAR 

 Last updated 9 days ago 

 Was this helpful?
