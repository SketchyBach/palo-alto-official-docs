Source: https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov/sonatype-nexus-post-pov.md

# Sonatype Nexus (Post POV)

### Introduction

Integrating Koi as an upstream registry in Sonatype Nexus Repository Manager allows your organization to enforce governance and security policies across all third-party packages before they reach developer environments or build pipelines.&#x20;

By routing package pulls through Koi, every package is evaluated, logged, and governed according to your policies - enabling centralized policy enforcement, real-time package inventory, and detailed audit trails for compliance and incident response.

This guide covers configuring npm or PyPI remote repositories in JFrog Artifactory to route through Koi.

### Configuration Guide

**Prerequisites**

* Access to your Nexus Repository Manager admin console
* Koi tenant provisioned with gateway URLs
* Network connectivity from Nexus to Koi gateway endpoints

**Integration Steps**

1. **Navigate to Repository Settings**
   * Log into Nexus Repository Manager
   * Go to **Settings > Repositories**
2. **Create or Edit Proxy Repository**
   * Click **Create repository** and select proxy type (`npm (proxy)` or `pypi (proxy)`)
   * Or edit an existing proxy repository
3. **Configure Remote Storage URL**

   * Replace the default public registry URL with the Koi gateway URL:

   | Package Type | Default URL                  | Koi Gateway URL                                     |
   | ------------ | ---------------------------- | --------------------------------------------------- |
   | npm          | `https://registry.npmjs.org` | `https://koi-npmjs-<customer>.gateway.koi.security` |
   | PyPI         | `https://pypi.org`           | `https://koi-pypi-<customer>.gateway.koi.security`  |
4. **Save Configuration**
   * Click **Save**
5. **(Optional) Add to Group Repository**
   * If using a group repository for unified access, add the Koi-configured proxy to the group members

***

### Traffic Flow

```
Developer → Nexus Proxy → Koi Gateway → Public Registry
                ↓              ↓
         Local Cache    Policy Check
```

***

### Validation

Test the Koi endpoint is reachable:

```bash
curl https://koi-npmjs-<customer>.gateway.koi.security/koi
```

***

### Known Limitations & Considerations

#### Caching Behavior

Nexus caches packages locally. Components cached **before** Koi integration remain accessible from cache and bypass Koi policy enforcement.

**Mitigations:**

* **Invalidate cache** after integration: **Settings > Repositories > \[Proxy Repository] > Invalidate Cache**
* For complete cache purge, clean up the blob store
* Ensure Koi is the sole upstream (no alternative routes to public registries)


---

---
