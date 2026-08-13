<!-- KOI source: https://docs.koi.ai/guides/governance-best-practices.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/governance-best-practices.md).

# Governance best practices

Koi’s governance model provides powerful ways to reduce risk, enforce control, and maintain compliance without slowing down end-users.

This guide walks through governance strategy and execution using:

* Guardrails for protection baseline, visit the [Guardrails documentation](https://success.koi.security/update/docs/protections-overview#/) to learn more.
* Marketplaces modes: blocklist vs allowlist
* Policies for advanced control and continuous evaluation
* End-user experience that balances security and productivity

Explore each best practice to learn how to implement strong governance across your software supply chain.

***

## Why Koi governance is different

Traditional tools rely on static allow or block lists that require ongoing maintenance, manual review, and often fail to scale. Koi takes a different approach.

With Koi, items are continuously scanned, enriched, and dynamically evaluated against your governance policies and risk signals. Instead of relying on static status flags, your governance posture is enforced in real time:

* **Guardrails** automate protection using live threat intelligence
* **Policies** apply logic based on fresh risk context
* Items are **continuously re-evaluated** as findings and risk posture change

This dynamic approach reduces operational overhead, eliminates blind spots, and ensures you’re always enforcing decisions based on the most current and comprehensive intelligence.

***

## The three pillars of governance

Koi’s governance model is built on three complementary layers:

* **Guardrails:** One-click protection using out-of-the-box controls.
* **Policies:** Flexible policies to allow, alert, or block based on conditions.
* **Remediation:** Automatic or on demand removal of out-of-policy items with full visibility and end-user notifications.

These pillars ensure a balance of control, automation, and usability across all supported marketplaces and platforms.

***

## Enforcement levels

Koi supports progressive enforcement so teams can start with visibility and tighten controls over time. Enforcement is enabled by the policy type you choose.

* **Monitor only**
  * Visibility with no breakage.
  * Enabled by: Alert policies.
  * Effect: Creates notifications and dashboard visibility only.
* **Warn**
  * Allows items, while notifying developers with clear warnings and recommendations.
  * Enabled by: Alert policies with end‑user notifications.
  * Effect: Users see a warning. No blocking occurs.
* **Block**
  * Prevents use or installation, with justifications and recommendations.
  * Enabled by: Allow & block policies set to action = Block.
  * Effect: Item is blocked according to matching rules.

***

## Governance modes: Blocklist vs allowlist

Koi supports two governance modes:

### Blocklist mode (default)

* All items are allowed unless explicitly blocked via policy or global block list
* Use to gradually increase security without disruption.
* Create block policies or alerts for high-risk items.

### Allowlist mode

* All items are blocked unless allowed via policy or global allow list.
* Use in strict environments where control is prioritized.
  * Automatically allow items based on risk score, source, or category.

Both modes integrate with guardrails and policies for full coverage.

***

## End-user experience

Koi is designed to balance governance with usability:

* **Inline feedback**: Users see policy decisions in their marketplaces, IDEs, or CLIs.
* **Integrated requests**: End-users can request approval to use items directly from the item they are searching for (via the web, IDE, CLI, or marketplace).
* **Approval workflow integration**: Route approvals into your ticketing systems such as Jira and ServiceNow, or any existing approval workflow your organization uses. Koi supports approval routing to any URL form, allowing seamless integration via API into your existing workflows.

This ensures that security doesn’t block productivity.

## Governance Enforcement Order

When evaluating an item, Koi applies rules in the following order. The first match wins:

1. **Critical Guardrails:** Guardrails marked as "Superior to Allow List" (e.g., Malware Protection) are evaluated first and cannot be overridden.
2. **Global Block List:** Items on your organization's block list are always blocked, regardless of other rules.
3. **Global Allow List:** Items on your organization's allow list are permitted, unless blocked by a critical guardrail.
4. **Guardrails:** Security guardrails like Delayed Access, Scan-first Protection, and Delisted Monitoring are evaluated.
5. **Custom Policies:** Your custom policies are applied in priority order as configured on the Policies page.
6. **Default Behavior:** If no rules match, the marketplace mode determines the outcome:
   * *Allowlist mode:* Block by default (only explicitly allowed items permitted)
   * *Blocklist mode:* Allow by default (only explicitly blocked items denied)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/governance-best-practices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
