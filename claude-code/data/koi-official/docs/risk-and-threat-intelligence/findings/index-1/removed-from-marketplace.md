<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/removed-from-marketplace.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/removed-from-marketplace.md).

# Removed from Marketplace

**Severity**

🔴 High

**Short Description**

Flags items that have been removed or delisted from the marketplace, potentially due to security vulnerabilities, or malicious behavior. Such items pose a risk as they are no longer maintained or patched.

**Suggestion**

It is recommended to review and remove this item from your environment as it is no longer maintained or trusted.

**Information**

This extension has been flagged as removed from its official marketplace. Items can be removed for various reasons, including security violations, malicious activity, or non-compliance with marketplace policies. Continuing to use such extensions in any environment (e.g., development tools, IDEs, or other software ecosystems) can pose significant risks.

When an item is removed from its marketplace, it indicates a lack of trust and ongoing maintenance. This can result in vulnerabilities, outdated functionality, or incompatibility with newer versions of the associated software platform.

**Risks of Removed Items**

* **Lack of Security Updates**: Items removed from their marketplace no longer receive critical patches, exposing users to potential exploits.
* **Trust Issues**: Removal implies the item may have violated policies, been identified as malicious, or lacked compliance with platform standards.
* **Compatibility Problems**: Unmaintained items may no longer function properly with updated platforms, leading to crashes or errors.
* **Increased Risk of Exploitation**: Malicious actors might target removed items to exploit vulnerabilities in outdated versions.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Its Purpose**: Assess whether the extension is still needed and if it provides critical functionality.
   * **Verify Alternatives**: Check if a trusted and actively maintained alternative is available.
   * **Evaluate Devices/Users**: Identify devices, users, or projects utilizing this extension to understand the scope of its usage.
2. **Immediate Action**:
   * **Remove the Extension**: Remove the extension from all systems or environments, as it is no longer trusted or maintained.
   * **Notify Stakeholders**: Inform users or teams about the removal and suggest a suitable replacement if necessary.

**Examples**

**Example 1**:

* **Reason for Removal**: Violation of marketplace policies
* **Description**: The extension was flagged for collecting sensitive developer credentials without consent and removed from the marketplace. It no longer receives updates, leaving users exposed to potential vulnerabilities.

**Example 2**:

* **Reason for Removal**: Security Concerns
* **Description**: The extension was identified as having exploitable vulnerabilities in its code, but it was removed from the marketplace before patches were issued.

**Detection Method**

ExtensionTotal continuously monitors software marketplaces and ecosystems for changes in the status of extensions. When an extension is removed, it is flagged in our system to alert users.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-1/removed-from-marketplace.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
