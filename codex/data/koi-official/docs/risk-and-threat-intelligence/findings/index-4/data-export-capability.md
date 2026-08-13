<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/data-export-capability.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/data-export-capability.md).

# Data Export Capability

**Severity**

🟡 Medium (4)

**Short Description**\
Flags MCPs that provide data export capabilities to external services. While often intended for legitimate integrations, these capabilities may be invoked unintentionally by an LLM, increasing the risk of data being shared outside the intended trust boundary.

**Suggestion**

Review the MCP's data export functionality and assess whether it aligns with your organization's data handling policies. Consider restricting or monitoring its use if sensitive data could be unintentionally shared.

**Information**

MCPs with data export capabilities allow information to be sent to external services, APIs, or endpoints. While this functionality supports legitimate use cases like cloud integrations or third-party workflows, it introduces risk when an LLM can invoke these capabilities. The model may export data without fully understanding sensitivity constraints, or be manipulated into sending information to unintended destinations. The risk increases when export targets are configurable or when the MCP lacks clear boundaries on what data can be shared.

**Risks of Vulnerable to Prompt Injection**

* **Unintentional Data Sharing**: The LLM may invoke export functions without recognizing the sensitivity of the data involved.
* **Trust Boundary Violations**: Data may be sent to external services outside the organization's security perimeter.
* **Misconfigured Destinations**: Export targets may be incorrectly configured, routing data to unauthorized endpoints.
* **Compliance Violations**: Exporting regulated data (PII, financial, health) may breach legal or contractual obligations.
* **Exploitation via Prompt Injection**: Attackers may manipulate the LLM into exporting sensitive data to attacker-controlled destinations.

**Recommended Actions**

* **Investigate the Item**:
  * Identify what data the MCP can export and to which destinations.
  * Review whether export targets are hardcoded or user-configurable.
  * Assess whether the LLM can invoke export functions autonomously.
* **Immediate Action**:
  * Restrict export capabilities to approved destinations only.
  * Implement confirmation prompts or manual approval for sensitive exports.
* **Mitigation**:
  * Apply data classification rules to prevent export of sensitive information.
  * Log all export operations for audit and monitoring purposes.
  * Limit the MCP's access to only the data necessary for its intended function.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/data-export-capability.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
