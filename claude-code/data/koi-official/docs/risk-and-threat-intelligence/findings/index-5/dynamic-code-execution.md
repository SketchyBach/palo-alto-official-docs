<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/dynamic-code-execution.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/dynamic-code-execution.md).

# Dynamic Code Execution

**Severity**

🟠 High (7)

**Short Description**

Flags items that fetch and execute code from a remote server at runtime. This behavior can bypass static analysis and poses a significant security risk, as it allows the extension’s functionality to change without review.

**Suggestion**

Carefully review the item's code to identify and assess the remote code execution behavior. Remove or replace the item if it fetches and executes code from untrusted or unverified remote servers.

**Information**

Items that fetch and execute code from remote servers at runtime pose significant security risks by introducing dynamic, unvetted functionality to the endpoint. Unlike static code that can be analyzed before installation, remotely loaded code bypasses security reviews and can change the item's behavior at any time without user knowledge or consent. Threat actors can exploit this mechanism to inject malicious payloads, update attack vectors, or change the item's functionality to perform unauthorized actions. This technique is commonly used to evade detection by security tools that rely on static analysis, as the malicious behavior only manifests when the remote code is executed at runtime.

**Risks of Dynamic Code Execution**

* **Bypassed Security Review**: Remotely fetched code can introduce malicious functionality that was not present during initial installation or security assessment.
* **Dynamic Malicious Updates**: The item's behavior can be changed at any time by the remote server, turning a previously benign item into a threat without user awareness.
* **Command-and-Control Channel**: The remote code execution mechanism can be used to establish a communication channel for receiving instructions from threat actors.
* **Malware Delivery**: Remote code execution can be leveraged to download and execute additional malicious payloads, including spyware, keyloggers, or ransomware.
* **Data Exfiltration**: Dynamically loaded code can be used to steal sensitive information such as credentials, browsing history, or corporate data.
* **Evasion Technique**: Static analysis tools cannot detect threats hidden in remotely fetched code, making this a preferred technique for sophisticated attackers.

**Recommended Actions**

1. **Investigate the Item**:
   * **Analyze Network Traffic**: Monitor the item's network activity to identify which remote servers it contacts and what code is being fetched.
   * **Review Code Execution Patterns**: Examine the item's code to understand when, how, and why remote code is executed.
   * **Verify Server Trustworthiness**: Determine if the remote servers are legitimate, secure, and under the control of trustworthy entities.
   * **Check for Obfuscation**: Look for signs that the remote code execution is deliberately hidden or obfuscated.
2. **Immediate Action**:
   * **Remove the Item**: If the remote code execution behavior cannot be justified or verified as safe, remove the item from the endpoint.
   * **Block Network Access**: Consider blocking network access to the remote servers used by the item to prevent code fetching.
   * **Assess Impact**: Determine if the item has already executed remote code and whether any malicious actions have been taken on the endpoint.
3. **Prevention and Monitoring**:
   * **Implement Network Monitoring**: Deploy network monitoring tools to detect and alert on items attempting to fetch and execute remote code.
   * **Enforce Security Policies**: Establish policies that prohibit or restrict items with dynamic code execution capabilities.
   * **Regular Audits**: Conduct periodic security audits of installed items to identify and remove those with risky behaviors.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/dynamic-code-execution.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
