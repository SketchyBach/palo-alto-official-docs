<!-- KOI source: https://docs.koi.ai/integration-guides/notifications-splunk-integration.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/notifications-splunk-integration.md).

# Notifications: Splunk integration

Koi provides the ability to send notifications from the system into Splunk via webhook.

#### What kind of notifications does Koi send to Splunk?

* Koi currently supports sending notifications from these triggers:
  * Malicious item detected
  * Guardrails

#### How to configure sending notifications to Splunk

1. Enable the desired notification type\[s] that you would like to send
2. Select the Webhook checkbox
3. Enter the webhook URL in the corresponding box that says 'Enter URL'
4. Click 'Save'

   Here's what the webhook URL config should look like:

   ![](https://files.readme.io/4fe0f86dfdc572ab13c90bb4ce15e96b2c21428336c26a7f3245c84bfb8359ff-image.png)
5. Enter the webhook authorization token with custom header
   1. Under the **Advanced Notifications settings > Webhook custom header** section below, enter the appropriate details:
      1. **Header name**: Authorization
      2. **Value**: Splunk \[token\_value]
6. Click 'Save'

   Note: the UI will not show the token value after saving, even if you have entered it correctly\
   Here's what this should look like (you can click the 'reveal' icon to see the value as you enter it):

   ![](https://files.readme.io/a3539b282ceebf06d9108fb68098062b36bc34b96802d46775b496936f7ba11b-image.png)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/notifications-splunk-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
