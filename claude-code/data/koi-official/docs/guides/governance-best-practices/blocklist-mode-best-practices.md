<!-- KOI source: https://docs.koi.ai/guides/governance-best-practices/blocklist-mode-best-practices.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/governance-best-practices/blocklist-mode-best-practices.md).

# Blocklist mode best practices

Blocklist mode is Koi’s default governance posture. In this mode, all marketplace items are allowed by default unless explicitly blocked using guardrails or policies. This mode is ideal for organizations that want to reduce risk incrementally, without introducing friction to end users on day one.

Here's how to get the most out of blocklist mode:

#### 1. Turn on guardrails

Start by enabling one-click protections that proactively block high-risk behaviors before any policies are configured:

* **Scan-first protection**\
  Prevent installation of newly published packages or extensions until they pass risk scanning.
* **Malware protection**\
  Automatically block items detected as malicious by threat intelligence and advanced scanning.
* **Delayed access (30 days)**\
  Block access to items until they have aged and stabilized in the marketplace.
* **Version update cooldown (2 days)**\
  Delay updates to avoid installing risky new versions immediately.
* **Sideloading visibility**\
  Identify extensions that bypass official marketplaces.

These guardrails provide broad coverage across risk types and marketplaces, and are recommended as your baseline.

***

#### 2. Create block policies

Define policies that explicitly block items based on your organizational risk criteria.

**Block based on critical indicators**

Use policy filters to target items with:

* Critical risk level
* High-risk findings such as:
  * Vulnerable to RCE or MitM
  * Exfiltrates cookies or data
  * Listed for sale or abandoned
  * Low install count and unverified publisher
  * Publisher domain expired
  * Obfuscated or theme-injected code
  * Risky tap sources (e.g. Homebrew third-party taps)

**Regulate sensitive categories**

Create policies to block categories while allowing specific exceptions:

* VPN & Proxy tools
* Password managers
* Screen capture tools

**Example policy logic:**

```
Marketplace is Chrome Web Store
AND Category is VPN & Proxy Services
AND Item ID is not <approved-id>
→ THEN block
```

You can use combinations of marketplace, category, publisher, install base, risk score, and more to fine-tune control.

***

#### 3. Use alert-only policies (optional)

Before enforcing a block, you can create alert-mode policies to:

* Gain visibility into usage patterns
  * Evaluate policy impact using real data
    * Identify sensitive categories in use

This approach allows teams to prepare for enforcement without disrupting workflows.

***

#### 4. Summary: Layered control

Blocklist mode supports progressive hardening:

You reduce risk immediately while maintaining end-user productivity.

***

To learn more about configuring policies, see the [Policy Library documentation](https://success.koi.security/update/docs/policy-library#/).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/governance-best-practices/blocklist-mode-best-practices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
