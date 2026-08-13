<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-health-information.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-health-information.md).

# Collection of Health Information

**Severity**

🟡 Medium (4)

**Short Description**

Flags items that disclose collecting health-related data, including heart rate, medical history, symptoms, diagnoses, or procedures, which could compromise sensitive personal information.

**Suggestion**

Review the item's privacy policy and data handling practices to ensure health information collection is necessary and properly secured. Consider removing the item if it collects excessive health data that is not essential for its stated functionality.

**Information**

Items that collect health-related information such as heart rate, medical history, symptoms, diagnoses, or medical procedures have access to some of the most sensitive categories of personal data. Health information is protected under various privacy regulations (such as HIPAA in the United States and GDPR in the European Union) due to its highly personal and confidential nature. When an item installed on an endpoint discloses that it collects such data, it introduces privacy and security concerns regarding how this information is stored, transmitted, and potentially shared with third parties.

**Risks of Collection of Health Information**

* **Privacy Violation**: Health data is among the most sensitive personal information and unauthorized collection or mishandling could violate privacy regulations and user trust.
* **Data Breach Exposure**: If the item's security measures are inadequate, health information could be exposed in a data breach, leading to identity theft or medical fraud.
* **Unauthorized Disclosure**: Collected health data may be shared with third parties without proper consent, potentially compromising patient confidentiality.
* **Regulatory Non-Compliance**: Organizations handling health information without proper safeguards may face regulatory penalties under HIPAA, GDPR, or other health privacy laws.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Data Collection Justification**: Determine whether health data collection is essential to the item's core functionality.
   * **Examine Privacy Policy**: Review how the item stores, processes, and shares health information.
   * **Assess Security Measures**: Verify that appropriate encryption and security controls protect health data in transit and at rest.
2. **Evaluate Compliance**:
   * **Check Regulatory Requirements**: Ensure the item complies with applicable health privacy regulations (HIPAA, GDPR, etc.).
   * **Verify Consent Mechanisms**: Confirm that users are properly informed and have consented to health data collection.
3. **Take Action Based on Risk Assessment**:
   * **Monitor Usage**: If the item serves a legitimate health-related purpose with proper safeguards, continue monitoring for privacy policy changes.
   * **Restrict Deployment**: Limit the item's use to users who specifically require health-related functionality.
   * **Remove If Necessary**: If the item collects excessive health data without justification or lacks adequate security measures, remove it from the endpoint.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/collection-of-health-information.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
