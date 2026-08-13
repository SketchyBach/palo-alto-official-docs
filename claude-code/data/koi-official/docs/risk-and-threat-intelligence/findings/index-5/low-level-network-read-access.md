<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/low-level-network-read-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/low-level-network-read-access.md).

# Low Level Network Read Access

**Severity**

🔵 Low (0)

**Short Description**

Flags items that monitor or capture network data by using low level library.

**Suggestion**

Review the item's purpose and necessity. If the item's functionality aligns with legitimate use cases and is required for business operations, it may be retained with monitoring. Otherwise, consider removing it.

**Information**

Items with low level network read access have the capability to monitor or capture network data by utilizing low-level libraries. This functionality allows the item to observe network traffic passing through the endpoint, which may be used for legitimate purposes such as network diagnostics, security monitoring, or performance analysis. However, such capabilities also require careful scrutiny as they provide deep visibility into network communications that could include sensitive data.

**Risks of Low Level Network Read Access**

* **Privacy Concerns**: The item can potentially observe unencrypted network traffic, including sensitive information transmitted over the network.
* **Data Interception**: Low-level network access may allow the item to capture packets containing credentials, personal data, or business-critical information.
* **Surveillance Potential**: The item could be used to monitor user activities and communications without authorization.
* **Misuse by Malicious Actors**: If the item is compromised or malicious, network capture capabilities could be exploited for data exfiltration or reconnaissance.

**Recommended Actions**

* **Investigate the Item**:
  * **Review Purpose**: Verify why the item requires low-level network read access and whether this aligns with its stated functionality.
  * **Evaluate Publisher**: Check the publisher's reputation and whether the item is from a trusted source.
  * **Assess Business Need**: Determine if the item's network monitoring capabilities are necessary for legitimate business or operational purposes.
* **Monitoring and Controls**:
  * **Monitor Network Activity**: Track the item's network behavior to ensure it operates within expected parameters.
  * **Apply Network Policies**: Implement network segmentation and access controls to limit the scope of data the item can access.
  * **Review Regularly**: Periodically reassess the need for this item and its network access permissions.
* **If Concerns Arise**:
  * **Remove the Item**: Uninstall the item if its purpose cannot be verified or if it exhibits suspicious network behavior.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/low-level-network-read-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
