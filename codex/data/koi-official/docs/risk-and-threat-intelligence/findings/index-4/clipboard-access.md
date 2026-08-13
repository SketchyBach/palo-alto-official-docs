<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/clipboard-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/clipboard-access.md).

# Clipboard Access

**Severity**

🟡 Medium (5)

**Short Description**

Flags items that access or monitor clipboard content. While clipboard access may be used for legitimate purposes, it can also be exploited to capture sensitive user data such as passwords, authentication tokens, or copied personal information. This behavior may indicate data harvesting or keylogging-like activity and warrants further scrutiny.

**Suggestion**

Review the item's clipboard access functionality and evaluate whether it is essential for its core purpose. If clipboard monitoring is not necessary or the item shows other suspicious indicators, consider removing it from the endpoint.

**Information**

Items that request clipboard access can read or monitor content that users copy to their clipboard. While legitimate items may use this capability for features such as paste enhancement or clipboard management, clipboard access also creates a risk pathway for data theft. The clipboard often contains sensitive information including passwords, authentication tokens, credit card numbers, personal messages, and other confidential data that users temporarily copy. When an item accesses the clipboard, it can silently capture this information without the user's knowledge or awareness. This type of behavior is commonly associated with data harvesting attacks and may indicate keylogging-like activity that attempts to capture user credentials or sensitive business information.

**Risks of Clipboard Access**

* **Credential Theft**: The item can capture passwords, API keys, and authentication tokens that users copy to the clipboard, enabling account compromise.
* **Data Exfiltration**: Sensitive information such as financial data, personal identifiable information (PII), or proprietary business content copied by users can be harvested and transmitted to unauthorized parties.
* **Privacy Violation**: Continuous clipboard monitoring allows the item to track user activity and collect data without explicit consent, violating user privacy.
* **Corporate Espionage Risk**: Confidential business communications, trade secrets, or strategic information copied temporarily can be intercepted and leaked.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Functionality**: Determine whether clipboard access is necessary for the item's advertised purpose and features.
   * **Examine Permissions**: Check what other sensitive permissions the item requests that might compound the risk.
   * **Check Network Activity**: Monitor whether the item transmits clipboard data to external servers or third-party services.
2. **Assess Legitimacy**:
   * **Evaluate Publisher**: Research the publisher's reputation and history to assess trustworthiness.
   * **Review User Feedback**: Look for reports of suspicious behavior or data collection practices.
   * **Verify Use Case**: Confirm that clipboard access aligns with the item's stated functionality.
3. **Mitigation Actions**:
   * **Remove if Unnecessary**: If the item's clipboard access cannot be justified or alternative items exist, remove it from the endpoint.
   * **Monitor Activity**: If the item is business-critical, implement monitoring to detect unauthorized data transmission.
   * **User Training**: Educate users about the risks of clipboard access and advise them to avoid copying sensitive information when such items are active.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/clipboard-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
