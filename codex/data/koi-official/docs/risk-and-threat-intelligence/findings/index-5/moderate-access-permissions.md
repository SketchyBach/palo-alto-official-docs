<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/moderate-access-permissions.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/moderate-access-permissions.md).

# Code Execution Permissions

**Severity**

🟡 Medium (5)

**Short Description**

Flags items that request permissions allowing them to inject, execute, or modify code at runtime. These capabilities expand the item’s control over the browser environment and significantly increase the potential for evasive behavior, or post-install exploitation.

**Suggestion**

Carefully evaluate the necessity of this item and its permission requirements. Consider removing or replacing the item if its functionality does not justify the elevated code execution capabilities.

**Information**

Items that request permissions to inject, execute, or modify code at runtime possess significant control over the browser environment and can alter the behavior of web pages and the browser itself. These capabilities allow the item to dynamically change code execution flow, inject scripts into web pages, and modify existing code in ways that may not be immediately visible. While some legitimate items require these permissions for their intended functionality, such capabilities also create opportunities for malicious actors to exploit the item for evasive behavior, hide malicious activities, or leverage the item for post-installation attacks. The broad control granted by code execution permissions makes it difficult to predict or audit the item's actual behavior at any given time.

**Included Permissions**

* debugger
* devtools
* userScripts
* experimental
* unsafe-eval
* content\_security\_policy
* web\_accessible\_resources
* scripting

**Risks of Code Execution Permissions**

* **Arbitrary Code Execution**: The item can execute code dynamically, potentially running malicious scripts that bypass initial security reviews.
* **Evasive Behavior**: Code modification capabilities can be used to hide malicious activities, alter detection mechanisms, or obfuscate true intentions.
* **Post-Install Exploitation**: The item could be updated or modified after installation to introduce malicious functionality that was not present during initial review.
* **Browser Environment Manipulation**: The item can alter the behavior of web pages, intercept user interactions, or modify security controls within the browser.
* **Privilege Escalation**: Runtime code execution can be leveraged to gain additional permissions or access beyond what was originally granted.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Permission Justification**: Determine whether the item's core functionality legitimately requires code execution permissions.
   * **Assess Publisher Reputation**: Verify the publisher's trustworthiness and history of security practices.
   * **Examine Code Behavior**: If possible, review what the item actually does with these permissions during runtime.
2. **Risk Assessment**:
   * **Evaluate Alternatives**: Search for similar items that provide the same functionality with fewer permissions.
   * **Consider Business Necessity**: Determine if the item is essential for business operations or if it can be removed.
   * **Monitor Behavior**: Track the item's activities for any unexpected or suspicious code execution patterns.
3. **Mitigation Actions**:
   * **Remove if Unnecessary**: If the item is not critical or alternatives exist, remove it to eliminate the risk.
   * **Implement Monitoring**: Deploy additional security controls to monitor the item's runtime behavior.
   * **Apply Security Policies**: Restrict installation of items with code execution permissions through organizational policies.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/moderate-access-permissions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
