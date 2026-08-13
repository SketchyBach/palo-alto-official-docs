<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/installation-velocity-anomaly.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/installation-velocity-anomaly.md).

# Installation Velocity Anomaly

**Severity**

🟡 Medium (6)

**Short Description**

Flags items with an unusually high installation velocity, indicating potential fake installations or abuse of the installation count mechanism to artificially boost credibility.

**Suggestion**

Investigate the item's installation patterns and publisher credibility. Consider removing the item if manipulation is confirmed or if the publisher cannot be verified as trustworthy.

**Information**

Items exhibiting unusually high installation velocity may indicate artificial manipulation of installation metrics to boost perceived credibility and trustworthiness. This pattern can suggest fake installations orchestrated by threat actors or unethical publishers attempting to game marketplace algorithms and user trust signals. Such manipulation is often used to make malicious or low-quality items appear popular and legitimate, thereby increasing their adoption rate among unsuspecting users.

**Risks of Installation Velocity Anomaly**

* **False Credibility**: Artificially inflated installation counts mislead users into trusting potentially malicious or low-quality items.
* **Marketplace Manipulation**: Abuse of installation mechanisms can help malicious items bypass security scrutiny and rank higher in search results.
* **Potential Malicious Intent**: Publishers engaging in installation count manipulation may also employ other deceptive or malicious tactics.
* **Compromised Trust Signals**: Users relying on installation counts as a trust indicator may be exposed to security risks.

**Recommended Actions**

1. **Investigate the Item**:
   * **Analyze Installation Patterns**: Review the timeline and geographic distribution of installations for anomalies.
   * **Verify Publisher Credibility**: Research the publisher's history, other published items, and reputation.
   * **Check User Reviews**: Look for authentic user feedback versus suspicious or generic reviews that may indicate coordinated manipulation.
2. **Assess Risk**:
   * **Evaluate Functionality**: Determine if the item's features justify its installation count or if capabilities seem limited.
   * **Review Permissions**: Check what system access and permissions the item requests.
   * **Monitor Behavior**: Observe the item for suspicious activity or unexpected behavior patterns.
3. **Take Action**:
   * **Remove If Suspicious**: If manipulation is confirmed or the publisher appears untrustworthy, remove the item from endpoints.
   * **Report to Marketplace**: Flag the item to the marketplace provider for investigation of potential abuse.
   * **Implement Controls**: Establish policies to verify item legitimacy before allowing installation, focusing on trusted publishers and verified items.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/installation-velocity-anomaly.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
