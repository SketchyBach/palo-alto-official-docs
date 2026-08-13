<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/file-creation.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/file-creation.md).

# File Creation

**Severity**

🔵 Low (2)

**Short Description**

Flags items that create or drop files onto the filesystem. This may include downloading content from remote sources or generating new files during execution. While file creation can be benign, it may also indicate attempts to persist malicious payloads, stage further actions, or evade detection by writing artifacts outside the monitored runtime.

**Suggestion**

Review the item's file creation behavior and verify that it aligns with its intended functionality. Monitor the item for any unexpected file operations or suspicious activity.

**Information**

Items that create or drop files onto the filesystem may generate new files during execution or download content from remote sources. While this capability is often benign and necessary for legitimate functionality (such as caching, storing user preferences, or downloading resources), it can also be exploited to persist malicious payloads, stage further attack actions, or evade detection by writing artifacts outside of monitored runtime environments. The low risk score indicates that file creation itself is not inherently malicious, but it warrants awareness and monitoring to ensure the behavior aligns with the item's stated purpose.

**Risks of File Creation**

* **Persistence Mechanisms**: The item may use file creation to establish persistence on the endpoint, allowing malicious code to survive reboots or security scans.
* **Staged Attacks**: Files dropped to the filesystem could serve as staging points for multi-stage attacks or payload delivery.
* **Detection Evasion**: Writing files outside of typical monitored locations may allow malicious activity to evade security tools and monitoring systems.
* **Unintended Data Storage**: Legitimate file creation could inadvertently expose sensitive data if files are stored in insecure locations.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review File Creation Behavior**: Identify what files are being created, where they are stored, and why they are necessary.
   * **Verify Legitimacy**: Confirm that file operations align with the item's documented purpose and functionality.
   * **Check File Locations**: Ensure files are not being written to unusual or sensitive system directories.
2. **Monitoring Action**:
   * **Track File Activity**: Monitor ongoing file creation patterns to detect any anomalies or unexpected behavior.
   * **Review Access Permissions**: Verify that created files have appropriate access controls and are not world-writable.
   * **Assess Remote Sources**: If the item downloads files, verify the sources are trusted and use secure protocols.
3. **Preventive Measures**:
   * **Apply Least Privilege**: Ensure the item operates with minimal necessary permissions for file system access.
   * **Regular Audits**: Periodically review the item's file operations to ensure continued alignment with legitimate use cases.
   * **Remove If Necessary**: If file creation behavior appears suspicious or cannot be justified, consider removing the item.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/file-creation.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
