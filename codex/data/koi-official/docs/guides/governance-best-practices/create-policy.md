<!-- KOI source: https://docs.koi.ai/guides/governance-best-practices/create-policy.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/governance-best-practices/create-policy.md).

# Policies creation

Policies provide visibility into installed items and granular control over what can enter your environment - without manually vetting each item. They're divided into two types: **Alert policies** for visibility and **Allow & block policies** for control.

***

### Policy Priority System

For **Allow & Block policies**, Koi uses a priority system to determine the governance status of items when multiple policies match. This system determines whether an item should be allowed or blocked in your environment.

#### How Priority Works

**Policy order determines priority**: The order of policies in your policies list determines their evaluation strength, with earlier policies taking precedence over later ones.

* **First policy** = Strongest (highest priority)
* **Last policy** = Weakest (lowest priority)

When multiple Allow & Block policies match the same item, Koi evaluates them in order and applies the action from the first matching policy.

{% hint style="info" %}

* **Alert policies are separate**: Alert policies don't participate in the priority system since they don't affect governance decisions. They trigger when their conditions are met with installed items, regardless of Allow/Block outcomes.
  * **Order matters:** When creating policies, consider their position in the list. Place more specific or critical policies higher up to ensure they take precedence.
  * **Global lists:** The Global Allowlist and Global Blocklist (along with [Guardrails](/guardrails/overview.md)) will take precedence over Custom Policy rules
    {% endhint %}

***

### Policy types

#### **Alert policies**

**Goal**

Stay informed when items that meet certain conditions are installed across your organization.

**Ideal for**

Alert policies help security teams understand what’s happening in their environment. You can create conditions that reflect your organizational state. Alert policies power Monitor and Warn modes, allowing teams to monitor and assess activity without actively enforcing blocks. You can optionally enable end-user notifications to inform users when a matching item is detected on their device. This approach supports gradual policy adoption and helps validate governance rules before applying enforcement.

**Example use cases**

* Alert when a browser extension with high risk and unknown publisher is enabled on endpoints.
* Alert on the use of items that are no longer maintained or supported.

{% hint style="info" %}
When creating or updating an alert policy it can take up to 15 minutes to take effect. Instances of items matching the policy condition will be notified once per policy.&#x20;
{% endhint %}

**Alerts can be sent via email or wehbook.**

Webhook spec example:

```json
{
    policy: {
    id: number;
    name: string;
    description: string;
    created_at: Date;
    creator_fullname?: string;
  },
    hits: {
      extension: {
  extension_id: string;
  display_name: string;
  publisher_display_name: string;
  version: string;
  marketplace: MarketplaceName;
  platform: Platform;
  reason?: string;
  local_full_path?: string;
},
      devices: {
        hostname: device.hostname,
      },
    }
}
```

#### **Allow & block policies**

**Goal**

Define which items should be allowed or blocked using dynamic, rule-based evaluation that runs continuously as new items are added or updated to public marketplace - giving you consistent up-to-date control over what enters your environment, that is enforced via Koi supply chain gateway .

**Ideal for**

Preventing risky or non-compliant items from being installed, while allowing trusted or low-risk items to be used without manual review.

* Enforcement level
  * Block: Prevents installation or use, with justifications and recommended next steps.
* How it’s enabled
  * Use an Allow & block policy with action = Block to enforce the Block level.
  * Policy priority determines which rule wins when multiple policies match.

**Example use cases**

* Block AI models without verified publishers or high-risk indicators.
* Allow npm packages signed by verified organizations.

{% hint style="info" %}
When creating or updating a policy it can take up to 60 minutes to take affect. If already installed, the item will be flagged under the “Open” tab on the Remediation page (can take several minutes).
{% endhint %}

***

### Policy creation flow

Koi’s policy creation flow is designed as a guided wizard that helps you create alert or allow & block policies step by step. Each step adapts dynamically based on the policy type you select, ensuring the right options and filters are available throughout the process.

#### 1. Access the Policies page

From the Koi platform, go to **Policies → Create new policy**.

The wizard will open and prompt you to choose the type of policy you want to create.

#### 2. Choose policy type

Select **Alert** or **Allow & block**.

Once selected, the rest of the flow will automatically adjust to match the chosen policy type.

* **Alert**: Configure visibility conditions for installed items.
* **Allow & block:** Define rules that automatically allow or block items based on defined attributes.

![](https://files.readme.io/2400c09f187ff3d06b93a81058a26e34e85de846457458057714d48db982c280-image.png)

#### 3. (Optional) Select endpoint groups

You can choose to apply the policy to specific **endpoint groups** for more precise governance.

This allows you to target policies to a subset of your environment - for example, developer machines or specific departments.

If no group is selected, the policy will apply to **all endpoints** by default.

#### 4. Define scope

Choose which **item types** the policy applies to.

Koi supports multiple item categories such as:

* **Extensions** – Browser, IDE and productivity tools extensions
* **Code packages** – npm or PyPI packages
* **OS packages** – Homebrew formulas
* **AI models** – Hugging Face models
* **Software** – Applications discovered on endpoints. *(Alert policies only)*
* **MCP servers** – MCP servers from official registries.

{% hint style="info" %}
Once you select an item type, the query builder will automatically update to reflect its relevant filters and parameters.
{% endhint %}

![](https://files.readme.io/9fcf237dccf664ab880bf6cd3fbb3f58d41633efd1d29f77321ba3a4596a0cd2-image.png)

#### 5. Define conditions

Use the **query builder** to define the rules for your policy. The available attributes in the query builder automatically adjust based on the item types you selected in the previous step.

* **Alert policies**: Conditions evaluate against **installed items in your inventory**. These rules determine when a notification is triggered based on what's already present across your endpoints.
* **Allow & block policies**: Conditions evaluate against **items from public marketplaces**. These rules define which items should be allowed or blocked before they enter your environment, based on their marketplace attributes.

![](https://files.readme.io/f71fe37b56d1be7d6aa954657a80ae25335ee720953fb5d14b26fafa9cfdb9b7-image.png)

Use **Impact check** to preview which currently installed items match your defined conditions before activating the policy.

![](https://files.readme.io/4995b1a56771b37f9038f5b1aa14322790ed942132c7f41758b0839b7754c934-image.png)

#### 6. Set action

The available actions depend on the policy type:

* **Alert policies –** Define how alerts are delivered and who receives them. Alerts can be sent via email or webhook, and you can optionally enable end-user notifications to notify users when a matching item is installed on their device. Learn more about end-user notifications →

  ![](https://files.readme.io/a6c5a727272e27c6eadce6ab5d06943bb9616ed7fd606badaa0b4c7f571921ba-image.png)
* **Allow / block policies** – Choose whether matching items should be *allowed* or *blocked* automatically when encountered.

  ![](https://files.readme.io/c5f41c028b0b78769db8c5e86e3426161da25412c42e10275d4ee10c4acffd22-image.png)

#### 7. Create policy

Click **Create policy** to save and activate it.

The policy will now appear in the **Policies** table, where you can view, edit it at any time.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/governance-best-practices/create-policy.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
