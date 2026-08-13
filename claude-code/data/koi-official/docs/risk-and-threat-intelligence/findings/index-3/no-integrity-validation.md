<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/no-integrity-validation.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/no-integrity-validation.md).

# No Integrity Validation

**Severity**

🟡 Medium (5)

**Short Description**

Flags items whose installation process does not verify downloaded files for integrity. Without validation, altered or malicious files may be installed, increasing exposure to security risks.

**Suggestion**

Review the item's installation process and verify whether it implements proper integrity checks. Consider replacing it with an alternative that validates file integrity, or remove it if the risk is unacceptable for your security posture.

**Information**

Items that do not verify the integrity of downloaded files during installation lack a critical security control. Integrity validation (such as checksum verification or cryptographic signature checking) ensures that files have not been tampered with during transit or at rest. Without this validation, the item may unknowingly install altered, corrupted, or malicious files that could have been modified by threat actors through man-in-the-middle attacks, compromised distribution channels, or other supply chain vulnerabilities.

**Risks of No Integrity Validation**

* **Malicious File Installation**: Altered or malicious files may be installed without detection, potentially introducing malware, backdoors, or other security threats to the endpoint.
* **Supply Chain Compromise**: Attackers who intercept or manipulate the download source can inject malicious code that will be installed without verification.
* **Man-in-the-Middle Attacks**: Network attackers can modify files during download, replacing legitimate components with compromised versions.
* **Data Integrity Loss**: Corrupted or incomplete files may be installed, leading to unpredictable behavior or system instability.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Installation Process**: Examine how the item downloads and installs files to confirm the absence of integrity checks.
  * **Assess Business Need**: Determine if the item is essential for operations or if safer alternatives exist.
  * **Evaluate Publisher Practices**: Check if the publisher has a history of security-conscious development.
* **Mitigation Steps**:
  * **Monitor Activity**: Track the item's behavior for signs of compromise or suspicious activity.
  * **Implement Compensating Controls**: Use endpoint protection tools to monitor file changes and detect malicious behavior.
  * **Consider Replacement**: Look for alternative items that implement proper integrity validation mechanisms.
  * **Remove If Necessary**: If the risk is unacceptable or alternatives are available, remove the item from the endpoint.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/no-integrity-validation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
