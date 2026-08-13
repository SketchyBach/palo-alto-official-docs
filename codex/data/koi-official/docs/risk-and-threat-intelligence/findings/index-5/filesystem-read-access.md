<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/filesystem-read-access.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/filesystem-read-access.md).

# Filesystem Read Access

**Severity**

🔵 Low (0)

**Short Description**

Flags items that access and read files from the filesystem.

**Suggestion**

No immediate action is required. This is an informational finding indicating normal functionality.

**Information**

This item has the ability to access and read files from the endpoint's filesystem. Filesystem read access is a common permission granted to many legitimate items that need to interact with local files, such as file managers, text editors, backup utilities, or document viewers. This capability allows the item to retrieve file contents for its intended functionality.

**Risks of Filesystem Read Access**

* **Informational Only**: With a risk score of 0, this finding represents expected and normal behavior for items requiring file access.
* **Privacy Considerations**: While the read permission itself is benign, it's important to ensure the item only accesses files necessary for its legitimate purpose.
* **Data Exposure Potential**: If combined with other permissions (such as network access), read access could theoretically enable data exfiltration, though this finding alone does not indicate malicious behavior.

**Recommended Actions**

* **Verify Item Purpose**:
  * **Review Functionality**: Confirm that the item's stated purpose legitimately requires reading files from the filesystem.
  * **Understand Scope**: Check which files or directories the item accesses and ensure this aligns with its intended use.
* **Ongoing Monitoring**:
  * **Monitor Behavior**: Track the item's file access patterns over time for any unexpected changes.
  * **Review Permissions**: Periodically verify that the item maintains appropriate file access scope and doesn't request additional risky permissions.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index-5/filesystem-read-access.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
