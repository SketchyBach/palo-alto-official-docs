<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/ossf-high-impact-check-failure.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/ossf-high-impact-check-failure.md).

# OSSF High Impact Check Failure

**Severity**

🟡 Medium (5)

**Short Description**

Flags items linked to repositories that score poorly on a high-severity OpenSSF Scorecard check. A low score in critical areas indicates a heightened risk of insecure development practices and potential supply chain vulnerabilities.

**Suggestion**

Investigate the item's source repository and its OpenSSF Scorecard results. Consider replacing the item with a more secure alternative that follows better development practices, or remove it if the risks outweigh the benefits.

**Information**

Items linked to repositories with poor OpenSSF Scorecard scores on high-severity checks indicate underlying security weaknesses in how the software was developed and maintained. The OpenSSF (Open Source Security Foundation) Scorecard evaluates repositories on critical security practices such as code review processes, vulnerability management, branch protection, dependency updates, and security policy presence. When an item fails high-impact checks, it suggests the source code may not have undergone proper security scrutiny, lacks automated security testing, or follows insecure development workflows. These deficiencies create opportunities for vulnerabilities to be introduced and persist undetected, potentially compromising any endpoint where the item is installed.

**Risks of OSSF High Impact Check Failure**

* **Insecure Development Practices**: The item may have been built without proper code review, security testing, or vulnerability scanning, increasing the likelihood of exploitable flaws.
* **Supply Chain Vulnerabilities**: Poor upstream security practices make the item susceptible to supply chain attacks, where malicious code could be injected without detection.
* **Unpatched Vulnerabilities**: Repositories with low scores often lack timely dependency updates and security patches, leaving known vulnerabilities unaddressed.
* **Lack of Security Accountability**: Absence of security policies and response procedures means vulnerabilities may not be properly disclosed or remediated when discovered.
* **Compromised Code Integrity**: Weak branch protection and access controls increase the risk of unauthorized modifications to the codebase.

**Recommended Actions**

* **Investigate the Item**:
  * **Review OpenSSF Scorecard Results**: Examine the specific checks that failed and understand which security practices are missing.
  * **Assess Criticality**: Determine how critical the item is to business operations and whether the security risks are acceptable.
  * **Evaluate Alternatives**: Search for similar items from repositories with better security scores and development practices.
  * **Check Publisher Response**: Verify if the publisher is aware of security concerns and actively working to improve their practices.
* **Immediate Action**:
  * **Monitor Closely**: If the item must remain installed, monitor for security updates and unusual behavior.
  * **Replace or Remove**: Consider replacing with a more secure alternative, or remove the item if acceptable substitutes exist or if the risks are too high.
  * **Engage with Publisher**: Report the security concerns to the publisher and encourage adoption of better security practices.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/ossf-high-impact-check-failure.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
