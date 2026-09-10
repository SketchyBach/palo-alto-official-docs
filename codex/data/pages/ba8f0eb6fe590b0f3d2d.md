---
url: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/code-execution
fetched_at: 2026-09-06T09:24:32.299Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Code Execution

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationRisk And Threat IntelligenceFindingsExecution & Behavior
Code Execution

Severity

🔵 Low (3)

Short Description

Flags plugin hooks that execute shell commands on the host system. Hooks run automatically on agent events, so any command they carry executes without an explicit user action.

Suggestion

Treat this as a review signal, not automatic malice — many legitimate hooks exist to run commands. Use the evidence to decide whether the command is expected for the hook's purpose and acceptable in your environment. Remove or replace the hook if it is not.

Information

Hooks are the plugin mechanism for running code in response to agent events, so a hook that executes shell commands is doing exactly what hooks are for. Formatters, linters, test runners, and notification hooks all work this way. That is why this finding carries a low severity on its own: it tells you execution exists, not that it is harmful.

What makes it worth reviewing is the trigger model. Hooks fire on agent events rather than on user request, so the command runs with the agent process's privileges without anyone deciding to run it in that moment. If the evidence shows destructive operations, see Unsafe Code Execution, which flags the dangerous subset specifically; if it shows commands built at runtime from remote content, see Dynamic Context.

Risks

Unattended execution: The command runs on an agent event, with no user confirmation step.

Process privileges: Commands inherit the agent process's filesystem, network, and account access.

Frequency amplification: A hook on a frequently fired event runs its command many times per session.

Supply-chain exposure: A compromised or updated version of the plugin can change what the hook executes without any visible change in behavior.

Recommended Actions

Investigate the component

Read the evidence to see the exact commands and which events trigger them.

Confirm the commands match the plugin's documented purpose.

Check whether the commands are fixed in the plugin source or assembled at runtime.

Contain and remediate

Allow only if the behavior is documented, narrowly scoped, and acceptable under your policy.

Prefer narrow, parameterized commands over broad shell invocations.

Run the agent without elevated privileges so hook commands inherit least privilege.

Pin the plugin version and re-review after upgrades.

Previous
Code Execution Instruction
Next
Overview

Last updated 1 month ago
