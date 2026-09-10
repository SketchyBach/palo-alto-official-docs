---
url: https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/risk-and-remediation/cicd-risks/investigate-prioritize-and-remediate-ci-cd-risk-issues
fetched_at: 2026-09-06T10:12:43Z
source: cortex-platform
---

# Investigate, prioritize, and remediate CI/CD risk issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Software supply chain security 

 Risk and remediation 

 CI/CD Risks 

 Investigate, prioritize, and remediate CI/CD risk issues 

 To effectively manage CI/CD RIsks, follow this lifecycle, moving from an open backlog to a resolved and prevented issue. 

 Stage 

 Decision 

 Primary surface 

 Assess 

 How much capacity to commit, and to what 

 Severity widget and SLA widget above the CI/CD Risks table 

 Prioritize 

 Which risk category to harden next 

 Insights widget above the CI/CD Risks table 

 Investigate 

 What the attack path is, what the blast radius is, and who owns the pipeline 

 CI/CD Risks Evidence Panel 

 Remediate 

 Which configuration to change 

 Resolution tab in the issue side panel 

 Prevent 

 Which enforcement point blocks regression 

 Unified Application Security Policies 

 Important: A CI/CD risk affects the infrastructure that builds every application, not one application. A compromised pipeline can alter artifacts after every application-level check has passed, which means an unresolved CI/CD risk reduces the confidence you can place in the rest of your security posture. 

 Assess 

 Before selecting an issue, read the shape of the backlog. Two widgets above the CI/CD Risks table answer that question, and neither is a work queue — each describes a distribution, so that you commit capacity against a measured posture rather than against the first issue you happen to open. Refer to Understand the CI/CD Risks table for more inforamtion. 

 Prioritize 

 Prioritize by severity , and use the OWASP CI/CD risk category to group the work. Severity rates the insecure configuration itself. Because no Urgency classification is computed for this finding type, the environmental context that Urgency would supply — the credentials the affected pipeline holds, whether the pipeline accepts untrusted input, and how many pipelines the configuration affects — is established manually during Stage 3 rather than delivered as a precomputed level. 

 Use the Insights widget. Each insight card pairs a severity level with a second risk dimension and states how many issues satisfy both conditions. Selecting a card applies both filters to the CI/CD Risks table. The CI/CD Risks table defines the following insight cards: 

 Insight 

 Condition 

 Critical issues mapped to OWASP Top 10 CI/CD security risks 

 CI/CD risk issues with Critical or High severity mapped to the OWASP Top 10 CI/CD Security Risks 

 Critical issues mapped to CIS GitHub / GitLab Benchmark 

 CI/CD risk issues with Critical or High severity mapped to the CIS GitHub Benchmark or the CIS GitLab Benchmark 

 Start with either card. Both isolate the Critical and High population already mapped to a recognized standard, which is the subset that carries both the highest technical risk and the clearest reporting value. 

 Group by OWASP CI/CD category before selecting an issue. This is the CI/CD-specific prioritization strategy, and it differs from the per-issue approach that suits other issue types. CI/CD risks are classified against the OWASP Top 10 CI/CD Security Risks, and a concentration within one category identifies a systemic weakness in how pipelines are authored rather than a set of independent defects. Hardening a whole category in one pass produces a durable standard; remediating individual findings within a category produces the same findings again on the next pipeline someone writes. 

 Prefer instance-level and organization-level risks over pipeline-level risks. A single setting corrected at the VCS organization or CI/CD instance level resolves the risk across every pipeline that inherits the setting. Sorting by Affected Pipelines Count in descending order identifies those corrections directly. 

 Note: For the column and filter model of the table itself, see Understand the CI/CD Risks table. 

 Investigate 

 A severity level tells you how dangerous the configuration is in principle. It does not tell you how the configuration is exploited in your environment, or which team can change it. Investigation answers three questions, and each answer changes the action you take. 

 How would an attacker use this configuration? 

 A permissive setting on an isolated pipeline with no credentials is a hygiene item. The same setting on a pipeline that holds deployment credentials and runs on fork-originated pull requests is an active attack path. 

 The CI/CD Risks Evidence Panel supplies the attack path evidence: the evidence sentence stating what was detected and why the configuration is a risk, the code component snippet showing the configuration that triggered the detection rule, and the OWASP CI/CD category that classifies the risk. 

 Evidence 

 Consequence 

 The pipeline holds privileged credentials and executes on untrusted input 

 The poisoned pipeline execution path is complete. Treat as an incident and escalate 

 The pipeline holds privileged credentials, input is trusted 

 An attacker who reaches the pipeline reaches the credentials. Harden ahead of the SLA deadline 

 The configuration weakens code promotion controls 

 Unreviewed code can reach a protected branch or a deployed artifact. Harden ahead of the SLA deadline 

 The configuration is permissive but the pipeline holds no credentials and builds nothing deployable 

 A hygiene item. Harden on the SLA schedule 

 What is exposed if the pipeline is compromised? 

 Blast radius determines the escalation level and how much capacity the issue justifies. 

 The blast radius of a CI/CD risk is not the pipeline — it is everything the pipeline builds and everywhere the pipeline deploys. A single compromised pipeline can alter artifacts for every application it builds, and the alteration passes every application-level scan because the alteration occurs after those scans complete. 

 Establish the credentials the pipeline holds, the number of affected pipelines, and the criticality of the applications the pipeline builds. An instance-level or organization-level risk multiplies across every pipeline that inherits the setting, which is why two issues with the same detection rule and the same severity can justify entirely different responses. 

 Who owns the pipeline, and what does the fix cost? 

 CI/CD risks are frequently assigned to a practitioner who did not write the pipeline, which makes ownership identification the primary investigative obstacle rather than an afterthought. 

 Each CI/CD risk issue identifies the specific resource where the violation occurred — the VCS organization, the CI/CD instance, the pipeline, or the configuration file — and shows the configuration that triggered the detection. That evidence reaches the owning team and the exact change without reverse-engineering the pipeline first. 

 The level at which the configuration is set determines the cost. A workflow-file change is a pull request against one repository, owned by the team that owns the repository. An instance-level or organization-level setting is an administrative change, owned by the platform team, and it affects every pipeline at once — higher coordination cost, far higher leverage. Establish the level during the investigation, because the level determines both who does the work and how many issues the work closes. 

 Note: For the evidence sentence, the code component snippet, and the OWASP CI/CD category classification, see CI/CD Risks Evidence Panel. 

 Remediate 

 Open the Resolution tab in the issue side panel. The Resolution tab presents the remediation paths available for the issue and the recommended configuration. 

 Path 

 Use when 

 Correct the pipeline or workflow definition 

 The insecure configuration is declared in a workflow file in the repository. A pull request against the owning repository, reviewed by the owning team 

 Correct the CI/CD instance or VCS organization setting 

 The insecure configuration is an administrative setting rather than a file. Resolves the risk across every pipeline that inherits the setting. Requires platform team access 

 Scope the credentials the pipeline holds 

 The configuration cannot be changed without breaking the build. Reducing credential scope shrinks the blast radius even when the permissive configuration remains 

 Document an approved exception 

 The configuration is required by a functional constraint. Record the justification, apply a compensating control, and keep the exception under review 

 Sequence within a severity level by the number of affected pipelines. Among equally severe issues, an instance-level correction resolves many pipelines at once and delivers the highest hardening throughput. 

 Escalate to a Case when the correction requires platform team access that the assigned practitioner does not hold. 

 Note: For inspecting the CI/CD instance, see CI/CD instance as an asset. For inspecting the pipeline, see CI/CD pipeline as an asset. 

 Prevent 

 A hardened pipeline regresses the next time someone edits a workflow. Close the loop with a Unified Application Security Policy that converts a one-time remediation into an enforced standard. 

 Apply the CI/CD Configuration Scanners policy type. Configure the CI/CD Configuration Scanners policy type to define how the platform responds when the CI/CD Risks finding type reappears. Align the policy grace period to the severity level — shorter grace periods for Critical and High risks, longer grace periods for Medium and Low risks. 

 Enforce at the category level rather than the finding level. Because CI/CD risks concentrate by OWASP CI/CD category, a policy scoped to a category prevents the whole class of misconfiguration rather than the single instance you remediated. This is the same category-first logic that governs prioritization in Stage 2, applied to enforcement. 

 Note the rule constraint. CI/CD detection rules are out-of-the-box only; custom CI/CD rules are not supported. Prevention is configured through policy conditions over the supplied rule inventory rather than by authoring a new rule. 

 Note: For policy triggers, actions, conditions, and grace period configuration, see Unified Application Security Policies. For the CI/CD detection rule inventory, see Application Security rules. 

 When the backlog itself is unreliable 

 The CI/CD risk backlog measures the instances and organizations that CI/CD risk scanning covers. An uncovered instance produces no findings, and the absence of findings reads as a clean pipeline estate rather than as an unscanned one. 

 Verify that CI/CD risk scanning is enabled for every onboarded data source, and that the discovered instance inventory matches the instances your organization actually operates. A shadow CI/CD instance — one that builds production artifacts but was never onboarded — contributes nothing to the backlog while carrying the same credentials and the same blast radius as a covered instance. 

 Treat coverage across discovered instances as a prerequisite to trusting the CI/CD risk distribution. 

 Note: For verifying that CI/CD risk scanning is active across discovered instances, see Application Security coverage. 

 Previous Understand the CI/CD Risks table 

 Next View and understand VCS and CI/CD pipeline risk findings 

 Last updated 1 month ago 

 Was this helpful?
