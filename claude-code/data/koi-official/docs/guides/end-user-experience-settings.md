<!-- KOI source: https://docs.koi.ai/guides/end-user-experience-settings.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/end-user-experience-settings.md).

# End user experience settings

Security policies work best when the people affected by them understand what's happening and what to do about it. The **End-User Experience** **settings** let you control how end users experience your organization's security policies - through clear notifications, helpful block messages, and transparent visibility into what's allowed and what isn't.

{% hint style="info" %}
Note that for any network-level action (block/allow) or result of a network-level action (notification/alert) for any item, the network integration must be established.&#x20;
{% endhint %}

***

### Notifications

When Koi enforces a policy - blocking an item, flagging a violation, or removing an item from a device - the end user may not know what happened or why. The Notifications section lets you keep them informed by sending an automatic message via **Slack** or **Email**.

> To use Slack notifications, your workspace needs to be connected to Koi's Slack app. See the [Slack integration guide](https://docs.koi.ai/integration-guides/slack-integration) for setup instructions.

#### What you can notify end users about

There are three events you can toggle notifications for:

| Event                          | What it means                                                                                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Item violating a policy**    | An end user has an item installed that matches an alert policy. They receive a message with details and guidance on what to do next.                                                             |
| **Item under block status**    | An end user has an item installed that's actively blocked by policy. The notification explains the situation and provides next steps.                                                            |
| **Item removed from endpoint** | Koi automatically removed an item from an end user's device due to policy enforcement. This is especially useful as it ensures no one is caught off guard when an item changes on their machine. |

Each event has its own toggle for Slack and Email, so you can enable whichever channels work for your organization.

<figure><img src="/files/hkGuUDFR9RB5DwXnvpYd" alt=""><figcaption></figcaption></figure>

#### Customizing notification messages

Every notification type has a **config button** (the gear icon on the right side of each row). Click it to open the customization modal where you can tailor exactly what end users see.

<figure><img src="/files/o4HKYvOALlPAUluB7mEG" alt=""><figcaption></figcaption></figure>

Here's what you can customize:

* **Image (optional):** Add your company logo or a custom image URL to display at the top of the Slack message.
* **Message template:** The message body, written in Markdown.&#x20;
  * Use dynamic variables like `{{device}}`, `{{policy_name}}`, and `{{policy_description}}` - these are filled in automatically for each notification.
* **Item details:** Checkboxes to include or exclude specific fields in the notification:
  * Item name
  * Item version
  * Platform
  * Koidex link (so the end user can understand the item's risk)
  * Request approval button
* **Send test message:** Enter a Slack member ID or email address to send a test notification. We recommend doing this before enabling notifications for your organization.

***

### Blocked Items in IDEs

This setting controls what happens when an end user opens their VS Code-based IDE (VS Code, Cursor, Windsurf, or Kiro) and searches for an extension that your policy blocks.

You have two choices:

<figure><img src="/files/FaEBd4xpzzJMDgpkuiLg" alt=""><figcaption></figcaption></figure>

#### Option 1: Filter out blocked items

Blocked extensions are **removed entirely** from the IDE marketplace. End users won't see them in search results and can't attempt to install them.

**Best for:** Organizations that want a strict approach - if it's blocked, it simply doesn't appear.

#### Option 2: Show blocked items

Blocked extensions **still appear** in the IDE, but with a clear message explaining they're blocked by organization policy.

**Best for:** Organizations that prefer transparency. End users can see the extension exists, understand why it's blocked, and take action (like [requesting approval](https://docs.koi.ai/guides/request-approval-workflow)).

***

### Customize Block Messages

When Koi blocks an item - whether it's an IDE extension, agent or a code package - end users see a message explaining why. This section lets you control what that message says for each category.

You can customize messages for two categories:

<table><thead><tr><th width="275.42578125">Category</th><th>Where it applies</th></tr></thead><tbody><tr><td><strong>Extensions</strong></td><td>IDE extension marketplaces</td></tr><tr><td><strong>Code packages</strong></td><td>Code Package registries - CLI-based requests</td></tr><tr><td><strong>Agents</strong></td><td>Agent chat interface (runtime policies for supported agents)</td></tr></tbody></table>

Click the **config button** (gear icon) next to either category to open the message editor.

#### Editing a block message

<figure><img src="/files/i3H8jfs3Huh61wCPPu5F" alt=""><figcaption></figcaption></figure>

The message editor includes:

* **Message template:** A Markdown-friendly editor where you write the message end users see when they encounter a blocked item. The default template is a solid starting point — it explains the block, names the policy, and provides clear next steps.
* **Insert variables:** Click any variable chip to insert it into your message.&#x20;

**For Extensions and Code packages:**

| Variable                    | What it shows                                                  |
| --------------------------- | -------------------------------------------------------------- |
| `{{item_name}}`             | Name of the blocked extension or package                       |
| `{{policy_name}}`           | The policy that triggered the block                            |
| `{{policy_description}}`    | A description of why the policy exists                         |
| `{{request_approval_link}}` | A link for the end user to request approval for the given item |
| `{{koidex_link}}`           | A link to Koidex for more details on the item's risk profile   |

**For Agents:**

| Variable                    | What it shows                                                                 |
| --------------------------- | ----------------------------------------------------------------------------- |
| `{{policy_name}}`           | The policy that triggered the block                                           |
| `{{blocked_action}}`        | The action the agent attempted that was blocked                               |
| `{{request_approval_link}}` | A link for the developer to request an exclusion (carries the reference ID)   |
| `{{policy_id}}`             | The reference shown to the developer and used by admins to locate the request |

* **Reset to default:** If you've customized things and want to start over, one click brings back the original template.

<figure><img src="/files/6pNgVN1HbMioJXv7VS3Q" alt=""><figcaption></figcaption></figure>

**Agents:** \
For agent surfaces (Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, and others), the agent may rephrase your message in the chat, so the exact wording and formatting aren't guaranteed. The request-approval link and reference are preserved.<br>

<figure><img src="/files/fPptw8zJdZGhwiJtKfPq" alt=""><figcaption></figcaption></figure>

***

### Putting It All Together

Here's a recommended approach for rolling out these settings:

1. **Set your visibility preference:** Decide whether blocked items should be hidden or shown in IDEs. Many teams start with "show" for transparency.
2. **Craft your block messages:** If you're showing blocked items, write clear messages that explain the reason and give end users a path forward.
3. **Turn on notifications:** Enable Slack and/or Email notifications for the events that matter to your organization. At a minimum, consider enabling "Item removed from endpoint" so end users know when something changes on their machine.
4. **Customize and test:** Tailor the notification templates to match your organization's voice. Use the "Send test message" feature to preview before going live.
5. **Iterate:** After rollout, gather feedback from end users. Are the messages clear and helpful? Adjust the templates as needed.

***

### Quick Reference

| Setting                        | What it controls                                  | Where end users see it                                  |
| ------------------------------ | ------------------------------------------------- | ------------------------------------------------------- |
| Slack/Email notifications      | Automatic messages when policies trigger          | Slack DM or Email                                       |
| Blocked items visibility       | Whether blocked items appear in IDE search        | IDE marketplace (VS Code, Cursor, Windsurf, Kiro)       |
| Block messages (Extensions)    | The message shown for blocked IDE extensions      | IDE extension details page                              |
| Block messages (Code packages) | The message shown for blocked code packages       | CLI output                                              |
| Block messages (Agents)        | The message shown when an agent action is blocked | Agent chat interface (Claude Code, Cursor, Codex, etc.) |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/end-user-experience-settings.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
