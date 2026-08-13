<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/flagged-by-community.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/flagged-by-community.md).

# Flagged by Community

**Severity**

🟡 Medium (4)

**Short Description**

Flags items that have user reviews or public comments accusing them of being malicious, risky, or deceptive.

**Suggestion**

Carefully review the item and the specific community feedback to assess the validity of the concerns. Remove the item if the reports indicate malicious or deceptive behavior.

**Information**

Items flagged by community members through user reviews or public comments raise concerns about the item's trustworthiness and safety. When users report an item as malicious, risky, or deceptive, it suggests potential security issues, privacy violations, or misleading functionality that may have been discovered through real-world usage. While not all community reports may be accurate or justified, they serve as important warning signals that warrant further investigation.

**Risks of Flagged by Community**

* **Malicious Behavior**: The item may contain malware, spyware, or other malicious code that users have experienced or detected.
* **Deceptive Practices**: The item may misrepresent its functionality, collect data without proper disclosure, or engage in misleading behavior.
* **Privacy Violations**: Community reports may indicate unauthorized data collection, tracking, or sharing of sensitive user information.
* **Reputational Damage**: Using items flagged by the community can expose the organization to security risks that have been publicly identified.

**Recommended Actions**

* **Investigate the Item**: \*\* **Review Community Feedback**: Examine the specific user reviews and public comments to understand the nature of the concerns. \*\* **Assess Credibility**: Evaluate whether the reports come from multiple independent sources and appear credible. \*\* **Analyze Item Behavior**: Investigate the item's actual functionality and permissions to verify reported issues.
* **Immediate Action**: \*\* **Monitor Closely**: If keeping the item, implement enhanced monitoring to detect any suspicious behavior. \*\* **Remove If Necessary**: If community reports indicate credible security or privacy concerns, remove the item from the endpoint. \*\* **Seek Alternatives**: Consider replacing the item with a more trusted alternative that provides similar functionality.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/flagged-by-community.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
