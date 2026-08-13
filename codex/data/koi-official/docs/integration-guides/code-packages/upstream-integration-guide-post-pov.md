<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov.md).

# Upstream Integration Guide (Post POV)

Integrating Koi as an upstream registry allows your organization to enforce governance and security policies across all third-party packages **before they reach developer environments or build pipelines**. By routing dependency requests through Koi, every package is evaluated, logged, and governed in accordance with your organization’s policies.

***

### Why Use Koi as an Upstream?

Positioning Koi as the upstream source for package requests enables:

* **Policy Enforcement** - Block, allow, or alert on packages based on risk, source, or metadata using Koi’s granular policy engine
* **Inventory & Visibility** - Maintain a centralized, real-time inventory of all packages entering your environment
* **Audit & Compliance** - Capture detailed logs of every requested package, version, and origin for compliance and incident response

***

### How It Works

1. A developer or system requests a third-party package (e.g., via CLI, CI pipeline, or IDE).
2. The request is routed through an artifact management system configured to proxy Koi.
3. Koi inspects the request:
   * Evaluates it against your policies and Koi's risk engine
   * Logs package metadata for visibility
   * Returns the package if permitted
4. The artifact system caches the package locally for future access.

This model ensures every new dependency is evaluated at the point of entry, with no disruption to existing developer workflows.

***

### Integration Overview

Koi supports upstream integration via any artifact management solution that allows:

* **Remote repositories** (to proxy external sources)
* **Virtual repositories** (to unify remote and local sources under a single endpoint)
* **Custom registry URLs** and optional **authentication headers**

#### Recommended Setup Pattern

1. **Remote Repository** Create a remote repository that points to the Koi upstream registry. This allows your artifact system to fetch packages from Koi, where they will be analyzed and governed before reaching your environment.
2. **Virtual Repository (Optional)** For a seamless developer experience, combine the Koi-backed remote repository with your local/internal repositories under a virtual repository. This allows developers to continue using a single registry endpoint.
3. **Configure Clients** Ensure your package managers (e.g., npm, pip, brew) are configured to use your artifact system’s virtual or remote repository. No direct interaction with Koi is needed on the developer side.

#### Note

It is recommended to configure Koi's upstream registry is the egressing repository to fetch artifacts. For example, with a remote repository it is important to configure Koi's repo at the top of the list to ensure fetching remote artifacts would be handled via Koi.

***

### Supported Platforms

Koi can be integrated as an upstream registry with any system that supports remote or proxy repositories, including:

* **JFrog Artifactory**
* **Sonatype Nexus Repository**
* **Azure Artifacts** (coming soon)
* **GitHub Packages** (coming soon)
* **GitLab Package Registry** (coming soon)

> If your system supports custom or remote registries for package managers like npm, Homebrew, PyPI, Maven, or others - it likely supports Koi integration.

***

### Miscellaneous

Koi provides upstream registry URLs and optional authentication credentials specific to your organization. These details are not included in this guide and should be obtained through your onboarding or support channel.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
