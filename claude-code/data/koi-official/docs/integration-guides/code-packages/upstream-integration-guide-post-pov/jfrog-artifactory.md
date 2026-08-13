<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov/jfrog-artifactory.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov/jfrog-artifactory.md).

# JFrog Artifactory (Post POV)

Integrating Koi as an upstream registry in JFrog Artifactory allows your organization to enforce governance and security policies across all third-party packages before they reach developer environments or build pipelines.&#x20;

By routing package pulls through Koi, every package is evaluated, logged, and governed according to your policies - enabling centralized policy enforcement, real-time package inventory, and detailed audit trails for compliance and incident response.

This guide covers configuring npm or PyPI remote repositories in JFrog Artifactory to route through Koi.

![](https://files.readme.io/837bb3225c98f4b2ab830490b6df380d61f7e9e7a2ef01c3f587b2f0df19f721-image.png)

***

## Creating a New Remote Repository

1. **Navigate to Artifacts**
   * Open JFrog Artifactory.
   * Go to **Artifacts** from the left-hand menu.
2. **Open Repository Management**
   * Click the **three dots** in the top-right corner.
   * Select **Manage Repositories**.
3. **Create a New Repository**
   * Click **Create a Repository**.
   * Choose **Remote Repository** as the type.
   * Select the wanted package type. (Koi currently supports upstreaming to NPM and PyPi)
4. **Configure the Repository**
   * **Repository Key**: Enter a unique identifier for the repository.
   * Replace `<customer_domain>` with the customer domain.
     * NPM

       ```
       https://koi-npmjs-<customer_domain>.gateway.koi.security
       ```
     * PyPi\
       Under **Pypi Settings** replace **Registry URL** with:

       ```
       https://koi-pypi-<customer_domain>.gateway.koi.security
       ```

       \- Make sure you edit **Registry URL**. Not **URL**.
5. **Save and Use the Repository**
   * Click **Create**.
   * Your new repository is now available for use.

***

## Updating an Existing Remote Repository

If you already have a remote NPM or PyPi repository configured, you can simply update its URL:

1. **Navigate to Manage Repositories**
   * Follow steps 1–2 above.
2. **Edit the Existing Repository**
   * Select your remote repository.
   * Click **Edit**.
3. **Update the URL**
   * Replace the current URL with:
     * NPM

       ```
       https://koi-npmjs-<customer_domain>.gateway.koi.security
       ```
     * PyPi\
       Under **Pypi Settings** replace **Registry URL** with:

       ```
       https://koi-pypi-<customer_domain>.gateway.koi.security
       ```

       \- Make sure you edit **Registry URL**. Not **URL**.<br>
   * Save your changes.

***

## Proxy Validation

To confirm that Artifactory is correctly configured to use Koi as its remote upstream, you can validate connectivity using the Koi feedback page.

```
https://koi-npmjs-<customer_domain>.gateway.koi.security/koi
```

```
https://koi-pypi-<customer_domain>.gateway.koi.security/koi
```

The /koi endpoint is a feedback and validation page that confirms:

* The request is reaching the Koi gateway.
* The proxy is correctly configured and reachable.
* The integration is functioning at a basic connectivity level.

**Notes**

* This endpoint is intended for validation and troubleshooting only and does not serve package content.
* If this page is not reachable, Artifactory will not be able to fetch packages through Koi.
* Make sure the URL matches the same Koi gateway domain configured as the remote repository URL in Artifactory.

***

## Important notes

### Prevention (blocking downloads)

Koi policies can allow or block packages from being downloaded. However, JFrog Artifactory remote repositories include a built-in caching mechanism, which can affect how “prevention” behaves:

* If a package/version was previously allowed and already downloaded through Artifactory, it may be served from Artifactory’s cache later - even if Koi now marks it as blocked.
* This can happen depending on your Artifactory caching policies (and whether the artifact still exists in cache).

**What this means in practice**

* Koi cannot directly control or purge your Artifactory cache. Koi operates as the remote upstream URL and does not have administrative permissions over your Artifactory instance.
* To ensure prevention is enforced for packages that may already be cached, you should:
* Adjust Artifactory remote repository cache policies appropriately, and/or
* Remove/purge the cached artifact from Artifactory (if you need the block to take effect immediately).

**What Koi can prevent reliably**

* Koi is expected to prevent downloads of packages that are not already present in Artifactory (i.e., packages that would require a fresh fetch via the configured remote URL).

### Remote URL ordering (Koi must be the source of truth)

For Koi to enforce policies consistently, Artifactory must be configured so that Koi is the remote URL used to fetch packages.

* Make sure there are no other upstream/remote URLs configured "before" Koi in any resolution path that could allow packages to bypass Koi.
* Koi should be the sole upstream for the repository unless you intentionally configure additional remotes and fully understand the expected behavior (e.g., fallback behavior could bypass Koi depending on your setup).

**Recommendation**

* Keep the integration simple: one remote → Koi for the repository where you want enforcement.
* If you need complex routing/fallback rules, document and test the expected resolution order to avoid "surprising" results.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov/jfrog-artifactory.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
