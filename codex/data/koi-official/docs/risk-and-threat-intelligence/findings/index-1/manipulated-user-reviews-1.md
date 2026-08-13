<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/manipulated-user-reviews-1.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/manipulated-user-reviews-1.md).

# Manipulated User Reviews

**Severity**

🟠 High (8)

**Short Description**

Flags items that exhibit signs of artificially inflated user reviews to create a false sense of trust and credibility. This may involve fake positive reviews, coordinated review campaigns, or reputation farming tactics. Such behavior undermines marketplace integrity and may conceal malicious or deceptive activity behind a manufactured appearance of legitimacy.

**Suggestion**

Investigate the item's review patterns and publisher reputation thoroughly. Consider removing the item if the reviews appear fraudulent or if the publisher cannot be verified as trustworthy.

**Information**

Items with manipulated user reviews use artificially inflated ratings and fake positive feedback to create a false impression of legitimacy and trustworthiness. This deceptive practice may involve coordinated review campaigns, reputation farming, or bot-generated reviews designed to manipulate marketplace rankings and user trust. Such tactics are often employed to mask malicious intent or low-quality functionality behind a manufactured facade of credibility, undermining the integrity of the marketplace ecosystem.

**Risks of Manipulated User Reviews**

* **False Sense of Security**: Manipulated reviews create an illusion of trustworthiness, leading users and organizations to install potentially harmful items.
* **Concealed Malicious Activity**: Fake positive reviews may be used to hide malicious functionality, data harvesting, or other harmful behaviors.
* **Compromised Decision Making**: Organizations relying on user reviews for vetting decisions may be misled into deploying risky or malicious items.
* **Marketplace Manipulation**: Fraudulent review campaigns distort marketplace rankings, pushing malicious items to prominence while burying legitimate alternatives.
* **Publisher Deception**: Items using review manipulation often indicate broader untrustworthiness in publisher practices and intentions.

**Recommended Actions**

1. **Investigate the Item**:
   * **Analyze Review Patterns**: Look for suspicious patterns such as sudden review spikes, generic language, or accounts with limited history.
   * **Verify Publisher Credibility**: Research the publisher's history, other published items, and presence outside the marketplace.
   * **Check External Sources**: Look for independent reviews, security analyses, or reports about the item from trusted sources.
2. **Immediate Action**:
   * **Restrict Usage**: Limit or monitor the item's usage until credibility can be established.
   * **Remove if Confirmed**: If manipulation is verified or the item shows additional suspicious indicators, remove it from endpoints.
   * **Report the Item**: Flag the item to marketplace administrators for review and potential removal.
3. **Organizational Response**:
   * **Update Vetting Procedures**: Implement policies that don't rely solely on user reviews for security decisions.
   * **Deploy Monitoring**: Track the item's behavior on endpoints for signs of malicious activity.
   * **User Education**: Inform users about the risks of relying on manipulated reviews when selecting items.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/manipulated-user-reviews-1.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
