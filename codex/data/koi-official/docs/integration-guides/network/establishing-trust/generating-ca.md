<!-- KOI source: https://docs.koi.ai/integration-guides/network/establishing-trust/generating-ca.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establishing-trust/generating-ca.md).

# Generating CA

#### **1. Create a directory for your CA**

Open a terminal and run:

```shell
mkdir -p ~/myCA
cd ~/myCA
```

#### **2. Generate the CA Private Key**

```shell
openssl genrsa -out myCA.key 4096
```

This generates a **4096-bit private key** for your CA.

#### **3. Create the CA Certificate**

```shell
openssl req -x509 -new -nodes -key myCA.key -sha256 -days 3650 -out myCA.pem
```

* **`-x509`**: Creates a self-signed certificate.
* **`-new`**: Generates a new certificate.
* **`-nodes`**: Skips encrypting the key (optional).
* **`-key myCA.key`**: Uses the private key generated earlier.
* **`-sha256`**: Uses SHA-256 for security.
* **`-days 3650`**: Makes the certificate valid for 10 years.
* **`-out myCA.pem`**: Saves the certificate in PEM format.

During this step, OpenSSL will prompt you for **distinguished name (DN)** details like country, organization, and common name. The **Common Name (CN)** should be something like `"My Root CA"`.

#### **4. Next Steps**

Now you have a working CA.

The file `myCA.key` is a secret - make sure to store it in a safe place such as a vault or a secrets-manager. This file will be used to sign the CSR sent to you before the beginning of the integration.

The file `myCA.pem` can be distributed and installed on the machines you want to integrate with Koi.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establishing-trust/generating-ca.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
