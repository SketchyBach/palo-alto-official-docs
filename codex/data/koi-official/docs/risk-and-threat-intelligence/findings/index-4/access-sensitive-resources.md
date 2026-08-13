<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/access-sensitive-resources.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/access-sensitive-resources.md).

# Access Sensitive Resources

**Severity**

🟡 Medium (4)

**Short Description**

Flags items where the MCP server reads, writes, or otherwise interacts with sensitive resources or data. This includes credentials, private keys, environment secrets, user files, and configuration files containing privileged information. Such access can expose high-value assets, enable privilege escalation, or compromise other systems within the environment.

**Suggestion**

Carefully review the item's access permissions and determine whether sensitive resource access is justified for its functionality. Consider removing or replacing the item if it accesses sensitive data without clear business necessity.

**Information**

Items that interact with sensitive resources such as credentials, private keys, environment secrets, user files, and configuration files pose significant security risks to endpoints. When an MCP server reads, writes, or otherwise accesses these high-value assets, it creates potential pathways for data compromise, unauthorized access to other systems, and privilege escalation. Even if the item's access is legitimate for its stated purpose, the presence of such capabilities increases the attack surface and potential for exploitation if the item is compromised or malicious.

**Risks of Access Sensitive Resources**

* **Credential Exposure**: The item can access stored credentials, API keys, or authentication tokens, enabling unauthorized access to other systems and services.
* **Private Key Compromise**: Access to private keys (SSH, GPG, SSL/TLS) can allow attackers to impersonate users or decrypt sensitive communications.
* **Environment Secret Leakage**: Interaction with environment variables and configuration files may expose secrets used by applications and services.
* **Privilege Escalation**: Access to privileged configuration files can enable attackers to elevate permissions and gain deeper system access.
* **Data Exfiltration**: The item can read sensitive user files and transmit confidential information to external parties.
* **Lateral Movement**: Compromised credentials and keys can be used to access other systems within the organization's environment.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Access Scope**: Identify which specific sensitive resources the item accesses and why.
   * **Validate Business Need**: Determine if the item's functionality legitimately requires access to these resources.
   * **Check Access Patterns**: Monitor when and how frequently the item accesses sensitive data.
2. **Immediate Action**:
   * **Assess Risk vs. Value**: Weigh the item's utility against the security risk it introduces.
   * **Apply Principle of Least Privilege**: If possible, restrict the item's permissions to only necessary resources.
   * **Remove if Unjustified**: If sensitive resource access is not essential to the item's core functionality, consider removing it.
3. **Long-term Measures**:
   * **Implement Monitoring**: Set up alerts for unusual access patterns to sensitive resources.
   * **Use Secret Management**: Employ dedicated secret management solutions to limit direct file-based credential access.
   * **Regular Audits**: Periodically review which items have access to sensitive resources and validate continued necessity.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/access-sensitive-resources.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
