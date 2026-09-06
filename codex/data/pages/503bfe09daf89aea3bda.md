---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/ai-skill-security/review-skill-scan-results
fetched_at: 2026-09-06T11:17:57Z
source: ai-security
---

# Review Skill Scan Results Clear

Updated on 

 Aug 27, 2026 

 Focus 

 Home 

 Prisma AIRS 

 AI Skill Security (Preview) 

 Review Skill Scan Results 

 Download PDF 

 Prisma AIRS 

 Review Skill Scan Results 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Supply Chain Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Review Skill Scan Results 

 Understand how to read AI Skill Security scan results, including overall verdicts,
 rule outcomes, and vulnerability findings. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Skill Security) 

 No License required for preview 

 A scan produces one of two overall verdicts: 

 Allowed —The skill passed all configured blocking security and governance
 rules and is recommended for use based on the current policy configuration. 

 Blocked —One or more configured blocking rules identified findings that you
 should review before trusting or using the skill. 

 Rule Outcomes 

 The Rule Outcomes tab provides a detailed breakdown of how
 each security and governance rule evaluated the uploaded skill. For each rule, you
 can view: 

 Rule Status —Indicates whether the rule passed or generated one or more
 findings. 

 Matching Vulnerabilities —Displays the number of vulnerabilities
 associated with the selected rule. 

 Rule Details —Provides a description of what the rule detects and the
 types of behaviors it is designed to identify. 

 Related Vulnerabilities —Lists the findings associated with the selected
 rule, including the affected file or component. 

 Recommendations —Provides guidance for reviewing and remediating the
 identified behavior before trusting or deploying the skill. 

 Vulnerabilities 

 The Vulnerabilities tab lists every finding identified during
 the scan. Selecting a vulnerability displays detailed information. For each
 vulnerability, you can view: 

 Finding Summary —A high-level overview describing the detected behavior
 and why it was identified. 

 Vulnerability Type —The category of behavior detected, such as data
 exfiltration or silent operation. 

 Description —Additional context explaining the behavior and the
 potential security risk. 

 Affected Component —The file or resource within the uploaded skill
 package where the finding was detected. 

 Supporting Details —Additional information to help you understand the
 finding and determine whether further investigation or remediation is
 needed.
