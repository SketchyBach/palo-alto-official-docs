---
url: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/ai-artifact-shadowing
fetched_at: 2026-09-06T09:24:16.259Z
source: koi-official-browser
capture_method: authenticated official browser
---

# AI Artifact Shadowing

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationRisk And Threat IntelligenceFindingsMalicious Behavior
AI Artifact Shadowing

Severity

🔴 High (7)

Short Description
Flags MCP server tools and plugin artifacts - including skills, commands, subagents, rules, and hooks - that impersonate or shadow a legitimate tool, skill, or capability. By displacing trusted AI artifacts the agent relies on, shadowed components can intercept, redirect, or manipulate agent behavior.

Suggestion

This behavior may indicate malicious intent. Strongly consider removing the offending MCP server or plugin and reviewing any actions it may have already performed on the endpoint.

Information

Artifact shadowing occurs when a malicious or misconfigured source introduces AI artifacts - MCP tools, skills, slash commands, subagents, rules, or hooks - that duplicate, override, or mimic the names and descriptions of legitimate ones. Because an agent selects artifacts based largely on their names and descriptions, it may load or invoke a shadowed implementation instead of the intended one. The attack exploits the trust relationship between the agent and its registered capabilities, causing the model to execute attacker-controlled logic while believing it is using a trusted capability. The same technique also applies to passive artifacts: a shadowed rules file or hook can silently alter instructions the agent treats as authoritative, without any explicit invocation.

Risks

Malicious Artifact Execution: The agent invokes an attacker-controlled tool, skill, command, or subagent disguised as a trusted capability.

Data Interception: Shadowed artifacts can capture sensitive parameters, context, or file contents intended for the legitimate capability.

Action Hijacking: Critical operations such as file writes, shell commands, or API calls can be redirected to malicious implementations.

Instruction Tampering: Shadowed rules and hooks can inject or override guidance the agent treats as authoritative, influencing behavior across an entire session.

Trust Exploitation: Users and the agent trust output that actually originates from a compromised implementation.

Privilege Abuse: Shadowed artifacts may perform unauthorized actions using permissions granted to the legitimate capability they impersonate.

Recommended Actions

Investigate the Item:

Review all registered artifacts - tools, skills, commands, subagents, rules, and hooks - and check for duplicate or confusingly similar names.

Examine registration and load order, and the precedence rules that determine which artifact wins on a name collision.

Verify the source of each artifact and whether externally supplied ones can override built-in or first-party definitions.

Immediate Action:

Remove or disable MCP servers and plugins that allow unrestricted artifact registration.

Revoke permissions for artifacts with suspicious or duplicate definitions.

Mitigation:

Enforce registration validation and integrity checks across all artifact types.

Namespace or pin artifacts to their source so collisions are surfaced rather than silently resolved.

Log artifact invocations and loads, and flag unexpected resolution patterns.

Previous
Tool Poisoning
Next
Safety Instruction Override

Last updated 1 month ago
