<!-- KOI source: https://docs.koi.ai/integration-guides/network/establishing-trust/deploy-certificate-manually.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establishing-trust/deploy-certificate-manually.md).

# Deploy Certificate Manually

#### Prerequisites

* Administrator privileges on the target endpoint.
* The Koi Root CA certificate file. Download it from your Koi deployment portal → **Network Integration** → **Establish Network Trust** → **Download CA**.

***

### macOS

#### 1. Install the Certificate

* **Double-click** the downloaded `.pem` file.
* macOS will open **Keychain Access** and prompt you to add the certificate.
* In the **Keychain** dropdown, select **System**.
* Click **Add**. Enter your macOS administrator password when prompted.

#### 2. Trust the Certificate

* In **Keychain Access**, select the **System** keychain from the left sidebar.
* Locate the newly imported Koi Root CA certificate.
* **Double-click** the certificate to open its details.
* Expand the **Trust** section.
* Set **When using this certificate** to **Always Trust**.
* Close the window. Enter your administrator password when prompted to confirm.

***

### Windows

#### 1. Rename the Certificate

* Rename the downloaded file extension from `.pem` to `.cer` so Windows recognizes it on double-click.

#### 2. Install the Certificate

* **Double-click** the `.cer` file. The **Certificate** dialog will open showing the certificate details.
* Click **Install Certificate…**
* In the **Certificate Import Wizard**, select **Local Machine** as the store location.
* Click **Next**. You may be prompted by User Account Control — click **Yes**.

#### 3. Place in Trusted Root Store

* Select **Place all certificates in the following store**.
* Click **Browse**, select **Trusted Root Certification Authorities**, and click **OK**.
* Click **Next**, then **Finish**.
* A security warning may appear confirming you want to install the certificate — click **Yes**.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establishing-trust/deploy-certificate-manually.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
