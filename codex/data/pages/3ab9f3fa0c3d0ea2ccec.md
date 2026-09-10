---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/unified-application-security-policies/references/reference-d-trigger-and-actions-mapping
fetched_at: 2026-09-06T10:12:14Z
source: cortex-platform
---

# Reference D: Trigger and actions mapping | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security Posture Management (ASPM) 

 Unified Application Security policies 

 References 

 Reference D: Trigger and actions mapping 

 Triggers define when the policy evaluates findings. Actions define what the policy does when a finding matches 

 Triggers and actions 

 Code Scanners configuration rules 

 Select at least one trigger and at least one action per trigger 

 If no code-related finding types are selected in the conditions, code-related triggers are disabled 

 If no image-related finding types are selected in the conditions, image-related triggers are disabled 

 When only third-party scanner finding types are selected in the conditions, only the Periodic Scan trigger is available. PR Scan and CI Scan triggers are disabled for third-party scanner findings 

 Code scanners triggers 

 Trigger 

 Available actions 

 Default behavior 

 PR scan 

 Block PR, PR Comment, Create Issue (+ Override Severity) 

 PR Comment is enabled by default when the trigger is activated 

 CI scan 

 Block CI, CLI Report, Create Issue (+ Override Severity) 

 CLI Report is enabled by default when the trigger is activated 

 Periodic scan 

 Create Issue (+ Override Severity) 

 — 

 Image-category triggers (available when image-related finding types are selected) 

 Trigger 

 SDLC stage 

 Shift-left value 

 Available actions 

 Use when 

 CI Image scan 

 Build pipeline (image) 

 High: Scans container images built during CI before they are pushed to a registry or deployed 

 Block CI, CLI Report, Create Issue (+ Override Severity) 

 Enable when CI/CD pipelines build container images CI Image Scan detects vulnerabilities, secrets, and malware in images at build time 

 Image Registry scan 

 Image registry 

 Baseline: Scans container images stored in registries for vulnerabilities, secrets, and malware 

 Create Issue (+ Override Severity) 

 Enable when monitoring container image registries for newly disclosed vulnerabilities in existing images 

 CI/CD Configuration Scanners triggers 

 The Periodic Scan trigger is the only available trigger. PR Scan and CI Scan triggers are not available 

 Important : CI/CD Configuration Scanners policies cannot include non-CI/CD finding types (such as Secrets, Vulnerabilities, or IaC Misconfigurations). The CI/CD Risks finding type is exclusive to the CI/CD Configuration Scanners policy type. To create policies for non-CI/CD finding types, select the Code Scanners policy type 

 Trigger 

 Available actions 

 Default behavior 

 Periodic scan 

 Create Issue (+ Override Severity) 

 The Periodic Scan trigger and the Create Issue action are enabled by default 

 Drift Detection Scanner triggers 

 The Periodic Scan trigger is the only available trigger. PR Scan and CI Scan triggers are not available 

 Important : Drift Detection Scanner policies cannot include non-drift finding types (such as Secrets, Vulnerabilities, or CI/CD Risks). The IaC Drift finding type is exclusive to the Drift Detection Scanner policy type. To create policies for non-drift finding types, select the Code Scanners or CI/CD Configuration Scanners policy type 

 Trigger 

 Available actions 

 Default behavior 

 Periodic scan 

 Create Issue (+ Override Severity) 

 The Periodic Scan trigger and the Create Issue action are enabled by default 

 Previous Reference C: Scope mapping details 

 Next Reference E: Grace period logic and configuration 

 Last updated 2 months ago 

 Was this helpful?
