---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/appsec-objectives-with-agentix/references/reference-c-metric-calculations
fetched_at: 2026-09-06T10:11:44Z
source: cortex-platform
---

# Reference C: Metric calculations | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 AppSec Objectives with Agentix 

 References 

 Reference C: Metric calculations 

 Each vulnerability objective reports four calculated metrics. Cortex Cloud computes each metric from the vulnerability issues and findings that match the objective scope and condition. The metrics are not real-time; they refresh through a background synchronization job that runs once when the objective is created and then on a recurring schedule. The detection rate and prevention rate are computed over a rolling 30-day window of findings. 

 Metric 

 Definition 

 Behavior at zero denominator 

 Remediation Rate 

 Resolved issues divided by total issues matching the scope and condition, as a percentage. 

 Returns 0 when there are no matching issues. 

 Detection Rate 

 Unique issues divided by periodic findings over the last 30 days, as a percentage — the share of the scope and condition that produces issues. Periodic findings are findings from periodic (scheduled) scans. 

 Returns 0 when there are no periodic findings. Returns 100 when unique issues exceed periodic findings. 

 Prevention Rate 

 Blocked non-periodic findings divided by non-periodic findings over the last 30 days, as a percentage — the share of the scope and condition blocked by PR or CI/CD actions. Non-periodic findings are findings from PR scans and CI/CD scans; blocked findings are those a PR or CI/CD policy blocked. 

 Returns 0 when there are no non-periodic findings. 

 Open Cases 

 The open cases with open, unresolved issues matching the scope and condition, with per-severity flags for critical, high, medium, and low cases. 

 No cases when none match. 

 NOTE : Detection rate quantifies how much of the targeted risk is being surfaced as issues, while prevention rate quantifies how much of that risk is being stopped earlier in the SDLC through PR or CI blocking. Read the two metrics together to understand whether an objective is shifting from detection toward prevention. 

 Previous Reference B: Objective condition filters 

 Next Code-to-Cloud 

 Last updated 1 month ago 

 Was this helpful?
