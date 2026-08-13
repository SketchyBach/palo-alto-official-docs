<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-personal-communications.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-personal-communications.md).

# Collection of Personal Communications

**Severity**

🔵 Low (3)

**Short Description**

Flags items that disclose collecting personal communications, such as emails, chat messages, or social media posts, which may compromise private conversations or sensitive data.

**Suggestion**

Review the item's permissions and data collection practices carefully. Monitor the item's behavior to ensure it operates within expected boundaries. Remove it if the collection of personal communications is not justified by its core functionality.

**Information**

Items that disclose collecting personal communications, such as emails, chat messages, or social media posts, have access to highly sensitive user data. This finding indicates that the item explicitly states it collects or processes private conversations, which may include confidential business communications, personal information, or sensitive organizational data. While some items may legitimately require such access for their intended functionality, this level of data access increases privacy and security risks.

**Risks of Collection of Personal Communications**

* **Privacy Violation**: The item may access and collect private conversations, emails, or messages without appropriate user awareness or consent.
* **Data Exfiltration**: Personal communications could be transmitted to third parties or external servers, exposing sensitive information.
* **Compliance Risk**: Collection of personal communications may violate data protection regulations such as GDPR, CCPA, or HIPAA.
* **Credential Exposure**: Communications may contain passwords, authentication tokens, or other sensitive credentials that could be compromised.
* **Business Intelligence Leakage**: Corporate communications may contain proprietary information, trade secrets, or strategic plans.

**Recommended Actions**

1. **Investigate the Item**:

* **Review Permissions**: Examine what specific permissions the item has requested and whether they align with its stated purpose.
* **Check Privacy Policy**: Review the item's privacy policy to understand how collected communications are used, stored, and shared.
* **Evaluate Necessity**: Determine if the collection of personal communications is essential for the item's core functionality.

2. **Monitoring and Controls**:

* **Monitor Data Flow**: Track outbound connections to identify where collected data is being transmitted.
* **Limit Scope**: If possible, restrict the item's access to only necessary communication channels or accounts.
* **User Awareness**: Ensure users understand what communications are being accessed by the item.

3. **Risk Mitigation**:

* **Seek Alternatives**: Consider alternative items that provide similar functionality without requiring access to personal communications.
* **Remove If Unjustified**: If the collection of communications cannot be justified or poses excessive risk, remove the item from endpoints.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-personal-communications.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
