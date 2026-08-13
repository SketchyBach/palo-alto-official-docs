---
url: https://docs.paloaltonetworks.com/best-practices/10-1/best-practices-for-migrating-to-application-based-policy/best-practices-for-migrating-to-application-based-policy/migrate-to-application-based-policy-using-policy-optimizer/convert-simple-rules-with-few-well-known-applications
fetched_at: 2026-08-13T15:30:03Z
source: palo-alto-main
---

# Convert Simple Rules with Few Well-Known Applications Clear

Convert Simple Rules with Few Well-Known Applications 

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
 Convert Simple Rules with Well-Known Apps After One Week 

 Updated on 

 Jan 26, 2024 

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

 Jan 26, 2024 

 Focus 

 Home 

 Best Practices 

 Best Practices for Migrating to Application-Based Policy 

 Best Practices for Migrating to Application-Based Policy 

 Migrate to Application-Based Policy Using Policy Optimizer 

 Convert Simple Rules with Well-Known Apps After One Week 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Best Practices for Migrating to Application-Based Policy 

 Convert Simple Rules with Well-Known Apps After One Week 

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

 Convert Simple Rules with Well-Known Apps After One Week 

 Convert legacy port-based security policy rules that
control a small number of well-known applications after one week
of monitoring production traffic. 

 After a week of monitoring
production traffic, you can safely begin to convert simple port-based
rules to App-ID based rules. Good candidates include rules for which
only one or a small number of well-known applications should legitimately
use the port because it’s fairly easy to determine which applications
you want to allow on a simple rule. Examples include port 21 (FTP),
port 22 (SSH), and port 53 (DNS). 

 Install the latest Content Updates before
you begin converting rules to ensure you have the latest application
signatures on your PAN-OS appliance. This example shows you how
to sort port-based rules to find candidates for safe conversion
and the options for converting those port-based rules directly to
App-ID based rules. 

 In Policies Security Policy Optimizer No App Specified , select Apps
Seen and Sort Ascending (or click Apps
Seen to reverse the current display order) to find the
port-based rules that have seen the fewest applications. 

 The port-based rules that have seen the fewest applications
are at the top of the No App Specified display.
You can safely convert rules for specific services, such as SSH,
directly to application-based rules and you can examine rules that
have seen few applications to see if you can safely convert them. 

 The
port-based rule intended to allow Server Message Block (SMB) traffic
has seen only three applications since migrating the configuration
to the PAN-OS appliance and therefore is a candidate for conversion. 

 Click the Apps Seen number or Compare to
examine the applications seen on the rule. 

 Applications & Usage shows the
applications actually seen in the traffic that match the rule. 

 Evaluate whether you want to allow all, some, or none
of the applications seen on the rule and select the applications
you want to allow. 

 You can match the exact usage of the rule, future-proof
the rule by adding the container apps, or select individual applications
to add to the rule. 

 If you want the rule to allow all applications
exactly as matched on the rule: 

 Select all Applications in Apps
Seen ). 

 Click Match Usage . 

 Click OK to convert the port-based
rule to an App-ID based rule. 

 Set the Service to application-default so
that no evasive, malicious applications can use the port. 

 If you want to allow all or some of the applications seen
on the rule or future-proof the rule by adding their container applications
(so all applications within each container are allowed and applications
added to the container app later are automatically allowed): 

 Select all the applications and then Add to This
Rule . 

 The
gray-shaded applications are the container apps. The green-shaded
applications are the applications seen on the rule. The unshaded
applications belong to the same container app but have not been
seen on the rule. 

 By default, Add container app is
selected, so all of the applications in the container are also selected
by default. 

 If you only want the rule to include the applications that
matched the rule, select Add container app .
Only applications seen on the rule are added to the rule. The container
app and the applications on the rule that have not matched the rule
are not selected. Click OK to select just
the applications seen on the rule. 

 If
you want to include the container app and all of its applications
in the rule, leave the selection as Add container app and
then click OK . Only the container apps appear
in Apps on Rule because they include (allow)
all of the applications they contain, which also “future proofs”
the rule by allowing applications added to the container in the
future: 

 Click OK on the Usage tab
to convert the rule. 

 Set the Service to application-default so
that no evasive, malicious applications can use the port. 

 If you want to select the applications to allow within a
container app, select those applications and then click Add
to This Rule . For example, if you decide not to allow
msrpc-base and select only ms-ds-smbv2 and ms-ds-smbv3 and Add
to Rule , Policy Optimizer shows you the related applications
in the container app (ms-ds-smb, shaded gray) and provides the opportunity
to future-proof the rule by adding those applications: 

 Select
the applications you want to allow and then click Add
to This Rule . 

 For example, if you decide not to
allow msrpc-base and select only ms-ds-smbv2 and ms-ds-smbv3 and Add
to This Rule , Policy Optimizer shows you the related
applications in the container app (ms-ds-smb, shaded gray) and provides
the opportunity to future-proof the rule by the container app with
all of its current and future applications: 

 The
green-shaded applications are the applications seen on the rule.
The unshaded applications belong to the same container app but have
not been seen on the rule. 

 You can allow all of the applications or select which applications
to allow. 

 To allow all the container app and all of its current
and future applications, click OK . Apps
on Rule shows the selected applications. Click OK to
convert the rule. 

 To allow only selected applications, deselect
the undesired applications. If you deselect an application in a
container, the container app is also deselected so that it doesn’t
automatically allow its child apps. 

 Click OK . Apps on Rule shows
the selected applications. 

 Click OK to convert the rule. 

 Set the Service to application-default so
that no evasive, malicious applications can use the port. 

 Previous 

 Migrate to Application-Based Policy Using Policy Optimizer 

 Next 

 Rules to Begin Converting After 30 Days 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
