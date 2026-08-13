<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/sensitive-permissions.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/sensitive-permissions.md).

# Broad Host Permissions

**Severity**

🟡 Medium (5)

**Short Description**

Flags items that declare overly broad host access patterns, enabling interaction with all websites. This level of access can be exploited to inject scripts into trusted sites and increases the risk of sensitive data exposure, cross-site surveillance, and credential harvesting.

**Suggestion**

Carefully review the item's permissions and purpose. If the item does not require access to all websites to function properly, consider removing it and finding an alternative with more restricted permissions.

**Information**

Items with broad host permissions have been granted access to interact with all websites visited by the user. This universal access enables the item to read, modify, and inject content into any web page, including sensitive platforms like banking sites, corporate portals, and email services. While some legitimate items require such permissions to function across multiple sites, this level of access creates significant security risks if the item is compromised, malicious, or poorly maintained. Threat actors can exploit these permissions to intercept sensitive information, manipulate trusted sites, or track user activity across the entire web.

**Included Permissions**

* file:///\*
* file:///\*/\*
* file://\*/\*
* https\://\*/\*
* http\://\*/\*
* http\://\*/
* https\://\*/
* \*://\*/\*
* \<all\_urls>
* https\://\*.\*/\*
* http\://\*.\*/\*
* http\://\*.\*.\*.\*/\*
* https\://\*.\*.\*.\*/\*

**Risks of Broad Host Permissions**

* **Sensitive Data Exposure**: The item can access and exfiltrate confidential information from any website, including passwords, financial data, personal communications, and corporate credentials.
* **Script Injection**: Malicious code can be injected into trusted sites, enabling phishing attacks, credential harvesting, or manipulation of legitimate web applications.
* **Cross-Site Surveillance**: The item can track browsing behavior across all websites, creating comprehensive user activity profiles that compromise privacy.
* **Man-in-the-Middle Attacks**: The item can intercept and modify data exchanged between the user and websites, potentially altering transactions or stealing sensitive information.
* **Privilege Escalation**: If the item is compromised through an update or supply chain attack, attackers gain immediate access to all websites visited by the user.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Necessity**: Determine if the item legitimately requires access to all websites or if its functionality could work with more limited permissions.
   * **Evaluate Publisher**: Verify the publisher's reputation, update history, and security practices.
   * **Check Purpose**: Ensure the stated functionality of the item aligns with its requested permissions.
2. **Immediate Action**:
   * **Restrict or Remove**: If the item does not need universal access, remove it and seek alternatives with narrower host permissions.
   * **Monitor Activity**: If keeping the item, closely monitor its network activity and behavior for signs of data exfiltration or suspicious actions.
   * **Review Alternatives**: Look for functionally similar items that request only specific host permissions rather than broad access patterns.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/sensitive-permissions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
