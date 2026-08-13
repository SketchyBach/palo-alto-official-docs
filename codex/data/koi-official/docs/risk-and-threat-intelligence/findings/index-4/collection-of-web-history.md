<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-web-history.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-web-history.md).

# Collection of Web History

**Severity**

🔵 Low (1)

**Short Description**

Flags items that disclose collecting web history, including visited web pages and associated metadata like page titles and visit times, which may be used for behavioral profiling.

**Suggestion**

Review the item's privacy policy and data collection practices to understand how web history is used. Monitor the item's behavior and consider removing it if the data collection is not essential to functionality.

**Information**

Items that collect web history have the capability to track and record the websites users visit, including detailed metadata such as page titles, visit timestamps, and browsing patterns. While some items may use this data for legitimate purposes such as synchronization or productivity features, the collection of browsing history creates a detailed profile of user behavior and interests that could be misused if the item's security is compromised or if the data is shared with third parties.

**Risks of Collection of Web History**

* **Privacy Exposure**: Web history reveals sensitive information about user interests, activities, and potentially confidential business research.
* **Behavioral Profiling**: Collected data can be used to build detailed user profiles for tracking, advertising, or surveillance purposes.
* **Data Breach Risk**: If the item or its backend systems are compromised, browsing history could be exposed to unauthorized parties.
* **Third-Party Sharing**: Web history data may be shared with or sold to third-party advertisers or data brokers without explicit user knowledge.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Privacy Policy**: Examine how web history is collected, stored, and used by the item.
  * **Assess Necessity**: Determine whether browsing history collection is essential to the item's core functionality.
  * **Check Data Sharing**: Verify if web history is shared with third-party services or advertisers.
* **Monitor and Act**:
  * **Monitor Activity**: Track the item's data transmission behavior to ensure it aligns with disclosed practices.
  * **Consider Alternatives**: Explore alternative items that provide similar functionality without extensive data collection.
  * **Remove If Unnecessary**: If the web history collection is not justified by the item's purpose, consider removing it to protect user privacy.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-web-history.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
