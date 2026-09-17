---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/onboard-and-configure-cortex-xdr/post-deployment-steps/set-up-your-environment/configure-security-settings
fetched_at: 2026-09-16T08:43:52Z
source: cortex-platform
---

# Configure security settings | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Onboard and configure Cortex XDR 

 Post-deployment steps 

 Set up your environment 

 Cortex XDR 3.x 

 Configure security settings 

 Configure security settings such as session expiration, user login expiration, and dashboard expiration. 

 You can configure security settings such as how long users can be logged into Cortex XDR, and from which domains and IP ranges users can log in. 

 Go to Settings → Configurations → General → Security Settings . 

 Settings 

 Options 

 Description 

 Session Expiration 

 User Login Expiration 

 The number of hours (between 1 and 24) after which the user login session expires. You can also choose to automatically log users out after a specified period of inactivity. 

 Dashboard Expiration 

 Whether the Dashboard page expires at the same time as the user login session or after seven days. This is useful when you view a dashboard on a separate screen. 

 For example, if you select seven days for dashboards and eight hours for login expiration and you are currently viewing the Dashboard page, the dashboard expiration takes priority (seven days). This ensures that the Dashboard page continues to display the widgets for an extended period. 

 Note 

 Sessions are saved by browser. If you have both dashboard tabs and non-dashboard tabs open in the same browser, the session applies to all tabs. Consequently, if a non-dashboard tab expires based on the User Login Expiration setting, the Dashboard Expiration setting is overridden and the dashboard session ends. To ensure the dashboard remains open for the configured duration, open the dashboard in a separate browser or an incognito window. 

 Allowed Sessions 

 Approved Domains 

 The domains from which you want to allow user access (login) to Cortex XDR. You can add or remove domains as necessary. 

 Approved IP Ranges 

 The IP ranges from which you want to allow user access (login) to Cortex XDR. You can also choose to limit API access from specific IP addresses. 

 User Expiration 

 Deactivate Inactive User 

 Deactivate an inactive user, and also set the user deactivation trigger period. By default, user expiration is disabled. When enabled, enter the number of days after which inactive users should be deactivated. 

 Same-Site Cookie Policy 

 Strict
Lax 

 Configure your Cortex tenant's SameSite cookie security policy by selecting between two settings to control how users log in from external links: 

 Strict (Recommended): Requires users to reauthenticate when clicking a link from another site, even if they are already signed in. 

 Lax : Offers a more seamless experience by allowing users to access the tenant directly from external links without needing to log in again. Yet, we advise against this setting for security reasons. 

 Allowed Domains 

 Domain Name 

 The domain names that can be used in your distribution lists for reports. For example, when generating a report, ensure the reports are not sent to email addresses outside your organization. 

 Previous Configure server settings 

 Next Log forwarding 

 Last updated 20 days ago 

 Was this helpful?
