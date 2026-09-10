---
url: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/data-export-capability
fetched_at: 2026-09-06T10:25:11.559Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Data Export Capability

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationRisk And Threat IntelligenceFindingsData Exposure & Privacy
Data Export Capability

Severity

🟡 Medium (4)

Short Description
Flags MCPs that provide data export capabilities to external services. While often intended for legitimate integrations, these capabilities may be invoked unintentionally by an LLM, increasing the risk of data being shared outside the intended trust boundary.

Suggestion

Review the MCP's data export functionality and assess whether it aligns with your organization's data handling policies. Consider restricting or monitoring its use if sensitive data could be unintentionally shared.

Information

MCPs with data export capabilities allow information to be sent to external services, APIs, or endpoints. While this functionality supports legitimate use cases like cloud integrations or third-party workflows, it introduces risk when an LLM can invoke these capabilities. The model may export data without fully understanding sensitivity constraints, or be manipulated into sending information to unintended destinations. The risk increases when export targets are configurable or when the MCP lacks clear boundaries on what data can be shared.

Risks of Vulnerable to Prompt Injection

Unintentional Data Sharing: The LLM may invoke export functions without recognizing the sensitivity of the data involved.

Trust Boundary Violations: Data may be sent to external services outside the organization's security perimeter.

Misconfigured Destinations: Export targets may be incorrectly configured, routing data to unauthorized endpoints.

Compliance Violations: Exporting regulated data (PII, financial, health) may breach legal or contractual obligations.

Exploitation via Prompt Injection: Attackers may manipulate the LLM into exporting sensitive data to attacker-controlled destinations.

Recommended Actions

Investigate the Item:

Identify what data the MCP can export and to which destinations.

Review whether export targets are hardcoded or user-configurable.

Assess whether the LLM can invoke export functions autonomously.

Immediate Action:

Restrict export capabilities to approved destinations only.

Implement confirmation prompts or manual approval for sensitive exports.

Mitigation:

Apply data classification rules to prevent export of sensitive information.

Log all export operations for audit and monitoring purposes.

Limit the MCP's access to only the data necessary for its intended function.

Previous
Undisclosed Privacy Data Collection
Next
Access Sensitive Resources Instruction

Last updated 6 months ago
