---
url: https://docs.paloaltonetworks.com/best-practices/internet-gateway-best-practices/best-practice-internet-gateway-security-policy/define-the-initial-internet-gateway-security-policy/step-4-create-the-temporary-tuning-rules
fetched_at: 2026-08-13T15:30:27Z
source: palo-alto-main
---

# Step 4: Create the Temporary Tuning Rules Clear

Step 4: Create the Temporary Tuning Rules 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Internet Gateway Best Practice Security Policy 

 : 
 Step 4: Create the Temporary Tuning Rules 

 Updated on 

 Aug 6, 2025 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Expand all | Collapse all 

 Best Practice Internet Gateway Security Policy 

 What Is a Best Practice Internet Gateway Security Policy? 

 Why Do I Need a Best Practice Internet Gateway Security Policy? 

 How Do I Deploy a Best Practice Internet Gateway Security Policy? 

 Identify Your Application Allow List 

 Map Applications to Business Goals for a Simplified Rulebase 

 Use Temporary Rules to Tune the Allow List 

 Application Allow List Example 

 Create User Groups for Access to Allowed Applications 

 Decrypt Traffic for Full Visibility and Threat Inspection 

 Transition Safely to Best Practice Security Profiles 

 Transition Vulnerability Protection Profiles Safely to Best Practices 

 Transition Anti-Spyware Profiles Safely to Best Practices 

 Transition Antivirus Profiles Safely to Best Practices 

 Transition WildFire Profiles Safely to Best Practices 

 Transition URL Filtering Profiles Safely to Best Practices 

 Transition File Blocking Profiles Safely to Best Practices 

 Create Best Practice Security Profiles for the Internet Gateway 

 Define the Initial Internet Gateway Security Policy 

 Step 1: Create Rules Based on Trusted Threat Intelligence Sources 

 Step 2: Create the Application Allow Rules 

 Step 3: Create the Application Block Rules 

 Step 4: Create the Temporary Tuning Rules 

 Step 5: Enable Logging for Traffic That Doesn’t Match Any Rules 

 Monitor and Fine-Tune the Policy Rulebase 

 Remove the Temporary Rules 

 Maintain the Rulebase 

 Updated on 

 Aug 6, 2025 

 Focus 

 Home 

 Best Practices 

 Internet Gateway Best Practice Security Policy 

 Best Practice Internet Gateway Security Policy 

 Define the Initial Internet Gateway Security Policy 

 Step 4: Create the Temporary Tuning Rules 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Internet Gateway Best Practice Security Policy 

 Step 4: Create the Temporary Tuning Rules 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Best Practice Internet Gateway Security Policy 

 What Is a Best Practice Internet Gateway Security Policy? 

 Why Do I Need a Best Practice Internet Gateway Security Policy? 

 How Do I Deploy a Best Practice Internet Gateway Security Policy? 

 Identify Your Application Allow List 

 Map Applications to Business Goals for a Simplified Rulebase 

 Use Temporary Rules to Tune the Allow List 

 Application Allow List Example 

 Create User Groups for Access to Allowed Applications 

 Decrypt Traffic for Full Visibility and Threat Inspection 

 Transition Safely to Best Practice Security Profiles 

 Transition Vulnerability Protection Profiles Safely to Best Practices 

 Transition Anti-Spyware Profiles Safely to Best Practices 

 Transition Antivirus Profiles Safely to Best Practices 

 Transition WildFire Profiles Safely to Best Practices 

 Transition URL Filtering Profiles Safely to Best Practices 

 Transition File Blocking Profiles Safely to Best Practices 

 Create Best Practice Security Profiles for the Internet Gateway 

 Define the Initial Internet Gateway Security Policy 

 Step 1: Create Rules Based on Trusted Threat Intelligence Sources 

 Step 2: Create the Application Allow Rules 

 Step 3: Create the Application Block Rules 

 Step 4: Create the Temporary Tuning Rules 

 Step 5: Enable Logging for Traffic That Doesn’t Match Any Rules 

 Monitor and Fine-Tune the Policy Rulebase 

 Remove the Temporary Rules 

 Maintain the Rulebase 

 Step 4: Create the Temporary Tuning Rules 

 The temporary tuning rules help you monitor the initial best practices rulebase for gaps and
 alert you to alarming behavior. 

 For example, temporary rules identify traffic that comes from unknown users or from
 applications running on unexpected ports. Monitor traffic that matches the temporary
 rules to gain a full understanding of all of the applications in use on your network
 (and ensure application availability while you transition to a best practice
 rulebase). Use this information to help you fine-tune your allow list, either by
 adding new allow rules for applications you weren’t aware you needed or to narrow
 your allow rules and replace application filters with application groups or specific
 applications. When traffic no longer matches these rules, you can remove the temporary rules . 

 Some temporary tuning rules go above the rules that block bad applications and some go after
 to ensure that targeted traffic matches the appropriate rule, while ensuring
 that bad traffic doesn't get onto your network. 

 Allow web-browsing and SSL on non-standard ports
for known users to determine if there are any legitimate applications
running on non-standard ports. 

 Why Do I Need This Rule? Rule Highlights 

 This rule helps determine if you have gaps in your policy where users can't access legitimate
 applications because they run on non-standard
 ports. 

 Monitor all traffic that matches this rule. For legitimate traffic, add the appropriate
 applications to the appropriate allow rules. Create a custom
 application when appropriate. 

 Unlike allow rules that allow applications only on the default port, this rule allows
 web-browsing and SSL traffic on any port to find
 gaps in your allow list. 

 Because this rule finds gaps in policy, limit it to known users on your network. 

 Explicitly allow SSL as an application in this rule if you want to allow users to be able to
 browse HTTPS sites that aren’t decrypted (for
 example, financial services and healthcare
 sites). 

 Attach best practices security profiles to scan for
 threats. 

 Add this rule above the application block rules or no traffic will match this rule. 

 Allow web-browsing and SSL traffic on non-standard ports
from unknown users to highlight all unknown users regardless of
port. 

 Why Do I Need This Rule? Rule Highlights 

 This rule helps determine whether you have gaps in your User-ID 
 coverage. 

 This rule helps identify compromised or embedded devices that try to reach the internet. 

 It's important to block non-standard port usage, even for web-browsing traffic, because it is an
 evasion technique. 

 While the majority of the application
allow rules apply to known users or specific user groups, this rule
explicitly matches traffic from unknown users. 

 This rule must go above the application block rules or traffic will never hit it. 

 Attach best practices security profiles to scan for threats. 

 Allow all applications on the application-default port
to identify unexpected applications. 

 Why Do I Need This Rule? Rule Highlights 

 This rule
provides visibility into applications that you weren’t aware were running
on your network so that you can fine-tune your application allow list. 

 Monitor all traffic that matches this rule to determine whether it represents a potential threat
 or whether you need to modify your allow rules to
 enable access to more applications. 

 Because this rule allows all applications,
you must add it after the application block rules to prevent bad
applications from running on your network. 

 If you run PAN-OS 7.0.x or earlier, to appropriately identify unexpected applications, create an
 application filter that includes all
 applications, instead of setting the rule to allow
 any application. 

 Allow any application on any port to identify applications running on
 non-standard ports. 

 Why Do I Need This Rule? Rule Highlights 

 This rule helps identify legitimate, known
 applications running on unknown ports. 

 This rule helps identify unknown applications for
 which you need to create a custom application and
 add to your application allow rules. 

 Traffic that matches this rule is actionable.
 Track down the source of the traffic and ensure
 that you don't allow unknown tcp, udp, or
 non-syn-tcp traffic. 

 Because this is a very general rule that allows any
 application from any user on any port, place it at
 the bottom of the rulebase. 

 Enable logging for traffic that matches this rule so
 that you can investigate misuse of applications and
 potential threats or identify legitimate
 applications that require a custom application. 

 Previous 

 Step 3: Create the Application Block Rules 

 Next 

 Step 5: Enable Logging for Traffic That Doesn’t Match Any Rules 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
