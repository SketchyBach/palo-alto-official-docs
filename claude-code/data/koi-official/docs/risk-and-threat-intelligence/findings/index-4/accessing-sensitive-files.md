<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/accessing-sensitive-files.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/accessing-sensitive-files.md).

# Accessing Sensitive Files

**Severity**

🟠 High (7)

**Short Description**

Flags items that attempt to access sensitive files on the host machine, raising potential security and privacy concerns.

**Suggestion**

Carefully review the item's file access permissions and behavior. Remove or replace the item if it attempts to access sensitive files without legitimate justification.

**Information**

Items that attempt to access sensitive files on the host machine pose significant security and privacy risks. Sensitive files may include user credentials, authentication tokens, configuration files, encryption keys, browser history, personal documents, or system files that contain confidential information. When an item requests access to such files, it raises concerns about data exfiltration, unauthorized surveillance, or compromise of system security. Threat actors may use this capability to steal sensitive data, harvest credentials for lateral movement, or gather intelligence about the user's environment and activities.

**Risks of Accessing Sensitive Files**

* **Data Exfiltration**: The item may read and transmit sensitive files to external servers, leading to exposure of confidential information.
* **Credential Theft**: Access to authentication files can allow attackers to steal passwords, tokens, or certificates for unauthorized access.
* **Privacy Violation**: The item may access personal documents, browsing history, or user data without consent, violating user privacy.
* **System Compromise**: Reading system configuration files may reveal security weaknesses or enable privilege escalation attacks.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review File Access Patterns**: Identify which sensitive files the item is attempting to access and determine if this access is justified by its stated functionality.
   * **Evaluate Necessity**: Assess whether the item's core functionality requires access to these sensitive files or if this represents suspicious behavior.
   * **Check for Data Transmission**: Monitor network activity to determine if accessed file contents are being transmitted externally.
2. **Immediate Action**:
   * **Remove the Item**: If the file access cannot be justified or appears malicious, remove the item immediately to prevent data compromise.
   * **Review Accessed Files**: Audit which sensitive files may have been accessed and assess potential impact.
   * **Rotate Credentials**: If credential files were accessed, consider rotating passwords, tokens, and other authentication materials as a precaution.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/accessing-sensitive-files.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
