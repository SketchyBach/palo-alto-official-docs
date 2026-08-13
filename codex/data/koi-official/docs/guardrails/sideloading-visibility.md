<!-- KOI source: https://docs.koi.ai/guardrails/sideloading-visibility.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/sideloading-visibility.md).

# Sideloading Monitoring

### **What is sideloading in Koi?**

Koi does **not block** sideloaded items by default, but provides **visibility** into those that were manually installed and are **unknown or unmanaged**. This helps security teams uncover risks that fall outside standard governance channels.

* If the item **does not exist in any known marketplace**, it is flagged as *sideloaded* and appears in the **Remediation** page for review.
* Koi risk engine currently assesses only items from public marketplaces, so such items will not have a risk level assigned.
* If the item exists in a known marketplace, it will be handled and evaluated by the risk engine like any other item in the Inventory, regardless of how it was installed.

> *Note*: Sideloaded items may be internally developed or purpose-built for your organization. For this reason, **Koi surfaces them for review but does not block or auto-remediate** by default, preserving developer workflows while giving security teams visibility and control.
>
> **Remediation** for Sideloaded items is supported for the VSCode Marketplace, Cursor, Windsurf, and Kiro.

### **Why it matters**

Sideloaded items may introduce hidden risks, especially when:

* They bypass marketplace review processes and governance policies
* They are created and shared internally without proper validation
* They obscure the source and behavior of the software
* They can serve as vectors for insider threats or malicious implants

Visibility into such items enables organizations to:

* Surface unmanaged or unofficial software
* Investigate unusual installs that may pose a security concern
* Maintain tighter control over what's running in their environment

#### Supported Marketplaces

![](https://files.readme.io/8955f9485d988b255841df8cfb14944f3a9799b166f3aa0b8697f62de1193fe8-image.png)

* VSCode Marketplace
* Cursor
* Windsurf
* Kiro


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/sideloading-visibility.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
