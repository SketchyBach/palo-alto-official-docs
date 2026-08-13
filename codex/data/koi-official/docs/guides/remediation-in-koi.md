<!-- KOI source: https://docs.koi.ai/guides/remediation-in-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/remediation-in-koi.md).

# Remediation in Koi

Koi supports two remediation models, designed to balance risk reduction with operational safety and end-user impact.

### **Automatic Remediation**

Automatic remediation is applied only in tightly scoped scenarios where risk is high and enforcement is safe.

For **supported marketplace items**, Koi will automatically remove an item in the following case:

* **Malware Protection Guardrail** – If an installed item is confirmed as malicious, Koi automatically removes it from the endpoint on the next script run.

### **Controlled Remediation**

Items that violate block policies but do not fall under automatic remediation are handled through **controlled remediation**.

These items appear in the **Open** tab of the Remediations page, where admins can:

* Review the violating item and affected endpoints
* Decide whether and when to remove it
* Trigger remediation manually to maintain enforcement control

This ensures remediation is intentional, auditable, and aligned with operational context.

#### **Force Remediation**

In some cases, remediation cannot complete automatically due to platform safeguards or runtime constraints. Koi provides **force remediation** to ensure enforcement can complete when required, with two enforcement options depending on the level of control needed.

#### **Option 1: Item-level force remediation**

Admins can apply force remediation to a **specific item** when remediation is blocked. Koi surfaces a clear remediation status in the Remediations tab, explaining what prevents removal and what will happen if force remediation is triggered.

Common scenarios include:

* **Windows extensions currently in use** (e.g. JetBrains IDEs, Notepad++, and in some cases Chrome extensions), where active processes must be terminated to complete removal.
* **OS package dependency protection**, commonly affecting Homebrew packages, where dependent packages prevent smooth removal.
* **MCP servers in agentic IDE clients** (e.g., Claude Desktop, Cursor), where the client must be restarted after config removal to fully terminate the MCP server.

Item-level force remediation allows admins to make a targeted, informed decision without impacting other items or endpoints.

<figure><img src="/files/7G4aUHS3z1vgxyi1lONY" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/bRGTAFrLdSWNNpUnMBAv" alt=""><figcaption></figcaption></figure>

#### **Option 2: Global force remediation**

Admins can also enable **global force remediation** from the Remediation settings. When enabled, Koi will automatically apply force remediation whenever remediation is blocked, terminating required processes or overriding dependency safeguards as needed.

<figure><img src="/files/kCOAQEKxKQNMOGRS0bQY" alt=""><figcaption></figcaption></figure>

This option is best suited for environments that prioritize strict enforcement and are comfortable with higher levels of end-user disruption.

> **Recommendation:**\
> For most environments, item-level force remediation provides better control and visibility. Global force remediation should be used only when consistent, immediate enforcement is required across the environment.

### **Remediation in Chrome:**&#x20;

To ensure hermetic remediation for Chrome extensions, Koi both:

* Removes the extension from disk, and
* Changes chrome policies to prevent reinstallation

By default, Chrome may attempt to reinstall an extension that was removed, as long as it still has metadata associated with it. As a result, after remediation you may observe the following behavior:

* The extension may appear as “Corrupted” in Chrome.
* In the All extensions page, the extension will be disabled, and the action button will be grayed out, ensuring the user cannot re-enable or reinstall it.

<figure><img src="/files/OfeSMAK88sEzxXxIt1X6" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/owkQF35tTZabetgddu6d" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/remediation-in-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
