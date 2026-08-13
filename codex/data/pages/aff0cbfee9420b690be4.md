---
url: https://docs.paloaltonetworks.com/best-practices/10-1/best-practices-for-migrating-to-application-based-policy/best-practices-for-migrating-to-application-based-policy/migrate-to-application-based-policy-using-policy-optimizer/rules-to-begin-converting-after-30-days/convert-rules-with-the-most-traffic
fetched_at: 2026-08-13T15:32:10Z
source: palo-alto-main
---

# Convert Rules with the Most Traffic Clear

Convert Rules with the Most Traffic 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Best Practices for Migrating to Application-Based Policy 

 : 
 Convert Rules That See the Most Traffic 

 Updated on 

 Fri Jan 26 17:43:41 PST 2024 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Version 

 10.1 

 10.1 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 Best Practices for Migrating to Application-Based Policy 

 Safely Enable Applications Using a Phased Transition 

 Migrate a Port-Based Policy to PAN-OS Using Expedition 

 Migrate to Application-Based Policy Using Policy Optimizer 

 Convert Simple Rules with Well-Known Apps After One Week 

 Rules to Begin Converting After 30 Days 

 Remove Unused Rules 

 Convert the Most Stable Rules 

 Convert Internet Access Rules 

 Convert Rules That See the Most Traffic 

 Convert Rules with Few Apps Seen Over a Time Period 

 Next Steps to Adopt Security Best Practices 

 Updated on 

 Fri Jan 26 17:43:41 PST 2024 

 Focus 

 Home 

 Best Practices 

 Best Practices for Migrating to Application-Based Policy 

 Best Practices for Migrating to Application-Based Policy 

 Migrate to Application-Based Policy Using Policy Optimizer 

 Rules to Begin Converting After 30 Days 

 Convert Rules That See the Most Traffic 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Best Practices for Migrating to Application-Based Policy 

 Convert Rules That See the Most Traffic 

 Table of Contents 

 Filter

 Version 

 10.1 

 10.1 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 Best Practices for Migrating to Application-Based Policy 

 Safely Enable Applications Using a Phased Transition 

 Migrate a Port-Based Policy to PAN-OS Using Expedition 

 Migrate to Application-Based Policy Using Policy Optimizer 

 Convert Simple Rules with Well-Known Apps After One Week 

 Rules to Begin Converting After 30 Days 

 Remove Unused Rules 

 Convert the Most Stable Rules 

 Convert Internet Access Rules 

 Convert Rules That See the Most Traffic 

 Convert Rules with Few Apps Seen Over a Time Period 

 Next Steps to Adopt Security Best Practices 

 Convert Rules That See the Most Traffic 

 Convert legacy port-based security policy rules that
have seen the largest amount of traffic in bytes over the past 30
days to application-based rules. 

 Sorting for rules that have seen the most
traffic over the past 30 days ( Traffic (Bytes, 30 days) )
shows you the current most active rules. (A longer time frame places
can mislead you by emphasizing older rules that remain at the top
of the list because they have large cumulative totals, even if they
no longer see much traffic.) Converting these rules to App-ID based
rules safeguards the largest amount of traffic for your effort. 

 If
multiple rules see a lot of traffic, use the Policies Security Policy Optimizer No App Specified information to
help prioritize which rules to convert first. For example, you could
prioritize rules with the most Apps Seen (potentially
the riskiest rules) or rules the with most Days with
No New Apps and the oldest Modified date
(the most stable high-traffic rules). 

 In Policies Security Policy Optimizer No App Specfied , sort the rules
in descending order by Traffic (Bytes, 30 days) to
place the most recently active rules at the top of the list. 

 Select a rule to begin converting and click the number
of Apps Seen . 

 In the Applications & Usage dialog,
sort and filter the Apps Seen on the rule
to determine how to handle the applications. 

 Sort or filter by application subcategory to group applications
that may require similar treatment and can be controlled in one
application-based rule. Sort on Traffic (30 days) to
see the amount of recent traffic on individual applications to prioritize
the currently most active applications. 

 Follow Step 4 through Step 7 in Convert Internet Access Rules to create
a cloned rule that controls each subcategory (or related subcategories)
of applications you want to treat similarly. 

 Previous 

 Convert Internet Access Rules 

 Next 

 Convert Rules with Few Apps Seen Over a Time Period 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
