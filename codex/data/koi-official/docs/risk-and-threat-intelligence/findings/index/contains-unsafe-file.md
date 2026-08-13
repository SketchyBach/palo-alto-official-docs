<!-- KOI source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/contains-unsafe-file.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/risk-and-threat-intelligence/findings/index/contains-unsafe-file.md).

# Contains Unsafe File

**Severity**

🟠 High (7)

**Short Description**

Flags items that include files retrieved from public repositories which have been scanned and identified as unsafe or potentially malicious. This may include executable payloads, obfuscated scripts, or files exhibiting suspicious behavior patterns. Public repositories, while useful for open sharing, can also host unvetted or intentionally harmful content, introducing risks of malware execution, data exfiltration, or supply chain compromise.

**Suggestion**

Carefully review any bundled or externally linked files within the item. Remove or replace the item if it contains unsafe or suspicious files that originate from untrusted sources.

**Information**

Items that import or bundle files from public repositories (e.g., GitHub, GitLab, npm, HuggingFace) without validation risk unintentionally incorporating malicious components. Threat actors may plant backdoors, obfuscation traps, or harmful payloads in open-source projects, which are then unknowingly consumed by developers or intentionally included by malicious actors.

Even non-executable files can serve as vectors for exploitation when interpreted or executed by the browser or system environment.

**Risks of Contains Unsafe File**

* **Malware Execution**: Included files may contain embedded payloads or behavior-triggered attacks.
* **Supply Chain Risk**: Upstream repository tampering can compromise all downstream users.
* **Persistence Mechanisms**: Malicious files can be used to establish footholds or reactivation hooks.

**Recommended Actions**

1. Investigate the Item:
   * **Identify File Origins**: Determine if bundled files were pulled from external/public sources.
   * **Scan File Contents**: Use malware analysis tools or static analyzers to check for suspicious logic.
   * **Check File Hashes**: Compare against known-bad signatures from threat intelligence feeds.
2. **Immediate Action**:
   * **Remove the Item**: If unsafe files are confirmed, remove the item to prevent compromise.
   * **Isolate Impact**: Assess whether the item has been distributed or installed widely.
   * **Report and Block**: Flag the source repository or upstream component for review and block reuse.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/risk-and-threat-intelligence/findings/index/contains-unsafe-file.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
