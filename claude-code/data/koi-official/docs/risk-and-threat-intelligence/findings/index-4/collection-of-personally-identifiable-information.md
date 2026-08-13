<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-personally-identifiable-information.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-personally-identifiable-information.md).

# Collection of Personally Identifiable Information

**Severity**

🔵 Low (1)

**Short Description**

Flags items that disclose collecting personally identifiable information, such as names, email addresses, ages, or identification numbers, potentially leading to privacy risks.

**Suggestion**

Review the item's privacy policy and data collection practices to understand what personally identifiable information is being collected and why. Monitor the item's behavior and assess whether the data collection is necessary for its functionality.

**Information**

Items that collect personally identifiable information (PII) such as names, email addresses, ages, or identification numbers may pose privacy risks to users and the organization. While many legitimate items require some level of personal data to function properly, the collection of PII raises concerns about data privacy, compliance with data protection regulations, and potential misuse of sensitive information. Understanding what data is collected, how it is used, and where it is stored is critical for maintaining user privacy and organizational security.

**Risks of Collection of Personally Identifiable Information**

* **Privacy Violations**: Collection of PII without proper consent or transparency may violate user privacy rights and expectations.
* **Data Breach Exposure**: PII collected by the item could be exposed in the event of a security breach, leading to identity theft or fraud.
* **Regulatory Non-Compliance**: Unauthorized or excessive PII collection may violate data protection regulations such as GDPR, CCPA, or HIPAA, resulting in legal penalties.
* **Data Misuse**: Collected PII could be sold to third parties, used for unauthorized marketing, or exploited by malicious actors.
* **Lack of Transparency**: Users may be unaware of what data is being collected and how it is being used, eroding trust.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Privacy Policy**: Examine the item's privacy policy to understand what PII is collected, why it's collected, and how it's used.
   * **Assess Data Necessity**: Determine if the PII collection is essential for the item's core functionality or if it's excessive.
   * **Check Third-Party Sharing**: Verify whether collected data is shared with external parties or advertisers.
2. **Monitor and Evaluate**:
   * **Review Permissions**: Check what permissions the item has been granted and whether they align with its stated purpose.
   * **Assess Compliance**: Ensure the item's data collection practices comply with relevant data protection regulations applicable to your organization.
   * **Monitor Updates**: Track changes to the item's privacy policy or data collection practices over time.
3. **Mitigate Risk**:
   * **User Awareness**: Inform users about the PII collection and provide guidance on privacy best practices.
   * **Consider Alternatives**: If the data collection seems excessive or unnecessary, evaluate alternative items with better privacy practices.
   * **Remove If Necessary**: If the item's data collection poses unacceptable privacy risks or violates organizational policies, consider removing it from endpoints.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-personally-identifiable-information.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
