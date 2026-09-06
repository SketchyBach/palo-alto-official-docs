---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/appsec-objectives-with-agentix
fetched_at: 2026-09-06T10:11:43Z
source: cortex-platform
---

# AppSec Objectives with Agentix | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 AppSec Objectives with Agentix 

 Drive risk reduction with AppSec objectives (Agentix) 

 Agentix-driven AppSec Objectives turn high-level security goals into tracked, measurable remediation programs without manual policy configuration. You describe a goal in natural language, for example, eliminate critical vulnerabilities in deployed repositorie s, and Cortex Cloud converts it into an objective, automatically creating a dedicated dashboard and adding it to a central tracking table to monitor progress. 

 The result is a continuous, measurable reduction in risk and a clear shift from reactive detection to proactive prevention across the software development life cycle (SDLC). 

 What an AppSec objective is 

 An AppSec objective is a focused, measurable goal that groups related open issues by a scope (which assets the objective covers) and a condition (which issues matter for the objective). Each objective is backed by a dedicated dashboard and a set of calculated metrics that quantify how close the objective is to completion. 

 An objective tracks issues, the deduplicated, actionable records that Cortex Cloud opens from underlying findings. This distinction matters: a single issue can consolidate many periodic findings for the same vulnerability across scans. By operating on issues, the objective ensures accurate, actionable metrics. Progress to resolution is measured using key indicators such as remediation rate, open cases, detection rate, and prevention rate calculated over these issues, rather than raw finding data. 

 Scope : Currently, only vulnerability objectives, which track vulnerability (CVE) issues on code and artifact assets, are supported. 

 Create an objective 

 Create Application Security objectives through the AppSec Agent (Agentix). You do not fill out a policy-style wizard. Instead, you describe the objective in natural language, either by selecting a predefined starter prompt or by typing your own, and the AppSec Agent translates the request into the asset scope and issue condition that define the objective. 

 When the AppSec Agent creates an objective, Cortex Cloud performs three actions: 

 Persists the objective and its scope and condition. 

 Builds a dedicated dashboard whose widgets are filtered to the objective scope and condition. 

 Starts a background synchronization that populates the objective metrics (remediation rate, detection rate, prevention rate, and open cases). 

 IMPORTANT: The AppSec Agent creates objectives only for goals that map to a supported objective type and its filters. If you request a goal outside the supported filters, the AppSec Agent notifies you and suggests the available starter prompts instead. 

 NOTE : If you do not specify a name or description for the objective, the AppSec Agent generates a human-readable name and description from your prompt. 

 Prerequisites 

 A license for Cloud Security and the Application Security add-on module 

 The AppSec Agent (Agentix) enabled in your tenant 

 Next step: Track objectives 

 Previous Application Security dashboard 

 Next Track objectives 

 Last updated 1 month ago 

 Was this helpful?
