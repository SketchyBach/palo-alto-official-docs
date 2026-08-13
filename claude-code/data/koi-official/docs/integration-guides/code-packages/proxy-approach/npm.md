<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/proxy-approach/npm.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/proxy-approach/npm.md).

# NPM

This documentation covers how to setup a Koi proxy as an explicit proxy for NPM.

**Route** - Ensure that NPM uses Koi proxy by setting it up as explicit proxy.

**Trust** - Make sure pip trusts Koi proxy certificate.

### Setting Up Route (Via Explicit Proxy)

#### Config File

It is possible to use `npm` CLI to edit `npmrc` configuration file.

1. Open Terminal / PowerShell - according to your operating system.
2. Execute the following command.

```shell
# per-user or project
npm config set proxy http://<customer_subdomain>.gateway.koi.security:8090
npm config set https-proxy http://<customer_subdomain>.gateway.koi.security:8090

# system/global (requires admin)
npm config set proxy http://<customer_subdomain>.gateway.koi.security:8090 --location=global
npm config set https-proxy http://<customer_subdomain>.gateway.koi.security:8090 --location=global
```

> **Notes**
>
> 1. The actual proxy details are listed in the deployment portal.

### Setting Up Trust

By default, Node.js, and therefore NPM, does not automatically use the system's certificate store on all operating systems. Node.js typically ships with its own bundled set of root CA certificates.

The referred certificate in the document is the certificate that was used to sign the proxy's served certificate. Depends on the chosen trust system, it would usually be Koi's Root CA or the organizational Root CA. For additional formation see: [Establishing Trust](/integration-guides/network/establishing-trust.md).

It is possible to configure the certificate in two main options.

#### Configure certificate in NPM config file

1. Have the certificate that signed the proxy's certificate available on the endpoint.
2. Set NPM certificate store to include the certificate from step 1.

```shell
# Configure CA
npm config set cafile path/to/cert/cert-to-trust.pem
```

#### Configure environment variables (optional)

Libraries like Requests refer to environment variables to check the certificate.

1. Have the certificate that signed the proxy's certificate available on the endpoint.
2. Set the environment variables.

```shell
# macOS / Linux
export NODE_EXTRA_CA_CERTS=path/to/cert/cert-to-trust.pem

# Windows - user specific
$env:"NODE_EXTRA_CA_CERTS" = "path/to/cert/cert-to-trust.pem"

# Windows - system wide (admin)
setx NODE_EXTRA_CA_CERTS "path/to/cert/cert-to-trust.pem" /M
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/proxy-approach/npm.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
