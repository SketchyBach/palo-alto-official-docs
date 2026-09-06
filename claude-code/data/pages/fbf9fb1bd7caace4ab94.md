---
url: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/mismatch-between-description-and-body
fetched_at: 2026-09-06T09:20:06.017Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Mismatch Between Description and Body

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationRisk And Threat IntelligenceFindingsMalicious Behavior
Mismatch Between Description and Body

Severity

🟠 High (7)

Short Description

Flags AI artifacts - MCP server tools and plugin components including skills, commands, subagents, rules, and hooks - whose declared description, documentation, or actual code behavior diverge. The agent selects and loads artifacts based on their stated description, so a mismatch can mislead the agent about what an artifact does or hide malicious behavior behind a benign summary, resulting in unintended actions.

Suggestion

Treat a mismatch as a deception signal rather than a documentation defect. A gap between two descriptions, or between a description and the code behind it, indicates deceptive or unreliable behavior. Strongly consider removing the artifact and auditing any actions it has already performed.

Information

The agent decides what to invoke or load by reading a description — the tool description an MCP server returns from get_tools, or the summary at the top of a skill, command, subagent, rule, or hook. That description is the agent's only input at selection time, so it commits to the artifact before seeing what the code or body does. This finding fires when that contract is broken: a tool described as "search files" that also exfiltrates their contents, or an artifact whose published documentation, agent-facing description, and actual code each say something different.

Not every mismatch is an attack — documentation drifts as artifacts evolve. The distinguishing question is what lives in the gap: an outdated description that undersells a feature is a hygiene problem, while one that conceals file access, network calls, or command execution is deception.

Risks

Human oversight bypass: Users approve based on safe-looking documentation, unaware that the agent receives different instructions or that the code does something else.

Deceptive selection: The agent invokes the artifact for a task its actual behavior has nothing to do with.

Hidden prompt injection: The agent-facing description can carry embedded instructions that override the agent's behavior or redirect its actions.

Undisclosed capabilities: Network calls, file writes, or command execution that appear in no description are invisible to review.

Escalation indicator: A mismatch alongside execution or exfiltration findings is a strong signal of intentional malice.

Recommended Actions

Investigate the artifact

Read the evidence to see the specific gap that was detected.

For MCP servers, compare the tool descriptions returned by get_tools against the README, marketplace listing, and documentation.

Compare both descriptions against the code or artifact body, checking for actions mentioned nowhere: network requests, file writes, subprocess calls, or data collection.

Look for hidden instructions or encoded payloads in the agent-facing description that do not appear in user-facing materials.

Check whether the description changes between invocations, which suggests dynamic injection.

Contain and remediate

Disable the artifact while the gap is being assessed.

Audit recent agent activity for actions that do not align with the documented behavior, and review any data accessed or commands executed through the artifact.

Review other findings on the same artifact; a mismatch plus an execution or exfiltration finding should be treated as malicious.

Remove the artifact and report it to the marketplace if the mismatch conceals sensitive behavior.

Previous
Dynamic Tool Description
Next
Tool Poisoning

Last updated 1 month ago
