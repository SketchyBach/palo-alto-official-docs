<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/process-execution.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/process-execution.md).

# Process Execution

**Severity**

🟡 Medium (4)

**Short Description**

Flags items that initiate new processes by executing files from local or remote paths. This behavior can be used to run additional code outside the extension’s scope, including potentially malicious payloads. Uncontrolled process execution increases the risk of system compromise.

**Suggestion**

Investigate the item to understand what processes it executes and why. If the item's process execution behavior cannot be fully validated or appears unnecessary for its stated functionality, consider removing it to prevent potential system compromise.

**Information**

Items that initiate new processes by executing files from local or remote paths operate outside their normal scope, allowing them to run additional code on the endpoint. This capability enables the item to launch executables, scripts, or other system commands that extend beyond standard functionality. When an item has the ability to spawn processes, it can potentially execute arbitrary code, including payloads retrieved from external sources or embedded within the item itself. This behavior creates a pathway for malicious actors to run unauthorized code, bypass security controls, and perform actions that may compromise the endpoint's security posture.

**Risks of Process Execution**

* **Arbitrary Code Execution**: The item can execute files or commands that run malicious payloads, malware, or unwanted software on the endpoint.
* **System Compromise**: Uncontrolled process execution can be leveraged to gain elevated privileges, install backdoors, or establish persistence mechanisms.
* **Bypass Security Controls**: Spawning external processes allows the item to circumvent sandboxing or security restrictions intended to limit its scope.
* **Remote Payload Execution**: The item may download and execute files from remote locations, introducing untrusted code into the environment.
* **Lateral Movement**: Malicious processes initiated by the item could be used to spread threats across the network or access additional resources.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Process Execution Behavior**: Identify which files or commands the item executes and determine if this behavior is necessary for its intended functionality.
   * **Analyze Executed Files**: Check the source and integrity of any files being executed—whether they originate locally or from remote locations.
   * **Examine Item Purpose**: Verify if process execution aligns with the item's stated purpose and whether legitimate alternatives exist that don't require this capability.
2. **Assess Risk Level**:
   * **Validate Legitimacy**: Determine if the item is from a trusted publisher with a proven track record.
   * **Check for Suspicious Patterns**: Look for signs of obfuscation, unusual execution paths, or connections to unknown remote sources.
3. **Immediate Action**:
   * **Monitor Activity**: If keeping the item, implement monitoring to track what processes it spawns and ensure they remain within expected parameters.
   * **Remove If Uncertain**: If the item's process execution behavior cannot be fully validated or appears excessive for its functionality, remove it from the endpoint.
   * **Apply Restrictions**: Where possible, implement endpoint security policies that limit or control process execution capabilities for such items.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/process-execution.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
