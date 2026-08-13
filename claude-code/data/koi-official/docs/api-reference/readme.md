<!-- KOI source: https://docs.koi.ai/api-reference/readme.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/api-reference/readme.md).

# Get Started with Koi API

Our platform is built with an API-first approach, allowing you to perform any action available in the UI through the API. This enables seamless automation and integration with your workflows. Follow the steps below to create and manage API keys.

#### Creating an API Key

1. Ensure Appropriate Role
   * To create an API key, you must have the **xt-Administrator** role.
2. Navigate to the **Settings** Page
3. Open the **API Access** Tab
4. Click **Create New API Key**

<figure><img src="/files/aT8tLIXcXfHgxnrug1eb" alt=""><figcaption></figcaption></figure>

1. Access our API key
   * Within a few seconds, a new API key will appear in the table.
   * Click the **Copy** button next to the key to copy it securely.
2. Authentication
   * Include the API key in each request by including the header `Authorization: Bearer <YOUR_API_KEY>`
   * Replace `<YOUR_API_KEY>` with your actual API key.
   * This header is required for all endpoints and is used to authenticate and authorize the request.

#### API Key Expiration Settings & notifications

Admins can now set an expiration date of up to 1 year when generating a new API key. The expiration notification emails are sent to the owner of the key, i.e., the admin who generated it. Notifications are sent 30, 7, and 3 days before the API key is set to expire. This ensures admins have time to renew or replace their key to maintain uninterrupted access to our API.

### Rate Limiting

To ensure reliable performance and fair usage across all customers, our API enforces rate limits on every route.

**The rate limit is 30 requests per minute per route.**

If a rate limit is exceeded, the API will return an HTTP 429 Too Many Requests response. When this occurs, you can retry after the time window resets.

We recommend implementing client-side retry logic with exponential backoff to avoid disruptions and ensure smooth integration.

### Item Identifiers per Marketplace

When interacting with APIs, provide item IDs in the format expected by each marketplace or repository:

| Marketplace / Source                                     | Format for API Request       | How to Find/Build the ID                                                                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                |
| -------------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Browsers (Chrome web store/Edge add-ons/Firefoxvadd-ons) | Extension ID                 | Get from extension details in the marketplace, or from the extension's URL or folder name                                                                                                                                                                                                                                                                                                                                                                            | `aapbdbdomjkkjkaonfhkkikfgjllcleb`                                     |
| IDEs(VSCode/Cursor)                                      | Extension “itemName”         | <p>Use <code>itemName</code> from marketplace extension URL: <a href="https://marketplace.visualstudio.com/items?**itemName=github.github-vscode-theme"><https://marketplace.visualstudio.com/items?**itemName=github.github-vscode-theme></a>\*\*</p><p>or the <strong>Identifier</strong> extension field from the IDE:</p><p><img src="https://files.readme.io/85efbfed3845fdc0e65ecfa0cc1c39fba1d825212c8ccadda81c4570a3bb1f6e-image.png" alt=""></p><p><br></p> | `github.github-vscode-theme`                                           |
| Homebrew                                                 | Full formula or cask name    | Full formula or cask name                                                                                                                                                                                                                                                                                                                                                                                                                                            | `homebrew/cask/sakura`                                                 |
| Office add-ins                                           | Item ID                      | Office Store ID starting with WA                                                                                                                                                                                                                                                                                                                                                                                                                                     | `WA200007038`                                                          |
| Hugging Face                                             | `models/ID` or `datasets/ID` | Prefix with `models/` or `datasets/` plus the Hugging Face asset name                                                                                                                                                                                                                                                                                                                                                                                                | `models/meta-llama/Llama-3.2-3B`                                       |
| npm                                                      | Package name                 | Use the exact package name from npm                                                                                                                                                                                                                                                                                                                                                                                                                                  | `/types-registry`                                                      |
| PyPI                                                     | Package name                 | Use the exact package name from PyPI                                                                                                                                                                                                                                                                                                                                                                                                                                 | `requests`                                                             |
| Github MCP registry                                      | publisher/repository         | Get from MCP details in the marketplace, or from the MCP's URL                                                                                                                                                                                                                                                                                                                                                                                                       | <https://github.com/mcp/upstash/context7> the ID is `upstash/context7` |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/api-reference/readme.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
