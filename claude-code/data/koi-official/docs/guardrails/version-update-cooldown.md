<!-- KOI source: https://docs.koi.ai/guardrails/version-update-cooldown.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/version-update-cooldown.md).

# Version Update Cooldown

Delay automatic updates for all installed packages by a set time window, allowing newly pushed versions to establish reputation and undergo public scrutiny before being deployed in your environment.

**Please note: On the Chrome Web Store, the version update cooldown applies only to items that are already installed.**

### Why It Matters

* Allows time for public scrutiny of newly pushed versions.
* Reduces the risk of deploying rushed or malicious updates.
* Marketplaces auto-update mechanism is a common target for threat actors.

### How It Works

* Automatically delays all updates for a configurable period.
* Updates are applied only after the cooldown period, ensuring stability and security.

### Advanced Version Update Cooldown Controls

Easily control how frequently non-binary software can update across multiple marketplaces with advanced, granular configuration options:

**Marketplace-specific cooldown:** Choose which marketplaces (e.g., VSCode, Chrome Web Store, npm) should enforce cooldown periods. Customize default values per marketplace (npm: 1 day; others: 2 days). Enable or disable cooldown on each marketplace for maximum flexibility.

**Per-item cooldown control:**

Fine-tune the cooldown period for individual non-binary software items. This feature is especially useful when:

* **Exclusions are needed**: You can exclude specific items from the default cooldown policy—for example, ensuring that internal tools or in-house extensions are always up-to-date, regardless of marketplace-wide rules.
* **Different update cadences**: Assign unique cooldown periods to each extension or package, reflecting their own release frequency, trust level, or business criticality.

**Granular periods:** Set cooldown periods with greater precision, including intervals like 12 hours and 1 day. This allows policy adaptation according to update cadence, risk profile, and marketplace activity patterns.

#### Supported Marketplaces

![](https://files.readme.io/2f98883f8a70b68747c33a6c55dabb737868588372d4c630e8deec5927413b60-image.png)

* VSCode Marketplace
* Chrome Web Store
* Cursor
* Windsurf
* npm
* OpenVSX

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/version-update-cooldown.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
