---
url: https://cortex-docs.paloaltonetworks.com/xpanse-api/get-started-with-cortex-xpanse-apis.md
fetched_at: 2026-09-06T11:20:20Z
source: cortex-platform
---

# Get Started with Xpanse APIs

> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/xpanse-api/get-started-with-cortex-xpanse-apis.md).

# Get Started with Xpanse APIs

Using the Cortex Xpanse APIs, you can integrate [Cortex Xpanse](https://cortex-docs.paloaltonetworks.com/cortex-xpanse-docs/) with third-party apps or services to ingest alerts, services, assets, and IP ranges and leverage investigation capabilities. The APIs allow you to manage incidents in a ticketing or automation system of your choice by reviewing and editing the incident's details, status, and assignee.

Before you can begin using Cortex Xpanse APIs, you must generate the following items from the Cortex Xpanse console:

| Value          | Description                                                                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **API Key**    | The API Key is your unique identifier used as the `Authorization:{key}` header required for authenticating API calls. Depending on your desired security level, you can generate two types of API keys, Advanced or Standard, from your Cortex Xpanse app. |
| **API Key ID** | The API Key ID is your unique token used to authenticate the API Key. The header used when running an API call is `x-xdr-auth-id:{key_id}`.                                                                                                                |
| **FQDN**       | The FQDN is a unique host and domain name associated with each tenant. When you generate the API Key and Key ID, you are assigned an individual FQDN.                                                                                                      |

Cortex XPanse API URIs are made up of your unique FQDN, the API name, and name of call. For example, `https://api-{fqdn}/public_api/v1/{name of api}/{name of call}/.`

The following steps describe how to generate the necessary key values:

1. Get your Cortex Xpanse API Key.

   1. In Cortex Xpanse, navigate to **Settings** > **Configurations** > **Integrations** > **API Keys**.

   2. Select **+ New Key**.

   3. Choose the type of API Key you want to generate based on your desired security level: **Advanced** or **Standard**. The Advanced API key hashes the key using a nonce, a random string, and a timestamp to prevent replay attacks. cURL does not support this but is suitable with scripts. Use the provided script to create the advanced API authentication token.

   > #### Note
   >
   > To integrate with Cortex XSOAR you must generate a Standard Key.

   4. If you want to define a time limit on the API key authentication, mark **Enable Expiration Date** and select the expiration date and time. Navigate to **Settings** > **Configurations** > **Integrations** > **API Keys** to track the **Expiration Time** field for each API key. In addition, Cortex Xpanse displays a API Key Expiration notification in the Notification Center one week and one day prior to the defined expiration date.

   5. Provide a comment that describes the purpose for the API key, if desired.

   6. Select the desired level of access for this key. You can select existing **Roles**, or you can select **Custom** to set the permissions on a more granular level.

   > #### Note
   >
   > Be sure to select a role with **View/Edit** access for the Public API. Use the predefined Instance Administrator role or a create a custom role with Public API permission. Roles are described in the Manage Roles section of the Cortex Xpanse User Guide.

   7. **Generate** the API Key.

   8. Copy the API key, and then click **Done**. This value represents your unique `Authorization:{key}`.

   > You will not be able to view the API Key again after you complete this step. Ensure that you copy it before closing the notification.
2. Get your Cortex Xpanse API Key ID.
   1. In the API Keys table, locate the **ID** field.
   2. Note your corresponding **ID** number. This value represents the `x-xdr-auth-id:{key_id}` token.
3. Get your FQDN.

   1. Right-click your API key and select **View Examples**.
   2. Copy the **CURL Example** URL. The example contains your unique FQDN: `https://api-{fqdn}/public_api/v1/{name of api}/{name of call}/`

   You can use the **CURL Example** URL to run the APIs.
4. Make your first API call. The following examples vary depending on the type of key you select. You can test authentication with Advanced API keys using the provided Python 3 example. With Standard API keys, use either the cURL example or the Python 3 example. Don’t forget to replace the example variables with your unique API key, API key ID, and FQDN tenant ID. After you verify authentication, you can begin making API calls.

```curl
curl -X POST https://api-{fqdn}/public_api/v1/{name of api}/{name of call}/ 
-H "x-xdr-auth-id:{key_id}" 
-H "Authorization:{key}" 
-H "Content-Type:application/json" 
-d '{}' 
```

```python
import requests
    def test_standard_authentication(api_key_id, api_key):
    headers = {
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key
    }
    parameters = {}
    res = requests.post(url="https://api-{fqdn}/public_api/v1/{name of api}/{name of call}",
						headers=headers,
						json=parameters)
    return res
```

```python
import requests

from datetime import datetime, timezone
import secrets
import string
import hashlib
import requests

def test_advanced_authentication(api_key_id, api_key):
   # Generate a 64 bytes random string
    nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
    # Get the current timestamp as milliseconds.
    timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
    # Generate the auth key:
    auth_key = "%s%s%s" % (api_key, nonce, timestamp)
    # Convert to bytes object
    auth_key = auth_key.encode("utf-8")
    # Calculate sha256:
    api_key_hash = hashlib.sha256(auth_key).hexdigest()
    # Generate HTTP call headers
    headers = {
        "x-xdr-timestamp": str(timestamp),
        "x-xdr-nonce": nonce,
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key_hash
    }
    parameters = {}
    res = requests.post(url="https://api-{fqdn}/public_api/v1/{name of api}/{name of call}",
						headers=headers,
						json=parameters)
    return res
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://cortex-docs.paloaltonetworks.com/xpanse-api/get-started-with-cortex-xpanse-apis.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
