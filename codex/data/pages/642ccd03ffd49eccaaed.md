---
url: https://docs.paloaltonetworks.com/pan-os/u-v/custom-app-id-and-threat-signatures/custom-application-and-threat-signatures/create-a-custom-threat-signature/create-a-combination-signature
fetched_at: 2026-09-16T07:40:52Z
source: palo-alto-main
---

# Create a Combination Signature Clear

Updated on 

 Thu Sep 03 18:17:31 PDT 2026 

 Focus 

 Home 

 Advanced Threat Prevention Powered by Precision AI® 

 Create a Custom Threat Signature 

 Create a Combination Signature 

 Download PDF 

 Advanced Threat Prevention Powered by Precision AI® 

 Create a Combination Signature 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced Threat Prevention 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Custom Application IDs and Signatures 

 Reference 

 Previous 

 Create a Custom Threat Signature 

 Next 

 Create a Custom Threat Signature from a Snort Signature 

 Create a Combination Signature 

 Learn how to use a time attribute in combination with
an existing threat signature. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 VM-Series 

 CN-Series 

 Advanced Threat Prevention (for enhanced feature
 support) or Threat Prevention License 

 You can create a combination signature to
monitor the frequency and rate of matches to a signature on your
network. You’ll need to know the Threat ID of an existing threat
signature or create a custom threat
signature that detects a particular event such as a Wordpress
login attempt. When you configure your combination signature, you’ll
have to specify the time conditions for matches to the threat—x
number of hits in y number of seconds. You can adjust the time attribute
according to needs and experience. 

 Add
a custom threat. 

 Click Objects Custom Objects Spyware/Vulnerability and
then click Add . 

 Under Configuration , fill out
the following required fields in the General and Properties sections. 

 Threat ID 

 For
a vulnerability signature, enter a numeric ID between 41000 and
45000. If the firewall runs PAN-OS 10.0 or later, the ID can also be
between 6800001 and 6900000. 

 For a spyware signature, the ID should be between 15000 and 18000.
If the firewall runs PAN-OS 10.0 or later, the ID can also be between 6900001
and 7000000. 

 Name —Specify the threat name. 

 Severity —Select the severity of the threat. 

 Define your signature. 

 Click Signatures and
select Combination . 

 Under Combination
Signatures , click Add And Condition or Add
Or Condition . 

 To add a condition within a group, select the group
and click Add Condition . 

 To move a condition within a group, select the condition
and click Move Up or Move Down . 

 You cannot
move conditions from one group to another. 

 To move a group, select the group and click Move
Up or Move Down . 

 Choose
the Threat ID for the signature you’d like
to use. You may also edit the condition name. 

 Under Time
Attribute specify the following: 

 Number of Hits —Specify the
threshold that will trigger any policy-based action as a number
of hits (1-1000) in a specified number of seconds (1-3600). 

 Aggregation Criteria —Specify whether
the hits are tracked by source IP address, destination IP address,
or a combination of source and destination IP addresses. 

 To move a condition within a group, select the condition
and click Move Up or Move Down . 

 You cannot
move conditions from one group to another. 

 To move a group, select the group and click Move
Up or Move Down . 

 Repeat sub-steps 2 , 3 , and 4 for each
matching condition. 

 If you leave Ordered Condition Match selected,
make sure the condition or group of conditions is in the desired
order. The most specific conditions should come first. To order
the conditions: Select a condition or a group and click Move
Up or Move Down . 

 You
cannot move conditions from one group to another. 

 Save the custom threat. 

 Click OK to save
the custom threat. 

 Commit your signature(s). 

 Test your custom signature . 

 Previous 

 Create a Custom Threat Signature 

 Next 

 Create a Custom Threat Signature from a Snort Signature
