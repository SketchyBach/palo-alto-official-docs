---
url: https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/risk-and-remediation/software-composition-analysis-sca-scanners/software-composition-analysis-sca-vulnerability-issues/investigate-prioritize-and-remediate-vulnerability-issues
fetched_at: 2026-09-06T10:12:40Z
source: cortex-platform
---

# Investigate, prioritize and remediate vulnerability issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Software supply chain security 

 Risk and remediation 

 Software Composition Analysis (SCA ) 

 Software Composition Analysis (SCA) vulnerability issues 

 Investigate, prioritize and remediate vulnerability issues 

 To effectively manage vulnerabilities, follow this lifecycle, moving from an open backlog to a resolved and prevented issue. 

 Stage 

 Action 

 Primary tenant surface 

 Assess 

 Understand your backlog through the widgets 

 Urgency Breakdown and SLA widgets 

 Prioritize 

 Decide which issue to work on next 

 Insights widget on the Vulnerabilities table 

 Investigate 

 Confirm blast radius and justify the ranking 

 Issue side panel 

 Remediate 

 Apply a fix or a compensating control 

 Resolution tab in the issue side panel 

 Prevent 

 Block future reintroduction using policies 

 Unified Application Security Policies 

 Assess 

 Before selecting an issue, review the Urgency widget to understand the overall shape of your backlog and allocate capacity effectively. Review the SLA widget alongside the Urgency widget: the SLA widget charts open issues by deadline status, where each CVE vulnerability issue carries an SLA target derived from its severity. Reading both widgets together separates deadline pressure from exploitability — an issue can be Overdue without being Top Urgent, and Top Urgent without being Overdue. 

 Prioritize 

 The prioritization rule 

 Prioritize by Urgency first. Use Severity as the tie-breaker within an Urgency tier. Severity answers a theoretical question: if an attacker exploited this CVE, how much damage results? Urgency answers an operational question: can an attacker actually reach this CVE, is the CVE being exploited in the wild, and does the affected asset matter to the business? 

 Use the Insights widget 

 Each insight card pairs an Urgency level with a second risk dimension and states how many issues satisfy both conditions. Selecting a card applies both filters to the Vulnerabilities table. The Vulnerabilities table defines six insight cards, covering SLA breach, business criticality, internet exposure, fix availability, dependency type, and traceability gaps. 

 Investigate 

 An Urgency level tells you an issue ranks highly. It does not tell you what happens if the issue is exploited, or what the fix will cost. Investigation answers three questions, and each answer changes the action you take. 

 Can an attacker reach this CVE? 

 A CVE in a package that never executes in a reachable position is a scheduling item. A CVE that is exploited in the wild, in a deployed and internet-exposed asset, is an incident. The Urgency Details section in the issue side panel supplies the reachability evidence : whether the CVE is listed in CISA KEV, its EPSS probability, its exploit maturity and exploit availability, and whether the affected package is used in an image, deployed, internet-exposed, or loaded into the memory of a deployed asset. 

 Impact: What is exposed if the CVE is exploited? 

 Blast radius determines the escalation level and how much capacity the issue justifies. The Urgency Details section reports the count of affected assets, the criticality and environment of the owning application, whether the affected asset has access to sensitive data or holds privileged capabilities, and the effectiveness of any compensating control already in place. The Code-to-Cloud graph shows the same exposure as a path, the repository, the pipeline that builds it, and every asset the pipeline deploys to. 

 Who owns the fix, and what does the fix cost? 

 The code evidence names the repository, the branch, the file path, and the commit that introduced the finding, along with the commit author. That identifies the team to route the work to and the manifest to change. The placement of the package (direct/transitive) determines the cost. 

 For complete investigation details, refer to Reference B: Investigation details . 

 Remediate 

 The Resolution tab presents the remediation paths available for the issue and the target fix version. 

 Steps: 

 Navigate to Application Security > Issues > Vulnerabilities . 

 Select the issue row to open the issue side card. The issue side card displays the current SLA status of the issue. 

 Select the Resolution tab. 

 Resolution details: 

 Path 

 Use when 

 Automated fix pull request 

 An Open pull request control, with a proposed code change | Cortex Cloud can fix the issue automatically 

 Manual package upgrade 

 A fix version exists, but the automated fix is not offered for the issue. Apply the upgrade manually 

 Compensating control 

 No fix version exists. Reduce exposure instead of upgrading. Apply a WAF rule, network segmentation, or runtime agent protection, and monitor for a fix release 

 Escalate to a Case when the remediation requires coordination across teams. 

 Result: The remediated issue moves to a resolved state and stops the SLA clock at its resolution timestamp. 

 Prevent 

 A remediated CVE that the next commit reintroduces has not been resolved. Close the loop with a Unified Application Security Policy that blocks the vulnerability pattern at the earliest enforcement point. 

 Select the trigger in shift-left order: a PR Scan trigger blocks the vulnerability before the code merges, and a CI Scan trigger blocks the vulnerable artifact before deployment. Align the policy grace period to the Urgency level — shorter grace periods for issues that reach Top Urgent, longer grace periods for issues that remain Not Urgent. 

 For policy triggers, actions, conditions, and grace period configuration, refer to Unified Application Security policies . 

 Previous Understand the Vulnerabilities table 

 Next View and understand CVE findings 

 Last updated 1 month ago 

 Was this helpful?
