<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/low-install-count.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/low-install-count.md).

# Low Install Count

**Severity**

🔵 Low (2)

**Short Description**

Flags items lacking installs on the marketplace, suggesting concerns about the extension's reputation and the publisher's reliability.

**Suggestion**

Monitor the item for marketplace adoption and publisher activity to assess its reliability. Consider replacing it with a more established alternative if available.

**Information**

Items with low install counts on the marketplace may lack sufficient user adoption, reviews, or demonstrated reliability. This limited usage indicates the item has not undergone extensive community scrutiny and its behavior in real-world scenarios remains largely unproven.

**Risks of Low Install Count**

* **Lack of Community Validation**: Low install counts mean fewer users have tested and verified the item's functionality and safety.
* **Uncertain Publisher Reputation**: The publisher may have limited track record or unclear operational standards.
* **Reduced Visibility of Issues**: With fewer users, potential security vulnerabilities or malicious behavior may go undetected for longer periods.
* **Potential Abandonment Risk**: Low adoption may indicate the item could be discontinued or lack ongoing maintenance and security updates.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Purpose**: Determine if the item's functionality is critical and whether more widely-adopted alternatives exist.
  * **Evaluate Publisher**: Research the publisher's history, other published items, and reputation in the marketplace.
  * **Check Reviews**: Look for any available user feedback or reported issues.
* **Ongoing Monitoring**:
  * **Track Install Growth**: Monitor whether the item gains adoption over time, which may indicate growing trust.
  * **Watch for Updates**: Verify that the publisher actively maintains the item with regular updates.
  * **Consider Alternatives**: If possible, replace with more established items that have proven track records and larger user bases.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/low-install-count.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
