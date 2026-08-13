---
url: https://docs.paloaltonetworks.com/best-practices/security-policy-best-practices/security-policy-best-practices/deploy-security-policy-best-practices/security-policy-rulebase-best-practices
fetched_at: 2026-08-13T15:30:34Z
source: palo-alto-main
---

# Security Policy Rulebase Best Practices Clear

Security Policy Rulebase Best Practices 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Security Policy Best Practices 

 : 
 Security Policy Rulebase Best Practices 

 Updated on 

 Apr 4, 2024 

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

 Security Policy Best Practices 

 Plan Security Policy Best Practices 

 Deploy Security Policy Best Practices 

 Security Policy Rule Best Practices 

 Security Policy Rulebase Best Practices 

 Policy Optimizer Best Practices 

 App-ID Cloud Engine Best Practices 

 Policy Recommendation Best Practices 

 Maintain Security Policy Best Practices 

 Updated on 

 Apr 4, 2024 

 Focus 

 Home 

 Best Practices 

 Security Policy Best Practices 

 Security Policy Best Practices 

 Deploy Security Policy Best Practices 

 Security Policy Rulebase Best Practices 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Security Policy Best Practices 

 Security Policy Rulebase Best Practices 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Security Policy Best Practices 

 Plan Security Policy Best Practices 

 Deploy Security Policy Best Practices 

 Security Policy Rule Best Practices 

 Security Policy Rulebase Best Practices 

 Policy Optimizer Best Practices 

 App-ID Cloud Engine Best Practices 

 Policy Recommendation Best Practices 

 Maintain Security Policy Best Practices 

 Security Policy Rulebase Best Practices 

 Best practices for PAN-OS and Prisma Access rulebase order, simplification, shadowing
 prevention, and hygiene. 

 The Security policy rulebase is an ordered
list of your Security policy rules. The order of the rules determines
how the firewall handles traffic. 

 Firewalls compare traffic to Security policy rules, starting with the first rule at the top of
 the Security policy rulebase. When traffic matches a rule’s criteria, the firewall executes the
 rule’s action on the traffic and doesn't compare the traffic to any other rules. If no rule
 matches the traffic, the firewall drops the traffic (implicit deny). The way you order the rules
 in the rulebase is critical because the firewall takes action on the traffic on the first rule
 match and then stops comparing the traffic to the rulebase. 

 If you migrated Security policy from another vendor’s firewall, the previous firewall might have
 evaluated traffic against its rulebase differently. For example, the order of the rules might
 not have made a difference on your old firewall but they are crucial on Palo Alto Networks
 firewalls. 

 Understanding how you want to handle different types of traffic and how Security policy rules
 work help you evaluate how to order rules in the
 rulebase. Design and optimize your Security policy rulebase in a
 logical manner, as described in this section. For existing
 rulebases, if the rulebase isn’t optimized as much as it could be,
 plan and test changes in accordance with the advice in this section.
 If you plan to roll out the changes in phases, make the changes at
 the appropriate time or times. 

 This section
covers: 

 Ordering Security
policy rules in the rulebase 

 Avoiding rulebase
bloat 

 Positioning to make
exceptions to a rule 

 Preventing and remediating
rule shadowing 

 Using device group
hierarchies on Panorama to simplify the rulebase 

 Order
Security policy rules logically in the rulebase. 

 Because the firewall executes a policy rule’s action on
traffic when that traffic matches the rule’s criteria, the order
of the rules is critical and determines which rule traffic matches,
and therefore, which action the firewall takes on the traffic and
how the firewall inspects the traffic: 

 Place rules that block malicious traffic at the top of the rulebase to prevent accidentally
 allowing bad traffic later in the rulebase. If you
 have an active Advanced Threat Prevention or
 active legacy Threat Prevention license, create block rules
 based on the predefined external dynamic lists
 (EDLs) and test them to ensure that they
 don’t block traffic that you want to allow. On
 Panorama, place these rules in the pre-rules so
 they execute before any firewall-specific
 rules. 

 Allow basic infrastructure applications and common services
such as DNS and NTP near the top of the rulebase to prevent accidentally
blocking them. These rules usually allow traffic from any source
zone to any destination zone and apply to everything and everyone. 

 On Panorama, place these rules in the pre-rules so they execute before any locally defined rules
 on the firewall. 

 The logic for all other rules is to place the most specific rules near the top of the rulebase
 and the most general rules closer to the bottom of the rulebase. If you place general rules
 before specific rules in the rulebase, traffic that you intend to match the specific rule
 might match the general rule instead, which might apply a different action and different
 inspection to the traffic than you want. This is called shadowing —another rule “shadows” the rule
 that you intend the traffic to match. 

 If you have not yet converted or cannot convert all of your
port- and service-based Security policy rules to App-ID-based rules,
place App-ID-based rules ahead of port- and service-based rules. 

 Keep the
rulebase as small as you can for easier management and to avoid
rulebase bloat. 

 If five of the following six objects are the same
in multiple rules, combine those rules into one rule: 

 Source
zone 

 Destination zone 

 Source IP address 

 Destination IP address 

 Service port 

 Application 

 For example, if three rules specify
different applications but have the same source and destination
zone, source and destination IP addresses, and service port, then you
can combine the rules into one rule that specifies the applications
from each of the original rules. 

 Use group objects to simplify policy creation and reduce
rulebase size. 

 Use application groups and address groups to
help consolidate rules that apply to all of the group members. 

 If you use both individual objects and group objects in policy, be aware that an object’s
 membership in a group might cause rule shadowing if the object is specified
 individually in a rule and also specified in a rule as part of an object group. In this
 case, the firewall might not take the intended action because the traffic might match the
 wrong rule first. If possible, combine the rules, unless your change control process
 requires a specific policy to track access. If you want to treat an object differently than
 other objects in a group, remove the object from the group. 

 Disable or remove rules from the Security policy rulebase
when you no longer need them. 

 Security policy rules might become unneeded when an organization changes applications or
 infrastructure, or when you no longer need temporary testing rules. If you don't disable or
 delete those rules, they might cause unexpected actions on traffic. It’s safest to disable a
 rule first so that you can enable it again if disabling it causes issues. When you disable
 rules, apply a tag with the date you disabled the rules. Periodically use Policy Optimizer’s
 Rule Usage feature to check how long each rule has
 been unused. After a period of time where you’re confident that you really don't need the
 rule, delete it. 

 Be aware of rules with applications that you use only for periodic events such as quarterly
 meetings or annual conferences. It might be appropriate to configure a
 Schedule that enables the rule only during the event time
 period. 

 Use Policy Optimizer to
optimize the rulebase. Policy Optimizer finds unused rules, rules
with unused applications, rules that haven’t been used over time,
and rules that don’t have Log Forwarding profiles, as well as enabling
you to manage new SaaS applications in Security policy if you have
a SaaS Security subscription. 

 On Panorama, use common global device groups that apply to
multiple VSYSs and firewalls across the organization for common,
global Security policy rules such as rules that control common basic
services and any other services or applications that you want to
apply to broad groups of devices. Create the device group hierarchy so
that you don’t have to repeat rules across groups—use the hierarchy
to write a rule one time and apply it to all appropriate firewall
groups. 

 Review the Security policy rulebase periodically as part
of regularly scheduled maintenance. 

 To make
an exception to a rule, place the more specific rule in front of
the more general rule. 

 For example, you want to block your employees from going to malicious websites, so you create a
 general Security policy rule that blocks access to all malicious websites for all employees.
 However, your InfoSec team and PEN testers need access for testing purposes. In this case, you
 create a rule that allows access to the required malicious websites for only those users
 (decrypting the traffic, applying the strictest Threat profiles to the rule, and specifying
 only the applications used for testing) and place that rule above the general rule in the
 rulebase. 

 When the InfoSec and pen testers try to access the malicious sites for testing, they are allowed,
 but no other users match the rule’s criteria, so the general rule blocks them. If you place
 the InfoSec and pen test team access rule after the general block rule, the general rule shadows the specific rule, and the InfoSec/pen
 tester traffic would match the general rule and be blocked. 

 Prevent
general rules from shadowing more specific rules. 

 Shadowing is when you place a broad rule that includes the same match criteria as a more specific
 rule higher in the rulebase than the specific rule,
 so traffic intended to match the specific rule
 instead matches the general rule first and is never
 compared to the specific rule. The result is that
 the firewall executes the action and inspection
 configured in the general rule when the intention is
 to execute the action and inspection in the specific
 rule. The general rule shadows the specific
 rule. 

 A shadow rule might shadow more than one other rule in the rulebase. 

 A
 partial shadowing conflict may occur when you
 specify a bi-directional NAT rule where the
 source or destination IP address (original or
 translated) overlaps with the source or
 destination IP address (original or translated) of
 another NAT rule (either shadowing or
 shadowed). 

 The easiest way to prevent shadowing is to construct the rulebase correctly from the start.
 However, existing rulebases and migrated rulebases might have shadow rules. To prevent and fix
 shadowing: 

 Understand the action that you want to take on the traffic and how you want to inspect it. 

 If the action and inspection in the specific rule are
how you want to handle the traffic, move the specific rule above
the general rule in the rulebase. If the action and inspection in
the general rule are how you want to handle the traffic, then you
don’t need the specific rule. 

 Place more specific Security policy rules above general rules
in the rulebase. If you place the general rule first, it shadows
the specific rule, for example: 

 Create a general rule
that blocks all access to Facebook. 

 Create a specific rule that allows marketing and PR groups
to access Facebook, but place the rule below the general Facebook
rule in the rulebase. 

 The general rule blocks all Facebook access regardless of user group, so traffic never matches
 the specific rule that allows access to the specific groups that you want to allow. 

 The
fix is to move the specific rule above the general rule in the rulebase. 

 Review and resolve shadowed rules to make sure the firewall
executes the action you want and inspects traffic in the manner
you want. 

 When you write a new Security policy rule: 

 Select
a commit option and then perform a Commit on
the firewall or a Validate Commit on Panorama to
check for configuration issues. Do not commit the configuration.
Resolve issues that the validation check discovers before proceeding. 

 Commit or Commit and Push the
configuration. 

 When the commit finishes, select Tasks from the bottom-right ribbon to
 open the Task Manager. 

 In the Type column, click Commit All to bring up
 Job Status . (Commit and Push doesn't provide shadowing
 information.) 

 Click the Status column message to
open the Last Push State Details and select
the Rule Shadow tab. If there is no Rule
Shadow tab, then the firewall has no shadowed rules. 

 The left side of Last Push State Details shows
the rules that shadow other rules. The name of each shadow rule
is a link to the rule. For each shadow rule, click the number in
the Count column to display the rules it
shadows. The shadowed rule names are listed, but they are not links
to the shadowed rules. 

 The list of shadow rules is not persistent across commit operations, so it is crucial for you to
 capture the list of shadowed rules for each shadow rule. For example, pull the status via
 an API using a script, copy and paste the list into a text editor, take a screen capture,
 take a photograph, or write down the names of the shadowing rules and the shadowed rules. 

 The PAN-OS
configuration Commit operation validates
for shadow rules. If rule shadowing is detected, it generates a
warning message that identifies the affected rules. If you perform
another commit operation before you capture the shadow list, the
shadow information is lost. Be sure to capture this information
immediately. 

 Find each shadowing and shadowed rule in the Security policy
rulebase and capture each rule’s configuration. 

 Compare each shadow rule with the rules that it shadows side by side and understand the purpose
 of each rule. This enables you to evaluate related rules together and understand how you
 want to handle the applications the rules control. 

 When you understand how you want to handle the applications
in a shadow rule and its shadowed rules, combine rules to simplify
the rulebase, disable or remove duplicate rules, and move specific
rules above general rules to resolve the shadowing. 

 Iterate to fix any remaining shadowing. 

 Repeat the process for each shadow rule. 

 On nonproduction test systems, you might want to keep shadowing and shadowed rules for testing
 new policy rules and other testing purposes. 

 On Panorama,
position Security policy rules appropriately within device group
hierarchies. 

 Position rules so that you don’t have to repeat the same
rule unnecessarily in multiple device groups. Rules that are common
to multiple device groups belong above those groups in the hierarchy
so one rule applies to all of the groups. 

 Construct the hierarchy in a thoughtful manner that only gives access to firewall groups that you
 intend to have access. Think about the access that each firewall needs when you construct
 device groups and think about the access each device group needs when you create the device
 group hierarchy. The key to construction is commonality—which firewalls need similar access,
 which groups of firewalls need similar access, and how to construct a hierarchy that enables
 groups higher in the hierarchy to contain rules that apply to the levels below them and
 eliminate the need to duplicate rules. 

 Place rules that apply to all firewalls in the highest group
in the hierarchy to avoid rule duplication. 

 Place rules that apply to sets of firewall groups high enough
in the hierarchy so that you don’t have to duplicate rules. 

 The Panorama Administrator’s Guide provides in-depth information about device groups, including an example illustration of a device
 group hierarchy . 

 Previous 

 Security Policy Rule Best Practices 

 Next 

 Policy Optimizer Best Practices 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
