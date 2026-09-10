---
url: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/registry-write-access
fetched_at: 2026-09-06T10:22:27.716Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Registry Write Access

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationRisk And Threat IntelligenceFindingsExecution & Behavior
Registry Write Access

Severity

🟢 Low (0)

Short Description

Flags extensions that can modify Windows registry settings.

Suggestion

Ensure the extension’s ability to alter registry settings is necessary and does not introduce security risks.

Information

Registry write access allows extensions to modify system settings, which could be used to persist malware or disable security protections.

Risks of Registry Write Capability

System Tampering: Extensions could modify startup programs or security settings.

Persistent Malware: Malicious extensions may use the registry to maintain persistence.

Recommended Actions

Validate Registry Write Access:

Ensure the extension requires registry modification capabilities.

Assess its compliance with security policies.

Enhance Controls:

Restrict registry modifications to trusted extensions.

Regularly audit registry changes.

Previous
Registry Read Access
Next
Serial Port Read Access

Last updated 8 months ago
