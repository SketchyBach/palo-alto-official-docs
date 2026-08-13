<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/manipulated-user-reviews.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/manipulated-user-reviews.md).

# Manipulated User Reviews

#### Severity

🔴 High (8)

#### Short Description

Flags items that exhibit signs of artificially inflated user reviews to create a false sense of trust and credibility. This may involve fake positive reviews, coordinated review campaigns, or reputation farming tactics. Such behavior undermines marketplace integrity and may conceal malicious or deceptive activity behind a manufactured appearance of legitimacy.

#### Suggestion

Do not rely on user ratings alone to assess the trustworthiness of the extension. Treat artificially boosted items with caution and investigate further for signs of malicious behavior.

#### Information

Review manipulation tactics are used to mislead users by simulating popularity or legitimacy through inflated ratings and testimonials. This can involve mass-posted fake reviews, paid or bot-generated praise, or sudden bursts of generic 5-star feedback. These signals are commonly associated with items that have something to hide—such as hidden trackers, adware, or exfiltration behavior.

Extensions employing manipulated reviews may escape scrutiny, gain wide distribution quickly, and maintain a presence in official marketplaces despite harmful behavior.

**Risks of Manipulated User Reviews**

* **False Sense of Security**: Users may install the extension based on misleading trust signals.
* **Wider Distribution of Malicious Items**: Artificial trust accelerates installs of harmful extensions.
* **Delayed Detection**: Boosted ratings may delay investigation or takedown of abusive items.
* **Paired with Hidden Behavior**: Often found alongside obfuscation, data abuse, or runtime injection.

#### Recommended Actions

1. **Investigate the Item**:
   * **Analyze Review Patterns**: Look for sudden bursts of positive reviews, repetitive language, or newly created reviewer accounts.
   * **Cross-Reference Behavior**: Compare the extension's claims with its actual behavior.
   * **Check Publisher History**: Review whether the same publisher uses similar manipulation tactics across items.
2. **Immediate Action**:
   * **Flag for Review Escalation**: Forward to security or platform trust teams for deeper review.
   * **Monitor for Risk Indicators**: Combine with other risk signals such as obfuscation, broad permissions, or user complaints.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/manipulated-user-reviews.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
