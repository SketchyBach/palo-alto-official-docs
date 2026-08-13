<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/managed-vs-manual-modes.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/managed-vs-manual-modes.md).

# Auto-Update Vs. Manual modes

## Understanding the Modes

The MDM Script Package is available in two deployment modes, both providing access to the same underlying script content with different delivery mechanisms.

Both modes execute the same script package. The difference lies in how the script is delivered and updated.

Manual Mode: Provides direct access to the current latest version of the script package through the deployment portal.

Auto-Update Mode: Uses a lightweight wrapper that dynamically downloads the same latest version with additional cryptographic verification.

At any given time, the script content downloaded through Auto-Update mode is identical to the Manual script available in the deployment portal.

## Auto-Update Mode

**What it is**: A lightweight wrapper script that dynamically retrieves and executes the latest version with cryptographic verification.

### How it works

* Secure Retrieval: Wrapper contacts Koi's API with encrypted parameters.
* Dynamic Download: Retrieves the current latest version of the script package.
* Signature Verification: Validates script authenticity using RSA-2048 cryptography.
* Secure Execution: Only executes if cryptographic verification passes.

### Security principles

* Cryptographic Authentication: Each script is signed with an RSA-2048 private key.
* Integrity Verification: SHA-256 hash validation prevents tampering.
* Encrypted Parameters: Deployment credentials are encrypted and secure.
* Public Key Validation: Uses embedded public key for signature verification.
* Fail-Safe Execution: Complete execution block if signature verification fails.

### Best for

* Ongoing operational deployments.
* Environments requiring automatic security updates.
* Teams preferring minimal maintenance overhead.
* Production deployments at scale.

## Manual Mode

### What it is

Direct download of the complete script package from your deployment portal.

### How it works

* Download the current latest version directly from the portal.
* The script includes all logic and functionality in a single, readable file.
* Deploy using your existing MDM/EDR system.
* When new versions are released, manually download from the portal and update in your MDM/EDR system.

### Best for

* Initial code review and security validation.
* Environments with strict change control processes.
* Reference and auditing purposes.

## Modification Policy

While the script is fully transparent and auditable, we do not recommend or support customer modifications to the script package. Any customization needs should be discussed and coordinated with our team to ensure compatibility and maintain security integrity.

## Comparison Overview

| Aspect                 | Manual Mode                                                                | Auto-Update Mode                              |
| ---------------------- | -------------------------------------------------------------------------- | --------------------------------------------- |
| Script Content         | Current latest version                                                     | Current latest version                        |
| Delivery Method        | Direct download                                                            | Dynamic retrieval                             |
| Update Mechanism       | Manual update                                                              | Automatic update                              |
| Cryptographic Security | Under user's discretion                                                    | RSA-2048 signature verification               |
| Code Visibility        | Complete source visible                                                    | Complete source visible. Extract from wrapper |
| Tampering Protection   | Under user's discretion                                                    | Dynamic signature validation                  |
| Maintenance Overhead   | Manual: download new versions from the portal and redistribute via MDM/EDR | Zero maintenance once deployed                |
| Operational Efficiency | Manual intervention required                                               | Fully automated                               |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/managed-vs-manual-modes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
