<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/malicious-activity-detected.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/malicious-activity-detected.md).

# Malicious Activity Detected

**Severity**

🔴 Critical (10)

**Short Description**

Flags items that exhibit confirmed malicious activity.

**Suggestion**

Immediately remove the item from the endpoint to prevent system compromise and data breach. This is a critical security threat requiring urgent action.

**Information**

Items exhibiting confirmed malicious activity pose an immediate and severe threat to organizational security and data. This finding indicates that the item has been verified to be engaging in hostile actions against the endpoint or network. Malicious items are designed by threat actors to compromise systems, steal sensitive information, disrupt operations, or provide unauthorized access. When confirmed malicious activity is detected, it represents one of the most dangerous types of threats that can be present on an endpoint and requires immediate intervention to prevent further damage.

**Risks of Malicious Activity Detected**

* **System Compromise**: The item may have already compromised the endpoint, potentially installing backdoors, rootkits, or persistent access mechanisms.
* **Data Theft and Exfiltration**: Confirmed malicious items often steal sensitive data including credentials, financial information, intellectual property, or personal data.
* **Command-and-Control Communication**: The item may be communicating with threat actor infrastructure, allowing remote control and execution of malicious commands.
* **Lateral Movement**: The item may attempt to spread across the network, compromising additional systems and escalating the scope of the attack.
* **Business Disruption**: Malicious activity can halt operations, damage systems, or result in significant financial and reputational harm.
* **Credential Harvesting**: The item may capture authentication credentials for use in further attacks or unauthorized access.

**Recommended Actions**

1. **Immediate Action**:
   * **Isolate the Endpoint**: Immediately disconnect the affected endpoint from the network to prevent lateral movement and further damage.
   * **Remove the Item**: Uninstall the item immediately and terminate any associated processes.
   * **Initiate Incident Response**: Activate your organization's incident response plan and engage security teams.
2. **Investigation and Containment**:
   * **Forensic Analysis**: Conduct a thorough analysis of the endpoint to identify what data was accessed, modified, or exfiltrated.
   * **Network Traffic Review**: Analyze outbound connections to identify command-and-control servers and potential data exfiltration.
   * **Credential Reset**: Force password resets for any credentials that may have been exposed on the affected endpoint.
   * **Scope Assessment**: Check for signs of lateral movement to other endpoints or systems in the network.
3. **Recovery and Prevention**:
   * **System Restoration**: Consider reimaging the affected endpoint from a known-good backup to ensure complete removal of malicious components.
   * **Update Security Policies**: Review and strengthen endpoint security policies to prevent installation of unauthorized items.
   * **Report to Authorities**: Consider reporting the incident to relevant cybersecurity authorities and law enforcement.
   * **Threat Intelligence Sharing**: Share indicators of compromise with industry peers and security communities to help prevent similar attacks.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/malicious-activity-detected.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
