<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/risk-level-at-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/risk-level-at-koi.md).

# Risk level at Koi

At Koi, we use a risk-based approach to evaluate the security of software extensions and packages. Our **Risk Level** provides an at-a-glance view of a particular item’s risk, helping your team prioritize which software items and packages need immediate attention.

Our evaluation methodology analyzes multiple factors, such as publisher reputation, behavior, code analysis, and external communication. Based on this analysis, each item is assigned a risk level, allowing you to quickly identify software that may pose a threat to your organization.

Our risk level is based on a scale from Low to Critical:

* **Low Risk** (1-3 inclusive)
* **Medium Risk** (4-6 inclusive)
* **High Risk** (7-9 inclusive)
* **Critical Risk** (10)

The risk level is calculated based on Koi’s risk engine and set of security findings detailed in the next section.

## How risk is set

Risk is calculated for every unique item, defined as the combination of an item and its version. This ensures that all distinct instances of an item are evaluated independently. Findings are derived from risk data information extracted directly from each extension. Findings are opinionated, individually scored security indicators that serve as the building blocks of the overall risk level.

## **Core Risk Principles**

Wings calculates an overall risk level for each item based on its findings. The methodology is designed to provide intuitive, actionable results.

1. **The Most Severe Finding Matters Most** The risk score is primarily driven by the highest severity finding. If an item has one critical issue, that becomes the dominant factor in its overall risk assessment.
2. **Additional Findings Have Diminishing Impact** Multiple lower-severity findings don't artificially inflate the risk score. Having ten minor issues won't make an item appear as risky as one with a critical finding. Each additional finding contributes incrementally less to the overall score, reflecting real world risk more accurately.
3. **Critical Findings Are Treated as Immediate Concerns** Certain findings-such as confirmed malware, or exploitation of critical vulnerabilities result in an immediate critical risk level, regardless of other factors.
4. **First-Party Items Receive Adjusted Scoring** Items developed internally (first-party) are assigned lower risk scores, reflecting the greater visibility, control, and trust associated with ***in house development***. However, this adjustment is disabled for severe security concerns where internal origin shouldn't reduce vigilance.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/risk-level-at-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
