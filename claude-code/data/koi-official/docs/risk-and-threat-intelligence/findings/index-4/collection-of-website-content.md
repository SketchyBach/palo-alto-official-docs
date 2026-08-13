<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-website-content.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-website-content.md).

# Collection of Website Content

**Severity**

🔵 Low (1)

**Short Description**

Flags items that disclose collecting website content, such as text, images, videos, or hyperlinks, which could potentially involve harvesting sensitive or copyrighted material.

**Suggestion**

Review the item's purpose and determine if collecting website content is necessary for its core functionality. Monitor the item's behavior to ensure it operates within expected boundaries.

**Information**

This item discloses the ability to collect website content including text, images, videos, or hyperlinks. While such capabilities may be legitimate for productivity tools, research applications, or content aggregators, they can also present concerns around unauthorized data harvesting, privacy violations, or intellectual property infringement. Items with content collection capabilities should be evaluated based on their stated purpose and data handling practices.

**Risks of Collection of Website Content**

* **Privacy Concerns**: The item may collect and store user browsing data or website content without proper consent or transparency.
* **Intellectual Property Risks**: Harvesting copyrighted material such as images, videos, or text could expose the organization to legal liability.
* **Data Accumulation**: Collected content may be stored insecurely or transmitted to third parties without adequate protection.
* **Sensitive Information Exposure**: The item could inadvertently capture confidential or proprietary information displayed on websites.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Purpose**: Verify whether content collection is essential for the item's intended functionality.
  * **Check Privacy Policy**: Examine how collected content is stored, processed, and shared.
  * **Assess Scope**: Determine what types of content are collected and from which websites.
* **Monitoring Action**:
  * **Monitor Usage**: Track the item's behavior to ensure it collects only necessary content and operates transparently.
  * **Review Regularly**: Periodically reassess whether the item remains appropriate for organizational use.
  * **Consider Alternatives**: If concerns persist, evaluate alternative items with more limited data collection capabilities.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-website-content.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
