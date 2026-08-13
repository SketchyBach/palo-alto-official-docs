<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-2/publisher-email-in-compromised-list.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-2/publisher-email-in-compromised-list.md).

# Publisher Email in Compromised List

**Severity**

🟠 Medium (4)

**Short Description**

Flags items where the publisher's email address has been found in known data breaches. This indicates potential security risks as compromised email accounts could be used for unauthorized access or malicious publishing.

**Suggestion**

Review the publisher's credibility and security posture. If the email address is associated with a known breach, consider the risk of account takeover or unauthorized item updates.

**Information**

This finding is triggered when the email address associated with an extension's publisher appears in public or commercial breach datasets (e.g., credential dumps, leaked password collections, or data breach disclosures). A breached email does not necessarily mean the item is compromised, but it increases the likelihood of unauthorized access to associated developer accounts—especially if MFA is not enabled.

Publisher accounts are often the gateway for pushing updates or managing extension distribution. If compromised, they can be used to insert malicious code, redirect users, or escalate attacks across environments.

**Risks of Publisher Email in Compromised List**

* **Account Takeover**: Stolen credentials may allow attackers to modify or re-publish the extension.
* **Malicious Updates**: Compromised developer accounts can inject harmful behavior into updates.
* **Loss of Trust**: Users and platforms may lose confidence in publisher integrity.
* **Credential Reuse Risk**: The same credentials may be reused across systems, increasing exposure.

**Recommended Actions**

1. **Investigate the Publisher**:
   * **Check for MFA**: Determine if the publisher uses multi-factor authentication.
   * **Review Publisher History**: Look for prior incidents or suspicious updates.
   * **Confirm Email Ownership**: Ensure the breached email is still in active use.
2. **Immediate Action**:
   * **Restrict Use in Sensitive Environments**: Consider limiting the item’s use until the risk is resolved.
   * **Monitor for Malicious Changes**: Flag the extension for change monitoring or automated re-review.
   * **Contact Publisher**: Notify the publisher if possible and request confirmation of account security.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-2/publisher-email-in-compromised-list.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
