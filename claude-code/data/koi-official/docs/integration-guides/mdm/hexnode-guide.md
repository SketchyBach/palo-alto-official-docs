<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/hexnode-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/hexnode-guide.md).

# Hexnode Guide

**Prerequisites**

* Access to your Hexnode UEM portal
* The script package provided by Koi
* Internet access from managed devices

**Integration Steps**

1. **Create a Custom Script**

* Navigate to **Content > My Files**.
* Click on **Add**.
* Upload the Koi script package.

2. **Create a new automation**

* Navigate to **Automate** and click on **New Automation**
* Select the relevant OS
* Set the Action:
  * Give it an indicative name
  * Select **Execute Custom Script** under scripts
  * Select **Hexnode Repository** and select the uploaded script from step 1.
  * Click **Add**.
* Set the Schedule:
  * Generally, it's up to you, but our recommendation is **Repeat at a set schedule** for once a day.
  * Click **Next**.
* Set the associated groups:
  * For example, `All Linux Devices`
  * Click **Next**.
* Click **Save**.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/hexnode-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
