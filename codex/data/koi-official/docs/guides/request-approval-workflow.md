<!-- KOI source: https://docs.koi.ai/guides/request-approval-workflow.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/request-approval-workflow.md).

# Request approval workflow

**Approval workflows** provide a structured way for end users to request access to items that are blocked by policy. Each request captures the necessary context and justification so reviewers can assess whether the exception is appropriate.

Koi’s Governance capabilities block risky or out‑of‑policy items by default. **Approval workflows** connect to Governance by providing a controlled, auditable process to review, approve, or reject exceptions - handled in Koi or routed to your ticketing system.

#### **Set up the workflow in 4 easy steps:**

1. **Create a Request Form**

   1. **(default) Option A: Use Koi’s approval workflow**&#x20;
      1. By default, approval requests are handled in Koi’s built-in approval requests flow. \
         Requesters will submit requests directly to Koi, and admins can review and act on those requests within the Koi platform.
   2. **Option B: Use your own ticketing system**\
      You can also configure your organization's internal ticketing system to manage approval requests.\
      \
      **How to configure:**
      1. In your internal ticketing system, create a request form and configure it to automatically open a ticket once submitted.
      2. In Koi's Approval settings, under Custom Form URL, paste the link to your internal request form. \
         \
         You can choose to apply the same request form for all marketplaces or define a different form per marketplace for finer control.

2. **Customize the form**
   1. **Set Marketplace scope:**\
      You can choose to apply the same request form for all marketplaces or define a different form per marketplace for finer control.

   2. **Configure pre-fill parameters**

      You can configure pre-fill parameters to automatically pass relevant context from Koi to your custom form. Supported parameters include\*:

      1. Marketplace
      2. Requester’s name
      3. Item ID
      4. Requester's User ID

> ***Note**: Pre-filled parameters are supported only for network-based prevention.*

![](https://files.readme.io/9d6a7b0e06bc72edce97fdb13fac9db88acf30f6399220f69eada2610133ba83-image.png)

3. **Retrieve Risk Data via Koidex API**

   Retrieve a risk report for the specific item, including risk scores, vulnerabilities, and other relevant details to support an informed decision.

   1. When a ticket is opened, submit a GET request to the [Koidex API](https://docs.koi.ai/api-reference/reference/koidex) to retrieve the item’s risk data and display it in the ticket.
   2. Ensure you query the API using the correct[ item identifier](https://docs.koi.ai/guides/item-identifiers-per-marketplace) for the relevant marketplace — this ensures accurate and complete data is returned.
4. **Handle Request Approvals**
   1. **Approve**: To approve the request, submit a POST request to the [Add to Allowlist API](https://docs.koi.ai/api-reference/reference/policies#post-api-external-v2-policies-allowlist). Once approved, the item will be added to the global allowlist in Koi and will be available for all users to install.
   2. **Reject**: To reject the request, submit a POST request to the [Add to Blocklist API](https://docs.koi.ai/api-reference/reference/policies#post-api-external-v2-policies-blocklist). This ensures the item remains blocked, preventing unwanted or risky content from entering your environment.

This workflow gives you full control over what enters your organization while maintaining flexibility for legitimate user requests and exceptions.

**Important:** Endpoint groups are **not supported** in alert-only mode. The guardrail will apply to all devices globally for alerting purposes. If you want scoped enforcement, switch 'Alert-only mode' off and you will be able to apply an Endpoint group restriction.

{% hint style="info" %}
**Note:** When an item is blocked due to a policy or guardrail, the Install button is replaced with a Request Approval option. This allows users to request access if they believe the item is necessary for their work.

The exception is items identified as malware. In these cases, users cannot request approval, and any attempt to do so will result in an error indicating that the item cannot be approved due to security concerns.

This behavior allows flexibility for policy-based exceptions while preventing approval requests for items that are confirmed to be malicious.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/request-approval-workflow.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
