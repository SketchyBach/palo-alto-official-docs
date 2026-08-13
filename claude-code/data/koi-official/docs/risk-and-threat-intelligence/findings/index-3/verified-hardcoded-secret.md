<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/verified-hardcoded-secret.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/verified-hardcoded-secret.md).

# Verified Hardcoded Secret

**Severity**

🔴 High (7)

**Short Description**

Flags extensions contain hardcoded valid secrets. Threat actors can access sensitive data and resources by exploiting hardcoded secrets, eventually compromising the extension.

**Suggestion**

It is strongly recommended to remove or replace the extension, as hardcoded secrets can compromise the integrity and security of your data.

**Information**

Hardcoding secrets into code exposes them to potential misuse. Verified hardcoded secrets are those confirmed to be valid and in active use, increasing the risk of compromise.

**Risks of Verified Hardcoded Secrets**

* **Credential Theft**: Hardcoded secrets can be extracted and used by unauthorized parties.
* **Data Theft**: Any data shared with the extension may be compromised.
* **Service Abuse**: API keys or tokens may be used to perform malicious actions on third-party services.

**Recommended Actions**

1. **Investigate the Item**:
   * **Identify the Secret**: Verify the type and scope of the hardcoded secret.
   * **Assess Impact**: Determine what systems or services the secret provides access to.
   * **Verify Publisher Practices**: Check whether the publisher has a history of responsible development.
2. **Immediate Action**:
   * **Remove the Extension**: Remove it to mitigate the risk of unauthorized access.
   * **Notify Stakeholders**: Alert stakeholders to the exposure and potential impact.

**Examples**

**Example 1**:

* **Secret**: API Key for Cloud Service
* **Description**: The extension hardcodes an API key that grants full administrative access to a cloud environment.

**Detection Method**

ExtensionTotal identifies hardcoded secrets using pattern-matching algorithms, entropy analysis, and validation against known secret formats (e.g., JWTs, API keys).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-3/verified-hardcoded-secret.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
