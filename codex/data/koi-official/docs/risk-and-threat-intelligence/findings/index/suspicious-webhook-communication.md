<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/suspicious-webhook-communication.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/suspicious-webhook-communication.md).

# Suspicious Webhook Communication

**Severity**

🟠 Medium (5)

**Short Description**

Flags extensions that potentially communicates to suspicious webhook URLs like discord webhooks. Webhooks are a common and useful way to send data between services, but they can also be used maliciously to exfiltrate data or control a compromised system.

**Suggestion**

Review the extension's network activity and remove it if the webhook endpoint is untrusted or unnecessary.

**Information**

Suspicious webhook communication indicates that the extension is sending data to an endpoint that may not be trusted or documented. This behavior could be used for exfiltrating sensitive information or executing remote commands.

**Risks of Suspicious Webhook Communication**

* **Data Exfiltration**: Sensitive information may be transferred without authorization.
* **Unauthorized Access**: Webhook endpoints can be used to execute commands or transfer malicious payloads.
* **Evasion of Detection**: Suspicious communication often uses encrypted or obfuscated methods to avoid detection.

**Recommended Actions**

1. **Investigate the Item**:
   * **Verify the Publisher**: Confirm the publisher’s credibility and the necessity of webhook communication.
   * **Evaluate Impact**: Identify affected users or systems and assess the potential risk.
2. **Immediate Action**:
   * **Remove the Extension**: If the webhook is untrusted or unnecessary, remove the extension.
   * **Notify Stakeholders**: Inform relevant teams to ensure proper mitigation steps.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/suspicious-webhook-communication.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
