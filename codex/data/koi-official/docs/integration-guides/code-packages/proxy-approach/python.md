<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/proxy-approach/python.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/proxy-approach/python.md).

# Python

This documentation covers how to setup a Koi proxy as an explicit proxy for Python.

**Route** - Ensure that Python uses Koi proxy by setting it up as explicit proxy.

**Trust** - Make sure pip trusts Koi proxy certificate.

### Setting Up Route (Via Explicit Proxy)

#### Config File

1. Open Terminal / PowerShell - according to your operating system.
2. Execute the following command.

```shell
# set user-level proxy
pip config set global.proxy "http://<customer_subdomain>.gateway.koi.security:8090"
# verify
pip config list
```

> **Notes**
>
> 1. The actual proxy details are listed in the deployment portal.
> 2. It is **recommended** to use the CLI.

### Setting Up Trust

By default, Python does not always rely on the operating system certificate store - many Python distributions ship a bundled CA and behavior can vary by platform and installation method.

Starting with pip 24.2 (on supported Python builds) pip will prefer the system trust store, but older pip/Python often continue to use the bundled certificate bundle unless you change it.

The referred certificate in the document is the certificate that was used to sign the proxy's served certificate. Depends on the chosen trust system, it would usually be Koi's Root CA or the organizational Root CA. For additional formation see: [Establishing Trust](/integration-guides/network/establishing-trust.md).

#### Configure certificate in pip

1. Have the certificate that signed the proxy's certificate available on the endpoint.
2. Set pip certificate store to include the certificate from step 1.

```shell
pip config set global.cert /path/to/cert-to-trust.pem

# optional command to verify:
pip config list
```

#### Configure environment variables (optional)

Libraries like Requests refer to environment variables to check the certificate.

1. Have the certificate that signed the proxy's certificate available on the endpoint.
2. Set the environment variables.

```shell
export REQUESTS_CA_BUNDLE=/path/to/cert-to-trust.pem
export SSL_CERT_FILE=/path/to/cert-to-trust.pem
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/proxy-approach/python.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
