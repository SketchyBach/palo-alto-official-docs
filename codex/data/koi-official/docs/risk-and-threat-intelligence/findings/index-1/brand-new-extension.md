<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/brand-new-extension.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/brand-new-extension.md).

# Brand New Marketplace Item

**Severity**

🔵 Low (3)

**Short Description**

Flags items that are brand new on the marketplace, suggesting concerns about the extension's reputation and the publisher's reliability.

**Suggestion**

Monitor the item for updates and publisher activity to ensure ongoing reliability. Remove it if concerns arise.

**Information**

Brand new items may lack sufficient reviews, reputation, or demonstrated reliability. This increases the risk of untested or potentially malicious behavior.

**Risks of Brand New Marketplace Item**

* **Lack of Trust**: New items have not yet established a reputation or undergone extensive scrutiny.
* **Uncertain Publisher Practices**: The publisher's operational standards may be unclear or unproven.
* **Potential for Malicious Activity**: Newly published items are sometimes used for quick malicious campaigns.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Purpose**: Understand why the item is needed and whether alternatives exist.
  * **Evaluate Publisher**: Verify the publisher's reliability and history, if available.
* **Immediate Action**:
  * **Monitor Closely**: Track updates and reviews for signs of reliability or risk.
  * **Remove If Necessary**: If the item demonstrates suspicious behavior or lacks updates, remove it.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/brand-new-extension.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
