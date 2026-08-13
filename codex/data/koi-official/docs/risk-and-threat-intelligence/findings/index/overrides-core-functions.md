<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/overrides-core-functions.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/overrides-core-functions.md).

# Overrides Core Functions

**Severity**

🟡 Medium (5)

**Short Description**

Flags items that alter or redefine built-in system or language functions, such as replacing native APIs (e.g., redefining fetch). Overriding core functions can obscure intended behavior, bypass security controls, or introduce hidden logic that enables data manipulation, credential theft, or unauthorized communication.

**Suggestion**

Carefully review the item's code to understand which core functions are being overridden and why. Remove or replace the item if the overrides are unnecessary or cannot be adequately justified from a security perspective.

**Information**

Items that override or redefine built-in system or language functions (such as native APIs like fetch, XMLHttpRequest, eval, or DOM manipulation methods) introduce significant security concerns. By altering core functionality, the item can intercept, modify, or redirect normal system behavior in ways that are hidden from both users and other security tools. While some legitimate items may override functions for debugging or polyfill purposes, this technique is also commonly employed by malicious actors to inject hidden logic, intercept sensitive data, or establish covert communication channels.

When core functions are redefined, the original intended behavior is replaced with custom logic that may bypass security controls, manipulate data before it reaches its destination, or enable unauthorized actions without user awareness.

**Risks of Overrides Core Functions**

* **Security Control Bypass**: Overriding core functions can circumvent built-in browser security mechanisms, content security policies, or other protective measures.
* **Data Interception and Theft**: Redefined functions like fetch or XMLHttpRequest can intercept network requests and responses, potentially capturing credentials, API keys, session tokens, or other sensitive information.
* **Hidden Malicious Logic**: The overridden function can inject malicious behavior that executes silently, such as logging keystrokes, modifying form data, or exfiltrating information.
* **Unauthorized Communication**: Modified network functions can establish covert channels to external servers, enabling data exfiltration or command-and-control communication.
* **Code Integrity Compromise**: Other scripts and components relying on native functions will unknowingly use the modified versions, potentially affecting the entire endpoint's security posture.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Code Logic**: Examine which core functions are being overridden and analyze the replacement implementation.
  * **Assess Legitimacy**: Determine if there is a valid functional or compatibility reason for the overrides.
  * **Check for Obfuscation**: Look for signs of code obfuscation or complexity designed to hide the true purpose of the overrides.
* **Immediate Action**:
  * **Monitor Behavior**: Track the item's network activity and data access patterns to identify suspicious behavior.
  * **Remove If Suspicious**: If the overrides cannot be justified or appear to include malicious logic, remove the item from the endpoint.
  * **Validate Alternatives**: Consider replacing the item with trusted alternatives that do not require core function overrides.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/overrides-core-functions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
