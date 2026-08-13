<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/registry-approach/python.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/registry-approach/python.md).

# Python

**Route** - Configure pip's index to point to the Koi proxy.

**Trust** - Koi serves a globally trusted TLS certificate. No additional trust configuration is needed.

### Before You Begin

We recommend reviewing how your developers' environments are configured before applying index changes. For example, check whether developers are using virtual environments, project-level `pip.conf` files, or tools such as `pyenv`, and make sure these are aligned with using the Koi proxy.

The `pip config set` command writes to a single configuration file, but pip resolves its index URL from multiple sources with a defined precedence order. Settings closer to the project or process level override global ones. The following sections describe common configurations that can interfere.

#### Virtual environments

pip configuration inside a virtual environment (`venv`, `virtualenv`) or conda environment may differ from the global config. If developers work inside virtual environments, verify the registry setting is applied within those environments as well.

#### Project-level configuration (`pip.conf`, `pyproject.toml`)

Projects can pin their own index URL in a local `pip.conf` (or `pip.ini` on Windows) placed in the project directory, or in `pyproject.toml`. These override the user-level and global pip config. Check your repositories for project-level index settings.

#### Python version managers (`pyenv`, `conda`)

Each managed Python installation has its own pip and its own configuration. After configuring the registry, verify the setting is active under each Python version your developers use:

```shell
pip config list
```

#### Alternative package managers (`poetry`, `pipenv`, `uv`, `pdm`)

`pip config set` does not affect other Python package managers. If developers use Poetry, Pipenv, uv, pdm, or similar tools, the registry must be configured for each tool separately.

#### `--index-url` / `--extra-index-url` in `requirements.txt`

These directives at the top of a `requirements.txt` file override pip's configured index at install time. Check your repositories for requirements files that set an index URL directly.

#### `PIP_EXTRA_INDEX_URL` environment variable

Even if `PIP_INDEX_URL` points to Koi, the `PIP_EXTRA_INDEX_URL` environment variable adds a secondary index. Packages can be fetched from that secondary index (e.g., public PyPI) without going through Koi. Check for and remove any conflicting values.

#### `PIP_INDEX_URL` environment variable

If `PIP_INDEX_URL` is set in a shell profile or elsewhere, it takes precedence over the `pip config` setting. Check shell profiles (`.bashrc`, `.zshrc`, `.profile`) and environment configuration for any existing value.

#### Artifact repositories (Artifactory, Nexus, etc.)

If your organization uses a centralized artifact repository, the index may already be pointed there. In that case, configure Koi as the upstream in the repository manager rather than on each endpoint. See the Upstream Integration Guide.

#### Recommendation

* **If your developers use a standardized dev container or dev environment** (e.g., devcontainers, a shared VM image, or a managed cloud workspace): configure the index at the environment level using `pip config set global.index-url` (user-level). This makes the developer environment the enforcement point and avoids having to update every project individually.
* **If developers work on local machines without a standardized environment**: configure the index at the project level by setting `index-url` in a project-level `pip.conf` or in `requirements.txt`, so that the Koi proxy is applied regardless of the developer's local setup.

***

### Configure the Index

#### Config File (recommended)

1. Open Terminal / PowerShell - according to your operating system.
2. Execute the following command.

```shell
pip config set global.index-url "https://koi-pypi-<customer_subdomain>.gateway.koi.security/simple"
# verify
pip config list
```

#### Environment Variables

Alternatively, set the index URL via environment variables.

```shell
# Linux / macOS (bash)
export PIP_INDEX_URL="https://koi-pypi-<customer_subdomain>.gateway.koi.security/simple"

# Windows PowerShell (session)
$env:PIP_INDEX_URL = "https://koi-pypi-<customer_subdomain>.gateway.koi.security/simple"

# Windows machine-wide (admin)
setx PIP_INDEX_URL "https://koi-pypi-<customer_subdomain>.gateway.koi.security/simple" /M
```

> **Note**: The actual proxy details are listed in the deployment portal.

### Trust

No additional trust configuration is needed. The Koi proxy serves a certificate signed by a globally recognized Root CA that is trusted by Python's built-in certificate store.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/registry-approach/python.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
