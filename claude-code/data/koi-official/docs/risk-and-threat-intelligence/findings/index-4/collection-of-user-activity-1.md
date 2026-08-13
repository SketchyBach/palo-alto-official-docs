<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-user-activity-1.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-user-activity-1.md).

# Collection of User Activity

**Severity**

🔵 Low (1)

**Short Description**

Flags items that disclose monitoring user activity, such as network behavior, clicks, mouse positions, scrolling, or keystroke logging, which may indicate invasive data practices.

**Suggestion**

Review the item's privacy policy and data handling practices to understand the scope and purpose of user activity monitoring. Assess whether this data collection aligns with organizational privacy policies and user consent requirements.

**Information**

Items that monitor user activity may collect detailed information about user interactions, including network behavior, mouse clicks, cursor positions, scrolling patterns, or keystrokes. While such monitoring may be used for legitimate purposes like analytics, user experience improvement, or productivity tracking, it raises privacy concerns due to the invasive nature of the data being collected. The presence of this capability indicates that the item has access to detailed behavioral data, which could potentially be misused, shared with third parties, or inadequately protected.

**Risks of Collection of User Activity**

* **Privacy Violations**: The item may collect sensitive behavioral data without adequate transparency or user consent, potentially violating privacy regulations and organizational policies.
* **Data Exposure**: Collected activity data could be transmitted to third parties or stored insecurely, increasing the risk of unauthorized access to sensitive user behavior patterns.
* **Compliance Risks**: Monitoring user activity without proper disclosure may conflict with GDPR, CCPA, or other data protection regulations, exposing the organization to legal liability.
* **User Trust**: Invasive monitoring practices can erode employee or user trust if not properly disclosed and justified.
* **Sensitive Data Capture**: Keystroke logging or screen monitoring could inadvertently capture passwords, confidential information, or personal data not intended for collection.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Data Collection Practices**: Examine the item's privacy policy and documentation to understand what user activity data is collected and how it is used.
  * **Assess Legitimate Purpose**: Determine whether the monitoring functionality serves a legitimate business purpose and is proportionate to that purpose.
  * **Check Consent Mechanisms**: Verify that users have been properly informed and have consented to this level of monitoring.
* **Immediate Action**:
  * **Evaluate Necessity**: Consider whether the item's functionality is essential or if alternatives with less invasive practices exist.
  * **Review Compliance**: Ensure the data collection practices comply with applicable privacy regulations and organizational policies.
  * **Monitor Data Handling**: If the item is retained, audit how collected data is stored, transmitted, and protected.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-user-activity-1.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
