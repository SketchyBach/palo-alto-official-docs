<!-- KOI source: https://docs.koi.ai/integration-guides/slack-integration.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/slack-integration.md).

# Slack integration

Koi offers a private Slack application, available only to Koi customers, which can be connected via the Koi Portal Settings.

#### What is it used for?

* Today, the app is primarily used to send end-user notifications (for example, when items are removed from their devices).
* In the future, the integration will be extended to support creating dedicated channels and sending broader security notifications to them.

#### What data does Koi collect?

The only information Koi collects and persists is the Slack user ID, which is required to deliver end-user notifications. This data is collected securely via the script package.

#### What permissions does the app request?

To support messaging and future channel integrations, the app requests the following Slack permissions:

* Send messages as @Koi Security
* Start direct messages and group direct messages with people
* Manage and create channels (public and private) that Koi Security has been added to
* Set channel and group DM descriptions
* Join public channels in a workspace
* View basic information about channels and DMs Koi Security is part of
* Add shortcuts and/or slash commands for quick use

#### What’s next

For details on the types of notifications Koi can send via Slack, and guidance on how to configure them, see the [End-user notifications documentation](/guides/end-user-notifications.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/slack-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
