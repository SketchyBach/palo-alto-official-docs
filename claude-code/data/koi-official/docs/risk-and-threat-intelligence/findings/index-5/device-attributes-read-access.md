<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/device-attributes-read-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/device-attributes-read-access.md).

# Device Attributes Read Access

**Severity**

🔵 Low (0)

**Short Description**

Flags items that access device attributes such as CPU, MAC address, or OS version.

**Suggestion**

Review the item to understand its purpose and determine if device attribute access is necessary for its functionality. If the item's purpose does not justify this access, consider removing it or replacing it with an alternative.

**Information**

This item has been flagged because it accesses device attributes such as CPU information, MAC address, or operating system version. While such access is common and often legitimate for items that need to optimize performance, provide system-specific features, or perform diagnostics, it can also be used for device fingerprinting and tracking purposes. The risk score of 0 indicates this is informational and typically represents normal functionality for many legitimate items.

**Risks of Device Attributes Read Access**

* **Device Fingerprinting**: The item can create a unique identifier for the endpoint by combining device attributes, enabling persistent tracking across sessions.
* **Privacy Concerns**: Collection of hardware and system information may expose details about the user's device configuration.
* **Reconnaissance**: In combination with other permissions, device attribute access could assist malicious actors in profiling the endpoint for targeted attacks.
* **Information Disclosure**: Device attributes like MAC addresses can reveal information about the network infrastructure and hardware manufacturer.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Purpose**: Verify whether the item's stated functionality requires access to device attributes.
  * **Assess Legitimacy**: Check if the item is from a trusted publisher and has legitimate use cases for this access.
  * **Evaluate Data Usage**: Understand what the item does with the collected device information.
* **Monitoring and Awareness**:
  * **Track Behavior**: Monitor the item for any unexpected data transmission or behavior changes.
  * **Educate Users**: Ensure users understand what device information is being accessed and why.
  * **Document Justification**: Maintain records of why this item is approved despite device attribute access.
* **Consider Alternatives**: If the item's primary function doesn't require device attribute access, explore alternative items with fewer permissions.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/device-attributes-read-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
