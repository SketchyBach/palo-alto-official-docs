---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/security-profiles/set-up-or-override-a-default-security-profile-group
fetched_at: 2026-08-13T17:09:59Z
source: palo-alto-main
---

# Set Up or Override a Default Security Profile Group Clear

Set Up or Override a Default Security Profile Group 

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

 Set Up or Override a Default Security Profile Group 

 Updated on 

 Mon Aug 11 16:31:23 PDT 2025 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Filter

 Updated on 

 Mon Aug 11 16:31:23 PDT 2025 

 Focus 

 Home 

 PAN-OS 

 Policy 

 Security Profiles 

 Set Up or Override a Default Security Profile Group 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Set Up or Override a Default Security Profile Group 

 Table of Contents 

 Filter

 Previous 

 Create a Security Profile Group 

 Next 

 Data Filtering 

 Set Up or Override a Default Security Profile Group 

 Use the following options to set up a default
security profile group to be used in new security policies, or to
override an existing default group. When an administrator creates
a new security policy, the default profile group will be automatically
selected as the policy’s profile settings, and traffic matching
the policy will be checked according to the settings defined in
the profile group (the administrator can choose to manually select
different profile settings if desired). Use the following options
to set up a default security profile group or to override your default
settings. 

 If no default security profile exists, the
profile settings for a new security policy are set to None by default. 

 Create a security profile group. 

 Select Objects Security Profile Groups and
Add a new security profile group. 

 Give the profile group a descriptive Name ,
for example, Threats. 

 If the firewall is in Multiple Virtual System Mode,
enable the profile to be Shared by all virtual
systems. 

 Add existing profiles to the group. For details on
creating profiles, see Security
Profiles . 

 Click OK to save the profile
group. 

 Add the security profile group to a security policy. 

 Add or modify a security policy
rule and select the Actions tab. 

 Select Group for the Profile
Type . 

 In the Group Profile drop-down,
select the group you created (for example, select the Threats group): 

 Click OK to save the policy
and Commit your changes. 

 Set up a default security profile group. 

 Select Objects Security Profile Groups and
add a new security profile group or modify an existing security
profile group. 

 Name the security profile group default : 

 Click OK and Commit . 

 Confirm that the default security profile group is
included in new security policies by default: 

 Select Policies Security and Add a
new security policy. 

 Select the Actions tab and view the Profile
Setting fields: 

 By default,
the new security policy correctly shows the Profile Type set
to Group and the default Group Profile is
selected. 

 Override a default security profile group. 

 If you have an existing default security profile group,
and you do not want that set of profiles to be attached to a new
security policy, you can continue to modify the Profile Setting
fields according to your preference. Begin by selecting a different
Profile Type for your policy ( Policies Security Security Policy Rule Actions ). 

 Previous 

 Create a Security Profile Group 

 Next 

 Data Filtering 

 On This Page 

 PAN-OS 

 Next-Generation Firewall 

 Policy 

 11.1 

 Network Security 

 11.1 & Later 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
