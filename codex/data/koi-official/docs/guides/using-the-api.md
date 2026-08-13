<!-- KOI source: https://docs.koi.ai/guides/using-the-api.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/using-the-api.md).

# Using the API

Our platform is built with an API-first approach, allowing you to perform any action available in the UI through the API. This enables seamless automation and integration with your workflows. Follow the steps below to create and manage API keys.

#### Creating an API Key

1. **Ensure Appropriate Role**
   * To create an API key, you must have the **xt-Administrator** role.
2. **Navigate to the Settings Page**
   * Access the **Settings** page from the top navigation bar.
3. **Open the API Access Tab**
   * In the **Settings** page, select the **API Access** tab.
4. **Click "Create New API Key"**

   * Click the **Create new API key** button.

   ![](https://files.readme.io/81f34df9377d994d8e5ef0b43df4d57115fdf594a7394e05586e023793f84cc3-image.png)
5. **Access Your API Key**
   * Within a few seconds, a new API key will appear in the table.
   * Click the **Copy** button next to the key to copy it securely.
6. Authentication
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

***

#### API Documentation

* Explore the full capabilities of the API [here](https://docs.koi.ai/api-reference/)

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/using-the-api.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
