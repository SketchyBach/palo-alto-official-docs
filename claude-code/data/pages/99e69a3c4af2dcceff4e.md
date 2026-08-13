---
url: https://docs.paloaltonetworks.com/ngfw/administration/app-id/security-policy-rule-optimization/identify-security-policy-rules-with-unused-applications
fetched_at: 2026-08-13T16:39:27Z
source: palo-alto-main
---

# Identify Security Policy Rules with Unused Applications Clear

Identify Security Policy Rules with Unused Applications 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Identify Security Policy Rules with Unused Applications 

 Updated on 

 Aug 3, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 App-ID 

 Security Policy Rule Optimization 

 Identify Security Policy Rules with Unused Applications 

 Download PDF 

 Next-Generation Firewall 

 Identify Security Policy Rules with Unused Applications 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Add Applications to an Existing Rule 

 Next 

 High Availability for Application Usage Statistics 

 Identify Security Policy Rules with Unused Applications 

 Policy Optimizer finds Security policy rules that specify
applications not seen on your network so you can remove the unused
apps to reduce the attack surface. 

 Where Can I Use This? What Do I Need? 

 Prisma Access 

 Next-Generation Firewall 

 This is a core Network Security feature for NGFWs and Prisma
 Access; no prerequisites needed. 

 If you have application-based Security policy
rules that allow a large number of applications, you can remove
unused applications (applications never seen on the rules) to tighten
those rules so that they only allow applications actually seen in
traffic that matches the rule. Identifying and removing unused applications
from Security policy rules is a best practice that strengthens your
security posture by reducing the attack surface. 

 Identify Security policy rules that have unused
applications. 

 Policies Security Policy Optimizer Unused Apps displays
all application-based rules that are configured with applications
that have not matched (been seen on) the rule. This means that these
rules allow applications that you may not use in your network (or
that another rule shadows the rule, so traffic that you expect to
match the rule matches an earlier rule in the rulebase). 

 The
number of Apps Allowed and Apps
Seen are updated approximately every hour, so if you
configure applications on a rule and don’t see as many Apps Allowed as
you expect, check again after about an hour. Depending on the firewall’s
load, it may take longer than one hour for these fields to update. 

 Prioritize which rules with unused applications to modify
first. 

 Policies Security Policy Optimizer Unused Apps enables
you to sort rules without
affecting their order in the rulebase and provides other information
that helps you prioritize rules to clean up based on your business
goals and risk tolerance. 

 The difference between Apps
Allowed (the number of applications on the allow list)
and Apps Seen (the number of allowed applications
actually seen on the rule) shows how many applications are configured
on each rule but not actually seen on the rule, which indicates
to what extent the rule is over-provisioned. Click Apps
Allowed to sort by the number of applications allowed
in a rule and click Apps Seen to sort by
the number of applications actually seen on a rule. 

 Days with No New Apps (click to sort)
shows you the number of days since the last time a new application
hit the rule. This indicates how likely it is that the rule is mature
and won’t see any applications that haven’t already been seen. The
longer the Days with No New Apps , the less
likely that new applications will hit the rule and the more likely
that you know all the applications the rule allows. 

 Created and Modified dates
also help determine whether a rule has matured enough to understand
whether applications not seen on the rule may be seen at a later
date or if the rule has seen all the applications expected to hit
the rule. The longer the time since a rule was Modified ,
the more likely the rule is mature. (If Created and Modified are
the same, the rule hasn’t been modified.) 

 Hit Count —Displays rules with the
most matches over a selected time frame. You can exclude rules for
which you reset the hit counter and specify the exclusion time period
in days. Excluding rules with recently reset hit counters prevents
misconceptions about rules that show fewer hits than you expect
because you didn’t know the counter was reset. 

 You can
also use Hit Count to View Policy Rule Usage . 

 You can also click Traffic (Bytes, 30 days) to
sort by the amount of traffic a rule has seen over the last 30 days.
Use this information to prioritize which rules to modify first.
For example, you can prioritize rules with the largest difference
between Apps Allowed and Apps
Seen and that also have the most Days with
No New Apps , because those rules have the greatest number
of unused applications and are the most mature. 

 Review the Apps Seen on the rule. 

 On Unused Apps , click Compare or
the number in the Apps Seen column to open Applications
& Usage , which shows the applications configured
on the rule ( Apps on Rule ) and the Apps
Seen on the rule. 

 The
number next to Apps Seen (10 in this example)
is the number of applications that matched the rule. Keep in mind
that it takes at least one hour for the firewall to update Apps Seen . 

 The number next to Apps on Rule (35
in this example) is how many applications are configured on the
rule, which is calculated by counting each application in a container
app (but not the container app itself—if you configure a container
app on the rule, the rule allows the container app’s individual
applications). Because the Applications list
shows only the applications you configure manually on the rule,
when you configure a container app on a rule, Applications only
shows the container app, not all of the individual applications
in the container (unless you also manually configure the individual
applications on the rule). For this reason, the number of Apps
on Rule may not be the same as the number of applications
you see in the Applications list. 

 Click the number next to Apps on Rule to
see all of the individual applications on the rule. 

 This example
rule has 10 Apps Seen (applications that
matched the rule) but allows 35 Apps on Rule .
The facebook container app is configured
on the rule and the rule sees traffic from the individual applications
facebook-base, facebook-chat, and facebook-video ( Apps Seen ).
When you click the Apps on Rule number, the Apps
on Rule dialog displays the individual applications
allowed, but not the container app itself. 

 You
cannot add or delete applications from the pop-up dialog. 

 Compare
the Apps Seen on the rule to the Apps
on Rule . If an application on the rule isn’t used (you
don’t see the application or you don’t see applications in an allowed
container in Apps Seen ), consider removing
the application from the rule to reduce the attack surface. Take
into account periodically used applications, such as for quarterly
or annual events, which may look unused if you don’t examine a long
enough time frame. Timeframe enables you
to select the time frame for the Apps Seen on
the rule. Select Anytime to see every application
seen over the life of the rule. Depending on the Created or Modified date
in the No App Specified dialog and the time
between periodic events, the rule may not have been on the firewall
long enough to see all periodically used applications. 

 Remove unused applications from the rule. 

 Delete (or Add )
applications in Apps on Rule to remove (or
add) applications manually, or Match Usage to
add the Apps Seen on the rule and delete
applications for which no matching traffic has been seen on the
rule with one click. 

 To remove applications from the rule
manually, select applications from Apps on Rule and Delete them.
Ensure that none of the applications are required for periodic events
before you remove them from the rule. (You can also add or delete
applications on the Security policy rule’s Application tab.) 

 Match
Usage moves the Apps Seen on
the rule to Apps on Rule and removes all
unused applications from the rule. 

 You can clone rules
from Policies Security and
from No App Specified to Migrate Port-Based to App-ID Based Security Policy Rules . You can’t
clone a rule starting from Unused Apps . 

 Commit the configuration. 

 Monitor updated rules and listen to user feedback to
ensure that updated rules allow the applications you want to allow
and don’t inadvertently block periodically used applications. 

 The number of Apps Allowed and Apps
Seen are updated approximately every hour. After you
remove all of the unused applications from a rule, the rule remains
listed in Policies Security Policy Optimzer Unused Apps until
the firewall updates the display. When the firewall updates the
display and the number of Apps Allowed is
the same as the number of Apps Seen , the
rule no longer displays in the Unused Apps screen.
However, depending on the firewall’s load, it may take longer than
one hour for these fields to update. 

 Previous 

 Add Applications to an Existing Rule 

 Next 

 High Availability for Application Usage Statistics 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
