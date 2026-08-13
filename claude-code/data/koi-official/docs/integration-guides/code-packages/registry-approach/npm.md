<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/registry-approach/npm.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/registry-approach/npm.md).

# NPM

**Route** - Configure npm's registry to point to the Koi proxy.

**Trust** - Koi serves a globally trusted TLS certificate. No additional trust configuration is needed.

### Before You Begin

We recommend reviewing how your developers' environments are configured before applying registry changes. For example, check whether developers are using project-level `.npmrc` files, an artifact repository (like Artifactory), or tools such as `nvm`, and make sure these are aligned with using the Koi proxy.

The `npm config set registry` command writes to a single configuration file, but npm resolves its registry from multiple sources with a defined precedence order. Settings closer to the project or process level override global ones. The following sections describe common configurations that can interfere.

#### Project-level `.npmrc` files

A `.npmrc` file in the project root (or any ancestor directory) overrides user-level and global registry settings. Check your repositories for project-level `.npmrc` files and update or remove any `registry=` lines that would conflict.

#### Scoped registries

`.npmrc` can define per-scope registries (e.g., `@mycompany:registry=https://...`). Packages under that scope use the scoped registry regardless of the global setting. Review scoped entries and decide whether they should also point to Koi.

#### Artifact repositories (Artifactory, Nexus, etc.)

If your organization uses a centralized artifact repository, the registry may already be pointed there. In that case, configure Koi as the upstream in the repository manager rather than on each endpoint. See the Upstream Integration Guide.

#### Node version managers (`nvm`, `fnm`, `volta`)

Switching Node versions can reset or isolate npm configuration. After configuring the registry, verify the setting persists when switching versions:

```shell
npm config get registry
```

#### Alternative package managers (`yarn`, `pnpm`)

`npm config set` has no effect on Yarn or pnpm. If developers use these tools, the registry must be configured for each tool separately.

#### `NPM_CONFIG_REGISTRY` environment variable

This environment variable overrides config file settings. Check shell profiles, `.env` files, and tooling wrappers for any existing value.

#### Recommendation

* **If your developers use a standardized dev container or dev environment** (e.g., devcontainers, a shared VM image, or a managed cloud workspace): configure the registry at the environment level using a user-level `~/.npmrc`. This makes the developer environment the enforcement point and avoids having to update every project individually.
* **If developers work on local machines without a standardized environment**: configure the registry at the project level by adding a `.npmrc` file to each repository, so that the Koi proxy is applied regardless of the developer's local setup.

***

### Configure the Registry

Use the `npm` CLI to set the registry in the `npmrc` configuration file.

1. Open Terminal / PowerShell - according to your operating system.
2. Execute the following command.

```shell
# user-level (~/.npmrc)
npm config set registry https://koi-npmjs-<customer_subdomain>.gateway.koi.security

# project-level (requires running from the project root)
npm config set registry https://koi-npmjs-<customer_subdomain>.gateway.koi.security --location=project

# system/global (requires admin)
npm config set registry https://koi-npmjs-<customer_subdomain>.gateway.koi.security --global
```

> **Note**: The actual proxy details are listed in the deployment portal.

### Update Lock Files

Existing `package-lock.json` files may contain hardcoded references to the previous registry. To ensure the Koi proxy URL is written into lock files, run:

```shell
npm config set replace-registry-host always
```

After setting this, run `npm install` in each project to regenerate the lock file with the updated registry URLs.

### Trust

No additional trust configuration is needed. The Koi proxy serves a certificate signed by a globally recognized Root CA that is trusted by NPM's built-in certificate store.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/registry-approach/npm.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
