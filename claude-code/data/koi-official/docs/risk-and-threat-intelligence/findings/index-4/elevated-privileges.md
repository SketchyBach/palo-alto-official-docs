<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/elevated-privileges.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/elevated-privileges.md).

# Elevated Privileges

**Severity**

🟡 Medium (4)

**Short Description**

Flags items that use or request elevated or administrative privileges. Elevated privileges can be legitimate for system administration tools, but may also indicate malicious attempts to gain higher access levels, bypass security controls, or perform unauthorized operations.

**Suggestion**

Review the item to determine if elevated privileges are legitimately required for its intended functionality. If the item is not a necessary system administration tool or the privilege usage cannot be justified, consider removing it from the endpoint.

**Information**

Items that request or use elevated or administrative privileges have access to deeper system resources and can perform operations that standard applications cannot. While elevated privileges are legitimate and necessary for system administration tools, security utilities, and certain productivity applications, they also present a significant attack surface. When an item operates with administrative access, it can modify system settings, access sensitive data, install additional software, or bypass standard security controls. Malicious actors often seek elevated privileges to maximize the impact of their attacks, enabling them to disable security tools, establish persistence mechanisms, or escalate further within an organization's network.

**Risks of Elevated Privileges**

* **Privilege Abuse**: The item could use elevated access to perform unauthorized operations, modify critical system files, or alter security configurations.
* **Security Control Bypass**: Administrative privileges may allow the item to disable endpoint protection, tamper with security logs, or circumvent access restrictions.
* **System Compromise**: If the item is compromised or malicious, elevated privileges enable threat actors to gain full control over the endpoint and potentially move laterally across the network.
* **Unauthorized Data Access**: The item may leverage administrative access to read sensitive files, access credential stores, or exfiltrate protected information.
* **Persistence Mechanisms**: Elevated privileges can be used to install backdoors, create hidden accounts, or modify system startup processes for long-term access.

**Recommended Actions**

1. **Investigate the Item**:
   * **Verify Legitimate Need**: Determine if the item genuinely requires elevated privileges for its stated purpose and functionality.
   * **Review Publisher Reputation**: Assess the trustworthiness of the item's publisher and check for any security concerns or past incidents.
   * **Analyze Privilege Usage**: Examine what specific administrative operations the item performs and whether they align with its intended use.
2. **Risk Assessment**:
   * **Evaluate Business Justification**: Confirm whether the item is essential for business operations or if alternative solutions with lower privilege requirements exist.
   * **Check Security Posture**: Review if the item has additional security findings or exhibits suspicious behavior patterns.
3. **Mitigation Actions**:
   * **Apply Least Privilege**: If possible, configure the item to operate with reduced permissions or use alternative versions that don't require elevated access.
   * **Monitor Activity**: Implement enhanced monitoring and logging for the item's activities, particularly system-level operations.
   * **Remove If Unnecessary**: If the elevated privileges cannot be justified or if the item is not critical to operations, remove it from the endpoint to reduce the attack surface.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/elevated-privileges.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
